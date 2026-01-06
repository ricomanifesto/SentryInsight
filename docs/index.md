# Exploitation Report

Critical vulnerabilities across multiple platforms are currently under active attack, highlighting urgent security concerns for organizations worldwide. The most severe issues include a critical MongoDB memory leak vulnerability nicknamed "MongoBleed" that allows unauthenticated attackers to extract sensitive credentials, and a two-factor authentication bypass vulnerability in Fortinet firewalls affecting over 10,000 Internet-exposed devices. Additionally, high-severity vulnerabilities in the n8n workflow automation platform and AdonisJS Bodyparser are enabling system command execution and arbitrary file writes respectively. Botnet activities have expanded significantly with Kimwolf infecting over 2 million Android devices and RondoDox exploiting Next.js servers through React2Shell attacks.

## Active Exploitation Details

### MongoBleed Memory Leak Vulnerability
- **Description**: A critical memory leak security vulnerability in MongoDB servers that exposes sensitive information
- **Impact**: Allows unauthenticated attackers to extract passwords and authentication tokens from MongoDB servers
- **Status**: Under active attack, patches available

### Fortinet 2FA Bypass Vulnerability
- **Description**: A five-year-old two-factor authentication bypass vulnerability affecting Fortinet firewalls
- **Impact**: Enables attackers to bypass multi-factor authentication controls on firewall management interfaces
- **Status**: Actively exploited with over 10,000 Internet-exposed devices still vulnerable

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security vulnerability in the open-source workflow automation platform n8n
- **Impact**: Enables authenticated attackers to execute arbitrary system commands on underlying servers
- **Status**: Recently disclosed, patches available (CVSS Score: 9.9)

### AdonisJS Bodyparser Critical Flaw
- **Description**: Critical security vulnerability in the "@adonisjs/bodyparser" npm package
- **Impact**: Allows attackers to perform arbitrary file writes on servers, potentially leading to complete system compromise
- **Status**: Patches available, users advised to update immediately (CVSS Score: 9.2)

### React2Shell Exploitation
- **Description**: Vulnerability being exploited by RondoDox botnet targeting Next.js servers
- **Impact**: Enables deployment of cryptomining payloads, botnet recruitment, and other malicious activities
- **Status**: Actively exploited in ongoing campaigns

## Affected Systems and Products

- **MongoDB Servers**: All versions affected by MongoBleed memory leak vulnerability
- **Fortinet Firewalls**: Over 10,000 Internet-exposed devices vulnerable to 2FA bypass
- **n8n Platform**: Open-source workflow automation platform installations
- **AdonisJS Applications**: Systems using "@adonisjs/bodyparser" npm package
- **Next.js Servers**: Web applications built on Next.js framework targeted by RondoDox
- **Android Devices**: Over 2 million devices infected by Kimwolf botnet
- **ShareFile, Nextcloud, OwnCloud**: Cloud file-sharing platforms targeted by Zestix threat actor
- **VSCode IDE Forks**: Cursor, Windsurf, Google Antigravity, and Trae development environments
- **Discord Platforms**: Targeted by VVS Stealer malware for credential harvesting

## Attack Vectors and Techniques

- **Memory Exploitation**: MongoBleed leverages memory leaks to extract credentials without authentication
- **Authentication Bypass**: Fortinet vulnerability allows circumvention of two-factor authentication
- **Command Injection**: n8n vulnerability enables system command execution through authenticated access
- **File System Manipulation**: AdonisJS flaw permits arbitrary file writes to server directories
- **Social Engineering**: ClickFix campaigns use fake Windows BSOD screens to distribute malware
- **Botnet Infrastructure**: Kimwolf uses exposed ADB interfaces and residential proxy networks
- **Supply Chain Attacks**: VSCode fork vulnerabilities enable malicious extension recommendations
- **Phishing Campaigns**: Google Cloud email features abused for legitimate-appearing phishing messages
- **Mobile Malware**: VVS Stealer uses obfuscated Python code to target Discord credentials

## Threat Actor Activities

- **Zestix**: Actively targeting corporate data through compromised cloud file-sharing platforms including ShareFile, Nextcloud, and OwnCloud instances
- **UAC-0184**: Russia-aligned threat actor leveraging Viber messaging platform to deliver malicious ZIP archives targeting Ukrainian military and government entities
- **Kimwolf Operators**: Managing massive Android botnet with over 2 million infected devices using residential proxy networks and exposed ADB interfaces
- **RondoDox Group**: Expanding botnet operations through React2Shell exploitation targeting Next.js servers for cryptomining and payload deployment
- **Transparent Tribe**: Conducting fresh RAT attacks against Indian governmental, academic, and strategic entities
- **Crimson Collective**: Extortion gang claiming breach of US broadband provider Brightspeed
- **ShinyHunters**: Claiming successful breach of cybersecurity firm Resecurity (disputed as honeypot access)
- **ClickFix Campaign Operators**: Targeting European hospitality sector with fake BSOD social engineering attacks