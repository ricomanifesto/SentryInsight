# Exploitation Report

Critical exploitation activity continues to surge across multiple sectors with several zero-day vulnerabilities being actively exploited in the wild. The most severe incidents include attackers breaching a federal agency through a GeoServer vulnerability (CVE-2024-36401) within two weeks of disclosure, a Cisco IOS zero-day being exploited in active attacks, and state-sponsored threat actors exploiting multiple vulnerabilities including Pandoc CVE-2025-51591 for AWS credential theft and a Libraesva Email Security Gateway flaw. Chinese APT groups remain particularly active, with RedNovember and UNC5221 conducting sophisticated espionage campaigns against global governments and U.S. organizations using advanced backdoors and exploiting both known and zero-day vulnerabilities.

## Active Exploitation Details

### GeoServer Critical Vulnerability
- **Description**: Critical flaw in GeoServer geospatial software that allows unauthorized access to systems
- **Impact**: Complete system compromise and unauthorized access to federal agency networks
- **Status**: Actively exploited within two weeks of initial disclosure; patches available
- **CVE ID**: CVE-2024-36401

### Cisco IOS Zero-Day Vulnerability
- **Description**: High-severity zero-day vulnerability in Cisco IOS and IOS XE Software currently being exploited
- **Impact**: Network device compromise and potential lateral movement capabilities
- **Status**: Active exploitation confirmed; security updates released by Cisco

### Pandoc Server-Side Request Forgery
- **Description**: Vulnerability in Pandoc Linux utility allowing attackers to make arbitrary HTTP requests
- **Impact**: AWS Instance Metadata Service (IMDS) exploitation leading to EC2 IAM credential theft
- **Status**: In-the-wild exploitation detected targeting cloud environments
- **CVE ID**: CVE-2025-51591

### Libraesva Email Security Gateway Vulnerability
- **Description**: Security flaw in Libraesva Email Security Gateway (ESG) solution
- **Impact**: Email security bypass and potential system compromise
- **Status**: Actively exploited by state-sponsored threat actors; security update released

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two vulnerabilities affecting Supermicro Baseboard Management Controller (BMC) firmware
- **Impact**: Persistent backdoor installation through maliciously crafted firmware images
- **Status**: Recently disclosed; exploitation potential for long-term persistence

### OnePlus OxygenOS SMS Access Flaw
- **Description**: Vulnerability in multiple OnePlus OxygenOS versions allowing unauthorized SMS access
- **Impact**: Any installed app can access SMS data and metadata without user permission
- **Status**: Currently unpatched; affects multiple OnePlus device models

### SonicWall SMA Security Device Exploitation
- **Description**: Ongoing attacks against SonicWall Secure Mobile Access (SMA) devices
- **Impact**: Installation of OVERSTEP backdoor allowing system control and credential theft
- **Status**: Active exploitation by UNC6148 threat group

## Affected Systems and Products

- **GeoServer**: Geospatial software used by federal agencies and organizations
- **Cisco IOS/IOS XE**: Network operating systems on Cisco routing and switching equipment
- **Pandoc**: Document conversion utility commonly used in Linux environments
- **Libraesva ESG**: Email Security Gateway solutions in enterprise environments
- **Supermicro Hardware**: BMC firmware on Supermicro server systems
- **OnePlus Devices**: Multiple models running affected OxygenOS versions
- **SonicWall SMA**: Secure Mobile Access appliances and security devices
- **AWS EC2**: Amazon Web Services cloud instances vulnerable through Pandoc exploitation
- **NPM Ecosystem**: Node.js package manager and JavaScript supply chain

## Attack Vectors and Techniques

- **Rapid Exploitation**: Attackers exploiting disclosed vulnerabilities within two weeks of public disclosure
- **Zero-Day Exploitation**: Active use of undisclosed vulnerabilities before patches are available
- **Supply Chain Attacks**: Malicious NPM packages using steganographic QR codes for payload delivery
- **Cloud Infrastructure Targeting**: AWS IMDS exploitation through document processing vulnerabilities
- **Firmware Backdooring**: Installation of persistent backdoors through BMC firmware manipulation
- **Phishing Campaigns**: GitHub notifications abuse and fake Y Combinator invitations for cryptocurrency theft
- **Living-off-the-Land**: Use of legitimate tools and proof-of-concepts for malicious purposes

## Threat Actor Activities

- **RedNovember (Chinese APT)**: Targeting global government and private sector organizations across multiple continents using Pantegana and Cobalt Strike tools; rapid exploitation of newly disclosed vulnerabilities
- **UNC5221 (Suspected Chinese)**: Infiltrating U.S. legal and technology sectors using BRICKSTORM backdoor for long-term persistence espionage operations lasting over a year
- **UNC6148**: Deploying OVERSTEP backdoor in ongoing SonicWall SMA attacks with system control and credential theft capabilities
- **Scattered Spider**: Despite recent arrests and shutdown claims, this cybercrime group has been linked to over $115 million in ransom payments through sophisticated social engineering attacks
- **State-Sponsored Actors**: Actively exploiting Libraesva Email Security Gateway vulnerabilities for intelligence gathering and persistent access
- **RTX Ransomware Group**: Causing widespread disruptions across European airports; UK authorities have arrested a suspect linked to these attacks