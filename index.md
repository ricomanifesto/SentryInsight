# Exploitation Report

Critical exploitation activity is surging across multiple threat vectors, with CISA flagging eight new vulnerabilities for active exploitation including a Bomgar RMM critical remote code execution flaw. Windows Defender is being weaponized through unpatched proof-of-concept exploits, while Apache ActiveMQ servers face widespread attacks affecting over 6,400 exposed systems. Meanwhile, threat actors are leveraging legitimate tools like Microsoft Teams for helpdesk impersonation attacks and deploying new malware variants including the Lotus data wiper targeting Venezuelan infrastructure and NGate Android malware exploiting NFC payment systems.

## Active Exploitation Details

### Bomgar RMM Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw in Bomgar remote monitoring and management tool that enables attackers to gain unauthorized system access
- **Impact**: Attackers can spread ransomware and compromise supply chains through the exploitation of this RMM platform
- **Status**: Actively exploited in attacks, represents significant supply chain risk
- **CVE ID**: CVE-2026-1731

### Catalyst SD-WAN Manager Vulnerability
- **Description**: New vulnerability in Catalyst SD-WAN Manager systems that CISA has flagged as actively exploited
- **Impact**: Attackers can compromise SD-WAN infrastructure and potentially gain network access
- **Status**: CISA has given U.S. government agencies four days to secure their systems
- **CVE ID**: Not specified in articles

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits targeting Microsoft's built-in security platform, turning the defense tool into an attacker asset
- **Impact**: Attackers can weaponize Windows Defender against the systems it's meant to protect
- **Status**: Two exploits remain unpatched and are being used in active attacks
- **CVE ID**: Not specified in articles

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: High-severity code injection vulnerability affecting Apache ActiveMQ message broker servers
- **Impact**: Remote code execution allowing attackers to compromise messaging infrastructure
- **Status**: Over 6,400 exposed servers vulnerable to ongoing attacks
- **CVE ID**: Not specified in articles

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in SGLang that enables remote code execution through malicious GGUF model files
- **Impact**: Attackers can achieve remote code execution on susceptible systems
- **Status**: Recently disclosed critical vulnerability
- **CVE ID**: CVE-2026-5760

### Google Antigravity IDE Prompt Injection Vulnerability
- **Description**: Vulnerability in Google's agentic AI-based integrated development environment enabling prompt injection attacks
- **Impact**: Sandbox escape and arbitrary code execution through sanitization bypass
- **Status**: Patched by Google
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Bomgar RMM**: Remote monitoring and management platforms vulnerable to critical RCE exploitation
- **Catalyst SD-WAN Manager**: SD-WAN infrastructure systems flagged by CISA for active exploitation
- **Windows Defender**: Microsoft's built-in security platform being weaponized by attackers
- **Apache ActiveMQ**: Message broker servers with over 6,400 exposed instances vulnerable to attacks
- **Lantronix and Silex Serial-to-IP Converters**: Over 22 vulnerabilities discovered in popular converter models
- **SGLang Systems**: AI/ML systems vulnerable to RCE through malicious model files
- **Google Antigravity IDE**: AI-based development environment affected by prompt injection issues
- **HandyPay NFC Application**: Legitimate mobile payment app being trojanized with NGate malware
- **Microsoft Teams**: Being increasingly abused for helpdesk impersonation attacks

## Attack Vectors and Techniques

- **Supply Chain Exploitation**: Attackers targeting RMM tools like Bomgar to spread ransomware across managed environments
- **Defense Evasion**: Weaponizing security tools like Windows Defender to turn them against protected systems
- **Network Infrastructure Targeting**: Active exploitation of SD-WAN and messaging infrastructure vulnerabilities
- **Social Engineering via Teams**: Threat actors impersonating helpdesk personnel through Microsoft Teams for initial access
- **Mobile Payment Fraud**: Trojanizing legitimate NFC payment applications to steal financial data and PINs
- **AI Model Poisoning**: Exploiting AI systems through malicious GGUF model files for remote code execution
- **Prompt Injection Attacks**: Bypassing AI system safeguards to achieve sandbox escape and code execution

## Threat Actor Activities

- **The Gentlemen Ransomware Group**: Deploying SystemBC proxy malware affecting over 1,570 corporate victims in bot-powered attacks
- **BlackCat/ALPHV Ransomware Operators**: Continued operations with insider negotiator pleading guilty to facilitating 2023 attacks
- **Scattered Spider Group**: Senior member pleaded guilty to wire fraud conspiracy and aggravated identity theft
- **Chinese APT Groups**: Targeting Indian banking sector and Korean policy circles with financial espionage operations
- **North Korean Lazarus Group**: Likely behind $290 million cryptocurrency heist targeting KelpDAO DeFi project
- **Venezuelan Infrastructure Attackers**: Deploying Lotus data wiper malware against energy and utility organizations
- **NGate Campaign Operators**: Targeting Brazilian users with trojanized HandyPay applications to steal NFC payment data
- **Cryptocurrency Scammers**: Infiltrating China's Apple App Store with 26 malicious wallet applications impersonating legitimate services