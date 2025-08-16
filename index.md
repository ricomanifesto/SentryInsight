# Exploitation Report

Critical exploitation activity is currently targeting multiple sectors with sophisticated attack techniques. The EncryptHub threat group continues exploiting a patched Microsoft Windows vulnerability to deploy Fickle Stealer malware, while Cisco has disclosed a maximum severity remote code execution flaw in its Firewall Management Center. The Crypto24 ransomware group is demonstrating advanced EDR evasion capabilities, and CISA has issued warnings about active exploitation of N-able vulnerabilities. Additionally, pro-Russian hackers have successfully compromised critical infrastructure, including water systems in Norway and Poland, while the UAT-7237 APT group targets Taiwan's web infrastructure using customized open-source tools.

## Active Exploitation Details

### Microsoft Windows MSC EvilTwin Vulnerability
- **Description**: A security flaw in Microsoft Windows that allows threat actors to deploy malicious payloads
- **Impact**: Enables deployment of information-stealing malware including Fickle Stealer
- **Status**: Patched but continues to be exploited by EncryptHub group

### Cisco Secure Firewall Management Center RADIUS Vulnerability
- **Description**: Critical remote code execution vulnerability in the RADIUS subsystem of Cisco's FMC software with maximum CVSS 10.0 severity rating
- **Impact**: Allows attackers to execute arbitrary code on affected systems
- **Status**: Security updates released by Cisco
- **CVE ID**: CVE-2025-20001

### N-able Critical Vulnerabilities
- **Description**: Two critical vulnerabilities enabling local code execution and command injection
- **Impact**: Allows authenticated attackers to execute code and inject commands
- **Status**: Under active attack according to CISA warning, patches available

### HTTP/2 MadeYouReset Vulnerability
- **Description**: Attack technique affecting multiple HTTP/2 implementations that bypasses existing DoS protections
- **Impact**: Enables large-scale denial-of-service attacks
- **Status**: Newly discovered vulnerability affecting various implementations

### Plex Media Server Security Vulnerability
- **Description**: Recently patched security vulnerability in Plex media servers
- **Impact**: Specific impact details not disclosed, but urgent patching recommended
- **Status**: Patched, users urged to update immediately

## Affected Systems and Products

- **Cisco Secure Firewall Management Center**: RADIUS subsystem vulnerability with maximum severity
- **Microsoft Windows**: MSC EvilTwin vulnerability being exploited for malware deployment
- **N-able Products**: Critical vulnerabilities under active exploitation
- **HTTP/2 Implementations**: Multiple implementations vulnerable to MadeYouReset DoS attacks
- **Plex Media Servers**: Security vulnerability requiring immediate patching
- **Android Devices**: ERMAC 3.0 banking trojan targeting mobile banking applications
- **Taiwan Web Infrastructure**: Targeted by UAT-7237 APT group using customized tools
- **Water Treatment Systems**: Critical infrastructure in Norway and Poland compromised

## Attack Vectors and Techniques

- **EDR Evasion**: Crypto24 ransomware employs custom utilities to bypass endpoint detection and response solutions
- **Banking Trojan Distribution**: ERMAC 3.0 source code leak exposes full malware infrastructure for Android banking attacks
- **Phishing Kit Evolution**: Mobile phishers targeting brokerage accounts using sophisticated "ramp and dump" cashout schemes
- **FIDO Bypass**: Downgrade attacks allowing phishing kits to circumvent FIDO authentication mechanisms
- **Infrastructure Compromise**: Direct attacks on critical water treatment and dam control systems
- **Open-Source Tool Customization**: APT groups modifying legitimate tools for malicious purposes

## Threat Actor Activities

- **EncryptHub**: Russian threat group continuing exploitation of patched Windows vulnerability to deploy Fickle Stealer malware
- **Crypto24 Ransomware Group**: Targeting large organizations with custom EDR evasion tools and data exfiltration capabilities
- **UAT-7237**: Chinese-speaking APT actor targeting Taiwan web infrastructure using customized open-source hacking tools for long-term persistence
- **WarLock Ransomware**: Claimed responsibility for Colt Telecommunications attack, offering stolen data for sale
- **Pro-Russian Hackers**: Conducting sabotage operations against water infrastructure in Norway and Poland, including dam control system manipulation
- **Mobile Phishing Groups**: Shifting focus to brokerage account targeting with sophisticated phishing kits and mobile wallet integration
- **Government Email Compromisers**: Selling live access to police and government email systems on dark web marketplaces