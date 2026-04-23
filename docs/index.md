# Exploitation Report

Current threat activity reveals multiple critical exploitation campaigns targeting diverse systems and platforms. A new Mirai botnet campaign is actively exploiting a command injection vulnerability in end-of-life D-Link routers to expand malicious infrastructure. Simultaneously, threat actors are leveraging unpatched Microsoft SharePoint servers through spoofing vulnerabilities that were previously exploited as zero-days. Supply chain attacks have intensified with self-propagating worms targeting npm packages and malicious Docker images compromising development environments. Advanced persistent threat groups, including China-linked actors, are deploying sophisticated backdoors across government systems while ransomware operations continue scaling with advanced encryption techniques. Critical privilege escalation vulnerabilities in ASP.NET Core and sandbox escape flaws in AI platforms present immediate risks requiring urgent patching.

## Active Exploitation Details

### D-Link Router Command Injection Vulnerability
- **Description**: A high-severity command injection vulnerability affecting D-Link DIR-823X routers that allows remote code execution
- **Impact**: Attackers can gain complete control of affected devices and enlist them into Mirai botnets for DDoS attacks and further malicious activities
- **Status**: Actively exploited by new Mirai-based malware campaign targeting end-of-life devices
- **CVE ID**: CVE-2025-29635

### Microsoft SharePoint Spoofing Vulnerability
- **Description**: A spoofing vulnerability in Microsoft SharePoint servers that was previously exploited as a zero-day
- **Impact**: Enables attackers to conduct spoofing attacks against SharePoint environments
- **Status**: Over 1,300 SharePoint servers remain unpatched and vulnerable to ongoing exploitation
- **CVE ID**: Not specified in articles

### iOS Notification Services Flaw
- **Description**: A vulnerability in iOS and iPadOS Notification Services that caused notifications marked for deletion to remain stored on devices
- **Impact**: Allowed forensic recovery of supposedly deleted notifications, including Signal messages in FBI investigations
- **Status**: Recently patched by Apple with out-of-band security updates
- **CVE ID**: CVE-2026-28950

### ASP.NET Core Privilege Escalation
- **Description**: A critical privilege escalation vulnerability in ASP.NET Core applications
- **Impact**: Allows attackers to escalate privileges within affected ASP.NET Core environments
- **Status**: Critical severity requiring immediate patching, addressed by Microsoft emergency updates
- **CVE ID**: CVE-2026-40372

### Cohere AI Terrarium Sandbox Escape
- **Description**: A critical vulnerability in the Python-based Terrarium sandbox used by Cohere AI
- **Impact**: Enables arbitrary code execution with root privileges and container escape capabilities
- **Status**: Critical vulnerability with 9.3 CVSS rating
- **CVE ID**: CVE-2026-5752

### Windows Defender Exploitation
- **Description**: Multiple proof-of-concept exploits targeting Microsoft's built-in Windows Defender security platform
- **Impact**: Converts the security tool into an attacker asset for malicious operations
- **Status**: Three exploits in active use, with two remaining unpatched

## Affected Systems and Products

- **D-Link DIR-823X Routers**: End-of-life devices vulnerable to command injection attacks
- **Microsoft SharePoint Servers**: Over 1,300 internet-exposed servers vulnerable to spoofing attacks
- **iOS and iPadOS Devices**: iPhones and iPads with vulnerable Notification Services
- **ASP.NET Core Applications**: Web applications using affected ASP.NET Core frameworks
- **Cohere AI Terrarium**: Python-based AI sandbox environments
- **Windows Defender**: Microsoft's built-in security platform on Windows systems
- **npm Package Ecosystem**: Node.js package repository and dependent applications
- **Docker Hub Repositories**: Containerized applications using compromised images
- **Lantronix and Silex Converters**: Serial-to-IP converter devices with multiple vulnerabilities
- **VMware ESXi Endpoints**: Virtual infrastructure targeted by ransomware operations

## Attack Vectors and Techniques

- **Botnet Recruitment**: Mirai campaigns exploiting router vulnerabilities to expand malicious infrastructure
- **Supply Chain Poisoning**: Self-propagating worms hijacking npm packages and Docker repositories
- **Living-off-the-Land**: Abuse of legitimate Microsoft Graph API for backdoor communications
- **Advanced Encryption**: Ransomware implementing Kyber1024 post-quantum encryption techniques
- **Social Engineering**: Fake job recruitment campaigns spreading malware through developer interviews
- **Sandbox Escape**: Container breakout techniques targeting AI platform security boundaries
- **Privilege Escalation**: Exploitation of web framework vulnerabilities for elevated access
- **Data Wiping**: Destructive attacks using custom wiper malware against critical infrastructure

## Threat Actor Activities

- **GopherWhisper (China-linked APT)**: Deployed Go-based backdoors across 12 Mongolian government systems using sophisticated attack toolsets
- **Harvester Group**: Developed Linux variant of GoGra backdoor leveraging Microsoft Graph API for command and control operations in South Asian campaigns
- **The Gentlemen Ransomware**: Rapidly scaled operations with over 1,570 victims identified through SystemBC proxy infrastructure
- **Kyber Ransomware Gang**: Targeting Windows and VMware ESXi systems with post-quantum encryption implementations
- **Mustang Panda**: Distributing new LOTUSLITE malware variants against Indian banking sector and South Korean policy organizations
- **DPRK-affiliated Groups**: Conducting "Contagious Interview" campaigns using compromised developer repositories for malware distribution
- **BlackCat Ransomware Associates**: Operating negotiation schemes involving insider threat actors
- **Supply Chain Attackers**: Executing coordinated campaigns against npm packages and Docker repositories for credential theft