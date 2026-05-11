# Exploitation Report

Current threat activity reveals a significant escalation in exploitation targeting educational institutions, with the ShinyHunters group conducting mass breaches of Canvas learning management systems affecting hundreds of colleges and universities nationwide. Simultaneously, multiple zero-day vulnerabilities are being actively exploited, including the Linux "Dirty Frag" privilege escalation flaw affecting all major distributions and CVE-2026-6973 in Ivanti EPMM systems. The threat landscape is further complicated by sophisticated malware campaigns, including the emergence of PCPJack worm targeting cloud infrastructure and various social engineering attacks leveraging legitimate platforms like Google Ads and Hugging Face to distribute malicious payloads.

## Active Exploitation Details

### Dirty Frag Linux Zero-Day
- **Description**: An unpatched local privilege escalation vulnerability in the Linux kernel that allows attackers to gain root privileges with a single command
- **Impact**: Complete system compromise with root access across all major Linux distributions
- **Status**: Currently unpatched with proof-of-concept exploit available

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager Mobile allowing remote code execution
- **Impact**: Admin-level access to affected systems through limited attacks in the wild
- **Status**: Under active exploitation with CISA mandating federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Canvas Platform Vulnerability
- **Description**: Security flaw in Instructure's Canvas learning management system exploited by ShinyHunters
- **Impact**: Mass defacement of login portals and data extortion affecting hundreds of educational institutions
- **Status**: Active exploitation causing nationwide disruption to schools and colleges

### PCPJack Multi-CVE Exploitation
- **Description**: Credential theft framework exploiting multiple vulnerabilities to spread worm-like across cloud systems
- **Impact**: Theft of cloud credentials while removing competing TeamPCP malware infections
- **Status**: Active exploitation targeting exposed cloud infrastructure

## Affected Systems and Products

- **Linux Distributions**: All major distributions affected by Dirty Frag zero-day vulnerability
- **Ivanti EPMM**: Endpoint Manager Mobile systems with CVE-2026-6973 vulnerability
- **Canvas LMS**: Learning management systems at hundreds of educational institutions
- **JDownloader**: Website compromised to distribute Python RAT malware through malicious installers
- **Ollama**: AI platform affected by out-of-bounds read vulnerability allowing memory leakage
- **cPanel/WHM**: Three new vulnerabilities patched for privilege escalation and code execution
- **Google Play Store**: Fake call history apps with 7.3 million downloads used for payment theft
- **Hugging Face**: Platform hosting fake OpenAI repository distributing infostealer malware
- **NVIDIA GeForce NOW**: Data breach affecting Armenian users
- **Zara**: Database breach exposing 197,000 customer records

## Attack Vectors and Techniques

- **Malvertising**: Google Ads abuse to distribute Mac malware through fake Claude.ai downloads
- **Supply Chain Compromise**: Website takeovers of legitimate software distributors like JDownloader
- **Social Engineering**: ClickFix technique pushing Vidar Stealer malware in Australia
- **Repository Poisoning**: Fake repositories on legitimate platforms like Hugging Face
- **Worm Propagation**: Self-spreading malware through WhatsApp and Outlook (TCLBanker/TCLBANKER)
- **PAM Module Abuse**: PamDOORa backdoor using Linux PAM modules to steal SSH credentials
- **Memory Exploitation**: Out-of-bounds read attacks against AI platforms like Ollama

## Threat Actor Activities

- **ShinyHunters**: Multiple attacks against Instructure Canvas systems and claimed second breach
- **RansomHouse**: Source code breach of Trellix cybersecurity company
- **TCLBanker Operators**: Brazilian banking trojan campaign targeting 59 financial platforms
- **PCPJack Developers**: Worm framework creators targeting cloud infrastructure while eliminating TeamPCP
- **darkworm**: Threat actor advertising PamDOORa Linux backdoor on Russian cybercrime forums for $1,600
- **Unknown Actors**: Multiple campaigns involving Google Ads abuse, fake mobile apps, and educational platform targeting