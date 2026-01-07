# Exploitation Report

The current threat landscape reveals significant exploitation activity targeting multiple platforms and technologies. Active attacks are leveraging command injection vulnerabilities in legacy D-Link DSL routers, critical security flaws in web applications including a 9.9 CVSS vulnerability in n8n workflow automation platform and a 9.2 CVSS flaw in AdonisJS Bodyparser. The Kimwolf Android botnet has expanded to over 2 million infected devices through proxy network exploitation, while threat actors are actively exploiting the MongoBleed vulnerability in MongoDB servers. Social engineering campaigns using ClickFix techniques and fake Blue Screen of Death displays are delivering DCRat malware to hospitality sector targets.

## Active Exploitation Details

### D-Link DSL Router Command Injection Vulnerability
- **Description**: Command injection vulnerability affecting multiple legacy D-Link DSL gateway routers that are no longer supported
- **Impact**: Allows threat actors to execute arbitrary commands on compromised devices
- **Status**: Currently being actively exploited in the wild; affected devices are out of support with no patches available

### n8n Workflow Automation Platform Vulnerability
- **Description**: Critical security vulnerability in the open-source workflow automation platform
- **Impact**: Enables authenticated attackers to execute arbitrary system commands on the underlying system
- **Status**: Actively disclosed with patches available
- **CVE ID**: CVSS score 9.9

### AdonisJS Bodyparser Critical Flaw
- **Description**: Critical security vulnerability in the "@adonisjs/bodyparser" npm package
- **Impact**: Allows attackers to perform arbitrary file write operations on servers
- **Status**: Patches available, users advised to update immediately
- **CVE ID**: CVSS score 9.2

### MongoBleed Memory Leak Vulnerability
- **Description**: Memory leak security vulnerability affecting MongoDB servers
- **Impact**: Allows unauthenticated attackers to extract passwords and tokens from MongoDB servers
- **Status**: Under active attack, patches available

### TOTOLINK EX200 Wireless Range Extender Flaw
- **Description**: Unpatched firmware security flaw in TOTOLINK EX200 wireless range extender
- **Impact**: Enables remote authenticated attackers to gain full control of the device
- **Status**: Remains unpatched according to CERT/CC disclosure

## Affected Systems and Products

- **D-Link DSL Gateway Routers**: Legacy models that are out of support and vulnerable to command injection
- **n8n Workflow Automation Platform**: Open-source automation platform vulnerable to command execution
- **AdonisJS Bodyparser**: npm package used in Node.js applications for parsing request bodies
- **MongoDB Servers**: Database servers affected by the MongoBleed memory leak vulnerability
- **TOTOLINK EX200**: Wireless range extender with unpatched firmware vulnerabilities
- **Android Devices**: Over 2 million devices infected by Kimwolf botnet through proxy networks
- **Chrome Web Store Extensions**: Two malicious extensions targeting ChatGPT and DeepSeek users
- **VS Code Forks**: AI-powered development environments including Cursor, Windsurf, Google Antigravity, and Trae

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of input validation flaws in legacy networking equipment
- **Proxy Network Tunneling**: Kimwolf botnet uses residential proxy networks to infect internal devices via exposed ADB interfaces
- **Social Engineering - ClickFix**: Fake Blue Screen of Death pages trick users into executing malicious code
- **Malicious Browser Extensions**: Extensions stealing conversation data from AI chat platforms
- **Supply Chain Attacks**: Exploitation of missing extensions in Open VSX registry for VS Code forks
- **Memory Leak Exploitation**: Direct extraction of sensitive data from MongoDB server memory
- **Viber Messaging Platform**: Delivery of malicious ZIP archives to Ukrainian targets

## Threat Actor Activities

- **UAC-0184**: Russia-aligned threat actor targeting Ukrainian military and government entities using Viber messaging platform
- **Kimwolf Botnet Operators**: Expanded Android botnet to over 2 million devices using proxy network exploitation techniques
- **ClickFix Campaign Actors**: Targeting European hospitality sector with fake BSOD screens delivering DCRat malware
- **Zestix**: Threat actor offering stolen corporate data from compromised ShareFile, Nextcloud, and OwnCloud instances
- **Scattered Lapsus$ Hunters (ShinyHunters)**: Caught in cybersecurity researcher honeypot operations
- **RondoDox Botnet**: Expanding operations with React2Shell exploitation targeting Next.js servers
- **BlackCat/ALPHV Ransomware Affiliates**: Two US cybersecurity professionals pleaded guilty to ransomware activities
- **Crimson Collective**: Extortion gang claiming breach of US broadband provider Brightspeed