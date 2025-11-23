# Exploitation Report

Critical exploitation activity continues to target enterprise systems with multiple high-severity vulnerabilities being actively exploited. The most significant threat involves a zero-day vulnerability in Oracle Identity Manager (CVE-2025-61757) that CISA has confirmed is under active exploitation, enabling remote code execution. Additional concerning activity includes a zero-day exploit targeting Oracle E-Business Suite that led to a major data breach at Cox Enterprises, and a maximum severity vulnerability in Grafana Enterprise (CVE-2025-41115) that allows privilege escalation and administrator impersonation. Threat actors are also leveraging novel techniques including browser notification-based command and control platforms and sophisticated supply chain attacks targeting major organizations.

## Active Exploitation Details

### Oracle Identity Manager Remote Code Execution Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle Identity Manager allowing remote code execution
- **Impact**: Attackers can gain complete control over affected systems and potentially access sensitive identity management data
- **Status**: Currently being exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Zero-day flaw in Oracle E-Business Suite that was exploited to breach Cox Enterprises network
- **Impact**: Data breach exposing personal information of impacted individuals; complete network compromise
- **Status**: Exploited in active breach; led to significant data exposure at major enterprise

### Grafana Enterprise Privilege Escalation Vulnerability
- **Description**: Maximum severity SCIM (System for Cross-domain Identity Management) flaw enabling user impersonation and privilege escalation
- **Impact**: Attackers can treat new users as administrators or escalate existing privileges to gain administrative access
- **Status**: Patched by Grafana Labs with security updates
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Vulnerability
- **Description**: Rate limiting flaw in WhatsApp's contact-discovery API allowing mass data scraping
- **Impact**: Researchers compiled database of 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Vulnerability exploited by researchers to demonstrate mass data collection capabilities

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems vulnerable to remote code execution
- **Oracle E-Business Suite**: Enterprise resource planning systems targeted in zero-day attacks
- **Grafana Enterprise**: Data visualization and monitoring platforms with SCIM configurations
- **WhatsApp API**: Mobile messaging platform's contact discovery functionality
- **Salesforce Customer Data**: Third-party Gainsight application providing unauthorized access to Salesforce environments
- **Russian IT Infrastructure**: Systems targeted by APT31 using cloud services for stealth operations
- **Transport for London Systems**: Critical transportation infrastructure compromised by Scattered Spider group

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in enterprise systems for initial access
- **Supply Chain Compromise**: Attacks through third-party vendors and applications to access primary targets
- **Browser Notification C2**: Matrix Push C2 platform using browser notifications for fileless, cross-platform phishing
- **Cloud Service Abuse**: APT31 leveraging legitimate cloud services to mask malicious activities
- **API Rate Limiting Bypass**: Exploitation of insufficient rate controls to enable mass data collection
- **SCIM Protocol Abuse**: Manipulation of identity management protocols for privilege escalation
- **Remote Access Tool Deployment**: Use of ScreenConnect and custom malware like BADAUDIO for persistent access

## Threat Actor Activities

- **APT31**: Chinese-linked group conducting stealthy cyberattacks against Russian IT sector using cloud services between 2024-2025
- **APT24**: China-nexus actor deploying BADAUDIO malware in years-long espionage campaign targeting Taiwan and over 1,000 domains
- **ShinyHunters**: Extortion group exploiting third-party applications to steal Salesforce customer data through Gainsight compromise
- **Scattered Spider**: Group conducting ransomware operations including breach of Transport for London causing millions in damages
- **Qilin Ransomware**: Operators using rogue ScreenConnect access and failed infostealer attempts before ransomware deployment
- **Matrix Push C2 Operators**: Bad actors leveraging browser notifications for cross-platform phishing and malware distribution