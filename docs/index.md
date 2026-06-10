# Exploitation Report

The cybersecurity landscape is currently experiencing intense exploitation activity, highlighted by Microsoft's record-breaking June 2026 Patch Tuesday addressing nearly 200 vulnerabilities, including three actively exploited zero-days. Critical threats include the Chrome V8 zero-day CVE-2026-11645 being exploited in the wild, multiple Microsoft Defender zero-days (YellowKey, GreenPlasma, MiniPlasma, and RoguePlanet) enabling SYSTEM privilege escalation, and ongoing exploitation of older vulnerabilities like the WinRAR flaw CVE-2025-8088 by Russian threat actors targeting Ukrainian organizations. Additional significant concerns include ServiceNow API exploitation allowing unauthorized customer data access, critical Ivanti Sentry vulnerabilities enabling root code execution, and a new Veeam Backup & Replication RCE flaw.

## Active Exploitation Details

### Chrome V8 Zero-Day
- **Description**: High-severity vulnerability in Google Chrome's V8 JavaScript engine
- **Impact**: Active exploitation in the wild allowing attackers to compromise Chrome browsers
- **Status**: Patched by Google in latest Chrome security update addressing 74 vulnerabilities
- **CVE ID**: CVE-2026-11645

### Microsoft Defender YellowKey Zero-Day
- **Description**: Zero-day vulnerability in Microsoft Defender allowing privilege escalation
- **Impact**: Enables attackers to gain SYSTEM privileges on fully patched Windows systems
- **Status**: Patched in Microsoft's June 2026 Patch Tuesday update

### Microsoft Defender GreenPlasma Zero-Day
- **Description**: Zero-day vulnerability in Microsoft Defender enabling system-level access
- **Impact**: Allows attackers to achieve SYSTEM privileges on updated Windows installations
- **Status**: Patched in Microsoft's June 2026 Patch Tuesday update

### Microsoft Defender MiniPlasma Zero-Day
- **Description**: Third zero-day vulnerability affecting Microsoft Defender
- **Impact**: Grants access to BitLocker-protected drives, compromising encrypted data
- **Status**: Patched in Microsoft's June 2026 Patch Tuesday update

### Microsoft Defender RoguePlanet Zero-Day
- **Description**: Newly disclosed zero-day vulnerability released by security researcher Chaotic Eclipse
- **Impact**: Grants SYSTEM access on fully updated Windows systems
- **Status**: Zero-day with proof-of-concept exploit publicly available, not yet patched

### ServiceNow API Vulnerability
- **Description**: Unauthenticated access flaw through vulnerable API endpoint
- **Impact**: Allows unauthorized querying of customer instance data, exposing sensitive information
- **Status**: Security fix applied on June 5, 2026, but incident already occurred

### WinRAR Vulnerability
- **Description**: Security flaw in WinRAR archive software
- **Impact**: Enables deployment of password-stealing malware and data theft capabilities
- **Status**: Patched in July 2025, but actively exploited by Russian threat actors
- **CVE ID**: CVE-2025-8088

### Veeam Backup & Replication RCE
- **Description**: Critical remote code execution vulnerability in Veeam backup software
- **Impact**: Allows domain users to execute arbitrary code on backup servers
- **Status**: Security patches released by Veeam
- **CVE ID**: CVE-2026-44963

## Affected Systems and Products

- **Google Chrome**: All versions prior to latest security update containing V8 engine fix
- **Microsoft Windows**: All supported versions affected by Defender zero-days, requiring June 2026 patches
- **Microsoft Defender**: All versions vulnerable to multiple zero-day exploits
- **ServiceNow Instances**: Customer instances accessible through vulnerable API endpoints
- **WinRAR Software**: Versions prior to July 2025 patch vulnerable to archive exploitation
- **Veeam Backup & Replication**: Domain-joined backup servers exposed to RCE attacks
- **Ivanti Sentry**: Secure mobile gateway solutions with maximum-severity root execution flaws
- **SAP NetWeaver**: Critical vulnerabilities in enterprise application platform
- **SAP Commerce Cloud**: Critical-severity flaws in e-commerce platform
- **protobuf.js**: Node.js applications using JavaScript/TypeScript Protocol Buffers implementation

## Attack Vectors and Techniques

- **Browser Exploitation**: Chrome V8 engine vulnerabilities exploited through malicious web content
- **Privilege Escalation**: Microsoft Defender flaws used to gain SYSTEM-level access on Windows
- **API Abuse**: Unauthenticated ServiceNow API endpoints exploited for data access
- **Archive Manipulation**: WinRAR vulnerability exploited through malicious archive files
- **Supply Chain Attacks**: Miasma worm compromising Microsoft GitHub repositories with password-stealing malware
- **Email Spoofing**: Microsoft Exchange "Ghost-Sender" technique enabling address spoofing
- **Remote Code Execution**: Veeam backup servers compromised through authenticated domain user access
- **Root Privilege Escalation**: Ivanti Sentry flaws enabling maximum-privilege code execution

## Threat Actor Activities

- **Russian-Aligned Groups**: Conducting sustained campaigns against Ukrainian military and government organizations using WinRAR exploits for data theft and cyberespionage
- **Chaotic Eclipse (Nightmare-Eclipse)**: Security researcher releasing proof-of-concept exploits for Microsoft Defender zero-days, including RoguePlanet
- **Unknown Threat Actors**: Exploiting ServiceNow API vulnerabilities to gain unauthorized access to customer instances and data
- **Miasma Campaign**: Supply chain attacks targeting Microsoft GitHub repositories, injecting password-stealing malware into 73 open-source projects across Azure, Microsoft, Azure-Samples, and MicrosoftDocs organizations