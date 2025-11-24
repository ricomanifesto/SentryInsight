# Exploitation Report

Critical exploitation activity is currently focused on several high-impact vulnerabilities across enterprise systems. Oracle Identity Manager is experiencing active exploitation through a zero-day vulnerability that enables remote code execution, prompting CISA to add it to the Known Exploited Vulnerabilities catalog. Cox Enterprises disclosed a significant data breach resulting from this Oracle E-Business Suite zero-day exploitation. Additionally, Grafana Enterprise faces a maximum severity vulnerability allowing administrative privilege escalation and user impersonation. WhatsApp's contact-discovery API was exploited to scrape 3.5 billion user accounts, while threat actors continue leveraging browser notifications for fileless phishing campaigns and targeting enterprise infrastructure through supply chain compromises.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager enabling remote code execution
- **Impact**: Attackers can gain complete control over affected systems and access sensitive identity management data
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity flaw in Grafana Enterprise's SCIM implementation allowing privilege escalation and user impersonation
- **Impact**: Attackers can gain administrative privileges or impersonate legitimate users under certain configurations
- **Status**: Patches released, no confirmed active exploitation reported
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Abuse
- **Description**: API vulnerability lacking rate limiting that allowed mass data scraping
- **Impact**: Exposure of 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Exploited by researchers to demonstrate the flaw, patching status unclear

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems vulnerable to zero-day exploitation
- **Oracle E-Business Suite**: Cox Enterprises systems compromised through zero-day exploitation
- **Grafana Enterprise**: Organizations using SCIM configuration vulnerable to privilege escalation
- **WhatsApp Platform**: Contact discovery API affecting billions of user accounts globally
- **Russian IT Infrastructure**: Targeted by APT31 using cloud services for stealthy attacks
- **Salesforce Customers**: Organizations affected through Gainsight third-party application compromise
- **LINE Messaging App**: Asian users vulnerable to message replay and impersonation attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Oracle vulnerabilities for initial access
- **Supply Chain Attacks**: Compromise of third-party vendors like Gainsight to access Salesforce customer data
- **API Abuse**: Rate limiting bypass in WhatsApp's contact discovery API for mass data collection
- **Browser Notification Phishing**: Matrix Push C2 platform leveraging browser notifications for fileless attacks
- **Cloud Service Abuse**: APT31 using legitimate cloud services to mask malicious activities
- **Custom Protocol Exploitation**: LINE messaging app vulnerabilities enabling message replay attacks
- **Insider Threats**: CrowdStrike incident involving employee sharing internal screenshots with hackers

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT infrastructure using cloud services between 2024-2025
- **APT24 (China-nexus)**: Deploying BADAUDIO malware in years-long espionage campaign targeting Taiwan and over 1,000 domains
- **ShinyHunters Group**: Exploiting third-party applications to steal Salesforce customer data through Gainsight compromise
- **Qilin Ransomware Operators**: Using rogue ScreenConnect access and failed infostealer attempts before ransomware deployment
- **Scattered Lapsus$ Hunters**: Continuing activities with insider threat components and social engineering tactics
- **Matrix Push C2 Users**: Deploying browser-based phishing campaigns using notification systems for cross-platform attacks