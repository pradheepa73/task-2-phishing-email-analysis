import email
import re
from email import policy

def analyze_email(file_path):
    print("="*50)
    print("PHISHING EMAIL ANALYSIS TOOL")
    print("="*50)
    with open(file_path, 'r') as f:
        msg = email.message_from_file(f, policy=policy.default)
    print("\n[+] HEADER ANALYSIS:")
    print(f"    From:        {msg['From']}")
    print(f"    Reply-To:    {msg['Reply-To']}")
    print(f"    Return-Path: {msg['Return-Path']}")
    print(f"    Subject:     {msg['Subject']}")
    print("\n[+] EXTRACTED URLs (DO NOT CLICK):")
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(errors='ignore')
                break
    else:
        body = msg.get_payload(decode=True).decode(errors='ignore')
    urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', body)
    if urls:
        for url in urls:
            print(f"    [!] {url}")
    else:
        print("    No URLs found.")
    print("\n" + "="*50)
    print("ANALYSIS COMPLETE.")
    print("="*50)

if __name__ == "__main__":
    analyze_email("phishing_sample.eml")