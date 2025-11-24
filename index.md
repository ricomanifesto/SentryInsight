# Exploitation Report

Critical exploitation activity continues to target enterprise systems with multiple zero-day vulnerabilities being actively exploited in the wild. Most concerning is the active exploitation of a critical Oracle Identity Manager zero-day vulnerability (CVE-2025-61757) that allows remote code execution, prompting CISA to add it to their Known Exploited Vulnerabilities catalog. Additionally, Cox Enterprises suffered a significant data breach after attackers exploited a zero-day flaw in Oracle E-Business Suite. The threat landscape remains dynamic with advanced persistent threat groups like APT31 conducting stealthy cyberattacks against Russian IT infrastructure, while APT24 has deployed new malware called BADAUDIO in long-term espionage campaigns targeting Taiwan and over 1,000 domains. Multiple high-severity vulnerabilities have also been disclosed across enterprise platforms, including a maximum severity SCIM flaw in Grafana Enterprise and API vulnerabilities in WhatsApp that exposed billions of user accounts.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager that enables remote code execution
- **Impact**: Attackers can achieve remote code execution on vulnerable systems, potentially leading to complete system compromise
- **Status**: Actively being exploited in the wild; CISA has added to Known Exploited Vulnerabilities (KEV) catalog
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Zero-day flaw in Oracle E-Business Suite that allowed unauthorized access to corporate networks
- **Impact**: Enabled hackers to breach Cox Enterprises' network and expose personal data of impacted individuals
- **Status**: Exploited in Cox Enterprises breach; patch status unknown

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity vulnerability in Grafana Enterprise's SCIM implementation
- **Impact**: Enables privilege escalation and user impersonation attacks, allowing attackers to treat new users as administrators
- **Status**: Patched by Grafana Labs
- **CVE ID**: CVE-2025-41115

### WhatsApp API Contact Discovery Flaw
- **Description**: Contact-discovery API vulnerability that lacked proper rate limiting controls
- **Impact**: Researchers were able to scrape 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Exploited for data collection; current patch status unclear

## Affected Systems and Products

- **Oracle Identity Manager**: Critical systems requiring immediate patching due to active exploitation
- **Oracle E-Business Suite**: Enterprise installations vulnerable to zero-day exploitation
- **Grafana Enterprise**: SCIM-enabled configurations at risk of privilege escalation attacks
- **WhatsApp API**: Contact discovery functionality exposing user data through rate limiting bypass
- **Russian IT Infrastructure**: Targeted by APT31 cyberattacks using cloud services for stealth operations
- **Taiwanese Organizations**: Over 1,000 domains compromised in APT24's BADAUDIO espionage campaign
- **Salesforce Environments**: Customer data accessed through compromised Gainsight third-party application
- **Transport for London Systems**: Breached by Scattered Spider threat actors causing millions in damages

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities in Oracle products being actively exploited for initial access
- **Cloud Service Abuse**: APT31 leveraging legitimate cloud services to conduct stealthy cyberattacks and evade detection
- **Third-Party Application Compromise**: ShinyHunters group exploiting Gainsight application to access Salesforce customer data
- **API Rate Limiting Bypass**: WhatsApp contact discovery API exploited through lack of proper rate limiting controls
- **Browser Notification Abuse**: Matrix Push C2 platform using browser notifications for fileless, cross-platform phishing attacks
- **Insider Threats**: CrowdStrike detecting insider sharing internal system screenshots with external hackers
- **SCIM Protocol Exploitation**: Grafana Enterprise vulnerable to privilege escalation through SCIM implementation flaws
- **Ransomware Deployment**: Qilin ransomware operators using rogue ScreenConnect access for network infiltration

## Threat Actor Activities

- **APT31**: Chinese advanced persistent threat group conducting stealthy cyberattacks against Russian IT sector using cloud services for operational security
- **APT24**: China-nexus threat actor deploying BADAUDIO malware in years-long espionage campaign targeting Taiwan and over 1,000 domains globally
- **ShinyHunters**: Extortion group exploiting third-party applications like Gainsight to steal Salesforce customer data in repeat attacks
- **Scattered Spider**: Threat actors (including British teenagers) targeting critical infrastructure like Transport for London, causing millions in damages
- **Qilin Ransomware Operators**: Conducting sophisticated attacks using rogue ScreenConnect access, failed infostealer attempts, and targeted ransomware deployment
- **Matrix Push C2 Operators**: Bad actors leveraging browser notifications for fileless, cross-platform phishing attacks and malicious link distribution
- **CrowdStrike Insider Threat**: Internal threat actor sharing sensitive system screenshots with external hackers via Telegram channels