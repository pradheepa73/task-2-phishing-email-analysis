# 🎣 Task 2: Phishing Email Analysis Report

![Security](https://img.shields.io/badge/Domain-Email_Security-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Tool](https://img.shields.io/badge/Tool-Python-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow)

> A professional analysis of a suspicious email sample, identifying phishing indicators, header discrepancies, and social engineering tactics.

---

## 📌 Executive Summary

This report analyzes a simulated phishing email disguised as a PayPal security alert. By comparing it against a legitimate baseline email, multiple phishing indicators were identified, including a spoofed sender domain, urgent threatening language, and a malicious URL. A custom Python script was also written to safely extract headers and URLs without executing malicious payloads.

---

## 🎯 Objective

To identify phishing characteristics in a suspicious email sample, understand email spoofing techniques, and document the social engineering tactics used by attackers.

---

## 🧰 Tools & Methodology

- **Custom Python Script (`analyze_email.py`):** Used to safely parse the raw `.eml` file, extract header discrepancies (`Reply-To`, `Return-Path`), and identify embedded URLs using Regex without clicking them.
- **VS Code:** Used as the isolated environment for analysis and documentation.
- **Manual Inspection:** Comparison of the phishing email against a legitimate baseline email to highlight visual and structural differences.

---

## 🔍 Legitimate Email vs. Phishing Email Comparison

To clearly identify the threat, I compared a legitimate email against the phishing sample.

| Feature | Legitimate Email (Safe) | Phishing Email (Malicious) |
| :--- | :--- | :--- |
| **Sender Address** | `service@paypal.com` (Official domain) | `security@paypal-alerts.com` (Spoofed domain) |
| **Greeting** | Personalized: "Hello John" | Generic: "Dear Customer" |
| **Tone & Language** | Calm, informative, professional | Urgent, threatening: "Within 24 hours" |
| **Link Destination** | Official: `https://www.paypal.com` | Fake: `http://paypal-verify-login.xyz` |
| **Call to Action** | "Log into your account" | "Click here to verify" |
| **Header Authentication** | SPF/DKIM/DMARC: **Pass** | SPF/DKIM/DMARC: **Fail** |

<img width="1920" height="1140" alt="comparison png" src="https://github.com/user-attachments/assets/fcbbb81c-6260-4fbb-a5ed-47c6311ca75c" />

---

## 📊 Indicators of Compromise (IOCs)

| Type | Value | Description |
| :--- | :--- | :--- |
| **Malicious Domain** | `paypal-alerts.com` | Spoofed domain impersonating PayPal. |
| **Malicious URL** | `http://paypal-verify-login.xyz` | Phishing landing page. |
| **Attacker Email** | `hacker@evil-domain.xyz` | Reply-To address used for credential harvesting. |
| **Return-Path** | `bounce@spammer-server.com` | True origin of the email (spoofed). |

---

## 🎯 MITRE ATT&CK Mapping

This phishing attempt maps to the following MITRE ATT&CK techniques:

- **T1566.002 (Phishing: Spearphishing Link):** The email uses a malicious link to harvest credentials.
- **T1585.002 (Establish Accounts: Email Accounts):** The attacker registered a look-alike domain (`paypal-alerts.com`).
- **T1204.001 (User Execution: Malicious Link):** The attacker relies on the user clicking the link.

---

## 🚩 Phishing Indicators Found

Based on the comparison and header analysis, the following red flags were identified:

1. **Spoofed Sender Address:** The email comes from `security@paypal-alerts.com`, which is not an official PayPal domain.
2. **Mismatched Reply-To:** If the user replies, the email goes to a completely different, suspicious address (`hacker@evil-domain.xyz`).
3. **Suspicious Return-Path:** The `Return-Path` header (`bounce@spammer-server.com`) reveals the true origin of the email, which does not match the "From" address.
4. **Urgent or Threatening Language:** The email uses phrases like "within 24 hours" and "permanently suspended" to induce panic.
5. **Mismatched/Malicious URL:** The link text says "Click here", but the real destination is `http://paypal-verify-login.xyz`. It uses HTTP (unencrypted) and a non-official domain.
6. **Generic Greeting:** The email starts with "Dear Customer" instead of the recipient's actual name, indicating a mass phishing campaign.

---

## 🧠 Social Engineering Tactics Used

| Tactic | Evidence in Email |
| :--- | :--- |
| **Authority** | Impersonating a trusted brand (PayPal). |
| **Urgency** | "Verify within 24 hours" |
| **Fear/Threat** | "Account permanently suspended" |
| **Pretexting** | "We noticed suspicious activity on your account." |

---

## 🎤 Interview Questions & Answers

### 1. What is phishing?
Phishing is a social engineering attack where attackers impersonate a trusted entity (bank, company, colleague) to trick victims into revealing sensitive information (passwords, credit cards) or installing malware.

### 2. How to identify a phishing email?
Check the sender's full email address (not just the display name), look for urgency or threats, hover over links to see the real destination, check for generic greetings, poor grammar, and unexpected attachments. Verify via a separate channel if unsure.

### 3. What is email spoofing?
Email spoofing is the creation of an email message with a forged sender address. Attackers make it appear as though the email came from someone else (e.g., `ceo@company.com`) to gain trust.

### 4. Why are phishing emails dangerous?
They can lead to credential theft, financial loss, ransomware infection, data breaches, and lateral movement within a corporate network. They bypass technical controls by targeting the human element.

### 5. How can you verify the sender's authenticity?
Check the full email headers (`Return-Path`, `Received`), look at SPF/DKIM/DMARC results, verify the domain name spelling, and call the person/company directly using a known phone number (not one provided in the email).

### 6. What tools can analyze email headers?
MXToolbox, Google Admin Toolbox (Messageheader), Microsoft Message Header Analyzer, and Mailheader.org.

### 7. What actions should be taken on suspected phishing emails?
Do not click any links or open attachments. Report it to your IT/security team. Delete it. If you clicked, change your passwords immediately and run a malware scan.

### 8. How do attackers use social engineering in phishing?
They exploit human emotions: fear (account suspended), urgency (24 hours), curiosity (unexpected invoice), or authority (CEO request). They create a false sense of trust to bypass logical thinking.

---

## 🛡️ Recommendations

1. **Do not click** any links or download attachments from the suspicious email.
2. **Report** the email to your IT/Security team or the company being impersonated.
3. **Verify** account status by manually typing the official website URL (e.g., `paypal.com`) into a browser.
4. **Enable MFA** (Multi-Factor Authentication) on all accounts to prevent credential theft.

---

## 🧠 Lessons Learned

Through this analysis, I learned that:

1. **Visual inspection is not enough.** Phishing emails can look exactly like real ones. Header analysis (SPF/DKIM/DMARC) and URL hovering are critical.
2. **Social engineering is powerful.** Attackers exploit urgency and fear to bypass logical thinking. Slowing down is the best defense.
3. **Automation helps.** Writing a Python script to parse headers safely reduced the risk of accidentally clicking a malicious link.

---

## 📁 Repository Structure

```text
task-2-phishing-email-analysis/
├── README.md                  # Professional SOC-style report
├── analyze_email.py           # Custom Python parser for safe analysis
├── data/
│   ├── legit_email.txt        # Baseline safe email
│   └── phishing_email.txt     # Malicious phishing sample
└── screenshots/
    └── comparison.png         # VS Code side-by-side screenshot
```

---

## 👤 Author

**Pradheepa M**  
B.Sc. Computer Science with Cybersecurity  
📧 pradheepa378@gmail.com  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pradheepa-m-051728372)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pradheepa73)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:pradheepa378@gmail.com)

---

<div align="center">

**"Empowering The Digital Defenders"**  
*Email Security Analysis — Task 2*

</div>

---

> **Prepared by:** Pradheepa.M  
> **Date:** 2026-10-02  
> **Repository:** https://github.com/pradheepa73/task-2-phishing-email-analysis
```
