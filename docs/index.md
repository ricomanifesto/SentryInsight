# Exploitation Report

The current cybersecurity landscape reveals several critical exploitation campaigns targeting diverse infrastructure components. Most notably, a new Mirai-based botnet campaign is actively exploiting CVE-2025-29635, a high-severity command injection vulnerability in end-of-life D-Link routers. Additionally, threat actors are exploiting CVE-2026-1731, a critical remote code execution flaw in Bomgar RMM tools, demonstrating significant supply chain risks. Microsoft has addressed multiple critical vulnerabilities including CVE-2026-40372 in ASP.NET Core and an unpatched SharePoint spoofing vulnerability that was initially exploited as a zero-day. The threat landscape is further complicated by sophisticated supply chain attacks, including self-propagating npm package compromises and malicious Docker images targeting development environments.

## Active Exploitation Details

### D-Link Router Command Injection Vulnerability
- **Description**: High-severity command-injection vulnerability affecting D-Link DIR-823X routers that are end-of-life
- **Impact**: Attackers can execute arbitrary commands and enlist devices into Mirai-based botnets
- **Status**: Actively exploited in the wild by Mirai campaign, no patches available for EOL devices
- **CVE ID**: CVE-2025-29635

### Bomgar RMM Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in Bomgar remote monitoring and management tool
- **Impact**: Can be exploited to spread ransomware and compromise supply chains
- **Status**: Actively exploited with surge in exploitation activity
- **CVE ID**: CVE-2026-1731

### Microsoft ASP.NET Core Privilege Escalation
- **Description**: Critical privilege escalation vulnerability in ASP.NET Core framework
- **Impact**: Allows attackers to escalate privileges within affected applications
- **Status**: Patched with out-of-band emergency security updates from Microsoft
- **CVE ID**: CVE-2026-40372

### Microsoft SharePoint Spoofing Vulnerability
- **Description**: Spoofing vulnerability affecting Microsoft SharePoint servers exposed online
- **Impact**: Enables spoofing attacks against SharePoint installations
- **Status**: Previously exploited as zero-day, still being exploited against unpatched systems with over 1,300 vulnerable servers identified

### Cohere AI Terrarium Sandbox Escape
- **Description**: Critical security vulnerability in Python-based Terrarium sandbox
- **Impact**: Results in arbitrary code execution, root access, and container escape
- **Status**: Vulnerability disclosed and rated 9.3 out of 10 severity
- **CVE ID**: CVE-2026-5752

### Windows Defender Exploitation
- **Description**: Multiple vulnerabilities turning Windows Defender into an attacker tool
- **Impact**: Allows attackers to abuse Microsoft's built-in security platform for malicious purposes
- **Status**: Three proof-of-concept exploits being used in active attacks, two remain unpatched

## Affected Systems and Products

- **D-Link DIR-823X Routers**: End-of-life models vulnerable to command injection attacks
- **Bomgar RMM Tools**: Remote monitoring and management systems at risk of RCE exploitation
- **Microsoft ASP.NET Core**: Web application framework affected by privilege escalation flaw
- **Microsoft SharePoint Servers**: Over 1,300 exposed servers vulnerable to spoofing attacks
- **Cohere AI Terrarium**: Python-based sandbox environment with container escape vulnerability
- **Windows Defender**: Microsoft's built-in security platform being weaponized by attackers
- **npm Package Ecosystem**: Node.js package manager affected by self-propagating supply chain attacks
- **Docker Hub Repository**: Checkmarx KICS official repository compromised with malicious images
- **VS Code Extensions**: Development environment extensions targeted in supply chain attacks
- **Lantronix and Silex Serial-to-IP Converters**: Industrial devices exposed to 22 BRIDGE:BREAK vulnerabilities

## Attack Vectors and Techniques

- **Botnet Recruitment**: Mirai-based campaigns exploiting router vulnerabilities to expand botnets
- **Supply Chain Poisoning**: Self-propagating worms targeting npm packages and Docker repositories
- **Privilege Escalation**: Exploitation of ASP.NET Core vulnerabilities for elevated access
- **Living-off-the-Land**: Weaponizing legitimate Windows Defender functionality for attacks
- **Container Escape**: Sandbox bypass techniques in AI development environments
- **Spoofing Attacks**: Targeting unpatched SharePoint servers for identity manipulation
- **Social Engineering**: DPRK fake job scams using "Contagious Interview" techniques
- **Wiper Attacks**: Lotus malware deployed against Venezuelan energy infrastructure
- **Post-Quantum Encryption**: Kyber ransomware implementing advanced encryption methods

## Threat Actor Activities

- **Mirai Operators**: Actively exploiting D-Link router vulnerabilities to build botnets
- **The Gentlemen Ransomware**: Rapidly scaling operations with over 1,570 victims identified through SystemBC C2 infrastructure
- **Kyber Ransomware Gang**: Targeting Windows and VMware ESXi systems with post-quantum encryption capabilities
- **Harvester Group**: Deploying Linux GoGra backdoor in South Asia using Microsoft Graph API for communication
- **Mustang Panda**: Distributing LOTUSLITE malware variants targeting Indian banks and South Korean policy circles
- **Scattered Spider**: Member "Tylerb" pleaded guilty to wire fraud conspiracy and aggravated identity theft
- **DPRK Threat Actors**: Conducting sophisticated fake job scams with self-propagating malware distribution
- **Supply Chain Attackers**: Compromising npm packages, Docker images, and VS Code extensions for credential theft
- **BlackCat Affiliates**: Ransomware negotiator pleaded guilty to involvement in BlackCat scheme
- **Venezuelan Energy Attackers**: Deploying Lotus wiper malware against energy and utility organizations