---
schema_version: 2
report_date: 2026-09-08
generated_at: 2026-09-08T23:21:00Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-08/
---
# Exploitation Report

## Executive Summary

Microsoft's September 2026 Patch Tuesday set a new record with 966 to 974 vulnerabilities addressed across Windows and associated products, including two actively exploited zero-day vulnerabilities.

While the volume of fixes creates significant deployment challenges for defenders, the most immediately critical issue is the active exploitation of CVE-2026-75650, a maximum-severity (CVSS 10.0) zero-day in Adobe Commerce and Magento Open Source dubbed "StyleSmuggler." Attackers have leveraged this flaw since at least September 4 to deploy a Rust-based backdoor and PHP web shells, achieving persistent server compromise.

## Active Exploitation Details

### Adobe Commerce/Magento StyleSmuggler Zero-Day
- **Description**: A critical zero-day vulnerability (CVE-2026-75650) in Adobe Commerce and Magento Open Source, codenamed StyleSmuggler, allows unauthenticated attackers to execute arbitrary code and achieve full server compromise. The flaw resides in the handling of style/layout XML processing and was discovered under active exploitation by Sansec on September 4, 2026.
- **Impact**: Attackers gain remote code execution leading to full server takeover, deployment of persistent Rust-based backdoors and PHP web shells, and potential exfiltration of e-commerce data including payment information.
- **Status**: Actively exploited in the wild since September 4, 2026. Adobe released emergency patches for affected versions of Adobe Commerce (2.4.7-p1, 2.4.6-p6, 2.4.5-p8, 2.4.4-p9) and Magento Open Source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-75650
- **Reporting**: [Bleeping Computer — Adobe fixes critical Magento zero-day exploited to backdoor servers](https://www.bleepingcomputer.com/news/security/adobe-fixes-critical-magento-zero-day-exploited-to-backdoor-servers/), [The Hacker News — Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html)

### Microsoft September 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's record-breaking September 2026 Patch Tuesday addressed 966 vulnerabilities (974 per some counts), including two actively exploited zero-day vulnerabilities. Specific CVE identifiers for the two zero-days were not disclosed in the reporting.
- **Impact**: Active exploitation of two undisclosed zero-days affecting Windows operating systems and other Microsoft software, enabling potential remote code execution, privilege escalation, or security feature bypass.
- **Status**: Patches released as part of September 2026 Patch Tuesday (KB5122878 for Windows 10, KB5124008/KB5122880 for Windows 11). 58 additional vulnerabilities assessed as "more likely to be exploited."
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Krebs on Security — Microsoft Plugs Nearly 1,000 Security Holes](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/), [Dark Reading — Patch Tuesday Sets Another Record With 974 CVEs](https://www.darkreading.com/vulnerabilities-threats/patch-tuesday-another-record-974-cves), [Bleeping Computer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/), [Bleeping Computer — Microsoft releases Windows 10 KB5122878 extended security update](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-10-kb5122878-extended-security-update/), [Bleeping Computer — Windows 11 cumulative updates KB5124008 & KB5122880 released](https://www.bleepingcomputer.com/news/microsoft/windows-11-cumulative-updates-kb5124008-and-kb5122880-released/)

### F5 BIG-IP APM Linux Rootkit and Fileless Web Shell
- **Description**: Threat actors are breaching F5 BIG-IP APM devices to deploy a sophisticated Linux rootkit that intercepts PHP file loading operations and injects a fileless web shell directly into memory, avoiding disk writes and traditional detection mechanisms.
- **Impact**: Persistent, stealthy access to compromised F5 BIG-IP APM environments with the ability to execute arbitrary commands, intercept traffic, and maintain access across reboots without leaving forensic artifacts on disk.
- **Status**: Active exploitation observed. No specific CVE identifier provided in reporting; mitigation guidance from F5 not detailed in source articles.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers breach F5 BIG-IP APM devices to deploy Linux rootkit](https://www.bleepingcomputer.com/news/security/hackers-breach-f5-big-ip-apm-devices-to-deploy-linux-rootkit/)

### WeChat Zero-Click Account Takeover Worm
- **Description**: Researchers at Calif demonstrated a zero-click worm that takes over WeChat accounts via incoming calls on both iPhone and Android. The victim does not need to answer or interact with the call; the attacker only needs to be in the victim's WeChat contacts list. The flaw was reported to Tencent in July 2026.
- **Impact**: Full account takeover without user interaction, potential for worm-like propagation through contact lists, access to private messages, payments, and personal data.
- **Status**: Proof-of-concept demonstrated by researchers; reported to vendor (Tencent) in July 2026. Tencent has reportedly addressed the issue. No CVE identifier provided.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)

