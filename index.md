# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems, with attackers focusing on authentication bypass vulnerabilities, zero-day exploits, and supply chain attacks. Notable active exploitations include a two-year-old Oracle WebLogic Server vulnerability that CISA has flagged for immediate remediation by federal agencies, an Android zero-day being exploited in targeted attacks, and a Palo Alto Networks PAN-OS GlobalProtect authentication bypass vulnerability under active exploitation. Additionally, threat actors are conducting large-scale supply chain attacks targeting npm packages and leveraging AI-driven techniques to accelerate vulnerability weaponization. WordPress sites are experiencing widespread attacks through plugin vulnerabilities, while password managers face sophisticated brute-force campaigns.

## Active Exploitation Details

### Oracle WebLogic Server Vulnerability
- **Description**: A high-severity vulnerability in Oracle WebLogic Server that was patched two years ago but is now being actively exploited
- **Impact**: Allows attackers to compromise WebLogic Server installations
- **Status**: Actively exploited in the wild; CISA has ordered federal agencies to patch immediately

### Android Zero-Day Vulnerability
- **Description**: A zero-day flaw in Android systems being exploited in targeted attacks
- **Impact**: Enables attackers to compromise Android devices in focused campaigns
- **Status**: Actively exploited; patched in June 2026 security update alongside 124 other vulnerabilities

### Palo Alto Networks PAN-OS GlobalProtect Authentication Bypass
- **Description**: Authentication bypass vulnerability in PAN-OS GlobalProtect VPN that allows unauthorized access
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access to VPN services
- **Status**: Under active exploitation in two attack waves starting mid-May; requires specific conditions to exploit

### Windows Netlogon Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw in Windows Netlogon service
- **Impact**: Allows attackers to execute arbitrary code remotely on affected Windows systems
- **Status**: Recently patched but now actively exploited by threat actors

### WP Maps Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in WP Maps Pro WordPress plugin affecting over 15,000 installations
- **Impact**: Enables creation of malicious administrator accounts on affected WordPress sites
- **Status**: Actively exploited to compromise WordPress websites

## Affected Systems and Products

- **Oracle WebLogic Server**: Legacy installations requiring immediate patching per CISA directive
- **Android Devices**: All Android versions prior to June 2026 security update
- **Palo Alto Networks PAN-OS**: GlobalProtect VPN implementations meeting specific exploitation conditions
- **Windows Systems**: Installations with vulnerable Netlogon service components
- **WordPress Sites**: Websites using WP Maps Pro plugin with over 15,000 affected installations
- **Red Hat npm Packages**: Over 30 packages under '@redhat-cloud-services' namespace compromised
- **Steam Community**: Nearly 2,000 WordPress sites infected through Steam profile-based C2 infrastructure
- **Dashlane Users**: Password manager accounts targeted in brute-force campaigns
- **Instagram Accounts**: High-profile accounts including Obama White House and U.S. Space Force compromised

## Attack Vectors and Techniques

- **ClickFix and FakeUpdate Campaigns**: Large-scale malware distribution through compromised websites using social engineering techniques
- **Supply Chain Attacks**: Targeting npm packages with credential-stealing malware variants including Shai-Hulud and Mini Shai-Hulud
- **AI-Driven Exploitation**: Accelerated vulnerability discovery, reproduction, and weaponization processes
- **Steam Profile C2**: Novel command-and-control infrastructure hiding payloads in Steam Community profile comments
- **Brute-Force Authentication**: Sophisticated attacks against password managers and user authentication systems
- **Meta AI Support Bot Manipulation**: Exploitation of AI support systems to seize social media accounts
- **Spear-Phishing with RAT Deployment**: Targeted campaigns delivering remote access trojans to government entities

## Threat Actor Activities

- **DriveSurge**: Operating large-scale malware distribution campaigns using ClickFix and FakeUpdates techniques on thousands of compromised sites
- **SideCopy (Pakistan-aligned)**: Targeting Afghanistan's Ministry of Finance with Xeno RAT through spear-phishing campaigns
- **China-Aligned Groups**: Conducting Operation Dragon Weave targeting Czech Republic and Taiwan officials with AdaptixC2 agent
- **Miasma Campaign Operators**: Compromising Red Hat npm packages with Mini Shai-Hulud credential-stealing worm for supply chain attacks
- **Iranian-Affiliated Actors**: Defacing high-profile Instagram accounts including government and military profiles using AI support bot manipulation
- **Spanish Government Data Doxer**: Individual arrested for leaking sensitive information of key state organization members including INCIBE