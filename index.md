# Exploitation Report

Critical exploitation activity is currently centered around several high-impact vulnerabilities and sophisticated attack campaigns. A cPanel vulnerability (CVE-2026-41940) is under active exploitation by the threat actor Mr_Rot13 to deploy Filemanager backdoors in compromised environments. Google has identified the first known AI-developed zero-day exploit targeting a popular web administration tool, marking a significant evolution in threat actor capabilities. Additionally, multiple supply chain attacks have compromised trusted software repositories, including the CheckMarx Jenkins AST plugin and fake repositories on Hugging Face and the JDownloader website, demonstrating attackers' focus on software supply chain infiltration.

## Active Exploitation Details

### cPanel Critical Vulnerability
- **Description**: A critical vulnerability in cPanel allowing unauthorized access and backdoor deployment
- **Impact**: Attackers can deploy the Filemanager backdoor on compromised cPanel environments, enabling persistent access and control
- **Status**: Under active exploitation by threat actor Mr_Rot13
- **CVE ID**: CVE-2026-41940

### AI-Developed Zero-Day Web Admin Tool Exploit
- **Description**: A zero-day exploit targeting a popular open-source web administration tool, developed using artificial intelligence systems
- **Impact**: Allows attackers to bypass two-factor authentication and gain unauthorized access to web administration interfaces
- **Status**: Active exploitation identified by Google Threat Intelligence Group, marking the first known AI-generated zero-day exploit

### Canvas Portal Vulnerability
- **Description**: A security vulnerability in Instructure's Canvas learning management system allowing portal defacement
- **Impact**: Hackers can modify Canvas login portals and leave extortion messages, potentially disrupting educational services
- **Status**: Confirmed exploitation used to deface portals with extortion demands

### Dirty Frag Linux Privilege Escalation
- **Description**: A privilege escalation vulnerability affecting enterprise Linux distributions, similar to previous flaws like Dirty Pipe and Copy Fail
- **Impact**: Allows local attackers to escalate privileges on Linux systems
- **Status**: May already be under limited exploitation according to security researchers

### Ollama Out-of-Bounds Read Vulnerability
- **Description**: A critical out-of-bounds read vulnerability in the Ollama AI platform
- **Impact**: Remote, unauthenticated attackers can leak entire process memory from affected Ollama instances
- **Status**: Disclosed vulnerability with potential for remote memory disclosure attacks

## Affected Systems and Products

- **cPanel and Web Host Manager (WHM)**: Multiple vulnerabilities including CVE-2026-41940 with active exploitation
- **Canvas Learning Management System**: Portal defacement vulnerability affecting educational institutions
- **Jenkins Marketplace**: Compromised CheckMarx AST plugin containing infostealer malware
- **Linux Enterprise Distributions**: Privilege escalation vulnerability dubbed "Dirty Frag"
- **Ollama AI Platform**: Critical memory disclosure vulnerability affecting AI model hosting
- **JDownloader**: Official website compromised to distribute Python RAT malware
- **Hugging Face Platform**: Fake OpenAI repositories distributing information-stealing malware
- **Android Devices**: TrickMo banking malware and fraudulent call history apps targeting financial data
- **macOS Systems**: Malvertising campaigns through Google Ads and Claude.ai pushing Mac malware
- **NVIDIA GeForce NOW**: Data breach affecting Armenian users

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Attackers compromising official software repositories and marketplaces to distribute malware through trusted channels
- **AI-Enhanced Exploit Development**: Use of large language models and artificial intelligence to develop sophisticated zero-day exploits
- **Malvertising Campaigns**: Abuse of Google Ads and legitimate AI chat platforms to redirect users to malicious downloads
- **Social Engineering**: Fake software repositories impersonating legitimate projects to trick users into downloading malware
- **Website Compromise**: Direct compromise of popular download sites to replace legitimate installers with malware
- **Blockchain-Based C2**: Use of TON blockchain for covert command-and-control communications in banking malware
- **Worm Propagation**: WhatsApp and Outlook-based worm mechanisms for spreading banking trojans

## Threat Actor Activities

- **Mr_Rot13**: Actively exploiting cPanel CVE-2026-41940 to deploy Filemanager backdoors in web hosting environments
- **TeamPCP**: Responsible for compromising the CheckMarx Jenkins AST plugin weeks after a previous KICS supply chain attack
- **ShinyHunters**: Claimed responsibility for a second attack against Instructure, targeting educational technology platforms
- **Unknown AI-Enabled Group**: First threat actor identified using AI to develop zero-day exploits for mass exploitation campaigns
- **TCLBANKER Operators**: Brazilian threat actors targeting 59 banking, fintech, and cryptocurrency platforms through WhatsApp and Outlook worms
- **TrickMo Developers**: Android banking malware operators adopting TON blockchain technology for stealthy command-and-control communications
- **Aviation Espionage Group**: Cyber espionage campaign targeting aerospace and drone operators to steal GIS files, terrain models, and GPS data