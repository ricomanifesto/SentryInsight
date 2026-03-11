# Exploitation Report

Critical vulnerability exploitation activity is intensifying across multiple platforms, with Microsoft addressing two actively exploited zero-day vulnerabilities in its March 2026 Patch Tuesday release alongside 77 other security flaws. The threat landscape is further complicated by active exploitation of recently patched Ivanti Endpoint Manager vulnerabilities, which CISA has flagged for immediate federal agency remediation. Sophisticated threat actors are deploying advanced evasion techniques including the new BlackSanta EDR killer targeting HR departments, while Russian state-sponsored group APT28 continues espionage operations using customized variants of open-source tools. Additionally, cybercriminals are exploiting misconfigurations in cloud services, particularly targeting Salesforce Experience Cloud sites and FortiGate devices as network entry points.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities in Microsoft Windows systems that were being actively exploited before patches were available
- **Impact**: Attackers can gain unauthorized access to Windows systems and potentially achieve privilege escalation or system compromise
- **Status**: Patched in Microsoft's March 2026 Patch Tuesday release, with security updates available for Windows 10 and Windows 11

### Ivanti Endpoint Manager (EPM) Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager that allows attackers to compromise endpoint management systems
- **Impact**: Threat actors can gain unauthorized access to enterprise endpoint management infrastructure
- **Status**: Recently patched but now actively exploited in the wild; CISA has ordered federal agencies to patch within three weeks

### SolarWinds Vulnerability
- **Description**: Security flaw in SolarWinds software that enables unauthorized access to affected systems
- **Impact**: Attackers can compromise network management and monitoring capabilities
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog

### VMware Workspace One Vulnerability
- **Description**: Security vulnerability affecting VMware's Workspace One platform
- **Impact**: Potential compromise of virtual desktop infrastructure and mobile device management systems
- **Status**: Actively exploited and flagged by CISA for immediate attention

### HPE Aruba Networking AOS-CX Critical Flaw
- **Description**: Critical vulnerability allowing unauthorized admin password resets in HPE's AOS-CX operating system
- **Impact**: Complete administrative takeover of network switching infrastructure
- **Status**: Multiple security vulnerabilities patched, including authentication and code execution issues

### Google Looker Studio LeakyLooker Vulnerabilities
- **Description**: Nine cross-tenant vulnerabilities enabling unauthorized SQL query execution across different customer environments
- **Impact**: Attackers could run arbitrary SQL queries on victims' databases and exfiltrate sensitive data
- **Status**: Disclosed vulnerabilities that could enable cross-tenant data breaches

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by zero-day exploits
- **Ivanti Endpoint Manager**: Enterprise endpoint management platforms vulnerable to active exploitation  
- **SolarWinds Products**: Network management and monitoring software under active attack
- **VMware Workspace One**: Virtual desktop and mobile device management platforms
- **HPE Aruba AOS-CX**: Network switching operating systems with critical authentication flaws
- **FortiGate NGFW Appliances**: Next-generation firewall devices being abused as network entry points
- **ASUS Routers**: Edge networking devices targeted by KadNap botnet malware
- **Google Looker Studio**: Business intelligence platform vulnerable to cross-tenant attacks
- **Salesforce Experience Cloud**: Public-facing cloud services with misconfiguration exploitation
- **Android Devices**: Mobile devices targeted by BeatBanker malware masquerading as Starlink app

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate exploitation of unpatched vulnerabilities before fixes are available
- **Phishing via Microsoft Teams**: Social engineering attacks using trusted collaboration platforms to deploy A0Backdoor malware
- **EDR Evasion**: BlackSanta malware specifically designed to bypass endpoint detection and response systems
- **Cloud Misconfiguration Abuse**: Exploitation of overly permissive configurations in Salesforce and other cloud services
- **Botnet Proxy Networks**: KadNap malware converting compromised routers into stealth proxy infrastructure
- **Zombie ZIP Technique**: New compression-based evasion method to slip malware past security tools
- **Modified Open-Source Tools**: Customized versions of legitimate tools like AuraInspector for scanning vulnerabilities
- **Quick Assist Abuse**: Legitimate remote access tools used for initial compromise and malware deployment
- **App Impersonation**: Malware disguised as legitimate applications like Starlink distributed through fake app stores

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Conducting long-term espionage operations against Ukrainian military personnel using BEARDSHELL and customized COVENANT malware variants
- **Sednit Group**: Russian-affiliated threat actor returning with sophisticated new malware toolkit after period of using simpler implants
- **Russian-Speaking Actors**: Targeting HR departments with BlackSanta EDR killer malware for over one year, focusing on workflow hijacking
- **Multiple Threat Groups**: Mass-scanning Salesforce Experience Cloud sites using modified AuraInspector tools to identify misconfigurations
- **Cybercriminal Networks**: Exploiting cloud vulnerabilities with attack windows shrinking from weeks to just days after disclosure
- **Botnet Operators**: Deploying KadNap malware to build proxy networks from compromised ASUS routers and edge devices