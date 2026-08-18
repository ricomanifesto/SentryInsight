---
schema_version: 2
report_date: 2026-08-18
generated_at: 2026-08-18T09:43:33Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-18/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited in the wild, with CISA adding a critical Ray framework flaw to its Known Exploited Vulnerabilities catalog and a suspected China-nexus APT leveraging a recently patched VMware vCenter directory traversal (CVE-2026-59310) to deploy Babuk-derived ransomware. Microsoft is racing to patch the ShieldBreak zero-day (CVE-2026-69414) in Defender, while researchers have published a two-stage Unisoc VoLTE video call exploit chain that achieves full Android kernel access with no fix available from the chipset maker.

The Forminator WordPress plugin (600,000+ installations) harbors a critical unauthenticated RCE (CVE-2026-15748), and GitLab has patched a critical GraphQL flaw (CVE-2026-19478) allowing unauthenticated deletion of public projects. A Certighost vulnerability (CVE-2026-54121) enables standard domain users to escalate Enterprise CA privileges to Domain Controller level. Meanwhile, the Mirai-derived Evooo1Bot botnet actively exploits known flaws in edge devices to build SOCKS5 proxy infrastructure, and Iranian nation-state actors continue evolving the Cavern C2 framework using DNS and Google Apps Script for stealthy communications targeting Israeli entities.

Data breaches continue at scale: SafePal suffered an authorization flaw exposing 39,798 cryptocurrency hardware wallet customers' PII, Clop ransomware claims breaches at Philips and GE, a French tax authority breach affected 678,000 individuals, and a threat actor alleges theft of 3.6 million Azure account records from Fortune 500 companies via compromised credentials.

## Active Exploitation Details

### CVE-2026-59310 - VMware vCenter Directory Traversal
- **Description**: Severe directory-traversal vulnerability in VMware vCenter Server that allows malicious actors to execute arbitrary code remotely
- **Impact**: Remote code execution leading to ransomware deployment (Babuk-derived) and full server compromise
- **Status**: Newly patched by Broadcom; actively exploited in the wild by suspected China-nexus APT
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [The Hacker News — Suspected China-Nexus Actor Exploits VMware vCenter Flaw, Deploys Babuk-Derived Ransomware](https://thehackernews.com/2026/08/suspected-china-nexus-actor-exploits.html)

### CVE-2026-69414 - ShieldBreak Zero-Day in Microsoft Defender
- **Description**: Zero-day vulnerability in Microsoft Defender disclosed by security researcher "Nightmare Eclipse" that bypasses Defender protections
- **Impact**: Security control bypass enabling malware execution and persistence evasion
- **Status**: Microsoft working on patch; not yet released as of reporting
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — Microsoft working on Defender patch for ShieldBreak zero-day](https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/)

### Ray Framework Critical Browser-Based RCE
- **Description**: Critical flaw in Ray, an open-source Python-native distributed computing framework for AI/ML workloads, enabling remote code execution through browser-based attack vectors
- **Impact**: Remote code execution on Ray clusters via crafted web requests
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog with evidence of active exploitation; patch status varies by deployment
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE](https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html)

### Unisoc VoLTE Video Call Exploit Chain
- **Description**: Two-stage exploit chain achieving full Android kernel access on devices running Unisoc modem firmware through a VoLTE video call; second stage published August 17, 2026, following initial RCE disclosure in March 2026
- **Impact**: Complete kernel-level compromise requiring only that the victim answers a video call; no fix available from chipset maker
- **Status**: Exploit chain publicly disclosed; no vendor patch available
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [The Hacker News — Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access](https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html), [Dark Reading — Video Call Exploit Chains Two Flaws in Unisoc Modems](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)

