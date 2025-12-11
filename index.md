# Exploitation Report

Critical exploitation activity is occurring across multiple platforms, with Google Chrome facing its eighth zero-day vulnerability of 2025 actively exploited in the wild. Microsoft's December Patch Tuesday addressed 57 security flaws including three zero-day vulnerabilities, with one being actively exploited. WinRAR vulnerability CVE-2025-6218 is under active attack by multiple threat groups and has been added to CISA's Known Exploited Vulnerabilities catalog. The React2Shell vulnerability continues to see heavy exploitation, with North Korean-linked actors and other threat groups leveraging this maximum-severity flaw to deploy cryptocurrency miners and malware across multiple sectors. Gladinet's CentreStack and Triofox products are being actively exploited through hard-coded cryptographic keys, affecting nine organizations.

## Active Exploitation Details

### Chrome Zero-Day Vulnerability
- **Description**: Eighth Chrome zero-day vulnerability of 2025 requiring emergency patches from Google
- **Impact**: Allows attackers to exploit Chrome users through active attacks
- **Status**: Emergency updates released to fix the vulnerability

### Microsoft Zero-Day Vulnerability
- **Description**: One of three zero-day vulnerabilities in Microsoft's December 2025 security updates
- **Impact**: Being actively exploited in the wild with proof-of-concept exploit code publicly available for related flaws
- **Status**: Patched in December 2025 Patch Tuesday

### WinRAR Security Flaw
- **Description**: Critical vulnerability in WinRAR file archiver and compression utility under active attack
- **Impact**: Allows multiple threat groups to exploit WinRAR installations
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-6218

### React2Shell Vulnerability
- **Description**: Maximum-severity security flaw in React Server Components (RSC) being heavily exploited
- **Impact**: Threat actors deliver cryptocurrency miners and various malware payloads across multiple sectors
- **Status**: Ongoing exploitation by multiple threat actors including North Korean-linked groups

### Gladinet Hard-Coded Keys Vulnerability
- **Description**: Hard-coded cryptographic keys vulnerability in Gladinet's CentreStack and Triofox products
- **Impact**: Enables unauthorized access and code execution capabilities
- **Status**: Active exploitation affecting nine organizations

### .NET SOAPwn Vulnerability
- **Description**: Exploitation primitives in .NET Framework through rogue WSDL files
- **Impact**: Achieves remote code execution against enterprise-grade applications
- **Status**: Research disclosed new attack vectors for file writes and RCE

## Affected Systems and Products

- **Google Chrome**: All versions prior to latest emergency security updates
- **Microsoft Windows**: Windows 10 and other Windows platforms affected by 57 security flaws
- **WinRAR**: File archiver and compression utility installations
- **React Server Components**: Applications using React Server Components framework
- **Gladinet CentreStack and Triofox**: File sync and sharing products with hard-coded keys
- **PCIe 5.0+ Systems**: Systems using PCIe Integrity and Data Encryption protocol
- **Android Devices**: Targeted by DroidLock ransomware malware
- **macOS Systems**: Targeted by AMOS infostealer through malicious ads
- **Docker Hub Images**: Over 10,000 container images leaking credentials
- **SAP Products**: Multiple SAP products with three critical vulnerabilities
- **Fortinet and Ivanti**: Products with authentication bypass and code execution flaws

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Chrome and Microsoft products
- **Hard-Coded Cryptographic Keys**: Exploitation of embedded authentication credentials in Gladinet products
- **Social Engineering with AI Platforms**: ClickFix-style attacks using Grok and ChatGPT for malware delivery
- **SEO Poisoning**: Google ads manipulation to distribute AMOS infostealer malware
- **Rogue WSDL Files**: .NET exploitation through malicious Web Service Description Language files
- **EDR Process Abuse**: Storm-0249 weaponizing endpoint detection and response platforms
- **VNC Connection Compromise**: Pro-Russia hacktivists targeting virtual network computing in OT systems
- **Container Image Poisoning**: Credential exposure through compromised Docker Hub images
- **Phishing Kit Deployment**: Spiderman phishing service targeting European banks
- **Ransomware Screen Locking**: DroidLock malware demanding ransom payments on Android devices

## Threat Actor Activities

- **North Korean-Linked Groups**: Exploiting React2Shell vulnerability to deploy EtherRAT malware and other payloads
- **Storm-0249**: Initial access broker conducting high-precision attacks by abusing EDR processes and Windows utilities
- **Pro-Russia Hacktivist Groups**: Targeting US critical infrastructure through VNC connection compromises, assisted by Ukrainian national
- **Multiple Threat Groups**: Actively exploiting WinRAR CVE-2025-6218 vulnerability across various campaigns
- **AMOS Campaign Operators**: Distributing infostealer malware through malicious Google ads targeting macOS users
- **Spiderman Phishing Operators**: Running phishing-as-a-service targeting dozens of European banks and cryptocurrency holders
- **DroidLock Operators**: Deploying Android ransomware with screen locking and data access capabilities
- **React2Shell Exploiters**: Various threat actors leveraging the vulnerability to deliver cryptocurrency miners across multiple sectors