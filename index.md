# Exploitation Report

Critical exploitation activity is currently underway across multiple fronts, with threat actors actively targeting enterprise infrastructure through zero-day vulnerabilities, legacy flaws, and sophisticated social engineering campaigns. The most concerning developments include active exploitation of a newly discovered Android zero-day in targeted attacks, continued abuse of a two-year-old Oracle WebLogic Server vulnerability now added to CISA's Known Exploited Vulnerabilities catalog, and ongoing exploitation of a critical Windows Netlogon remote code execution flaw. Meanwhile, sophisticated threat actors including the Russian-aligned Gamaredon group, Pakistan-linked SideCopy, and China-aligned groups are conducting coordinated campaigns targeting government entities and critical infrastructure across multiple regions.

## Active Exploitation Details

### Android Zero-Day Vulnerability
- **Description**: Google has patched a zero-day flaw in Android that was being exploited in targeted attacks as part of the June 2026 security update
- **Impact**: Attackers can leverage this vulnerability for targeted exploitation against specific Android devices
- **Status**: Patched in June 2026 Android security update; was actively exploited before patching

### Oracle WebLogic Server Authentication Bypass
- **Description**: A high-severity authentication bypass vulnerability in Oracle WebLogic Server that allows unauthorized access
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access to WebLogic Server instances
- **Status**: Patched two years ago but now actively exploited; added to CISA KEV catalog
- **CVE ID**: CVE-2024-21182

### Windows Netlogon Remote Code Execution Flaw
- **Description**: A critical vulnerability in Windows Netlogon service that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected Windows systems
- **Status**: Recently patched but now actively exploited in attacks according to Belgium's cybersecurity authority

### Palo Alto Networks GlobalProtect VPN Authentication Bypass
- **Description**: An authentication bypass vulnerability affecting PAN-OS GlobalProtect VPN that allows unauthorized access under certain conditions
- **Impact**: Attackers can bypass VPN authentication to gain unauthorized network access
- **Status**: Under active exploitation in two attack waves starting mid-May 2026

### WinRAR Vulnerability (Gamaredon Campaign)
- **Description**: A vulnerability in WinRAR file archiver being exploited to deliver malware payloads
- **Impact**: Enables delivery of GammaWorm and GammaSteel malware for data theft and lateral movement
- **Status**: Actively exploited by Russian threat actor Gamaredon targeting Ukrainian entities

## Affected Systems and Products

- **Oracle WebLogic Server**: Enterprise application server infrastructure
- **Android Devices**: Mobile devices running Android operating system
- **Windows Netlogon Service**: Windows domain authentication infrastructure
- **Palo Alto Networks PAN-OS GlobalProtect**: VPN gateway solutions
- **WinRAR**: File compression and archiving software
- **Instagram/Meta Platforms**: Social media accounts compromised through AI support system abuse
- **Red Hat npm Packages**: Over 30 packages in '@redhat-cloud-services' namespace
- **WordPress Websites**: Nearly 2,000 sites infected with malware using Steam profiles for C2
- **Dashlane Password Manager**: Personal subscription plan user accounts

## Attack Vectors and Techniques

- **Spear-Phishing**: Used by SideCopy group targeting Afghanistan's Ministry of Finance with Xeno RAT
- **Supply Chain Attacks**: Miasma campaign compromising Red Hat npm packages with credential-stealing worm
- **AI Support System Abuse**: Attackers convincing Meta's AI support tools to hijack Instagram accounts
- **Malicious File Archives**: Gamaredon delivering malware through compromised WinRAR files
- **Website Compromise**: DriveSurge threat actor hijacking thousands of sites for ClickFix and FakeUpdate attacks
- **Brute-Force Attacks**: Targeting Dashlane password manager accounts and encrypted vault downloads
- **Command and Control via Gaming Platforms**: WordPress malware hiding C2 data in Steam Community profile comments

## Threat Actor Activities

- **Gamaredon (Russian-aligned)**: Continuing WinRAR exploitation campaign to deliver GammaWorm and GammaSteel malware against Ukrainian targets for data theft and network propagation
- **SideCopy (Pakistan-linked)**: Conducting spear-phishing operations against Afghanistan's Ministry of Finance using Xeno RAT for remote access and espionage
- **Operation Dragon Weave (China-aligned)**: Targeting officials and citizens in Czech Republic and Taiwan with AdaptixC2 agent for cyber espionage activities
- **DriveSurge**: Operating large-scale malware distribution campaigns using ClickFix and FakeUpdate techniques on compromised websites
- **Miasma Campaign Operators**: Executing supply chain attacks against Red Hat npm packages to deploy credential-stealing worms on developer systems