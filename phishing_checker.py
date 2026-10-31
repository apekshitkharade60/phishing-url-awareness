import re
from urllib.parse import urlparse

def inspect_url(raw_url):
    """CHECK VISIBLE URL TEXT FOR SELECTED WARNING SIGNS"""
    url=raw_url.strip()
    findings=[]

    if not url:
        return["NO URL ENTERED."]
    candidate = url if "://" in url else "http://" + url
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()
    if not host:
        return["COULDNOT IDENTIFY A HOSTNAME."]
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url)>100:
        findings.append("UNUSUALLY LONG URL(OVER 100 CHARACTERS).")
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")
    if not findings:
        findings.append("No listed warning signs found. THIS DOESNOT PROVE SAFETY.")
    return findings
INFO_MESSAGES = ("No URL entered.", "Could not identify a hostname.", "No listed warning signs found.", "This text is not a valid URL format.")


def has_warnings(findings):
    return not any(findings[0].startswith(info) for info in INFO_MESSAGES)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break
        print("\nResult:")
        findings = inspect_url(raw_url)
        for item in findings:
            print("- " + item)
        if has_warnings(findings):
            print("\nREVIEW CAREFULLY: " + str(len(findings)) + " warning sign(s) found.")
        print("Never enter passwords from unexpected links.")

if __name__ == "__main__":
    main()