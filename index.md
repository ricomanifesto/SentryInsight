# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure and remote management tools, with attackers leveraging both zero-day vulnerabilities and recently discovered flaws. The most concerning developments include active exploitation of Windows Defender through proof-of-concept exploits, ongoing attacks against Cisco Catalyst SD-WAN Manager systems, and widespread targeting of Apache ActiveMQ servers. Additionally, threat actors are increasingly abusing legitimate collaboration tools like Microsoft Teams for social engineering attacks and deploying sophisticated malware campaigns targeting financial institutions and cryptocurrency platforms.

## Active Exploitation Details

### Windows Defender Security Platform Exploits
- **Description**: Three proof-of-concept exploits are being used in active attacks against Microsoft's built-in security platform
- **Impact**: Attackers can turn Windows Defender into an attack tool, compromising the system's primary security defense
- **Status**: Two of the three exploits remain unpatched, indicating ongoing vulnerability exposure

### Cisco Catalyst SD-WAN Manager Vulnerability
- **Description**: A critical vulnerability in Catalyst SD-WAN Manager systems is being actively exploited in attacks
- **Impact**: Successful exploitation allows attackers to compromise SD-WAN infrastructure and potentially access connected networks
- **Status**: CISA has flagged this as actively exploited and given U.S. government agencies four days to secure their systems

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: A high-severity code injection vulnerability affecting Apache ActiveMQ servers
- **Impact**: Attackers can execute arbitrary code on vulnerable servers, leading to system compromise
- **Status**: Over 6,400 exposed servers are currently vulnerable to ongoing attacks

### Bomgar RMM Critical Remote Code Execution
- **Description**: A critical remote code execution flaw in the Bomgar remote monitoring and management tool
- **Impact**: Exploitation can lead to ransomware deployment and supply chain compromise
- **Status**: Active exploitation demonstrates significant supply chain risk
- **CVE ID**: CVE-2026-1731

### Google Antigravity IDE Prompt Injection
- **Description**: A prompt injection vulnerability in Google's agentic AI-based Antigravity IDE affecting filesystem operations
- **Impact**: Enables sandbox escape and arbitrary code execution through AI prompt manipulation
- **Status**: Critical RCE flaw has been patched by Google

### SGLang Remote Code Execution
- **Description**: A critical vulnerability in SGLang that enables remote code execution via malicious GGUF model files
- **Impact**: Successful exploitation results in complete system compromise
- **Status**: Critical severity with CVSS score of 9.8
- **CVE ID**: CVE-2026-5760

## Affected Systems and Products

- **Microsoft Windows Defender**: Built-in security platform vulnerable to proof-of-concept exploits
- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management systems under active attack
- **Apache ActiveMQ**: Over 6,400 exposed message broker servers vulnerable to code injection
- **Bomgar RMM**: Remote monitoring and management tool experiencing surge in exploitation
- **Google Antigravity IDE**: AI-based integrated development environment for filesystem operations
- **Lantronix and Silex Serial-to-IP Converters**: Industrial devices exposed to 22 BRIDGE:BREAK vulnerabilities
- **SGLang Framework**: Machine learning inference framework vulnerable to malicious model files
- **Microsoft Teams**: Collaboration platform increasingly abused for social engineering attacks
- **Android NFC Payment Systems**: HandyPay and related applications targeted by NGate malware

## Attack Vectors and Techniques

- **Proof-of-Concept Exploit Weaponization**: Security researchers' proof-of-concept code being used in active attacks against Windows Defender
- **SD-WAN Infrastructure Targeting**: Direct exploitation of network management vulnerabilities for infrastructure compromise
- **Message Broker Exploitation**: Code injection attacks against exposed Apache ActiveMQ servers
- **Supply Chain Attacks**: Exploitation of remote management tools to spread ransomware and compromise connected organizations
- **AI Prompt Injection**: Manipulation of AI systems through crafted prompts to achieve code execution
- **Social Engineering via Collaboration Tools**: Threat actors impersonating IT helpdesk personnel through Microsoft Teams
- **Malicious Model File Distribution**: Distribution of weaponized machine learning model files to achieve remote code execution
- **NFC Payment Data Theft**: Trojanized mobile applications stealing Near Field Communication payment data and PINs

## Threat Actor Activities

- **The Gentlemen Ransomware Group**: Deploying SystemBC proxy malware across a botnet of over 1,570 corporate victims for bot-powered attacks
- **BlackCat/ALPHV Ransomware Operators**: Continuing attacks against U.S. companies with insider negotiators pleading guilty to conspiracy charges
- **Scattered Spider Cybercrime Group**: Senior member Tyler Robert Buchanan pleaded guilty to wire fraud conspiracy and identity theft
- **Chinese APT Groups**: Targeting Indian financial institutions and Korean policy circles with minimal operational security
- **Lazarus Group (North Korean APT)**: Suspected involvement in $290 million cryptocurrency heist against KelpDAO DeFi project
- **NGate Malware Operators**: Targeting Brazilian users with trojanized mobile payment applications to steal NFC payment data
- **Lotus Data Wiper Attackers**: Conducting targeted attacks against Venezuelan energy and utility organizations
- **French Government Data Breach**: Threat actors compromising France Titres agency and offering stolen citizen data for sale
- **Cryptocurrency Wallet Impersonators**: Distributing 26 malicious apps on Apple App Store impersonating popular wallet applications