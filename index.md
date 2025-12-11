# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems with active campaigns leveraging both zero-day vulnerabilities and recently disclosed flaws. The most significant threats include active exploitation of WinRAR vulnerability CVE-2025-6218 by multiple threat groups, Microsoft addressing three zero-day vulnerabilities with one being actively exploited, and widespread exploitation of the React2Shell flaw in React Server Components by North Korean-linked actors deploying new EtherRAT malware. Additional critical concerns include Fortinet authentication bypass vulnerabilities, SAP critical security flaws, and sophisticated social engineering campaigns using AI chatbot platforms to distribute malware across macOS and Android systems.

## Active Exploitation Details

### WinRAR Security Vulnerability
- **Description**: Critical security flaw in the WinRAR file archiver and compression utility that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Multiple threat groups are actively exploiting this vulnerability for malicious purposes
- **Status**: Under active attack by multiple threat groups
- **CVE ID**: CVE-2025-6218

### Microsoft Zero-Day Vulnerabilities
- **Description**: Three zero-day vulnerabilities addressed in Microsoft's December 2025 Patch Tuesday, with one being actively exploited in the wild
- **Impact**: Active exploitation allowing unauthorized access and potential system compromise
- **Status**: Patches available but exploitation ongoing in the wild

### React2Shell Critical Flaw
- **Description**: Maximum-severity security flaw in React Server Components (RSC) enabling remote code execution
- **Impact**: Delivery of cryptocurrency miners, new malware variants including EtherRAT, and system compromise across multiple sectors
- **Status**: Heavy exploitation ongoing by various threat actors including North Korean-linked groups

### .NET SOAPwn Vulnerability
- **Description**: Exploitation primitives in the .NET Framework that can be leveraged against enterprise-grade applications
- **Impact**: Remote code execution through file writes via rogue WSDL files
- **Status**: Research disclosed with potential for active exploitation

### PCIe Encryption Weaknesses
- **Description**: Three security vulnerabilities in the PCIe Integrity and Data Encryption (IDE) protocol specification
- **Impact**: Exposure of PCIe 5.0+ systems to faulty data handling by local attackers
- **Status**: Newly disclosed vulnerabilities affecting modern systems

## Affected Systems and Products

- **WinRAR**: File archiver and compression utility actively targeted
- **Microsoft Windows**: Multiple products across the Windows platform with 57 vulnerabilities patched
- **React Server Components**: Web applications using RSC framework
- **FortiOS, FortiWeb, FortiProxy, FortiSwitchManager**: Critical authentication bypass vulnerabilities
- **SAP Products**: Multiple SAP products with three critical-severity flaws
- **macOS Systems**: Targeted by AMOS infostealer campaigns through malicious Google ads
- **Android Devices**: DroidLock ransomware targeting Android systems
- **Docker Hub**: Over 10,000 container images exposing credentials and authentication keys
- **PCIe 5.0+ Systems**: Modern systems with advanced PCIe encryption protocols

## Attack Vectors and Techniques

- **Social Engineering via AI Platforms**: Malicious Google ads impersonating ChatGPT and Grok conversations to deliver AMOS infostealer
- **ClickFix Style Attacks**: Combining SEO poisoning and legitimate AI domains for malware delivery
- **EDR Process Abuse**: Storm-0249 weaponizing endpoint detection and response platforms and Windows utilities
- **Phishing-as-a-Service**: Spiderman phishing kit targeting European banks and cryptocurrency holders
- **VNC Connection Compromise**: Pro-Russian hactivists targeting critical infrastructure through virtual network computing vulnerabilities
- **Supply Chain Exploitation**: Attackers exploiting development tools, compromised credentials, and malicious NPM packages
- **Container Image Poisoning**: Credential exposure through misconfigured Docker Hub images

## Threat Actor Activities

- **Storm-0249**: Initial access broker conducting high-precision attacks by abusing EDR processes and Windows utilities in stealthy operations
- **North Korean-Linked Actors**: Exploiting React2Shell vulnerability to deploy new EtherRAT malware and other previously undocumented tools
- **Pro-Russian Hactivists**: Targeting US critical infrastructure including water systems, election systems, and nuclear facilities through VNC connection compromises
- **Ukrainian National**: Charged for assisting Russian hacktivist groups in cyberattacks against critical infrastructure worldwide
- **Multiple Threat Groups**: Actively exploiting WinRAR CVE-2025-6218 for various malicious campaigns
- **GrayBravo**: Expanding malware service infrastructure with four distinct threat clusters using CastleLoader
- **AMOS Campaign Operators**: Conducting sophisticated social engineering campaigns through Google ads targeting macOS users
- **DroidLock Operators**: Deploying new Android ransomware with screen locking and data exfiltration capabilities