# Exploitation Report

Critical exploitation activity is currently dominated by several high-severity vulnerabilities being actively exploited in the wild. Most concerning are a zero-day SNMP vulnerability in Cisco IOS systems allowing remote code execution, a GeoServer flaw that successfully breached a federal agency, and ongoing exploitation of vulnerabilities in SonicWall security devices. State-sponsored threat actors are particularly active, with Chinese APT groups deploying sophisticated backdoors and email security gateway exploits, while supply chain attacks through malicious packages continue to pose significant risks to organizations worldwide.

## Active Exploitation Details

### Cisco IOS SNMP Zero-Day Vulnerability
- **Description**: High-severity SNMP vulnerability in Cisco IOS and IOS XE Software currently being exploited in attacks
- **Impact**: Allows remote attackers to execute arbitrary code or trigger denial-of-service conditions
- **Status**: Zero-day vulnerability with active exploitation confirmed; security updates released by Cisco

### GeoServer Critical Vulnerability
- **Description**: Critical vulnerability in GeoServer that was exploited to breach a federal agency
- **Impact**: Successful breach of a large federal civilian executive branch agency using geospatial systems
- **Status**: Actively exploited less than two weeks after initial disclosure
- **CVE ID**: CVE-2024-36401

### Libraesva Email Security Gateway Vulnerability
- **Description**: Security flaw in Libraesva Email Security Gateway solution being exploited by state-sponsored actors
- **Impact**: Allows threat actors to compromise email security infrastructure
- **Status**: Active exploitation by state-sponsored groups; security update released

### Pandoc Linux Utility Vulnerability
- **Description**: Security flaw in Pandoc utility being exploited to target AWS infrastructure
- **Impact**: Enables attacks on AWS Instance Metadata Service (IMDS) to steal EC2 IAM credentials
- **Status**: In-the-wild exploitation confirmed targeting cloud environments
- **CVE ID**: CVE-2025-51591

### SonicWall SMA Vulnerability
- **Description**: Vulnerability in SonicWall security devices being exploited by threat actors
- **Impact**: Installation of OVERSTEP backdoor allowing system control, password theft, and activity concealment
- **Status**: Ongoing attacks with persistent backdoor deployment

## Affected Systems and Products

- **Cisco IOS and IOS XE Software**: SNMP-enabled devices vulnerable to remote code execution
- **GeoServer**: Geospatial systems in federal agencies and organizations
- **Libraesva Email Security Gateway**: Email security infrastructure in targeted organizations
- **Pandoc**: Linux utility in AWS cloud environments
- **SonicWall SMA Devices**: Security appliances vulnerable to backdoor installation
- **Supermicro Hardware**: BMC firmware allowing persistent backdoor creation
- **OnePlus OxygenOS**: Multiple versions allowing unauthorized SMS access
- **Wondershare RepairIt**: Software exposing user data and AI models

## Attack Vectors and Techniques

- **SNMP Exploitation**: Remote attackers leveraging SNMP vulnerabilities for code execution
- **Supply Chain Attacks**: Malicious Rust crates impersonating legitimate libraries to steal cryptocurrency wallet keys
- **Email Gateway Compromise**: State-sponsored actors exploiting email security solutions
- **Cloud Metadata Attacks**: Exploitation of Pandoc to access AWS instance metadata and steal credentials
- **Backdoor Installation**: Deployment of OVERSTEP and BRICKSTORM backdoors for persistent access
- **Phishing Campaigns**: GitHub notifications abused to impersonate Y Combinator for cryptocurrency theft
- **Package Repository Attacks**: Malicious npm packages hiding malware in steganographic QR codes

## Threat Actor Activities

- **UNC6148**: Attacking SonicWall devices with OVERSTEP backdoor deployment
- **UNC5221**: Using BRICKSTORM backdoor to infiltrate U.S. legal and technology sectors
- **RedNovember**: Chinese APT group targeting global governments with Pantegana and Cobalt Strike
- **Scattered Spider**: Cybercrime group linked to $115 million in ransom payments, with recent member arrests
- **Chinese State-Sponsored Groups**: Exploiting Libraesva email security gateways and conducting long-term espionage operations
- **RTX Ransomware Operators**: Causing widespread airport disruptions across Europe
- **Cryptocurrency Thieves**: Deploying malicious Rust crates with 8,424 confirmed downloads targeting Solana and Ethereum wallets