# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, with several maximum-severity flaws posing immediate threats to organizations. The most concerning activity includes active exploitation of a critical D-Link router vulnerability (CVE-2026-0625), a maximum-severity n8n workflow automation platform flaw dubbed "Ni8mare," and newly disclosed Veeam Backup & Replication vulnerabilities. Additionally, threat actors are leveraging sophisticated social engineering campaigns, including ClickFix-style attacks targeting hospitality sectors, malicious Chrome extensions compromising AI chat conversations, and SEO poisoning campaigns by the Black Cat cybercrime group.

## Active Exploitation Details

### D-Link DSL Router Remote Code Execution Vulnerability
- **Description**: A critical security flaw affecting legacy D-Link DSL gateway routers that enables remote code execution
- **Impact**: Complete remote compromise of affected router devices, allowing attackers to gain full control over network infrastructure
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-0625

### n8n Workflow Automation Platform "Ni8mare" Vulnerability
- **Description**: A maximum severity vulnerability in the n8n workflow automation platform that allows remote unauthenticated attackers to take complete control over locally deployed instances
- **Impact**: Full server takeover, enabling attackers to execute arbitrary code and access sensitive workflow data without authentication
- **Status**: Critical vulnerability requiring immediate patching

### Veeam Backup & Replication Remote Code Execution
- **Description**: Multiple security flaws in Veeam's Backup & Replication software, including a critical remote code execution vulnerability
- **Impact**: Attackers can execute arbitrary code on backup servers, potentially compromising backup infrastructure and data integrity
- **Status**: Recently patched, but poses significant risk to unpatched systems

### TOTOLINK EX200 Firmware Vulnerability
- **Description**: An unpatched security flaw in TOTOLINK EX200 wireless range extender firmware
- **Impact**: Remote authenticated attackers can gain full control of the device
- **Status**: Remains unpatched, exposing devices to potential takeover

## Affected Systems and Products

- **D-Link DSL Gateway Routers**: Legacy models affected by critical RCE vulnerability
- **n8n Workflow Automation Platform**: Both self-hosted and cloud versions impacted by maximum severity flaw
- **Veeam Backup & Replication**: Multiple versions affected by critical RCE and other security vulnerabilities
- **TOTOLINK EX200**: Wireless range extender with unpatched firmware vulnerability
- **Chrome Browser Extensions**: Two malicious extensions targeting ChatGPT and DeepSeek users
- **ownCloud Platform**: File-sharing platform experiencing credential theft incidents
- **Microsoft Outlook**: Classic version experiencing bugs preventing encrypted email access

## Attack Vectors and Techniques

- **SEO Poisoning**: Black Cat cybercrime group using fraudulent sites advertising popular software to distribute malware
- **ClickFix Social Engineering**: Threat actors deploying fake Blue Screen of Death pages to deliver DCRat malware
- **Malicious Browser Extensions**: Chrome extensions designed to exfiltrate AI chat conversations and browsing data
- **Email-Based Phishing**: Fake hotel booking emails redirecting staff to malicious BSoD pages
- **Domain Spoofing**: Exploitation of misconfigured email routing and spoof protections for internal domain phishing
- **Credential Stuffing**: Attackers using compromised credentials against cloud platforms lacking multi-factor authentication

## Threat Actor Activities

- **Black Cat Cybercrime Group**: Conducting SEO poisoning malware campaigns targeting users searching for popular software downloads
- **PHALT#BLYX Campaign**: Targeting hospitality sector with fake booking emails leading to DCRat malware deployment
- **Zestix Threat Actor**: Using various infostealers to obtain credentials and breach file-sharing instances of approximately 50 enterprises
- **NoName057(16)**: Pro-Russian hacktivist group using DDoSia tool to mobilize volunteers for attacks against Ukraine and Western targets
- **Scattered Lapsus$ Hunters**: Also known as ShinyHunters, caught in cybersecurity researcher honeypot operations
- **State-Sponsored Activities**: China reportedly increasing attacks on Taiwan's energy sector by tenfold in 2025