### CVE-2026-15748 - Forminator WordPress Plugin Unauthenticated RCE
- **Description**: Critical unauthenticated remote code execution vulnerability in Forminator Forms WordPress plugin (600,000+ active installations) via malicious PHP file uploads
- **Impact**: Arbitrary code execution on vulnerable WordPress sites without authentication
- **Status**: Disclosed by security researcher; patch availability not specified in reporting
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-15748
- **Reporting**: [The Hacker News — Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

### CVE-2026-19478 - GitLab GraphQL Critical Flaw
- **Description**: Critical vulnerability in GitLab Community Edition and Enterprise Edition GraphQL API that, under certain conditions, allows unauthenticated attackers to remotely modify or delete public projects and user data
- **Impact**: Unauthenticated modification and deletion of public projects and associated user data
- **Status**: GitLab released security updates addressing the vulnerability
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [The Hacker News — Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

### CVE-2026-54121 - Certighost Enterprise CA Privilege Escalation
- **Description**: Vulnerability allowing a standard domain user to turn an Enterprise Certificate Authority into a Domain Controller, effectively escalating to Tier 0 identity infrastructure privileges
- **Impact**: Full Active Directory domain compromise through PKI privilege escalation
- **Status**: Patch available; described as "the easy part" while the underlying standing privilege issue remains
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-54121
- **Reporting**: [Bleeping Computer — Certighost and the Privilege Hiding in Your Certificate Authority](https://www.bleepingcomputer.com/news/security/certighost-and-the-privilege-hiding-in-your-certificate-authority/)

### Snowflake GitHub Actions Workflow Injection
- **Description**: GitHub Actions workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository exploitable through crafted GitHub issues to execute commands in workflows containing internal Jira credentials
- **Impact**: Command execution with access to internal Jira credentials in CI/CD pipeline
- **Status**: Disclosed by Wiz researchers; remediation status not specified
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)

### SafePal Authorization Flaw and Data Breach
- **Description**: Authorization flaw in an order-tracking plug-in exploited to expose names, email addresses, shipping addresses, phone numbers, and purchase details of approximately 39,798 customers; stolen data now offered for sale
- **Impact**: Large-scale PII and order data breach affecting cryptocurrency hardware wallet customers
- **Status**: Flaw exploited; affected customers notified individually; data circulating on threat actor markets
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers](https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html), [Bleeping Computer — SafePal data breach impacts 39,798 customers, stolen info for sale](https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/)

### Evooo1Bot Linux Botnet Campaign
- **Description**: Mirai-derived modular Linux botnet actively exploiting known vulnerabilities in internet-facing gateway devices to enroll them as SOCKS5 traffic relay nodes, with added credential theft, reverse SOCKS relays, and exploitation modules beyond DDoS
- **Impact**: Compromised devices become persistent attacker infrastructure for proxying, credential harvesting, and lateral movement
- **Status**: Active botnet campaign observed by multiple researchers since December 2025
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Dark Reading — Linux Botnet Evooo1Bot Expands Mirai Capabilities Well Beyond DDoS](https://www.darkreading.com/cyber-risk/linux-botnet-evooo1bot-mirai-capabilities-beyond-ddos), [The Hacker News — Evooo1Bot Linux Botnet Exploits Known Flaws to Turn Edge Devices Into SOCKS5 Proxies](https://thehackernews.com/2026/08/evooo1bot-linux-botnet-exploits-known.html), [Bleeping Computer — New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/)

### Clop Ransomware Campaign Against Philips and GE
- **Description**: Clop ransomware gang claims breaches of Philips and General Electric systems with data theft; both companies investigating the claims
- **Impact**: Potential large-scale data exfiltration from major industrial technology companies
- **Status**: Under active investigation by victim organizations; initial access vector not publicly disclosed
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Philips and GE investigating Clop ransomware data theft claims](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)

### Cavern C2 Framework (Iranian Nation-State)
- **Description**: Iranian nation-state command-and-control framework using DNS tunneling and Google Apps Script to blend into legitimate traffic, targeting entities in Israel with previously unreported components discovered through ongoing monitoring since December 2025
- **Impact**: Stealthy persistent access and command execution on compromised networks
- **Status**: Active evolution and deployment by tracked threat activity cluster
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic](https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html)

### AmnesiaStealer macOS Malware
- **Description**: New information-stealing malware targeting macOS users via ClickFix social engineering attacks, featuring a streaming module allowing interactive remote control of victim's web browser sessions
- **Impact**: Browser session hijacking, credential theft, and interactive attacker control
- **Status**: Newly discovered in-the-wild malware family
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — New AmnesiaStealer macOS malware hijacks browser sessions via remote control](https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/)

## Affected Systems and Products

