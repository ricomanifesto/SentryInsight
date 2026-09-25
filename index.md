---
schema_version: 2
report_date: 2026-09-25
generated_at: 2026-09-25T16:59:23Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-25/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited in the wild, with two flaws added to CISA's Known Exploited Vulnerabilities catalog based on confirmed exploitation evidence. The Roundcube Webmail pre-authentication SQL injection (CVE-2026-48842) has escalated to active code injection attacks, while a WSO2 API Control Plane path traversal (CVE-2026-5430) and an Adobe Commerce vulnerability are under active exploitation. Simultaneously, North Korean threat actors executed a $351.6 million cryptocurrency heist against Bitget through backend compromise, and Iranian-linked actors compromised a dozen US water systems over the summer.

Supply chain attacks are intensifying with the Mini Shai-Hulud campaign re-activating compromised GitHub Actions, a placeholder domain (third-party.com) serving ClickFix lures across 1,700+ repositories, and Ukrainian business websites hijacked for Psychedelic Stealer distribution. New malware families including PamStealer on macOS, Carbonato targeting exposed Docker hosts, and SectopRAT hiding in legitimate applications demonstrate evolving persistence and evasion techniques. Unpatched OnePlus/Oppo Android flaws allow root access without permissions, while Ghost service accounts enable Microsoft 365 data theft in Chile.

## Active Exploitation Details

### Roundcube Webmail Pre-Auth SQL Injection (CVE-2026-48842)
- **Description**: A pre-authentication SQL injection vulnerability in the virtuser_query plugin of Roundcube Webmail, stemming from a preg_replace() backslash handling flaw that allows unauthenticated attackers to inject arbitrary SQL commands.
- **Impact**: Attackers can achieve remote code execution and full compromise of the webmail server without authentication, leading to email data theft, lateral movement, and persistent access.
- **Status**: Patched in versions 1.6.16 and 1.7.1; actively exploited in the wild per Canadian Centre for Cyber Security alerts.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-48842
- **Reporting**: [The Hacker News — Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html), [Bleeping Computer — Hackers now exploit critical Roundcube flaw in code injection attacks](https://www.bleepingcomputer.com/news/security/critical-roundcube-flaw-now-actively-exploited-in-code-injection-attacks/)

### WSO2 API Control Plane Path Traversal (CVE-2026-5430)
- **Description**: A path traversal vulnerability in WSO2 API Control Plane that allows attackers to access arbitrary files on the server filesystem, with a CVSS score of 9.8 indicating critical severity.
- **Impact**: Attackers can read sensitive configuration files, credentials, and potentially achieve remote code execution through file write primitives.
- **Status**: Added to CISA KEV catalog based on evidence of active exploitation; patch availability implied by KEV addition.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [The Hacker News — WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)

### Adobe Commerce/Magento Vulnerability
- **Description**: A critical security flaw impacting Adobe Commerce and Magento platforms, added to CISA KEV alongside the WSO2 vulnerability based on confirmed active exploitation.
- **Impact**: Potential for remote code execution, data exfiltration, and full e-commerce platform compromise affecting customer payment data and order systems.
- **Status**: Added to CISA KEV catalog with active exploitation confirmed; patches expected from Adobe.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)

### Mini Shai-Hulud GitHub Actions Supply Chain Compromise
- **Description**: Compromise of two GitHub Actions repositories (actions-cool/issues-helper and actions-cool/maintain-one-comment) during the May 2026 Mini Shai-Hulud campaign, which were disabled, then re-enabled and resumed malicious execution.
- **Impact**: Supply chain poisoning affecting all downstream workflows using these actions, enabling credential theft, repository compromise, and malware deployment across CI/CD pipelines.
- **Status**: Repositories disabled for second time; active malware execution observed after re-activation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

