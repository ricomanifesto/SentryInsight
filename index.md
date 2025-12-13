# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by large-scale attacks targeting React Server Components through the React2Shell vulnerability (CVE-2025-55182), which has prompted CISA to issue emergency patching orders for federal agencies. Concurrently, multiple zero-day vulnerabilities are under active exploitation, including a Windows RasMan service flaw and an undocumented Gladinet CentreStack cryptographic vulnerability. The threat landscape is further complicated by sophisticated malware campaigns leveraging GitHub repositories, malicious VSCode extensions, and advanced phishing kits employing AI-powered techniques to bypass multi-factor authentication.

## Active Exploitation Details

### React2Shell Vulnerability
- **Description**: A critical vulnerability in React Server Components that enables remote code execution and denial-of-service attacks
- **Impact**: Attackers can execute arbitrary code remotely and cause service disruptions through denial-of-service attacks
- **Status**: Under active widespread exploitation with proof-of-concept exploits containing WAF bypasses flooding the internet
- **CVE ID**: CVE-2025-55182

### Windows RasMan Zero-Day
- **Description**: A zero-day vulnerability affecting the Windows Remote Access Connection Manager (RasMan) service
- **Impact**: Allows attackers to crash the RasMan service, potentially disrupting remote access capabilities
- **Status**: Actively exploited in the wild with unofficial patches available but no official Microsoft fix yet released

### GeoServer XXE Vulnerability
- **Description**: A high-severity XML External Entity (XXE) injection flaw in OSGeo GeoServer
- **Impact**: Enables attackers to read sensitive files, perform server-side request forgery, and potentially execute remote code
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog

### Gladinet CentreStack Cryptographic Flaw
- **Description**: An undocumented vulnerability in the cryptographic algorithm implementation of CentreStack and Triofox products
- **Impact**: Enables remote code execution attacks against secure remote file access systems
- **Status**: Currently being exploited in active attacks with no CVE assigned

### Gogs Zero-Day Vulnerability
- **Description**: An unpatched vulnerability in the self-hosted Git service Gogs that bypasses a previous RCE bug fix
- **Impact**: Allows remote code execution on affected Gogs installations
- **Status**: Exploited for months before discovery and remains unpatched

## Affected Systems and Products

- **React Applications**: Systems using React Server Components are vulnerable to DoS and source code exposure
- **Windows Systems**: All Windows versions with RasMan service are affected by the zero-day vulnerability
- **GeoServer Deployments**: OSGeo GeoServer installations vulnerable to XXE injection attacks
- **Gladinet Products**: CentreStack and Triofox secure file access solutions affected by cryptographic flaw
- **Gogs Installations**: Self-hosted Git service deployments remain vulnerable to unpatched RCE bypass
- **VSCode Users**: Developers using Visual Studio Code Marketplace extensions targeted by malicious packages
- **GitHub Repositories**: Python repositories hosting fake OSINT and GPT utilities spreading PyStoreRAT malware
- **Notepad++ Users**: WinGUp update tool vulnerability allowing malicious update delivery

## Attack Vectors and Techniques

- **Web Application Exploitation**: Attackers using WAF bypass techniques in React2Shell exploit code
- **XXE Injection**: XML External Entity attacks targeting GeoServer implementations
- **Service Disruption**: RasMan service crashes through zero-day exploitation
- **Supply Chain Attacks**: Malicious packages distributed through GitHub and VSCode Marketplace
- **Social Engineering**: Fake torrent files hiding malware in subtitle files targeting movie downloads
- **Phishing Campaigns**: AI-powered phishing kits (BlackForce, GhostFrame, InboxPrime AI, Spiderman) bypassing MFA
- **Malware Distribution**: PyStoreRAT JavaScript-based RAT distributed through fake utility repositories
- **Update Mechanism Abuse**: Exploitation of software updaters to deliver malicious payloads

## Threat Actor Activities

- **Hamas-Linked Hackers**: Targeting Middle Eastern diplomatic entities with improved malware and expanded regional operations
- **Supply Chain Attackers**: Increasing focus on GitHub Actions and open source software repositories for malware distribution
- **Phishing Groups**: Deploying advanced AI-powered credential theft operations with MFA bypass capabilities
- **Insider Threats**: Former Coupang employee maintaining system access post-employment to exfiltrate 33.7 million customer records
- **Malware Distributors**: Leveraging popular software platforms like VSCode Marketplace and GitHub to distribute trojans hidden in fake PNG files and utility tools