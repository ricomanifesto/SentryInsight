# Exploitation Report

Critical exploitation activity is currently targeting multiple sectors with sophisticated attack techniques. The EncryptHub threat group continues exploiting a patched Microsoft Windows vulnerability to deploy Fickle Stealer malware, while Cisco has disclosed a maximum severity remote code execution flaw in its Firewall Management Center. The Crypto24 ransomware group is demonstrating advanced EDR evasion capabilities, and CISA has issued warnings about active exploitation of N-able vulnerabilities. Additionally, pro-Russian hackers have successfully compromised critical infrastructure systems, including water treatment facilities in Norway and Poland, highlighting the escalating threat to operational technology environments.

## Active Exploitation Details

### Microsoft Windows MSC EvilTwin Vulnerability
- **Description**: A security flaw in Microsoft Windows that has been patched but continues to be exploited by threat actors
- **Impact**: Allows deployment of malicious payloads including the Fickle Stealer malware
- **Status**: Patched but actively exploited by EncryptHub group

### Cisco Secure Firewall Management Center RADIUS Vulnerability
- **Description**: A critical remote code execution vulnerability in the RADIUS subsystem of Cisco's Secure Firewall Management Center software
- **Impact**: Allows attackers to execute arbitrary code on affected systems
- **Status**: Recently disclosed with maximum CVSS 10.0 severity rating, patches available
- **CVE ID**: CVE-2025-20001

### N-able Critical Vulnerabilities
- **Description**: Two critical vulnerabilities affecting N-able systems that enable local code execution and command injection
- **Impact**: Allows authenticated attackers to execute code and inject commands
- **Status**: Under active attack according to CISA warning, patches required immediately

### Plex Media Server Security Vulnerability
- **Description**: A recently patched security vulnerability affecting Plex media servers
- **Impact**: Specific impact details not disclosed, but urgent patching recommended
- **Status**: Patched, users urged to update immediately

### HTTP/2 MadeYouReset Vulnerability
- **Description**: A new attack technique affecting multiple HTTP/2 implementations that bypasses existing protections
- **Impact**: Enables large-scale denial-of-service attacks
- **Status**: Newly discovered vulnerability affecting multiple implementations

## Affected Systems and Products

- **Cisco Secure Firewall Management Center**: RADIUS subsystem vulnerability with maximum severity
- **Microsoft Windows**: MSC EvilTwin vulnerability being exploited for malware delivery
- **N-able Systems**: Critical vulnerabilities enabling code execution and command injection
- **Plex Media Servers**: Security vulnerability requiring immediate patching
- **HTTP/2 Implementations**: Multiple implementations vulnerable to MadeYouReset DoS attacks
- **Water Treatment Systems**: Critical infrastructure in Norway and Poland compromised
- **Android Devices**: ERMAC 3.0 banking trojan targeting mobile banking applications
- **Brokerage Services**: Mobile phishing attacks targeting customer accounts

## Attack Vectors and Techniques

- **EDR Evasion**: Crypto24 ransomware group using custom utilities to bypass endpoint detection and response solutions
- **Banking Trojans**: ERMAC 3.0 malware targeting Android banking applications with advanced capabilities
- **Phishing Kits**: Sophisticated mobile phishing targeting brokerage accounts in "ramp and dump" schemes
- **FIDO Bypass**: Downgrade attacks allowing phishing kits to circumvent FIDO authentication
- **Infrastructure Compromise**: Direct attacks on operational technology systems controlling water treatment facilities
- **Ransomware Deployment**: WarLock ransomware targeting telecommunications infrastructure

## Threat Actor Activities

- **EncryptHub**: Russian threat group continuing exploitation of patched Windows vulnerability to deploy Fickle Stealer malware
- **UAT-7237**: Chinese-speaking APT group targeting Taiwan web infrastructure using customized open-source hacking tools
- **Crypto24 Ransomware Group**: Targeting large organizations with custom EDR evasion tools and advanced technical capabilities
- **WarLock Ransomware**: Claimed responsibility for Colt Telecommunications attack, offering stolen data for sale
- **Pro-Russian Hackers**: Attributed to water infrastructure attacks in Norway and Poland, demonstrating capability to manipulate critical operational systems
- **Mobile Phishing Groups**: Cybercriminal organizations targeting brokerage services with sophisticated phishing kits and mobile wallet conversion techniques