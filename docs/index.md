# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, with threat actors targeting network infrastructure, workflow automation systems, and cloud services. The most severe activity involves legacy D-Link DSL routers being actively exploited through a command injection vulnerability, while high-severity remote code execution flaws in n8n workflow automation and Veeam Backup & Replication systems present significant risks to enterprise environments. Additional threats include malicious browser extensions stealing AI chat conversations from nearly 900,000 users, sophisticated social engineering campaigns using fake system errors, and targeted attacks on cloud file-sharing platforms for corporate data theft.

## Active Exploitation Details

### D-Link DSL Router Command Injection Vulnerability
- **Description**: A critical command injection vulnerability affecting multiple legacy D-Link DSL gateway routers that are no longer supported
- **Impact**: Allows remote code execution with full device compromise, enabling attackers to take complete control of affected routers
- **Status**: Actively being exploited in the wild; affected devices are out of support with no patches available
- **CVE ID**: CVE-2026-0625

### n8n Workflow Automation RCE Vulnerability
- **Description**: Maximum severity remote code execution vulnerability in the open-source workflow automation platform n8n affecting both self-hosted and cloud versions
- **Impact**: Authenticated attackers can execute arbitrary system commands on underlying servers
- **Status**: Critical vulnerability with CVSS score of 10.0, patches available

### Veeam Backup & Replication RCE Vulnerability  
- **Description**: Critical remote code execution vulnerability in Veeam's Backup & Replication software
- **Impact**: Could allow attackers to execute arbitrary code on backup systems, potentially compromising backup integrity and availability
- **Status**: Critical severity with CVSS score of 9.0, security updates released

### TOTOLINK EX200 Firmware Vulnerability
- **Description**: Unpatched security flaw in TOTOLINK EX200 wireless range extender firmware
- **Impact**: Remote authenticated attackers can achieve full device takeover and complete system control
- **Status**: Remains unpatched with no available fixes

### AdonisJS Bodyparser Vulnerability
- **Description**: Critical vulnerability in the "@adonisjs/bodyparser" npm package
- **Impact**: Enables arbitrary file write operations on servers, potentially leading to system compromise
- **Status**: Critical severity with CVSS score of 9.2, updates available

## Affected Systems and Products

- **D-Link DSL Gateway Routers**: Legacy models no longer receiving security support
- **n8n Platform**: Both self-hosted deployments and cloud-hosted instances affected
- **Veeam Backup & Replication**: Enterprise backup and replication software installations
- **TOTOLINK EX200**: Wireless range extender devices with vulnerable firmware
- **AdonisJS Applications**: Systems using the vulnerable bodyparser npm package
- **Chrome Browser**: Extensions marketplace with malicious extensions targeting AI chat services
- **Cloud File-sharing Platforms**: ShareFile, Nextcloud, and OwnCloud instances targeted for data theft

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of input validation failures in D-Link router firmware
- **Authenticated RCE**: Leveraging authenticated access to execute system commands in n8n platforms
- **Social Engineering - ClickFix**: Fake Blue Screen of Death displays tricking users into executing malicious code
- **Browser Extension Abuse**: Malicious Chrome extensions exfiltrating ChatGPT and DeepSeek conversations
- **Supply Chain Attacks**: Missing extensions in VS Code forks creating opportunities for malicious package injection
- **Email-based Attacks**: Fake booking confirmation emails redirecting to malicious infrastructure
- **Proxy Network Abuse**: Kimwolf botnet exploiting residential proxy vulnerabilities for lateral movement

## Threat Actor Activities

- **Zestix Group**: Targeting cloud file-sharing platforms (ShareFile, Nextcloud, OwnCloud) for corporate data theft and offering stolen data for sale
- **ClickFix Operators**: Running PHALT#BLYX campaign targeting hospitality sector with fake BSOD screens delivering DCRat remote access trojans
- **Chrome Extension Attackers**: Operating malicious browser extensions that have compromised approximately 900,000 users' AI chat conversations
- **Kimwolf Botnet Operators**: Managing Android malware network affecting over 2 million devices through residential proxy exploitation
- **China-linked Groups**: Significantly escalating attacks against Taiwan's energy sector with a tenfold increase in activity
- **Scattered Lapsus$ Hunters**: Also known as ShinyHunters, continuing data theft operations and being targeted by security researcher honeypots