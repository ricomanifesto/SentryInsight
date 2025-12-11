# Exploitation Report

Current threat landscape shows critical zero-day exploitation across multiple platforms and software products. The most severe activity involves active exploitation of an unpatched zero-day vulnerability in Gogs Git service affecting over 700 internet-facing servers, Google Chrome zero-day attacks marking the eighth such exploit this year, and widespread exploitation of hard-coded cryptographic keys in Gladinet products. Additional concerning activity includes React2Shell exploitation delivering cryptocurrency miners, WinRAR vulnerability exploitation by multiple threat groups, and Microsoft patching 56 flaws including one actively exploited vulnerability and two zero-days.

## Active Exploitation Details

### Gogs Zero-Day Remote Code Execution
- **Description**: High-severity unpatched security vulnerability in Gogs self-hosted Git service enabling remote code execution on internet-facing instances
- **Impact**: Attackers can gain remote code execution and compromise servers, with over 700 instances already compromised
- **Status**: Currently unpatched and under active exploitation

### Google Chrome Zero-Day Vulnerability
- **Description**: High-severity undisclosed vulnerability in Google Chrome browser being actively exploited in the wild
- **Impact**: Enables attackers to exploit Chrome users through active in-the-wild attacks
- **Status**: Patched by Google in emergency security updates, marking the eighth Chrome zero-day exploited in 2025

### Gladinet Hard-Coded Cryptographic Keys
- **Description**: Hard-coded cryptographic keys vulnerability in Gladinet's CentreStack and Triofox products
- **Impact**: Allows unauthorized access and code execution, affecting nine organizations in active attacks
- **Status**: Currently being exploited in active attacks by threat actors

### React2Shell Critical Vulnerability
- **Description**: Maximum-severity security flaw in React Server Components (RSC)
- **Impact**: Heavy exploitation delivering cryptocurrency miners and various malware across multiple sectors
- **Status**: Continues to witness active exploitation by multiple threat actors

### WinRAR Vulnerability
- **Description**: Security flaw in WinRAR file archiver and compression utility
- **Impact**: Being exploited by multiple threat groups for malicious activities
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-6218

### Microsoft Windows Actively Exploited Vulnerability
- **Description**: One of 56 security flaws patched by Microsoft in December 2025 security updates
- **Impact**: Active exploitation in the wild targeting Windows platform
- **Status**: Patched by Microsoft along with two zero-day vulnerabilities

## Affected Systems and Products

- **Gogs Git Service**: Self-hosted Git service instances exposed to the internet
- **Google Chrome**: Web browser across all supported platforms
- **Gladinet CentreStack and Triofox**: Cloud storage and file sharing solutions
- **React Server Components**: Web applications using React Server Components
- **WinRAR**: File archiver and compression utility
- **Microsoft Windows**: Various Windows platform components and services
- **Fortinet Products**: Authentication systems requiring urgent patches
- **Ivanti Products**: Enterprise software solutions with code execution vulnerabilities
- **SAP Products**: Enterprise applications with authentication bypass flaws

## Attack Vectors and Techniques

- **Remote Code Execution**: Direct exploitation of unpatched vulnerabilities in internet-facing services
- **Browser-Based Attacks**: Zero-day exploitation targeting Chrome users through web-based vectors
- **Hard-Coded Key Exploitation**: Abuse of embedded cryptographic keys for unauthorized system access
- **Malware Distribution**: React2Shell exploitation for cryptocurrency miner deployment
- **Social Engineering**: ClickFix-style attacks using legitimate AI platforms (Grok, ChatGPT) for malware delivery
- **Supply Chain Attacks**: Exploitation of development tools and compromised credentials
- **Phishing Operations**: Spiderman phishing kit targeting European banking customers
- **SEO Poisoning**: Google Ads abuse for macOS infostealer malware distribution

## Threat Actor Activities

- **Multiple APT Groups**: Coordinated exploitation of WinRAR vulnerability across different threat groups
- **WIRTE APT**: Leveraging AshenLoader sideloading to install AshTag espionage backdoor targeting Middle East government and diplomatic entities
- **Storm-0249**: Initial access broker weaponizing EDR platforms and Windows utilities in high-precision attacks
- **Pro-Russia Hacktivists**: Targeting US critical infrastructure through VNC connection compromises in OT systems
- **Ukrainian National**: Charged for assisting Russian hacktivist groups in attacks on critical infrastructure including water systems and nuclear facilities
- **Cryptocurrency Miners**: Widespread deployment through React2Shell exploitation across multiple sectors
- **Banking Fraud Operations**: Spiderman phishing service targeting dozens of European banks and cryptocurrency holders