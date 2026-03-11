# Exploitation Report

This period has witnessed significant exploitation activity across multiple platforms and attack vectors. Microsoft's March 2026 Patch Tuesday addressed 77-84 vulnerabilities including two publicly disclosed zero-day vulnerabilities, while threat actors have actively exploited recently patched vulnerabilities in Ivanti EPM, SolarWinds, and VMware Workspace One. Notable campaigns include UNC6426's supply chain attack exploiting the nx npm package compromise, widespread targeting of FortiGate devices for network infiltration, and the emergence of new malware variants like BlackSanta EDR killer and KadNap botnet targeting ASUS routers. The period also saw sophisticated attacks against cloud services, including Salesforce Experience Cloud misconfigurations and supply chain compromises targeting developer environments.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities patched in Microsoft's March 2026 Patch Tuesday
- **Impact**: Active exploitation allowing unauthorized access to systems
- **Status**: Patches available as part of March 2026 security updates (KB5078885, KB5079473, KB5078883)

### Ivanti Endpoint Manager Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager (EPM) recently patched but now actively exploited
- **Impact**: Network compromise and unauthorized system access
- **Status**: CISA flagged as actively exploited, federal agencies ordered to patch within three weeks

### SolarWinds Vulnerability
- **Description**: Security flaw in SolarWinds products being actively exploited in the wild
- **Impact**: Network infiltration and potential data exfiltration
- **Status**: CISA added to Known Exploited Vulnerabilities (KEV) catalog

### VMware Workspace One Vulnerability  
- **Description**: Critical security flaw in VMware Workspace One platform
- **Impact**: Administrative access and system compromise
- **Status**: CISA flagged as actively exploited, patches required

### FortiGate NGFW Exploitation
- **Description**: Threat actors exploiting FortiGate Next-Generation Firewall appliances as network entry points
- **Impact**: Network breach and service account credential theft
- **Status**: Active exploitation campaign targeting enterprise networks

### nx npm Supply Chain Compromise
- **Description**: Supply chain attack targeting the nx npm package used by developers
- **Impact**: AWS cloud environment compromise achieved within 72 hours
- **Status**: UNC6426 threat actor leveraged stolen keys for complete cloud breach

## Affected Systems and Products

- **Microsoft Windows**: All versions affected by March 2026 Patch Tuesday vulnerabilities including Windows 10 and Windows 11
- **Ivanti Endpoint Manager**: EPM systems vulnerable to active exploitation
- **SolarWinds Products**: Multiple SolarWinds solutions targeted in active campaigns
- **VMware Workspace One**: Enterprise mobility management platform at risk
- **FortiGate Firewalls**: Next-Generation Firewall appliances compromised for network entry
- **ASUS Routers**: Over 14,000 edge devices infected by KadNap malware
- **Salesforce Experience Cloud**: Publicly accessible sites with misconfigurations under mass scanning
- **Google Looker Studio**: Nine cross-tenant vulnerabilities discovered (LeakyLooker flaws)
- **HPE Aruba AOS-CX**: Multiple authentication and code execution vulnerabilities
- **Developer Environments**: npm packages, Rust crates, and CI/CD pipelines targeted

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious npm packages (nx) and Rust crates targeting developer environments
- **Zero-Day Exploitation**: Two Microsoft zero-days being actively exploited
- **Network Device Compromise**: FortiGate firewalls and ASUS routers as entry points
- **EDR Evasion**: BlackSanta malware specifically designed to kill endpoint detection systems
- **Cloud Misconfigurations**: Salesforce Experience Cloud and overly permissive configurations targeted
- **Mobile Malware**: BeatBanker Android malware masquerading as Starlink application
- **Stealth Techniques**: Zombie ZIP compression method to evade security detection
- **AI-Assisted Social Engineering**: Threat actors using geometry-based human verification bypass
- **Proxy Botnet Operations**: KadNap malware creating stealth proxy networks from infected devices

## Threat Actor Activities

- **UNC6426**: Exploited nx npm supply chain compromise to achieve complete AWS environment takeover within 72 hours
- **APT28 (Russian State-Sponsored)**: Deployed BEARDSHELL and customized COVENANT malware for long-term surveillance of Ukrainian military personnel
- **Sednit Group**: Russian-affiliated actor returned with sophisticated new malware toolkit after years of using simple implants
- **Russian-Speaking Actors**: Targeting HR departments with BlackSanta EDR killer for over one year
- **Unknown Threat Actors**: Mass scanning Salesforce Experience Cloud sites using modified AuraInspector tools
- **Cybercriminal Groups**: Operating KadNap botnet with over 14,000 infected ASUS routers for proxy services
- **Developer-Focused Attackers**: Distributing malicious Rust crates and exploiting CI/CD pipelines to steal secrets