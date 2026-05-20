# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitations across multiple platforms and systems. Critical vulnerabilities are being actively exploited in Microsoft Exchange servers through a cross-site scripting vulnerability, Linux kernel systems via local privilege escalation flaws, and ChromaDB AI applications through server hijacking vulnerabilities. Supply chain attacks have emerged as a dominant threat vector with multiple malicious package campaigns targeting npm repositories and compromised development tools. Threat actors are increasingly leveraging legitimate Microsoft services and OAuth authentication mechanisms to bypass security controls, while sophisticated malware operations are targeting both Windows and macOS platforms with advanced stealer variants.

## Active Exploitation Details

### Microsoft Exchange Zero-Day
- **Description**: Cross-site scripting (XSS) vulnerability affecting Microsoft Exchange servers
- **Impact**: Allows attackers to compromise Outlook Web Access (OWA) mailboxes
- **Status**: Currently under active attack with no patch available
- **CVE ID**: CVE-2026-42897

### Linux Kernel Local Privilege Escalation
- **Description**: DirtyDecrypt vulnerability in the Linux kernel allowing local privilege escalation
- **Impact**: Enables attackers to gain elevated privileges on compromised Linux systems
- **Status**: Recently patched with proof-of-concept exploit code now publicly available
- **CVE ID**: CVE-2026-31635

### ChromaDB Server Hijacking
- **Description**: Maximum severity vulnerability in the Python FastAPI version of ChromaDB project
- **Impact**: Allows unauthenticated attackers to execute arbitrary code on exposed servers
- **Status**: Actively exploitable on unpatched systems

### Windows Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities including YellowKey, GreenPlasma, and MiniPlasma
- **Impact**: Various exploitation capabilities affecting Windows systems
- **Status**: Recently disclosed and continuing post-Patch Tuesday exploitation attempts

## Affected Systems and Products

- **Microsoft Exchange**: Servers running vulnerable versions susceptible to XSS attacks
- **Linux Kernel**: Systems vulnerable to DirtyDecrypt local privilege escalation
- **ChromaDB**: AI applications using vulnerable Python FastAPI versions
- **npm Ecosystem**: Over 600 malicious packages targeting Node.js developers
- **Visual Studio Code**: Nx Console extension version 18.95.0 compromised with credential stealer
- **GitHub Actions**: actions-cool/issues-helper workflow compromised for credential harvesting
- **SEPPMail Secure E-Mail Gateway**: Enterprise email security solutions with RCE vulnerabilities
- **Microsoft 365 and Azure**: Production environments targeted through Self-Service Password Reset abuse
- **macOS Systems**: Targeted by SHub Reaper stealer and fake security update campaigns
- **Android Devices**: 455 apps involved in Trapdoor ad fraud scheme affecting 659 million daily bid requests

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Multiple campaigns including Shai-Hulud targeting npm packages and compromised development tools
- **OAuth Consent Abuse**: EvilTokens platform compromising over 340 Microsoft 365 organizations through OAuth consent bypassing MFA
- **Social Engineering**: Fake software installers spoofing legitimate applications (WeChat, Miro, Apple security updates)
- **Malware-Signing-as-a-Service**: Abuse of Microsoft Artifact Signing service to generate fraudulent code-signing certificates
- **Cross-Site Scripting**: Exploitation of XSS vulnerabilities in Microsoft Exchange for mailbox compromise
- **Privilege Escalation**: Local privilege escalation through kernel vulnerabilities
- **Credential Harvesting**: Compromised extensions and workflows stealing CI/CD and development credentials

## Threat Actor Activities

- **ShinyHunters**: Claimed responsibility for 7-Eleven data breach
- **Shai-Hulud Operators**: Conducting large-scale npm package compromise campaigns
- **EvilTokens Platform**: Phishing-as-a-service operation targeting Microsoft 365 organizations
- **SHub Reaper Operators**: Deploying macOS stealers through fake application installers
- **Trapdoor Campaign**: Android ad fraud operation affecting hundreds of applications
- **Microsoft 365 Attackers**: Abusing Self-Service Password Reset for Azure data theft
- **Exchange Exploiters**: Actively targeting Microsoft Exchange zero-day vulnerability