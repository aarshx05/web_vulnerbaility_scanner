Web App Vulnerability Scanner

This repository contains a Web Application Vulnerability Scanner powered by OWASP ZAP, Flask, and AWS S3. It provides a user-friendly interface for scanning websites for security vulnerabilities, generating detailed reports, and storing them in the cloud for easy access.

Features

OWASP ZAP Integration: Uses OWASP ZAP's API to perform spidering, passive, and active scans.

Detailed Reports: Automatically generates reports in PDF, JSON, and CSV formats.

Cloud Storage: Stores reports in AWS S3 for secure, centralized access.

Flask Web Interface: Offers an intuitive UI for scanning, viewing results, and accessing reports.

Custom Filters: Implements custom rendering for vulnerability details using Jinja2 filters.

Table of Contents

Prerequisites

Installation

Usage

Configuration

How It Works

Future Prospects

Contributing

License

Prerequisites

Ensure you have the following installed and configured on your system:

OWASP ZAP

Download and install from https://www.zaproxy.org/download/.

Python 3.8+

AWS CLI (Configured with appropriate credentials)

Boto3 (For AWS S3 interactions)

Flask (For the web interface)

FPDF (For PDF report generation)

Installation

Clone the repository:

git clone https://github.com/yourusername/web-app-vulnerability-scanner.git
cd web-app-vulnerability-scanner

Set up a Python virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure environment variables:
Create a .env file to store sensitive credentials:

ZAP_API_KEY=your_zap_api_key
S3_BUCKET_NAME=your_s3_bucket_name

Start OWASP ZAP:
Ensure ZAP is running on your local machine (http://localhost:8080).

Run the Flask application:

python app.py

Usage

Scanning a Website

Open your browser and navigate to http://127.0.0.1:5000.

Enter the target website URL in the input box and click "Scan."

Monitor the scan progress in the terminal logs.

Once the scan is complete, view the vulnerabilities and download reports in PDF, JSON, or CSV formats.

Viewing Reports

Access the "Existing Reports" section on the homepage.

Click on a report to view or download it.

Example Commands

Run OWASP ZAP in headless mode:

zap.sh -daemon -config api.key=your_zap_api_key

Configuration

Environment Variables:

ZAP_API_KEY: The API key for authenticating with OWASP ZAP.

S3_BUCKET_NAME: The name of the AWS S3 bucket for storing reports.

AWS Credentials:
Ensure the AWS CLI is configured with access to the specified S3 bucket.

aws configure

Custom Filters:
The nl2br filter converts newline characters to <br> tags for rendering vulnerability descriptions.

How It Works

Spidering: The scanner identifies all reachable URLs on the target website.

Passive Scanning: ZAP scans the captured URLs for vulnerabilities without altering the website.

Active Scanning: ZAP performs an in-depth scan to identify critical vulnerabilities.

Report Generation:

Vulnerabilities are compiled into a PDF, JSON, and CSV.

Reports are uploaded to AWS S3 for centralized access.

Cloud Storage: Reports are stored and retrieved from AWS S3 via the boto3 library.

Future Prospects

Enhancements

Multi-Scanner Integration:

Incorporate additional tools like Burp Suite or Nessus for broader vulnerability coverage.

Authentication Support:

Enable scans behind login pages using ZAP authentication scripts.

Dynamic Dashboard:

Implement a real-time dashboard with charts and graphs for vulnerability trends.

User Management:

Add role-based access to the application for multiple users.

Custom Policies:

Allow users to define custom scanning rules and policies.

AI-Powered Features

Risk Analysis:

Use machine learning to classify and prioritize vulnerabilities based on severity and likelihood of exploitation.

Automated Remediation Suggestions:

Generate detailed, context-aware recommendations for fixing vulnerabilities.

Scalability

Distributed Scanning:

Deploy the scanner on a cluster for concurrent scans.

Cloud-Native Deployment:

Containerize the application using Docker and orchestrate with Kubernetes.

Integration with CI/CD:

Embed vulnerability scans into DevOps pipelines for continuous security testing.

Contributing

We welcome contributions from the community! To contribute:

Fork this repository.

Create a feature branch (git checkout -b feature-name).

Commit your changes (git commit -m "Add feature").

Push to the branch (git push origin feature-name).

Open a Pull Request.