### Bitget Backend Compromise by North Korean Actors
- **Description**: Suspected North Korean threat actors compromised Bitget's backend infrastructure to authorize unauthorized transfers from hot and warm wallets, stealing $351.6 million in cryptocurrency.
- **Impact**: Massive financial loss, exposure of wallet infrastructure, and demonstration of sophisticated targeting of cryptocurrency exchange backend systems.
- **Status**: Active attack confirmed on September 24, 2026; cold wallets and majority of assets reportedly secure.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Says Suspected North Korean Hackers Stole $351.6M After Backend Compromise](https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html), [Bleeping Computer — Hackers steal $351.6 million in Bitget crypto exchange hack](https://www.bleepingcomputer.com/news/security/hackers-steal-3516-million-in-bitget-crypto-exchange-hack/)

### OnePlus/Oppo Android Root Exploit Chain
- **Description**: Two chained vulnerabilities in OnePlus's proprietary software (OxygenOS) allowing a malicious app with zero permissions to gain root access on OnePlus 15 and potentially many other OnePlus and OPPO devices.
- **Impact**: Full device compromise including access to all user data, keystroke logging, persistent rootkit installation, and bypass of Android security model.
- **Status**: Unpatched as of reporting; OnePlus acknowledged flaws affect multiple devices across OnePlus and OPPO brands.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [The Hacker News — Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions](https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html)

### ClickFix Campaigns (Ukrainian Sites & third-party.com)
- **Description**: Active ClickFix social engineering campaigns using fake Cloudflare verification pages on compromised Ukrainian business sites and the placeholder domain third-party.com (referenced in 1,700+ repositories) to deliver Psychedelic Stealer and ClickFix lures respectively.
- **Impact**: Credential theft, malware installation (Psychedelic Stealer), and supply chain risk to developers copying code from affected repositories.
- **Status**: Active campaigns observed; third-party.com serving malicious content to Windows browsers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Hacked Ukrainian Sites Serve Fake Cloudflare ClickFix Lures for Psychedelic Stealer](https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html), [The Hacker News — Placeholder third-party\[.\]com Referenced Across 1,700+ Repositories Now Serves Malicious Content](https://thehackernews.com/2026/09/placeholder-third-partycom-referenced.html)

### Ghost Service Account M365 Data Theft
- **Description**: Forgotten and lost service accounts in Microsoft 365 environments being exploited to bypass employee account controls and exfiltrate organizational data in Chile.
- **Impact**: Full M365 environment compromise including email, SharePoint, Teams data, and potential lateral movement to on-premises systems via hybrid identity.
- **Status**: Active data theft campaign observed; organizations with locked-down employee accounts still vulnerable.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Ghost Service Accounts Enable M365 Data Theft in Chile](https://www.darkreading.com/cyberattacks-data-breaches/ghost-service-accounts-m365-data-theft-chile)

### Iranian-Linked Water System Compromises
- **Description**: Iranian-linked threat actors compromised a dozen US water systems during summer 2026, representing critical infrastructure targeting.
- **Impact**: Potential disruption of water treatment and distribution, public health risks, and demonstration of critical infrastructure access capabilities.
- **Status**: Confirmed compromises during summer 2026; part of broader Iranian critical infrastructure targeting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — 3 Cyber Threats That Defined the Summer of 2026](https://www.darkreading.com/cyberattacks-data-breaches/3-cyber-threats-defined-summer-2026)

## Affected Systems and Products

- **Roundcube Webmail**: Versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1; Linux/Unix webmail servers
- **WSO2 API Control Plane**: All versions prior to patched release; API management platforms on Linux/Windows
- **Adobe Commerce / Magento**: Affected versions per Adobe security advisory; e-commerce platforms on Linux/Windows
- **GitHub Actions**: actions-cool/issues-helper and actions-cool/maintain-one-comment; CI/CD pipelines using these actions
- **Bitget Exchange Backend**: Hot/warm wallet authorization systems; cryptocurrency exchange infrastructure
- **OnePlus/Oppo Android Devices**: OnePlus 15 on OxygenOS and many other OnePlus/OPPO devices; Android mobile platform
- **Microsoft 365**: Tenants with orphaned/unmanaged service accounts; cloud identity and productivity platform
- **US Water Systems**: SCADA/ICS infrastructure at 12+ water treatment facilities; critical infrastructure OT environments
- **Ukrainian Business Websites**: Compromised legitimate websites serving as ClickFix distribution points; web servers
- **Developer Repositories**: 1,700+ repositories referencing third-party.com placeholder; software supply chain

## Attack Vectors and Techniques

- **Pre-Auth SQL Injection to RCE**: Unauthenticated database query manipulation via virtuser_query plugin leading to code execution on Roundcube servers
- **Path Traversal**: Directory traversal in WSO2 API Control Plane enabling arbitrary file read and potential write escalation
- **Supply Chain Compromise**: Malicious code injection into legitimate GitHub Actions repositories with subsequent re-activation after temporary takedown
- **Backend Infrastructure Compromise**: Direct targeting of cryptocurrency exchange wallet authorization systems, likely via credential theft or API abuse
- **Android Privilege Escalation Chain**: Chaining two OnePlus proprietary software flaws to achieve root from zero-permission app context
- **ClickFix Social Engineering**: Fake Cloudflare verification pages tricking users into executing Windows Installer commands from clipboard
- **Placeholder Domain Hijacking**: Registration of documentation placeholder domain (third-party.com) to serve malicious content to trusting repositories
- **Ghost Service Account Abuse**: Exploitation of unmanaged M365 service accounts with persistent credentials to bypass user account controls
- **Critical Infrastructure Intrusion**: Targeted compromise of water treatment SCADA systems by nation-state actors
- **AI Agent Instruction Smuggling**: Salesbleed technique exploiting Salesforce Agents to inject malicious instructions into Slack communications
- **Living-off-the-Land Persistence**: SectopRAT hiding inside legitimate applications; PamStealer using JXA dropper with server-side payload decryption
- **Exposed Docker Daemon Hijacking**: Carbonato malware targeting unauthenticated Docker APIs to deploy Hermes Agent AI framework
- **iCloud Calendar C2**: MacSync malware using public iCloud calendar events for payload delivery and command-and-control

## Threat Actor Activities

- **North Korean Threat Actors (suspected Lazarus/APT38)**: $351.6M Bitget cryptocurrency heist via backend compromise; IT worker infiltration campaigns targeting HR processes
- **Iranian-Linked Actors**: Compromise of 12 US water systems during summer 2026; critical infrastructure targeting campaign
- **Russian Hybrid Warfare Operators**: Cyber sabotage, disinformation, and drone attacks against European nations supporting Ukraine; coordinated cyber-physical operations
- **Mini Shai-Hulud Operators**: Supply chain campaign compromising GitHub Actions in May 2026 with reactivation in September; persistent access maintenance
- **ClickFix Campaign Operators**: Ukrainian website compromises for Psychedelic Stealer distribution; third-party.com placeholder domain hijack for developer targeting
- **PamStealer Developers**: macOS malware evolution with server-side decryption chain and multi-layer persistence; active development and deployment
- **Carbonato Botnet Operators**: New botnet targeting exposed Docker daemons to deploy AI agent framework; automated scanning and exploitation
- **SectopRAT Operators**: RAT revival using legitimate application masquerading; behavioral evasion focus
- **MacSync Operators**: macOS malware leveraging iCloud calendar infrastructure for C2; novel delivery mechanism
- **Ghost Account Exploiters**: M365 data theft in Chile via orphaned service accounts; identity hygiene exploitation
- **Salesbleed Operators**: Agentic AI abuse targeting Salesforce-Slack integration channels; cross-application instruction injection