# Exploitation Report

The current threat landscape shows intensified exploitation activity across multiple critical vulnerabilities, with threat actors leveraging both zero-day vulnerabilities and recently patched flaws. Microsoft's March 2026 Patch Tuesday addressed two publicly disclosed zero-day vulnerabilities among 79 total security flaws. CISA has flagged several high-severity vulnerabilities in enterprise software as actively exploited, including flaws in Ivanti Endpoint Manager, SolarWinds, and VMware Workspace One. Advanced persistent threat groups, particularly Russian state-sponsored APT28, are conducting sophisticated espionage operations using customized malware frameworks. Meanwhile, botnet operators are targeting edge devices and network infrastructure, with the KadNap malware compromising over 14,000 ASUS routers to create stealth proxy networks for malicious traffic routing.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities affecting Windows systems were addressed in Microsoft's March 2026 Patch Tuesday
- **Impact**: Allows attackers to exploit unpatched Windows systems with publicly available vulnerability information
- **Status**: Patched in March 2026 security updates, but exploitation likely ongoing on unpatched systems

### Ivanti Endpoint Manager Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager (EPM) recently patched but now actively exploited
- **Impact**: Attackers can compromise enterprise endpoint management infrastructure
- **Status**: Actively exploited according to CISA; U.S. federal agencies ordered to patch within three weeks

### SolarWinds Vulnerability
- **Description**: Security flaw in SolarWinds software flagged by CISA as actively exploited
- **Impact**: Potential compromise of network monitoring and management infrastructure
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### VMware Workspace One Vulnerability  
- **Description**: Security vulnerability in VMware Workspace One platform being actively exploited
- **Impact**: Compromise of enterprise mobile device management and virtual desktop infrastructure
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog

### HPE AOS-CX Critical Vulnerability
- **Description**: Critical authentication bypass flaw in Hewlett Packard Enterprise Aruba Networking AOS-CX operating system allowing admin password resets
- **Impact**: Complete administrative takeover of network switching infrastructure
- **Status**: Recently patched by HPE

### Google Looker Studio Cross-Tenant Vulnerabilities
- **Description**: Nine cross-tenant vulnerabilities dubbed "LeakyLooker" affecting Google Looker Studio
- **Impact**: Attackers could execute arbitrary SQL queries on victims' databases and exfiltrate sensitive data across tenant boundaries
- **Status**: Disclosed vulnerabilities, patch status unclear

## Affected Systems and Products

- **Microsoft Windows**: All Windows versions affected by March 2026 zero-day vulnerabilities
- **Ivanti Endpoint Manager (EPM)**: Enterprise endpoint management systems actively targeted
- **SolarWinds Software**: Network monitoring and IT management platforms
- **VMware Workspace One**: Enterprise mobility management and virtual desktop infrastructure
- **HPE Aruba Networking AOS-CX**: Network switching operating system with critical authentication bypass
- **ASUS Routers**: Over 14,000 devices compromised by KadNap malware for botnet operations  
- **FortiGate NGFW Appliances**: Next-Generation Firewall devices used as network entry points
- **Google Looker Studio**: Business intelligence and data visualization platform
- **Salesforce Experience Cloud**: Customer portal and community platforms with misconfigurations
- **Microsoft Teams**: Corporate communication platform targeted for malware delivery

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging publicly disclosed but unpatched Windows vulnerabilities
- **Supply Chain Compromise**: Malicious npm packages masquerading as legitimate software installers
- **Social Engineering via Teams**: Phishing campaigns using Microsoft Teams to deliver A0Backdoor malware and gain remote access
- **Botnet Infrastructure**: KadNap malware creating stealth proxy networks using compromised edge devices
- **Network Appliance Compromise**: FortiGate devices exploited as initial access points for network breaches
- **Cross-Tenant Data Exfiltration**: LeakyLooker vulnerabilities enabling unauthorized database access across Google Looker tenants
- **Configuration Exploitation**: Salesforce Experience Cloud misconfigurations allowing unauthorized guest user data access
- **AirDrop File Transfer**: UNC4899 using AirDrop to deliver trojanized files to cryptocurrency organization work devices
- **EDR Evasion**: BlackSanta malware specifically designed to bypass endpoint detection and response systems
- **Signal/WhatsApp Account Hijacking**: Phishing campaigns targeting government officials and military personnel

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Conducting long-term surveillance operations against Ukrainian military personnel using BEARDSHELL and COVENANT implants; customizing open-source Covenant framework for espionage
- **UNC4899 (North Korean)**: Sophisticated cryptocurrency theft operations targeting crypto organizations through trojanized AirDrop file transfers and cloud infrastructure compromise
- **ShinyHunters**: Claiming ongoing attacks against Salesforce Aura platforms to steal customer data through misconfigured Experience Cloud sites
- **Russian-Speaking Attackers**: Operating BlackSanta EDR killer campaigns targeting HR workflows to deliver security-bypassing malware
- **KadNap Botnet Operators**: Compromising ASUS routers and edge devices to build proxy networks for malicious traffic routing
- **FortiGate Exploiters**: Using compromised FortiGate appliances as persistent network access points for credential theft and lateral movement
- **Teams-Based Social Engineers**: Targeting financial and healthcare organizations through Microsoft Teams phishing to deploy backdoor malware