### FreeIPA/389 Directory Server Authentication Bypass Chain
- **Description**: A vulnerability chain in FreeIPA (the identity management system for Linux domains) and 389 Directory Server allows anonymous, unauthenticated clients to create a Kerberos identity of their choosing and add it to the administrators group, achieving full domain compromise.
- **Impact**: Complete compromise of Linux domain identity infrastructure, enabling attackers to create persistent administrative accounts, access all domain resources, and maintain long-term access.
- **Status**: Vulnerability disclosed by Red Hat; requires chaining two flaws (FreeIPA + 389 Directory Server). No CVE identifiers provided in reporting. Patch status not explicitly stated.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — FreeIPA Flaw Chain Lets Anonymous Clients Create Reusable Administrator Credentials](https://thehackernews.com/2026/09/freeipa-flaw-chain-lets-anonymous.html)

### ChatGPT Prompt Injection for Gmail Data Exfiltration
- **Description**: Check Point Research demonstrated a flaw in ChatGPT where a single planted instruction in a conversation could cause the AI to silently exfiltrate data from a user's connected Gmail account and pass it to an attacker-controlled ChatGPT account through a hidden channel, while appearing to answer the user's question normally.
- **Impact**: Covert exfiltration of email data and potentially other connected service data through AI prompt injection, bypassing user awareness and standard security controls.
- **Status**: Proof-of-concept demonstrated by researchers. No CVE identifier provided. OpenAI response not detailed in reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account](https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html)

### Liquid Network "Elements Bug" Bitcoin Theft
- **Description**: Attackers exploited a vulnerability in the Liquid Network's Elements sidechain software to steal nearly 4,000 BTC (approximately $47M at the time). The attackers returned 3,400 BTC the following day but continue to hold approximately 598.5 BTC. The network remains paused.
- **Impact**: Theft of substantial cryptocurrency reserves from a Bitcoin sidechain, undermining trust in the federation model and causing service disruption.
- **Status**: Active exploitation occurred September 6, 2026. Partial funds returned. Network paused. No CVE identifier provided for the "Elements Bug."
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [The Hacker News — Liquid Hackers Return 3,400 Bitcoin Taken via Elements Bug, Still Holding $47M in BTC](https://thehackernews.com/2026/09/liquid-hackers-return-3400-bitcoin.html)

### SAP Kernel "OVERPASS" Memory Corruption
- **Description**: SAP addressed 20 vulnerabilities in its September 2026 security updates, including a maximum-severity memory corruption flaw in the SAP Kernel code, codenamed "OVERPASS." Specific CVE identifier not provided in reporting.
- **Impact**: Memory corruption in the core SAP Kernel could allow remote code execution or denial of service in SAP enterprise systems.
- **Status**: Patches released in September 2026 SAP Security Patch Day. Exploitation status not explicitly confirmed in reporting.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — SAP warns of maximum severity 'OVERPASS' kernel vulnerability](https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/)

## Affected Systems and Products

- **Adobe Commerce / Magento Open Source**: Versions 2.4.7-p1, 2.4.6-p6, 2.4.5-p8, 2.4.4-p9 and earlier affected by CVE-2026-75650 (StyleSmuggler)
- **Microsoft Windows**: All supported versions (Windows 10, Windows 11 23H2/24H2/25H2, Windows Server 2016/2025) affected by September 2026 Patch Tuesday vulnerabilities (966-974 flaws)
- **F5 BIG-IP APM**: Access Policy Manager environments targeted for Linux rootkit deployment and fileless web shell injection
- **WeChat**: iOS and Android clients vulnerable to zero-click account takeover via incoming calls (patched per researcher report)
- **FreeIPA / 389 Directory Server / Red Hat Identity Management**: Linux domain identity systems vulnerable to anonymous admin credential creation chain
- **SAP Kernel**: Core SAP ERP and S/4HANA systems affected by "OVERPASS" memory corruption and 19 other vulnerabilities
- **Liquid Network / Elements**: Bitcoin sidechain software vulnerable to "Elements Bug" enabling unauthorized fund transfers
- **ChatGPT / OpenAI API**: Conversational AI platform with Gmail integration vulnerable to prompt injection data exfiltration
- **Google Workspace**: Third-party application integrations retaining excessive persistent access (contextual risk, not active exploit)

