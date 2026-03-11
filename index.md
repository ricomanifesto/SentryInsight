# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitation targeting enterprise systems, cloud infrastructures, and network devices. Microsoft's March 2026 Patch Tuesday addressed 2 zero-day vulnerabilities alongside 79 other security flaws, while CISA has flagged multiple vulnerabilities in SolarWinds, Ivanti, and VMware Workspace One as actively exploited. The threat landscape is further complicated by sophisticated supply chain attacks through malicious Rust crates, advanced EDR evasion techniques, and targeted campaigns against critical infrastructure including FortiGate firewalls and ASUS routers. State-sponsored groups like APT28 continue their espionage operations with customized toolkits, while cybercriminals deploy new malware variants that bypass traditional security defenses.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities affecting Windows systems that were patched in March 2026
- **Impact**: Attackers can exploit these flaws to compromise Windows devices and potentially gain system-level access
- **Status**: Patches available through KB5078885 extended security update for Windows 10 and cumulative updates for Windows 11

### Ivanti Endpoint Manager Vulnerability
- **Description**: High-severity vulnerability in Ivanti EPM that allows unauthorized access to endpoint management systems
- **Impact**: Attackers can gain control over managed endpoints and potentially pivot throughout enterprise networks
- **Status**: Recently patched but now actively exploited in the wild according to CISA

### SolarWinds Platform Vulnerabilities
- **Description**: Security flaws in SolarWinds software that enable unauthorized access to network monitoring infrastructure
- **Impact**: Compromise of critical network visibility and management capabilities
- **Status**: Actively exploited according to CISA KEV catalog

### VMware Workspace One Vulnerabilities
- **Description**: Security vulnerabilities affecting VMware's unified endpoint management platform
- **Impact**: Potential compromise of enterprise mobile and desktop device management
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### HPE AOS-CX Critical Authentication Flaw
- **Description**: Critical vulnerability in Aruba Networking AOS-CX operating system allowing admin password resets
- **Impact**: Complete administrative takeover of network infrastructure devices
- **Status**: Multiple security vulnerabilities patched including authentication bypass and code execution issues

### Google Looker Studio Cross-Tenant Vulnerabilities (LeakyLooker)
- **Description**: Nine cross-tenant vulnerabilities enabling unauthorized access to victim databases
- **Impact**: Arbitrary SQL query execution and data exfiltration across tenant boundaries
- **Status**: Disclosed vulnerabilities that could permit cross-tenant data access

## Affected Systems and Products

- **Microsoft Windows Systems**: Windows 10, Windows 11 versions 23H2, 24H2, and 25H2 affected by zero-day vulnerabilities and 77+ additional security flaws
- **Ivanti Endpoint Manager**: EPM systems vulnerable to high-severity exploitation
- **SolarWinds Platform**: Network monitoring and management infrastructure
- **VMware Workspace One**: Unified endpoint management platforms
- **HPE Aruba Networking**: AOS-CX operating system with authentication and code execution vulnerabilities
- **ASUS Router Devices**: Over 14,000 edge devices infected by KadNap botnet malware
- **FortiGate NGFW Appliances**: Next-Generation Firewall devices exploited as network entry points
- **Google Looker Studio**: Business intelligence platform with cross-tenant access vulnerabilities
- **Salesforce Experience Cloud**: Publicly accessible sites with misconfiguration exploitation
- **Android Devices**: Targeted by BeatBanker malware masquerading as Starlink applications

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Five malicious Rust crates masquerading as time utilities to steal developer secrets from CI/CD pipelines
- **EDR Evasion**: BlackSanta malware specifically designed to kill endpoint detection and response systems
- **Social Engineering**: Microsoft Teams phishing campaigns delivering A0Backdoor malware through Quick Assist remote access
- **Network Device Compromise**: Exploitation of router and firewall vulnerabilities for persistent network access
- **Zombie ZIP Technique**: New compression-based evasion method to bypass antivirus and EDR detection
- **Geometry-Based Human Simulation**: Advanced sandbox evasion using mouse movement patterns to simulate human behavior
- **Cross-Platform Mobile Targeting**: Android malware distribution through fake Google Play Store websites
- **Cloud Misconfiguration Exploitation**: Mass scanning of Salesforce Experience Cloud sites using modified AuraInspector tools

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Deploying BEARDSHELL and customized COVENANT malware variants for long-term surveillance of Ukrainian military personnel
- **Sednit Group**: Resurfacing with sophisticated new malware toolkit after years of using simple implants
- **Russian-Speaking Threat Actors**: Targeting HR departments with BlackSanta EDR killer malware for over one year
- **KadNap Botnet Operators**: Infecting 14,000+ ASUS routers to create stealth proxy network for cybercrime operations
- **BeatBanker Campaign**: Android banking malware operators using fake Starlink applications to hijack mobile devices
- **FortiGate Exploitation Campaign**: Threat actors abusing firewall appliances as entry points to steal service account credentials
- **Rust Crate Poisoners**: Cybercriminals targeting developer environments through malicious package repositories
- **Salesforce Reconnaissance Operations**: Threat actors conducting mass scanning operations against misconfigured cloud environments