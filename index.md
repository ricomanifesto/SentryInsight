# Exploitation Report

Current threat activity demonstrates a significant escalation in supply chain attacks and zero-day exploitation targeting critical infrastructure. Notable active exploitation includes CVE-2026-42897, a Microsoft Exchange zero-day vulnerability with no available patch that enables compromise of Outlook Web Access mailboxes through cross-site scripting attacks. Additionally, multiple sophisticated supply chain campaigns are targeting developer environments, with compromised VS Code extensions, GitHub Actions, and npm packages delivering credential stealers. The emergence of the MiniPlasma Windows zero-day with publicly available proof-of-concept code poses immediate privilege escalation risks to fully patched systems, while the leaked Shai-Hulud malware source code has spawned numerous copycat attacks across package repositories.

## Active Exploitation Details

### Microsoft Exchange Zero-Day Vulnerability
- **Description**: Cross-site scripting (XSS) vulnerability in Microsoft Exchange Server affecting Outlook Web Access
- **Impact**: Allows attackers to compromise OWA mailboxes and potentially gain unauthorized access to email systems
- **Status**: Currently under active attack with no patch available
- **CVE ID**: CVE-2026-42897

### MiniPlasma Windows Privilege Escalation Zero-Day
- **Description**: Local privilege escalation vulnerability in Windows systems allowing attackers to gain SYSTEM privileges
- **Impact**: Complete system compromise on fully patched Windows systems with highest privilege access
- **Status**: Proof-of-concept exploit publicly released, actively exploitable
- **CVE ID**: Not specified in articles

### Shai-Hulud Worm and Variants
- **Description**: Self-replicating malware targeting npm package repositories with leaked source code enabling widespread adoption
- **Impact**: Information stealing, credential harvesting, and supply chain compromise
- **Status**: Source code leaked, multiple copycat attacks observed in wild

### DirtyDecrypt Linux Privilege Escalation
- **Description**: Local privilege escalation vulnerability in Linux kernel's rxgk module
- **Impact**: Root access compromise on affected Linux systems
- **Status**: Recently patched with proof-of-concept exploit available

## Affected Systems and Products

- **Microsoft Exchange Server**: Outlook Web Access components vulnerable to XSS attacks
- **Windows Systems**: All versions affected by MiniPlasma zero-day privilege escalation
- **Visual Studio Code**: Nx Console extension version 18.95.0 compromised with credential stealer
- **GitHub Actions**: actions-cool/issues-helper workflow compromised for CI/CD credential theft
- **npm Package Repository**: Multiple @antv ecosystem packages compromised via maintainer account breach
- **Linux Systems**: Distributions with rxgk module vulnerable to DirtyDecrypt exploitation
- **Grafana Labs**: Source code accessed through stolen GitHub token compromise
- **OpenClaw AI Framework**: Multiple vulnerabilities in rapidly growing AI agent deployments

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Targeting developer tools, package managers, and CI/CD pipelines for credential harvesting
- **Extension Poisoning**: Malicious VS Code extensions delivering credential stealers to development environments
- **Package Repository Attacks**: Compromised maintainer accounts pushing malicious packages to npm and other repositories
- **Device-Code Phishing**: Tycoon2FA kit abusing Microsoft 365 authentication flows with Trustifi URL manipulation
- **Cross-Site Scripting**: Exchange zero-day exploitation targeting web-based email access
- **Privilege Escalation**: Local exploitation techniques for Windows and Linux systems
- **AppleScript Spoofing**: SHub macOS infostealer masquerading as Apple security updates

## Threat Actor Activities

- **Mini Shai-Hulud Campaign**: Compromising npm packages through maintainer account breaches targeting @antv ecosystem
- **Iranian Cyber Operations**: Expanding offensive capabilities targeting automatic tank gauge systems in fuel infrastructure
- **MENA Cybercrime Networks**: 201 arrests and 382 suspects identified in INTERPOL Operation Ramz targeting Middle East and North Africa
- **Supply Chain Attackers**: Multiple coordinated campaigns targeting developer workstations and software distribution channels
- **Tycoon2FA Operations**: Enhanced phishing kit targeting Microsoft 365 accounts through device-code manipulation techniques