---
schema_version: 2
report_date: 2026-09-26
generated_at: 2026-09-26T20:55:25Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-26/
---
# Exploitation Report

## Executive Summary

Threat actors are actively exploiting multiple critical vulnerabilities across enterprise software platforms, with Oracle PeopleSoft, Microsoft SharePoint, and Roundcube Webmail facing confirmed in-the-wild attacks. The ShinyHunters extortion gang has resumed mass exploitation of CVE-2026-35273 in Oracle PeopleSoft using a URL-encoding technique to bypass web application firewalls, deploying web shells on vulnerable servers globally. Simultaneously, CISA has added a SharePoint code injection flaw (CVE-2026-65660) and a MikroTik RouterOS vulnerability to its Known Exploited Vulnerabilities catalog, while Canadian authorities warn of active exploitation of a pre-authentication SQL injection in Roundcube Webmail (CVE-2026-48842). A critical authentication bypass in WSO2 products (CVE-2026-5430) is also being exploited according to CISA.

Supply chain and infrastructure compromises continue to escalate. The Mini Shai-Hulud campaign has re-activated compromised GitHub Actions that were briefly re-enabled by their maintainer, resuming execution of malicious code in downstream CI/CD pipelines. Suspected North Korean actors compromised Bitget's backend infrastructure, stealing $351.6 million from hot and warm wallets. Kiteworks received credible threat intelligence of an imminent zero-day attack, prompting an emergency shutdown advisory. Meanwhile, the ShinyHunters group separately compromised the Clop ransomware gang's leak site through an unpatched Grav CMS path traversal flaw, demonstrating cross-group targeting.

New malware capabilities are emerging across platforms. The Lunex Stealer MaaS platform abuses a vulnerable AMD driver to disable security monitoring and steal browser credentials via ClickFix-style social engineering targeting Ukrainian users. PamStealer macOS malware has added server-side payload decryption and multi-layer persistence using JXA droppers. An unauthenticated CSRF flaw in the Elementor WordPress plugin (CVSS 8.8, no CVE assigned) allows admin account takeover when an administrator clicks a crafted link. These developments underscore the expanding attack surface across enterprise applications, development pipelines, and endpoint environments.

## Active Exploitation Details

