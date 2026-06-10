# Exploitation Report

Critical exploitation activity is ongoing across multiple enterprise platforms, with attackers leveraging both zero-day vulnerabilities and known flaws against high-value targets. Active exploits include CVE-2026-11645, a Chrome V8 zero-day under active attack, CVE-2026-44963 affecting Veeam backup infrastructure, and CVE-2025-8088 in WinRAR being weaponized by Russia-aligned groups against Ukrainian organizations. ServiceNow instances have been compromised through an unauthenticated API vulnerability, while Microsoft Defender faces a new zero-day dubbed "RoguePlanet" that grants SYSTEM privileges. Supply chain attacks have also escalated, with the Miasma worm compromising 73 Microsoft repositories and injecting credential-stealing malware.

## Active Exploitation Details

### Chrome V8 Zero-Day
- **Description**: High-severity vulnerability in Google Chrome's V8 JavaScript engine being actively exploited in the wild
- **Impact**: Allows attackers to execute arbitrary code through browser exploitation
- **Status**: Google has released security patches; actively being exploited
- **CVE ID**: CVE-2026-11645

### ServiceNow Unauthenticated Access Flaw
- **Description**: Security vulnerability allowing unauthorized access through vulnerable API endpoints without authentication
- **Impact**: Enables attackers to query and access customer instance data, potentially exposing sensitive organizational information
- **Status**: ServiceNow applied security patches on June 5, 2026; actively exploited by unknown threat actors

### Veeam Backup & Replication Remote Code Execution
- **Description**: Critical vulnerability in Veeam's backup software allowing remote code execution by domain users
- **Impact**: Compromises backup infrastructure integrity and could lead to ransomware deployment or data theft
- **Status**: Security patches released by Veeam
- **CVE ID**: CVE-2026-44963

### WinRAR Archive Processing Vulnerability
- **Description**: Security flaw in WinRAR archive processing being exploited nearly a year after patch release
- **Impact**: Enables deployment of credential-stealing malware and data exfiltration capabilities
- **Status**: Patches available since July 2025; actively exploited by Russia-aligned groups
- **CVE ID**: CVE-2025-8088

### Microsoft Defender RoguePlanet Zero-Day
- **Description**: Newly disclosed zero-day vulnerability in Microsoft Defender with proof-of-concept exploit released
- **Impact**: Grants SYSTEM-level privileges on updated Windows systems, bypassing security controls
- **Status**: Actively exploitable; proof-of-concept publicly available

### Ivanti Sentry Maximum Severity Flaw
- **Description**: Critical vulnerability in Ivanti's Sentry secure mobile gateway solution
- **Impact**: Enables remote code execution with root privileges on affected systems
- **Status**: Patches released by Ivanti

## Affected Systems and Products

- **Google Chrome**: V8 JavaScript engine vulnerable to zero-day exploitation
- **ServiceNow Instances**: Customer instances exposed through API vulnerability
- **Veeam Backup & Replication**: Domain-joined backup servers at risk of remote code execution
- **WinRAR Software**: Archive processing functionality vulnerable to malware injection
- **Microsoft Defender**: Windows endpoint protection with privilege escalation vulnerability
- **Ivanti Sentry**: Secure mobile gateway solutions with root-level compromise risk
- **SAP NetWeaver and Commerce Cloud**: Enterprise applications with critical security flaws
- **Microsoft Exchange**: Email spoofing vulnerabilities in hybrid configurations
- **protobuf.js**: Node.js applications using JavaScript Protocol Buffers implementation

## Attack Vectors and Techniques

- **Browser-Based Exploitation**: Zero-day attacks through Chrome V8 engine targeting web users
- **API Exploitation**: Unauthenticated access through vulnerable ServiceNow API endpoints
- **Supply Chain Compromise**: Miasma worm injecting malicious code into Microsoft repositories on GitHub
- **Spear Phishing with Malicious Archives**: WinRAR exploitation targeting Ukrainian organizations with weaponized archives
- **Privilege Escalation**: Microsoft Defender exploitation for SYSTEM-level access
- **Email Spoofing**: "Ghost-Sender" technique using Exchange hybrid configurations
- **SSD Timing Attacks**: FROST attack using JavaScript to track user activity via storage timing analysis

## Threat Actor Activities

- **Russia-Aligned Groups**: Conducting sustained campaigns against Ukrainian military and government targets using WinRAR exploits for data theft and cyberespionage operations
- **Unknown ServiceNow Attackers**: Exploiting API vulnerabilities to gain unauthorized access to customer instances and data
- **Miasma Supply Chain Attackers**: Compromising Microsoft repositories to inject credential-stealing malware affecting development pipelines
- **Chaotic Eclipse (Nightmare-Eclipse)**: Anonymous security researcher releasing Microsoft Defender zero-day exploits with public proof-of-concept code
- **Chrome Exploitation Groups**: Actively exploiting V8 zero-day vulnerability against web users in targeted campaigns