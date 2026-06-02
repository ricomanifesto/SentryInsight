# Exploitation Report

Current exploitation activity reveals several critical vulnerabilities being actively targeted by threat actors across multiple platforms and systems. Notable active exploitation includes a Palo Alto Networks GlobalProtect VPN authentication bypass vulnerability, a critical Windows Netlogon remote code execution flaw, and a WordPress plugin vulnerability allowing unauthorized administrator account creation. Additionally, large-scale supply chain attacks have compromised Red Hat npm packages and targeted OpenAI Codex users, while sophisticated malware campaigns are leveraging compromised websites and innovative attack vectors including AI-powered social engineering and Steam profile-based command and control infrastructure.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A medium-severity authentication bypass vulnerability affecting Palo Alto Networks PAN-OS and Prisma Access systems
- **Impact**: Allows attackers to bypass authentication mechanisms and potentially breach corporate networks
- **Status**: Under active exploitation in two attack waves starting in mid-May 2026
- **CVE ID**: CVE-2026-0257

### Windows Netlogon Remote Code Execution
- **Description**: A critical vulnerability in Windows Netlogon service that allows remote code execution
- **Impact**: Enables attackers to execute arbitrary code remotely on vulnerable Windows systems
- **Status**: Recently patched but now being actively exploited by threat actors

### WP Maps Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the WP Maps Pro WordPress plugin affecting over 15,000 installations
- **Impact**: Allows creation of malicious administrator accounts without authentication
- **Status**: Actively exploited to compromise WordPress websites

### CIFSwitch Linux Privilege Escalation
- **Description**: Local privilege escalation vulnerability in the Linux kernel affecting multiple distributions
- **Impact**: Allows attackers to forge CIFS authentication key descriptions and abuse kernel key request mechanisms to gain root access
- **Status**: Newly discovered vulnerability affecting multiple Linux distributions

## Affected Systems and Products

- **Palo Alto Networks**: PAN-OS and Prisma Access systems with GlobalProtect VPN functionality
- **Microsoft Windows**: Systems running vulnerable Netlogon service components
- **WordPress Sites**: Websites using WP Maps Pro plugin (over 15,000 affected installations)
- **Linux Systems**: Multiple distributions vulnerable to CIFSwitch kernel flaw
- **Red Hat npm Packages**: Over 30 packages under '@redhat-cloud-services' namespace compromised
- **OpenAI Codex Users**: Developers targeted through malicious codexui-android npm package
- **Dashlane Users**: Password manager accounts targeted by brute-force attacks
- **Instagram Accounts**: High-profile accounts including Obama White House and U.S. Space Force compromised
- **WordPress Websites**: Nearly 2,000 sites infected with Steam-based malware

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of PAN-OS GlobalProtect to circumvent security controls
- **Supply Chain Attacks**: Compromise of legitimate npm packages to distribute credential-stealing malware
- **Social Engineering**: AI-powered manipulation of Meta's support systems to hijack accounts
- **Malware Distribution**: ClickFix and FakeUpdate techniques on compromised websites
- **Command and Control**: Novel use of Steam Community profiles to hide C2 communications
- **Brute Force Attacks**: Automated credential attacks against password management platforms
- **ChatGPT Abuse**: Exploitation of content-sharing features to host fake outage pages

## Threat Actor Activities

- **DriveSurge**: Operating large-scale malware distribution campaigns using compromised websites for ClickFix and FakeUpdate attacks
- **Miasma Campaign**: Supply chain attack targeting Red Hat npm packages with Shai-Hulud credential-stealing malware
- **Dragon Weave Operation**: China-aligned cyber espionage campaign targeting Czech Republic and Taiwan officials with AdaptixC2 agents
- **WordPress Malware Operators**: Sophisticated campaign infecting nearly 2,000 WordPress sites with Steam-based C2 infrastructure
- **Instagram Account Hijackers**: Threat actors exploiting Meta's AI support systems to compromise high-profile accounts with pro-Iranian messaging