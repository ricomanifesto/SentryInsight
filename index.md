# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in widespread attacks across multiple platforms. The YellowKey BitLocker bypass vulnerability (CVE-2026-45585) represents a significant Windows zero-day that allows attackers to bypass BitLocker encryption and gain access to protected drives. Simultaneously, privilege escalation vulnerabilities in Linux systems are being actively targeted, with PinTheft affecting Arch Linux systems and DirtyDecrypt (CVE-2026-31635) impacting the Linux kernel. The threat landscape is further complicated by supply chain attacks through malicious VS Code extensions leading to major repository breaches at GitHub and Grafana, alongside a massive npm package poisoning campaign compromising over 600 packages in the Shai-Hulud operation. A maximum severity vulnerability in ChromaDB for AI applications is also enabling server hijacking attacks, while Azure environments face sophisticated attacks abusing legitimate Microsoft services.

## Active Exploitation Details

### YellowKey BitLocker Bypass
- **Description**: A zero-day vulnerability in Windows BitLocker that allows unauthorized access to encrypted drives by bypassing BitLocker protection mechanisms
- **Impact**: Attackers can gain access to encrypted data on protected drives, potentially exposing sensitive information stored on BitLocker-protected systems
- **Status**: Microsoft has released mitigations following public disclosure, but the vulnerability remains a critical concern
- **CVE ID**: CVE-2026-45585

### PinTheft Linux Privilege Escalation
- **Description**: A recently patched Linux privilege escalation vulnerability specifically affecting Arch Linux systems
- **Impact**: Local attackers can exploit this flaw to gain root privileges on vulnerable Arch Linux systems
- **Status**: Publicly available proof-of-concept exploit code has been released, increasing exploitation risk despite patches being available

### DirtyDecrypt Linux Kernel Vulnerability
- **Description**: A local privilege escalation vulnerability in the Linux kernel that allows attackers to elevate their privileges
- **Impact**: Successful exploitation enables local privilege escalation, potentially giving attackers full system control
- **Status**: Proof-of-concept exploit code has been publicly released following recent patching
- **CVE ID**: CVE-2026-31635

### ChromaDB Maximum Severity Vulnerability
- **Description**: A critical vulnerability in the Python FastAPI version of ChromaDB affecting AI applications
- **Impact**: Unauthenticated attackers can execute arbitrary code on exposed ChromaDB servers, leading to complete server compromise
- **Status**: Maximum severity rating indicates critical exploitation risk for AI applications using ChromaDB

### Drupal Critical Security Vulnerability
- **Description**: A critical vulnerability in Drupal core with high exploitation risk requiring immediate patching
- **Impact**: Threat actors may develop working exploits within hours of update disclosure, posing immediate risk to Drupal installations
- **Status**: Critical security release issued with urgent patching recommendations due to rapid exploit development potential

## Affected Systems and Products

- **Windows Systems**: BitLocker-protected drives vulnerable to YellowKey bypass attacks
- **Arch Linux**: Systems affected by PinTheft privilege escalation vulnerability
- **Linux Kernel**: Broad range of Linux distributions affected by DirtyDecrypt vulnerability
- **ChromaDB Servers**: AI applications using Python FastAPI version exposed to arbitrary code execution
- **Drupal Installations**: Core Drupal systems requiring immediate security updates
- **GitHub Repositories**: Approximately 3,800 internal repositories compromised through malicious VS Code extension
- **Grafana Systems**: Source code exposed through TanStack npm attack vector
- **npm Ecosystem**: Over 600 malicious packages deployed in Shai-Hulud supply chain attack
- **Microsoft 365/Azure**: Production environments targeted through Self-Service Password Reset abuse

## Attack Vectors and Techniques

- **Malicious Browser Extensions**: VS Code extensions used to compromise developer environments and access internal repositories
- **Supply Chain Poisoning**: Mass publication of malicious npm packages to compromise downstream applications and systems
- **Legitimate Service Abuse**: Microsoft Self-Service Password Reset and other administrative features weaponized for data theft
- **Social Engineering**: SHub Reaper stealer using fake WeChat and Miro installers to target macOS systems
- **Code Signing Abuse**: Malware-signing-as-a-service operations exploiting Microsoft's Artifact Signing service for fraudulent certificates
- **AI-Generated Domains**: Typosquatting campaigns using AI-generated lookalike domains embedded in third-party scripts
- **Ad Fraud Networks**: Trapdoor operation targeting Android devices through 455 malicious apps generating fraudulent ad revenue

## Threat Actor Activities

- **TeamPCP**: Claimed responsibility for GitHub breach affecting approximately 4,000 internal repositories through employee device compromise
- **ShinyHunters**: Confirmed breach of 7-Eleven systems in extortion campaign targeting major retail infrastructure
- **Shai-Hulud Operators**: Conducted large-scale npm supply chain attack compromising over 600 packages in coordinated campaign
- **Azure-Targeting Groups**: Sophisticated threat actors abusing legitimate Microsoft services for data theft in production environments
- **Android Fraud Networks**: Trapdoor operators running ad fraud scheme affecting 659 million daily bid requests across 455 malicious applications
- **Ransomware Affiliates**: Leveraging malware-signing-as-a-service operations to distribute signed malware through compromised Microsoft platforms