# Exploitation Report

Critical exploitation activity is currently dominated by Microsoft's March 2026 Patch Tuesday release addressing 79-84 security flaws including two publicly disclosed zero-day vulnerabilities. Threat actors are actively exploiting recently patched vulnerabilities in enterprise infrastructure, with CISA flagging critical flaws in SolarWinds, Ivanti EPM, and VMware Workspace One for active exploitation. Notable campaigns include UNC6426's sophisticated supply chain attack leveraging stolen npm package credentials to achieve AWS administrator access within 72 hours, and APT28's deployment of custom malware variants for long-term surveillance operations. The threat landscape also features new evasion techniques like the "Zombie ZIP" method and BlackSanta EDR killer, alongside widespread botnet operations targeting edge devices and mobile platforms.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities patched in Microsoft's March 2026 Patch Tuesday update
- **Impact**: These vulnerabilities were publicly known before patches were available, creating significant exposure windows for exploitation
- **Status**: Patches released in March 2026 security updates including Windows 11 KB5079473, KB5078883, and Windows 10 KB5078885

### Ivanti Endpoint Manager (EPM) Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager recently patched but now actively exploited
- **Impact**: Allows attackers to compromise endpoint management systems
- **Status**: CISA has flagged as actively exploited and ordered federal agencies to patch within three weeks

### SolarWinds Vulnerability
- **Description**: Security flaw in SolarWinds products identified by CISA as actively exploited
- **Impact**: Potential for supply chain compromise and enterprise network infiltration
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog

### VMware Workspace One Vulnerability
- **Description**: Security vulnerability in VMware Workspace One platform
- **Impact**: Compromise of virtual desktop infrastructure and endpoint management
- **Status**: Flagged by CISA as actively exploited

### HPE AOS-CX Authentication Bypass
- **Description**: Critical authentication vulnerability allowing admin password resets in Aruba Networking AOS-CX operating system
- **Impact**: Complete administrative access to network infrastructure devices
- **Status**: Multiple security vulnerabilities patched including authentication and code execution issues

### FortiGate Next-Generation Firewall Exploitation
- **Description**: Threat actors are abusing FortiGate NGFW appliances as entry points to breach networks
- **Impact**: Network breach and service account credential theft
- **Status**: Ongoing campaign targeting FortiGate devices for initial access

### Google Looker Studio Cross-Tenant Vulnerabilities
- **Description**: Nine cross-tenant vulnerabilities dubbed "LeakyLooker" discovered in Google Looker Studio
- **Impact**: Could permit attackers to run arbitrary SQL queries on victims' databases and exfiltrate sensitive data
- **Status**: Vulnerabilities disclosed, requiring immediate attention from Google Looker Studio users

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by March 2026 Patch Tuesday vulnerabilities
- **Ivanti Endpoint Manager**: EPM systems actively targeted following recent patch release
- **SolarWinds Products**: Various SolarWinds software components flagged for active exploitation
- **VMware Workspace One**: Virtual desktop infrastructure platforms under active attack
- **HPE Aruba Networking**: AOS-CX operating system with critical authentication flaws
- **FortiGate Appliances**: Next-Generation Firewall devices used as network entry points
- **Google Looker Studio**: Business intelligence platform vulnerable to cross-tenant attacks
- **ASUS Routers**: Over 14,000 edge devices infected by KadNap botnet malware
- **Android Devices**: Mobile platforms targeted by BeatBanker malware posing as Starlink app
- **Salesforce Experience Cloud**: Publicly accessible sites targeted via modified AuraInspector tool
- **npm Package Ecosystem**: JavaScript package repository affected by nx package supply chain compromise

## Attack Vectors and Techniques

- **Supply Chain Compromise**: UNC6426 leveraged stolen keys from compromised nx npm package to achieve rapid cloud environment breach
- **EDR Evasion**: BlackSanta malware specifically designed to bypass endpoint detection and response systems
- **Zombie ZIP Technique**: New method to conceal payloads in compressed files to avoid security solution detection
- **Social Engineering**: BeatBanker malware uses fake Starlink applications and counterfeit Google Play Store websites
- **Network Device Exploitation**: KadNap botnet targets ASUS routers and edge devices to create proxy networks
- **HR Department Targeting**: BlackSanta campaign specifically focuses on human resources workflows
- **Geometry-Based Evasion**: Advanced malware using geometric patterns to simulate human behavior and evade sandbox detection
- **Mass Scanning Operations**: Threat actors using modified tools to identify misconfigured Salesforce Experience Cloud sites
- **Cross-Tenant Attacks**: Exploitation of multi-tenant cloud services to access unauthorized data
- **Malicious Package Distribution**: Five malicious Rust crates distributed via crates.io to steal developer secrets

## Threat Actor Activities

- **UNC6426**: Conducted sophisticated supply chain attack achieving AWS administrator access within 72 hours using stolen nx npm package credentials
- **APT28**: Russian state-sponsored group deploying BEARDSHELL and custom COVENANT malware variants for long-term surveillance of Ukrainian military personnel
- **Russian-Speaking Actors**: Operating BlackSanta EDR killer campaign targeting HR departments for over one year
- **Sednit Group**: Russian-affiliated actor resurging with sophisticated new malware toolkit after years of using simple implants
- **KadNap Operators**: Cybercriminals managing botnet of 14,000+ infected ASUS routers for proxy network operations
- **BeatBanker Distributors**: Android malware operators creating fake Starlink applications and counterfeit app stores
- **Salesforce Scanners**: Threat actors using modified AuraInspector tools to mass-scan for Experience Cloud misconfigurations
- **Malicious Rust Developers**: Publishing time-related utility crates to steal .env file data from CI/CD pipelines