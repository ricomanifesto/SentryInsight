# Exploitation Report

Critical zero-day exploitation activity is currently targeting Linux systems and enterprise infrastructure, with the newly disclosed "Dirty Frag" Linux kernel vulnerability enabling root access across all major distributions. Simultaneously, threat actors are exploiting vulnerabilities in Ivanti Endpoint Manager Mobile (CVE-2026-6973) in active attacks, while sophisticated malware campaigns leverage compromised websites and fraudulent repositories to distribute banking trojans and information stealers. The ShinyHunters group continues aggressive attacks against educational infrastructure, compromising Canvas portals across hundreds of institutions, while new Linux backdoors and worms are actively stealing credentials from cloud environments and developer systems.

## Active Exploitation Details

### Dirty Frag Linux Zero-Day
- **Description**: An unpatched local privilege escalation vulnerability in the Linux kernel that allows attackers to gain root privileges with a single command
- **Impact**: Complete system compromise with root access on all major Linux distributions including Ubuntu, Red Hat, SUSE, and others
- **Status**: Currently unpatched zero-day with public proof-of-concept exploit available

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager Mobile allowing remote code execution
- **Impact**: Attackers can gain administrator-level access to mobile device management infrastructure
- **Status**: Under active exploitation in limited attacks, patches available
- **CVE ID**: CVE-2026-6973

### Ollama Out-of-Bounds Read Vulnerability
- **Description**: Critical security vulnerability allowing remote process memory leak in Ollama AI platform
- **Impact**: Remote, unauthenticated attackers can leak entire process memory contents
- **Status**: Recently disclosed, patch status unknown

## Affected Systems and Products

- **Linux Systems**: All major distributions including Ubuntu, Red Hat, SUSE, Debian affected by Dirty Frag zero-day
- **Ivanti EPMM**: Mobile device management platforms under active attack
- **Canvas Education Platform**: Hundreds of colleges and universities experiencing compromised login portals
- **JDownloader**: Popular download manager website compromised to distribute Python RAT malware
- **Hugging Face Platform**: AI model repository targeted for malicious OpenAI impersonation campaigns
- **cPanel/WHM**: Web hosting control panels affected by three newly patched vulnerabilities
- **NVIDIA GeForce NOW**: Armenian users affected by confirmed data breach
- **Zara**: 197,000 customer records exposed in database breach

## Attack Vectors and Techniques

- **Website Compromise**: JDownloader official site hacked to replace legitimate installers with Python-based RAT malware
- **Repository Poisoning**: Fake OpenAI Privacy Filter repository on Hugging Face delivering Rust-based information stealer
- **Malvertising**: Google Ads abuse combined with Claude.ai shared chats to distribute Mac malware
- **Mobile App Fraud**: 7.3 million downloads of fake call history apps on Google Play Store stealing payments
- **Supply Chain Targeting**: Quasar Linux RAT specifically targeting developer credentials for broader compromise
- **Blockchain C2**: TrickMo Android banker adopting TON blockchain for covert command-and-control communications
- **Worm Propagation**: TCLBanker malware self-spreading through WhatsApp and Outlook, targeting 59 financial platforms

## Threat Actor Activities

- **ShinyHunters**: Conducting second attack against Instructure's Canvas platform, exploiting vulnerabilities to deface login portals across hundreds of educational institutions
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-concept images
- **Brazilian Threat Actors**: Deploying TCLBanker trojan via trojanized Logitech AI Prompt Builder MSI installers
- **PCPJack Operators**: New worm framework stealing cloud credentials while actively removing competing TeamPCP malware infections
- **Linux Backdoor Developers**: PamDOORa backdoor being sold for $1,600 on Russian Rehub cybercrime forum by "darkworm" actor
- **Android Banking Groups**: Enhanced TrickMo campaigns targeting European users with blockchain-based infrastructure
- **Mac Malware Distributors**: Sophisticated campaigns abusing legitimate platforms like Google Ads and Claude.ai for distribution