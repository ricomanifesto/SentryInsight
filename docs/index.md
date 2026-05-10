# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with attackers targeting Linux systems through the newly disclosed "Dirty Frag" local privilege escalation exploit and Ivanti Endpoint Manager Mobile through CVE-2026-6973. Meanwhile, threat actors are conducting sophisticated supply chain attacks, including website compromises of popular download managers, malicious app distribution through official app stores, and abuse of legitimate platforms like Google Ads and Claude.ai to distribute malware. The PCPJack credential stealer is exploiting multiple vulnerabilities to spread worm-like across cloud systems, while the ShinyHunters group continues their education sector targeting campaign.

## Active Exploitation Details

### Linux "Dirty Frag" Zero-Day Local Privilege Escalation
- **Description**: An unpatched local privilege escalation vulnerability in the Linux kernel that allows attackers to gain root privileges with a single command
- **Impact**: Complete system compromise with root-level access on all major Linux distributions
- **Status**: Currently unpatched zero-day with public proof-of-concept exploit available

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager Mobile allowing remote code execution
- **Impact**: Admin-level access to enterprise mobile device management systems
- **Status**: Under active exploitation in limited attacks
- **CVE ID**: CVE-2026-6973

### PCPJack Multi-CVE Exploitation
- **Description**: Credential theft framework exploiting five different vulnerabilities to spread across cloud infrastructure
- **Impact**: Credential theft, lateral movement across cloud environments, and removal of competing malware (TeamPCP)
- **Status**: Active worm-like propagation across exposed cloud systems

### cPanel and WHM Vulnerabilities
- **Description**: Three newly patched vulnerabilities in cPanel and Web Host Manager affecting web hosting infrastructure
- **Impact**: Privilege escalation, code execution, and denial-of-service attacks
- **Status**: Patches released, immediate update required

### Ollama Out-of-Bounds Read
- **Description**: Critical vulnerability in Ollama allowing remote, unauthenticated attackers to leak entire process memory
- **Impact**: Complete memory disclosure and potential system compromise
- **Status**: Vulnerability disclosed, patch status unclear

## Affected Systems and Products

- **Linux Distributions**: All major distributions vulnerable to Dirty Frag zero-day privilege escalation
- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management platforms under targeted attack
- **cPanel/WHM**: Web hosting control panels requiring immediate patching
- **JDownloader**: Popular download manager with compromised website distributing malware
- **Canvas/Instructure**: Education technology platform suffering ongoing ShinyHunters attacks
- **Ollama**: AI/ML platform with critical memory disclosure vulnerability
- **Google Play Store**: Multiple fraudulent apps with 7.3 million downloads stealing payments
- **Hugging Face**: AI model repository hosting fake OpenAI projects with malware
- **Cloud Infrastructure**: AWS, Azure, and other cloud platforms targeted by PCPJack worm

## Attack Vectors and Techniques

- **Malvertising**: Google Ads abuse to redirect Claude.ai searches to malware distribution sites
- **Supply Chain Compromise**: Website takeovers of legitimate software distributors (JDownloader)
- **Repository Poisoning**: Fake projects on legitimate platforms (Hugging Face, targeting OpenAI users)
- **ClickFix Social Engineering**: Fraudulent error messages tricking users into executing malware
- **Worm Propagation**: Self-spreading malware across cloud infrastructure using credential theft
- **App Store Abuse**: Fraudulent applications on official stores mimicking legitimate functionality
- **Email and Messaging Worms**: Self-propagation through WhatsApp and Outlook contacts
- **Platform Impersonation**: Fake repositories and profiles on trusted development platforms

## Threat Actor Activities

- **ShinyHunters**: Conducting sustained campaign against education sector, specifically targeting Canvas/Instructure with multiple breaches and portal defacements
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach with proof-of-concept data leak
- **TCLBANKER Operators**: Brazilian banking trojan campaign targeting 59 financial platforms using trojanized Logitech software installers
- **PCPJack Developers**: Advanced persistent threat creating worm-like credential stealer that actively removes competing malware while propagating
- **Darkworm**: Linux backdoor developer advertising PamDOORa on Russian cybercrime forums for SSH credential theft
- **Quasar Linux RAT Operators**: Targeting developers' systems for software supply chain compromise and credential theft
- **Google Ads Malvertisers**: Sophisticated campaign abusing legitimate advertising platforms and AI chat services for malware distribution