# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitation targeting critical infrastructure and enterprise systems. State-sponsored actors are exploiting vulnerabilities in email security gateways, federal agencies are experiencing breaches through unpatched GeoServer instances, and threat actors are leveraging misconfigured cloud infrastructure for large-scale attacks. Meanwhile, supply chain attacks continue to proliferate through compromised npm packages and SEO poisoning campaigns, while critical vulnerabilities in SolarWinds Web Help Desk require immediate attention. The emergence of new evasion techniques and sophisticated malware delivery methods highlights the evolving threat landscape facing organizations worldwide.

## Active Exploitation Details

### Libraesva Email Security Gateway Vulnerability
- **Description**: Critical vulnerability in Libraesva's Email Security Gateway solution being actively exploited by threat actors
- **Impact**: Allows unauthorized access to email security infrastructure, potentially compromising organizational email communications and security controls
- **Status**: Emergency patch released by Libraesva to address the actively exploited vulnerability

### GeoServer Vulnerability
- **Description**: Unpatched vulnerability in GeoServer geographic information system software
- **Impact**: Enables network compromise and unauthorized access to federal systems
- **Status**: Successfully exploited to breach unnamed U.S. federal civilian executive branch (FCEB) agency network

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical vulnerability in SolarWinds Web Help Desk software allowing remote code execution without authentication
- **Impact**: Attackers can execute arbitrary commands on susceptible systems, potentially leading to full system compromise
- **Status**: Third hotfix released; ongoing patching efforts required
- **CVE ID**: CVE-2025-26399

### SonicWall SMA100 Series Rootkit Deployment
- **Description**: Vulnerability in SonicWall SMA 100 series devices being exploited to deploy rootkit malware
- **Impact**: Persistent backdoor access to network infrastructure and potential lateral movement capabilities
- **Status**: Firmware update released to remove deployed rootkit malware

## Affected Systems and Products

- **Libraesva Email Security Gateway**: Email security infrastructure systems
- **GeoServer**: Geographic information system software used by federal agencies
- **SolarWinds Web Help Desk**: IT service desk and ticketing systems
- **SonicWall SMA 100 Series**: Secure Mobile Access appliances and network security devices
- **AWS Docker Containers**: Misconfigured cloud container environments
- **npm Ecosystem**: Node.js package management and JavaScript development environments
- **GitHub Repositories**: Source code repositories and development platforms
- **European Airport Systems**: Check-in and boarding systems across major airports
- **Stellantis Customer Systems**: Automotive manufacturer customer data platforms via Salesforce

## Attack Vectors and Techniques

- **SEO Poisoning**: Large-scale campaigns using compromised legitimate websites to deliver malicious content and redirect traffic
- **Supply Chain Attacks**: Malicious npm packages using QR codes to hide second-stage payloads for cookie theft
- **Container Exploitation**: ShadowV2 botnet targeting misconfigured AWS Docker containers for DDoS-for-hire services
- **Phishing Campaigns**: Sophisticated email-based attacks delivering FormBook malware to Eurasian organizations
- **Web Shell Deployment**: BadIIS malware using compromised web servers to plant persistent access mechanisms
- **EDR Evasion**: New EDR-Freeze tool leveraging Windows Error Reporting system to suspend security software
- **Third-Party Platform Compromise**: Attacks targeting service providers to access downstream customer data

## Threat Actor Activities

- **State-Sponsored Actors**: Actively exploiting Libraesva Email Security Gateway vulnerabilities for intelligence gathering and persistent access
- **Chinese-Speaking Threat Actor**: Operating "Operation Rewrite" SEO poisoning campaign using BadIIS malware for financial gain and web traffic manipulation
- **ComicForm Group**: Previously undocumented hacking group conducting phishing campaigns against Belarus, Kazakhstan, and Russia since April 2025
- **SectorJ149**: Deploying FormBook malware in coordinated attacks against Eurasian targets
- **Nimbus Manticore**: Iran-linked group targeting European organizations with improved malware variants outside their typical focus areas
- **Ransomware Groups**: Disrupting critical infrastructure including European airport systems through targeted attacks on service providers
- **Cybercriminal Networks**: Operating €100 million cryptocurrency investment fraud schemes spanning 23 countries with over 100 victims