## Attack Vectors and Techniques

- **Multi-Hop Google Redirect Phishing**: Threat actors chain multiple Google services (Google.com, Google AMP, Google Translate, etc.) to create redirect chains that evade URL filtering and security analysis, ultimately delivering credential harvesting pages or ScreenConnect remote access installer payloads.
- **ClickFix Social Engineering**: Attackers use fake error messages, CAPTCHA challenges, or "verification" prompts to trick users into executing malicious PowerShell commands or scripts, establishing persistent access through legitimate system tools.
- **Autonomous AI Agent Credential Harvesting**: Financially motivated threat actors deploy multi-agent AI frameworks (observed by Google GTIG) that automate reconnaissance, vulnerability scanning, exploit delivery, and credential collection at scale, compromising thousands of credentials in under six hours.
- **Fileless Memory-Resident Web Shell**: Linux rootkit on F5 BIG-IP APM intercepts PHP `require`/`include` operations at the kernel/library level to inject malicious code directly into the PHP interpreter's memory space, achieving persistence without disk artifacts.
- **Zero-Click Contact-Based Propagation**: WeChat worm exploits a flaw in incoming call handling to execute code and take over accounts without any user interaction, spreading automatically through the victim's contact list.
- **Prompt Injection via Planted Instructions**: Malicious instructions embedded in ChatGPT conversations (shared links, imported contexts, or third-party plugins) cause the AI to silently exfiltrate connected service data (Gmail) to attacker-controlled channels.
- **Fake E-Commerce Infrastructure (DoppelCart)**: Operation of 119,000+ fraudulent domains mimicking legitimate retailers to harvest payment card data at scale, using automated deployment and SEO manipulation.
- **Rust Backdoor + PHP Web Shell Deployment**: Post-exploitation toolkit deployed via StyleSmuggler (CVE-2026-75650) combining a compiled Rust binary for persistent C2 with a PHP web shell for web-accessible command execution.

## Threat Actor Activities

- **ShinyHunters**: Extortion group claimed breach of Florida Department of Motor Vehicles "DAVID" database, exfiltrating over 200,000 driver records. Active in data theft and extortion campaigns targeting government and corporate databases.
- **Slim Spider**: Previously undocumented, financially motivated threat actor tracked by CrowdStrike targeting Brazilian financial institutions since at least March 2026. Demonstrates deep operational knowledge of Brazilian financial infrastructure including the instant payment system (PIX) and crypto custody operations.
- **DoppelCart Operators**: Organized fraud network operating 119,000+ fake e-commerce domains for payment card harvesting. Highly automated infrastructure deployment with sophisticated evasion of takedown efforts.
- **ClickFix Campaign Operators**: Multiple distinct threat groups employing the ClickFix social engineering technique (fake verification prompts leading to PowerShell execution) for initial access and persistent foothold establishment.
- **Google GTIG-Observed AI Agent Operators**: Diverse threat actors (financially motivated and state-aligned) leveraging autonomous multi-agent AI frameworks to automate the full attack lifecycle from reconnaissance to credential exfiltration at unprecedented speed and scale.
- **Liquid Network Attackers**: Unknown operators who exploited the "Elements Bug" in the Liquid Bitcoin sidechain to steal ~4,000 BTC, returning 3,400 BTC but retaining ~598.5 BTC. Motivation unclear (white-hat pressure, operational security, or partial return negotiation).
- **Calif Researchers**: Security firm that discovered and demonstrated the WeChat zero-click worm, responsibly disclosed to Tencent in July 2026. Not a threat actor but relevant to exploitation landscape.
- **Sansec Researchers**: Discovered active exploitation of StyleSmuggler (CVE-2026-75650) starting September 4, 2026, and attributed the Rust backdoor/PHP web shell deployment to this campaign.