# Exploitation Report

A significant wave of active exploitations is targeting critical infrastructure and enterprise systems across multiple platforms. The most concerning activities include the exploitation of CVE-2025-55182 in Next.js environments affecting 766 hosts for credential harvesting, active zero-day attacks against TrueConf conference servers enabling malicious software updates, and the ongoing exploitation of F5 BIG-IP APM instances with over 14,000 systems still vulnerable to remote code execution attacks. Additionally, threat actors are leveraging the DarkSword exploit kit against iOS devices and exploiting critical Cisco IMC authentication bypass vulnerabilities to gain administrative access to enterprise systems.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: A vulnerability in Next.js hosting environments being actively exploited for large-scale credential harvesting operations
- **Impact**: Attackers can steal database credentials, SSH private keys, and Amazon Web Services access tokens from compromised hosts
- **Status**: Active exploitation observed against 766 Next.js hosts in ongoing campaigns
- **CVE ID**: CVE-2025-55182

### TrueConf Conference Server Zero-Day
- **Description**: An unpatched vulnerability in TrueConf conference servers allowing remote code execution through malicious software updates
- **Impact**: Enables attackers to execute arbitrary files on all endpoints connected to compromised conference servers
- **Status**: Active zero-day exploitation with malicious software updates being pushed to connected clients

### F5 BIG-IP APM Remote Code Execution
- **Description**: Critical vulnerability in F5 BIG-IP Application Policy Manager instances enabling remote code execution
- **Impact**: Complete system compromise with remote code execution capabilities
- **Status**: Over 14,000 instances remain exposed and vulnerable to ongoing attacks despite patch availability

### Cisco IMC Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Cisco Integrated Management Controller with CVSS score of 9.8
- **Impact**: Unauthenticated remote attackers can gain administrative access to management systems
- **Status**: Recently patched but exploitation capabilities confirmed

### DarkSword iOS Exploit Kit
- **Description**: Advanced exploit kit targeting iOS devices through various attack vectors
- **Impact**: Device compromise and potential data exfiltration from targeted iOS devices
- **Status**: Active exploitation prompting Apple to expand security update availability to more devices

### Progress ShareFile Pre-Authentication RCE
- **Description**: Chain of vulnerabilities in Progress ShareFile enabling unauthenticated remote code execution
- **Impact**: Pre-authentication file exfiltration and potential system compromise
- **Status**: Newly discovered vulnerabilities that can be chained for complete system compromise

## Affected Systems and Products

- **Next.js Hosting Platforms**: 766 confirmed compromised hosts with credential theft operations
- **TrueConf Conference Servers**: All versions vulnerable to zero-day exploitation for malicious updates
- **F5 BIG-IP APM**: Over 14,000 internet-exposed instances vulnerable to RCE attacks
- **Cisco IMC Systems**: Integrated Management Controller instances across enterprise environments
- **iOS Devices**: iPhone and iPad devices targeted by DarkSword exploit kit
- **Progress ShareFile**: Enterprise-grade secure file transfer solutions vulnerable to pre-auth attacks
- **Android Devices**: 2.3 million devices infected through NoVoice malware on Google Play Store

## Attack Vectors and Techniques

- **Credential Harvesting**: Large-scale operations targeting database credentials, SSH keys, and cloud access tokens through React2Shell exploitation
- **Malicious Software Updates**: Zero-day exploitation of conference servers to push arbitrary code to connected endpoints
- **Authentication Bypass**: Critical bypass techniques targeting enterprise management controllers
- **Pre-Authentication Attacks**: Chained vulnerability exploitation enabling unauthenticated system access
- **Mobile Malware Distribution**: Android rootkit distribution through legitimate app stores affecting millions of devices
- **Device Code Phishing**: EvilTokens service facilitating Microsoft account hijacking through device code manipulation
- **Proxy Evasion**: Residential proxy networks evading IP reputation systems in 78% of analyzed sessions

## Threat Actor Activities

- **REF1695 Operation**: Financially motivated campaign using fake ISO installers to deploy RATs and cryptocurrency miners since November 2023
- **Vidar Malware Distributors**: Exploiting Claude Code source code leaks to distribute information-stealing malware via fake GitHub repositories
- **Augmented Marauder**: Multipronged banking trojan campaigns targeting Spanish-speaking users with Casbaneiro malware
- **Iranian-Linked Groups**: Claiming responsibility for data-wiping attacks against major corporations including Stryker Corporation
- **DeFi Protocol Attackers**: Sophisticated operation seizing Security Council powers to steal $280 million from Drift Protocol
- **NoVoice Malware Authors**: Android malware campaign affecting 2.3 million devices through Google Play Store distribution
- **WhatsApp Spyware Operators**: Targeting approximately 200 users with fake iOS apps containing spyware, linked to Italian firm activities