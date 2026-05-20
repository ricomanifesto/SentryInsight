# Exploitation Report

Critical exploitation activity is escalating across multiple platforms, with Windows zero-day vulnerabilities continuing to emerge after recent Patch Tuesday releases, while threat actors are simultaneously targeting macOS systems with sophisticated infostealers and compromising software supply chains through npm packages and GitHub Actions. A particularly concerning zero-day vulnerability (CVE-2026-42897) in Microsoft Exchange is under active attack with no patch currently available, while Linux kernel exploitation tools have been released for CVE-2026-31635. Supply chain attacks have intensified with over 600 malicious npm packages deployed in new Shai-Hulud campaigns, and credential theft operations are targeting developers through compromised VS Code extensions and GitHub repositories.

## Active Exploitation Details

### Microsoft Exchange Zero-Day Vulnerability
- **Description**: Cross-site scripting (XSS) vulnerability affecting Microsoft Exchange servers
- **Impact**: Attackers can compromise Outlook Web Access (OWA) mailboxes and potentially gain unauthorized access to email systems
- **Status**: Currently under active attack with no patch available
- **CVE ID**: CVE-2026-42897

### Windows Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities including YellowKey, GreenPlasma, and MiniPlasma discovered by security researchers
- **Impact**: Various exploitation capabilities across Windows systems
- **Status**: Disclosed over a six-week period following Patch Tuesday releases, exploitation status varies

### Linux Kernel Local Privilege Escalation
- **Description**: DirtyDecrypt vulnerability in the Linux kernel allowing local privilege escalation
- **Impact**: Local attackers can escalate privileges on affected Linux systems
- **Status**: Recently patched with proof-of-concept exploit code now publicly available
- **CVE ID**: CVE-2026-31635

### SEPPMail Secure E-Mail Gateway Vulnerabilities
- **Description**: Critical security vulnerabilities in enterprise-grade email security solution
- **Impact**: Remote code execution and access to mail traffic
- **Status**: Disclosed vulnerabilities requiring immediate patching

### OAuth Consent Bypass Attacks
- **Description**: EvilTokens phishing-as-a-service platform exploiting OAuth consent mechanisms
- **Impact**: Bypasses multi-factor authentication and compromises Microsoft 365 organizations
- **Status**: Active exploitation with over 340 organizations compromised across five countries within five weeks

## Affected Systems and Products

- **Microsoft Exchange Servers**: Outlook Web Access (OWA) components vulnerable to XSS attacks
- **Windows Operating Systems**: Multiple versions affected by zero-day vulnerabilities YellowKey, GreenPlasma, and MiniPlasma
- **Linux Kernel**: Various distributions affected by DirtyDecrypt local privilege escalation vulnerability
- **SEPPMail Secure E-Mail Gateway**: Enterprise email security solutions
- **macOS Systems**: Targeted by SHub Reaper stealer variants spoofing Apple security updates
- **npm Package Ecosystem**: Over 600 malicious packages deployed in supply chain attacks
- **Visual Studio Code**: Compromised Nx Console extension targeting developers
- **GitHub Actions**: Popular workflow actions-cool/issues-helper compromised
- **Microsoft 365 and Azure**: Targeted through Self-Service Password Reset abuse

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of Exchange servers to compromise OWA mailboxes
- **Supply Chain Poisoning**: Compromised npm packages and VS Code extensions delivering malicious payloads
- **Social Engineering**: SHub stealer variants masquerading as legitimate software updates from Google, Microsoft, and Apple
- **OAuth Consent Manipulation**: EvilTokens platform bypassing MFA through malicious consent requests
- **GitHub Repository Compromise**: Malicious code injection into popular GitHub Actions workflows
- **Credential Harvesting**: Targeting CI/CD pipelines and developer environments
- **AppleScript-Based Execution**: macOS malware using legitimate scripting capabilities for persistence
- **Self-Service Feature Abuse**: Exploitation of legitimate Microsoft administrative features

## Threat Actor Activities

- **ShinyHunters Gang**: Confirmed breach of 7-Eleven convenience store chain systems with data theft
- **Shai-Hulud Operators**: Multiple waves of supply chain attacks targeting npm ecosystem with self-replicating worm capabilities
- **SHub Reaper Operators**: Sophisticated macOS targeting campaign using fake installers and Apple script execution
- **EvilTokens PhaaS Users**: Widespread Microsoft 365 compromise campaigns across multiple countries
- **Mini Shai-Hulud Campaign**: Targeted compromise of @antv ecosystem packages through maintainer account takeover
- **GitHub Actions Attackers**: Supply chain compromise of popular development workflows for credential theft
- **Trapdoor Android Operators**: Ad fraud scheme affecting 659 million daily bid requests using 455 compromised applications