# Exploitation Report

Critical exploitation activity is currently focused on several high-impact vulnerabilities across enterprise infrastructure. Oracle Identity Manager is experiencing active zero-day exploitation, prompting emergency warnings from CISA and requiring immediate patching by federal agencies. Concurrently, a maximum severity vulnerability in Grafana Enterprise is enabling admin spoofing and privilege escalation attacks. The exploitation landscape is further complicated by sophisticated threat actor campaigns, including APT31's stealthy attacks on Russian IT infrastructure using cloud services, and APT24's multi-year espionage operations deploying previously unknown malware across Taiwan and over 1,000 domains. Zero-day exploitation of Oracle E-Business Suite has resulted in significant data breaches, while novel attack vectors like browser notification-based phishing are emerging through platforms like Matrix Push C2.

## Active Exploitation Details

### Oracle Identity Manager Remote Code Execution Vulnerability
- **Description**: A critical zero-day vulnerability in Oracle Identity Manager that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on vulnerable systems, potentially leading to complete system compromise
- **Status**: Actively exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog with mandatory patching deadline for federal agencies
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: A zero-day flaw in Oracle E-Business Suite that was exploited to breach Cox Enterprises' network
- **Impact**: Unauthorized access to corporate networks and exposure of personal data belonging to affected individuals
- **Status**: Previously unknown vulnerability that was exploited before patches were available

### Grafana Enterprise SCIM Vulnerability
- **Description**: A maximum severity flaw in Grafana's SCIM (System for Cross-domain Identity Management) implementation
- **Impact**: Enables privilege escalation and user impersonation, allowing attackers to treat new users as administrators
- **Status**: Patches available; affects Grafana Enterprise configurations
- **CVE ID**: CVE-2025-41115

## Affected Systems and Products

- **Oracle Identity Manager**: Federal agencies and organizations running Oracle identity management solutions
- **Oracle E-Business Suite**: Enterprise resource planning systems, specifically affecting Cox Enterprises
- **Grafana Enterprise**: Organizations using Grafana's enterprise monitoring and visualization platform
- **Russian IT Infrastructure**: Companies in Russia's information technology sector targeted by APT31
- **Taiwan Organizations**: Government and private sector entities affected by APT24's multi-year campaign
- **Salesforce Instances**: Customers affected through compromised Gainsight third-party application
- **WhatsApp Platform**: 3.5 billion mobile phone numbers exposed through API abuse
- **LINE Messaging App**: Asian users vulnerable to custom protocol exploitation

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging previously unknown vulnerabilities in Oracle products before patches are available
- **Cloud Service Abuse**: APT31 using legitimate cloud services to mask malicious activities and evade detection
- **Third-Party Application Compromise**: ShinyHunters group exploiting Gainsight to access Salesforce customer data
- **Browser Notification Phishing**: Matrix Push C2 platform using browser notifications for fileless, cross-platform attacks
- **API Rate Limiting Bypass**: Exploitation of WhatsApp's contact-discovery API to scrape billions of phone numbers
- **Custom Protocol Exploitation**: Abuse of LINE messaging app's leaky protocol for message replays and impersonation
- **Privilege Escalation**: SCIM implementation flaws allowing unauthorized administrative access
- **Ransomware Deployment**: Qilin ransomware attacks using compromised ScreenConnect for initial access

## Threat Actor Activities

- **APT31**: China-linked group conducting stealthy cyberattacks against Russian IT sector between 2024-2025, utilizing cloud services for operational security
- **APT24**: China-nexus threat actor deploying BADAUDIO malware in nearly three-year espionage campaign targeting Taiwan and over 1,000 domains worldwide
- **ShinyHunters**: Extortion group repeatedly targeting Salesforce customers through third-party application compromises
- **Scattered Spider**: British teenagers involved in Transport for London breach causing millions in damage and customer data exposure
- **Qilin Ransomware Operators**: Sophisticated attackers using ScreenConnect access and failed infostealer attempts before deploying ransomware
- **CrowdStrike Insider Threat**: Internal employee feeding sensitive information to external hackers and Scattered Lapsus$ Hunters group