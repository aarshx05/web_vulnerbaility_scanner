# Web App Vulnerability Scanner

## Overview

The **Web App Vulnerability Scanner** is a robust application that integrates OWASP ZAP with a user-friendly web interface built using Flask. It enables users to scan websites for vulnerabilities, generate detailed reports (PDF, JSON, and CSV), and store them securely in AWS S3 for easy access and review.

---

## Features

- **OWASP ZAP Integration**: Automated scanning with progress tracking for spidering, passive, and active scans.
- **Report Generation**: Creates reports in PDF, JSON, and CSV formats.
- **AWS S3 Storage**: Uploads and retrieves reports securely.
- **Web Interface**: User-friendly Flask application with real-time feedback and report viewing.
- **Customizable Templates**: Easily extendable and modifiable templates for new use cases.
- **Security Measures**: Includes features like escaping user input and using API keys for secure operations.

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Installation](#installation)  
3. [Usage](#usage)  
4. [How It Works](#how-it-works)  
5. [Future Prospects](#future-prospects)  
6. [Contributing](#contributing)  
7. [License](#license)

---

## Prerequisites

1. **Python** (3.8 or above)  
2. **OWASP ZAP** installed and running locally or on a remote server.  
3. **AWS Account** with an S3 bucket set up.  
4. API keys for OWASP ZAP and AWS configured.  
5. Recommended: Virtual environment for Python dependencies.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web-app-vulnerability-scanner.git
   cd web-app-vulnerability-scanner
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the root directory:
   ```
   ZAP_API_KEY=your_owasp_zap_api_key
   S3_BUCKET_NAME=your_s3_bucket_name
   AWS_ACCESS_KEY_ID=your_aws_access_key_id
   AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
   ```

5. Start the Flask application:
   ```bash
   flask run
   ```

---

## Usage

### Running the Scanner

1. Open the application in your browser at `http://127.0.0.1:5000/`.
2. Enter the target URL in the input field and start the scan.
3. Monitor scan progress in real time.
4. View vulnerabilities on the results page.
5. Download reports in your preferred format (PDF, JSON, CSV).

### Viewing Reports

- The home page lists all existing reports stored in the S3 bucket.
- Select a report to view its detailed contents.

### API Endpoints

- **Scan a URL**: `/scan` (POST)  
  Payload:  
  ```json
  {
      "target_url": "http://example.com"
  }
  ```

- **List Reports**: `/view-report` (GET)  
  Parameters:  
  ```
  report_name=<report_file_name>
  ```

---

## How It Works

1. **Spidering**:
   - Crawls the target website to discover URLs.
2. **Scanning**:
   - Performs passive and active vulnerability scans using OWASP ZAP.
3. **Reporting**:
   - Converts scan results into PDF, JSON, and CSV formats.
4. **Storage**:
   - Uploads reports to AWS S3 for secure storage.
5. **Visualization**:
   - Displays vulnerabilities and provides download links for reports via the web interface.

---

## Future Prospects

### 1. **Integration with More Tools**
   - Add support for tools like Burp Suite, Nessus, or Nmap for comprehensive security analysis.

### 2. **Enhanced Reporting**
   - Provide interactive dashboards with charts and graphs for easier vulnerability management.

### 3. **Automated Scanning**
   - Set up periodic scans for monitoring websites and send alerts for newly discovered vulnerabilities.

### 4. **Role-Based Access**
   - Implement user authentication and role-based access to secure sensitive operations.

### 5. **Threat Intelligence Integration**
   - Enrich reports with contextual threat intelligence from external sources.

### 6. **Containerization**
   - Package the application using Docker for easy deployment across environments.

### 7. **Multi-Cloud Support**
   - Extend storage options to Google Cloud Storage or Azure Blob Storage.

---

## Contributing

We welcome contributions from the community! Here's how you can get started:

1. Fork the repository.  
2. Create a new branch for your feature/bug fix.  
3. Commit your changes with descriptive messages.  
4. Push your changes to your fork.  
5. Open a pull request and describe your changes in detail.

---

## Contact

For any queries or feedback, feel free to reach out via email at `aarsh.chaurasia.201007@gmail.com` or open an issue in the GitHub repository.  
