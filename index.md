# Exploitation Report

Multiple critical zero-day vulnerabilities and active exploitation campaigns have been identified across major enterprise platforms. Microsoft's June 2026 Patch Tuesday addressed a record 206 vulnerabilities including three actively exploited zero-days (YellowKey, GreenPlasma, and MiniPlasma) that allow privilege escalation to SYSTEM level on fully patched Windows systems. A new Microsoft Defender zero-day called RoguePlanet was disclosed immediately after the patch release, demonstrating ongoing security researcher discoveries of critical flaws. ServiceNow confirmed unauthorized access to customer instances through an exploited API vulnerability, while Russian threat actors are weaponizing a WinRAR vulnerability in targeted campaigns against Ukrainian organizations. Additional critical vulnerabilities have been identified in Ivanti Sentry, Veeam Backup & Replication, and protobuf.js that enable remote code execution.

## Active Exploitation Details

### YellowKey Zero-Day
- **Description**: Microsoft Defender vulnerability allowing privilege escalation to SYSTEM level
- **Impact**: Attackers gain full administrative control on fully patched Windows systems
- **Status**: Patched in Microsoft's June 2026 Patch Tuesday release

### GreenPlasma Zero-Day  
- **Description**: Windows privilege escalation vulnerability
- **Impact**: Enables attackers to gain SYSTEM privileges on updated Windows systems
- **Status**: Fixed in June 2026 security updates

### MiniPlasma Zero-Day
- **Description**: BitLocker protection bypass vulnerability
- **Impact**: Grants unauthorized access to BitLocker-protected drives
- **Status**: Patched by Microsoft in June 2026

### RoguePlanet Zero-Day
- **Description**: New Microsoft Defender vulnerability granting SYSTEM access
- **Impact**: Allows privilege escalation to SYSTEM level on updated Windows systems
- **Status**: Active zero-day with proof-of-concept exploit released publicly

### ServiceNow API Vulnerability
- **Description**: Unauthenticated access flaw in ServiceNow API endpoint
- **Impact**: Unauthorized access to customer instances and data exposure
- **Status**: Security patch applied by ServiceNow on June 5, 2026

### WinRAR Vulnerability
- **Description**: Security flaw in WinRAR being exploited in targeted campaigns
- **Impact**: Data theft and cyberespionage capabilities
- **Status**: Previously fixed in July but actively exploited by Russian threat actors
- **CVE ID**: CVE-2025-8088

### Ivanti Sentry Critical Vulnerabilities
- **Description**: Two critical flaws in Ivanti Sentry secure mobile gateway, including maximum severity issue
- **Impact**: Remote code execution with root privileges
- **Status**: Patches released by Ivanti

### Veeam Backup & Replication RCE
- **Description**: Critical remote code execution vulnerability in backup software
- **Impact**: Domain users can execute remote code on backup servers
- **Status**: Security patches released
- **CVE ID**: CVE-2026-44963

### Microsoft Exchange Spoofing Flaw
- **Description**: "Ghost-Sender" vulnerability allowing email address spoofing
- **Impact**: Enables spoofing of any email address for phishing attacks
- **Status**: Widespread misconfiguration being actively abused

### Protobuf.js Vulnerabilities
- **Description**: Six vulnerabilities in JavaScript/TypeScript Protocol Buffers implementation
- **Impact**: Remote code execution and denial of service in Node.js applications
- **Status**: Vulnerabilities flagged by researchers

## Affected Systems and Products

- **Microsoft Windows**: All versions affected by zero-day vulnerabilities, with patches available for YellowKey, GreenPlasma, and MiniPlasma
- **Microsoft Defender**: Vulnerable to RoguePlanet zero-day exploit
- **ServiceNow Instances**: Customer environments affected by unauthorized API access
- **WinRAR**: Versions vulnerable to CVE-2025-8088 being targeted
- **Ivanti Sentry**: Secure mobile gateway solution with maximum severity flaws
- **Veeam Backup & Replication**: Domain-joined backup servers exposed to RCE
- **Microsoft Exchange**: Servers vulnerable to email spoofing attacks
- **Node.js Applications**: Using protobuf.js library exposed to RCE and DoS
- **SAP NetWeaver**: Critical vulnerabilities in enterprise platform
- **SAP Commerce Cloud**: Critical security flaws requiring immediate patching

## Attack Vectors and Techniques

- **Privilege Escalation**: Multiple zero-days enabling SYSTEM level access on Windows
- **API Exploitation**: Unauthenticated access through vulnerable ServiceNow endpoints
- **Email Spoofing**: Ghost-Sender technique for bypassing email authentication
- **Archive File Exploitation**: Weaponized WinRAR files for malware delivery
- **Supply Chain Attacks**: Miasma worm compromising Microsoft GitHub repositories
- **Remote Code Execution**: Critical vulnerabilities in backup and enterprise software
- **BitLocker Bypass**: Direct access to encrypted drive contents
- **Phishing Simulation**: AI agents vulnerable to traditional phishing tactics

## Threat Actor Activities

- **Russian Attackers**: Conducting targeted campaigns against Ukrainian military and government organizations using CVE-2025-8088
- **Unknown Actors**: Exploiting ServiceNow vulnerability for unauthorized customer data access
- **Chaotic Eclipse/Nightmare-Eclipse**: Security researcher releasing proof-of-concept for RoguePlanet zero-day
- **Supply Chain Attackers**: Miasma campaign compromising 73 Microsoft GitHub repositories
- **Cybercriminals**: Actively exploiting Exchange Ghost-Sender vulnerability for email spoofing campaigns