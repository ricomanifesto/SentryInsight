# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms and systems. The most severe activity includes the "Dirty Frag" Linux kernel zero-day allowing root privilege escalation across major distributions, an Ivanti Endpoint Manager Mobile vulnerability (CVE-2026-6973) being exploited in limited attacks, and a widespread ShinyHunters campaign targeting educational institutions through Canvas platform breaches. Additionally, multiple malware campaigns are leveraging supply chain compromises, including the JDownloader website breach distributing Python RATs and fraudulent applications on major platforms. The PCPJack credential stealer is actively exploiting five vulnerabilities to spread worm-like across cloud infrastructure while new banking trojans target financial platforms through messaging applications.

## Active Exploitation Details

### Linux Kernel "Dirty Frag" Zero-Day
- **Description**: A local privilege escalation vulnerability in the Linux kernel that allows attackers to gain root access with a single command
- **Impact**: Complete system compromise with root privileges on all major Linux distributions
- **Status**: Currently unpatched zero-day with proof-of-concept exploit available

### Ivanti EPMM Remote Code Execution
- **Description**: A high-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM)
- **Impact**: Admin-level access and complete system compromise
- **Status**: Under active exploitation in limited attacks; patches available
- **CVE ID**: CVE-2026-6973

### cPanel and WHM Vulnerabilities
- **Description**: Three newly disclosed vulnerabilities in cPanel and Web Host Manager systems
- **Impact**: Privilege escalation, code execution, and denial-of-service attacks
- **Status**: Patches recently released, exploitation status unknown

### PCPJack Credential Stealer Vulnerabilities
- **Description**: Five vulnerabilities being exploited by the PCPJack malware framework to target cloud infrastructure
- **Impact**: Credential theft and worm-like propagation across cloud systems
- **Status**: Active exploitation for credential harvesting and system compromise

### PAN-OS Critical RCE
- **Description**: A critical remote code execution vulnerability in Palo Alto Networks PAN-OS
- **Impact**: Root access and espionage capabilities
- **Status**: Under active exploitation attempts since April 2026

## Affected Systems and Products

- **Linux Systems**: All major Linux distributions affected by Dirty Frag zero-day
- **Ivanti EPMM**: Endpoint Manager Mobile systems vulnerable to remote code execution
- **cPanel/WHM**: Web hosting control panels with privilege escalation vulnerabilities
- **Canvas Platform**: Educational technology platform compromised in mass breach campaign
- **JDownloader**: Download manager website compromised to distribute malicious installers
- **Hugging Face**: AI model repository hosting fake OpenAI projects with malware
- **Google Play Store**: Android platform hosting fraudulent call history applications
- **Cloud Infrastructure**: Systems targeted by PCPJack credential stealer
- **Palo Alto Networks**: PAN-OS systems vulnerable to critical RCE

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious installers distributed through compromised legitimate websites
- **Social Engineering**: ClickFix techniques and fake repositories targeting developers
- **Worm Propagation**: Self-spreading malware through WhatsApp and Outlook
- **Credential Harvesting**: PAM module manipulation and SSH credential theft
- **Platform Impersonation**: Fake applications and repositories mimicking legitimate services
- **Zero-Day Exploitation**: Direct kernel exploitation for privilege escalation
- **Mass Defacement**: Bulk compromise of educational login portals
- **Mobile Malware**: Android applications stealing payment information

## Threat Actor Activities

- **ShinyHunters**: Conducting second major attack campaign against Instructure/Canvas platform with mass defacement of educational login portals
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach
- **TCLBANKER Operators**: Deploying banking trojan targeting 59 financial platforms through trojanized Logitech installer
- **PCPJack Developers**: Operating credential theft framework targeting cloud infrastructure while removing competing TeamPCP malware
- **darkworm**: Russian cybercrime forum actor selling PamDOORa Linux backdoor for $1,600
- **Brazilian Banking Groups**: Operating TCLBANKER campaign with self-spreading capabilities
- **Fraudulent App Publishers**: Distributing fake call history apps on Google Play Store with 7.3 million downloads