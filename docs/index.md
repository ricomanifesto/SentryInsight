# Exploitation Report

The current threat landscape shows widespread active exploitation of recently patched vulnerabilities alongside sophisticated malware campaigns targeting critical infrastructure. CISA has added multiple vulnerabilities to its Known Exploited Vulnerabilities catalog, including flaws in Ivanti Endpoint Manager, SolarWinds, and VMware Workspace One that are being actively exploited in the wild. Microsoft's March 2026 Patch Tuesday addressed two zero-day vulnerabilities that were publicly disclosed before patches were available. Threat actors are increasingly targeting edge networking devices, with over 14,000 ASUS routers compromised by the KadNap botnet, while FortiGate devices are being exploited as entry points for network breaches. State-sponsored groups including Russian APT28 and North Korean UNC4899 continue sophisticated campaigns using custom toolsets and novel attack vectors.

## Active Exploitation Details

### Ivanti Endpoint Manager Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager (EPM) that allows unauthorized access to systems
- **Impact**: Attackers can gain unauthorized access to endpoint management systems and potentially compromise managed endpoints
- **Status**: Recently patched but now actively exploited in attacks, flagged by CISA with federal agencies ordered to patch within three weeks

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities in Windows systems addressed in March 2026 Patch Tuesday
- **Impact**: Exploitation allows attackers to compromise Windows systems before patches were available
- **Status**: Patches now available through KB5078885 extended security update for Windows 10 and cumulative updates KB5079473 and KB5078883 for Windows 11

### SolarWinds Vulnerability
- **Description**: Security flaw in SolarWinds products being actively exploited by threat actors
- **Impact**: Potential for supply chain attacks and unauthorized access to managed systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog based on evidence of active exploitation

### VMware Workspace One Vulnerability
- **Description**: Security vulnerability in VMware Workspace One platform
- **Impact**: Compromises enterprise mobility management and endpoint security
- **Status**: Actively exploited in the wild, flagged by CISA for immediate patching

### HPE AOS-CX Critical Authentication Flaw
- **Description**: Critical vulnerability in Hewlett Packard Enterprise Aruba Networking AOS-CX operating system allowing admin password resets
- **Impact**: Attackers can reset administrator passwords and gain full administrative access to network infrastructure
- **Status**: Multiple vulnerabilities patched including authentication bypass and code execution issues

## Affected Systems and Products

- **ASUS Routers**: Over 14,000 devices compromised by KadNap malware to create proxy botnet network
- **FortiGate NGFW Appliances**: Next-Generation Firewall devices being exploited as network entry points for credential theft
- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by zero-day vulnerabilities
- **Ivanti Endpoint Manager**: Enterprise endpoint management platform with actively exploited vulnerability
- **HPE Aruba AOS-CX**: Network operating system with critical authentication and code execution flaws
- **Google Looker Studio**: Nine cross-tenant vulnerabilities discovered allowing arbitrary SQL queries
- **Salesforce Experience Cloud**: Publicly accessible sites targeted through misconfiguration exploitation
- **npm Package Repository**: Malicious packages targeting macOS systems with credential-stealing malware

## Attack Vectors and Techniques

- **Zombie ZIP Technique**: New method for concealing malware payloads in compressed files to evade security detection
- **FortiGate Device Exploitation**: Threat actors using compromised firewall devices as initial access points for network breaches
- **AirDrop File Transfer**: UNC4899 using trojanized files transferred via AirDrop to compromise developer workstations
- **Microsoft Teams Phishing**: Attackers contacting employees through Teams to deploy A0Backdoor malware via Quick Assist
- **Modified AuraInspector Tool**: Threat actors using customized open-source tools for mass-scanning Salesforce platforms
- **Signal and WhatsApp Phishing**: Account hijacking attacks targeting government officials and military personnel
- **Malvertising with ClickFix**: InstallFix campaign spreading fake Claude AI coding assistant sites
- **NPM Package Masquerading**: Malicious packages posing as legitimate OpenClaw installer to deploy RATs
- **Geometric CAPTCHA Evasion**: Malware using geometry-based techniques to prove "humanness" and evade sandbox detection

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Using custom BEARDSHELL and COVENANT malware variants for long-term surveillance of Ukrainian military personnel and deploying customized Covenant post-exploitation framework
- **Sednit (Russian-Affiliated)**: Resurfacing with sophisticated new toolkit after years of using simple implants
- **UNC4899 (North Korean)**: Conducting sophisticated cloud compromise campaign against cryptocurrency organizations, stealing millions in cryptocurrency through AirDrop-based initial access
- **BlackSanta Campaign**: Russian-speaking attackers hijacking HR workflows to deliver EDR-killing malware for data theft operations
- **Russian State-Sponsored Groups**: Targeting government officials, military personnel, and journalists through Signal and WhatsApp account hijacking campaigns
- **Cybercriminal Networks**: Operating KadNap botnet targeting ASUS routers to create proxy infrastructure for malicious traffic routing