# Exploitation Report

Current threat activity demonstrates a concerning landscape of active exploitation targeting critical infrastructure, enterprise systems, and financial platforms. Key incidents include active attacks against Apache ActiveMQ servers with over 6,400 systems vulnerable to code injection attacks, a critical SGLang vulnerability enabling remote code execution through malicious model files, and sophisticated malware campaigns including ZionSiphon targeting Israeli water systems and NGate Android malware stealing NFC payment data. Notable threat actor activities include Chinese APT groups targeting Indian financial institutions, North Korean Lazarus hackers conducting a $290 million cryptocurrency heist, and widespread supply chain compromises affecting major platforms like Vercel and Apple's App Store.

## Active Exploitation Details

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: High-severity code injection vulnerability affecting Apache ActiveMQ message broker servers
- **Impact**: Allows remote attackers to execute arbitrary code on vulnerable servers
- **Status**: Actively exploited in the wild with over 6,400 exposed servers vulnerable to ongoing attacks

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in SGLang that enables remote code execution through malicious GGUF model files
- **Impact**: Successful exploitation results in complete system compromise and remote code execution
- **Status**: Recently disclosed with proof-of-concept available
- **CVE ID**: CVE-2026-5760

### Google Antigravity IDE Prompt Injection Flaw
- **Description**: Vulnerability in Google's agentic integrated development environment allowing prompt injection attacks
- **Impact**: Enables code execution through manipulated prompts in the AI-powered IDE
- **Status**: Patched by Google following responsible disclosure

### Anthropic MCP Design Vulnerability
- **Description**: Critical "by design" weakness in the Model Context Protocol's architecture
- **Impact**: Could enable remote code execution and cascading effects across AI supply chain
- **Status**: Newly discovered architectural flaw requiring protocol-level fixes

## Affected Systems and Products

- **Apache ActiveMQ**: Over 6,400 servers exposed online vulnerable to code injection attacks
- **SGLang Framework**: AI inference systems processing GGUF model files susceptible to malicious payloads
- **Google Antigravity IDE**: AI-powered development environment vulnerable to prompt injection
- **Microsoft Teams**: Increasingly abused platform for helpdesk impersonation and social engineering
- **HandyPay NFC Application**: Legitimate mobile payment app trojanized to deliver NGate malware
- **Vercel Infrastructure**: Web development platform compromised through third-party AI tool access
- **Apple App Store China**: 26 malicious cryptocurrency wallet applications discovered
- **Israeli Water Systems**: Critical infrastructure targeted by ZionSiphon malware
- **Serial-to-IP Devices**: OT/ICS systems with thousands of legacy and new vulnerabilities

## Attack Vectors and Techniques

- **Code Injection**: Remote exploitation of Apache ActiveMQ servers through injection vulnerabilities
- **Malicious Model Files**: SGLang systems compromised through weaponized GGUF files
- **Prompt Injection**: AI development environments manipulated through crafted input prompts
- **Supply Chain Compromise**: Third-party AI tools used as entry points for broader infrastructure access
- **Mobile App Trojanization**: Legitimate applications repackaged with malicious functionality
- **NFC Data Theft**: Android malware capturing payment card data through compromised NFC applications
- **Social Engineering**: Microsoft Teams platform abuse for helpdesk impersonation attacks
- **OAuth Token Theft**: Stolen authentication tokens enabling lateral movement and persistent access

## Threat Actor Activities

- **Chinese APT Groups**: Targeting Indian financial institutions and Korean policy organizations using established tactics, techniques, and procedures
- **Lazarus Group (North Korea)**: Conducted $290 million cryptocurrency heist against KelpDAO DeFi platform
- **Scattered Spider Collective**: British leader pleaded guilty to wire fraud and cryptocurrency theft charges
- **BlackCat Ransomware Operators**: Former cybersecurity negotiator pleaded guilty to participating in ransomware attacks in 2023
- **NGate Campaign Actors**: Targeting Brazilian users with trojanized HandyPay applications to steal NFC payment data
- **The Gentlemen Ransomware**: Now utilizing SystemBC proxy malware botnet with over 1,570 compromised corporate hosts
- **ZionSiphon Operators**: Specifically targeting Israeli water treatment and desalination operational technology systems
- **Cryptocurrency Wallet Scammers**: Deployed 26 malicious applications on Apple's App Store in China impersonating legitimate wallets