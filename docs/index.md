# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems across various sectors. The most severe threats include the Dirty Frag zero-day vulnerability affecting all major Linux distributions with root privilege escalation capabilities, an Ivanti EPMM vulnerability being exploited as a zero-day providing administrative access, and sophisticated malware campaigns including the new PCPJack credential stealer exploiting multiple vulnerabilities to spread across cloud systems. Additionally, major breaches have affected educational platforms Canvas/Instructure by the ShinyHunters group, while new malware strains like TCLBanker and PamDOORa are actively targeting financial institutions and Linux systems respectively.

## Active Exploitation Details

### Dirty Frag Zero-Day
- **Description**: An unpatched local privilege escalation vulnerability in the Linux kernel that allows attackers to gain root privileges with a single command
- **Impact**: Complete system compromise with root access across all major Linux distributions
- **Status**: Currently unpatched zero-day with public proof-of-concept exploit available

### Ivanti EPMM Remote Code Execution
- **Description**: A high-severity vulnerability in Ivanti Endpoint Manager Mobile allowing remote code execution
- **Impact**: Administrative-level access to mobile device management systems
- **Status**: Under active exploitation in limited attacks, patch available
- **CVE ID**: CVE-2026-6973

### Ollama Out-of-Bounds Read
- **Description**: Critical vulnerability in Ollama allowing remote, unauthenticated attackers to leak entire process memory
- **Impact**: Complete process memory disclosure exposing sensitive data
- **Status**: Disclosed vulnerability requiring immediate patching

### PCPJack Multi-CVE Exploitation
- **Description**: Advanced credential theft framework exploiting five different vulnerabilities to spread worm-like across cloud infrastructure
- **Impact**: Credential theft, lateral movement across cloud environments, and removal of competing malware
- **Status**: Active in the wild targeting exposed cloud systems

## Affected Systems and Products

- **Linux Kernel**: All major Linux distributions vulnerable to Dirty Frag privilege escalation
- **Ivanti EPMM**: Mobile device management platforms exposed to remote code execution
- **Ollama**: AI model serving platforms at risk of memory disclosure
- **Canvas/Instructure**: Educational technology platforms breached by ShinyHunters
- **Cloud Infrastructure**: AWS, Azure, and other cloud platforms targeted by PCPJack
- **cPanel/WHM**: Web hosting management platforms with three newly patched vulnerabilities
- **JDownloader**: Download manager website compromised to distribute Python RAT
- **Banking/Fintech Platforms**: 59 platforms targeted by TCLBanker trojan
- **Google Play Store**: Fraudulent call history apps with 7.3 million downloads
- **NVIDIA GeForce NOW**: Gaming service affected by data breach
- **Zara**: Fashion retailer database breach affecting 197,000 customers

## Attack Vectors and Techniques

- **Malvertising Campaigns**: Google Ads abuse to distribute Mac malware targeting Claude.ai users
- **Website Compromise**: JDownloader site hacked to replace legitimate installers with malware
- **Supply Chain Attacks**: Fake repositories on platforms like Hugging Face impersonating legitimate projects
- **ClickFix Social Engineering**: Australian ACSC warns of campaigns distributing Vidar Stealer
- **WhatsApp and Outlook Worms**: TCLBanker spreading through messaging platforms
- **PAM Module Abuse**: PamDOORa backdoor using Linux authentication modules for SSH credential theft
- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being exploited before patches available
- **Cloud Infrastructure Scanning**: Automated discovery and exploitation of exposed cloud services

## Threat Actor Activities

- **ShinyHunters**: Conducting second attack against Instructure/Canvas, causing nationwide educational disruptions
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach
- **TCLBanker Operators**: Brazilian threat actors targeting financial platforms with self-spreading malware
- **PCPJack Developers**: Advanced threat actors replacing TeamPCP infections while stealing credentials
- **darkworm**: Threat actor selling PamDOORa Linux backdoor on Russian cybercrime forums
- **Crimenetwork Operators**: German authorities shut down relaunched criminal marketplace generating €3.6 million
- **State-Sponsored Groups**: CISA directive suggests federal agencies under active threat from Ivanti EPMM exploitation