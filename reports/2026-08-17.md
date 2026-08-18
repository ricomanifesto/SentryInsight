---
schema_version: 2
report_date: 2026-08-17
generated_at: 2026-08-17T21:37:02Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-17/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, ranging from enterprise software to consumer devices. GitLab, Forminator WordPress plugin, VMware vCenter, SAP Commerce Cloud, Apple macOS Screen Sharing, and Microsoft Defender all have confirmed exploitation activity, with several carrying maximum CVSS scores of 9.8–10.0.

A suspected China-nexus APT is leveraging the VMware vCenter flaw (CVE-2026-59310) to deploy Babuk-derived ransomware, while Iranian nation-state actors continue evolving the Cavern C2 framework using DNS and Google Apps Script for stealthy communications. The Unisoc VoLTE exploit chain demonstrates a sophisticated two-stage attack achieving full Android kernel access with no vendor fix available, and the Evooo1Bot Linux botnet is actively weaponizing known vulnerabilities to convert edge devices into persistent SOCKS5 proxy infrastructure.

## Active Exploitation Details

### GitLab GraphQL Authentication Bypass (CVE-2026-19478)
- **Description**: A critical vulnerability in GitLab Community Edition and Enterprise Edition that allows unauthenticated attackers to remotely modify or delete public projects and user data under certain conditions through the GraphQL API.
- **Impact**: Unauthenticated remote modification or deletion of public projects and user data.
- **Status**: Security updates released by GitLab; patch available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [The Hacker News — Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

### Forminator WordPress Plugin Unauthenticated RCE (CVE-2026-15748)
- **Description**: Critical remote code execution vulnerability in Forminator Forms WordPress plugin (600,000+ active installations) enabling arbitrary code execution via malicious PHP file uploads without authentication.
- **Impact**: Full unauthenticated remote code execution on vulnerable WordPress sites.
- **Status**: Vulnerability disclosed; patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-15748
- **Reporting**: [The Hacker News — Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

### Certighost Enterprise CA Privilege Escalation (CVE-2026-54121)
- **Description**: Vulnerability allowing a standard domain user to escalate privileges and turn an Enterprise Certificate Authority into a Domain Controller, exposing fundamental PKI trust issues.
- **Impact**: Domain compromise via CA privilege escalation; Tier 0 identity infrastructure breach.
- **Status**: Patch available; described as "the easy part" with deeper architectural lessons needed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-54121
- **Reporting**: [Bleeping Computer — Certighost and the Privilege Hiding in Your Certificate Authority](https://www.bleepingcomputer.com/news/security/certighost-and-the-privilege-hiding-in-your-certificate-authority/)

### ShieldBreak Microsoft Defender Zero-Day (CVE-2026-69414)
- **Description**: Zero-day vulnerability in Microsoft Defender disclosed by researcher "Nightmare Eclipse" that bypasses security controls; Microsoft is actively developing a patch.
- **Impact**: Defender bypass and potential security control evasion.
- **Status**: Zero-day disclosed; Microsoft working on patch; no fix released yet.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: mitigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — Microsoft working on Defender patch for ShieldBreak zero-day](https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/)

### VMware vCenter Directory Traversal (CVE-2026-59310)
- **Description**: Severe directory traversal vulnerability in VMware vCenter Server (CVSS 9.8) allowing unauthenticated remote code execution; actively exploited by a suspected China-nexus APT to deploy Babuk-derived ransomware.
- **Impact**: Unauthenticated remote code execution leading to ransomware deployment.
- **Status**: Newly patched by Broadcom; active exploitation confirmed in the wild.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [The Hacker News — Suspected China-Nexus Actor Exploits VMware vCenter Flaw, Deploys Babuk-Derived Ransomware](https://thehackernews.com/2026/08/suspected-china-nexus-actor-exploits.html)

### SAP Commerce Cloud Authentication Bypass (CVE-2026-58231)
- **Description**: Maximum-severity vulnerability (CVSS 10.0) involving insufficient authorization checks and input validation, allowing unauthenticated attackers to abuse a default authentication client.
- **Impact**: Unauthenticated access and potential full compromise of SAP Commerce Cloud instances.
- **Status**: Patched; active exploitation attempts observed days after patch release.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-58231
- **Reporting**: [The Hacker News — SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch](https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html)

### Apple macOS Screen Sharing Authentication Flaw (CVE-2026-65400)
- **Description**: Critical authentication issue in macOS Screen Sharing component (CVSS 9.8) allowing network-adjacent attackers to bypass authentication; actively exploited to deploy Monero cryptocurrency miners on internet-exposed Macs.
- **Impact**: Unauthorized remote access and cryptominer deployment.
- **Status**: Recently patched by Apple; active exploitation confirmed by NCSC-NL.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65400
- **Reporting**: [The Hacker News — Apple macOS Screen Sharing Flaw Exploited on Internet-Exposed Macs to Install Monero Miner](https://thehackernews.com/2026/08/apple-macos-screen-sharing-flaw.html)

### Snowflake GitHub Actions Workflow Injection
- **Description**: Command injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository via crafted GitHub issues triggering malicious workflow execution in `.github/workflows/jira_issue.yml` containing internal Jira credentials.
- **Impact**: Command execution in CI/CD pipeline with access to internal credentials.
- **Status**: Disclosed by Wiz researchers; patch status not specified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)

### Unisoc VoLTE Video Call Exploit Chain
- **Description**: Two-stage exploit chain achieving full Android kernel access on devices with Unisoc modem firmware through a VoLTE video call; second stage published August 17, 2026, following initial RCE disclosure in March 2026.
- **Impact**: Full kernel-level compromise via zero-click or one-click VoLTE call.
- **Status**: No fix available from chipset maker; exploit code published.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access](https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html)

### Evooo1Bot Linux Botnet Known Vulnerability Exploitation
- **Description**: Mirai-derived modular botnet actively exploiting known vulnerabilities in internet-facing gateway devices to enroll them as SOCKS5 proxy nodes, extending beyond DDoS with credential theft and reverse SOCKS relays.
- **Impact**: Device compromise, persistent proxy infrastructure, credential theft, network pivoting.
- **Status**: Active campaigns observed; exploits known flaws (specific CVEs not enumerated in sources).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Evooo1Bot Linux Botnet Exploits Known Flaws to Turn Edge Devices Into SOCKS5 Proxies](https://thehackernews.com/2026/08/evooo1bot-linux-botnet-exploits-known.html), [Bleeping Computer — New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/), [Dark Reading — Linux Botnet Evooo1Bot Expands Mirai Capabilities Well Beyond DDoS](https://www.darkreading.com/cyber-risk/linux-botnet-evooo1bot-mirai-capabilities-beyond-ddos)

### MCP Server Enterprise Secret Exposure
- **Description**: Model Context Protocol servers exposing enterprise secrets through plaintext configuration files, over-permissioned access, and prompt injection, often before security teams are aware the servers are running.
- **Impact**: Silent exposure of sensitive enterprise data and credentials to AI agents.
- **Status**: Architectural risk; no specific patch; requires configuration and governance controls.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — How MCP Servers Can Expose Enterprise Secrets](https://thehackernews.com/2026/08/how-mcp-servers-can-expose-enterprise.html)

### Expired Domain Hijacking (Dropcatch Domains)
- **Description**: Threat actors acquiring expired domains (50,400 in H1 2026, ~$7M spent) to inherit traffic and reputation, redirecting victims to scams and malware.
- **Impact**: Large-scale traffic redirection to malicious content; brand reputation abuse.
- **Status**: Ongoing campaign; no technical patch; requires domain monitoring and registration hygiene.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Hackers Spend Nearly $7 Million on Expired Domains to Redirect Traffic to Scams and Malware](https://thehackernews.com/2026/08/hackers-spend-nearly-7-million-on.html)

### Service Provider Vulnerability Bank Fraud
- **Description**: Vulnerability at an unnamed service provider exploited to withdraw funds from Commerzbank customer accounts, resulting in €30M fraud; four arrests in Brazil, three charged in Europe.
- **Impact**: Direct financial theft from bank customers via service provider compromise.
- **Status**: Law enforcement action taken; vulnerability details not disclosed.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

## Affected Systems and Products

- **GitLab Community Edition and Enterprise Edition**: All versions prior to security update addressing CVE-2026-19478
- **Forminator Forms WordPress Plugin**: Versions prior to patched release; 600,000+ active installations affected
- **Microsoft Active Directory Certificate Services (Enterprise CA)**: Domain-joined environments with standard user accounts; CVE-2026-54121
- **Microsoft Defender**: Versions affected by ShieldBreak zero-day (CVE-2026-69414); patch in development
- **VMware vCenter Server**: Versions vulnerable to CVE-2026-59310 directory traversal; patched by Broadcom
- **SAP Commerce Cloud**: Instances with default authentication client misconfiguration; CVE-2026-58231 patched
- **Apple macOS**: Versions with Screen Sharing enabled and exposed to internet; CVE-2026-65400 patched
- **Snowflake snowflake-connector-net Repository**: Public GitHub repository with vulnerable `.github/workflows/jira_issue.yml`
- **Android Devices with Unisoc Modem Firmware**: Devices supporting VoLTE video calls; no vendor fix available
- **Linux-based Edge/Gateway Devices**: Routers, IoT gateways, and embedded devices targeted by Evooo1Bot (Mirai-based)
- **MCP (Model Context Protocol) Servers**: Enterprise AI agent integrations with plaintext configs and excessive permissions
- **Expired/Deleting Domains**: Domains in redemption period or recently dropped; acquired for malicious redirection
- **Service Provider Infrastructure**: Unnamed provider whose flaw enabled Commerzbank fraud

## Attack Vectors and Techniques

- **GraphQL API Abuse**: Unauthenticated mutation operations against public project endpoints in GitLab
- **Malicious File Upload RCE**: PHP file upload bypassing authentication in Forminator WordPress plugin
- **Certificate Authority Privilege Escalation**: Standard user exploiting CA misconfiguration to gain Domain Controller equivalence (Certighost)
- **Security Product Bypass**: Zero-day exploitation of Microsoft Defender internals (ShieldBreak) to evade detection
- **Directory Traversal to RCE**: Path manipulation in VMware vCenter leading to arbitrary code execution
- **Default Authentication Client Abuse**: Unauthenticated exploitation of pre-configured auth client in SAP Commerce Cloud
- **Screen Sharing Authentication Bypass**: Network-adjacent attacker exploiting macOS Screen Sharing flaw (CVE-2026-65400)
- **GitHub Actions Workflow Injection**: Crafted issue titles/payloads triggering command injection in CI/CD pipeline
- **VoLTE Protocol Exploit Chain**: Two-stage baseband-to-kernel exploit delivered via video call signaling
- **Known Vulnerability Exploitation at Scale**: Automated scanning and exploitation of disclosed flaws for botnet recruitment (Evooo1Bot)
- **AI Agent Configuration Exposure**: Plaintext secrets, excessive scopes, and prompt injection in MCP server deployments
- **Domain Lifecycle Hijacking**: Automated registration of expired domains to inherit SEO/traffic for malware distribution
- **Service Provider Supply Chain Compromise**: Exploitation of third-party service flaw to access banking infrastructure
- **DNS and Google Apps Script C2**: Covert command-and-control blending with legitimate traffic (Cavern framework)
- **Babuk-Derived Ransomware Deployment**: Custom encryptor deployed post-exploitation via VMware vCenter flaw
- **Cryptominer Deployment**: Monero miner installed on compromised internet-exposed Macs
- **SOCKS5 Proxy Enrollment**: Compromised devices converted to persistent traffic relay nodes (Evooo1Bot)
- **Credential Theft and Reverse SOCKS**: Post-exploitation modules for lateral movement and persistence

## Threat Actor Activities

- **Suspected China-Nexus APT**: Actively exploiting CVE-2026-59310 (VMware vCenter) to deploy Babuk-derived ransomware; attributed by cybersecurity researchers
- **Iranian Nation-State Actors (Cavern/Cav3rn Operators)**: Evolving C2 framework using DNS tunneling and Google Apps Script for stealthy communications targeting Israeli entities; monitored by Kaspersky since December 2025
- **Clop Ransomware Gang**: Claiming breaches of Philips and General Electric (GE); investigating data theft claims by both companies
- **Nightmare Eclipse**: Security researcher who disclosed ShieldBreak zero-day (CVE-2026-69414) in Microsoft Defender
- **Evooo1Bot Operators**: Deploying Mirai-derived modular botnet with exploitation modules, credential theft, and SOCKS5 proxy capabilities; targeting internet-facing Linux gateways globally
- **Azure Credential Thief**: Threat actor selling 3.6 million alleged Azure account records from Fortune 500 companies; initial access via compromised credentials
- **Dropcatch Domain Operators**: Organized acquisition of 50,400 expired domains in H1 2026 (~$7M investment) for traffic redirection to scams and malware
- **Bank Fraud Syndicate**: Four individuals arrested in Brazil, three charged in Europe for €30M Commerzbank fraud via service provider vulnerability exploitation
- **SSD Secure Disclosure**: Researchers publishing Unisoc VoLTE exploit chain (two-stage, March and August 2026) achieving full Android kernel access
- **Wiz Researchers**: Disclosed Snowflake GitHub Actions workflow injection vulnerability in public repository
- **AmnesiaStealer Operators**: Distributing macOS information stealer via ClickFix attacks with interactive browser session hijacking capability