# Formats output results

def format_results(results):
    formatted = "\n".join([f"Parameter: {r.get('parameter', '-')}, Field: {r.get('field', '-')}, Payload: {r['payload']}, URL: {r['url']}" for r in results])
    return formatted
