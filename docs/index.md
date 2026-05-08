# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with particular concern around Ivanti Endpoint Manager Mobile (EPMM) systems and a newly disclosed Linux kernel privilege escalation flaw called "Dirty Frag." The Ivanti EPMM vulnerability CVE-2026-6973 is being exploited to grant administrative access to enterprise mobile device management systems, while the Linux Dirty Frag zero-day enables local privilege escalation to root access across all major Linux distributions. Additionally, threat actors are leveraging multiple vulnerabilities through the PCPJack credential-stealing framework and conducting widespread attacks against educational institutions through compromised Canvas platforms.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) that allows unauthorized administrative access
- **Impact**: Attackers can gain admin-level access to mobile device management systems, potentially compromising enterprise mobile security infrastructure
- **Status**: Currently being exploited as zero-day attacks; patch available with 4-day federal compliance deadline from CISA
- **CVE ID**: CVE-2026-6973

### Linux Kernel "Dirty Frag" Privilege Escalation
- **Description**: Local privilege escalation vulnerability affecting the Linux kernel across all major distributions, described as a successor to Copy Fail
- **Impact**: Local attackers can gain root privileges with a single command on most major Linux distributions
- **Status**: Unpatched zero-day vulnerability with proof-of-concept exploit available
- **CVE ID**: CVE-2026-31 (referenced as predecessor Copy Fail)

### Canvas Education Platform Vulnerabilities
- **Description**: Multiple vulnerabilities in the Canvas education technology platform exploited by ShinyHunters extortion gang
- **Impact**: Mass defacement of Canvas login portals, data extortion attacks disrupting educational institutions nationwide
- **Status**: Ongoing exploitation affecting hundreds of colleges and universities

### PCPJack Multi-CVE Exploitation Framework
- **Description**: Credential theft framework targeting exposed cloud infrastructure by exploiting multiple known vulnerabilities
- **Impact**: Steals credentials from cloud systems while removing TeamPCP malware artifacts to avoid detection
- **Status**: Active worm-like spreading across cloud environments using five different CVEs

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems vulnerable to remote code execution
- **Linux Distributions**: All major Linux distributions affected by Dirty Frag kernel vulnerability
- **Canvas Platform**: Educational technology platform serving schools, colleges, and universities nationwide
- **Cloud Infrastructure**: Exposed cloud systems targeted by PCPJack framework
- **Banking and Cryptocurrency Platforms**: 59 platforms targeted by TCLBanker malware
- **WhatsApp and Outlook**: Used as spreading vectors for TCLBanker trojan
- **SSH Systems**: Linux systems with PAM modules targeted by PamDOORa backdoor

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM and Linux kernel
- **Social Engineering**: ClickFix techniques used to distribute Vidar Stealer malware in Australia
- **Supply Chain Compromise**: Quasar Linux RAT targeting developers to compromise software supply chains
- **Trojanized Installers**: TCLBanker using fake Logitech AI Prompt Builder MSI installers
- **PAM Module Abuse**: PamDOORa backdoor exploiting Linux PAM authentication modules
- **Worm-Like Propagation**: PCPJack framework spreading autonomously across cloud infrastructure
- **Portal Defacement**: Mass compromise of Canvas login portals for extortion purposes

## Threat Actor Activities

- **ShinyHunters**: Conducting mass extortion campaign against educational institutions through Canvas platform compromises
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach with leaked proof images
- **"darkworm"**: Advertising PamDOORa Linux backdoor on Russian cybercrime forum Rehub for $1,600
- **PCPJack Operators**: Deploying credential-stealing framework while actively cleaning TeamPCP infections from compromised systems
- **TCLBanker Campaign**: Targeting banking, fintech, and cryptocurrency platforms through self-spreading malware
- **Australian ClickFix Campaign**: Using social engineering to distribute Vidar Stealer information-stealing malware