- **VMware vCenter Server**: All versions prior to patched releases; directory traversal enables RCE (CVE-2026-59310)
- **Microsoft Defender**: Versions affected by ShieldBreak zero-day; patch in development (CVE-2026-69414)
- **Ray Distributed Computing Framework**: Open-source AI/ML clusters; browser-based RCE actively exploited
- **Android Devices with Unisoc Modem Firmware**: VoLTE video call exploit chain achieves full kernel access; no vendor fix available
- **Forminator Forms WordPress Plugin**: Versions prior to patch; 600,000+ active installations vulnerable to unauthenticated RCE (CVE-2026-15748)
- **GitLab Community Edition and Enterprise Edition**: Versions prior to security releases; GraphQL API allows unauthenticated project deletion (CVE-2026-19478)
- **Windows Server with Enterprise Certificate Authority**: Standard domain users can escalate CA to Domain Controller privileges (CVE-2026-54121)
- **Snowflake snowflake-connector-net Repository**: GitHub Actions workflow (.github/workflows/jira_issue.yml) vulnerable to issue-triggered command injection
- **SafePal Order-Tracking System**: Authorization flaw in plug-in exposed 39,798 customer records
- **Internet-Facing Gateway Devices (Routers, IoT)**: Linux-based edge devices targeted by Evooo1Bot for SOCKS5 proxy enrollment
- **Philips and GE Enterprise Systems**: Under investigation for Clop ransomware data theft claims
- **macOS Systems**: Targeted by AmnesiaStealer via ClickFix attacks with browser session hijacking
- **Israeli Organizational Networks**: Targeted by Iranian Cavern C2 framework using DNS and Google Apps Script

## Attack Vectors and Techniques

- **VoLTE Video Call Exploit Delivery**: Two-stage kernel exploit chain delivered via incoming video call; victim only needs to answer (Unisoc modems)
- **Browser-Based RCE via Ray Dashboard**: Crafted web requests to Ray cluster dashboards trigger remote code execution
- **Unauthenticated PHP Upload RCE**: Malicious PHP files uploaded through Forminator plugin endpoints without authentication
- **GraphQL API Abuse**: Unauthenticated GraphQL mutations modify/delete public GitLab projects under specific conditions
- **Enterprise CA Privilege Escalation**: Standard domain user exploits Certighost (CVE-2026-54121) to gain Domain Controller equivalence via PKI
- **GitHub Actions Workflow Injection**: Crafted GitHub issues trigger command execution in CI/CD pipelines with embedded credentials
- **Authorization Bypass in Order Tracking**: Flawed access controls in SafePal plug-in expose customer PII without authentication
- **Known Vulnerability Exploitation for Botnet Recruitment**: Evooo1Bot leverages unpatched flaws in edge devices for SOCKS5 proxy enrollment
- **DNS Tunneling with Google Apps Script**: Cavern C2 uses legitimate Google infrastructure for covert command and control communications
- **ClickFix Social Engineering**: AmnesiaStealer tricks macOS users into executing malicious commands via fake browser error pages
- **Compromised Credential Access**: Threat actor claims 3.6 million Azure records stolen using valid credentials against Fortune 500 companies
- **Third-Party Supply Chain Breach**: Pokémon Center customer data stolen via CEVA Logistics; French tax authority breached through DGFiP systems
- **Directory Traversal to RCE**: VMware vCenter path traversal (CVE-2026-59310) weaponized for arbitrary code execution and ransomware deployment

## Threat Actor Activities

- **Suspected China-Nexus APT**: Actively exploiting CVE-2026-59310 in VMware vCenter to deploy Babuk-derived ransomware; attributed by cybersecurity researchers
- **Clop Ransomware Gang**: Claiming breaches of Philips and General Electric with data theft; investigating by both companies
- **Iranian Nation-State Actors (Cavern/Cav3rn)**: Operating evolved C2 framework since December 2025 targeting Israeli entities using DNS and Google Apps Script for stealth
- **Evooo1Bot Operators**: Running Mirai-derived botnet campaign exploiting known flaws in edge devices to build SOCKS5 proxy infrastructure with credential theft capabilities
- **Nightmare Eclipse (Security Researcher)**: Disclosed ShieldBreak zero-day (CVE-2026-69414) in Microsoft Defender; Microsoft developing patch
- **SSD Secure Disclosure Researchers**: Published two-stage Unisoc VoLTE video call exploit chain achieving full Android kernel access
- **Wiz Researchers**: Disclosed Snowflake GitHub Actions workflow injection vulnerability in public repository
- **Unknown Threat Actor**: Selling 3.6 million alleged Azure account records from Fortune 500 companies obtained via compromised credentials
- **AmnesiaStealer Operators**: Distributing macOS info-stealer via ClickFix attacks with interactive browser session hijacking module
- **Data Brokers/Threat Actors**: Selling SafePal customer data (39,798 records) obtained through authorization flaw exploitation