# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited in the wild, with CISA adding CVE-2025-61757, a remote code execution flaw in Oracle Identity Manager, to its Known Exploited Vulnerabilities catalog. Threat actors have successfully breached major enterprises including Cox Enterprises through a zero-day in Oracle E-Business Suite, while sophisticated APT groups continue targeting organizations through various attack vectors. Additional concerning activity includes WhatsApp API exploitation enabling mass data harvesting, new command-and-control platforms leveraging browser notifications for fileless attacks, and Grafana Enterprise vulnerabilities allowing complete administrative privilege escalation.

## Active Exploitation Details

### Oracle Identity Manager Remote Code Execution
- **Description**: Critical security flaw in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on vulnerable systems, potentially gaining complete control over identity management infrastructure
- **Status**: Actively exploited in the wild according to CISA; added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day
- **Description**: Previously unknown vulnerability in Oracle E-Business Suite that was exploited before patches were available
- **Impact**: Enabled threat actors to breach Cox Enterprises network and access personal data of affected individuals
- **Status**: Zero-day exploitation confirmed; Cox Enterprises disclosed successful breach through this vulnerability

### WhatsApp Contact Discovery API Rate Limiting Bypass
- **Description**: Flaw in WhatsApp's contact-discovery API that lacked proper rate limiting controls
- **Impact**: Researchers were able to compile a database of 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Successfully exploited by researchers to demonstrate mass data harvesting capabilities

### Grafana Enterprise SCIM Authentication Bypass
- **Description**: Maximum severity vulnerability in Grafana Enterprise's SCIM (System for Cross-domain Identity Management) implementation
- **Impact**: Allows attackers to treat new users as administrators or escalate privileges, enabling complete administrative access
- **Status**: Patched by Grafana Labs
- **CVE ID**: CVE-2025-41115

## Affected Systems and Products

- **Oracle Identity Manager**: Identity management systems vulnerable to remote code execution
- **Oracle E-Business Suite**: Enterprise resource planning systems affected by zero-day exploitation
- **WhatsApp Platform**: Contact discovery API exposed billions of user phone numbers
- **Grafana Enterprise**: Identity management and privilege escalation vulnerabilities
- **LINE Messaging App**: Custom protocol vulnerabilities enabling message replay and impersonation attacks
- **Salesforce Ecosystem**: Unauthorized data access through Gainsight-linked OAuth activity
- **ScreenConnect**: Used as attack vector in Qilin ransomware operations
- **Windows 11 Systems**: Gaming performance issues from October security updates affecting 24H2 and 25H2 versions

## Attack Vectors and Techniques

- **API Rate Limiting Abuse**: WhatsApp contact discovery exploitation through lack of proper controls
- **Zero-Day Exploitation**: Oracle products targeted before patches were available
- **OAuth Token Abuse**: Salesforce customer data accessed through compromised Gainsight applications
- **Browser Notification Hijacking**: Matrix Push C2 platform using notifications for fileless, cross-platform phishing
- **Remote Access Tool Compromise**: Qilin ransomware operations leveraging rogue ScreenConnect access
- **SCIM Protocol Manipulation**: Grafana Enterprise authentication bypass enabling privilege escalation
- **Custom Protocol Exploitation**: LINE messaging vulnerabilities allowing message replay and impersonation

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services for infrastructure between 2024-2025
- **APT24 (China-nexus)**: Deploying BADAUDIO malware in years-long espionage campaign targeting Taiwan and over 1,000 domains
- **Qilin Ransomware Group**: Executing sophisticated attacks using ScreenConnect compromise and failed infostealer attempts
- **ShinyHunters Group**: Targeting Salesforce customers through third-party application exploitation via Gainsight
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damage
- **Internal Threat Actor**: CrowdStrike insider confirmed sharing internal system screenshots with external hackers via Telegram
- **Matrix Push C2 Operators**: Deploying new command-and-control platform for browser-based phishing campaigns