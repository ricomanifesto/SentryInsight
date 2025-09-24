# Exploitation Report

Critical exploitation activity is surging across multiple vectors, with state-sponsored actors actively exploiting vulnerabilities in enterprise infrastructure and supply chain components. The most significant developments include active exploitation of Libraesva Email Security Gateway by state-sponsored hackers, a federal agency breach through unpatched GeoServer instances, and the deployment of SonicWall SMA 100 series rootkit malware. Meanwhile, threat actors are leveraging sophisticated techniques including SEO poisoning campaigns, supply chain attacks through compromised npm packages, and the abuse of legitimate cloud infrastructure for malicious operations.

## Active Exploitation Details

### Libraesva Email Security Gateway Vulnerability
- **Description**: A critical vulnerability in Libraesva's Email Security Gateway solution that allows unauthorized access to email security systems
- **Impact**: Complete compromise of email security infrastructure, potential access to sensitive communications and email metadata
- **Status**: Emergency patch released by Libraesva; actively exploited by state-sponsored threat actors

### GeoServer Remote Code Execution Vulnerability
- **Description**: An unpatched vulnerability in GeoServer instances allowing remote code execution without authentication
- **Impact**: Complete system compromise, lateral movement within federal networks, data exfiltration capabilities
- **Status**: Confirmed exploitation against U.S. federal civilian executive branch agency; patch available but not applied in compromised instance

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical vulnerability allowing remote code execution without authentication in Web Help Desk software
- **Impact**: Complete system compromise, arbitrary command execution on susceptible systems
- **Status**: Third hotfix released; vulnerability requires immediate patching
- **CVE ID**: CVE-2025-26399

### SonicWall SMA 100 Series Rootkit Deployment
- **Description**: Rootkit malware specifically targeting SonicWall SMA 100 series devices through exploitation of undisclosed vulnerabilities
- **Impact**: Persistent access, traffic interception, potential network pivot point for further attacks
- **Status**: Active deployment confirmed; firmware update released to remove malware

### Supermicro BMC Security Bypass Vulnerabilities
- **Description**: Two security vulnerabilities in Supermicro Baseboard Management Controller firmware that allow bypass of Root of Trust security mechanisms
- **Impact**: Malicious firmware installation, hardware-level persistence, complete system control
- **Status**: Vulnerabilities disclosed; patch status unclear

## Affected Systems and Products

- **Libraesva Email Security Gateway**: All versions prior to emergency patch
- **GeoServer**: Unpatched instances vulnerable to remote code execution
- **SolarWinds Web Help Desk**: All versions prior to latest hotfix containing CVE-2025-26399 fix
- **SonicWall SMA 100 Series**: Devices compromised with rootkit malware
- **Supermicro BMC Firmware**: Systems with vulnerable firmware versions
- **AWS Docker Containers**: Misconfigured containers exploited by ShadowV2 botnet
- **NPM Ecosystem**: Packages compromised with malicious code including 'fezbox' package
- **GitHub Pages**: Fake repositories hosting Mac malware
- **European Airport Systems**: Check-in and boarding systems affected by ransomware

## Attack Vectors and Techniques

- **SEO Poisoning**: BadIIS malware campaign using compromised websites and search engine manipulation to redirect traffic and deploy web shells
- **Supply Chain Attacks**: Compromised npm packages using innovative techniques like QR codes to fetch second-stage payloads
- **Container Exploitation**: ShadowV2 botnet leveraging misconfigured AWS Docker containers for DDoS-for-hire services
- **Social Engineering**: Fake GitHub repositories masquerading as legitimate software to deliver Atomic infostealers
- **Firmware Manipulation**: Direct exploitation of BMC vulnerabilities to bypass hardware security mechanisms
- **Infrastructure Abuse**: Legitimate cloud-native tools used to evade detection in botnet operations

## Threat Actor Activities

- **State-Sponsored Hackers**: Active exploitation of Libraesva Email Security Gateway and federal agency infrastructure via GeoServer vulnerabilities
- **Chinese-Speaking Threat Actor**: Operation Rewrite SEO poisoning campaign using BadIIS malware to compromise legitimate web servers for financial gain
- **Iranian-Linked Group "Nimbus Manticore"**: Targeting European entities with improved malware variants and expanded geographic focus
- **ShadowV2 Botnet Operators**: Operating DDoS-for-hire service using compromised AWS infrastructure and cloud-native tools for evasion
- **Mac-Targeting Attackers**: Large-scale SEO poisoning campaign delivering Atomic infostealers through fake GitHub repositories
- **Ransomware Groups**: Successful attacks against European airport infrastructure causing operational disruptions
- **NPM Package Attackers**: Sophisticated supply chain attacks using innovative techniques like QR code-based payload delivery