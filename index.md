# Exploitation Report

Critical exploitation activity has surged with multiple zero-day vulnerabilities being actively exploited in the wild. The most severe threats include CVE-2025-61757, an Oracle Identity Manager remote code execution flaw that CISA has confirmed is under active exploitation, and CVE-2025-41115, a maximum severity vulnerability in Grafana Enterprise enabling administrator privilege escalation. Additionally, Cox Enterprises suffered a major data breach through exploitation of an unnamed Oracle E-Business Suite zero-day vulnerability. These incidents highlight the growing trend of attackers targeting enterprise infrastructure and identity management systems, while sophisticated threat actors like APT24 and APT31 continue launching multi-year espionage campaigns using custom malware and cloud services.

## Active Exploitation Details

### Oracle Identity Manager RCE Vulnerability
- **Description**: Critical remote code execution vulnerability affecting Oracle Identity Manager systems
- **Impact**: Allows attackers to execute arbitrary code remotely, potentially leading to complete system compromise
- **Status**: Currently being actively exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Oracle E-Business Suite Zero-Day
- **Description**: Unspecified zero-day vulnerability in Oracle E-Business Suite that enabled unauthorized access to Cox Enterprises systems
- **Impact**: Led to major data breach exposing personal information of impacted individuals
- **Status**: Exploited in attacks against Cox Enterprises, specific patch status unclear

### Grafana Enterprise Admin Spoofing Vulnerability
- **Description**: Maximum severity vulnerability enabling user impersonation and privilege escalation in Grafana Enterprise
- **Impact**: Attackers can treat new users as administrators or escalate existing privileges
- **Status**: Patched by Grafana Labs with security updates released
- **CVE ID**: CVE-2025-41115

### WhatsApp Contact Discovery API Flaw
- **Description**: Rate limiting vulnerability in WhatsApp's contact-discovery API allowing mass data scraping
- **Impact**: Researchers compiled list of 3.5 billion WhatsApp phone numbers and associated personal information
- **Status**: Exploitation demonstrated by researchers, current patch status not specified

### Ray Framework Vulnerability
- **Description**: Two-year-old security flaw in Ray open-source AI framework being exploited by ShadowRay 2.0 botnet
- **Impact**: Attackers convert infected clusters with NVIDIA GPUs into cryptocurrency mining operations
- **Status**: Actively exploited despite age of vulnerability, many systems remain unpatched

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems vulnerable to remote code execution
- **Oracle E-Business Suite**: Business applications suite affected by zero-day vulnerability
- **Grafana Enterprise**: Data visualization and monitoring platform with admin spoofing vulnerability
- **WhatsApp API**: Contact discovery service vulnerable to rate limiting bypass
- **Ray AI Framework**: Open-source artificial intelligence framework clusters with GPU resources
- **Android Devices**: Targeted by Sturnus banking trojan and Tsundere botnet malware
- **Windows Systems**: Affected by gaming performance issues from October security updates and targeted by various malware campaigns

## Attack Vectors and Techniques

- **API Rate Limiting Bypass**: Exploitation of insufficient rate limiting in WhatsApp's contact discovery API for mass data harvesting
- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Oracle products for initial access
- **Privilege Escalation**: Abuse of SCIM configuration flaws in Grafana for admin impersonation
- **Cryptocurrency Mining**: Conversion of compromised AI clusters into mining botnets using GPU resources
- **Malvertising Campaigns**: Distribution of TamperedChef malware through fake software installers
- **Browser Notification Abuse**: Matrix Push C2 platform leveraging browser notifications for fileless attacks
- **OAuth Token Manipulation**: Unauthorized access to Salesforce data through Gainsight-linked applications
- **Ransomware Deployment**: Qilin ransomware using ScreenConnect access for network infiltration

## Threat Actor Activities

- **APT31 (China-linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services between 2024-2025
- **APT24 (China-nexus)**: Deploying BADAUDIO malware in multi-year espionage campaign targeting Taiwan and 1,000+ domains
- **Qilin Ransomware Group**: Executing sophisticated ransomware attacks using rogue ScreenConnect access and failed infostealer attempts
- **ShadowRay 2.0 Operators**: Building self-spreading GPU cryptomining botnet by exploiting unpatched Ray framework vulnerabilities
- **Scattered Spider**: British teenagers charged in Transport for London breach causing millions in damage
- **Iran-linked Actors**: Conducting cyber-enabled kinetic targeting by mapping ship AIS data before physical missile attacks
- **HackOnChat Campaign**: Global WhatsApp hijacking operation using deceptive authentication portals and impersonation pages
- **Tsundere Botnet**: Actively expanding Windows-targeting botnet using game lures and Ethereum-based command and control