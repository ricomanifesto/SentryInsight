# Exploitation Report

Microsoft released a record-breaking 206 security fixes in June 2026, addressing three actively exploited zero-day vulnerabilities alongside critical remote code execution flaws. The most significant exploitation activity includes zero-day vulnerabilities in Microsoft Defender granting SYSTEM-level access, ServiceNow API flaws enabling unauthorized customer data access, and a newly disclosed Microsoft Defender zero-day called "RoguePlanet." Additional critical exploitation includes supply chain attacks against Microsoft GitHub repositories, WinRAR vulnerabilities being weaponized by Russian threat actors against Ukrainian targets, and critical remote code execution flaws in enterprise software including Veeam Backup & Replication, Ivanti Sentry, and SAP products.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities (YellowKey, GreenPlasma, MiniPlasma)
- **Description**: Three zero-day vulnerabilities in Microsoft Defender that allow privilege escalation and unauthorized access to encrypted drives
- **Impact**: Attackers can gain SYSTEM privileges on fully patched Windows systems and access BitLocker-protected drives
- **Status**: Patched by Microsoft during June 2026 Patch Tuesday

### Microsoft Defender RoguePlanet Zero-Day
- **Description**: A newly disclosed zero-day vulnerability in Microsoft Defender released by security researcher Chaotic Eclipse
- **Impact**: Grants SYSTEM access on updated Windows systems
- **Status**: Currently unpatched, proof-of-concept exploit publicly available

### ServiceNow API Access Flaw
- **Description**: Unauthenticated access vulnerability through a vulnerable API endpoint
- **Impact**: Unauthorized access to customer instances and data exposure
- **Status**: Security patch applied on June 5, 2026

### WinRAR Vulnerability
- **Description**: Previously patched vulnerability being actively exploited in targeted campaigns
- **Impact**: Used for data theft and cyberespionage operations
- **Status**: Fixed in July 2025, but still being exploited against unpatched systems
- **CVE ID**: CVE-2025-8088

### Ivanti Sentry Maximum Severity Flaw
- **Description**: Critical vulnerability in Ivanti's Sentry secure mobile gateway solution
- **Impact**: Remote code execution with root privileges
- **Status**: Recently patched by Ivanti

### Veeam Backup & Replication RCE Vulnerability
- **Description**: Critical flaw affecting domain-joined backup servers
- **Impact**: Remote code execution by domain users
- **Status**: Security patches released
- **CVE ID**: CVE-2026-44963

## Affected Systems and Products

- **Microsoft Windows**: All versions affected by Defender zero-days, record 206 vulnerabilities patched
- **Microsoft Defender**: Multiple zero-day vulnerabilities granting SYSTEM access
- **ServiceNow Instances**: Customer data exposed through API vulnerability
- **Ivanti Sentry**: Secure mobile gateway solution vulnerable to root-level code execution
- **Veeam Backup & Replication**: Enterprise backup software exposed to RCE attacks
- **SAP NetWeaver and Commerce Cloud**: Four critical-severity vulnerabilities patched
- **protobuf.js**: Six vulnerabilities exposing Node.js applications to RCE and DoS
- **WinRAR**: Legacy vulnerability still being exploited in targeted campaigns
- **Microsoft GitHub Repositories**: 73 repositories compromised in supply chain attack

## Attack Vectors and Techniques

- **Privilege Escalation**: Zero-day exploits targeting Microsoft Defender to gain SYSTEM privileges
- **API Exploitation**: Unauthenticated access through vulnerable ServiceNow API endpoints
- **Supply Chain Attacks**: Miasma worm compromising Microsoft GitHub repositories with malicious code injection
- **Targeted Phishing**: WinRAR exploits delivered through targeted campaigns against specific organizations
- **Remote Code Execution**: Critical vulnerabilities in enterprise software allowing unauthorized code execution
- **Email Spoofing**: Microsoft Exchange "Ghost-Sender" misconfiguration enabling email address spoofing

## Threat Actor Activities

- **Russian Threat Actors**: Actively exploiting WinRAR vulnerability in targeted campaigns against Ukrainian military and government organizations
- **Chaotic Eclipse (Nightmare-Eclipse)**: Security researcher releasing proof-of-concept exploits for Microsoft Defender zero-days
- **Miasma Campaign Operators**: Compromising Microsoft GitHub repositories through supply chain attacks, affecting continuous integration pipelines
- **Unknown ServiceNow Attackers**: Exploiting API vulnerabilities to gain unauthorized access to customer instances and sensitive data