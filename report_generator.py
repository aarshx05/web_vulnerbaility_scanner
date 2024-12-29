import json
import csv
from fpdf import FPDF
import unicodedata
import boto3
import os


# S3 Bucket Name
S3_BUCKET_NAME = "your-s3-bucket-abcd"


def sanitize_text(text):
    """Replace unsupported characters or remove non-ASCII characters."""
    if not isinstance(text, str):
        return str(text)  # Handle non-string values gracefully
    text = unicodedata.normalize('NFKD', text)  # Decompose special characters
    return ''.join(c for c in text if ord(c) < 128)  # Remove non-ASCII characters


def generate_json(vulnerabilities, file_name):
    """Generate JSON file for vulnerabilities."""
    with open(file_name, "w") as json_file:
        json.dump(vulnerabilities, json_file, indent=4)
    return file_name


def generate_csv(vulnerabilities, file_name):
    """Generate CSV file for vulnerabilities."""
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["URL", "Vulnerability", "Description", "Risk", "Solution"])
        writer.writeheader()
        writer.writerows(vulnerabilities)
    return file_name


def upload_to_s3(file_path, file_name):
    """Upload a file to S3 and return its URL."""
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, S3_BUCKET_NAME, file_name)
        return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
    except Exception as e:
        print(f"Error uploading {file_name} to S3: {e}")
        return None


def generate_and_upload_reports(target_url, vulnerabilities, webname, timestamp):
    """Generate reports (PDF, JSON, CSV) and upload to S3."""
    pdf_file = f"vuln_report_{webname}_{timestamp}.pdf"
    json_file = f"vuln_report_{webname}_{timestamp}.json"
    csv_file = f"vuln_report_{webname}_{timestamp}.csv"

    # Generate reports
    generate_json(vulnerabilities, json_file)
    generate_csv(vulnerabilities, csv_file)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Vulnerability Scan Report", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Target URL: {sanitize_text(target_url)}", ln=True, align="L")

    if vulnerabilities:
        pdf.cell(200, 10, txt="Vulnerabilities Found:", ln=True, align="L")
        pdf.set_font("Arial", size=10)
        for idx, vuln in enumerate(vulnerabilities, 1):
            pdf.multi_cell(0, 10, txt=sanitize_text((
                f"{idx}. URL: {vuln['URL']}\n"
                f"   Vulnerability: {vuln['Vulnerability']}\n"
                f"   Description: {vuln['Description']}\n"
                f"   Risk: {vuln['Risk']}\n"
                f"   Solution: {vuln['Solution']}\n"
            )))
    else:
        pdf.cell(200, 10, txt="No vulnerabilities found.", ln=True, align="L")

    pdf.output(pdf_file)

    # Upload to S3
    pdf_url = upload_to_s3(pdf_file, pdf_file)
    json_url = upload_to_s3(json_file, json_file)
    csv_url = upload_to_s3(csv_file, csv_file)

    # Clean up local files
    os.remove(pdf_file)
    os.remove(json_file)
    os.remove(csv_file)

    return {"pdf": pdf_url, "json": json_url, "csv": csv_url}


def list_reports_in_bucket():
    """List all reports in the S3 bucket."""
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
        if 'Contents' in response:
            return [
                {
                    "file_name": obj['Key'],
                    "url": f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{obj['Key']}"
                }
                for obj in response['Contents']
            ]
        else:
            return []
    except Exception as e:
        print(f"Error listing bucket contents: {e}")
        return []
