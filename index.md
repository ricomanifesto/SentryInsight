# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across enterprise systems, with Oracle Identity Manager facing immediate threats and Grafana Enterprise experiencing maximum severity privilege escalation issues. The current threat landscape shows sophisticated attacks targeting identity management systems, enterprise applications, and cloud services, with threat actors leveraging both zero-day flaws and supply chain compromises to gain unauthorized access to sensitive data and systems.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can potentially gain complete control over affected systems and access sensitive identity management data
- **Status**: Actively being exploited in the wild according to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Flaw
- **Description**: Zero-day vulnerability in Oracle E-Business Suite that was exploited to breach Cox Enterprises' network
- **Impact**: Complete network compromise leading to exposure of personal data from company systems
- **Status**: Exploited in attacks against Cox Enterprises, patch status unclear

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity flaw in Grafana Enterprise's SCIM implementation that enables admin impersonation and privilege escalation
- **Impact**: Attackers can treat new users as administrators or escalate privileges within Grafana systems
- **Status**: Patched by Grafana Labs
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Flaw
- **Description**: Rate limiting vulnerability in WhatsApp's contact-discovery API
- **Impact**: Researchers were able to scrape 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Exploited by researchers to demonstrate mass data collection capabilities

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems vulnerable to remote code execution
- **Oracle E-Business Suite**: Enterprise resource planning systems compromised through zero-day exploitation
- **Grafana Enterprise**: Data visualization and monitoring platforms with SCIM configurations at risk
- **WhatsApp API**: Mobile messaging platform's contact discovery functionality
- **LINE Messaging App**: Encrypted messaging application using vulnerable custom protocol
- **Salesforce (via Gainsight)**: Customer relationship management systems accessed through third-party application compromise
- **ScreenConnect**: Remote access software used as entry point for ransomware attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Oracle products and other enterprise systems
- **Supply Chain Attacks**: Compromise of third-party vendors like Gainsight to access Salesforce customer data
- **API Abuse**: Rate limiting bypass techniques to mass-harvest contact information from messaging platforms
- **Browser Notifications**: Matrix Push C2 platform leveraging browser notifications for fileless, cross-platform phishing
- **Rogue Remote Access**: Unauthorized ScreenConnect access leading to ransomware deployment
- **Custom Protocol Exploitation**: Message replay and impersonation attacks against LINE messaging's leaky protocol

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services for command and control
- **APT24 (China-nexus)**: Multi-year espionage campaign against Taiwan using BADAUDIO malware, compromising over 1,000 domains
- **ShinyHunters Group**: Exploiting third-party applications to steal Salesforce customer data through Gainsight compromise
- **Qilin Ransomware Operators**: Leveraging compromised ScreenConnect access for ransomware deployment and data exfiltration
- **Scattered Spider**: Teenagers linked to Transport for London breach causing millions in damages and customer data exposure
- **CrowdStrike Insider**: Internal threat actor sharing system screenshots with external hackers via Telegram