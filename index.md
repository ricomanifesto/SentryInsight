# Exploitation Report

The current threat landscape reveals a surge in critical zero-day exploitation activity, with Microsoft addressing six actively exploited zero-day vulnerabilities in February 2026 alone. Three of these zero-days are security feature bypass flaws that allow attackers to circumvent built-in protections across multiple Microsoft products. The exploitation activity spans across various platforms, with significant threats targeting SolarWinds Web Help Desk instances exposed to the public internet, critical SQL injection vulnerabilities in Fortinet's FortiClientEMS enabling unauthenticated code execution, and sophisticated mobile malware platforms like ZeroDayRAT providing complete device access. Nation-state actors, particularly from North Korea and China, continue to leverage advanced techniques including AI-generated content for social engineering and strategic infiltration of major telecommunications infrastructure.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities in Microsoft Windows operating systems and other software, with three identified as security feature bypass flaws
- **Impact**: Attackers can bypass built-in security protections across multiple Microsoft products, potentially gaining elevated privileges and system access
- **Status**: Actively exploited in the wild, patches released in February 2026 Patch Tuesday updates

### Fortinet FortiClientEMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in FortiClientEMS that enables unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable systems without authentication
- **Status**: Critical vulnerability patched by Fortinet
- **CVE ID**: CVE-2024-47575

### Ivanti Zero-Day Vulnerability
- **Description**: Zero-day exploit targeting Ivanti systems used by Dutch government agencies
- **Impact**: Employee contact data exposure and potential system compromise
- **Status**: Actively exploited, affected Dutch Data Protection Authority and Council for the Judiciary

### SmarterMail Server Vulnerability
- **Description**: Unpatched vulnerability in SmarterMail server instances
- **Impact**: Complete network compromise leading to ransomware deployment
- **Status**: Exploited by Warlock ransomware gang in January 2026

## Affected Systems and Products

- **Microsoft Windows Operating Systems**: All versions affected by six zero-day vulnerabilities, with patches available through February 2026 Patch Tuesday
- **Microsoft 365**: Admin center outages affecting business and enterprise subscriptions in North America
- **Fortinet FortiClientEMS**: Critical SQL injection vulnerability requiring immediate patching
- **SolarWinds Web Help Desk**: Instances exposed to public internet targeted by attackers
- **Ivanti Systems**: Government deployments compromised through zero-day exploitation
- **SmarterMail Servers**: Unpatched instances vulnerable to ransomware attacks
- **Android and iOS Devices**: Targeted by ZeroDayRAT commercial spyware platform
- **Linux Systems**: Compromised by SSHStalker botnet using IRC for command and control
- **Singapore Telecommunications**: Four largest providers (Singtel, StarHub, M1, Simba) breached by Chinese threat actors

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Microsoft products and Ivanti systems
- **SQL Injection Attacks**: Critical unauthenticated code execution through FortiClientEMS vulnerabilities
- **Bring Your Own Vulnerable Driver (BYOVD)**: Reynolds ransomware embeds vulnerable drivers to disable EDR security tools
- **Social Engineering with AI**: North Korean actors using AI-generated video content and ClickFix techniques for malware delivery
- **LinkedIn Impersonation**: DPRK operatives impersonating real professionals using hijacked LinkedIn accounts for remote job applications
- **IRC Command and Control**: SSHStalker botnet utilizing Internet Relay Chat for C2 communications
- **Malicious Software Distribution**: Fake 7-Zip websites distributing trojanized installers with proxy tools
- **Living-off-the-Plant Techniques**: Advanced OT attacks using legitimate plant systems and tools for malicious purposes

## Threat Actor Activities

- **North Korean Hackers**: Conducting tailored cryptocurrency theft campaigns using new macOS malware, AI-generated content, and sophisticated social engineering techniques targeting the crypto sector
- **Chinese APT Groups (UNC3886)**: Successfully breached Singapore's four largest telecommunications providers, demonstrating advanced persistent threat capabilities
- **DPRK IT Workers**: Infiltrating companies through LinkedIn account impersonation, applying for remote positions using real professional identities
- **Warlock Ransomware Gang (Storm-2603)**: Exploited unpatched SmarterMail servers to breach SmarterTools network infrastructure
- **ZeroDayRAT Operators**: Commercializing advanced mobile spyware platform on Telegram, providing full remote control capabilities for Android and iOS devices
- **Reynolds Ransomware Group**: Deploying sophisticated ransomware with embedded BYOVD components to evade endpoint detection and response tools
- **SSHStalker Botnet Operators**: Building Linux-based botnet infrastructure using traditional IRC protocols for command and control operations