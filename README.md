"""
# Advanced XSS Scanner

Advanced XSS Scanner is a Python-based tool to identify and exploit XSS vulnerabilities in web applications. 
It automatically detects user input parameters, crafts payloads, encodes them if necessary, and scans for vulnerabilities.

## Features
- Automatic parameter detection in URLs (with optional deep scanning).
- Input field detection on webpages.
- Payload generation and encoding (HTML, URL, Base64).
- Supports custom payloads.
- Saves results in JSON, CSV, or log format.
- Readable formatted output for easy analysis.

## Installation
```bash
git clone https://github.com/your-repo/Advanced_XSS_Scanner.git
cd Advanced_XSS_Scanner
pip install -r requirements.txt
```

## Usage
```bash
python src/main.py --url "http://example.com/search?id=1" --encode "url" --custom-payloads "payloads/custom_payloads.txt"
```

## Options
- `--url`: Target URL.
- `--encode`: Encoding type (`html`, `url`, `base64`).
- `--custom-payloads`: Path to custom payloads file.
- `--output`: Output format (`json`, `csv`, `log`).
- `--deep-scan`: Enable deep scanning for nested parameters and endpoints.

## File Structure
- **src/**: Core functionality.
- **config/**: Default payloads and encoding settings.
- **payloads/**: Custom and encoded payloads.
- **logs/**: Scan results.

## Example
```bash
python src/main.py --url "http://example.com" --deep-scan --output log
```
"""
