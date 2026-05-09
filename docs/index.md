# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, with threat actors targeting enterprise infrastructure and cloud systems. The most severe active exploitation involves an Ivanti Endpoint Manager Mobile vulnerability (CVE-2026-6973) being exploited for remote code execution with admin-level access. Additionally, a new Linux kernel zero-day dubbed "Dirty Frag" allows local privilege escalation to root across major distributions. Multiple malware campaigns are leveraging social engineering and supply chain attacks, including the ShinyHunters group's ongoing extortion campaign against educational platforms and new credential-stealing frameworks targeting cloud infrastructure.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) being exploited in limited zero-day attacks
- **Impact**: Allows attackers to achieve admin-level access to affected systems
- **Status**: Under active exploitation; CISA has given federal agencies four days to patch
- **CVE ID**: CVE-2026-6973

### Linux Kernel Dirty Frag Zero-Day
- **Description**: Unpatched local privilege escalation vulnerability in the Linux kernel, described as a successor to Copy Fail
- **Impact**: Enables local attackers to gain root privileges on most major Linux distributions with a single command
- **Status**: Zero-day with proof-of-concept exploit available; currently unpatched

### PAN-OS Remote Code Execution Vulnerability
- **Description**: Critical security flaw in Palo Alto Networks PAN-OS that threat actors have attempted to exploit
- **Impact**: Enables root access and potential espionage activities
- **Status**: Under active exploitation attempts since April 9, 2026

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Systems vulnerable to remote code execution attacks
- **Linux Kernel**: All major Linux distributions affected by Dirty Frag zero-day
- **Palo Alto Networks PAN-OS**: Firewalls and security appliances at risk of compromise
- **cPanel and Web Host Manager (WHM)**: Three vulnerabilities allowing privilege escalation, code execution, and denial-of-service
- **Canvas Learning Management System**: Educational platforms targeted in mass extortion campaign
- **Hugging Face Platform**: Malicious repositories impersonating legitimate projects
- **Google Play Store**: Fraudulent apps with 7.3 million downloads stealing payments

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in enterprise systems
- **Social Engineering**: ClickFix attacks and fake repositories to distribute malware
- **Supply Chain Compromise**: Malicious apps on official platforms and trojanized software installers
- **Credential Theft**: PAM module manipulation and cloud infrastructure targeting
- **Worm Propagation**: Self-spreading malware using WhatsApp and Outlook for distribution
- **Extortion Campaigns**: Mass defacement and data theft for ransom demands

## Threat Actor Activities

- **ShinyHunters**: Conducting second attack against Instructure/Canvas with mass portal defacement and extortion
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach
- **TCLBanker Operators**: Targeting 59 banking, fintech, and cryptocurrency platforms with self-spreading trojan
- **PCPJack Framework Authors**: Deploying credential-stealing worm that exploits 5 CVEs across cloud systems
- **darkworm (PamDOORa Author)**: Advertising Linux backdoor on Russian cybercrime forums for $1,600
- **Quasar Linux RAT Operators**: Targeting developers' systems for software supply chain compromise