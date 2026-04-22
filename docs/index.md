# Exploitation Report

The current threat landscape reveals significant active exploitation across multiple critical vulnerabilities, with several high-impact attacks targeting enterprise infrastructure. Most concerning is the ongoing exploitation of a SharePoint spoofing vulnerability that was previously exploited as a zero-day and continues to affect over 1,300 unpatched servers worldwide. Additionally, threat actors are actively exploiting CVE-2026-1731 in Bomgar RMM tools to spread ransomware, while CVE-2026-5752 in Cohere AI's Terrarium sandbox enables container escapes. A new SD-WAN vulnerability has been flagged by CISA as actively exploited, and Apache ActiveMQ servers remain under assault through a high-severity code injection flaw affecting over 6,400 exposed systems.

## Active Exploitation Details

### SharePoint Spoofing Vulnerability
- **Description**: A spoofing vulnerability affecting Microsoft SharePoint servers that was initially exploited as a zero-day
- **Impact**: Allows attackers to conduct spoofing attacks against SharePoint installations
- **Status**: Over 1,300 servers remain unpatched and vulnerable to ongoing attacks despite patches being available

### Bomgar RMM Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in the Bomgar remote monitoring and management tool
- **Impact**: Enables attackers to execute arbitrary code remotely and spread ransomware through supply chain compromises
- **Status**: Actively exploited in the wild with significant supply chain risk implications
- **CVE ID**: CVE-2026-1731

### Cohere AI Terrarium Sandbox Vulnerability
- **Description**: Critical security vulnerability in the Python-based Terrarium sandbox environment
- **Impact**: Allows arbitrary code execution, root access, and container escape capabilities
- **Status**: Rated 9.3 severity, enabling complete sandbox compromise
- **CVE ID**: CVE-2026-5752

### Catalyst SD-WAN Manager Vulnerability
- **Description**: A newly identified vulnerability in Catalyst SD-WAN Manager systems
- **Impact**: Being actively exploited to compromise SD-WAN infrastructure
- **Status**: CISA has mandated federal agencies patch within four days due to active exploitation

### Apache ActiveMQ Code Injection Vulnerability
- **Description**: High-severity code injection vulnerability affecting Apache ActiveMQ message broker servers
- **Impact**: Enables remote code execution and system compromise
- **Status**: Over 6,400 exposed servers vulnerable to ongoing attacks

### ASP.NET Core Privilege Escalation
- **Description**: Critical privilege escalation vulnerability in ASP.NET Core framework
- **Impact**: Allows attackers to escalate privileges within ASP.NET applications
- **Status**: Microsoft released emergency out-of-band patches
- **CVE ID**: CVE-2026-40372

## Affected Systems and Products

- **Microsoft SharePoint**: Over 1,300 servers exposed online remain unpatched against spoofing attacks
- **Bomgar RMM Tools**: Remote monitoring and management systems vulnerable to ransomware distribution
- **Cohere AI Terrarium**: Python-based sandbox environments at risk of container escape
- **Catalyst SD-WAN Manager**: Software-defined wide area network management platforms
- **Apache ActiveMQ**: Message broker servers with 6,400+ exposed instances vulnerable
- **ASP.NET Core**: Web application framework requiring emergency patching
- **Lantronix and Silex Serial-to-IP Converters**: Over 20,000 devices affected by BRIDGE:BREAK vulnerabilities
- **Google Antigravity IDE**: Agentic integrated development environment with prompt injection risks
- **Microsoft Graph API**: Used maliciously by GoGra malware for command and control

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: SharePoint vulnerability was initially exploited before patches were available
- **Supply Chain Attacks**: Bomgar RMM exploitation used to spread ransomware across managed environments
- **Container Escape**: Terrarium sandbox vulnerability enables attackers to break out of isolated environments
- **Prompt Injection**: Google Antigravity IDE vulnerable to malicious prompt injection leading to code execution
- **Data Wiping Attacks**: Lotus Wiper malware targeting Venezuelan energy and utility infrastructure
- **Living-Off-The-Land**: GoGra malware abuses legitimate Microsoft Graph API for covert communications
- **Cross-App Permission Stacking**: Toxic combinations of permissions across applications create elevated risks
- **Android Malware Distribution**: NGate campaign trojanizes legitimate HandyPay app to steal NFC data

## Threat Actor Activities

- **Mustang Panda**: Deploying new LOTUSLITE variant targeting Indian banking sector and South Korean policy circles
- **The Gentlemen Ransomware**: Operating ransomware-as-a-service with 1,570+ victims identified through SystemBC proxy malware
- **Scattered Spider**: Member Tyler Robert Buchanan pleaded guilty to wire fraud and identity theft schemes
- **BlackCat/ALPHV Ransomware**: Former negotiator Angelo Martino pleaded guilty to conducting 2023 attacks against U.S. companies
- **Venezuelan Energy Sector Attackers**: Unknown threat actors deploying Lotus Wiper against critical infrastructure
- **French Government Breach**: Threat actor compromised France Titres agency and offered stolen citizen data for sale