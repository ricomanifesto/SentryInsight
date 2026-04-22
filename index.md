# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value platforms with attackers leveraging both newly discovered vulnerabilities and established attack vectors. The most concerning developments include active exploitation of Catalyst SD-WAN Manager vulnerabilities flagged by CISA, widespread targeting of over 6,400 Apache ActiveMQ servers through code injection attacks, and the abuse of Windows Defender through unpatched proof-of-concept exploits. Additionally, ransomware operations continue to evolve with The Gentlemen group deploying SystemBC proxy malware across more than 1,570 victim networks, while serial-to-IP converters face exposure through 22 newly identified BRIDGE:BREAK vulnerabilities affecting thousands of industrial devices.

## Active Exploitation Details

### Catalyst SD-WAN Manager Vulnerability
- **Description**: A critical vulnerability in Cisco Catalyst SD-WAN Manager that CISA has flagged for active exploitation
- **Impact**: Allows attackers to compromise SD-WAN infrastructure and potentially pivot to connected networks
- **Status**: Actively exploited in attacks; CISA has mandated federal agencies patch within four days

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: A high-severity code injection vulnerability affecting Apache ActiveMQ message broker servers
- **Impact**: Enables attackers to execute arbitrary code on vulnerable servers
- **Status**: Over 6,400 servers exposed online are vulnerable to ongoing attacks

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits targeting Microsoft's built-in security platform
- **Impact**: Turns Windows Defender into an attacker tool, potentially bypassing security measures
- **Status**: Two exploits remain unpatched and are being used in active attacks

### Bomgar RMM Remote Code Execution
- **Description**: A critical remote code execution flaw in the Bomgar remote monitoring and management tool
- **Impact**: Can be exploited to spread ransomware and compromise supply chains
- **Status**: Experiencing a surge in exploitation activity
- **CVE ID**: CVE-2026-1731

### SGLang Remote Code Execution
- **Description**: A critical vulnerability in SGLang that enables remote code execution through malicious GGUF model files
- **Impact**: Allows attackers to execute arbitrary code on susceptible systems
- **Status**: Recently disclosed with proof-of-concept available
- **CVE ID**: CVE-2026-5760

### Google Antigravity IDE Prompt Injection
- **Description**: A prompt injection vulnerability in Google's agentic AI product for filesystem operations
- **Impact**: Enables sandbox escape and arbitrary code execution through sanitization bypass
- **Status**: Recently patched by Google

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Enterprise SD-WAN infrastructure components
- **Apache ActiveMQ**: Message broker servers with over 6,400 instances exposed online
- **Microsoft Windows Defender**: Built-in security platform across Windows environments
- **Bomgar RMM**: Remote monitoring and management tools used in enterprise environments
- **Lantronix and Silex Serial-to-IP Converters**: Thousands of industrial device converters affected by 22 vulnerabilities
- **SGLang**: Machine learning language processing systems
- **Google Antigravity IDE**: AI-based development environment platform
- **HandyPay NFC Application**: Mobile payment processing tools targeted by NGate malware
- **KelpDAO DeFi Platform**: Cryptocurrency platform suffering $290 million loss
- **Microsoft Teams**: Enterprise collaboration platform increasingly abused for social engineering

## Attack Vectors and Techniques

- **Code Injection**: Exploitation of Apache ActiveMQ servers through high-severity injection vulnerabilities
- **Proof-of-Concept Weaponization**: Active use of PoC exploits against Windows Defender with two remaining unpatched
- **Supply Chain Attacks**: Targeting of RMM tools to compromise multiple downstream organizations
- **Prompt Injection**: Malicious manipulation of AI systems to achieve code execution and sandbox escape
- **NFC Data Theft**: Trojanized mobile applications stealing payment card data and PINs
- **Social Engineering**: Helpdesk impersonation attacks through Microsoft Teams external collaboration
- **Proxy Malware Deployment**: SystemBC botnet operations across corporate networks
- **Data Wiping Operations**: Lotus malware targeting energy and utility infrastructure

## Threat Actor Activities

- **The Gentlemen Ransomware Group**: Operating a SystemBC proxy malware botnet affecting over 1,570 corporate victims for ransomware deployment
- **BlackCat/ALPHV Operators**: Continuing ransomware operations with insider negotiator involvement in 2023 attacks
- **Scattered Spider Members**: Senior members facing legal consequences with Tyler Robert Buchanan pleading guilty to wire fraud and identity theft
- **North Korean Lazarus Group**: Suspected involvement in $290 million KelpDAO cryptocurrency heist
- **Chinese APT Groups**: Targeting Indian banking sector and Korean policy circles with espionage operations
- **Venezuelan Energy Sector Attackers**: Deploying Lotus data wiper against energy and utility organizations
- **NGate Malware Operators**: Targeting Brazilian Android users through trojanized HandyPay applications
- **French Government Data Thieves**: Breaching France Titres agency and offering stolen citizen data for sale