# Exploitation Report

Critical vulnerability exploitation continues across multiple attack vectors, with Microsoft, Google, and Cisco systems under active attack. Key highlights include Microsoft's emergency patching of a critical ASP.NET Core privilege escalation vulnerability, ongoing exploitation of over 1,300 unpatched SharePoint servers through a spoofing vulnerability that was previously exploited as a zero-day, and CISA flagging a new SD-WAN flaw as actively exploited. Additional critical issues include a sandbox escape vulnerability in Cohere AI's Terrarium tool rated 9.3, Windows Defender being weaponized through unpatched exploits, and over 6,400 Apache ActiveMQ servers vulnerable to ongoing code injection attacks. The Bomgar RMM exploitation surge demonstrates significant supply chain risks through CVE-2026-1731.

## Active Exploitation Details

### Microsoft ASP.NET Core Privilege Escalation Vulnerability
- **Description**: Critical privilege escalation flaw in ASP.NET Core requiring emergency out-of-band security updates
- **Impact**: Allows attackers to escalate privileges within affected systems
- **Status**: Microsoft has released emergency patches to address the vulnerability

### Microsoft SharePoint Spoofing Vulnerability
- **Description**: Spoofing vulnerability affecting SharePoint servers that was previously exploited as a zero-day
- **Impact**: Enables spoofing attacks against vulnerable SharePoint installations
- **Status**: Over 1,300 servers remain unpatched and vulnerable to ongoing attacks

### Cohere AI Terrarium Sandbox Vulnerability
- **Description**: Critical security vulnerability in Python-based Terrarium sandbox allowing arbitrary code execution
- **Impact**: Enables root code execution and container escape
- **Status**: Vulnerability has been disclosed with critical severity rating
- **CVE ID**: CVE-2026-5752

### Cisco Catalyst SD-WAN Manager Vulnerability
- **Description**: New vulnerability in SD-WAN systems flagged by CISA as actively exploited
- **Impact**: Allows attackers to compromise SD-WAN infrastructure
- **Status**: CISA has given U.S. government agencies four days to secure systems

### Bomgar RMM Critical Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in Bomgar remote monitoring and management tool
- **Impact**: Can be exploited to spread ransomware and compromise supply chains
- **Status**: Actively exploited with surge in activity
- **CVE ID**: CVE-2026-1731

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: High-severity code injection vulnerability affecting Apache ActiveMQ servers
- **Impact**: Enables code injection attacks against vulnerable servers
- **Status**: Over 6,400 servers exposed online remain vulnerable to ongoing attacks

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits turning Windows Defender into an attacker tool
- **Impact**: Microsoft's built-in security platform weaponized for malicious purposes
- **Status**: Two exploits remain unpatched and are being used in active attacks

### Google Antigravity IDE Prompt Injection Vulnerability
- **Description**: Vulnerability in Google's agentic integrated development environment enabling prompt injection
- **Impact**: Allows sandbox escape and arbitrary code execution through sanitization bypass
- **Status**: Google has patched the vulnerability

## Affected Systems and Products

- **Microsoft ASP.NET Core**: Web application framework requiring emergency patches
- **Microsoft SharePoint Servers**: Over 1,300 exposed servers remain vulnerable to spoofing attacks
- **Cohere AI Terrarium**: Python-based sandbox environment with container escape vulnerability
- **Cisco Catalyst SD-WAN Manager**: Network infrastructure systems under active exploitation
- **Bomgar RMM**: Remote monitoring and management platform with critical RCE flaw
- **Apache ActiveMQ**: Message broker servers with over 6,400 vulnerable instances exposed online
- **Windows Defender**: Microsoft's built-in security platform being weaponized
- **Google Antigravity IDE**: AI-based development environment with prompt injection flaw
- **Lantronix and Silex Serial-to-IP Converters**: Industrial devices affected by 22 BRIDGE:BREAK vulnerabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: SharePoint spoofing vulnerability previously exploited before patches were available
- **Emergency Patch Requirements**: Critical ASP.NET Core vulnerability requiring immediate out-of-band updates
- **Supply Chain Attacks**: Bomgar RMM exploitation used to spread ransomware across supply chains
- **Container Escape**: Terrarium sandbox vulnerability enabling escape to host system with root privileges
- **Code Injection**: Apache ActiveMQ servers vulnerable to injection attacks through exposed interfaces
- **Security Tool Weaponization**: Windows Defender exploits turning defensive tools into attack vectors
- **Prompt Injection**: AI system manipulation through crafted inputs in Google Antigravity IDE
- **Infrastructure Targeting**: SD-WAN systems compromised to disrupt network communications

## Threat Actor Activities

- **Mustang Panda**: Chinese APT group deploying new LOTUSLITE variant targeting India banks and South Korea policy circles
- **BlackCat/ALPHV Ransomware**: Former negotiator Angelo Martino pleaded guilty to conducting ransomware attacks against U.S. companies in 2023
- **The Gentlemen Ransomware**: RaaS operation with 1,570+ victims revealed through SystemBC C2 server analysis
- **Scattered Spider**: Senior member Tyler Robert Buchanan pleaded guilty to wire fraud conspiracy and aggravated identity theft
- **Lazarus Group**: North Korean state-sponsored hackers likely behind $290 million KelpDAO cryptocurrency heist
- **NGate Campaign**: Android malware operators targeting Brazil through trojanized HandyPay application to steal NFC payment data
- **Lotus Data Wiper**: Previously undocumented malware used in targeted attacks against Venezuelan energy and utility organizations