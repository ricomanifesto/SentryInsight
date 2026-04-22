# Exploitation Report

Current threat landscape shows significant active exploitation across multiple critical vulnerabilities, with attackers leveraging both zero-day flaws and recently patched vulnerabilities for maximum impact. Most concerning are the ongoing attacks against Microsoft SharePoint servers through an unpatched spoofing vulnerability that was previously exploited as a zero-day, the active exploitation of a new SD-WAN vulnerability flagged by CISA, and the emergence of Bomgar RMM exploitation for ransomware deployment. Additionally, threat actors are weaponizing Windows Defender through multiple proof-of-concept exploits, while sophisticated supply chain attacks target npm ecosystems and developer environments through fake job recruitment campaigns.

## Active Exploitation Details

### SharePoint Spoofing Vulnerability
- **Description**: A spoofing vulnerability affecting Microsoft SharePoint servers that was previously exploited as a zero-day
- **Impact**: Allows attackers to conduct spoofing attacks against vulnerable SharePoint installations
- **Status**: Actively being exploited in ongoing attacks with over 1,300 servers remaining unpatched

### SD-WAN Manager Vulnerability
- **Description**: A newly identified vulnerability in Catalyst SD-WAN Manager systems
- **Impact**: Enables remote code execution and potential system compromise
- **Status**: Actively exploited in attacks, flagged by CISA with mandatory patching deadline for federal agencies

### Bomgar RMM Critical Flaw
- **Description**: Critical remote code execution vulnerability in Bomgar remote monitoring and management tool
- **Impact**: Exploited to spread ransomware and compromise supply chains
- **Status**: Experiencing surge in exploitation activity
- **CVE ID**: CVE-2026-1731

### Windows Defender Exploitation
- **Description**: Multiple proof-of-concept exploits targeting Microsoft's built-in security platform
- **Impact**: Converts Windows Defender into an attacker tool, compromising endpoint security
- **Status**: Being used in active attacks with two exploits remaining unpatched

### ASP.NET Core Privilege Escalation
- **Description**: Critical vulnerability in ASP.NET Core allowing privilege escalation
- **Impact**: Attackers can escalate privileges on affected systems
- **Status**: Microsoft released emergency out-of-band patches
- **CVE ID**: CVE-2026-40372

### Cohere AI Terrarium Sandbox Flaw
- **Description**: Critical security vulnerability in Python-based Terrarium sandbox
- **Impact**: Enables root code execution and container escape
- **Status**: Recently disclosed with high severity rating
- **CVE ID**: CVE-2026-5752

## Affected Systems and Products

- **Microsoft SharePoint**: Over 1,300 servers exposed online remain vulnerable to spoofing attacks
- **Catalyst SD-WAN Manager**: Systems actively targeted with mandatory federal patching requirements
- **Bomgar RMM**: Remote monitoring and management installations experiencing exploitation surge
- **Windows Defender**: Microsoft's built-in security platform being weaponized through multiple exploits
- **ASP.NET Core**: Web development framework requiring emergency patching
- **Lantronix and Silex Serial-to-IP Converters**: Thousands of devices exposed through 22 BRIDGE:BREAK vulnerabilities
- **npm Ecosystem**: Node Package Manager supply chain under active attack
- **Linux Systems**: Targeted by GoGra backdoor utilizing Microsoft Graph API
- **Venezuelan Energy Infrastructure**: Hit by Lotus wiper malware in destructive attacks
- **Cohere AI Terrarium**: Python sandbox environment with critical container escape flaw

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Self-propagating npm attacks stealing developer credentials and auth tokens
- **Fake Job Recruitment**: DPRK-linked "Contagious Interview" campaigns using compromised developer repositories as infection vectors
- **Wiper Malware Deployment**: Lotus wiper targeting critical infrastructure in Venezuela's energy sector
- **Remote Access Trojans**: Distribution through compromised repositories in developer-focused social engineering
- **Proxy Malware**: SystemBC deployment by The Gentlemen ransomware operation affecting 1,570+ victims
- **Living-off-the-Land**: GoGra backdoor abusing legitimate Microsoft Graph API for command and control
- **Mobile Malware**: NGate campaign trojanizing HandyPay app to steal NFC data and PINs in Brazil
- **Privilege Escalation**: Exploitation of ASP.NET Core vulnerability for system compromise

## Threat Actor Activities

- **DPRK Groups**: Conducting fake job recruitment campaigns targeting developers with self-propagating malware
- **Mustang Panda**: Deploying LOTUSLITE variant targeting Indian banks and South Korean policy circles
- **The Gentlemen Ransomware**: Operating RaaS with SystemBC proxy malware affecting over 1,500 victims
- **Scattered Spider**: Senior member Tyler Robert Buchanan pleaded guilty to wire fraud and identity theft
- **BlackCat Affiliates**: Ransomware negotiator Angelo Martino pleaded guilty to conducting 2023 attacks
- **Venezuelan Infrastructure Attackers**: Deploying Lotus wiper against energy and utility organizations
- **Supply Chain Attackers**: Targeting npm ecosystem with self-spreading credential theft campaigns
- **Chinese APT Groups**: Targeting Indian financial sector and Korean policy circles with updated LOTUSLITE malware