# Exploitation Report

The current threat landscape shows several critical zero-day vulnerabilities under active exploitation, with particularly concerning activity targeting enterprise infrastructure and cloud environments. The most severe active exploitations include CVE-2026-6973 affecting Ivanti Endpoint Manager Mobile, which grants admin-level access and has prompted CISA to issue emergency patching directives. Additionally, a new Linux kernel zero-day dubbed "Dirty Frag" is being exploited to gain root privileges across major distributions. Cloud infrastructure faces significant threats from the PCPJack credential stealer exploiting five different CVEs to spread worm-like across systems, while the ShinyHunters group continues exploiting vulnerabilities in Canvas education platforms. Threat actors are also leveraging sophisticated social engineering through ClickFix campaigns and deploying advanced malware like TCLBANKER, which spreads through WhatsApp and Outlook.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: A high-severity remote code execution flaw in Ivanti Endpoint Manager Mobile that allows attackers to gain administrative privileges on affected systems
- **Impact**: Grants admin-level access to enterprise mobile device management infrastructure, enabling full system compromise
- **Status**: Under active exploitation in limited attacks; patches available
- **CVE ID**: CVE-2026-6973

### Linux Kernel "Dirty Frag" Zero-Day
- **Description**: An unpatched local privilege escalation vulnerability in the Linux kernel that allows attackers to gain root access with a single command
- **Impact**: Enables complete system compromise on all major Linux distributions
- **Status**: Actively exploited with public proof-of-concept exploit available; no patches currently available

### Canvas Education Platform Vulnerabilities
- **Description**: Multiple vulnerabilities in the Canvas learning management system exploited to deface login portals and conduct data extortion
- **Impact**: Widespread disruption of educational services across hundreds of colleges and universities
- **Status**: Under active exploitation by ShinyHunters group

### PCPJack Multi-CVE Exploitation Framework
- **Description**: A credential theft framework that exploits five different vulnerabilities to spread across cloud infrastructure
- **Impact**: Steals cloud credentials and secrets while removing competing malware from compromised systems
- **Status**: Actively spreading through exposed cloud environments

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platforms vulnerable to CVE-2026-6973
- **Linux Distributions**: All major Linux distributions affected by Dirty Frag zero-day exploit
- **Canvas Learning Management System**: Educational institutions using Canvas platform experiencing login portal compromises
- **Cloud Infrastructure**: Exposed cloud environments targeted by PCPJack framework
- **Android Devices**: Google Play Store apps with 7.3 million downloads spreading fraudulent payment stealing malware
- **PAN-OS Firewalls**: Palo Alto Networks devices targeted for root access and espionage
- **WhatsApp and Outlook**: Communication platforms used for TCLBANKER malware distribution
- **Banking and Financial Platforms**: 59 different banking, fintech, and cryptocurrency platforms targeted by TCLBANKER

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in critical enterprise systems
- **Social Engineering via ClickFix**: Fake error messages tricking users into executing malicious PowerShell scripts
- **Worm-Like Propagation**: PCPJack framework automatically spreading across compromised cloud infrastructure
- **Supply Chain Compromise**: Quasar Linux RAT targeting developers to infiltrate software development environments
- **Mobile App Store Fraud**: Malicious apps disguised as legitimate call history tools on Google Play Store
- **PAM Module Abuse**: PamDOORa backdoor exploiting Linux PAM authentication system to steal SSH credentials
- **Communication Platform Hijacking**: TCLBANKER spreading through WhatsApp messages and Outlook emails
- **Educational Platform Defacement**: Mass compromise of Canvas login portals for extortion purposes

## Threat Actor Activities

- **ShinyHunters Group**: Conducting mass extortion campaign against Canvas education platform with widespread portal defacements
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach
- **PCPJack Operators**: Deploying sophisticated credential theft framework while actively removing competing TeamPCP malware
- **TCLBANKER Campaign**: Brazilian threat actors targeting 59 financial platforms using self-spreading trojan via messaging applications
- **ClickFix Campaigns**: Australian-targeted attacks distributing Vidar Stealer malware through social engineering
- **PamDOORa Distributors**: Russian cybercrime forum actors selling Linux backdoor for $1,600
- **Quasar Linux RAT Campaign**: Targeting software developers to establish persistent access for supply chain attacks
- **North Korean IT Workers**: Operating laptop farms to fraudulently obtain remote employment at American companies