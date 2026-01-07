# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with several high-severity vulnerabilities under active attack. The most concerning developments include active exploitation of legacy D-Link DSL routers through a command injection vulnerability (CVE-2026-0625), a maximum-severity remote code execution flaw in the n8n workflow automation platform, and critical vulnerabilities in Veeam Backup & Replication software. Additionally, sophisticated social engineering campaigns are leveraging fake Blue Screen of Death screens and malicious browser extensions to compromise systems and steal sensitive data, while the Kimwolf Android botnet continues to expand by exploiting residential proxy networks.

## Active Exploitation Details

### D-Link DSL Router Command Injection Vulnerability
- **Description**: A critical command injection vulnerability affecting multiple legacy D-Link DSL gateway routers that are no longer supported
- **Impact**: Attackers can achieve remote code execution and full device compromise on affected routers
- **Status**: Currently under active exploitation in the wild, with no patches available as devices are end-of-life
- **CVE ID**: CVE-2026-0625

### n8n Workflow Automation RCE Vulnerability
- **Description**: A maximum-severity remote code execution vulnerability in the open-source workflow automation platform n8n
- **Impact**: Authenticated attackers can execute arbitrary system commands on underlying servers
- **Status**: Critical vulnerability with CVSS score of 10.0, affecting both self-hosted and cloud versions

### Veeam Backup & Replication RCE Vulnerability  
- **Description**: A critical remote code execution vulnerability in Veeam's Backup & Replication software
- **Impact**: Successful exploitation could result in complete system compromise
- **Status**: Recently patched by Veeam with CVSS score of 9.0

### TOTOLINK EX200 Firmware Vulnerability
- **Description**: An unpatched security flaw in TOTOLINK EX200 wireless range extender firmware
- **Impact**: Remote authenticated attackers can gain full device control and complete system takeover
- **Status**: Disclosed by CERT/CC but remains unpatched

### AdonisJS Bodyparser Vulnerability
- **Description**: A critical vulnerability in the "@adonisjs/bodyparser" npm package
- **Impact**: Successful exploitation enables arbitrary file write operations on affected servers
- **Status**: Critical severity with CVSS score of 9.2, patches available

## Affected Systems and Products

- **D-Link DSL Gateway Routers**: Legacy models that are end-of-life and no longer receiving security updates
- **n8n Platform**: Both self-hosted installations and cloud-hosted versions of the workflow automation platform
- **Veeam Backup & Replication**: Enterprise backup and replication software installations
- **TOTOLINK EX200**: Wireless range extender devices with vulnerable firmware
- **AdonisJS Applications**: Web applications using the vulnerable bodyparser npm package
- **Chrome Browser**: Users with malicious extensions targeting ChatGPT and DeepSeek conversations
- **Android Devices**: Mobile devices infected through residential proxy network vulnerabilities
- **VS Code Forks**: AI-powered development environments including Cursor, Windsurf, Google Antigravity, and Trae

## Attack Vectors and Techniques

- **Command Injection**: Direct exploitation of input validation flaws in D-Link router firmware
- **Social Engineering**: ClickFix campaigns using fake Blue Screen of Death screens to trick users into executing malware
- **Malicious Browser Extensions**: Data exfiltration through compromised Chrome extensions affecting 900,000 users
- **Supply Chain Attacks**: Exploitation of missing extensions in VS Code forks creating security risks in Open VSX registry
- **Botnet Propagation**: Kimwolf malware spreading through compromised residential proxy networks to infect internal devices
- **Email-Based Attacks**: Fake hotel booking emails redirecting staff to malicious BSoD pages delivering DCRat malware
- **Residential Proxy Abuse**: Exploitation of proxy network vulnerabilities to reach internal corporate networks

## Threat Actor Activities

- **Kimwolf Botnet Operators**: Successfully compromised over 2 million Android devices by exploiting residential proxy vulnerabilities
- **ClickFix Campaign Actors**: Targeting hospitality sector in Europe with sophisticated social engineering using fake Windows BSOD screens
- **Chrome Extension Threat Actors**: Deployed malicious extensions to steal ChatGPT and DeepSeek conversations from 900,000 users
- **Scattered Lapsus$ Hunters**: Also known as ShinyHunters, recently caught in cybersecurity researcher honeypot operations
- **PHALT#BLYX Campaign**: Targeting hotel staff with fake booking emails that redirect to malicious BSoD pages delivering DCRat remote access trojan
- **Zestix Group**: Conducting corporate data theft attacks by targeting cloud file-sharing platforms including ShareFile, Nextcloud, and OwnCloud instances
- **Chinese State Actors**: Taiwan reports tenfold increase in attacks against energy sector infrastructure in 2025