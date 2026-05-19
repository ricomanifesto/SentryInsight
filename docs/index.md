# Exploitation Report

The current threat landscape reveals a surge in critical exploitation activities across multiple attack vectors. Microsoft Exchange is experiencing active zero-day exploitation through CVE-2026-42897, a cross-site scripting vulnerability with no available patch. Simultaneously, Linux systems face elevated risks from CVE-2026-31635, a local privilege escalation vulnerability in the kernel dubbed "DirtyDecrypt" that now has publicly available proof-of-concept exploit code. The software supply chain ecosystem is under severe assault through massive npm package compromises, with threat actors deploying Shai-Hulud malware variants across hundreds of packages. Enterprise email security is compromised through SEPPMail gateway vulnerabilities enabling remote code execution, while development environments face targeted attacks through compromised VS Code extensions and GitHub Actions workflows.

## Active Exploitation Details

### Microsoft Exchange Zero-Day Vulnerability
- **Description**: Cross-site scripting vulnerability in Microsoft Exchange Server allowing attackers to compromise Outlook Web Access mailboxes
- **Impact**: Attackers can gain unauthorized access to OWA mailboxes and potentially steal sensitive email communications
- **Status**: Currently being actively exploited with no patch available
- **CVE ID**: CVE-2026-42897

### DirtyDecrypt Linux Kernel Vulnerability
- **Description**: Local privilege escalation vulnerability in the Linux kernel that allows attackers to gain elevated privileges
- **Impact**: Local attackers can escalate their privileges to gain root access on affected Linux systems
- **Status**: Recently patched but proof-of-concept exploit code has been publicly released
- **CVE ID**: CVE-2026-31635

### SEPPMail Secure E-Mail Gateway Vulnerabilities
- **Description**: Critical security vulnerabilities in SEPPMail Secure E-Mail Gateway enterprise email security solution
- **Impact**: Remote code execution capabilities and unauthorized access to mail traffic
- **Status**: Vulnerabilities disclosed with exploitation potential for RCE and mail interception

## Affected Systems and Products

- **Microsoft Exchange Server**: Outlook Web Access components vulnerable to XSS attacks
- **Linux Kernel**: Multiple distributions affected by DirtyDecrypt privilege escalation flaw
- **SEPPMail Secure E-Mail Gateway**: Enterprise-grade email security solution with RCE vulnerabilities
- **npm Package Ecosystem**: Over 600 malicious packages deployed in Shai-Hulud campaign
- **Visual Studio Code Marketplace**: Nx Console extension compromised with credential stealer
- **GitHub Actions Workflows**: actions-cool/issues-helper workflow compromised for credential harvesting
- **@antv npm Packages**: Multiple packages in the @antv ecosystem compromised through maintainer account breach
- **macOS Systems**: SHub infostealer variant targeting users through fake Apple security updates
- **Grafana Environment**: Source code accessed through stolen GitHub tokens
- **7-Eleven Systems**: Customer data compromised in ShinyHunters extortion campaign

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of Exchange Server to compromise webmail access
- **Local Privilege Escalation**: DirtyDecrypt technique targeting Linux kernel vulnerabilities
- **Supply Chain Poisoning**: Massive npm package compromise campaigns using Shai-Hulud malware
- **Extension Marketplace Compromise**: Malicious VS Code extensions with credential stealing capabilities
- **GitHub Actions Manipulation**: Compromised workflow tags redirecting to malicious commits
- **Social Engineering**: Fake Apple security updates distributing macOS infostealers
- **Token Theft**: Stolen GitHub access tokens enabling unauthorized repository access
- **OAuth Consent Bypass**: EvilTokens phishing-as-a-service platform bypassing MFA protections
- **Maintainer Account Compromise**: Direct compromise of package maintainer accounts for malicious updates

## Threat Actor Activities

- **ShinyHunters Gang**: Executed successful breach against 7-Eleven convenience store chain claiming customer data theft
- **EvilTokens PhaaS Operators**: Compromised over 340 Microsoft 365 organizations across five countries within five weeks using OAuth consent bypass techniques
- **Shai-Hulud Campaign Actors**: Deployed over 600 malicious npm packages in coordinated supply chain attacks, with leaked source code enabling copycat campaigns
- **Linux Exploit Developers**: Released public proof-of-concept code for DirtyDecrypt vulnerability increasing exploitation risks
- **VS Code Extension Attackers**: Targeted developers through compromised Nx Console extension containing credential stealing malware
- **GitHub Actions Threat Actors**: Compromised popular GitHub workflow to harvest CI/CD credentials from development environments
- **macOS Infostealer Operators**: Deployed SHub malware variant using AppleScript to mimic legitimate Apple security updates
- **Iranian Cyber Groups**: Expanded offensive operations targeting fuel tank systems and critical infrastructure components