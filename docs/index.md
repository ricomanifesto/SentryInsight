# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems across various sectors. The most severe threats include active exploitation of Bomgar RMM systems, Apache ActiveMQ servers, and Catalyst SD-WAN Manager vulnerabilities. Over 6,400 Apache ActiveMQ servers remain vulnerable to ongoing attacks, while threat actors are weaponizing legitimate security tools like Windows Defender for malicious purposes. Ransomware operations continue to evolve with The Gentlemen group deploying SystemBC proxy malware across more than 1,570 compromised hosts, and state-sponsored North Korean hackers conducting major cryptocurrency heists worth $290 million.

## Active Exploitation Details

### Bomgar RMM Critical Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw in the Bomgar remote monitoring and management tool
- **Impact**: Attackers can exploit this vulnerability to spread ransomware and compromise supply chains
- **Status**: Actively exploited in attacks with significant supply chain risk implications
- **CVE ID**: CVE-2026-1731

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: High-severity code injection vulnerability affecting Apache ActiveMQ message broker servers
- **Impact**: Enables attackers to execute arbitrary code on vulnerable systems
- **Status**: Currently being actively exploited with over 6,400 exposed servers identified as vulnerable
- **CVE ID**: Not specified in source material

### Catalyst SD-WAN Manager Vulnerability
- **Description**: New vulnerability in Catalyst SD-WAN Manager systems flagged by CISA
- **Impact**: Allows unauthorized access and potential network compromise
- **Status**: Actively exploited in attacks, with federal agencies given 4-day deadline to patch
- **CVE ID**: Not specified in source material

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits targeting Microsoft's built-in security platform
- **Impact**: Turns Windows Defender into an attacker tool for malicious purposes
- **Status**: Being used in active attacks with two exploits remaining unpatched
- **CVE ID**: Not specified in source material

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical vulnerability in SGLang that can be exploited via malicious GGUF model files
- **Impact**: Remote code execution on susceptible systems
- **Status**: Critical vulnerability with CVSS score of 9.8
- **CVE ID**: CVE-2026-5760

### Google Antigravity IDE Prompt Injection Flaw
- **Description**: Vulnerability in Google's agentic integrated development environment allowing prompt injection
- **Impact**: Enables sandbox escape and arbitrary code execution
- **Status**: Recently patched by Google
- **CVE ID**: Not specified in source material

## Affected Systems and Products

- **Bomgar RMM**: Remote monitoring and management systems across enterprise environments
- **Apache ActiveMQ**: Over 6,400 exposed message broker servers worldwide
- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management platforms
- **Microsoft Windows Defender**: Built-in security platform on Windows systems
- **SGLang**: AI/ML inference systems using GGUF model files
- **Google Antigravity IDE**: AI-based development environment for filesystem operations
- **Lantronix and Silex Serial-to-IP Converters**: Thousands of industrial communication devices
- **HandyPay NFC Applications**: Mobile payment processing tools on Android devices

## Attack Vectors and Techniques

- **Supply Chain Exploitation**: Targeting RMM tools to gain widespread access to customer networks
- **Code Injection**: Exploiting message broker vulnerabilities for arbitrary code execution
- **Security Tool Weaponization**: Converting legitimate security software into attack tools
- **Prompt Injection**: Manipulating AI systems to escape sandboxes and execute code
- **Social Engineering**: Microsoft Teams impersonation for helpdesk fraud schemes
- **Mobile Malware**: Trojanizing legitimate payment applications to steal NFC data
- **Proxy Botnets**: Using SystemBC malware for distributed command and control operations

## Threat Actor Activities

- **The Gentlemen Ransomware Group**: Operating SystemBC proxy malware botnet with 1,570+ compromised hosts for ransomware deployment
- **North Korean Lazarus Group**: Conducted $290 million cryptocurrency heist against KelpDAO DeFi project
- **Scattered Spider Member**: Tyler Buchanan pleaded guilty to wire fraud and identity theft charges
- **BlackCat Ransomware Negotiators**: Multiple individuals including Angelo Martino pleaded guilty to facilitating 2023 attacks
- **Chinese APT Groups**: Targeting Indian banking sector and Korean policy circles with espionage campaigns
- **NGate Malware Operators**: Distributing Android malware through trojanized HandyPay applications in Brazil
- **Cryptocurrency Thieves**: Infiltrating Apple App Store in China with 26 malicious wallet applications