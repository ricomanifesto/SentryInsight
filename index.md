# Exploitation Report

Current cybersecurity activity reveals several critical zero-day exploits and active vulnerability campaigns targeting organizations worldwide. Microsoft has restricted Internet Explorer mode in Edge browser after discovering hackers are exploiting zero-day vulnerabilities in the Chakra JavaScript engine to gain unauthorized access to target systems. Meanwhile, threat actors are actively exploiting a newly disclosed Oracle E-Business Suite vulnerability that allows unauthorized access to sensitive data without authentication. Additional concerning activity includes the RondoDox botnet campaign weaponizing over 50 vulnerabilities across 30+ vendors, Chinese state hackers maintaining year-long persistence through ArcGIS exploitation, and a new Android side-channel attack called Pixnapping that enables theft of 2FA codes without requiring permissions.

## Active Exploitation Details

### Chakra JavaScript Engine Zero-Day
- **Description**: Zero-day vulnerabilities in Microsoft's Chakra JavaScript engine used in Internet Explorer mode within Edge browser
- **Impact**: Allows hackers to gain unauthorized access to target devices and systems
- **Status**: Microsoft has restricted access to IE mode after receiving credible reports of active exploitation in August 2025

### Oracle E-Business Suite Vulnerability
- **Description**: Security flaw in Oracle's E-Business Suite that allows unauthorized access to sensitive data
- **Impact**: Attackers can access sensitive organizational data without authentication
- **Status**: Oracle issued emergency security update over the weekend to patch the vulnerability

### RMPocalypse AMD SEV-SNP Flaw
- **Description**: Security vulnerability that undermines confidential computing guarantees in AMD's Secure Encrypted Virtualization with Secure Nested Paging
- **Impact**: Single 8-byte write can shatter confidential computing protections
- **Status**: AMD has released fixes to address the vulnerability

### Pixnapping Android Side-Channel Attack
- **Description**: Side-channel attack affecting Android devices from Google and Samsung
- **Impact**: Allows covert theft of two-factor authentication codes, Google Maps timelines, and other sensitive data without requiring permissions
- **Status**: Newly discovered vulnerability with ongoing research

### Framework UEFI Secure Boot Bypass
- **Description**: Signed UEFI shell components in Framework laptops that can bypass Secure Boot protections
- **Impact**: Could allow attackers to compromise boot integrity and bypass security controls
- **Status**: Affects around 200,000 Linux Framework systems

## Affected Systems and Products

- **Microsoft Edge Browser**: Internet Explorer mode functionality compromised by Chakra engine exploits
- **Oracle E-Business Suite**: Enterprise business applications vulnerable to unauthorized data access
- **AMD Processors**: SEV-SNP confidential computing features affected by RMPocalypse
- **Android Devices**: Google and Samsung devices vulnerable to Pixnapping side-channel attacks
- **Framework Laptops**: Approximately 200,000 Linux systems with Secure Boot bypass risk
- **ArcGIS Geo-Mapping Tool**: Components weaponized as web shells for persistent access
- **SonicWall SSL VPN**: Over 100 accounts compromised using stolen credentials
- **npm, PyPI, and RubyGems**: Malicious packages across multiple software ecosystems
- **Windows 10**: End of support status creates ongoing vulnerability exposure

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Chakra JavaScript engine
- **Web Shell Deployment**: Chinese hackers converting ArcGIS components into persistent backdoors
- **Credential Stuffing**: Large-scale attacks against SonicWall VPN services using stolen credentials
- **Supply Chain Attacks**: Malicious packages in software repositories using Discord for command and control
- **Botnet Operations**: RondoDox leveraging 50+ vulnerabilities across multiple vendors simultaneously
- **Side-Channel Attacks**: Pixnapping technique bypassing Android permission models
- **Phishing Campaigns**: TA585 threat actor delivering MonsterV2 malware through email campaigns
- **RDP Brute Force**: Multi-country botnet targeting Remote Desktop Protocol services from 100,000+ IP addresses

## Threat Actor Activities

- **Chinese State Hackers**: Maintained undetected access for over one year using weaponized ArcGIS geo-mapping components as web shells
- **TA585 Threat Actor**: Conducting phishing campaigns to deliver MonsterV2 off-the-shelf malware with advanced capabilities
- **Clop Ransomware Gang**: Listed Harvard University on leak site following exploitation of Oracle zero-day vulnerability
- **RondoDox Operators**: Running extensive botnet campaign exploiting vulnerabilities across 30+ vendors in "exploit shopping mall" approach
- **Unknown Threat Actors**: Actively exploiting Internet Explorer mode zero-days, prompting Microsoft's emergency restrictions
- **Multi-National Botnet**: Coordinating attacks against US RDP services from over 100,000 IP addresses across multiple countries
- **Astaroth Banking Trojan Group**: Using GitHub infrastructure to maintain operations resilience after takedowns
- **ChaosBot Operators**: Deploying Rust-based backdoor using Discord channels for command and control communications