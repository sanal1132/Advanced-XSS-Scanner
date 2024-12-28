import json
import csv

def save_results(results, output_format):
    if output_format == "json":
        with open("logs/scan_results.json", "w") as f:
            json.dump(results, f, indent=4)
    elif output_format == "csv":
        with open("logs/scan_results.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["parameter", "payload", "url"])
            writer.writeheader()
            writer.writerows(results)
    elif output_format == "log":
        with open("logs/scan_results.log", "w") as f:
            for result in results:
                f.write(f"Parameter: {result.get('parameter')}, Payload: {result.get('payload')}, URL: {result.get('url')}\n")
