# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple attack vectors. Critical vulnerabilities are being actively exploited in Wing FTP Server systems, while sophisticated supply chain attacks through the GlassWorm malware campaign are targeting hundreds of repositories across GitHub, npm, and VSCode platforms. Ransomware groups including LeakNet and Warlock are evolving their tactics with new social engineering techniques and stealthier post-exploitation methods. Meanwhile, credential theft has surged dramatically in the second half of 2025, driven by industrialized infostealer malware operations and AI-enhanced social engineering campaigns. State-sponsored threat actors, particularly those with China and North Korea nexus, are conducting extensive espionage campaigns targeting military organizations and using novel techniques for persistent access and malware distribution.

## Active Exploitation Details

### Wing FTP Server Path Information Disclosure Vulnerability
- **Description**: A medium-severity security flaw in Wing FTP Server that allows attackers to leak server path information
- **Impact**: Information disclosure that may be chained with other vulnerabilities to achieve remote code execution
- **Status**: Actively exploited in the wild; CISA has added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog

### GlassWorm Supply Chain Attack
- **Description**: Coordinated malware campaign targeting software development platforms and repositories
- **Impact**: Injection of malicious code into Python repositories, VSCode extensions, and npm packages affecting hundreds of projects
- **Status**: Ongoing campaign using stolen GitHub tokens to force-push malware into repositories

### Companies House WebFiling Security Flaw
- **Description**: Security vulnerability in the UK's Companies House WebFiling service that exposed business data
- **Impact**: Unauthorized access to sensitive business information and company registry data
- **Status**: Service was taken offline for remediation and has since been restored

### AI Code Execution Environment Data Exfiltration
- **Description**: New DNS-based data exfiltration method targeting AI platforms including Amazon Bedrock, LangSmith, and SGLang
- **Impact**: Sensitive data exfiltration from AI environments and potential remote code execution
- **Status**: Disclosed vulnerabilities affecting multiple AI service platforms

## Affected Systems and Products

- **Wing FTP Server**: All versions affected by path information disclosure vulnerability
- **GitHub Repositories**: Hundreds of Python repositories targeted by GlassWorm malware injection
- **VSCode Extensions**: Multiple extensions compromised through OpenVSX and VSCode marketplaces
- **npm Packages**: Various npm packages infected with GlassWorm malware
- **Amazon Bedrock**: AI service platform affected by DNS exfiltration techniques
- **LangSmith**: AI development platform vulnerable to data exfiltration attacks
- **SGLang**: AI inference platform with code execution vulnerabilities
- **Companies House WebFiling**: UK business registry service exposed sensitive data
- **Samsung Galaxy Book 4**: Windows 11 devices experiencing C: drive access issues
- **Microsoft Exchange Online**: Service outages affecting mailbox and calendar access

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: LeakNet ransomware using fake website prompts to trick users into executing malicious code
- **DNS Exfiltration**: Novel technique for stealing data from AI code execution environments using domain name system queries
- **GitHub Token Theft**: Attackers using stolen authentication tokens to inject malware into repositories
- **BYOVD (Bring Your Own Vulnerable Driver)**: Warlock ransomware group employing new driver-based techniques for stealthy operations
- **Deno Runtime Loader**: LeakNet deploying in-memory malware loaders based on open-source Deno runtime
- **Phishing with Trusted Brands**: Multi-stage phishing campaigns leveraging legitimate brand domains for credential theft
- **KakaoTalk Propagation**: North Korean actors using compromised desktop messaging applications to distribute malware
- **Font Rendering Attacks**: New technique hiding malicious commands from AI tools using HTML font manipulation

## Threat Actor Activities

- **LeakNet Ransomware Group**: Adopting ClickFix tactics and deploying Deno-based malware loaders for stealthy corporate environment infiltration
- **Warlock Ransomware Group**: Showcasing enhanced post-exploitation capabilities with new BYOVD techniques and improved cross-network stealth
- **China-Nexus Actors**: Conducting extensive cyber espionage campaigns against Southeast Asian military organizations with novel backdoors and persistent access techniques
- **North Korean Konni Group**: Deploying EndRAT malware through phishing campaigns and using KakaoTalk desktop applications for malware propagation
- **GlassWorm Operators**: Coordinating sophisticated supply chain attacks across multiple platforms with evolved evasion techniques and dependency hiding
- **Sanctioned Chinese and Iranian Entities**: Targeted by European Union sanctions for cyberattacks against critical infrastructure
- **Credential Theft Syndicates**: Industrializing infostealer malware operations with AI-enhanced social engineering capabilities