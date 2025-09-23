# Exploitation Report

Critical security vulnerabilities are being actively exploited across multiple platforms, with SolarWinds Web Help Desk facing a severe remote code execution flaw (CVE-2025-26399), while SonicWall SMA100 devices are being targeted with rootkit malware. Threat actors are leveraging sophisticated attack vectors including SEO poisoning campaigns, malicious GitHub repositories, and supply chain attacks targeting npm packages and macOS systems. Notable activities include DPRK-linked hackers deploying BeaverTail malware through ClickFix techniques, Chinese threat actors spreading BadIIS malware via SEO poisoning, and widespread campaigns targeting cryptocurrency and password management applications.

## Active Exploitation Details

### SolarWinds Web Help Desk Remote Code Execution Vulnerability
- **Description**: A critical vulnerability in SolarWinds Web Help Desk software that allows attackers to execute arbitrary commands on susceptible systems without authentication
- **Impact**: Complete system compromise through remote code execution without requiring authentication credentials
- **Status**: Third patch released by SolarWinds; hotfix available for remediation
- **CVE ID**: CVE-2025-26399

### SonicWall SMA100 Rootkit Malware
- **Description**: Active deployment of rootkit malware targeting SonicWall SMA 100 series devices through sophisticated attacks
- **Impact**: Persistent backdoor access and system compromise with deep-level system integration
- **Status**: SonicWall has released firmware update specifically designed to remove the rootkit malware

### Microsoft Entra ID Token Validation Flaw
- **Description**: Critical token validation failure in Microsoft Entra ID allowing impersonation of any user including Global Administrators across any tenant
- **Impact**: Complete administrative access to any Microsoft tenant, enabling data theft and system manipulation
- **Status**: Microsoft has patched the vulnerability

### American Archive of Public Broadcasting Access Control Bypass
- **Description**: Long-standing vulnerability allowing unauthorized downloading of protected and private media content
- **Impact**: Exposure of restricted media content and potential intellectual property theft
- **Status**: Quietly patched this month after years of exposure

## Affected Systems and Products

- **SolarWinds Web Help Desk**: All versions prior to the latest hotfix release
- **SonicWall SMA 100 Series**: Network security appliances targeted with rootkit deployment
- **Microsoft Entra ID**: All tenants using the identity management service
- **AWS Docker Containers**: Misconfigured containers exploited by ShadowV2 botnet
- **npm Ecosystem**: Package repository targeted with supply chain attacks including the malicious 'fezbox' package
- **macOS Systems**: Targeted through fake password managers and GitHub repositories distributing Atomic infostealer
- **Airport Check-in Systems**: European airports affected by ransomware targeting check-in and boarding systems
- **Stellantis Salesforce Platform**: Customer data compromised through third-party service provider breach

## Attack Vectors and Techniques

- **SEO Poisoning**: BadIIS malware campaign using search engine manipulation to redirect traffic and plant web shells
- **Malicious GitHub Repositories**: Fake repositories distributing password manager imposters and other malware to macOS users
- **ClickFix Techniques**: DPRK hackers using deceptive user interaction methods to deliver BeaverTail and InvisibleFerret malware
- **QR Code Obfuscation**: npm package 'fezbox' using QR codes to hide second-stage cookie-stealing payloads
- **Supply Chain Attacks**: Multiple attacks targeting npm ecosystem requiring GitHub to mandate 2FA and access tokens
- **Docker Container Exploitation**: ShadowV2 botnet exploiting misconfigured AWS containers for DDoS-for-hire services
- **EDR Evasion**: New EDR-Freeze tool using Windows Error Reporting system to suspend security software from user mode
- **Ransomware**: European airport disruptions caused by attacks on check-in and boarding systems

## Threat Actor Activities

- **DPRK-linked Groups**: Conducting cryptocurrency job scams using ClickFix techniques to deliver BeaverTail malware and target crypto industry professionals
- **Chinese-speaking Actors**: Operating BadIIS malware campaigns with SEO poisoning to compromise IIS servers and redirect web traffic
- **ComicForm Group**: Previously undocumented threat actor targeting organizations in Belarus, Kazakhstan, and Russia with Formbook malware since April 2025
- **SectorJ149**: Collaborating with ComicForm in Eurasian cyberattacks deploying Formbook malware
- **Nimbus Manticore**: Iran-linked hackers expanding operations to target European organizations with improved malware variants
- **Cryptocurrency Fraud Ring**: European law enforcement dismantled operation responsible for €100 million in losses from over 100 victims
- **ShadowV2 Operators**: Running DDoS-for-hire service through compromised AWS Docker containers