### Oracle PeopleSoft CVE-2026-35273 Remote Code Execution
- **Description**: A critical unauthenticated remote code execution vulnerability in Oracle PeopleSoft (CVSS 9.8) that was initially exploited as a zero-day. Attackers are using a URL-encoding trick to bypass web application firewall rules designed to mitigate the flaw.
- **Impact**: Unauthenticated remote code execution leading to web shell deployment and full server compromise.
- **Status**: Actively exploited in widespread campaigns; patch available from Oracle.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint CVE-2026-65660 Code Injection
- **Description**: A code injection vulnerability in Microsoft Office SharePoint (CVSS 8.8) that allows remote code execution.
- **Impact**: Remote code execution on SharePoint servers.
- **Status**: Actively exploited in the wild; added to CISA Known Exploited Vulnerabilities catalog.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html), [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Roundcube Webmail CVE-2026-48842 Pre-Auth SQL Injection
- **Description**: A pre-authentication SQL injection vulnerability in the virtuser_query plugin of Roundcube Webmail versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1. The flaw stems from a preg_replace() backslash handling issue.
- **Impact**: Pre-authentication SQL injection leading to potential data exfiltration, authentication bypass, or remote code execution.
- **Status**: Actively exploited in the wild; patches available in versions 1.6.16 and 1.7.1.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-48842
- **Reporting**: [The Hacker News — Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)

### WSO2 Authentication Bypass CVE-2026-5430
- **Description**: A critical authentication bypass vulnerability affecting multiple products from enterprise software provider WSO2.
- **Impact**: Authentication bypass allowing unauthorized access to WSO2 product instances.
- **Status**: Actively exploited in attacks; CISA has issued a warning.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Elementor WordPress Plugin CSRF Vulnerability
- **Description**: A cross-site request forgery (CSRF) vulnerability in the Elementor Website Builder WordPress plugin that allows unauthenticated attackers to create rogue administrator accounts when an admin clicks a crafted link.
- **Impact**: Full site takeover via unauthorized administrator account creation.
- **Status**: Unpatched as of reporting; no CVE identifier assigned yet.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### Grav CMS Path Traversal Vulnerability
- **Description**: An unauthenticated path traversal vulnerability in Grav CMS that was unpatched at the time of exploitation.
- **Impact**: Server compromise and defacement; used to hack the Clop ransomware gang's data leak site.
- **Status**: Exploited in targeted attack; patch status unclear.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Mini Shai-Hulud GitHub Actions Supply Chain Compromise
- **Description**: Two third-party GitHub Actions (actions-cool/issues-helper and actions-cool/maintain-one-comment) were compromised during the May 2026 Mini Shai-Hulud campaign, re-enabled by their maintainer, and remained accessible with malicious code for over a week.
- **Impact**: Malicious code execution in CI/CD pipelines of repositories using the compromised actions.
- **Status**: Repositories disabled for a second time after re-activation; malicious payloads were active.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/), [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

### Kiteworks Potential Zero-Day Threat
- **Description**: Kiteworks (formerly Accellion) received credible threat intelligence from federal authorities indicating a threat actor may attempt to target Kiteworks systems, prompting an emergency shutdown advisory.
- **Impact**: Potential compromise of secure file-sharing systems; specific vulnerability not publicly disclosed.
- **Status**: Threat intelligence indicates imminent attack; no confirmed exploitation reported.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyber Attack](https://thehackernews.com/2026/09/kiteworks-urges-customers-to-shut-down.html), [Bleeping Computer — Kiteworks urges 6-hour server shutdown over potential zero-day attacks](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)

### MikroTik RouterOS Vulnerability
- **Description**: A vulnerability in MikroTik RouterOS added to CISA's Known Exploited Vulnerabilities catalog alongside the SharePoint flaw.
- **Impact**: Network device compromise; specific impact details not provided in source excerpts.
- **Status**: Actively exploited in the wild per CISA KEV addition.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

## Affected Systems and Products

- **Oracle PeopleSoft**: Vulnerable servers running unpatched versions affected by CVE-2026-35273; global targeting across multiple sectors.
- **Microsoft SharePoint**: On-premises SharePoint servers vulnerable to CVE-2026-65660 code injection.
- **MikroTik RouterOS**: RouterOS devices with unpatched vulnerability; specific versions not detailed in sources.
- **Roundcube Webmail**: Versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1 vulnerable to CVE-2026-48842 pre-auth SQL injection.
- **WSO2 Products**: Multiple enterprise products from WSO2 affected by CVE-2026-5430 authentication bypass.
- **Adobe Commerce**: Referenced in CISA warning alongside SharePoint and WSO2 flaws; specific vulnerability not detailed in excerpts.
- **Elementor WordPress Plugin**: WordPress sites using vulnerable versions of Elementor Website Builder plugin.
- **Grav CMS**: Unpatched installations vulnerable to unauthenticated path traversal.
- **Kiteworks Secure File Sharing**: On-premises Kiteworks appliances potentially targeted by imminent zero-day attack.
- **GitHub Actions (actions-cool)**: Repositories using actions-cool/issues-helper and actions-cool/maintain-one-comment actions compromised in Mini Shai-Hulud campaign.
- **AMD GPU Drivers**: Vulnerable driver versions abused by Lunex Stealer to disable security monitoring on Windows systems.
- **macOS Systems**: Targeted by PamStealer malware with JXA-based droppers and server-side payload decryption.
- **Bitget Cryptocurrency Exchange**: Backend infrastructure compromised, hot and warm wallets drained.

## Attack Vectors and Techniques

- **WAF Bypass via URL Encoding**: ShinyHunters uses URL-encoding tricks to evade web application firewall rules mitigating CVE-2026-35273, enabling continued exploitation of Oracle PeopleSoft.
- **ClickFix-Style Social Engineering**: Lunex Stealer operators deploy fake CAPTCHA pages and Cloudflare verification checks on compromised Ukrainian websites to trick users into executing malicious PowerShell commands.
- **GitHub Actions Supply Chain Injection**: Mini Shai-Hulud campaign compromised third-party GitHub Action repositories, injecting malicious code that executes in downstream CI/CD pipelines when the actions are used.
- **CSRF via Crafted Administrative Links**: Elementor vulnerability exploited by luring authenticated administrators to click malicious links that trigger unauthorized admin account creation.
- **Unauthenticated Path Traversal**: Grav CMS flaw allows directory traversal without authentication, enabling file read/write and server compromise.
- **Pre-Authentication SQL Injection**: Roundcube virtuser_query plugin flaw exploited via preg_replace() backslash manipulation before authentication.
- **Authentication Bypass**: WSO2 products vulnerable to critical authentication bypass allowing unauthorized access.
- **Vulnerable Driver Exploitation (BYOVD)**: Lunex Stealer abuses a legitimate but vulnerable AMD driver to disable security monitoring tools and elevate privileges.
- **Server-Side Payload Decryption**: PamStealer macOS malware uses a server-side decryption chain where the main payload key material is only available from C2, preventing static analysis.
- **Backend Infrastructure Compromise**: Suspected North Korean actors achieved backend access to Bitget exchange systems, enabling unauthorized transfers from hot and warm wallets.
- **Web Shell Deployment**: Oracle PeopleSoft exploitation culminates in web shell deployment for persistent remote access.

## Threat Actor Activities

- **ShinyHunters**: Extortion gang conducting widespread Oracle PeopleSoft exploitation using WAF bypass techniques; separately compromised Clop ransomware gang's leak site via Grav CMS path traversal, defacing and forcing migration to new Tor address.
- **North Korean Threat Actors (Suspected)**: Attributed by Bitget to the $351.6 million cryptocurrency theft from hot and warm wallets following backend compromise on September 24, 2026.
- **Mini Shai-Hulud Operators**: Supply chain threat actors who compromised GitHub Actions in May 2026 campaign; payloads reactivated when maintainer re-enabled repositories, demonstrating persistence in software supply chain.
- **Lunex/Psychedelic Stealer Operators**: MaaS platform operators distributing stealer malware via compromised Ukrainian websites with ClickFix lures; abuse AMD driver vulnerability for defense evasion and credential theft.
- **PamStealer Operators**: macOS malware developers iterating on PamStealer with advanced anti-analysis (server-side decryption) and persistence (multi-layer, JXA-based) techniques.
- **Clop Ransomware Gang**: Victim of ShinyHunters intrusion; data leak site compromised via unpatched Grav CMS, forcing infrastructure migration.
- **Unknown Actors (Kiteworks Targeting)**: Federal threat intelligence indicates an unidentified threat actor planning imminent attacks against Kiteworks file-sharing appliances; possible zero-day exploitation.