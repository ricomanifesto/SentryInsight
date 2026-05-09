# Exploitation Report

Current exploitation activity reveals several critical zero-day vulnerabilities and active attack campaigns targeting diverse infrastructure. Most notably, the Linux "Dirty Frag" zero-day enables root access across major distributions, while Ivanti EPMM faces active exploitation through CVE-2026-6973. The threat landscape is further complicated by sophisticated malware campaigns including TCLBANKER banking trojan, PCPJack credential stealer exploiting five CVEs, and the PamDOORa backdoor targeting SSH credentials. Educational institutions face massive disruption through ShinyHunters' attacks on Canvas platforms, while new worm-like malware demonstrates advanced evasion and propagation techniques across cloud environments.

## Active Exploitation Details

### Linux Dirty Frag Zero-Day
- **Description**: An unpatched local privilege escalation vulnerability in the Linux kernel that allows attackers to gain root privileges with a single command
- **Impact**: Complete system compromise with root access across all major Linux distributions
- **Status**: Actively exploited zero-day with public proof-of-concept exploit available, currently unpatched

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager Mobile allowing remote code execution with admin-level access
- **Impact**: Complete system compromise with administrative privileges on mobile endpoint management infrastructure
- **Status**: Actively exploited in limited zero-day attacks, patch available
- **CVE ID**: CVE-2026-6973

### PAN-OS Critical Remote Code Execution
- **Description**: Critical security flaw in Palo Alto Networks PAN-OS enabling remote code execution and root access
- **Impact**: Complete firewall compromise allowing espionage and network infiltration
- **Status**: Under active exploitation attempts since April 9, 2026

## Affected Systems and Products

- **Linux Distributions**: All major distributions vulnerable to Dirty Frag privilege escalation exploit
- **Ivanti Endpoint Manager Mobile**: Systems running vulnerable EPMM versions subject to zero-day exploitation
- **Palo Alto Networks Firewalls**: PAN-OS systems targeted for remote code execution attacks
- **Canvas Educational Platform**: Login portals across hundreds of colleges and universities compromised by ShinyHunters
- **Banking and Financial Platforms**: 59 banking, fintech, and cryptocurrency platforms targeted by TCLBANKER trojan
- **Cloud Infrastructure**: Exposed cloud systems targeted by PCPJack credential stealer
- **WhatsApp and Outlook**: Communication platforms exploited for malware propagation
- **Google Play Store**: Android platform affected by fraudulent call history apps with 7.3 million downloads

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Fake error messages used to distribute Vidar Stealer malware in Australian campaign
- **PAM Module Exploitation**: PamDOORa backdoor leverages Linux PAM modules to steal SSH credentials
- **MSI Installer Trojanization**: TCLBANKER distributed through fake Logitech AI Prompt Builder installer
- **Worm Propagation**: Self-spreading malware using WhatsApp and Outlook for distribution
- **Parquet File Abuse**: PCPJack uses parquet files for stealthy target discovery across cloud environments
- **Canvas Portal Defacement**: Mass exploitation campaign targeting educational platform login portals
- **Fraudulent App Distribution**: Fake call history applications on Google Play Store for payment theft

## Threat Actor Activities

- **ShinyHunters**: Conducting second major attack against Instructure, exploiting Canvas vulnerabilities to deface login portals across educational institutions nationwide
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-intrusion images
- **Brazilian Banking Threat Actors**: Operating TCLBANKER trojan campaign targeting Latin American financial institutions
- **darkworm**: Advertising PamDOORa backdoor on Russian cybercrime forum Rehub for $1,600
- **PCPJack Operators**: Running sophisticated credential theft operations while actively removing TeamPCP malware from infected systems
- **North Korean IT Workers**: Utilizing laptop farms operated by convicted Americans to fraudulently obtain remote employment at U.S. companies