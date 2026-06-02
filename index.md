# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms and products, creating urgent security risks for organizations worldwide. The most severe threats include a Windows Netlogon remote code execution vulnerability, an Android zero-day flaw, and authentication bypass issues in Palo Alto Networks GlobalProtect VPN systems. Additional concerns involve a WordPress plugin vulnerability being exploited to create administrator accounts, and a two-year-old Oracle WebLogic Server flaw that CISA has flagged for government remediation due to active exploitation. Supply chain attacks are also escalating, with compromised npm packages targeting Red Hat services and OpenAI Codex users.

## Active Exploitation Details

### Windows Netlogon Remote Code Execution Vulnerability
- **Description**: A critical vulnerability affecting Windows Netlogon service that allows remote code execution
- **Impact**: Threat actors can execute arbitrary code remotely on affected Windows systems
- **Status**: Recently patched but now being actively exploited by threat actors

### Android Zero-Day Vulnerability
- **Description**: A zero-day flaw in Android systems being exploited in targeted attacks
- **Impact**: Allows attackers to exploit Android devices in focused campaigns
- **Status**: Patched in June 2026 Android security updates addressing 124 total vulnerabilities

### Palo Alto Networks GlobalProtect VPN Authentication Bypass
- **Description**: An authentication bypass vulnerability in PAN-OS GlobalProtect VPN systems
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access
- **Status**: Under active exploitation in two attack waves beginning in mid-May, requires specific conditions

### WP Maps Pro WordPress Plugin Critical Flaw
- **Description**: A critical security vulnerability in the WP Maps Pro WordPress plugin
- **Impact**: Allows threat actors to create malicious administrator accounts on affected WordPress sites
- **Status**: Actively being exploited to compromise WordPress installations

### Oracle WebLogic Server Vulnerability
- **Description**: A high-severity vulnerability in Oracle WebLogic Server that was patched two years ago
- **Impact**: Enables attackers to compromise WebLogic Server installations
- **Status**: CISA has ordered federal agencies to patch due to confirmed active exploitation

## Affected Systems and Products

- **Android Devices**: All Android systems vulnerable to the patched zero-day flaw
- **Windows Systems**: Windows installations with Netlogon service exposed to the critical RCE vulnerability
- **Palo Alto Networks**: PAN-OS GlobalProtect VPN systems susceptible to authentication bypass
- **WordPress Sites**: Installations using WP Maps Pro plugin (over 15,000 sales on Envato Market)
- **Oracle WebLogic**: WebLogic Server installations still unpatched from two-year-old vulnerability
- **Red Hat npm Packages**: Over 30 packages under '@redhat-cloud-services' namespace compromised
- **Steam Community**: WordPress malware campaign using Steam profiles for C2 infrastructure
- **Meta AI Support**: Instagram accounts compromised through AI support bot manipulation

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Miasma campaign compromising Red Hat npm packages with Shai-Hulud credential-stealing malware
- **Social Engineering**: Exploitation of Meta's AI support bot to seize Instagram accounts including Obama White House and U.S. Space Force accounts
- **Brute Force Attacks**: Targeted attacks against Dashlane password manager users with encrypted vault downloads
- **Spear Phishing**: SideCopy group targeting Afghanistan's Ministry of Finance with Xeno RAT
- **ClickFix and FakeUpdate**: DriveSurge threat actor operating large-scale malware distribution on compromised websites
- **WordPress Malware**: Campaign infecting nearly 2,000 sites using Steam Community profiles to hide C2 data
- **npm Package Compromise**: codexui-android package targeting OpenAI Codex authentication tokens

## Threat Actor Activities

- **SideCopy**: Pakistan-aligned group conducting spear-phishing campaigns against Afghanistan's Ministry of Finance using open-source remote access tools
- **DriveSurge**: Threat actor conducting large-scale malware distribution through compromised websites using ClickFix and FakeUpdates techniques
- **Dragon Weave Operation**: China-aligned groups targeting Czech Republic and Taiwan officials with AdaptixC2 agent delivery
- **Supply Chain Attackers**: Multiple threat actors targeting developer environments through compromised npm packages and malicious tools
- **WordPress Attackers**: Threat actors actively exploiting WP Maps Pro vulnerability to create unauthorized administrator accounts on WordPress installations