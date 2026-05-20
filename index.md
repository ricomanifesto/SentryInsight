# Exploitation Report

The current threat landscape reveals a surge in supply chain attacks targeting developer environments and open-source ecosystems, alongside critical infrastructure vulnerabilities. Notable incidents include GitHub's internal repository breach claimed by TeamPCP affecting approximately 4,000 repositories, a maximum severity vulnerability in ChromaDB for AI applications allowing server hijacking, and multiple compromised development tools including the Nx Console VS Code extension and GitHub Actions workflows. Additionally, Windows systems face continued zero-day exploitation with new vulnerabilities YellowKey, GreenPlasma, and MiniPlasma following recent Patch Tuesday updates, while Linux kernel vulnerabilities are being actively targeted with proof-of-concept exploits.

## Active Exploitation Details

### ChromaDB Server Hijacking Vulnerability
- **Description**: A maximum severity vulnerability in the latest Python FastAPI version of ChromaDB that allows unauthenticated attackers to run arbitrary code on exposed servers
- **Impact**: Complete server compromise and arbitrary code execution without authentication
- **Status**: Recently disclosed, patch status unclear

### DirtyDecrypt Linux Kernel Vulnerability
- **Description**: A local privilege escalation vulnerability in the Linux kernel that has been recently patched
- **Impact**: Allows attackers to escalate privileges on compromised Linux systems
- **Status**: Patched but proof-of-concept exploit code has been released
- **CVE ID**: CVE-2026-31635

### Windows Zero-Day Vulnerabilities
- **Description**: Multiple Windows zero-day vulnerabilities discovered and disclosed by security researchers
- **Impact**: Various impacts including potential system compromise and privilege escalation
- **Status**: Actively exploited zero-day vulnerabilities disclosed after recent Patch Tuesday

### SEPPMail Secure E-Mail Gateway Vulnerabilities
- **Description**: Critical security vulnerabilities in SEPPMail Secure E-Mail Gateway enterprise email security solution
- **Impact**: Remote code execution and unauthorized access to mail traffic
- **Status**: Critical vulnerabilities recently disclosed

## Affected Systems and Products

- **GitHub Platform**: Internal repositories and infrastructure compromised with approximately 4,000 repositories affected
- **ChromaDB**: Latest Python FastAPI version vulnerable to unauthenticated remote code execution
- **Linux Kernel**: Systems running vulnerable kernel versions susceptible to local privilege escalation
- **Windows Operating System**: Multiple versions affected by newly disclosed zero-day vulnerabilities
- **VS Code Marketplace**: Nx Console extension version 18.95.0 compromised with credential stealer
- **npm Package Registry**: Over 600 malicious packages published in Shai-Hulud supply chain campaign
- **GitHub Actions**: Popular actions-cool/issues-helper workflow compromised
- **SEPPMail Secure E-Mail Gateway**: Enterprise email security solutions vulnerable to RCE
- **Microsoft 365 and Azure**: Production environments targeted through Self-Service Password Reset abuse
- **7-Eleven Systems**: Corporate systems breached by ShinyHunters group

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromised development tools, npm packages, VS Code extensions, and GitHub Actions workflows
- **Repository Compromise**: Direct access to internal code repositories and development infrastructure
- **Unauthenticated Remote Code Execution**: Exploitation of web application vulnerabilities in AI/ML platforms
- **Social Engineering**: OAuth consent phishing bypassing multi-factor authentication through EvilTokens PhaaS platform
- **Privilege Escalation**: Local privilege escalation through kernel vulnerabilities with available proof-of-concept exploits
- **Malware-as-a-Service**: Abuse of Microsoft's Artifact Signing service for fraudulent code-signing certificates
- **Credential Harvesting**: Targeting of CI/CD pipelines and development environments for sensitive credentials
- **Ad Fraud Operations**: Trapdoor Android malware scheme affecting 659 million daily bid requests across 455 apps

## Threat Actor Activities

- **TeamPCP**: Claimed breach of GitHub's internal repositories affecting approximately 4,000 repositories, listed platform's source code and internal organization data
- **ShinyHunters**: Successfully breached 7-Eleven's corporate systems in confirmed cyberattack
- **EvilTokens Operators**: Launched phishing-as-a-service platform compromising over 340 Microsoft 365 organizations across five countries within five weeks
- **Shai-Hulud Campaign**: Published over 600 malicious npm packages in coordinated supply chain attack
- **Microsoft 365 Threat Actors**: Actively abusing Self-Service Password Reset functionality and legitimate administration features for data theft in Azure environments
- **Trapdoor Operators**: Conducting large-scale Android ad fraud operations through HUMAN's Satori Threat Intelligence detection
- **Nx Console Attackers**: Compromised popular VS Code extension to steal developer credentials
- **GitHub Actions Compromisers**: Redirected popular workflow tags to malicious commits for CI/CD credential harvesting