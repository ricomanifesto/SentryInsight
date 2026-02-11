# Exploitation Report

The current threat landscape reveals critical ongoing exploitation activities targeting multiple platforms and industries. Microsoft has addressed six actively exploited zero-day vulnerabilities in their February 2026 Patch Tuesday, highlighting the persistent targeting of Windows systems. Meanwhile, threat actors are exploiting unpatched SolarWinds Web Help Desk vulnerabilities and compromising SmarterMail servers to deploy malicious tools and ransomware. The emergence of sophisticated mobile malware platforms and advanced ransomware variants incorporating defense evasion techniques demonstrates the evolving sophistication of cybercriminal operations. Additionally, state-sponsored actors continue conducting large-scale espionage campaigns against critical infrastructure, particularly targeting telecommunications providers across multiple countries.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities actively exploited in the wild before patches were released
- **Impact**: Attackers can gain unauthorized access and execute arbitrary code on Windows systems
- **Status**: Patched in Microsoft's February 2026 Patch Tuesday security updates

### SolarWinds Web Help Desk Vulnerabilities
- **Description**: Multiple flaws in SolarWinds Web Help Desk (WHD) allowing remote code execution
- **Impact**: Attackers gain code execution rights on exposed systems and deploy legitimate forensics tools like Velociraptor for malicious purposes
- **Status**: Currently being exploited in active attacks

### SmarterMail Server Vulnerabilities
- **Description**: Unpatched vulnerabilities in SmarterMail email server software
- **Impact**: Complete network compromise leading to ransomware deployment
- **Status**: Actively exploited by Warlock ransomware gang to breach SmarterTools' own network

### Ivanti Zero-Day Vulnerabilities
- **Description**: Zero-day exploits targeting Ivanti systems
- **Impact**: Exposure of employee contact data and system compromise
- **Status**: Confirmed exploitation by threat actors targeting Dutch government agencies

### Fortinet FortiClientEMS SQL Injection Flaw
- **Description**: Critical SQL injection vulnerability enabling remote code execution
- **Impact**: Unauthenticated attackers can execute arbitrary code on vulnerable systems
- **Status**: Patches released by Fortinet
- **CVE ID**: CVE-2026-47923

## Affected Systems and Products

- **Microsoft Windows Systems**: Windows 10 and Windows 11 affected by six zero-day vulnerabilities
- **SolarWinds Web Help Desk**: Exposed installations vulnerable to code execution attacks
- **SmarterMail Email Servers**: Unpatched instances targeted by ransomware groups
- **Fortinet FortiClientEMS**: Systems vulnerable to SQL injection attacks
- **Ivanti Systems**: Government and enterprise deployments compromised
- **Android and iOS Devices**: Targeted by ZeroDayRAT mobile spyware platform
- **Singapore Telecommunications Infrastructure**: Four largest telecom providers breached
- **Cloud Infrastructure**: AWS and other cloud platforms targeted by TeamPCP threat actor

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Targeting of unknown vulnerabilities before patches are available
- **Supply Chain Attacks**: Compromise of software vendors to target their customers
- **Bring Your Own Vulnerable Driver (BYOVD)**: Reynolds ransomware embeds vulnerable drivers to disable EDR security tools
- **Living-off-the-Plant Techniques**: OT-specific attack methods using legitimate industrial tools
- **Fake Software Distribution**: Malicious 7-Zip websites distributing trojanized installers
- **Social Engineering on LinkedIn**: DPRK operatives impersonating professionals to infiltrate companies
- **Mobile Device Compromise**: ZeroDayRAT providing full remote control over smartphones and tablets
- **Automated Cloud Attacks**: Worm-like attacks targeting exposed cloud services and interfaces

## Threat Actor Activities

- **UNC3886 (China-linked)**: Conducting cyber espionage campaigns against Singapore's four largest telecommunications providers
- **Warlock Ransomware Gang (Storm-2603)**: Exploiting SmarterMail vulnerabilities to deploy ransomware and breach SmarterTools network
- **DPRK IT Workers**: Using stolen LinkedIn identities to apply for remote positions and infiltrate companies
- **TeamPCP**: Compromising cloud infrastructure at scale to create crime botnet operations
- **Reynolds Ransomware Operators**: Deploying advanced ransomware with embedded defense evasion capabilities
- **Chinese Cyberspies**: Targeting critical infrastructure and government agencies across multiple countries
- **ZeroDayRAT Operators**: Advertising commercial mobile spyware platform on Telegram for cybercriminal use