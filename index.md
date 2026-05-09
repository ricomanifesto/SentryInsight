# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple critical vulnerabilities and malware campaigns. Zero-day vulnerabilities in Ivanti Endpoint Manager Mobile (CVE-2026-6973) and the Linux kernel ("Dirty Frag") are under active exploitation, enabling remote code execution and privilege escalation respectively. The ShinyHunters threat group has launched multiple successful attacks against educational platforms, compromising Canvas login portals and Instructure systems affecting hundreds of institutions nationwide. Meanwhile, sophisticated malware frameworks including TCLBANKER, PCPJack, and PamDOORa are actively targeting financial institutions, cloud infrastructure, and Linux systems through innovative attack vectors including self-spreading mechanisms and credential theft capabilities.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) allowing attackers to execute arbitrary code on affected systems
- **Impact**: Attackers can gain administrative-level access to endpoint management systems, potentially compromising entire mobile device fleets
- **Status**: Under active exploitation in zero-day attacks; patches available but CISA has mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Kernel Dirty Frag Zero-Day
- **Description**: Unpatched local privilege escalation vulnerability in the Linux kernel affecting all major distributions
- **Impact**: Local attackers can gain root privileges with a single command, compromising system integrity completely
- **Status**: Zero-day exploitation with publicly available proof-of-concept exploit; no patches currently available
- **CVE ID**: CVE-2026-31 (related to Copy Fail vulnerability)

### ShinyHunters Educational Platform Attacks
- **Description**: Mass exploitation campaign targeting Canvas login portals and Instructure systems through unspecified vulnerabilities
- **Impact**: Data extortion affecting hundreds of colleges and universities, disrupting classes and exposing personal information of hundreds of millions of users
- **Status**: Ongoing active exploitation with successful breaches reported across multiple educational institutions

### PCPJack Multi-CVE Exploitation Framework
- **Description**: Advanced credential theft framework exploiting five different CVEs to spread worm-like across cloud infrastructure
- **Impact**: Steals cloud credentials, AWS keys, and other sensitive data while removing competing TeamPCP malware infections
- **Status**: Active exploitation targeting exposed cloud systems with automated propagation capabilities

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: All versions prior to latest security updates
- **Linux Distributions**: All major distributions including Ubuntu, Red Hat, SUSE, Debian affected by Dirty Frag zero-day
- **Canvas Learning Management System**: Login portals at hundreds of educational institutions compromised
- **Instructure Platforms**: Multiple successful breaches by ShinyHunters threat group
- **Financial Platforms**: 59 banking, fintech, and cryptocurrency platforms targeted by TCLBANKER trojan
- **Cloud Infrastructure**: Exposed AWS, Azure, and other cloud environments targeted by PCPJack framework
- **Android Devices**: Google Play Store apps with 7.3 million downloads used for payment fraud
- **WhatsApp and Outlook**: Used as propagation vectors for TCLBANKER malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM and Linux kernel
- **Social Engineering**: ClickFix techniques used to distribute Vidar Stealer malware in Australia
- **Mobile App Fraud**: Fake call history applications on Google Play Store tricking users into payment theft
- **Worm Propagation**: Self-spreading capabilities through WhatsApp and Outlook for TCLBANKER distribution
- **PAM Module Hijacking**: PamDOORa backdoor uses Linux PAM modules to steal SSH credentials
- **Cloud Credential Harvesting**: Automated scanning and exploitation of exposed cloud infrastructure
- **Supply Chain Targeting**: Quasar Linux RAT specifically targets developer systems for software supply chain compromise

## Threat Actor Activities

- **ShinyHunters Group**: Conducting multiple high-profile attacks against educational technology platforms, claiming responsibility for Canvas and Instructure breaches affecting millions of users
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-concept images
- **darkworm Actor**: Advertising PamDOORa Linux backdoor on Russian cybercrime forums for $1,600
- **Brazilian Threat Actors**: Operating TCLBANKER banking trojan with sophisticated self-propagation mechanisms
- **PCPJack Operators**: Running advanced credential theft operations while actively competing with and removing TeamPCP malware
- **North Korean IT Workers**: Using laptop farms operated by convicted U.S. nationals to fraudulently obtain remote employment at 70+ American companies