# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, with CISA warning of active attacks targeting Oracle Identity Manager through CVE-2025-61757, a remote code execution flaw. Meanwhile, Cox Enterprises suffered a significant data breach after attackers exploited a zero-day vulnerability in Oracle E-Business Suite. Additional high-severity vulnerabilities have been identified in Grafana Enterprise products, including a maximum CVSS 10.0 SCIM flaw enabling privilege escalation. Threat actors continue to leverage sophisticated attack vectors, with APT31 conducting stealthy operations against Russian IT infrastructure, APT24 deploying custom malware in multi-year espionage campaigns, and various groups exploiting third-party integrations like Gainsight to compromise Salesforce customer data.

## Active Exploitation Details

### Oracle Identity Manager RCE Vulnerability
- **Description**: A critical remote code execution vulnerability in Oracle Identity Manager that allows attackers to execute arbitrary code on affected systems
- **Impact**: Attackers can gain unauthorized access to systems, potentially leading to complete system compromise and data exfiltration
- **Status**: Currently being actively exploited in the wild; CISA has added it to the Known Exploited Vulnerabilities catalog and mandated federal agencies to patch by a specific deadline
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day
- **Description**: A zero-day vulnerability in Oracle E-Business Suite that was exploited to breach Cox Enterprises' network infrastructure
- **Impact**: Complete network compromise leading to unauthorized access to personal data of impacted individuals
- **Status**: Exploited in active breach; zero-day status indicates no patch was available at the time of exploitation

### Grafana Enterprise SCIM Vulnerability
- **Description**: A maximum severity SCIM (System for Cross-domain Identity Management) implementation flaw in Grafana Enterprise
- **Impact**: Enables privilege escalation and user impersonation under certain configurations, allowing attackers to gain administrative access
- **Status**: Patched by Grafana Labs with security updates released
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Flaw
- **Description**: A rate-limiting bypass vulnerability in WhatsApp's contact-discovery API that allowed unauthorized data scraping
- **Impact**: Enabled compilation of 3.5 billion WhatsApp mobile phone numbers and associated personal information
- **Status**: Exploited by researchers to demonstrate the vulnerability's impact

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems requiring immediate patching
- **Oracle E-Business Suite**: Enterprise resource planning systems vulnerable to zero-day exploitation
- **Grafana Enterprise**: Data visualization and monitoring platforms with SCIM configurations
- **WhatsApp API**: Mobile messaging platform's contact discovery functionality
- **Salesforce Platform**: Customer relationship management systems accessed through Gainsight third-party applications
- **LINE Messaging App**: Encrypted messaging application using custom protocol with security weaknesses

## Attack Vectors and Techniques

- **Remote Code Execution**: Direct exploitation of Oracle Identity Manager flaws for system compromise
- **Zero-Day Exploitation**: Leveraging unknown vulnerabilities in Oracle E-Business Suite before patches are available
- **API Abuse**: Rate-limiting bypass techniques to scrape massive datasets from WhatsApp's contact discovery service
- **Third-Party Integration Abuse**: Exploiting OAuth connections between Salesforce and Gainsight applications for unauthorized data access
- **Cloud Service Leverage**: Using legitimate cloud infrastructure to conduct stealthy cyber operations while evading detection
- **Browser Notification Hijacking**: Matrix Push C2 platform utilizing browser notifications for fileless, cross-platform phishing campaigns
- **Custom Protocol Exploitation**: Targeting weaknesses in LINE's proprietary messaging protocol for message replay and impersonation attacks

## Threat Actor Activities

- **APT31**: China-linked advanced persistent threat group conducting sophisticated cyber operations against Russian IT sector infrastructure between 2024 and 2025, utilizing cloud services for stealth
- **APT24**: China-nexus threat actor deploying custom BADAUDIO malware in multi-year espionage campaigns targeting Taiwan and over 1,000 domains for persistent network access
- **ShinyHunters**: Extortion group affiliated actors exploiting third-party Gainsight applications to steal Salesforce customer data in repeat attack patterns
- **Qilin Ransomware**: Operators conducting targeted attacks using rogue ScreenConnect access and infostealer techniques before deploying ransomware payloads
- **Matrix Push C2 Operators**: Cybercriminals leveraging browser notifications as attack vectors for distributing malicious links through cross-platform phishing campaigns
- **Scattered Lapsus$ Hunters**: Threat group involved in data theft operations, including recent activity involving CrowdStrike insider information sharing