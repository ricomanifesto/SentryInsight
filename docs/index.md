# Exploitation Report

Critical vulnerabilities across multiple enterprise systems are under active exploitation, highlighting urgent threats to infrastructure security. Key concerns include a privilege escalation flaw in ASP.NET Core requiring emergency patching (CVE-2026-40372), ongoing exploitation of SharePoint servers through a spoofing vulnerability previously exploited as a zero-day, and active attacks against Apache ActiveMQ servers affecting over 6,400 exposed instances. Additional threats include exploitation of Bomgar RMM systems (CVE-2026-1731) enabling supply chain compromises, Windows Defender being weaponized through unpatched exploits, and Cisco SD-WAN vulnerabilities flagged by CISA for immediate remediation. The threat landscape also features destructive malware campaigns targeting critical infrastructure and sophisticated backdoors leveraging legitimate Microsoft services for stealth operations.

## Active Exploitation Details

### ASP.NET Core Privilege Escalation Vulnerability
- **Description**: A critical privilege escalation vulnerability in ASP.NET Core that allows attackers to elevate their privileges within affected applications
- **Impact**: Attackers can gain elevated access to ASP.NET Core applications, potentially leading to full application compromise
- **Status**: Microsoft has released out-of-band emergency security updates to address this critical flaw
- **CVE ID**: CVE-2026-40372

### SharePoint Server Spoofing Vulnerability
- **Description**: A spoofing vulnerability in Microsoft SharePoint servers that was initially exploited as a zero-day attack
- **Impact**: Allows attackers to conduct spoofing attacks against SharePoint deployments, potentially compromising authentication and data integrity
- **Status**: Over 1,300 SharePoint servers remain unpatched and vulnerable to ongoing attacks despite patches being available

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: A high-severity code injection vulnerability affecting Apache ActiveMQ message broker servers
- **Impact**: Enables remote code execution on vulnerable servers, allowing attackers to compromise messaging infrastructure
- **Status**: Over 6,400 exposed ActiveMQ servers remain vulnerable to active exploitation campaigns

### Bomgar RMM Remote Code Execution Flaw
- **Description**: A critical remote code execution vulnerability in Bomgar remote monitoring and management tool
- **Impact**: Exploitation enables ransomware deployment and supply chain compromise through managed service provider networks
- **Status**: Actively being exploited to spread ransomware and compromise supply chains
- **CVE ID**: CVE-2026-1731

### Cisco Catalyst SD-WAN Manager Vulnerability
- **Description**: A newly identified vulnerability in Cisco Catalyst SD-WAN Manager systems
- **Impact**: Allows attackers to compromise software-defined WAN infrastructure and network management systems
- **Status**: CISA has flagged this as actively exploited, requiring federal agencies to patch within four days

### Windows Defender Exploitation Chain
- **Description**: Three proof-of-concept exploits that weaponize Microsoft's built-in Windows Defender security platform
- **Impact**: Turns the security tool into an attack vector, allowing attackers to abuse trusted system components
- **Status**: Two of the three exploits remain unpatched and are being used in active attacks

### Cohere AI Terrarium Sandbox Escape
- **Description**: A critical vulnerability in the Python-based Terrarium sandbox used by Cohere AI
- **Impact**: Enables arbitrary code execution, root access, and container escape from the sandbox environment
- **Status**: Recently disclosed vulnerability with high severity rating
- **CVE ID**: CVE-2026-5752

## Affected Systems and Products

- **Microsoft ASP.NET Core**: All versions affected by the privilege escalation vulnerability requiring emergency patches
- **Microsoft SharePoint Servers**: Over 1,300 servers exposed online remain vulnerable to spoofing attacks
- **Apache ActiveMQ**: Over 6,400 message broker servers exposed to internet-facing attacks
- **Bomgar RMM**: Remote monitoring and management deployments vulnerable to supply chain attacks
- **Cisco Catalyst SD-WAN Manager**: Enterprise network management systems requiring immediate patching
- **Windows Defender**: Microsoft's built-in security platform being weaponized in active campaigns
- **Cohere AI Terrarium**: Python-based sandbox environment used in AI applications
- **Lantronix and Silex Serial-to-IP Converters**: Industrial devices affected by 22 BRIDGE:BREAK vulnerabilities
- **Google Antigravity IDE**: AI-based development environment with prompt injection vulnerabilities

## Attack Vectors and Techniques

- **Privilege Escalation**: Exploitation of ASP.NET Core flaws to gain elevated system access
- **Zero-Day Exploitation**: Initial SharePoint attacks using previously unknown vulnerabilities
- **Code Injection**: ActiveMQ servers compromised through injection of malicious code
- **Supply Chain Attacks**: Bomgar RMM exploitation to spread ransomware through managed service networks
- **Living-off-the-Land**: Windows Defender being turned into an attack tool using trusted system components
- **Sandbox Escape**: Container breakout techniques targeting AI sandbox environments
- **Prompt Injection**: AI system manipulation through crafted input prompts in development environments
- **Data Wiping Campaigns**: Destructive malware targeting critical infrastructure in Venezuela
- **Backdoor Communications**: Malware using legitimate Microsoft Graph API for command and control

## Threat Actor Activities

- **Lotus Wiper Operators**: Conducted destructive attacks against Venezuelan energy and utility organizations using previously undocumented data-wiping malware
- **Mustang Panda (Chinese APT)**: Deployed new LOTUSLITE backdoor variant targeting Indian banking sector and South Korean policy circles
- **The Gentlemen Ransomware Group**: Operates ransomware-as-a-service with over 1,570 victims identified through SystemBC proxy malware infrastructure
- **BlackCat/ALPHV Affiliates**: Conducted ransomware attacks against U.S. companies with assistance from insider ransomware negotiators
- **Scattered Spider Members**: Senior cybercrime group members pleading guilty to wire fraud and identity theft schemes
- **GoGra Malware Operators**: Deploy Linux backdoors that abuse Microsoft Graph API and Outlook for stealthy command and control communications
- **NGate Campaign Actors**: Target Brazilian users with trojanized HandyPay applications to steal NFC payment data and PINs
- **France Titres Attackers**: Breached French government agency responsible for administrative document issuance and offered stolen citizen data for sale