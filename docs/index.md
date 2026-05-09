# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with threat actors targeting enterprise infrastructure and end-user systems. The most severe activity involves CVE-2026-6973 in Ivanti EPMM being exploited for remote code execution with admin-level access, and a new Linux kernel zero-day called "Dirty Frag" that allows privilege escalation to root across all major distributions. Additionally, the PCPJack credential theft framework is exploiting five different vulnerabilities to spread worm-like across cloud environments, while the ShinyHunters group has launched widespread attacks against educational institutions through Canvas platform compromises.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager Mobile (EPMM) allowing remote code execution
- **Impact**: Attackers can gain administrator-level access to affected systems and conduct unauthorized activities
- **Status**: Under active exploitation in limited attacks; patches available
- **CVE ID**: CVE-2026-6973

### Linux Kernel Dirty Frag Privilege Escalation
- **Description**: Unpatched local privilege escalation vulnerability in the Linux kernel, described as a successor to Copy Fail
- **Impact**: Local attackers can gain root privileges on most major Linux distributions with a single command
- **Status**: Zero-day vulnerability with proof-of-concept exploit available; no patch currently available

### PCPJack Cloud Infrastructure Exploitation
- **Description**: Credential theft framework targeting exposed cloud infrastructure while removing TeamPCP artifacts
- **Impact**: Steals credentials from cloud environments and spreads worm-like across systems
- **Status**: Actively exploiting five different vulnerabilities to propagate

### cPanel and WHM Vulnerabilities
- **Description**: Three vulnerabilities affecting cPanel and Web Host Manager platforms
- **Impact**: Could lead to privilege escalation, code execution, and denial-of-service attacks
- **Status**: Patches recently released by cPanel

## Affected Systems and Products

- **Ivanti EPMM**: Endpoint Manager Mobile systems vulnerable to remote code execution
- **Linux Distributions**: All major Linux distributions affected by Dirty Frag kernel vulnerability
- **Cloud Infrastructure**: Multiple cloud environments targeted by PCPJack framework
- **cPanel/WHM**: Web hosting control panel systems requiring immediate patching
- **Canvas Platform**: Educational technology platform compromised in mass attacks
- **Android Devices**: Fake call history apps affecting 7.3 million Play Store downloads
- **WhatsApp and Outlook**: Targeted by TCLBANKER trojan for self-spreading capabilities
- **Hugging Face Platform**: Repository hosting malicious OpenAI impersonation
- **PAN-OS Systems**: Palo Alto Networks firewall systems under attempted exploitation

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities in Ivanti EPMM and Linux kernel
- **Social Engineering**: ClickFix technique pushing Vidar Stealer malware in Australia
- **Supply Chain Compromise**: Fake repositories on legitimate platforms (Hugging Face, Google Play Store)
- **Worm Propagation**: Self-spreading malware through messaging platforms (WhatsApp, Outlook)
- **Credential Theft**: Targeting SSH credentials through PAM module backdoors (PamDOORa)
- **Mass Defacement**: ShinyHunters exploiting Canvas vulnerabilities for widespread portal compromise
- **Trojanized Installers**: TCLBANKER using fake Logitech AI Prompt Builder installers

## Threat Actor Activities

- **ShinyHunters**: Conducting second major attack against Instructure/Canvas, affecting hundreds of educational institutions nationwide
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach
- **Brazilian Threat Actors**: Operating TCLBANKER banking trojan targeting 59 financial platforms
- **Russian Cybercriminals**: Advertising PamDOORa Linux backdoor on Rehub forum for $1,600
- **North Korean IT Workers**: Using "laptop farms" operated by sentenced Americans to fraudulently obtain remote employment
- **Various APT Groups**: Exploiting Ivanti EPMM vulnerability for espionage and unauthorized access