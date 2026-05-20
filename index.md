# Exploitation Report

Critical cybersecurity threats are actively targeting enterprise infrastructure through multiple attack vectors, with several zero-day vulnerabilities and sophisticated exploitation campaigns emerging. A Microsoft Exchange zero-day vulnerability (CVE-2026-42897) is currently under active attack with no available patch, while a Linux kernel privilege escalation flaw (CVE-2026-31635) has proof-of-concept exploit code publicly released. Supply chain attacks have intensified through compromised npm packages and VS Code extensions, affecting developer environments globally. Additionally, enterprise AI applications face maximum severity vulnerabilities in ChromaDB, and threat actors are exploiting legitimate Microsoft services for credential theft and malware distribution.

## Active Exploitation Details

### Microsoft Exchange Zero-Day
- **Description**: Cross-site scripting (XSS) vulnerability in Microsoft Exchange that allows attackers to compromise Outlook Web Access (OWA) mailboxes
- **Impact**: Attackers can gain unauthorized access to enterprise email systems and potentially escalate privileges within Exchange environments
- **Status**: Currently under active attack with no patch available
- **CVE ID**: CVE-2026-42897

### Linux Kernel Local Privilege Escalation
- **Description**: A security flaw in the Linux kernel dubbed "DirtyDecrypt" that enables local privilege escalation attacks
- **Impact**: Local attackers can escalate privileges to gain root access on affected Linux systems
- **Status**: Patched but proof-of-concept exploit code has been publicly released
- **CVE ID**: CVE-2026-31635

### ChromaDB Maximum Severity Vulnerability
- **Description**: Critical vulnerability in the latest Python FastAPI version of the ChromaDB project affecting AI applications
- **Impact**: Unauthenticated attackers can execute arbitrary code on exposed ChromaDB servers, potentially compromising AI infrastructure
- **Status**: Maximum severity rating, actively exploitable on exposed systems

### Windows Zero-Day Vulnerabilities
- **Description**: Multiple new zero-day vulnerabilities identified as YellowKey, GreenPlasma, and MiniPlasma
- **Impact**: Various attack vectors enabling system compromise and privilege escalation on Windows systems
- **Status**: Recently disclosed, part of ongoing vulnerability disclosure campaign

## Affected Systems and Products

- **Microsoft Exchange**: Outlook Web Access (OWA) components vulnerable to XSS attacks
- **Linux Kernel**: Multiple distributions affected by privilege escalation vulnerability
- **ChromaDB**: Python FastAPI implementations in AI application environments
- **Windows Systems**: Multiple versions affected by newly disclosed zero-day vulnerabilities
- **npm Ecosystem**: Over 600 malicious packages targeting Node.js developers
- **VS Code Extensions**: Nx Console extension compromised to steal developer credentials
- **GitHub Actions**: actions-cool/issues-helper workflow compromised for CI/CD credential theft
- **Microsoft 365**: Production environments targeted through Self-Service Password Reset abuse
- **SEPPMail Secure E-Mail Gateway**: Enterprise email security solutions vulnerable to RCE
- **macOS Systems**: Targeted by SHub infostealer variants spoofing Apple security updates

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Microsoft Exchange vulnerability enabling mailbox compromise
- **Supply Chain Attacks**: Compromised npm packages and VS Code extensions targeting developers
- **Social Engineering**: Fake Apple security updates and WeChat/Miro installers distributing malware
- **Legitimate Service Abuse**: Microsoft Self-Service Password Reset exploited for data theft
- **Phishing-as-a-Service**: EvilTokens platform bypassing MFA through OAuth consent manipulation
- **AppleScript Exploitation**: macOS backdoors installed through fake security update prompts
- **Code Signing Abuse**: Malware-signing-as-a-service operations using fraudulent Microsoft certificates
- **Ad Fraud Schemes**: Trapdoor operation generating 659 million daily fraudulent bid requests

## Threat Actor Activities

- **ShinyHunters Gang**: Claimed responsibility for 7-Eleven data breach, continuing extortion operations
- **EvilTokens Platform**: Compromised over 340 Microsoft 365 organizations across five countries within five weeks
- **Shai-Hulud Campaign**: Published 600+ malicious npm packages in coordinated supply chain attack
- **Mini Shai-Hulud**: Targeted @antv ecosystem through compromised maintainer accounts
- **Trapdoor Operators**: Conducted large-scale Android ad fraud using 455 compromised applications
- **SHub Reaper**: Advanced macOS stealer shifting from ClickFix to AppleScript-based execution
- **Microsoft Certificate Abusers**: Malware-signing-as-a-service operation disrupted by Microsoft
- **Exchange Attackers**: Actively exploiting zero-day vulnerability for enterprise email compromise