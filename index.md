# Exploitation Report

Critical active exploitation is occurring across multiple attack vectors, with threat actors leveraging zero-day vulnerabilities, supply chain attacks, and persistent backdoors to compromise high-value targets. The most severe activity includes a zero-day vulnerability in Cisco IOS and IOS XE Software being exploited for remote code execution and denial-of-service attacks, alongside CVE-2024-36401 in GeoServer which enabled attackers to breach a federal agency within two weeks of disclosure. State-sponsored groups are deploying sophisticated backdoors like BRICKSTORM and OVERSTEP for long-term espionage, while cybercriminals continue exploiting supply chain weaknesses through malicious packages and payment skimmers.

## Active Exploitation Details

### Cisco IOS and IOS XE SNMP Vulnerability
- **Description**: High-severity zero-day vulnerability in Cisco IOS Software and IOS XE Software SNMP functionality
- **Impact**: Remote attackers can execute arbitrary code or trigger denial-of-service conditions
- **Status**: Currently being exploited in the wild; security updates released

### GeoServer Critical Vulnerability
- **Description**: Critical security flaw in GeoServer geospatial software
- **Impact**: Complete system compromise allowing unauthorized access to federal agency systems
- **Status**: Actively exploited less than two weeks after initial disclosure
- **CVE ID**: CVE-2024-36401

### Pandoc Linux Utility Vulnerability
- **Description**: Security flaw in Pandoc document conversion utility
- **Impact**: Attackers can target AWS Instance Metadata Service (IMDS) and steal EC2 IAM credentials
- **Status**: In-the-wild exploitation confirmed
- **CVE ID**: CVE-2025-51591

### Libraesva Email Security Gateway Vulnerability
- **Description**: Vulnerability in Libraesva Email Security Gateway solution
- **Impact**: System compromise by state-sponsored threat actors
- **Status**: Actively exploited by nation-state groups; security update released

### SonicWall SMA Device Attacks
- **Description**: Ongoing attacks against SonicWall Secure Mobile Access devices
- **Impact**: Installation of OVERSTEP backdoor for persistent access, credential theft, and activity concealment
- **Status**: Active campaign by UNC6148 threat group

## Affected Systems and Products

- **Cisco IOS and IOS XE Software**: Network infrastructure devices vulnerable to SNMP-based attacks
- **GeoServer**: Geospatial data servers used by federal civilian executive branch agencies
- **Pandoc**: Linux document conversion utility in cloud environments
- **Libraesva Email Security Gateway**: Enterprise email security solutions
- **SonicWall SMA Devices**: Secure remote access appliances
- **Supermicro Hardware**: Baseboard Management Controller (BMC) firmware vulnerabilities allowing persistent backdoors
- **OnePlus OxygenOS**: Mobile devices allowing unauthorized SMS access
- **Wondershare RepairIt**: Software with critical flaws exposing user data and AI models
- **NPM/PyPI Packages**: JavaScript and Python package repositories
- **Rust Crates**: Development libraries targeting cryptocurrency wallets

## Attack Vectors and Techniques

- **SNMP Exploitation**: Remote code execution through vulnerable Simple Network Management Protocol implementations
- **Supply Chain Poisoning**: Malicious packages in NPM, PyPI, and Rust repositories targeting developers
- **Payment Skimmer Attacks**: iframe-based overlays on checkout pages to steal credit card data
- **Steganographic Malware**: QR code-hidden malware in NPM packages for credential theft
- **Phishing Campaigns**: GitHub notifications impersonating Y Combinator for cryptocurrency theft
- **BMC Firmware Attacks**: Persistent backdoors through maliciously crafted firmware images
- **Mobile App Exploitation**: Unauthorized SMS access without user permissions

## Threat Actor Activities

- **UNC5221/UNC6148**: Suspected Chinese espionage groups deploying BRICKSTORM and OVERSTEP backdoors against U.S. legal, technology, and SaaS sectors
- **RedNovember**: Chinese APT group targeting global governments using Pantegana and Cobalt Strike tools
- **Scattered Spider**: Cybercrime group linked to $115 million in ransom payments; recent arrests of key members including 19-year-old UK national
- **State-Sponsored Groups**: Nation-state actors exploiting Libraesva Email Security Gateway vulnerabilities
- **Russian Disinformation Campaign**: Information warfare targeting Moldovan elections
- **RTX Ransomware**: Attack causing widespread European airport disruptions leading to UK arrest