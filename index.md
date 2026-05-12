# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting enterprise systems and popular software platforms. Most notably, threat actors are actively exploiting a critical cPanel vulnerability (CVE-2026-41940) to deploy backdoors on hosting environments, while simultaneously leveraging AI-generated zero-day exploits for the first time in documented history. Supply chain attacks have intensified with compromises of the Checkmarx Jenkins plugin, JDownloader website, and malicious repositories on trusted platforms like Hugging Face. Additionally, banking trojans and Android malware are evolving with new communication methods, and attackers are increasingly abusing legitimate services like Google Ads and Claude.ai for malware distribution.

## Active Exploitation Details

### cPanel Critical Vulnerability
- **Description**: A critical security flaw in cPanel that allows threat actors to deploy backdoors on compromised hosting environments
- **Impact**: Full system compromise and deployment of the "Filemanager" backdoor for persistent access
- **Status**: Under active exploitation by threat actor "Mr_Rot13"
- **CVE ID**: CVE-2026-41940

### AI-Generated Zero-Day 2FA Bypass
- **Description**: First documented zero-day exploit developed using artificial intelligence targeting a popular open-source web administration tool's two-factor authentication mechanism
- **Impact**: Complete bypass of 2FA protections, allowing unauthorized access to web administration interfaces
- **Status**: Active exploitation identified by Google Threat Intelligence Group, likely developed with AI systems

### Canvas Portal Defacement Vulnerability
- **Description**: Security vulnerability in Instructure's Canvas learning management system allowing unauthorized modification of login portals
- **Impact**: Portal defacement and display of extortion messages targeting educational institutions
- **Status**: Confirmed exploitation with hackers successfully modifying Canvas login portals

### Ollama Memory Leak Vulnerability
- **Description**: Out-of-bounds read vulnerability in Ollama that allows remote attackers to leak entire process memory
- **Impact**: Unauthorized access to sensitive process memory contents without authentication
- **Status**: Critical vulnerability disclosed, exploitation potential confirmed

### Dirty Frag Linux Privilege Escalation
- **Description**: Privilege escalation vulnerability affecting enterprise Linux distributions, similar to Copy Fail and Dirty Pipe flaws
- **Impact**: Local privilege escalation allowing attackers to gain elevated system access
- **Status**: May already be under limited exploitation according to security researchers

## Affected Systems and Products

- **cPanel/WHM**: Web hosting control panels vulnerable to critical exploitation
- **Checkmarx Jenkins AST Plugin**: Compromised plugin distributed through Jenkins Marketplace
- **Instructure Canvas**: Educational platform login portals targeted for defacement
- **JDownloader**: Official website compromised to distribute Python RAT malware
- **Ollama**: AI model serving platform vulnerable to memory leak attacks
- **Enterprise Linux Distributions**: Multiple distros affected by Dirty Frag privilege escalation
- **Windows Systems**: Targeted by GhostLock file access blocking tool and various infostealers
- **Android Devices**: TrickMo banking malware targeting European users
- **macOS Systems**: Targeted through malvertising campaigns via Google Ads and Claude.ai
- **NVIDIA GeForce NOW**: Data breach affecting Armenian users

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromise of trusted software repositories and official download sites
- **AI-Powered Exploit Development**: First documented use of artificial intelligence to generate zero-day exploits
- **Malvertising Campaigns**: Abuse of Google Ads and legitimate chat platforms to distribute malware
- **Repository Poisoning**: Fake repositories on trusted platforms like Hugging Face and Jenkins Marketplace
- **Website Compromise**: Direct compromise of official software download sites
- **TON Blockchain C2**: Use of blockchain technology for covert command and control communications
- **Windows API Abuse**: Legitimate file APIs exploited to block file access (GhostLock technique)
- **WhatsApp/Outlook Worms**: Banking trojans spreading through messaging and email platforms

## Threat Actor Activities

- **Mr_Rot13**: Actively exploiting cPanel CVE-2026-41940 to deploy Filemanager backdoors on hosting environments
- **TeamPCP**: Responsible for compromising the Checkmarx Jenkins AST plugin in a supply chain attack
- **Unknown AI-Powered Actor**: First threat group identified using AI to develop zero-day exploits for web admin tools
- **ShinyHunters**: Claims second attack against Instructure, targeting educational technology platforms
- **TCLBANKER Operators**: Brazilian banking trojan operators targeting 59 financial and cryptocurrency platforms
- **TrickMo Operators**: Android banking malware campaign targeting European users with blockchain-based C2
- **Aviation Espionage Group**: Cyber espionage campaign targeting aerospace and drone operators to steal GIS and GPS data