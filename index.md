# Exploitation Report

The cybersecurity landscape is experiencing unprecedented exploitation activity with Microsoft releasing a record-breaking 206 security fixes, including three actively exploited zero-day vulnerabilities. Critical zero-days named YellowKey, GreenPlasma, and MiniPlasma have been patched after being exploited to gain SYSTEM privileges on fully patched Windows systems and access BitLocker-protected drives. Additionally, a new zero-day called RoguePlanet targeting Microsoft Defender has been disclosed with proof-of-concept exploit code released. ServiceNow suffered a security incident involving unauthorized access through an exploited API flaw, while Ivanti Sentry faces maximum-severity vulnerabilities allowing root code execution. Russian threat actors are actively weaponizing a WinRAR vulnerability against Ukrainian organizations, and Microsoft's GitHub repositories were compromised in a supply chain attack affecting 73 projects.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities (YellowKey, GreenPlasma, MiniPlasma)
- **Description**: Three zero-day vulnerabilities in Windows systems that were actively exploited before Microsoft's June 2026 Patch Tuesday
- **Impact**: Attackers can gain SYSTEM privileges on fully patched Windows systems and access BitLocker-protected drives
- **Status**: Patches released by Microsoft in June 2026 Patch Tuesday addressing 206 total vulnerabilities

### Microsoft Defender RoguePlanet Zero-Day
- **Description**: A newly disclosed zero-day vulnerability in Microsoft Defender discovered by security researcher Chaotic Eclipse
- **Impact**: Grants SYSTEM access on updated Windows systems
- **Status**: Proof-of-concept exploit released; patch status unclear

### ServiceNow API Vulnerability
- **Description**: An unauthenticated access flaw in ServiceNow's API endpoint that was exploited by unknown threat actors
- **Impact**: Unauthorized access to customer instances and data exposure
- **Status**: Security patch applied on June 5, 2026

### WinRAR Vulnerability Against Ukrainian Organizations
- **Description**: Russian attackers are exploiting a WinRAR vulnerability in targeted campaigns against Ukrainian organizations
- **Impact**: Data theft and cyberespionage operations against military and government targets
- **Status**: Previously patched in July (referencing CVE-2025-8088), but still being actively exploited
- **CVE ID**: CVE-2025-8088

### Ivanti Sentry Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Ivanti's Sentry secure mobile gateway solution, including a maximum-severity flaw
- **Impact**: Remote code execution with root privileges
- **Status**: Patches released by Ivanti

### Veeam Backup & Replication RCE Vulnerability
- **Description**: A critical flaw in Veeam's Backup & Replication software affecting domain-joined backup servers
- **Impact**: Remote code execution allowing domain users to run remote code
- **Status**: Security patches released by Veeam
- **CVE ID**: CVE-2026-44963

## Affected Systems and Products

- **Microsoft Windows**: All versions affected by the three zero-day vulnerabilities (YellowKey, GreenPlasma, MiniPlasma)
- **Microsoft Defender**: Affected by RoguePlanet zero-day on updated Windows systems
- **ServiceNow Instances**: Customer instances exposed through vulnerable API endpoints
- **Ivanti Sentry**: Secure mobile gateway solution with maximum-severity vulnerabilities
- **Veeam Backup & Replication**: Domain-joined backup servers vulnerable to RCE attacks
- **WinRAR**: Targeted in campaigns against Ukrainian organizations
- **Microsoft GitHub Repositories**: 73 repositories compromised across Azure, microsoft, Azure-Samples, and MicrosoftDocs organizations
- **SAP NetWeaver and Commerce Cloud**: Four critical-severity flaws patched in June 2026
- **protobuf.js**: Six vulnerabilities exposing Node.js applications to RCE and DoS attacks

## Attack Vectors and Techniques

- **Privilege Escalation**: Zero-day vulnerabilities exploited to gain SYSTEM privileges on Windows systems
- **BitLocker Bypass**: Exploitation techniques to access BitLocker-protected drives
- **API Exploitation**: Unauthenticated access through vulnerable ServiceNow API endpoints
- **Supply Chain Compromise**: Miasma worm attack targeting Microsoft GitHub repositories with password-stealing malware
- **Social Engineering**: Targeted phishing campaigns using WinRAR vulnerabilities
- **Remote Code Execution**: Multiple RCE vulnerabilities across Ivanti, Veeam, and other platforms
- **Email Spoofing**: Microsoft Exchange misconfiguration allowing attackers to spoof any email address (Ghost-Sender technique)

## Threat Actor Activities

- **Russian Threat Groups**: Conducting two separate campaigns exploiting WinRAR vulnerabilities for data theft and cyberespionage against Ukrainian military and government targets
- **Unknown ServiceNow Attackers**: Exploited API vulnerability on June 5, 2026, to gain unauthorized access to customer instances
- **Miasma Supply Chain Attackers**: Compromised 73 Microsoft GitHub repositories, injecting password-stealing malware into continuous integration pipelines
- **Chaotic Eclipse (Nightmare-Eclipse)**: Security researcher who disclosed the RoguePlanet zero-day with proof-of-concept exploit
- **Zero-Day Exploiters**: Unknown threat actors who actively exploited the YellowKey, GreenPlasma, and MiniPlasma vulnerabilities before patches were available