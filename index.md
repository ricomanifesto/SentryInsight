# Exploitation Report

Critical exploitation activity continues across multiple attack vectors, with several high-severity vulnerabilities being actively exploited in the wild. CISA has flagged eight new vulnerabilities for its Known Exploited Vulnerabilities catalog, including active exploitation of Cisco Catalyst SD-WAN Manager flaws. Notable incidents include a prompt injection vulnerability in Google's Antigravity AI tool that enabled remote code execution, active exploitation of over 6,400 Apache ActiveMQ servers through a code injection flaw, and a critical SGLang vulnerability (CVE-2026-5760) with a CVSS score of 9.8 that enables remote code execution via malicious model files. The threat landscape also shows significant ransomware activity with BlackCat attacks, cryptocurrency theft operations targeting major DeFi platforms, and sophisticated mobile malware campaigns.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Vulnerability
- **Description**: CISA has flagged a new SD-WAN vulnerability as actively exploited in attacks
- **Impact**: Allows attackers to compromise SD-WAN infrastructure and potentially gain network access
- **Status**: U.S. government agencies given four days to secure systems against this actively exploited vulnerability

### Apache ActiveMQ Code Injection Flaw
- **Description**: High-severity code injection vulnerability affecting Apache ActiveMQ servers
- **Impact**: Enables remote code execution and system compromise
- **Status**: Over 6,400 servers exposed online are vulnerable to ongoing exploitation attacks

### Google Antigravity Prompt Injection Vulnerability
- **Description**: Prompt injection vulnerability in Google's agentic AI integrated development environment that allows sandbox escape
- **Impact**: Enables arbitrary code execution and remote code execution capabilities
- **Status**: Patched by Google, was a sanitization issue in the AI-based tool for filesystem operations

### SGLang Remote Code Execution Flaw
- **Description**: Critical security vulnerability in SGLang that could result in remote code execution on susceptible systems
- **Impact**: Remote code execution via malicious GGUF model files
- **Status**: Recently disclosed critical vulnerability
- **CVE ID**: CVE-2026-5760

### Anthropic MCP Design Weakness
- **Description**: Critical "by design" weakness in the Model Context Protocol's architecture
- **Impact**: Could enable remote code execution with cascading effects on AI supply chain
- **Status**: Design vulnerability affecting MCP architecture

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: CISA-flagged vulnerability affecting SD-WAN infrastructure
- **Apache ActiveMQ**: Over 6,400 servers exposed online vulnerable to code injection attacks
- **Google Antigravity**: AI-based integrated development environment with filesystem operations
- **SGLang**: Machine learning framework vulnerable to RCE via malicious model files
- **Anthropic Model Context Protocol**: Architecture design weakness affecting AI supply chain
- **HandyPay NFC Application**: Legitimate mobile payments app trojanized by NGate malware
- **Apple App Store (China)**: 26 malicious cryptocurrency wallet apps impersonating legitimate services
- **Microsoft Teams**: Platform increasingly abused for helpdesk impersonation attacks
- **Serial-to-IP Devices**: OT devices with thousands of vulnerabilities being targeted more frequently

## Attack Vectors and Techniques

- **Prompt Injection**: Exploiting AI systems through malicious prompts to achieve code execution
- **Code Injection**: Targeting Apache ActiveMQ servers for remote code execution
- **Malicious Model Files**: Using crafted GGUF files to achieve RCE in SGLang systems
- **Mobile Malware**: NGate Android malware hiding in trojanized legitimate applications
- **App Store Infiltration**: Fake cryptocurrency wallet apps stealing seed phrases and recovery data
- **Social Engineering**: Microsoft Teams abuse for helpdesk impersonation and credential theft
- **OAuth Token Theft**: Targeting OAuth tokens as new attack surface for lateral movement
- **NFC Data Theft**: Stealing Near Field Communication payment data and PINs through mobile malware

## Threat Actor Activities

- **Scattered Spider**: British member Tyler Robert Buchanan pleaded guilty to wire fraud and identity theft charges
- **BlackCat/ALPHV Ransomware**: Angelo Martino, former ransomware negotiator, pleaded guilty to conducting attacks against U.S. companies in 2023
- **Lazarus Group**: North Korean state-sponsored hackers likely behind $290 million KelpDAO cryptocurrency heist
- **Chinese APT Groups**: Targeting Indian banks and Korean policy circles with espionage operations
- **The Gentlemen Ransomware**: Now using SystemBC proxy malware botnet with over 1,570 compromised hosts
- **NGate Campaign**: Targeting Brazilian users through trojanized HandyPay application for NFC data theft
- **Cryptocurrency Scammers**: Operating 26 malicious wallet apps on Apple App Store in China
- **Website Defacement Groups**: Attacking Seiko USA website and claiming customer data theft from Shopify database