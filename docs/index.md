# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise environments with sophisticated attack campaigns. Russian-speaking threat actors are actively deploying the BlackSanta EDR killer to compromise HR departments, while cybercriminals are exploiting recently patched vulnerabilities in Ivanti, SolarWinds, and VMware systems. Notable threats include the KadNap botnet compromising over 14,000 ASUS routers, APT28's deployment of customized malware for Ukrainian military surveillance, and widespread abuse of misconfigured Salesforce cloud environments. Attackers are increasingly leveraging zero-day vulnerabilities and novel evasion techniques to bypass modern security controls.

## Active Exploitation Details

### BlackSanta EDR Killer
- **Description**: Advanced malware designed to disable endpoint detection and response (EDR) systems, deployed through compromised HR workflows
- **Impact**: Complete bypass of security monitoring, allowing attackers to steal sensitive data without detection
- **Status**: Actively exploited by Russian-speaking threat actors for over a year

### Ivanti Endpoint Manager Vulnerability
- **Description**: High-severity flaw in Ivanti Endpoint Manager (EPM) recently patched but now under active attack
- **Impact**: System compromise and unauthorized access to enterprise endpoints
- **Status**: Actively exploited in the wild, flagged by CISA with mandatory patching deadline for federal agencies

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities addressed in March 2026 Patch Tuesday
- **Impact**: System compromise and potential privilege escalation
- **Status**: Publicly disclosed and patched, but exploitation details indicate active targeting

### FortiGate NGFW Exploitation
- **Description**: Threat actors abusing FortiGate Next-Generation Firewall appliances as network entry points
- **Impact**: Network breach and theft of service account credentials
- **Status**: Active campaign targeting enterprise firewall infrastructure

### SolarWinds and VMware Workspace One Vulnerabilities
- **Description**: Security flaws in SolarWinds software and VMware Workspace One platforms
- **Impact**: System compromise and unauthorized access to enterprise environments
- **Status**: Actively exploited, added to CISA's Known Exploited Vulnerabilities catalog

### Google Looker Studio LeakyLooker Flaws
- **Description**: Nine cross-tenant vulnerabilities enabling arbitrary SQL query execution across customer databases
- **Impact**: Data exfiltration and unauthorized access to sensitive information across multiple tenants
- **Status**: Disclosed vulnerabilities with potential for exploitation

### HPE AOS-CX Critical Authentication Bypass
- **Description**: Critical vulnerability in Aruba Networking AOS-CX operating system allowing administrative password resets
- **Impact**: Complete system takeover through authentication bypass
- **Status**: Recently patched with multiple authentication and code execution issues addressed

## Affected Systems and Products

- **Ivanti Endpoint Manager**: Enterprise endpoint management systems requiring immediate patching
- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by zero-day vulnerabilities and cumulative updates
- **FortiGate Appliances**: Next-Generation Firewall devices used as network entry points
- **ASUS Routers**: Over 14,000 edge networking devices compromised by KadNap botnet
- **SolarWinds Software**: Enterprise monitoring and management solutions
- **VMware Workspace One**: Digital workspace platforms with active exploitation
- **Google Looker Studio**: Business intelligence and data visualization platform
- **HPE Aruba Networking**: AOS-CX operating system with critical authentication flaws
- **Salesforce Experience Cloud**: Publicly accessible cloud sites with configuration vulnerabilities
- **Android Devices**: Mobile platforms targeted by BeatBanker malware posing as Starlink applications

## Attack Vectors and Techniques

- **EDR Evasion**: BlackSanta malware specifically designed to disable endpoint detection and response systems
- **Social Engineering**: Microsoft Teams phishing campaigns deploying A0Backdoor malware through Quick Assist
- **Malvertising**: InstallFix campaigns spreading fake AI coding assistant sites
- **Supply Chain Attacks**: Malicious npm packages masquerading as legitimate OpenClaw installers
- **Zombie ZIP Technique**: Novel compression method to conceal payloads from security scanning tools
- **Geometry-Based Evasion**: Advanced sandbox evasion using geometric patterns to simulate human behavior
- **Configuration Exploitation**: Mass scanning of misconfigured Salesforce environments using modified AuraInspector tools
- **Botnet Proxy Networks**: KadNap malware creating stealth proxy infrastructure through compromised routers
- **Cross-Tenant Attacks**: Exploitation of cloud platform vulnerabilities to access multiple customer environments

## Threat Actor Activities

- **Russian-Speaking Groups**: Year-long campaign targeting HR departments with BlackSanta EDR killer and sophisticated toolkit deployment
- **APT28 (Sednit)**: Russian state-sponsored group using BEARDSHELL and COVENANT malware for Ukrainian military surveillance with customized Covenant framework variants
- **Cybercriminal Networks**: KadNap botnet operators compromising thousands of ASUS routers for proxy traffic infrastructure
- **Financial Threat Actors**: BeatBanker campaign targeting Android users through fake Starlink applications and fraudulent app stores
- **Enterprise Attackers**: Coordinated campaigns exploiting FortiGate appliances and Salesforce misconfigurations for credential theft and data access
- **Supply Chain Attackers**: npm ecosystem targeting with malicious packages deploying remote access trojans on macOS systems