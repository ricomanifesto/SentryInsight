# Exploitation Report

Several critical vulnerabilities are currently being exploited in the wild, with the MongoBleed memory leak vulnerability under active attack allowing unauthenticated extraction of passwords and tokens from MongoDB servers. The cybersecurity landscape also shows significant activity around critical flaws in workflow automation platforms and web frameworks, with a 9.9 CVSS vulnerability in n8n enabling authenticated system command execution and a 9.2 CVSS flaw in AdonisJS Bodyparser allowing arbitrary file writes. Threat actors are leveraging diverse attack vectors including social engineering through fake BSOD screens, exploitation of exposed Android Debug Bridge connections affecting over 2 million devices, and sophisticated phishing campaigns abusing Google Cloud services.

## Active Exploitation Details

### MongoBleed Memory Leak Vulnerability
- **Description**: A critical memory leak security vulnerability affecting MongoDB servers that allows extraction of sensitive data from server memory
- **Impact**: Unauthenticated attackers can extract passwords, authentication tokens, and other sensitive information from MongoDB server memory
- **Status**: Currently under active attack with exploitation being observed in the wild

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security flaw in the open-source workflow automation platform n8n with a maximum CVSS score of 9.9
- **Impact**: Authenticated attackers can execute arbitrary system commands on the underlying server infrastructure
- **Status**: Recently disclosed vulnerability requiring immediate patching

### AdonisJS Bodyparser Arbitrary File Write
- **Description**: Critical vulnerability in the "@adonisjs/bodyparser" npm package with CVSS score of 9.2
- **Impact**: Successful exploitation allows attackers to write arbitrary files to the server, potentially leading to complete system compromise
- **Status**: Fixed version available, users advised to update immediately

### Fortinet Firewall 2FA Bypass
- **Description**: Five-year-old two-factor authentication bypass vulnerability affecting Fortinet firewalls
- **Impact**: Attackers can bypass multi-factor authentication protections to gain unauthorized access to firewall management interfaces
- **Status**: Over 10,000 Internet-exposed devices remain vulnerable and actively exploited

### React2Shell Exploitation in RondoDox Botnet
- **Description**: Vulnerability exploitation targeting Next.js servers as part of the RondoDox botnet expansion
- **Impact**: Enables deployment of cryptomining payloads, botnet infections, and other malicious activities targeting IoT networks and enterprises
- **Status**: Recent attacks showing expanded scope and targeting

## Affected Systems and Products

- **MongoDB Servers**: All versions affected by MongoBleed vulnerability requiring immediate patching
- **n8n Platform**: Open-source workflow automation platform users need to update to latest version
- **AdonisJS Applications**: Web applications using "@adonisjs/bodyparser" npm package
- **Fortinet Firewalls**: Over 10,000 Internet-exposed devices vulnerable to 2FA bypass
- **Android Devices**: Over 2 million devices infected via exposed ADB connections in Kimwolf botnet
- **Next.js Servers**: Targeted by RondoDox botnet for React2Shell exploitation
- **VSCode IDE Forks**: Cursor, Windsurf, Google Antigravity, and Trae exposed to malicious extension attacks
- **Cloud File-Sharing Platforms**: ShareFile, Nextcloud, and OwnCloud instances targeted for corporate data theft
- **Viber Messaging Platform**: Abused to deliver malicious ZIP archives to Ukrainian military and government

## Attack Vectors and Techniques

- **Memory Leak Exploitation**: Direct extraction of sensitive data from MongoDB server memory without authentication
- **Social Engineering**: Fake Windows Blue Screen of Death screens used to trick users into executing malware
- **Exposed ADB Exploitation**: Android Debug Bridge connections exploited through residential proxy networks
- **Phishing Campaigns**: Multi-stage attacks abusing Google Cloud Application Integration features
- **Malicious Extensions**: VSCode fork ecosystems exploited through non-existent extension recommendations
- **Platform Abuse**: Legitimate messaging platforms like Viber used for malware delivery
- **Supply Chain Attacks**: Third-party service compromises affecting multiple downstream customers

## Threat Actor Activities

- **Zestix**: Corporate data theft operations targeting cloud file-sharing platforms including ShareFile, Nextcloud, and OwnCloud instances
- **UAC-0184**: Russia-aligned group targeting Ukrainian military and government entities via Viber messaging platform with malicious ZIP archives
- **Kimwolf Operators**: Botnet campaign infecting over 2 million Android devices through exposed ADB and proxy network tunneling
- **ClickFix Campaign**: Social engineering operation targeting European hospitality sector with fake BSOD screens
- **Transparent Tribe**: Fresh RAT attacks against Indian governmental, academic, and strategic entities
- **ShinyHunters**: Claims of breaching cybersecurity firm Resecurity (disputed as honeypot access)
- **Crimson Collective**: Extortion gang claiming breach of US broadband provider Brightspeed
- **BlackCat/ALPHV Affiliates**: US cybersecurity professionals pleading guilty to ransomware activities