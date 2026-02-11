# Exploitation Report

Microsoft's February 2026 Patch Tuesday addressed six actively exploited zero-day vulnerabilities, representing the most critical exploitation activity currently observed. These zero-days include three security feature bypass flaws that enable attackers to circumvent built-in protections across multiple Microsoft products. Additionally, threat actors are exploiting unpatched SmarterMail instances to deploy Warlock ransomware, while Dutch authorities confirmed exploitation of Ivanti zero-day vulnerabilities that exposed employee contact data. Critical exploitation activity is also occurring against Fortinet FortiClientEMS through SQL injection attacks enabling unauthenticated code execution.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities in Microsoft Windows and related software, with three specifically identified as security feature bypass flaws
- **Impact**: Attackers can bypass built-in security protections and gain elevated access across multiple Microsoft products
- **Status**: Actively exploited in the wild; patches released in February 2026 Patch Tuesday updates

### Fortinet FortiClientEMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in FortiClientEMS enabling remote code execution
- **Impact**: Unauthenticated attackers can execute arbitrary code on vulnerable systems
- **Status**: Critical patches released by Fortinet
- **CVE ID**: CVE-2026-[number referenced but not fully provided in source]

### SmarterMail Server Vulnerabilities
- **Description**: Unpatched vulnerabilities in SmarterMail server software exploited by ransomware groups
- **Impact**: Complete system compromise leading to ransomware deployment
- **Status**: Actively exploited by Warlock ransomware gang

### Ivanti Zero-Day Vulnerabilities
- **Description**: Zero-day vulnerabilities in Ivanti systems affecting government organizations
- **Impact**: Exposure of employee contact data and potential system compromise
- **Status**: Confirmed exploitation by Dutch authorities; ongoing investigation

## Affected Systems and Products

- **Microsoft Windows**: All supported versions affected by zero-day vulnerabilities
- **Microsoft 365**: Various components impacted by security feature bypass flaws
- **Fortinet FortiClientEMS**: Critical SQL injection vulnerability enabling code execution
- **SmarterMail Server**: Multiple versions vulnerable to exploitation by ransomware groups
- **Ivanti Systems**: Government installations compromised through zero-day exploitation
- **Linux Systems**: SSHStalker botnet targeting Linux servers and IoT devices
- **macOS and Windows**: North Korean malware campaigns targeting cryptocurrency sector
- **Android and iOS Devices**: ZeroDayRAT spyware providing complete device access
- **7-Zip Installation**: Fake websites distributing trojanized installers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities actively exploited before patches became available
- **SQL Injection**: Critical unauthenticated code execution through FortiClientEMS vulnerabilities
- **Ransomware Deployment**: Warlock gang leveraging unpatched SmarterMail instances for initial access
- **Social Engineering**: North Korean groups using AI-generated video and ClickFix techniques
- **Supply Chain Attacks**: Fake software distribution sites delivering trojanized installers
- **IRC Command and Control**: SSHStalker botnet using traditional IRC protocols for stealth
- **BYOVD Techniques**: Reynolds ransomware embedding vulnerable drivers to disable EDR tools
- **Mobile Spyware**: ZeroDayRAT providing full remote access to mobile devices
- **Cloud Infrastructure Compromise**: TeamPCP conducting automated worm-like attacks on exposed cloud services

## Threat Actor Activities

- **Warlock Ransomware Gang (Storm-2603)**: Successfully breached SmarterTools through unpatched SmarterMail vulnerabilities in January 2026
- **North Korean Operatives**: Conducting sophisticated campaigns targeting cryptocurrency sector using AI-generated content and fake LinkedIn profiles for company infiltration
- **Chinese Threat Actor UNC3886**: Breached all four major Singapore telecommunications providers (Singtel, StarHub, M1, and Simba) in 2025
- **SSHStalker Operators**: Deploying new Linux botnet using IRC for command and control operations
- **Reynolds Ransomware Group**: Utilizing BYOVD techniques to disable endpoint security solutions
- **TeamPCP**: Compromising cloud infrastructure at scale through automated attacks on exposed services
- **DPRK IT Workers**: Impersonating legitimate professionals on LinkedIn to secure remote positions and infiltrate organizations
- **ZeroDayRAT Operators**: Marketing commercial spyware platform on Telegram for mobile device compromise