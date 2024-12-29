from zapv2 import ZAPv2
import time

# ZAP Configuration
ZAP_API_KEY = "jitee64mm839asn91c5ev4ad5k"
ZAP_BASE_URL = "http://localhost:8080"

# Initialize ZAP API client
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={"http": ZAP_BASE_URL, "https": ZAP_BASE_URL})


def spider_website(base_url):
    print(f"[+] Starting spidering for {base_url}...")
    spider_id = zap.spider.scan(base_url)
    time.sleep(2)

    while int(zap.spider.status(spider_id)) < 100:
        print(f"Spider progress: {zap.spider.status(spider_id)}%")
        time.sleep(5)

    print("[+] Spidering complete.")
    print(f"Discovered URLs: {zap.spider.results(spider_id)}")


def scan_website(base_url):
    # Open the target URL in ZAP
    spider_website(base_url)
    time.sleep(2)  # Wait for spider results to be processed

    # Start passive scan
    print("[+] Starting passive scan...")
    while int(zap.pscan.records_to_scan) > 0:
        print(f"Passive scan progress: {zap.pscan.records_to_scan} records left")
        time.sleep(2)

    # Start active scan
    print("[+] Starting active scan...")
    scan_id = zap.ascan.scan(base_url)
    while int(zap.ascan.status(scan_id)) < 100:
        print(f"Active scan progress: {zap.ascan.status(scan_id)}%")
        time.sleep(5)

    # Fetch and display results
    print("[+] Scan complete. Fetching results...")
    alerts = zap.core.alerts(baseurl=base_url)
    return alerts


def parse_alerts(alerts):
    print(f"[+] Found {len(alerts)} vulnerabilities:\n")
    vulnerabilities = []
    for alert in alerts:
        vulnerabilities.append({
            "URL": alert.get("url"),
            "Vulnerability": alert.get("alert"),
            "Description": alert.get("description"),
            "Risk": alert.get("risk"),
            "Solution": alert.get("solution"),
        })
    return vulnerabilities
