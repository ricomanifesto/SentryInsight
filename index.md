# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms including D-Link routers, Microsoft SharePoint servers, and supply chain infrastructure. Most notably, CVE-2025-29635 is being actively exploited by Mirai botnet campaigns against end-of-life D-Link routers, while over 1,300 Microsoft SharePoint servers remain vulnerable to ongoing spoofing attacks that were previously exploited as zero-days. Microsoft has released emergency patches for CVE-2026-40372, a critical ASP.NET Core privilege escalation vulnerability. Additionally, sophisticated supply chain attacks are targeting npm packages and Docker repositories, with ransomware operations like "The Gentlemen" rapidly scaling their activities using advanced techniques.

## Active Exploitation Details

### D-Link Router Command Injection Vulnerability
- **Description**: High-severity command-injection vulnerability affecting D-Link DIR-823X routers that allows remote code execution
- **Impact**: Attackers can execute arbitrary commands and enlist devices into Mirai botnets for distributed attacks
- **Status**: Actively exploited by new Mirai campaign; affects end-of-life devices with no patches available
- **CVE ID**: CVE-2025-29635

### Microsoft SharePoint Spoofing Vulnerability
- **Description**: Spoofing vulnerability in Microsoft SharePoint servers that was previously exploited as a zero-day
- **Impact**: Attackers can conduct spoofing attacks against SharePoint installations
- **Status**: Actively exploited in ongoing attacks; patches available but over 1,300 servers remain unpatched

### ASP.NET Core Privilege Escalation Vulnerability
- **Description**: Critical privilege escalation vulnerability in ASP.NET Core framework
- **Impact**: Attackers can escalate privileges within affected ASP.NET Core applications
- **Status**: Emergency patches released by Microsoft in out-of-band updates
- **CVE ID**: CVE-2026-40372

### Cohere AI Terrarium Sandbox Vulnerability
- **Description**: Critical security flaw in Python-based Terrarium sandbox allowing arbitrary code execution and container escape
- **Impact**: Root code execution and container escape capabilities
- **Status**: Critical vulnerability with CVSS rating of 9.3
- **CVE ID**: CVE-2026-5752

### Bomgar RMM Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in Bomgar remote monitoring and management tool
- **Impact**: Can be exploited to spread ransomware and compromise supply chains
- **Status**: Experiencing surge in exploitation activity
- **CVE ID**: CVE-2026-1731

## Affected Systems and Products

- **D-Link DIR-823X Routers**: End-of-life devices vulnerable to command injection attacks
- **Microsoft SharePoint Servers**: Over 1,300 internet-exposed servers remain unpatched against spoofing attacks
- **ASP.NET Core Applications**: All versions affected by privilege escalation vulnerability
- **npm Package Ecosystem**: Multiple compromised packages targeting developer authentication tokens
- **Docker Hub Repositories**: Malicious images in official Checkmarx KICS repository
- **VS Code Extensions**: Malicious extensions targeting the Checkmarx supply chain
- **Cohere AI Terrarium**: Python-based sandbox with critical code execution flaw
- **Bomgar RMM**: Remote monitoring and management tool with RCE vulnerability
- **iOS/iPadOS Devices**: Notification Services flaw allowing deleted notification data retention
- **Lantronix and Silex Serial-to-IP Converters**: 22 vulnerabilities exposed in thousands of devices

## Attack Vectors and Techniques

- **Command Injection**: Mirai campaigns exploiting D-Link router vulnerabilities to build botnets
- **Supply Chain Poisoning**: Self-propagating worms targeting npm packages and Docker repositories
- **Privilege Escalation**: Exploitation of ASP.NET Core framework vulnerabilities
- **Container Escape**: Terrarium sandbox exploitation for arbitrary code execution
- **Social Engineering**: DPRK fake job scams using "Contagious Interview" techniques
- **Notification Data Persistence**: Exploitation of iOS bug to recover deleted Signal messages
- **Microsoft Graph API Abuse**: GoGra backdoor using legitimate Microsoft infrastructure for C2 communications
- **Post-Quantum Encryption**: Kyber ransomware implementing advanced encryption techniques
- **RMM Tool Exploitation**: Bomgar platform compromise for ransomware distribution

## Threat Actor Activities

- **Mirai Operators**: Actively exploiting D-Link router vulnerabilities to expand botnet infrastructure
- **The Gentlemen Ransomware**: Rapidly scaling operations with sophisticated techniques and over 1,570 victims identified through SystemBC C2 infrastructure
- **Kyber Ransomware Gang**: Targeting Windows and VMware ESXi systems with post-quantum encryption variants
- **Harvester Group**: Deploying Linux GoGra backdoor in South Asia using Microsoft Graph API for stealth communications
- **Mustang Panda**: Distributing new LOTUSLITE variant targeting Indian banking sector and South Korean policy circles
- **Scattered Spider Member**: Tyler Robert Buchanan pleading guilty to wire fraud conspiracy and aggravated identity theft
- **DPRK-linked Actors**: Conducting fake job scams with self-propagating malware distribution
- **Supply Chain Attackers**: Targeting npm ecosystem with self-spreading worms to steal developer tokens
- **Unknown Threat Actor**: Using Lotus wiper malware against Venezuelan energy and utility organizations