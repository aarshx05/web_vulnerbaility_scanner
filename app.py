from flask import Flask, render_template, request, redirect, url_for, jsonify
from markupsafe import Markup, escape
from scanner import scan_website, parse_alerts
from report_generator import generate_and_upload_reports, list_reports_in_bucket
import time
from urllib.parse import urlparse
import boto3
app = Flask(__name__)

vulnerabilities = []
S3_BUCKET_NAME = "your-s3-bucket-abcd"

# Custom `nl2br` filter
@app.template_filter('nl2br')
def nl2br_filter(value):
    """Convert newlines into <br> tags."""
    if value is None:
        return ''
    return Markup(escape(value).replace('\n', '<br>'))

# Home route
@app.route('/')
def index():
    # Fetch existing reports from the bucket
    existing_reports = list_reports_in_bucket()
    return render_template('index.html', vulnerabilities=vulnerabilities, enumerate=enumerate, existing_reports=existing_reports)

@app.route('/scan', methods=['POST'])
def scan():
    global vulnerabilities
    target_url = request.form.get('target_url')
    if not target_url:
        return jsonify({"error": "Target URL is required!"}), 400

    webname = target_url.replace("http://", "").replace("https://", "").replace("/", "_")
    timestamp = int(time.time())

    # Run the scanner
    raw_alerts = scan_website(target_url)
    vulnerabilities = parse_alerts(raw_alerts)

    # Generate and upload reports
    report_links = generate_and_upload_reports(target_url, vulnerabilities, webname, timestamp)

    # List existing reports
    existing_reports = list_reports_in_bucket()

    return render_template('index.html', vulnerabilities=vulnerabilities, report_links=report_links, existing_reports=existing_reports)


@app.route('/view-report', methods=['GET'])
def view_report():
    """View the selected report."""
    report_name = request.args.get('report_name')
    if not report_name:
        return "No report selected!", 400

    s3_client = boto3.client('s3')
    try:
        report_obj = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=report_name)
        report_content = report_obj['Body'].read().decode('utf-8')

        # Determine file type and parse if JSON/CSV
        if report_name.endswith('.json'):
            vulnerabilities = json.loads(report_content)
        elif report_name.endswith('.csv'):
            report_content = report_content.encode('latin1').decode('utf-8')
            vulnerabilities = list(csv.DictReader(report_content.splitlines()))
        else:
            vulnerabilities = []

        return render_template('index.html', vulnerabilities=vulnerabilities, existing_reports=list_reports_in_bucket())

    except Exception as e:
        return f"Error fetching report: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
