# Exploitation Report

The current threat landscape reveals several critical vulnerabilities under active exploitation, with particular concern around infrastructure targeting and sophisticated attack campaigns. A critical n8n vulnerability with a 9.9 CVSS score is enabling authenticated attackers to execute arbitrary system commands, while the MongoBleed vulnerability is being actively exploited to extract sensitive credentials from MongoDB servers. Additionally, large-scale botnet operations are leveraging exposed Android Debug Bridge (ADB) interfaces and React2Shell vulnerabilities to compromise millions of devices, while threat actors continue to exploit a five-year-old Fortinet 2FA bypass vulnerability affecting over 10,000 exposed firewalls.

## Active Exploitation Details

### Critical n8n Vulnerability
- **Description**: A critical security vulnerability in n8n workflow automation platform allowing command execution
- **Impact**: Authenticated attackers can execute arbitrary system commands on the underlying server
- **Status**: Recently disclosed, requires immediate patching

### MongoBleed Memory Leak Vulnerability
- **Description**: A memory leak security vulnerability in MongoDB servers that exposes sensitive information
- **Impact**: Unauthenticated attackers can extract passwords and authentication tokens from MongoDB instances
- **Status**: Under active attack, patches available

### Fortinet 2FA Bypass Vulnerability
- **Description**: A five-year-old two-factor authentication bypass vulnerability in Fortinet firewalls
- **Impact**: Attackers can bypass authentication mechanisms and gain unauthorized access
- **Status**: Actively exploited with over 10,000 exposed devices still vulnerable

### React2Shell Vulnerability
- **Description**: Critical vulnerability affecting Next.js servers and IoT devices
- **Impact**: Enables remote code execution and device hijacking for botnet enrollment
- **Status**: Exploited by RondoDox botnet in persistent nine-month campaign

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Open-source automation platform with critical command execution vulnerability
- **MongoDB Servers**: Database servers vulnerable to memory leak attacks exposing credentials
- **Fortinet Firewalls**: Over 10,000 Internet-exposed devices vulnerable to 2FA bypass
- **Next.js Servers**: Web servers targeted by React2Shell exploitation
- **Android Devices**: Over 2 million devices infected via exposed ADB interfaces
- **ShareFile, Nextcloud, OwnCloud**: File-sharing platforms targeted for corporate data theft
- **VSCode IDE Forks**: Development environments including Cursor, Windsurf, Google Antigravity, and Trae vulnerable to malicious extension attacks

## Attack Vectors and Techniques

- **Exposed ADB Exploitation**: Kimwolf botnet leveraging exposed Android Debug Bridge interfaces through residential proxy networks
- **Memory Leak Exploitation**: MongoBleed attacks extracting sensitive data from MongoDB server memory
- **Authentication Bypass**: Fortinet firewall exploitation bypassing two-factor authentication
- **Social Engineering**: ClickFix campaigns using fake Windows BSOD screens to distribute malware
- **Messaging Platform Abuse**: UAC-0184 using Viber messaging to deliver malicious ZIP archives
- **Cloud Service Abuse**: Attackers impersonating Google-generated messages through Google Cloud Application Integration
- **Extension Poisoning**: Malicious actors creating non-existent extensions for VSCode IDE forks

## Threat Actor Activities

- **Kimwolf Operators**: Compromised over 2 million Android devices through proxy network tunneling and ADB exploitation
- **RondoDox Botnet**: Nine-month persistent campaign targeting IoT devices and web servers using React2Shell vulnerability
- **Zestix**: Corporate data theft operations targeting cloud file-sharing platforms
- **UAC-0184**: Russia-aligned threat actor targeting Ukrainian military and government through Viber messaging platform
- **Transparent Tribe**: Fresh RAT attacks against Indian governmental, academic, and strategic entities
- **Crimson Collective**: Extortion gang claiming breach of US broadband provider Brightspeed
- **VVS Stealer Operators**: Python-based information stealer targeting Discord credentials and tokens