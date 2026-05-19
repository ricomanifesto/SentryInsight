# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation, with attackers leveraging unpatched flaws in Microsoft Exchange Server and Windows systems to compromise organizations. Supply chain attacks have intensified through compromised npm packages, GitHub repositories, and developer tools, while threat actors are exploiting OAuth consent mechanisms to bypass multi-factor authentication. The cybersecurity landscape is experiencing significant threats from the leaked Shai-Hulud malware source code, which has enabled widespread infostealer campaigns across the npm ecosystem. Additionally, vulnerabilities in enterprise security solutions like SEPPMail are providing attackers with remote code execution capabilities and access to sensitive email traffic.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day
- **Description**: A cross-site scripting (XSS) vulnerability in Microsoft Exchange Server allowing attackers to compromise Outlook Web Access (OWA) mailboxes
- **Impact**: Attackers can gain unauthorized access to email systems and potentially escalate privileges within the environment
- **Status**: Currently under active exploitation with no patch available
- **CVE ID**: CVE-2026-42897

### MiniPlasma Windows Zero-Day
- **Description**: A privilege escalation vulnerability in Windows systems that affects fully patched installations
- **Impact**: Enables attackers to escalate privileges to SYSTEM level, providing complete control over compromised systems
- **Status**: Proof-of-concept code has been publicly released by security researcher Chaotic Eclipse
- **CVE ID**: Not specified in source materials

### OAuth Consent Bypass Attacks
- **Description**: Phishing-as-a-Service platform called EvilTokens exploiting OAuth consent mechanisms to bypass multi-factor authentication
- **Impact**: Compromised more than 340 Microsoft 365 organizations across five countries within five weeks of operation
- **Status**: Active exploitation campaign targeting enterprise environments

### SEPPMail Secure E-Mail Gateway Vulnerabilities
- **Description**: Critical security vulnerabilities in SEPPMail's enterprise email security solution
- **Impact**: Remote code execution capabilities and unauthorized access to mail traffic
- **Status**: Vulnerabilities disclosed with patches available

### Drupal Core Security Issues
- **Description**: Urgent security vulnerabilities affecting all supported branches of Drupal
- **Impact**: Potential for widespread website compromise
- **Status**: Security updates scheduled for release on May 20, 2026

## Affected Systems and Products

- **Microsoft Exchange Server**: OWA mailboxes vulnerable to XSS-based attacks
- **Windows 11**: Security update installation failures and privilege escalation vulnerabilities
- **Microsoft 365**: Organizations targeted through OAuth consent bypass attacks
- **VS Code Marketplace**: Compromised Nx Console extension version 18.95.0
- **npm Package Repository**: Multiple malicious packages including Shai-Hulud variants and AntV ecosystem packages
- **GitHub Actions**: Compromised actions-cool/issues-helper workflow
- **SEPPMail Secure E-Mail Gateway**: Enterprise email security solution with RCE vulnerabilities
- **Drupal CMS**: All supported branches requiring urgent security updates
- **OpenClaw AI Framework**: "Claw Chain" vulnerabilities enabling credential theft
- **macOS Systems**: SHub infostealer variant disguised as Apple security updates

## Attack Vectors and Techniques

- **OAuth Consent Manipulation**: Attackers bypass MFA by exploiting OAuth consent flows in Microsoft 365 environments
- **Supply Chain Compromise**: Malicious packages injected into npm repository, VS Code marketplace, and GitHub Actions
- **Cross-Site Scripting**: XSS vulnerability in Exchange Server used to compromise OWA mailboxes
- **Social Engineering**: Fake Apple security update messages used to install macOS infostealers
- **Privilege Escalation**: Zero-day Windows vulnerability enabling SYSTEM-level access
- **Credential Harvesting**: Malicious extensions and packages designed to steal developer credentials
- **Repository Poisoning**: Legitimate packages compromised through maintainer account takeovers
- **AppleScript Abuse**: macOS malware using AppleScript to display fake security prompts

## Threat Actor Activities

- **EvilTokens PhaaS Operators**: Compromised 340+ Microsoft 365 organizations using OAuth consent bypass techniques
- **Mini Shai-Hulud Campaign**: Threat actors leveraging leaked malware source code to compromise npm packages
- **Iranian Threat Groups**: Expanding cyber offensive operations to target fuel tank infrastructure systems
- **Supply Chain Attackers**: Multiple campaigns targeting developer environments through compromised tools and repositories
- **Cybercrime Networks**: INTERPOL Operation Ramz resulted in 201 arrests across Middle East and North Africa regions
- **Repository Compromise Groups**: Attackers gaining access to GitHub tokens and stealing source code from organizations like Grafana Labs
- **CISA Contractor Incident**: AWS GovCloud credentials inadvertently exposed on public GitHub repository
- **TeamPCP**: Security research group that open-sourced Shai-Hulud malware, leading to widespread abuse by threat actors