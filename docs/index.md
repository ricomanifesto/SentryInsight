# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, with threat actors leveraging a range of attack vectors from zero-day exploits to social engineering campaigns. The most significant activity involves the WinRAR vulnerability CVE-2025-6218, which multiple threat groups are actively exploiting. Microsoft's December 2025 Patch Tuesday addressed 57 flaws including three zero-days, with one being actively exploited in the wild. The React2Shell vulnerability continues to see heavy exploitation, with North Korea-linked actors deploying new EtherRAT malware. Additionally, critical authentication bypass vulnerabilities in Fortinet FortiCloud SSO and remote code execution flaws in .NET Framework are creating significant security risks for enterprise environments.

## Active Exploitation Details

### WinRAR File Archiver Vulnerability
- **Description**: Security flaw in the WinRAR file archiver and compression utility that is being actively exploited by multiple threat groups
- **Impact**: Allows attackers to compromise systems through malicious archive files
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog, indicating active exploitation
- **CVE ID**: CVE-2025-6218

### Microsoft Windows Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Microsoft Windows platform that has been actively exploited in the wild
- **Impact**: Allows attackers to compromise Windows systems through unknown attack vectors
- **Status**: Patched in December 2025 Patch Tuesday, but was actively exploited before patch release
- **CVE ID**: Not specified in the articles

### React2Shell Vulnerability
- **Description**: Maximum-severity security flaw in React Server Components (RSC) that continues to witness heavy exploitation
- **Impact**: Enables delivery of cryptocurrency miners, EtherRAT malware, and other malicious payloads across multiple sectors
- **Status**: Actively exploited by North Korea-linked actors and other threat groups
- **CVE ID**: Not specified in the articles

### .NET SOAPwn Vulnerability
- **Description**: Exploitation primitives in the .NET Framework that could be leveraged against enterprise-grade applications
- **Impact**: Achieves remote code execution and arbitrary file writes via rogue WSDL files
- **Status**: Newly disclosed research showing exploitation potential
- **CVE ID**: Not specified in the articles

### Fortinet FortiCloud SSO Authentication Bypass
- **Description**: Critical vulnerabilities in FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager
- **Impact**: Allows attackers to bypass FortiCloud SSO authentication mechanisms
- **Status**: Security updates released to address the flaws
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **WinRAR**: File archiver and compression utility affected by actively exploited vulnerability
- **Microsoft Windows**: Various versions affected by zero-day vulnerabilities and 57 total security flaws
- **React Server Components**: Web applications using RSC framework vulnerable to maximum-severity exploit
- **.NET Framework**: Enterprise applications using .NET vulnerable to remote code execution
- **Fortinet Products**: FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager affected by authentication bypass
- **macOS Systems**: Targeted by AMOS infostealer malware through malicious Google ads
- **Android Devices**: Affected by DroidLock ransomware malware
- **Docker Hub Images**: Over 10,000 container images exposing credentials and authentication keys
- **PCIe 5.0+ Systems**: Vulnerable to data handling issues due to encryption weaknesses

## Attack Vectors and Techniques

- **Malicious Archive Files**: WinRAR vulnerability exploited through crafted archive files
- **Social Engineering with AI Platforms**: Fake ChatGPT and Grok conversation guides used to distribute AMOS infostealer
- **Google Ad Poisoning**: Search engine optimization poisoning combined with malicious advertisements
- **EDR Process Abuse**: Storm-0249 threat group weaponizing endpoint detection and response platforms
- **Rogue WSDL Files**: .NET applications targeted through malicious Web Services Description Language files
- **Compromised VNC Connections**: Pro-Russian hacktivist groups targeting virtual network computing in OT systems
- **Ransomware Screen Locking**: DroidLock malware using device screen locking for ransom demands
- **Container Image Exploitation**: Exposed credentials in Docker Hub images creating attack opportunities
- **Phishing Kit Operations**: Spiderman phishing service creating pixel-perfect cloned banking sites

## Threat Actor Activities

- **Multiple Threat Groups**: Actively exploiting WinRAR CVE-2025-6218 vulnerability
- **North Korea-linked Actors**: Exploiting React2Shell vulnerability to deploy EtherRAT malware and cryptocurrency miners
- **Storm-0249**: Initial access broker conducting high-precision attacks using EDR process abuse
- **Pro-Russian Hacktivist Groups**: Targeting US critical infrastructure through compromised VNC connections in operational technology systems
- **Ukrainian National**: Charged for assisting Russian hacktivist groups in cyberattacks against critical infrastructure including water systems, election systems, and nuclear facilities
- **GrayBravo**: Expanding malware service infrastructure with CastleLoader being used by four distinct threat clusters
- **AMOS Campaign Operators**: Running infostealer campaigns through malicious Google search advertisements
- **DroidLock Operators**: Deploying Android ransomware with screen locking and data exfiltration capabilities
- **Spiderman Phishing Service**: Targeting customers of dozens of European banks and cryptocurrency holders