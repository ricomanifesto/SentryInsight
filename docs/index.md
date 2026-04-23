# Exploitation Report

Current exploitation activity shows a significant surge in critical vulnerabilities being actively targeted across multiple platforms and systems. Most notably, a new Mirai botnet campaign is exploiting CVE-2025-29635, a command injection vulnerability in end-of-life D-Link routers. Microsoft has issued emergency patches for a critical ASP.NET Core privilege escalation flaw (CVE-2026-40372), while over 1,300 SharePoint servers remain vulnerable to ongoing spoofing attacks. Additionally, supply chain attacks are proliferating through npm packages and Docker repositories, with self-propagating worms stealing developer authentication tokens. Ransomware operations continue to evolve, with The Gentlemen group rapidly scaling operations and new variants like Kyber implementing post-quantum encryption techniques.

## Active Exploitation Details

### D-Link Router Command Injection Vulnerability
- **Description**: A high-severity command-injection vulnerability affecting D-Link DIR-823X routers that allows remote code execution
- **Impact**: Enables attackers to execute arbitrary commands and enlist devices into Mirai botnets for DDoS attacks and further malicious activities
- **Status**: Actively exploited in ongoing Mirai campaigns targeting end-of-life devices with no patches available
- **CVE ID**: CVE-2025-29635

### Microsoft ASP.NET Core Privilege Escalation Flaw
- **Description**: A critical privilege escalation vulnerability in ASP.NET Core that allows attackers to elevate their privileges within affected systems
- **Impact**: Attackers can gain elevated access to systems and potentially compromise entire application environments
- **Status**: Microsoft released emergency out-of-band patches to address active exploitation concerns
- **CVE ID**: CVE-2026-40372

### SharePoint Spoofing Vulnerability
- **Description**: A spoofing vulnerability in Microsoft SharePoint servers that was previously exploited as a zero-day
- **Impact**: Enables attackers to conduct spoofing attacks and potentially gain unauthorized access to SharePoint environments
- **Status**: Over 1,300 exposed SharePoint servers remain unpatched despite ongoing exploitation

### Bomgar RMM Remote Code Execution
- **Description**: A critical remote code execution vulnerability in Bomgar remote monitoring and management tool
- **Impact**: Can be exploited to spread ransomware and compromise supply chains through managed service provider networks
- **Status**: Experiencing surge in exploitation activity demonstrating supply chain risks
- **CVE ID**: CVE-2026-1731

### Cohere AI Terrarium Sandbox Escape
- **Description**: A critical security vulnerability in the Python-based Terrarium sandbox environment
- **Impact**: Results in arbitrary code execution with root privileges and container escape capabilities
- **Status**: Recently disclosed with proof-of-concept available
- **CVE ID**: CVE-2026-5752

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits targeting Microsoft's built-in Windows Defender security platform
- **Impact**: Turns the security tool into an attacker weapon, compromising system defenses
- **Status**: Currently being used in active attacks with two exploits remaining unpatched

## Affected Systems and Products

- **D-Link DIR-823X Routers**: End-of-life devices vulnerable to command injection attacks through Mirai campaigns
- **Microsoft ASP.NET Core**: Web applications and services using affected ASP.NET Core versions
- **Microsoft SharePoint**: Over 1,300 internet-exposed SharePoint servers lacking security patches
- **Bomgar RMM**: Remote monitoring and management deployments used by managed service providers
- **Cohere AI Terrarium**: Python-based sandbox environments in AI development platforms
- **Windows Defender**: Microsoft's built-in antivirus and security platform on Windows systems
- **npm Package Registry**: Node.js package ecosystem targeted by supply chain attacks
- **Docker Hub**: Official container repositories including Checkmarx KICS images
- **Lantronix and Silex Devices**: Serial-to-IP converters with 22 newly discovered vulnerabilities

## Attack Vectors and Techniques

- **Command Injection**: Direct exploitation of input validation flaws in D-Link routers for remote code execution
- **Supply Chain Compromise**: Self-propagating worms spreading through npm packages and Docker images to steal developer tokens
- **Privilege Escalation**: ASP.NET Core vulnerability exploitation to gain elevated system access
- **Social Engineering**: DPRK-linked fake job interview campaigns spreading malware through compromised developer repositories
- **Living-off-the-Land**: GoGra backdoor using legitimate Microsoft Graph API infrastructure for command and control communications
- **Sandbox Escape**: Terrarium vulnerability exploitation enabling container breakout and root code execution
- **Anti-Virus Weaponization**: Exploiting Windows Defender to turn security tools against the systems they protect
- **Post-Quantum Encryption**: Kyber ransomware implementing advanced Kyber1024 encryption for enhanced payload protection

## Threat Actor Activities

- **Mirai Botnet Operators**: Actively exploiting D-Link router vulnerabilities to expand botnet infrastructure for DDoS capabilities
- **The Gentlemen Ransomware Group**: Rapidly scaling operations with sophisticated techniques and SystemBC proxy malware deployment affecting over 1,570 victims
- **Kyber Ransomware Operation**: Targeting Windows systems and VMware ESXi endpoints while experimenting with post-quantum encryption methods
- **Harvester APT Group**: Deploying Linux variants of GoGra backdoor against South Asian targets using Microsoft Graph API for stealthy communications
- **Mustang Panda**: Distributing new LOTUSLITE malware variants targeting Indian banking sector and South Korean policy organizations
- **DPRK-linked Groups**: Conducting "Contagious Interview" campaigns using fake job offers to spread remote access trojans through developer communities
- **Scattered Spider Member**: Senior cybercrime group member pleading guilty to wire fraud and identity theft charges
- **Supply Chain Attackers**: Operating sophisticated npm and Docker repository compromise campaigns with self-propagating worm capabilities