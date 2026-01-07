# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, posing significant risks to organizations worldwide. The most severe threats include a maximum-severity remote code execution vulnerability in n8n workflow automation platform (CVE-2026-0625), active exploitation of legacy D-Link DSL routers through command injection flaws, and critical remote code execution vulnerabilities in Veeam Backup & Replication software. Additionally, sophisticated social engineering campaigns are targeting the hospitality sector with fake blue screen of death pages, while malicious Chrome extensions have compromised data from nearly 900,000 users. These exploitation activities demonstrate a concerning trend of attackers targeting both enterprise infrastructure and end-user systems through multiple attack vectors.

## Active Exploitation Details

### D-Link DSL Router Command Injection Vulnerability
- **Description**: A critical command injection vulnerability affecting multiple legacy D-Link DSL gateway routers that are no longer supported
- **Impact**: Allows attackers to execute arbitrary commands remotely, leading to complete device compromise
- **Status**: Currently under active exploitation in the wild; no patches available for end-of-life devices
- **CVE ID**: CVE-2026-0625

### n8n Workflow Automation RCE Vulnerability
- **Description**: Maximum-severity remote code execution vulnerability in the open-source workflow automation platform n8n
- **Impact**: Authenticated attackers can execute arbitrary system commands on underlying servers
- **Status**: Critical vulnerability with patches available; affects both self-hosted and cloud versions
- **CVE ID**: CVE-2026-0625

### Veeam Backup & Replication RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in Veeam's Backup & Replication software
- **Impact**: Remote code execution on backup servers, potentially compromising backup infrastructure
- **Status**: Security updates released to address multiple flaws including this critical issue

### AdonisJS Bodyparser Arbitrary File Write
- **Description**: Critical security flaw in the "@adonisjs/bodyparser" npm package allowing arbitrary file writes
- **Impact**: Attackers can write arbitrary files to servers, potentially leading to system compromise
- **Status**: Updates available to address the vulnerability

### TOTOLINK EX200 Firmware Vulnerability
- **Description**: Unpatched security flaw in TOTOLINK EX200 wireless range extender firmware
- **Impact**: Remote authenticated attackers can achieve full device takeover
- **Status**: Remains unpatched with no security updates available

## Affected Systems and Products

- **D-Link DSL Gateway Routers**: Multiple legacy models that are end-of-life and no longer supported
- **n8n Platform**: Both self-hosted installations and cloud versions of the workflow automation platform
- **Veeam Backup & Replication**: Enterprise backup and replication software installations
- **AdonisJS Applications**: Web applications using the "@adonisjs/bodyparser" npm package
- **TOTOLINK EX200**: Wireless range extender devices with vulnerable firmware
- **Chrome Browser**: Users with malicious extensions installed from Chrome Web Store
- **Android Devices**: Over 2 million devices infected by Kimwolf botnet through residential proxy networks

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of input validation flaws in D-Link router interfaces to execute arbitrary commands
- **Social Engineering (ClickFix)**: Fake blue screen of death pages delivered through phishing emails targeting hospitality sector
- **Browser Extension Abuse**: Malicious Chrome extensions stealing ChatGPT and DeepSeek conversations from users
- **Botnet Infrastructure**: Kimwolf Android botnet leveraging residential proxy networks to infect internal devices
- **Supply Chain Attacks**: VS Code forks recommending non-existent extensions creating supply chain risks
- **Email Routing Exploitation**: Misconfigured email routing and spoof protections enabling internal domain phishing
- **Credential Theft**: ownCloud users targeted for credential compromise requiring MFA implementation

## Threat Actor Activities

- **NoName057(16)**: Pro-Russian hacktivist group using DDoSia custom denial-of-service tool to mobilize volunteers against Ukraine and Western targets
- **Scattered Lapsus$ Hunters (ShinyHunters)**: Cybercriminal group caught in researcher honeypot operations
- **ClickFix Campaign Operators**: Threat actors targeting hospitality sector with fake BSoD pages to deploy DCRat remote access Trojan
- **State-Sponsored Actors**: China's cyber operations against Taiwan's energy sector increased tenfold in 2025
- **Kimwolf Botnet Operators**: Criminal group managing Android botnet with over 2 million infected devices
- **Chrome Extension Attackers**: Cybercriminals deploying malicious browser extensions to steal AI chat conversations from 900,000+ users