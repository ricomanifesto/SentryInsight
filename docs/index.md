# Exploitation Report

Critical zero-day vulnerabilities and supply chain attacks are dominating the current threat landscape. Microsoft's BitLocker bypass vulnerability CVE-2026-45585 (YellowKey) represents a significant zero-day threat affecting Windows systems, while multiple high-impact breaches have compromised major technology platforms including GitHub's internal repositories and npm package infrastructure. The emergence of sophisticated attack vectors targeting AI applications, OAuth consent mechanisms, and Linux kernel vulnerabilities demonstrates the expanding attack surface facing organizations. Threat actors are increasingly leveraging legitimate services and trusted platforms to conduct malicious activities, with particular focus on supply chain compromises and privilege escalation attacks.

## Active Exploitation Details

### YellowKey BitLocker Bypass Vulnerability
- **Description**: A zero-day vulnerability in Windows BitLocker that allows unauthorized access to protected drives
- **Impact**: Attackers can bypass BitLocker encryption and gain access to encrypted data on protected systems
- **Status**: Microsoft has released mitigations following public disclosure, but this remains an active zero-day threat
- **CVE ID**: CVE-2026-45585

### DirtyDecrypt Linux Kernel Vulnerability
- **Description**: A local privilege escalation vulnerability in the Linux kernel with publicly available proof-of-concept exploit code
- **Impact**: Local attackers can escalate privileges to gain root access on affected Linux systems
- **Status**: Recently patched with PoC exploit code now publicly available
- **CVE ID**: CVE-2026-31635

### ChromaDB FastAPI Server Vulnerability
- **Description**: A maximum severity vulnerability in the Python FastAPI version of ChromaDB project affecting AI applications
- **Impact**: Unauthenticated attackers can execute arbitrary code on exposed ChromaDB servers
- **Status**: Critical vulnerability affecting AI infrastructure components

### Microsoft Self-Service Password Reset Abuse
- **Description**: Legitimate Microsoft 365 and Azure administration features being exploited for unauthorized data access
- **Impact**: Threat actors can steal data from production environments by abusing legitimate password reset functionality
- **Status**: Active attacks targeting Microsoft cloud environments

## Affected Systems and Products

- **Windows Systems**: BitLocker-enabled systems vulnerable to YellowKey bypass attacks
- **Linux Kernel**: Systems running vulnerable kernel versions affected by DirtyDecrypt privilege escalation
- **ChromaDB AI Applications**: Python FastAPI implementations vulnerable to remote code execution
- **GitHub Platform**: Internal repositories compromised affecting approximately 3,800 repositories
- **npm Package Registry**: Over 600 malicious packages published in Shai-Hulud supply chain campaign
- **Microsoft 365/Azure**: Production environments targeted through legitimate admin feature abuse
- **7-Eleven Systems**: Corporate infrastructure compromised in data breach
- **Grafana Labs**: Source code exposed through TanStack npm attack vector
- **Android Applications**: 455 apps compromised in Trapdoor ad fraud scheme affecting 659 million daily requests
- **Drupal Core**: All supported branches requiring urgent security updates scheduled for May 20, 2026

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious VS Code extensions targeting developer environments and npm package poisoning campaigns
- **OAuth Consent Abuse**: EvilTokens phishing-as-a-service platform bypassing MFA through OAuth consent mechanisms
- **Malicious Code Signing**: Abuse of Microsoft Artifact Signing service to generate fraudulent certificates for malware
- **Social Engineering**: SHub Reaper stealer using fake WeChat and Miro installers to backdoor macOS systems
- **Ad Fraud Networks**: Trapdoor operation leveraging Android applications for malvertising and fraud activities
- **Legitimate Service Abuse**: Exploitation of Microsoft password reset features and other admin functions
- **Zero-Day Exploitation**: Active use of unpublished vulnerabilities before patches are available

## Threat Actor Activities

- **TeamPCP**: Conducted breach of GitHub's internal repositories, claiming access to approximately 4,000 repositories and exfiltrating source code
- **ShinyHunters**: Extortion group responsible for 7-Eleven data breach, continuing operations against retail infrastructure
- **EvilTokens Operators**: Phishing-as-a-service platform compromising over 340 Microsoft 365 organizations across five countries within five weeks
- **Shai-Hulud Campaign**: Supply chain attackers publishing over 600 malicious npm packages in coordinated infrastructure compromise
- **Microsoft 365 Threat Actor**: Unidentified group targeting Azure and Microsoft 365 environments through abuse of legitimate administration features
- **Trapdoor Operators**: Android-focused threat actors running large-scale ad fraud operation affecting hundreds of applications
- **Malware Signing Service**: Cybercrime-as-a-service operation abusing Microsoft's legitimate code signing infrastructure