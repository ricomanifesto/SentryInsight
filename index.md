# Exploitation Report

Critical vulnerability exploitation activity is intensifying across multiple platforms and sectors, with several zero-day vulnerabilities being actively exploited by both cybercriminals and nation-state actors. The most significant incidents include CISA confirming that threat actors successfully breached a federal agency by exploiting CVE-2024-36401 in GeoServer within two weeks of disclosure, and Cisco warning of active exploitation of a zero-day vulnerability in IOS and IOS XE software. Additional concerns include state-sponsored hackers exploiting Libraesva Email Security Gateway vulnerabilities, active exploitation of CVE-2025-51591 in Pandoc targeting AWS environments, and the discovery of multiple critical flaws in enterprise systems including Supermicro BMC firmware and OnePlus devices.

## Active Exploitation Details

### GeoServer Critical Vulnerability
- **Description**: Critical vulnerability in GeoServer geospatial software that allows unauthorized access to federal systems
- **Impact**: Successful breach of a large federal civilian executive branch agency
- **Status**: Actively exploited less than two weeks after initial disclosure
- **CVE ID**: CVE-2024-36401

### Cisco IOS Zero-Day Vulnerability
- **Description**: High-severity zero-day vulnerability in Cisco IOS and IOS XE Software currently being exploited in attacks
- **Impact**: Allows attackers to compromise network infrastructure devices
- **Status**: Active exploitation confirmed, security updates released by Cisco
- **CVE ID**: Not specified in article

### Libraesva Email Security Gateway Vulnerability
- **Description**: Vulnerability in Libraesva Email Security Gateway solution being exploited by state-sponsored threat actors
- **Impact**: Compromise of email security infrastructure
- **Status**: Active exploitation by state-sponsored actors, security update released
- **CVE ID**: Not specified in article

### Pandoc Vulnerability Targeting AWS
- **Description**: Security flaw in Pandoc Linux utility being exploited to target AWS Instance Metadata Service (IMDS)
- **Impact**: Theft of EC2 IAM credentials and potential cloud infrastructure compromise
- **Status**: In-the-wild exploitation confirmed
- **CVE ID**: CVE-2025-51591

### SonicWall SMA Attacks
- **Description**: Ongoing attacks against SonicWall SMA security devices using OVERSTEP backdoor
- **Impact**: Installation of persistent backdoors allowing system control, password theft, and activity concealment
- **Status**: Active campaign by UNC6148 threat group

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two vulnerabilities in Supermicro Baseboard Management Controller firmware allowing malicious image updates
- **Impact**: Creation of persistent backdoors in hardware systems
- **Status**: Recently disclosed vulnerabilities with backdoor potential

### OnePlus OxygenOS Vulnerability
- **Description**: Unpatched vulnerability in multiple OnePlus OxygenOS versions allowing unauthorized SMS access
- **Impact**: Any installed app can access SMS data and metadata without permissions
- **Status**: Unpatched vulnerability affecting multiple OnePlus device versions

## Affected Systems and Products

- **GeoServer**: Geospatial software used by federal agencies
- **Cisco IOS/IOS XE**: Network infrastructure devices and software
- **Libraesva Email Security Gateway**: Enterprise email security solutions
- **Pandoc**: Linux utility for document conversion
- **AWS EC2**: Cloud computing instances and IAM credential systems
- **SonicWall SMA**: Security management appliances
- **Supermicro Hardware**: Server hardware with BMC firmware
- **OnePlus Devices**: Mobile devices running OxygenOS
- **Wondershare RepairIt**: File repair software with data exposure risks

## Attack Vectors and Techniques

- **Rapid Exploitation**: Attackers exploiting vulnerabilities within two weeks of disclosure
- **Zero-Day Exploitation**: Active use of previously unknown vulnerabilities
- **Backdoor Installation**: Deployment of persistent access mechanisms like OVERSTEP
- **Cloud Infrastructure Targeting**: Specific attacks against AWS IMDS for credential theft
- **Supply Chain Attacks**: Malicious NPM packages with steganographic QR code obfuscation
- **Phishing Campaigns**: GitHub notifications abuse and fake PyPI websites
- **Hardware-Level Persistence**: BMC firmware exploitation for persistent backdoors
- **Mobile Platform Exploitation**: Unauthorized access to SMS data without permissions

## Threat Actor Activities

- **UNC6148**: Deploying OVERSTEP backdoor in SonicWall SMA attacks with persistent access capabilities
- **UNC5221**: Using BRICKSTORM backdoor to infiltrate U.S. legal and technology sectors for over a year
- **RedNovember (Chinese APT)**: Targeting global governments using Pantegana and Cobalt Strike, leveraging open-source tools and proof-of-concepts
- **Scattered Spider**: Cybercrime group with members charged for $115M in ransoms, though claims of shutdown remain disputed
- **State-Sponsored Actors**: Exploiting Libraesva Email Security Gateway vulnerabilities for espionage operations
- **Russian Disinformation Campaigns**: Targeting Moldovan elections through coordinated information warfare
- **Supply Chain Attackers**: Deploying malicious NPM packages with sophisticated obfuscation techniques
- **RTX Ransomware Operators**: Causing widespread European airport disruptions with recent UK arrest