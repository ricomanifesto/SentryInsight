# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited by threat actors across multiple platforms and industries. Most concerning are the active exploitation of CVE-2024-36401 in GeoServer systems used by federal agencies, CVE-2025-51591 in Pandoc affecting AWS environments, and an unnamed Cisco IOS zero-day vulnerability currently under attack. State-sponsored groups, particularly suspected Chinese actors like UNC5221 and RedNovember, are conducting sustained espionage campaigns using sophisticated backdoors including BRICKSTORM and Pantegana. Additionally, cybercriminal groups like Scattered Spider continue high-value ransomware operations despite recent arrests, while new malware families and attack vectors emerge targeting everything from supply chain components to mobile devices.

## Active Exploitation Details

### GeoServer Critical Vulnerability
- **Description**: Critical flaw in GeoServer geospatial software that allows unauthorized access to systems
- **Impact**: Complete system compromise and data access for federal agencies
- **Status**: Exploited less than two weeks after disclosure, used to breach large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Cisco IOS Zero-Day Vulnerability
- **Description**: High-severity zero-day vulnerability affecting Cisco IOS and IOS XE Software
- **Impact**: System compromise and potential network infiltration
- **Status**: Currently being exploited in active attacks, security updates released by Cisco

### Pandoc AWS Credential Theft Vulnerability
- **Description**: Security flaw in Pandoc Linux utility enabling attacks against AWS Instance Metadata Service (IMDS)
- **Impact**: Theft of EC2 IAM credentials and cloud environment compromise
- **Status**: Actively exploited in the wild to target AWS environments
- **CVE ID**: CVE-2025-51591

### Libraesva Email Security Gateway Vulnerability
- **Description**: Vulnerability in Libraesva Email Security Gateway (ESG) solution
- **Impact**: System compromise and potential email security bypass
- **Status**: Exploited by state-sponsored threat actors, security update released

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two vulnerabilities affecting Supermicro Baseboard Management Controller (BMC) firmware
- **Impact**: Allows attackers to update systems with maliciously crafted images, creating persistent backdoors
- **Status**: Disclosed vulnerabilities that can enable long-term persistence

### OnePlus SMS Access Vulnerability
- **Description**: Vulnerability in multiple OnePlus OxygenOS versions allowing unauthorized SMS access
- **Impact**: Any installed app can access SMS data and metadata without permission or user interaction
- **Status**: Currently unpatched, affects multiple OxygenOS versions

## Affected Systems and Products

- **GeoServer**: Geospatial software used by federal agencies and organizations
- **Cisco IOS/IOS XE**: Network infrastructure software across enterprise and government networks
- **AWS EC2**: Cloud instances running Pandoc utility vulnerable to credential theft
- **Libraesva ESG**: Email security gateway solutions in enterprise environments
- **Supermicro Hardware**: BMC firmware in server and infrastructure hardware
- **OnePlus Devices**: Multiple OxygenOS versions on OnePlus smartphones
- **SonicWall SMA**: Security appliances targeted by OVERSTEP backdoor deployments
- **Wondershare RepairIt**: Software with critical flaws exposing user data and AI models

## Attack Vectors and Techniques

- **Rapid Exploitation**: Vulnerabilities exploited within weeks of disclosure, demonstrating sophisticated threat actor capabilities
- **Federal Agency Targeting**: Direct attacks on government infrastructure using geospatial software vulnerabilities
- **Cloud Credential Theft**: Exploitation of Linux utilities to steal AWS IAM credentials via IMDS attacks
- **Firmware Backdoors**: Installation of persistent backdoors in BMC firmware for long-term access
- **Supply Chain Attacks**: NPM packages containing steganographically hidden malware in QR codes
- **Mobile Permission Bypass**: Unauthorized access to SMS data without user consent or permission requests
- **Email Gateway Compromise**: State-sponsored exploitation of email security solutions
- **Social Engineering**: GitHub notifications abused to impersonate Y Combinator for cryptocurrency theft
- **Ransomware Deployment**: RTX ransomware causing widespread European airport disruptions

## Threat Actor Activities

- **UNC5221**: China-nexus group using BRICKSTORM backdoor to infiltrate U.S. legal and technology sectors for over a year
- **RedNovember**: Suspected Chinese hackers targeting global government and private organizations using Pantegana and Cobalt Strike
- **UNC6148**: Threat actors deploying OVERSTEP backdoor in ongoing SonicWall SMA attacks
- **Scattered Spider**: Cybercrime group linked to $115 million in ransoms, with recent arrests of key members including 19-year-old Thalha Jubair
- **State-Sponsored Actors**: Multiple nation-state groups exploiting Libraesva ESG vulnerabilities for espionage
- **RTX Ransomware Operators**: Group causing major disruptions to European airports, with UK arrest of suspect
- **Supply Chain Attackers**: Threat actors deploying YiBackdoor malware with code overlaps to IcedID and Latrodectus
- **Cryptocurrency Thieves**: Campaigns targeting GitHub users with fake Y Combinator invitations for crypto theft