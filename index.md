# Exploitation Report

Current threat landscape shows intense exploitation activity across multiple attack vectors, with particularly concerning developments in supply chain attacks, ransomware operations, and critical infrastructure targeting. Active exploitation campaigns include a Mirai botnet targeting end-of-life D-Link routers through CVE-2025-29635, widespread abuse of unpatched SharePoint servers, and sophisticated supply chain attacks affecting npm packages and Docker repositories. The emergence of advanced ransomware groups like "The Gentlemen" and destructive wiper malware targeting Venezuelan energy infrastructure demonstrates the evolving sophistication of threat actors. Critical vulnerabilities in remote management tools and AI-based systems are being actively exploited, while several zero-day vulnerabilities have been discovered and patched across Microsoft products and third-party applications.

## Active Exploitation Details

### D-Link Router Command Injection Vulnerability
- **Description**: High-severity command-injection vulnerability affecting D-Link DIR-823X routers that are end-of-life
- **Impact**: Remote code execution allowing attackers to compromise devices and enlist them in Mirai botnets
- **Status**: Actively exploited by new Mirai campaign, no patches available for EOL devices
- **CVE ID**: CVE-2025-29635

### Microsoft SharePoint Spoofing Vulnerability
- **Description**: Spoofing vulnerability in Microsoft SharePoint servers that was initially exploited as a zero-day
- **Impact**: Allows attackers to conduct spoofing attacks and potentially gain unauthorized access
- **Status**: Over 1,300 servers remain unpatched and vulnerable to ongoing exploitation
- **Status**: Patches available but not widely deployed

### ASP.NET Core Privilege Escalation
- **Description**: Critical privilege escalation vulnerability in ASP.NET Core framework
- **Impact**: Allows attackers to escalate privileges within affected applications
- **Status**: Microsoft released emergency out-of-band patches
- **CVE ID**: CVE-2026-40372

### Cohere AI Terrarium Sandbox Escape
- **Description**: Critical vulnerability in Python-based Terrarium sandbox allowing arbitrary code execution
- **Impact**: Enables root code execution and container escape from sandboxed environments
- **Status**: Recently disclosed with patches available
- **CVE ID**: CVE-2026-5752

### Bomgar RMM Remote Code Execution
- **Description**: Critical remote code execution flaw in Bomgar remote monitoring and management tool
- **Impact**: Can be exploited to spread ransomware and compromise supply chains
- **Status**: Active exploitation observed with supply chain implications
- **CVE ID**: CVE-2026-1731

### Google Antigravity AI Tool RCE
- **Description**: Critical prompt-injection vulnerability in Google's AI-based 'Antigravity' tool for filesystem operations
- **Impact**: Allows sandbox escape and arbitrary code execution through sanitization bypass
- **Status**: Recently patched by Google

## Affected Systems and Products

- **D-Link DIR-823X Routers**: End-of-life devices vulnerable to command injection attacks
- **Microsoft SharePoint Servers**: Over 1,300 internet-exposed servers remain unpatched
- **ASP.NET Core Applications**: Web applications using vulnerable framework versions
- **Cohere AI Terrarium**: Python-based sandbox environments
- **Bomgar RMM Tools**: Remote monitoring and management deployments
- **Google Antigravity**: AI-based filesystem operation tools
- **npm Package Ecosystem**: Node.js packages and developer environments
- **Docker Hub Repositories**: Specifically checkmarx/kics repository
- **iOS/iPad Devices**: Apple devices with notification services vulnerability
- **Lantronix and Silex Serial-to-IP Converters**: Industrial communication devices
- **Windows Defender**: Microsoft's built-in security platform

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Self-propagating worms targeting npm packages and Docker images to steal developer tokens
- **Botnet Recruitment**: Mirai malware exploiting router vulnerabilities to expand botnets
- **Living-off-the-Land**: Using legitimate Microsoft Graph API for command and control communications
- **Ransomware-as-a-Service**: The Gentlemen ransomware operation scaling rapidly with sophisticated techniques
- **Post-Quantum Encryption**: Kyber ransomware implementing Kyber1024 encryption algorithms
- **Data Wiping Attacks**: Lotus wiper malware targeting critical infrastructure
- **Privilege Escalation**: Exploiting framework vulnerabilities to gain elevated system access
- **Container Escape**: Breaking out of sandboxed environments through code injection
- **Prompt Injection**: Manipulating AI systems to execute arbitrary commands
- **Social Engineering**: DPRK fake job scams using "Contagious Interview" techniques

## Threat Actor Activities

- **The Gentlemen Ransomware Group**: Rapidly scaling ransomware-as-a-service operation with over 1,570 victims identified through SystemBC C2 infrastructure
- **Mirai Botnet Operators**: Actively exploiting D-Link router vulnerabilities to expand botnet capabilities
- **Harvester APT Group**: Deploying Linux GoGra backdoor targeting South Asian entities using Microsoft Graph API for stealth
- **Kyber Ransomware Gang**: Targeting Windows systems and VMware ESXi with post-quantum encryption capabilities
- **DPRK-linked Actors**: Conducting fake job scams with self-propagating malware distribution
- **Mustang Panda**: Using new LOTUSLITE variant to target Indian banking sector and South Korean policy organizations
- **Scattered Spider**: Member Tyler Buchanan pleaded guilty to wire fraud and identity theft charges
- **Unknown Venezuelan Actors**: Deploying Lotus wiper malware against energy and utility infrastructure
- **npm Supply Chain Attackers**: Creating self-propagating worms to steal developer authentication tokens
- **Docker Hub Attackers**: Compromising official repositories to distribute malicious container images