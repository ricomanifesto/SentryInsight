# Exploitation Report

The current threat landscape reveals multiple critical vulnerabilities under active exploitation, with zero-day attacks targeting enterprise infrastructure and widespread malware campaigns compromising cloud environments. Most concerning are the active exploitation of Ivanti EPMM vulnerabilities enabling administrative access, the emergence of a new Linux zero-day privilege escalation flaw called "Dirty Frag," and sophisticated worm-like malware frameworks targeting cloud credentials. Educational institutions face particular risk with mass compromises of Canvas learning platforms, while new banking trojans and stealer malware are spreading through social engineering campaigns across WhatsApp and email platforms.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) that allows attackers to gain administrative-level access to systems
- **Impact**: Complete system compromise with admin-level privileges, enabling full control over endpoint management infrastructure
- **Status**: Currently being exploited in zero-day attacks in the wild; patches available but CISA has mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Kernel "Dirty Frag" Zero-Day Privilege Escalation
- **Description**: Unpatched local privilege escalation vulnerability affecting the Linux kernel across all major distributions, described as a successor to previous Copy Fail exploits
- **Impact**: Local attackers can gain root privileges on compromised Linux systems with a single command
- **Status**: Active zero-day with proof-of-concept exploit available; no patches currently available

### PAN-OS Critical Remote Code Execution Flaw
- **Description**: Critical vulnerability in Palo Alto Networks PAN-OS that enables remote code execution and root access
- **Impact**: Complete firewall compromise allowing espionage activities and network infiltration
- **Status**: Under active exploitation since at least April 9, 2026, with attempted exploit activities detected

### cPanel and WHM Vulnerabilities
- **Description**: Three newly disclosed vulnerabilities in cPanel and Web Host Manager affecting web hosting infrastructure
- **Impact**: Privilege escalation, code execution, and denial-of-service attacks against web hosting platforms
- **Status**: Patches released and available for immediate deployment

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platforms with administrative access compromise
- **Linux Kernel**: All major Linux distributions vulnerable to privilege escalation attacks
- **Palo Alto Networks PAN-OS**: Firewall and security appliances subject to remote code execution
- **cPanel/WHM**: Web hosting control panels and management interfaces
- **Canvas LMS Platform**: Educational technology platforms used by hundreds of colleges and universities
- **Android Devices**: Google Play Store apps with over 7.3 million downloads containing fraudulent payment theft functionality
- **Cloud Infrastructure**: AWS, Azure, and other cloud platforms targeted by credential theft frameworks
- **Financial Platforms**: 59 banking, fintech, and cryptocurrency platforms targeted by TCLBANKER trojan

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise infrastructure
- **Social Engineering via ClickFix**: Fake software update prompts used to distribute Vidar Stealer malware
- **WhatsApp and Outlook Worms**: Self-spreading malware using messaging platforms for initial infection
- **Trojanized Software Installers**: Legitimate-looking MSI installers for popular software containing banking trojans
- **PAM Module Backdoors**: Linux systems compromised through malicious Pluggable Authentication Modules
- **Canvas Portal Defacement**: Mass compromise of educational login portals for extortion campaigns
- **CVE Exploitation Chains**: PCPJack framework exploiting five different CVEs to spread across cloud systems
- **Supply Chain Targeting**: Quasar Linux RAT specifically targeting developer systems for broader compromise

## Threat Actor Activities

- **ShinyHunters**: Conducting second major attack against Instructure/Canvas with mass portal defacement and extortion campaigns affecting hundreds of educational institutions
- **RansomHouse**: Claiming responsibility for Trellix source code repository breach with leaked proof-of-concept evidence
- **Brazilian Banking Threat Actors**: Operating TCLBANKER trojan campaigns targeting South American financial institutions
- **"darkworm" Actor**: Advertising PamDOORa Linux backdoor on Russian cybercrime forums for $1,600
- **PCPJack Operators**: Running sophisticated credential theft operations while actively removing competing TeamPCP malware infections
- **North Korean IT Workers**: Using laptop farm operations to fraudulently obtain remote employment at American companies for intelligence gathering