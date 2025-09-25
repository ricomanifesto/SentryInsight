# Exploitation Report

Current exploitation activity reveals critical zero-day vulnerabilities being actively targeted by threat actors across multiple platforms. Cisco has confirmed active exploitation of a high-severity zero-day in IOS and IOS XE software, while attackers are leveraging CVE-2025-51591 in Pandoc to target AWS infrastructure and steal IAM credentials. State-sponsored threat actors are exploiting a Libraesva Email Security Gateway vulnerability, and sophisticated groups like UNC5221 continue using the BRICKSTORM backdoor for long-term persistence operations against U.S. organizations. Additional vulnerabilities in Supermicro BMC firmware and OnePlus OxygenOS further expand the attack surface for malicious actors.

## Active Exploitation Details

### Cisco IOS Zero-Day Vulnerability
- **Description**: A high-severity zero-day vulnerability affecting Cisco IOS and IOS XE Software
- **Impact**: Allows attackers to exploit network infrastructure devices running Cisco's operating systems
- **Status**: Currently being exploited in active attacks; Cisco has released security updates to address the vulnerability

### Pandoc Server-Side Request Forgery
- **Description**: A vulnerability in the Pandoc Linux utility that enables server-side request forgery attacks
- **Impact**: Attackers can infiltrate Amazon Web Services infrastructure, target AWS Instance Metadata Service (IMDS), and steal EC2 IAM credentials
- **Status**: Active in-the-wild exploitation confirmed by cloud security researchers
- **CVE ID**: CVE-2025-51591

### Libraesva Email Security Gateway Vulnerability
- **Description**: A security flaw in Libraesva's Email Security Gateway (ESG) solution
- **Impact**: Enables unauthorized access and compromise of email security infrastructure
- **Status**: Actively exploited by state-sponsored threat actors; security update released by Libraesva

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two vulnerabilities affecting Supermicro Baseboard Management Controller (BMC) firmware
- **Impact**: Allow attackers to update systems with maliciously crafted firmware images, creating persistent backdoors in hardware infrastructure
- **Status**: Newly discovered vulnerabilities with potential for widespread impact

### OnePlus OxygenOS SMS Access Flaw
- **Description**: A vulnerability in multiple OnePlus OxygenOS versions affecting SMS data access controls
- **Impact**: Allows any installed application to access SMS data and metadata without requiring permissions or user interaction
- **Status**: Currently unpatched vulnerability affecting OnePlus mobile devices

## Affected Systems and Products

- **Cisco IOS and IOS XE Software**: Network infrastructure devices running affected operating system versions
- **Pandoc Utility**: Linux systems utilizing the Pandoc document converter, particularly in AWS environments
- **Libraesva Email Security Gateway**: Organizations using ESG solutions for email security
- **Supermicro Hardware**: Systems with vulnerable BMC firmware implementations
- **OnePlus Devices**: Multiple OxygenOS versions across OnePlus smartphone lineup
- **Amazon Web Services**: EC2 instances and IAM credential systems targeted through Pandoc exploitation

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in critical network infrastructure
- **Server-Side Request Forgery**: Leveraging Pandoc vulnerability to make unauthorized requests to AWS IMDS
- **Firmware Manipulation**: Crafting malicious firmware images to establish persistent hardware-level backdoors
- **Privilege Escalation**: Exploiting SMS access controls to gain unauthorized data access on mobile devices
- **Cloud Infrastructure Targeting**: Sophisticated attacks against cloud service providers and their metadata services
- **Supply Chain Compromise**: Using legitimate cloud-native tools and infrastructure for malicious purposes

## Threat Actor Activities

- **State-Sponsored Groups**: Actively exploiting Libraesva Email Security Gateway vulnerabilities for espionage and intelligence gathering operations
- **UNC5221 (China-Nexus)**: Deploying BRICKSTORM backdoor malware for long-term persistence against U.S. legal services, SaaS providers, and technology sectors
- **UNC6148**: Installing OVERSTEP backdoor in SonicWall SMA devices to maintain system control and credential theft capabilities
- **RedNovember (Chinese APT)**: Targeting global government and private sector organizations using Pantegana and Cobalt Strike tools across multiple continents
- **Scattered Spider Members**: Recent law enforcement activities with arrests of key members, though group operations continue despite claimed shutdown
- **Cloud-Focused Attackers**: Leveraging Pandoc CVE-2025-51591 for AWS infrastructure compromise and credential harvesting operations