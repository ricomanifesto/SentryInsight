# Exploitation Report

The current threat landscape reveals a concerning mix of zero-day vulnerabilities under active exploitation and sophisticated malware campaigns targeting critical infrastructure. Most notably, threat actors are actively exploiting vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) systems and leveraging the "Dirty Frag" Linux kernel zero-day to gain root privileges across major distributions. The ShinyHunters extortion group continues their aggressive campaign against educational platforms, while new malware families like TCLBANKER and PCPJack are employing novel spreading techniques and targeting cloud infrastructure. Additionally, a critical PAN-OS vulnerability is being exploited for espionage operations, demonstrating the continued focus on network infrastructure by advanced persistent threat actors.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) that grants admin-level access to attackers
- **Impact**: Allows attackers to execute arbitrary code remotely and gain administrative privileges on affected systems
- **Status**: Actively exploited in zero-day attacks, CISA has mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Kernel "Dirty Frag" Local Privilege Escalation
- **Description**: Unpatched zero-day vulnerability in the Linux kernel allowing local privilege escalation with a single command
- **Impact**: Enables local attackers to gain root privileges on most major Linux distributions
- **Status**: Currently unpatched zero-day with public proof-of-concept exploit available

### PAN-OS Remote Code Execution Vulnerability
- **Description**: Critical security flaw in Palo Alto Networks PAN-OS that enables root access and facilitates espionage operations
- **Impact**: Threat actors can gain root access to firewall systems and conduct espionage activities
- **Status**: Under active exploitation since at least April 9, 2026, with unsuccessful exploitation attempts detected

### PCPJack Framework CVE Exploitation
- **Description**: Credential theft framework that exploits multiple CVEs to spread worm-like across cloud systems
- **Impact**: Steals credentials from exposed cloud infrastructure and removes competing malware
- **Status**: Actively spreading across cloud environments, displacing TeamPCP malware

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Systems vulnerable to remote code execution attacks
- **Linux Distributions**: All major Linux distributions affected by Dirty Frag kernel vulnerability
- **Palo Alto Networks PAN-OS**: Firewall systems targeted for root access and espionage
- **Canvas Educational Platform**: Login portals compromised in mass extortion campaign by ShinyHunters
- **Cloud Infrastructure**: AWS, Azure, and other cloud platforms targeted by PCPJack credential theft
- **Banking and Fintech Platforms**: 59 financial platforms targeted by TCLBANKER trojan
- **Android Devices**: Fake call history apps distributed through Google Play Store affecting 7.3 million downloads
- **NVIDIA GeForce NOW**: Armenian users affected by data breach
- **Instructure Systems**: Second attack claimed by ShinyHunters affecting educational technology platform

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being actively exploited including Ivanti EPMM and Linux Dirty Frag
- **Social Engineering**: ClickFix techniques used to distribute Vidar Stealer malware in Australia
- **Trojanized Software**: TCLBANKER distributed via fake Logitech AI Prompt Builder MSI installers
- **Worm Propagation**: TCLBANKER self-spreads through WhatsApp and Outlook communications
- **PAM Module Abuse**: PamDOORa backdoor uses Linux PAM modules to steal SSH credentials
- **Cloud Infrastructure Exploitation**: PCPJack exploits exposed cloud services to steal credentials
- **Supply Chain Targeting**: Quasar Linux RAT targets developer systems for software supply chain compromise
- **Educational Platform Exploitation**: Mass defacement of Canvas login portals through vulnerability exploitation
- **Mobile App Store Abuse**: Fraudulent apps on Google Play Store tricking users into payment theft

## Threat Actor Activities

- **ShinyHunters**: Conducting second major attack against Instructure, mass exploitation of Canvas platform vulnerabilities affecting hundreds of colleges and universities
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-concept images
- **TCLBANKER Operators**: Brazilian threat actors targeting financial institutions with self-propagating banking trojan
- **PCPJack Operators**: Advanced threat actors targeting cloud infrastructure while displacing competing TeamPCP malware
- **darkworm**: Threat actor advertising PamDOORa Linux backdoor on Russian cybercrime forums for $1,600
- **ClickFix Campaign Operators**: Targeting Australian organizations with Vidar Stealer distribution campaigns
- **North Korean IT Workers**: Using laptop farms operated by U.S. nationals to fraudulently obtain remote employment at American companies
- **Advanced Persistent Threat Groups**: Exploiting PAN-OS vulnerabilities for espionage operations and root access to network infrastructure