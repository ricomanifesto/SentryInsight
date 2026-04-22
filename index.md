# Exploitation Report

Current exploitation activity reveals multiple critical vulnerabilities being actively targeted, including unpatched Windows Defender exploits, a Bomgar RMM remote code execution flaw (CVE-2026-1731), and newly added CISA KEV vulnerabilities affecting Cisco Catalyst SD-WAN Manager and Apache ActiveMQ systems. Threat actors are leveraging these vulnerabilities alongside sophisticated malware campaigns, with over 6,400 Apache ActiveMQ servers currently exposed to ongoing attacks and ransomware operations using proxy botnets to target corporate networks.

## Active Exploitation Details

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits targeting Microsoft's built-in security platform are being used in active attacks
- **Impact**: Attackers can turn Windows Defender into an attack tool, compromising the security platform itself
- **Status**: Two of the three exploits remain unpatched, indicating ongoing vulnerability

### Bomgar RMM Remote Code Execution
- **Description**: Critical remote code execution vulnerability in the remote monitoring and management tool
- **Impact**: Exploitation enables ransomware deployment and supply chain compromise
- **Status**: Currently being exploited to spread ransomware
- **CVE ID**: CVE-2026-1731

### Catalyst SD-WAN Manager Vulnerability
- **Description**: Critical vulnerability in Cisco's SD-WAN Manager infrastructure
- **Impact**: Network compromise and unauthorized access to enterprise SD-WAN deployments
- **Status**: Actively exploited in attacks, flagged by CISA with 4-day remediation deadline

### Apache ActiveMQ Code Injection
- **Description**: High-severity code injection vulnerability in Apache ActiveMQ message broker
- **Impact**: Remote code execution and system compromise
- **Status**: Over 6,400 servers exposed online are vulnerable to ongoing attacks

### Google Antigravity AI Tool RCE
- **Description**: Prompt injection vulnerability in Google's agentic AI product for filesystem operations
- **Impact**: Sandbox escape and arbitrary code execution through sanitization bypass
- **Status**: Recently patched by Google

### SGLang Remote Code Execution
- **Description**: Critical vulnerability in SGLang that enables remote code execution via malicious GGUF model files
- **Impact**: Remote code execution on susceptible systems
- **Status**: High severity with CVSS 9.8 score
- **CVE ID**: CVE-2026-5760

## Affected Systems and Products

- **Microsoft Windows Defender**: Built-in security platform vulnerable to exploitation techniques
- **Bomgar RMM**: Remote monitoring and management infrastructure
- **Cisco Catalyst SD-WAN Manager**: Enterprise network management systems
- **Apache ActiveMQ**: Message broker services with 6,400+ exposed servers
- **Google Antigravity**: AI-based development environment and filesystem tools
- **Lantronix and Silex Serial-to-IP Converters**: Industrial OT devices with 22 newly discovered vulnerabilities
- **SGLang**: Large language model serving framework
- **HandyPay NFC Application**: Mobile payment processing platform targeted by NGate malware
- **Vercel Development Platform**: OAuth token compromise affecting customer data

## Attack Vectors and Techniques

- **Proof-of-Concept Exploit Weaponization**: Active use of POC exploits against Windows Defender
- **Supply Chain Targeting**: RMM tool exploitation for downstream customer compromise
- **Prompt Injection Attacks**: AI tool manipulation for sandbox escape and code execution
- **Malicious Model File Distribution**: GGUF files weaponized for remote code execution
- **NFC Data Theft**: Android malware trojanizing legitimate payment applications
- **OAuth Token Abuse**: Stolen authentication tokens for lateral movement and data access
- **Helpdesk Impersonation**: Microsoft Teams abuse for social engineering attacks
- **Proxy Botnet Operations**: SystemBC malware creating corporate victim networks

## Threat Actor Activities

- **The Gentlemen Ransomware**: Deploying SystemBC proxy malware across 1,570+ victim hosts for bot-powered attacks
- **Scattered Spider Member**: Senior member Tyler Robert Buchanan pleaded guilty to wire fraud conspiracy and identity theft
- **BlackCat Ransomware Associates**: Former DigitalMint employee Angelo Martino pleaded guilty to conducting 2023 ransomware attacks
- **North Korean Lazarus Group**: Suspected involvement in $290 million KelpDAO cryptocurrency heist
- **Chinese APT Operations**: Targeting Indian financial sector and Korean policy circles with dated techniques
- **Venezuelan Energy Sector Attackers**: Deploying Lotus data wiper malware against energy and utility organizations
- **Cryptocurrency Theft Operations**: 26 malicious wallet apps infiltrating China's Apple App Store to steal recovery phrases