import argparse
import os
from src.scanner.parameter_finder import find_parameters
from src.scanner.field_detector import detect_input_fields
from src.scanner.payload_tester import test_payloads
from src.utils.encoder import encode_payload
from src.utils.logger import save_results
from src.utils.http_handler import send_request
from src.ui.output_formatter import format_results

def main():
    parser = argparse.ArgumentParser(description="Advanced XSS Scanner")
    parser.add_argument("--url", required=True, help="Target URL for scanning")
    parser.add_argument("--encode", choices=["html", "url", "base64"], help="Encoding type for payloads")
    parser.add_argument("--custom-payloads", help="Path to custom payloads file")
    parser.add_argument("--output", choices=["json", "csv", "log"], default="json", help="Output format for results")
    parser.add_argument("--deep-scan", action="store_true", help="Enable deep scanning to analyze nested parameters and endpoints")

    args = parser.parse_args()

    url = args.url
    encode_type = args.encode
    custom_payloads_path = args.custom_payloads
    output_format = args.output
    deep_scan = args.deep_scan

    # Step 1: Identify parameters in the URL
    print("[+] Finding parameters in the URL...")
    parameters = find_parameters(url, deep_scan=deep_scan)
    print(f"[+] Found parameters: {parameters}")

    # Step 2: Detect user input fields on the target URL
    print("[+] Detecting input fields...")
    input_fields = detect_input_fields(url)
    print(f"[+] Detected input fields: {input_fields}")

    # Step 3: Load payloads
    payloads = []
    if custom_payloads_path and os.path.exists(custom_payloads_path):
        with open(custom_payloads_path, "r") as f:
            payloads = [line.strip() for line in f.readlines()]
    else:
        with open("config/default_payloads.txt", "r") as f:
            payloads = [line.strip() for line in f.readlines()]
    print(f"[+] Loaded {len(payloads)} payloads.")

    # Step 4: Encode payloads if needed
    if encode_type:
        print(f"[+] Encoding payloads using {encode_type} encoding...")
        payloads = [encode_payload(payload, encode_type) for payload in payloads]

    # Step 5: Test payloads on parameters and input fields
    print("[+] Testing payloads...")
    results = test_payloads(url, parameters, input_fields, payloads)

    # Step 6: Format results for readability
    formatted_results = format_results(results)
    print("[+] Scan Results:")
    print(formatted_results)

    # Step 7: Save results
    print(f"[+] Saving results to logs/scan_results.{output_format}...")
    save_results(results, output_format)

    print("[+] Scan completed.")

if __name__ == "__main__":
    main()

