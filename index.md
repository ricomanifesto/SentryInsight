# Exploitation Report

Critical exploitation activity continues to surge across multiple attack vectors, with threat actors leveraging supply chain vulnerabilities, zero-day exploits, and sophisticated malware campaigns. The most severe concerns include self-propagating npm supply chain attacks stealing developer credentials, critical privilege escalation vulnerabilities in ASP.NET Core (CVE-2026-40372), ongoing exploitation of SharePoint spoofing vulnerabilities, and destructive wiper malware targeting critical infrastructure. Advanced persistent threat groups are deploying new variants of backdoors while exploiting legitimate Microsoft services for command and control operations, demonstrating the evolving sophistication of modern cyber threats.

## Active Exploitation Details

### ASP.NET Core Privilege Escalation Vulnerability
- **Description**: Critical security vulnerability in ASP.NET Core that allows attackers to escalate privileges through exploitation of the framework
- **Impact**: Attackers can gain elevated privileges within affected applications, potentially leading to complete system compromise
- **Status**: Microsoft has released emergency out-of-band patches to address the vulnerability
- **CVE ID**: CVE-2026-40372

### SharePoint Server Spoofing Vulnerability
- **Description**: Zero-day spoofing vulnerability affecting Microsoft SharePoint servers that remains actively exploited in ongoing attacks
- **Impact**: Attackers can conduct spoofing attacks against SharePoint infrastructure, potentially leading to authentication bypass and unauthorized access
- **Status**: Over 1,300 SharePoint servers remain unpatched and vulnerable to ongoing exploitation

### Cohere AI Terrarium Sandbox Escape
- **Description**: Critical vulnerability in Python-based Terrarium sandbox environment that enables arbitrary code execution and container escape
- **Impact**: Attackers can achieve root code execution and escape sandbox containment, potentially compromising the underlying host system
- **Status**: Vulnerability disclosed with patches available
- **CVE ID**: CVE-2026-5752

### Bomgar RMM Remote Code Execution
- **Description**: Critical remote code execution flaw in Bomgar remote monitoring and management tool being actively exploited
- **Impact**: Attackers can execute arbitrary code remotely, spread ransomware, and compromise supply chains through managed endpoints
- **Status**: Active exploitation observed with supply chain implications
- **CVE ID**: CVE-2026-1731

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits turning Microsoft's built-in Windows Defender security platform into an attacker tool
- **Impact**: Attackers can weaponize the legitimate security software for malicious purposes, bypassing detection mechanisms
- **Status**: Active exploitation confirmed; two exploits remain unpatched

### Google Antigravity AI Tool RCE
- **Description**: Critical remote code execution vulnerability in Google's AI-based 'Antigravity' tool caused by prompt injection and sanitization issues
- **Impact**: Allows sandbox escape and arbitrary code execution through prompt injection attacks
- **Status**: Patched by Google following disclosure

### npm Supply Chain Self-Propagating Attack
- **Description**: Self-propagating worm that hijacks npm packages to steal developer authentication tokens and spreads through compromised accounts
- **Impact**: Theft of developer credentials, unauthorized package publishing, and potential widespread supply chain contamination
- **Status**: Active ongoing campaign targeting Node.js ecosystem

## Affected Systems and Products

- **ASP.NET Core Applications**: All versions affected by privilege escalation vulnerability requiring emergency patching
- **Microsoft SharePoint Servers**: Over 1,300 internet-exposed servers vulnerable to spoofing attacks
- **Cohere AI Terrarium**: Python-based sandbox environments susceptible to container escape
- **Bomgar RMM Platform**: Remote monitoring and management installations vulnerable to RCE exploitation
- **Windows Defender**: Microsoft's built-in security platform across Windows environments
- **Google Antigravity Tool**: AI-based filesystem operation tool affected by prompt injection
- **npm Package Ecosystem**: Node.js development environment and package management infrastructure
- **Lantronix and Silex Devices**: Serial-to-IP converters affected by 22 BRIDGE:BREAK vulnerabilities
- **Linux Systems**: Targeted by GoGra backdoor variants using Microsoft Graph API
- **Venezuelan Energy Infrastructure**: Critical systems targeted by Lotus wiper malware
- **Indian Banking Sector**: Financial institutions targeted by LOTUSLITE malware variants

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Self-propagating worms spreading through compromised npm packages and developer accounts
- **Privilege Escalation**: Exploitation of ASP.NET Core vulnerabilities to gain elevated system access
- **Container Escape**: Breaking out of sandbox environments through code execution vulnerabilities
- **Living-off-the-Land**: Weaponizing legitimate tools like Windows Defender for malicious purposes
- **Prompt Injection**: Manipulating AI systems to achieve code execution and sandbox escape
- **Spoofing Attacks**: Exploiting SharePoint vulnerabilities for authentication bypass
- **Remote Code Execution**: Leveraging RMM platform vulnerabilities for supply chain compromise
- **Microsoft Graph API Abuse**: Using legitimate Microsoft infrastructure for backdoor communication
- **Data Wiping**: Deploying destructive malware against critical infrastructure systems
- **Social Engineering**: DPRK-attributed fake job scams with self-propagating malware delivery

## Threat Actor Activities

- **Harvester Group**: Deploying Linux GoGra backdoor variants targeting South Asian entities using Microsoft Graph API for command and control
- **Mustang Panda**: Distributing new LOTUSLITE malware variants targeting Indian banking sector and South Korean policy organizations
- **The Gentlemen Ransomware Group**: Operating ransomware-as-a-service with SystemBC proxy malware affecting over 1,570 victims
- **DPRK-Attributed Actors**: Conducting sophisticated fake job scams with self-propagating remote access trojans
- **Scattered Spider Member**: British national pleading guilty to wire fraud and identity theft as part of cybercrime operations
- **BlackCat Ransomware Associates**: Multiple individuals charged and pleading guilty to ransomware negotiation and attack facilitation
- **Venezuelan Infrastructure Attackers**: Unknown threat actors deploying Lotus wiper malware against energy and utility companies
- **npm Supply Chain Attackers**: Cybercriminals conducting self-propagating attacks against Node.js development infrastructure
- **NGate Campaign Operators**: Android malware distributors targeting Brazilian users through trojanized HandyPay applications