# Exploitation Report

Critical zero-day vulnerabilities and active malware campaigns are dominating the current threat landscape. Most notably, attackers are exploiting CVE-2026-6973 in Ivanti Endpoint Manager Mobile (EPMM) in limited wild attacks, while a new Linux zero-day dubbed "Dirty Frag" provides root access across all major distributions. Simultaneously, sophisticated malware frameworks like PCPJack are exploiting multiple vulnerabilities to spread worm-like across cloud systems, and the ShinyHunters group has launched mass extortion campaigns against educational institutions. The threat environment is further complicated by supply chain attacks targeting developer environments and widespread malvertising campaigns leveraging trusted platforms.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager Mobile allowing remote code execution with admin-level access
- **Impact**: Attackers can gain administrative privileges on mobile device management systems
- **Status**: Under active exploitation in limited attacks; patch available
- **CVE ID**: CVE-2026-6973

### Linux Kernel Dirty Frag Zero-Day
- **Description**: Local privilege escalation vulnerability in the Linux kernel, described as successor to Copy Fail vulnerability
- **Impact**: Allows local attackers to gain root privileges on most major Linux distributions with a single command
- **Status**: Unpatched zero-day with public proof-of-concept exploit available

### Ollama Out-of-Bounds Read
- **Description**: Critical vulnerability in Ollama allowing remote, unauthenticated attackers to leak entire process memory
- **Impact**: Complete process memory disclosure leading to potential credential theft and sensitive data exposure
- **Status**: Recently disclosed vulnerability requiring immediate patching

### PCPJack Multi-CVE Exploitation
- **Description**: Credential theft framework exploiting five different CVEs to spread across cloud systems
- **Impact**: Steals cloud credentials and secrets while actively removing competing malware (TeamPCP)
- **Status**: Active in the wild with worm-like propagation capabilities

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management systems vulnerable to remote code execution
- **Linux Distributions**: All major Linux distributions affected by Dirty Frag zero-day privilege escalation
- **Ollama**: AI model platform vulnerable to memory leak attacks
- **Canvas Education Platform**: Learning management system targeted in mass extortion campaigns
- **JDownloader**: Popular download manager with compromised installers distributing Python RAT
- **cPanel and WHM**: Web hosting control panels with three newly patched vulnerabilities
- **macOS Systems**: Targeted through malicious Google Ads and Claude.ai chat abuse
- **Android Devices**: Fake call history apps on Google Play Store with 7.3 million downloads
- **Cloud Infrastructure**: AWS, Azure, and other cloud platforms targeted by PCPJack framework

## Attack Vectors and Techniques

- **Malvertising**: Abuse of Google Ads to promote malicious macOS applications disguised as Claude AI downloads
- **Supply Chain Compromise**: Replacement of legitimate software installers with malware-laden versions
- **Social Engineering (ClickFix)**: Fake browser error messages tricking users into running malicious PowerShell scripts
- **Platform Abuse**: Creation of fake repositories on trusted platforms like Hugging Face to distribute malware
- **Worm Propagation**: Self-spreading malware using messaging platforms (WhatsApp, Outlook) for distribution
- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities for privilege escalation and system compromise
- **PAM Module Hijacking**: Linux backdoors using Pluggable Authentication Modules to steal SSH credentials
- **Memory Exploitation**: Out-of-bounds read attacks targeting AI platforms for sensitive data extraction

## Threat Actor Activities

- **ShinyHunters**: Conducting mass extortion campaigns against educational institutions, targeting Canvas platforms and Instructure systems multiple times
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-concept images
- **TCLBanker Operators**: Targeting 59 banking, fintech, and cryptocurrency platforms using trojanized Logitech software installers
- **PCPJack Framework Users**: Advanced threat actors targeting cloud infrastructure with multi-CVE exploitation techniques
- **Darkworm**: Threat actor advertising PamDOORa Linux backdoor on Russian cybercrime forums for $1,600
- **Malvertising Groups**: Sophisticated campaigns abusing legitimate platforms (Google Ads, Claude.ai) to distribute macOS malware
- **Mobile Malware Distributors**: Publishing fraudulent applications on Google Play Store with millions of downloads for payment theft