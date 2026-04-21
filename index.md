# Exploitation Report

Critical exploitation activity is currently targeting multiple high-impact systems across various sectors. The most significant threats include active exploitation of Bomgar RMM systems enabling ransomware deployment and supply chain attacks, ongoing attacks against Apache ActiveMQ servers affecting over 6,400 systems worldwide, and CISA-flagged exploitation of Catalyst SD-WAN Manager vulnerabilities. Additionally, a critical SGLang vulnerability with a CVSS score of 9.8 is enabling remote code execution through malicious model files, while Google has patched a critical prompt injection flaw in their AI-based Antigravity IDE tool that allowed sandbox escape and arbitrary code execution.

## Active Exploitation Details

### Bomgar RMM Critical Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in Bomgar remote monitoring and management tool that enables attackers to compromise systems and spread malware
- **Impact**: Ransomware deployment, supply chain compromise, and lateral movement across managed networks
- **Status**: Currently being actively exploited in the wild
- **CVE ID**: CVE-2026-1731

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: High-severity code injection vulnerability in Apache ActiveMQ message broker systems exposed to the internet
- **Impact**: Remote code execution and complete system compromise of message broker infrastructure
- **Status**: Actively exploited with over 6,400 vulnerable servers identified by Shadowserver

### Catalyst SD-WAN Manager Vulnerability
- **Description**: CISA-flagged vulnerability in Cisco Catalyst SD-WAN Manager systems being actively exploited
- **Impact**: Network infrastructure compromise and potential lateral movement across SD-WAN environments
- **Status**: Active exploitation confirmed by CISA, federal agencies given 4-day remediation deadline

### SGLang Remote Code Execution via Malicious Model Files
- **Description**: Critical vulnerability in SGLang framework that allows remote code execution through malicious GGUF model files
- **Impact**: Complete system compromise when processing untrusted AI model files
- **Status**: Recently disclosed with patches available
- **CVE ID**: CVE-2026-5760

### Google Antigravity IDE Prompt Injection Vulnerability
- **Description**: Critical prompt injection vulnerability in Google's AI-based Antigravity IDE tool that allows sandbox escape
- **Impact**: Arbitrary code execution through filesystem operations and sandbox bypass
- **Status**: Recently patched by Google

## Affected Systems and Products

- **Bomgar RMM Systems**: Remote monitoring and management infrastructure used by managed service providers
- **Apache ActiveMQ Servers**: Over 6,400 internet-exposed message broker systems
- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management systems in enterprise environments
- **SGLang Framework**: AI/ML systems processing GGUF model files
- **Google Antigravity IDE**: AI-powered integrated development environment for filesystem operations
- **Lantronix and Silex Serial-to-IP Converters**: Industrial OT devices with 22 newly discovered vulnerabilities

## Attack Vectors and Techniques

- **Remote Code Execution**: Direct exploitation of RCE vulnerabilities in Bomgar RMM and Apache ActiveMQ systems
- **Prompt Injection**: AI system manipulation through crafted prompts to achieve code execution in Antigravity IDE
- **Malicious Model Files**: Weaponized GGUF files targeting SGLang framework for remote code execution
- **Supply Chain Attacks**: Exploitation of managed service provider tools like Bomgar to compromise downstream clients
- **Network Infrastructure Targeting**: Direct attacks against SD-WAN management systems for network-wide access

## Threat Actor Activities

- **BlackCat/ALPHV Ransomware Operations**: Former cybersecurity negotiator Angelo Martino pleaded guilty to conducting BlackCat ransomware attacks against U.S. companies in 2023
- **Scattered Spider Group**: British national Tyler Robert Buchanan, a senior member, pleaded guilty to wire fraud conspiracy and aggravated identity theft
- **Lazarus Group**: North Korean state-sponsored hackers suspected in $290 million KelpDAO cryptocurrency heist
- **Chinese APT Groups**: Targeting Indian financial sector and Korean policy circles with relatively unsophisticated but persistent campaigns
- **The Gentlemen Ransomware**: Now utilizing SystemBC proxy malware botnet comprising over 1,570 compromised hosts for enhanced attack capabilities