# Exploitation Report

Current cybersecurity landscape reveals concerning exploitation activity across multiple vectors, with critical vulnerabilities being actively exploited in enterprise environments. The most significant threats include a command injection vulnerability in Fortinet's FortiSIEM platform (CVE-2025-64155) that came under immediate attack following disclosure, sophisticated malware campaigns targeting Fortune 100 companies, and advanced social engineering attacks using fake browser extensions. Additionally, hardware-level vulnerabilities affecting AMD processors and AI prompt injection flaws in Google services demonstrate the expanding attack surface facing organizations. Threat actors are leveraging increasingly sophisticated techniques including browser crashes for malware delivery, malformed archive structures for evasion, and targeted spear phishing campaigns against government entities.

## Active Exploitation Details

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM platform that allows attackers to execute arbitrary commands on vulnerable systems
- **Impact**: Attackers can gain unauthorized access to security information and event management systems, potentially compromising entire security infrastructure
- **Status**: Disclosed earlier this week and quickly came under attack from various IP addresses
- **CVE ID**: CVE-2025-64155

### Google Gemini Prompt Injection Vulnerability
- **Description**: A security flaw leveraging indirect prompt injection targeting Google Gemini to bypass authorization guardrails and access Google Calendar data
- **Impact**: Unauthorized access to private calendar information through malicious calendar invites
- **Status**: Recently disclosed vulnerability affecting Google's AI assistant integration

### AMD StackWarp Hardware Vulnerability
- **Description**: A hardware vulnerability affecting AMD processors from Zen 1 through Zen 5 generations that breaks SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) protections
- **Impact**: Compromises confidential computing protections and secure virtualization features
- **Status**: Disclosed by CISPA researchers, affects multiple generations of AMD CPUs

### StealC Malware Panel Cross-Site Scripting Vulnerability
- **Description**: An XSS vulnerability in the web-based control panel used by StealC information stealer operators
- **Impact**: Allows researchers and potentially other threat actors to gather intelligence on malware operations
- **Status**: Actively exploited vulnerability in cybercriminal infrastructure

## Affected Systems and Products

- **Fortinet FortiSIEM**: Security information and event management platform under active exploitation
- **Google Gemini**: AI assistant service vulnerable to prompt injection attacks affecting calendar data access
- **AMD Zen 1-5 CPUs**: Hardware-level vulnerability affecting confidential computing features
- **Google Chrome**: Multiple malicious extensions targeting enterprise platforms and ad-blocking functionality
- **Microsoft Windows**: Out-of-band updates required to fix shutdown and Cloud PC functionality issues
- **U.S. Supreme Court Systems**: Electronic filing system breached and compromised
- **AmeriCorps and Department of Veterans Affairs**: Federal agency systems compromised in multi-target attack

## Attack Vectors and Techniques

- **ClickFix Browser Attacks**: Malicious Chrome extensions deliberately crash browsers to prompt users into downloading malware
- **Malvertising Campaigns**: Fake ad-blocker extensions like NexShield used as initial infection vectors
- **Archive Evasion**: GootLoader malware uses 500-1,000 concatenated ZIP archives to bypass security detection
- **Spear Phishing**: Venezuela-themed campaigns targeting U.S. government and policy entities
- **Enterprise Impersonation**: Malicious extensions masquerading as Workday and NetSuite platforms
- **Ransomware Deployment**: PDFSider malware used by ransomware groups targeting Fortune 100 finance companies

## Threat Actor Activities

- **Russian-aligned Hacktivist Groups**: Continued targeting of UK critical infrastructure and local government organizations
- **Black Basta Ransomware**: Leadership identified with Ukrainian and German law enforcement adding leaders to EU Most Wanted and INTERPOL Red Notice
- **KongTuke Campaign**: Ongoing operation using CrashFix Chrome extension to deliver ModeloRAT malware
- **Access Brokers**: Jordanian national pleaded guilty to selling network access to at least 50 corporate networks
- **State-Sponsored Groups**: Advanced persistent threat actors using LOTUSLITE backdoor for intelligence gathering against U.S. policy entities
- **Ransomware Operators**: Targeting Fortune 100 companies in finance sector with custom malware strains