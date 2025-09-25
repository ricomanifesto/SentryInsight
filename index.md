# Exploitation Report

Critical exploitation activity has been observed across multiple platforms and systems, with several zero-day vulnerabilities being actively exploited in the wild. Most notably, Cisco has warned of active exploitation of a high-severity SNMP vulnerability in IOS and IOS XE Software that allows remote code execution or denial-of-service attacks. Federal agencies have been compromised through the GeoServer vulnerability CVE-2024-36401, which was exploited less than two weeks after disclosure. State-sponsored threat actors are actively exploiting vulnerabilities in Libraesva Email Security Gateway systems, while the Pandoc utility vulnerability CVE-2025-51591 is being leveraged to target AWS infrastructure and steal EC2 IAM credentials. These incidents demonstrate sophisticated attackers' ability to rapidly weaponize newly disclosed vulnerabilities for high-impact compromises.

## Active Exploitation Details

### Cisco IOS/IOS XE SNMP Zero-Day Vulnerability
- **Description**: A high-severity vulnerability in Cisco IOS Software and IOS XE Software's SNMP implementation that allows remote attackers to execute arbitrary code or cause denial-of-service conditions
- **Impact**: Remote code execution capabilities and system disruption through DoS attacks
- **Status**: Currently being actively exploited in attacks; security updates have been released

### GeoServer Critical Vulnerability
- **Description**: A critical security flaw in GeoServer that enables unauthorized system access
- **Impact**: Complete compromise of affected federal agency systems and potential access to sensitive geospatial data
- **Status**: Actively exploited within two weeks of disclosure to compromise a large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Libraesva Email Security Gateway Vulnerability
- **Description**: A security vulnerability in Libraesva's Email Security Gateway (ESG) solution being exploited by state-sponsored actors
- **Impact**: Compromise of email security infrastructure and potential access to sensitive communications
- **Status**: Actively exploited by state-sponsored threat actors; security update released

### Pandoc Server-Side Request Forgery Vulnerability
- **Description**: A vulnerability in the Pandoc Linux utility that allows server-side request forgery attacks
- **Impact**: Access to AWS Instance Metadata Service (IMDS) and theft of EC2 IAM credentials
- **Status**: In-the-wild exploitation confirmed targeting AWS infrastructure
- **CVE ID**: CVE-2025-51591

### SonicWall SMA Device Vulnerability
- **Description**: Ongoing attacks against SonicWall security devices through exploitation of unspecified vulnerabilities
- **Impact**: Installation of OVERSTEP backdoor allowing system control, credential theft, and activity concealment
- **Status**: Actively exploited by threat actor UNC6148

## Affected Systems and Products

- **Cisco IOS Software**: All versions with SNMP functionality enabled
- **Cisco IOS XE Software**: All versions with SNMP functionality enabled
- **GeoServer**: Geospatial server software used by federal agencies
- **Libraesva Email Security Gateway**: Email security appliances in enterprise environments
- **Pandoc**: Linux utility used for document conversion
- **AWS EC2 Instances**: Cloud infrastructure running vulnerable Pandoc installations
- **SonicWall SMA Devices**: Secure mobile access appliances
- **Supermicro BMC Firmware**: Baseboard Management Controller systems
- **OnePlus OxygenOS**: Multiple versions of OnePlus mobile operating system

## Attack Vectors and Techniques

- **SNMP Exploitation**: Remote attackers leveraging SNMP protocol vulnerabilities for RCE
- **Server-Side Request Forgery**: Pandoc vulnerability exploited to access AWS metadata services
- **Supply Chain Attacks**: Malicious Rust crates impersonating legitimate libraries to steal cryptocurrency wallet keys
- **Backdoor Installation**: OVERSTEP backdoor deployment on compromised SonicWall devices
- **Steganographic QR Codes**: NPM packages hiding malware in obfuscated QR codes
- **Payment Skimmer Overlays**: Sophisticated iframe manipulation techniques bypassing security controls
- **Phishing Campaigns**: GitHub notifications abused to impersonate Y Combinator for cryptocurrency theft

## Threat Actor Activities

- **UNC6148**: Deploying OVERSTEP backdoors in ongoing SonicWall SMA attacks with capabilities for system control and credential theft
- **RedNovember (Chinese APT)**: Targeting global governments using Pantegana and Cobalt Strike tools, leveraging open-source software and proof-of-concepts
- **UNC5221**: Using BRICKSTORM backdoor to infiltrate U.S. legal and technology sectors in long-term espionage operations
- **Scattered Spider**: Core members charged in connection with $115 million in ransom payments, though group claims to have shut down
- **State-Sponsored Actors**: Actively exploiting Libraesva Email Security Gateway vulnerabilities for intelligence gathering
- **Cybercrime Rings**: International operations resulting in law enforcement seizure of $439 million in stolen assets