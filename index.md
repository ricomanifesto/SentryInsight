# Exploitation Report

Critical exploitation activity is targeting multiple sectors with a focus on infrastructure vulnerabilities and supply chain attacks. State-sponsored threat actors are actively exploiting vulnerabilities in Libraesva Email Security Gateway solutions, while attackers are leveraging GeoServer exploits to breach federal agency networks. The SolarWinds Web Help Desk critical remote code execution vulnerability and Supermicro BMC firmware flaws present significant risks to enterprise environments. Additionally, sophisticated SEO poisoning campaigns and supply chain attacks through compromised npm packages are being used to deploy malware and steal sensitive data.

## Active Exploitation Details

### Libraesva Email Security Gateway Vulnerability
- **Description**: A vulnerability in Libraesva's Email Security Gateway solution that allows unauthorized access and system compromise
- **Impact**: Complete system compromise and potential access to email communications and security configurations
- **Status**: Emergency fix released by Libraesva; actively exploited by state-sponsored threat actors

### GeoServer Vulnerability
- **Description**: An unpatched vulnerability in GeoServer instances that allows unauthorized network access
- **Impact**: Complete network breach and lateral movement within federal agency infrastructure
- **Status**: Actively exploited; led to successful breach of U.S. federal civilian executive branch agency

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical vulnerability in SolarWinds Web Help Desk software allowing arbitrary command execution
- **Impact**: Complete system compromise and unauthorized code execution without authentication
- **Status**: Third hotfix released; requires immediate patching
- **CVE ID**: CVE-2025-26399

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two security vulnerabilities in Supermicro Baseboard Management Controller firmware that allow bypassing Root of Trust security mechanisms
- **Impact**: Malicious firmware can evade security controls and maintain persistent access to server infrastructure
- **Status**: Newly disclosed vulnerabilities requiring firmware updates

### American Archive of Public Broadcasting Access Control Bypass
- **Description**: Vulnerability allowing unauthorized download of protected and private media content
- **Impact**: Exposure of restricted media files and potential copyright violations
- **Status**: Quietly patched after years of exposure

## Affected Systems and Products

- **Libraesva Email Security Gateway**: All versions prior to emergency update
- **GeoServer**: Unpatched instances vulnerable to remote exploitation
- **SolarWinds Web Help Desk**: All versions prior to CVE-2025-26399 hotfix
- **Supermicro BMC Firmware**: Multiple firmware versions with Root of Trust bypass vulnerabilities
- **SonicWall SMA 100 Series**: Devices infected with rootkit malware requiring firmware updates
- **AWS Docker Containers**: Misconfigured containers being exploited for DDoS botnets
- **npm Ecosystem**: Malicious packages including 'fezbox' with QR code-based payload delivery
- **GitHub Pages**: Compromised repositories hosting fake software and malware
- **Stellantis Salesforce Instance**: Third-party platform compromised exposing customer data

## Attack Vectors and Techniques

- **SEO Poisoning Campaigns**: Large-scale manipulation of search results to redirect users to malicious content using BadIIS malware and compromised web servers
- **Supply Chain Attacks**: Malicious npm packages using innovative QR code techniques to fetch second-stage payloads and steal browser cookies
- **Docker Container Exploitation**: ShadowV2 botnet targeting misconfigured AWS Docker containers for DDoS-for-hire services
- **Phishing Campaigns**: ComicForm group deploying Formbook malware through targeted phishing in Eurasian countries
- **Ransomware Attacks**: European airport systems disrupted by ransomware targeting check-in and boarding systems
- **EDR Evasion**: New EDR-Freeze tool using Windows Error Reporting system to suspend security software from user mode
- **GitHub Repository Spoofing**: Fake repositories distributing Atomic infostealers targeting Mac users

## Threat Actor Activities

- **State-Sponsored Actors**: Actively exploiting Libraesva ESG vulnerabilities and targeting federal agency networks through GeoServer exploits
- **Chinese-Speaking Threat Actors**: Conducting SEO poisoning campaigns using BadIIS malware for traffic redirection and web shell deployment
- **ComicForm Group**: Previously undocumented hacking group targeting organizations in Belarus, Kazakhstan, and Russia with Formbook malware since April 2025
- **Nimbus Manticore (Iran-Linked)**: Targeting European organizations with improved malware variants outside their usual focus areas
- **SectorJ149**: Collaborating with ComicForm in deploying Formbook malware across Eurasian targets
- **Cryptocurrency Fraud Ring**: European law enforcement arrested five suspects linked to €100 million cryptocurrency investment fraud affecting over 100 victims across 23 countries
- **ShadowV2 Operators**: Running DDoS-for-hire services through compromised AWS infrastructure for financial gain