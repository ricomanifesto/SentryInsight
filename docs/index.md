# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple platforms and systems. Critical zero-day vulnerabilities are being actively exploited, including the Ivanti EPMM CVE-2026-6973 remote code execution flaw that grants admin-level access and the Linux "Dirty Frag" kernel vulnerability enabling root privilege escalation across major distributions. A sophisticated worm-like credential stealing framework called PCPJack is exploiting five different vulnerabilities to spread across cloud environments while simultaneously cleaning TeamPCP infections. Educational institutions are facing widespread disruption through the ShinyHunters extortion gang's attacks on Canvas learning management systems, while malvertising campaigns are targeting macOS users through Google Ads and legitimate Claude.ai chats. The threat landscape also includes new banking trojans, supply chain compromises, and multiple data breaches affecting major organizations.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) that allows attackers to gain administrative-level access to affected systems
- **Impact**: Complete administrative control over EPMM deployments, enabling data access, system manipulation, and potential lateral movement
- **Status**: Under active exploitation in limited attacks in the wild; patches available
- **CVE ID**: CVE-2026-6973

### Linux Dirty Frag Zero-Day Privilege Escalation
- **Description**: Unpatched local privilege escalation vulnerability affecting the Linux kernel, described as a successor to Copy Fail vulnerability
- **Impact**: Local attackers can gain root privileges on most major Linux distributions with a single command
- **Status**: Zero-day vulnerability with proof-of-concept exploit available; currently unpatched

### PCPJack Multi-CVE Exploitation Framework
- **Description**: Sophisticated worm-like credential theft framework that exploits five different vulnerabilities to spread across cloud infrastructure
- **Impact**: Steals credentials from exposed cloud systems while actively removing TeamPCP malware artifacts, enabling persistent access to multiple cloud environments
- **Status**: Active in the wild, targeting exposed cloud infrastructure

### Ollama Out-of-Bounds Read Vulnerability
- **Description**: Critical security vulnerability in Ollama that allows remote, unauthenticated attackers to leak entire process memory
- **Impact**: Complete memory disclosure potentially exposing sensitive data, credentials, and system information
- **Status**: Disclosed vulnerability requiring immediate patching

### cPanel and WHM Multiple Vulnerabilities
- **Description**: Three newly discovered vulnerabilities in cPanel and Web Host Manager affecting web hosting management platforms
- **Impact**: Privilege escalation, code execution, and denial-of-service attacks possible
- **Status**: Patches released, immediate update recommended

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: All versions affected by CVE-2026-6973 RCE vulnerability
- **Linux Kernel**: Major Linux distributions including Ubuntu, Red Hat, SUSE, and Debian affected by Dirty Frag zero-day
- **Cloud Infrastructure**: AWS, Azure, and Google Cloud environments targeted by PCPJack credential stealer
- **Ollama AI Platform**: All versions vulnerable to memory leak attacks
- **cPanel/WHM**: Web hosting control panels requiring security updates
- **Canvas Learning Management System**: Educational platform portals compromised by ShinyHunters
- **JDownloader**: Popular download manager compromised to distribute Python RAT malware
- **macOS Systems**: Targeted through malicious Google Ads and Claude.ai chat abuse
- **Android Devices**: Google Play Store apps with 7.3 million downloads stealing payments
- **NVIDIA GeForce NOW**: Armenian user data exposed in confirmed breach

## Attack Vectors and Techniques

- **Malvertising Campaigns**: Abuse of Google Ads targeting "Claude mac download" searches to distribute macOS malware
- **Supply Chain Compromise**: JDownloader website compromised to replace legitimate installers with Python RAT malware
- **Social Engineering**: ClickFix technique used to distribute Vidar Stealer malware in Australia
- **Repository Poisoning**: Fake OpenAI repositories on Hugging Face platform distributing infostealer malware
- **Worm Propagation**: PCPJack spreads worm-like across cloud systems using multiple CVE exploits
- **PAM Module Abuse**: PamDOORa backdoor uses Linux PAM modules to steal SSH credentials
- **WhatsApp and Outlook Spreading**: TCLBanker trojan self-spreads through messaging platforms
- **Zero-Day Exploitation**: Direct kernel-level attacks using Dirty Frag privilege escalation
- **Web Portal Defacement**: Mass compromise of Canvas login portals for extortion purposes

## Threat Actor Activities

- **ShinyHunters**: Conducting mass extortion campaigns against educational institutions through Canvas platform exploitation and claiming multiple breaches including second attack on Instructure
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach with leaked proof images
- **Darkworm**: Advertising PamDOORa Linux backdoor on Russian Rehub cybercrime forum for $1,600
- **Brazilian Threat Actors**: Operating TCLBANKER banking trojan targeting 59 financial platforms across banking, fintech, and cryptocurrency sectors
- **Cloud-Focused Attackers**: Using PCPJack framework to systematically compromise cloud infrastructure while displacing TeamPCP malware
- **Mobile App Fraudsters**: Distributed fake call history apps on Google Play Store with 7.3 million downloads for payment theft
- **German Cybercriminals**: Operated Crimenetwork marketplace generating 3.6 million euros before police shutdown and admin arrest