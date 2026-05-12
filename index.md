# Exploitation Report

Critical exploitation activity is currently affecting multiple platforms with significant security implications. A cPanel vulnerability (CVE-2026-41940) is under active exploitation by the threat actor Mr_Rot13 to deploy Filemanager backdoors on compromised systems. Google has reported the first known instance of AI-assisted zero-day exploit development, where attackers used artificial intelligence to create a zero-day 2FA bypass for mass exploitation targeting a popular web administration tool. Additionally, supply chain attacks have compromised the Checkmarx Jenkins AST plugin and JDownloader download manager, while an Ivanti Endpoint Manager Mobile vulnerability is being exploited as a zero-day, prompting CISA to issue emergency patching directives for federal agencies.

## Active Exploitation Details

### cPanel Critical Vulnerability
- **Description**: Critical vulnerability in cPanel allowing unauthorized access and backdoor deployment
- **Impact**: Attackers can deploy the Filemanager backdoor on compromised cPanel environments, potentially gaining persistent access to web hosting systems
- **Status**: Under active exploitation by Mr_Rot13 threat actor; patches available
- **CVE ID**: CVE-2026-41940

### AI-Developed Zero-Day 2FA Bypass
- **Description**: First known zero-day exploit developed using artificial intelligence systems targeting a popular web administration tool
- **Impact**: Bypasses two-factor authentication mechanisms, allowing unauthorized access to administrative interfaces
- **Status**: Active exploitation detected by Google Threat Intelligence Group; represents a significant evolution in exploit development methodologies

### Ivanti Endpoint Manager Mobile Zero-Day
- **Description**: High-severity vulnerability in Ivanti EPMM being exploited in zero-day attacks
- **Impact**: Allows attackers to compromise mobile device management systems
- **Status**: Active zero-day exploitation; CISA has mandated federal agencies patch within four days

### Checkmarx Jenkins AST Plugin Supply Chain Attack
- **Description**: TeamPCP threat group compromised the Checkmarx Jenkins AST plugin in the Jenkins Marketplace
- **Impact**: Organizations using the compromised plugin may have their CI/CD pipelines compromised
- **Status**: Modified malicious version published to Jenkins Marketplace; users must verify they are using legitimate versions

### Canvas Learning Management System Vulnerability
- **Description**: Security vulnerability in Instructure Canvas allowing unauthorized portal modification
- **Impact**: Hackers can deface Canvas login portals and leave extortion messages
- **Status**: Confirmed exploitation by Instructure; vulnerability used for portal defacement and extortion

## Affected Systems and Products

- **cPanel and Web Host Manager (WHM)**: Web hosting control panels vulnerable to backdoor deployment
- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management systems under zero-day attack
- **Jenkins AST Plugin**: CI/CD pipeline security tools compromised in supply chain attack
- **Canvas Learning Management System**: Education technology platforms used by institutions worldwide
- **JDownloader**: Popular download manager with compromised website distributing malware
- **Ollama AI Platform**: Out-of-bounds read vulnerability allowing remote memory leak
- **Linux Enterprise Distributions**: "Dirty Frag" privilege escalation vulnerability affecting enterprise systems
- **Hugging Face Repository Platform**: Fake OpenAI repositories distributing information-stealing malware

## Attack Vectors and Techniques

- **AI-Assisted Exploit Development**: First documented use of artificial intelligence to develop zero-day exploits
- **Supply Chain Compromises**: Attackers targeting trusted software repositories and distribution channels
- **Website Compromises**: Direct compromise of legitimate software websites to distribute malware
- **Malvertising Campaigns**: Abuse of Google Ads and legitimate AI chat platforms to distribute malware
- **Repository Poisoning**: Creation of fake repositories on trusted platforms like Hugging Face
- **2FA Bypass Techniques**: Advanced methods to circumvent two-factor authentication systems
- **Privilege Escalation**: "Dirty Frag" vulnerability enabling local privilege escalation on Linux systems

## Threat Actor Activities

- **Mr_Rot13**: Actively exploiting cPanel CVE-2026-41940 to deploy Filemanager backdoors on compromised hosting environments
- **TeamPCP**: Conducted supply chain attack against Checkmarx Jenkins AST plugin following previous KICS supply chain compromise
- **ShinyHunters**: Claims second attack against Instructure, targeting educational technology platforms with potential exposure of hundreds of millions of personal records
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-concept images
- **Unknown AI-Leveraging Group**: First threat actor identified using artificial intelligence for zero-day exploit development, marking significant evolution in attack methodologies
- **Aviation-Targeting Espionage Group**: Quietly compromising aerospace and drone operators to steal GIS files, terrain models, and GPS mapping data
- **TCLBANKER Operators**: Brazilian banking trojan targeting 59 financial platforms via WhatsApp and Outlook worm propagation
- **TrickMo Android Banking Group**: Enhanced Android banking malware using TON blockchain for covert command-and-control communications