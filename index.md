# Exploitation Report

Current exploitation activity reveals several critical security threats across multiple platforms and systems. The most significant concerns include active exploitation of a WinRAR vulnerability affecting file archiver systems, Microsoft addressing multiple zero-day vulnerabilities with one already being exploited in the wild, and widespread exploitation of the React2Shell vulnerability in React Server Components. Additionally, threat actors are leveraging sophisticated malware campaigns including AMOS infostealer targeting macOS systems, DroidLock ransomware affecting Android devices, and Storm-0249's abuse of EDR processes for stealthy attacks. The landscape also shows increased activity from North Korean-linked actors deploying new malware variants and pro-Russia hacktivist groups targeting critical infrastructure systems.

## Active Exploitation Details

### WinRAR Vulnerability
- **Description**: Security flaw impacting the WinRAR file archiver and compression utility that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Multiple threat groups are actively exploiting this vulnerability to compromise systems
- **Status**: Under active attack by multiple threat groups, patches available
- **CVE ID**: CVE-2025-6218

### Microsoft Zero-Day Vulnerabilities
- **Description**: Microsoft addressed 56-57 security flaws including multiple zero-day vulnerabilities in Windows platforms and supported software
- **Impact**: One zero-day is being actively exploited in the wild, allowing attackers to compromise Windows systems
- **Status**: Actively exploited, patches released in December 2025 Patch Tuesday
- **CVE ID**: Not specified in articles

### React2Shell Vulnerability
- **Description**: Maximum-severity security flaw in React Server Components (RSC) enabling remote code execution
- **Impact**: Threat actors leverage this vulnerability to deliver cryptocurrency miners, EtherRAT malware, and other malicious payloads across multiple sectors
- **Status**: Continues to witness heavy exploitation across various threat groups including North Korea-linked actors
- **CVE ID**: Not specified in articles

### .NET SOAPwn Flaw
- **Description**: Exploitation primitives in the .NET Framework that can be leveraged against enterprise-grade applications
- **Impact**: Achieves remote code execution and file writes via rogue WSDL
- **Status**: Research disclosed, exploitation techniques identified
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **WinRAR File Archiver**: Compression utility vulnerable to active exploitation by multiple threat groups
- **Microsoft Windows**: Multiple versions affected by zero-day vulnerabilities requiring December 2025 patches
- **React Server Components**: Systems using RSC affected by critical remote code execution vulnerability
- **macOS Systems**: Targeted by AMOS infostealer malware through malicious Google ads
- **Android Devices**: Affected by DroidLock ransomware capable of screen locking and data access
- **FortiOS, FortiWeb, FortiProxy, FortiSwitchManager**: Critical authentication bypass vulnerabilities in Fortinet products
- **SAP Products**: Multiple products affected by three critical vulnerabilities
- **PCIe 5.0+ Systems**: Three security vulnerabilities in PCIe Integrity and Data Encryption protocol
- **Docker Hub Images**: Over 10,000 container images exposing credentials and authentication keys

## Attack Vectors and Techniques

- **SEO Poisoning**: Malicious Google search ads directing users to fake ChatGPT and Grok conversations leading to AMOS infostealer installation
- **ClickFix Social Engineering**: Combining SEO poisoning and legitimate AI domains for malware delivery
- **EDR Process Abuse**: Storm-0249 weaponizing endpoint detection and response platforms for stealthy attacks
- **Ransomware Screen Locking**: DroidLock malware locks Android screens demanding ransom payments
- **VNC Connection Compromise**: Pro-Russia hacktivists targeting virtual network computing connections in operational technology systems
- **Packer-as-a-Service**: Shanya service providing malware obfuscation to help ransomware actors evade detection
- **Phishing Kits**: Spiderman phishing service creating pixel-perfect cloned sites targeting European banks
- **Supply Chain Attacks**: Exploitation of development tools, compromised credentials, and malicious NPM packages

## Threat Actor Activities

- **Storm-0249**: Initial access broker conducting high-precision attacks by weaponizing EDR platforms and Windows utilities
- **North Korean-linked Actors**: Exploiting React2Shell vulnerability to deploy previously undocumented EtherRAT malware
- **Pro-Russia Hacktivist Groups**: Targeting US critical infrastructure including water systems, election systems, and nuclear facilities through VNC compromises
- **Ukrainian National**: Charged for role in cyberattacks targeting critical infrastructure worldwide in collaboration with Russian hacktivist groups
- **Multiple Threat Groups**: Actively exploiting WinRAR vulnerability for system compromise
- **GrayBravo**: Expanding malware service infrastructure with four distinct threat clusters using CastleLoader
- **AMOS Campaign Operators**: Abusing Google search advertisements to distribute macOS infostealer malware through fake AI conversation guides
- **Ransomware Actors**: Utilizing Shanya packer-as-a-service to obfuscate malware and evade endpoint detection systems