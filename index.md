---
schema_version: 2
report_date: 2026-09-28
generated_at: 2026-09-28T04:44:55Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-28/
---
# Exploitation Report

## Executive Summary

Citrix has confirmed active exploitation of two critical NetScaler remote code execution zero-days (CVE-2026-88771 and CVE-2026-88772), with patches now available for both flaws plus six additional vulnerabilities. One of the NetScaler flaws affects every deployment on an impacted version, including default configurations, making immediate patching essential for all NetScaler ADC and Gateway administrators.

The ShinyHunters extortion group has intensified campaigns against Oracle PeopleSoft installations, leveraging a URL-encoding technique to bypass web application firewall protections for CVE-2026-35273 (CVSS 9.8). This critical unauthenticated RCE flaw, previously exploited as a zero-day, is now seeing renewed mass exploitation with web shell deployment across multiple sectors globally. Simultaneously, ShinyHunters compromised the Clop ransomware gang's leak site through an unpatched Grav CMS path traversal vulnerability.

CISA has added Microsoft SharePoint (CVE-2026-65660, CVSS 8.8) and MikroTik RouterOS vulnerabilities to its Known Exploited Vulnerabilities catalog, confirming active exploitation in the wild. A critical WSO2 authentication bypass (CVE-2026-5430) and Adobe Commerce flaws are also under active attack. Meanwhile, a high-severity CSRF vulnerability in the Elementor WordPress plugin (CVSS 8.8, no CVE assigned) enables unauthenticated admin account creation, and compromised GitHub Actions from the Mini Shai-Hulud campaign were re-enabled and executed malicious code for over a week.

## Active Exploitation Details

### Citrix NetScaler RCE Zero-Days (CVE-2026-88771, CVE-2026-88772)
- **Description**: Two critical remote code execution vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway. One vulnerability affects every deployment on an affected version, including those in default configuration.
- **Impact**: Unauthenticated remote code execution leading to full system compromise
- **Status**: Actively exploited in the wild; security updates released by Citrix on September 27, 2026 addressing both zero-days plus six additional flaws
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771, CVE-2026-88772
- **Reporting**: [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### Oracle PeopleSoft Unauthenticated RCE (CVE-2026-35273)
- **Description**: Critical security flaw in Oracle PeopleSoft allowing unauthenticated remote code execution with a CVSS score of 9.8. Initially exploited as a zero-day, now seeing renewed mass exploitation.
- **Impact**: Full server compromise, web shell deployment, data theft across multiple sectors globally
- **Status**: Actively exploited; WAF bypass technique using URL-encoding allows attackers to circumvent mitigations
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint Code Injection (CVE-2026-65660)
- **Description**: Code injection vulnerability in Microsoft Office SharePoint with CVSS score 8.8, added to CISA KEV catalog citing evidence of active exploitation.
- **Impact**: Remote code execution on SharePoint servers
- **Status**: Actively exploited in the wild; CISA KEV listing mandates federal agency remediation
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html), [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### WSO2 Authentication Bypass (CVE-2026-5430)
- **Description**: Critical authentication bypass vulnerability affecting multiple products from enterprise software provider WSO2.
- **Impact**: Authentication bypass leading to unauthorized access to WSO2 product deployments
- **Status**: Actively exploited in attacks per CISA warning
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Elementor WordPress Plugin CSRF
- **Description**: Cross-site request forgery vulnerability in Elementor Website Builder WordPress plugin allowing unauthenticated attackers to create rogue administrator accounts and take control of sites. CVSS score 8.8.
- **Impact**: Full site takeover via admin account creation when administrator clicks crafted link
- **Status**: Vulnerability disclosed with high severity; no CVE identifier assigned yet
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### MikroTik RouterOS Vulnerability
- **Description**: Security flaw in MikroTik RouterOS added to CISA KEV catalog with evidence of active exploitation.
- **Impact**: Router compromise enabling network interception, pivoting, and persistence
- **Status**: Actively exploited in the wild per CISA KEV listing
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### Grav CMS Path Traversal
- **Description**: Unauthenticated path traversal vulnerability in Grav CMS exploited to compromise the Clop ransomware gang's data leak site.
- **Impact**: Server compromise, site defacement, forced migration to new Tor address
- **Status**: Actively exploited; unpatched at time of Clop site compromise
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Mini Shai-Hulud GitHub Actions Supply Chain Compromise
- **Description**: Two third-party GitHub Actions (actions-cool/issues-helper and actions-cool/maintain-one-comment) compromised during May 2026 campaign, re-enabled by maintainer and executed malicious code for over a week.
- **Impact**: Malicious code execution in CI/CD pipelines of repositories using compromised actions
- **Status**: Payloads still active after re-enablement; actions disabled for second time
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/), [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: Vulnerability in Cloudflare Containers and Sandboxes allowing customers with Workers Paid accounts to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data exposure in multi-tenant container environment
- **Status**: Fixed by Cloudflare; no indication of active exploitation prior to fix
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

### Adobe Commerce Flaws
- **Description**: Vulnerabilities in Adobe Commerce actively exploited in attacks per CISA warning.
- **Impact**: E-commerce platform compromise, potential payment data theft
- **Status**: Actively exploited per CISA
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Kiteworks Potential Zero-Day Threat
- **Description**: Kiteworks (formerly Accellion) urging customers to shut down systems for 6-9 hours over credible threat intelligence from federal authorities indicating imminent cyber attack, potentially involving zero-day exploitation.
- **Impact**: Potential full system compromise of secure file-sharing infrastructure
- **Status**: Threat intelligence indicates imminent attack; no confirmed exploitation or CVE at time of reporting
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyber Attack](https://thehackernews.com/2026/09/kiteworks-urges-customers-to-shut-down.html), [Bleeping Computer — Kiteworks urges 6-hour server shutdown over potential zero-day attacks](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)

### Lunex Stealer / Psychedelic Stealer Malware Campaign
- **Description**: Malware-as-a-service platform (Lunex) distributing Psychedelic Stealer via compromised Ukrainian websites using ClickFix-style Cloudflare verification checks. Abuses AMD driver to disable security monitoring and steal browser credentials through a four-stage attack chain.
- **Impact**: Credential theft, security monitoring bypass, persistent access on Ukrainian-speaking users' systems
- **Status**: Active MaaS campaign with novel AMD driver abuse technique
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html)

### PamStealer macOS Malware Evolution
- **Description**: Updated PamStealer macOS malware featuring live C2 payload decryption via server-side chain, multi-layer persistence, and continued use of JavaScript for Automation (JXA) dropper mechanism with modified lure and delivery methods.
- **Impact**: Persistent macOS compromise, credential theft, evasion of static analysis through server-side decryption
- **Status**: Active malware development and deployment
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [The Hacker News — PamStealer macOS Malware Adds Live C2 Payload Decryption and Multi-Layer Persistence](https://thehackernews.com/2026/09/pamstealer-macos-malware-adds-live-c2.html)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All deployments on affected versions including default configurations; patches released September 27, 2026
- **Oracle PeopleSoft**: Installations vulnerable to CVE-2026-35273; WAF mitigations bypassable via URL-encoding
- **Microsoft SharePoint**: On-premises SharePoint servers vulnerable to CVE-2026-65660 code injection
- **MikroTik RouterOS**: RouterOS versions affected by actively exploited flaw (specific versions per CISA KEV)
- **WSO2 Products**: Multiple enterprise products including API Manager, Identity Server, and Enterprise Integrator affected by CVE-2026-5430
- **Adobe Commerce**: E-commerce platform installations with actively exploited vulnerabilities
- **Elementor Website Builder WordPress Plugin**: Versions prior to patched release; WordPress sites with plugin installed
- **Grav CMS**: Unpatched installations vulnerable to unauthenticated path traversal
- **GitHub Actions**: Repositories using actions-cool/issues-helper and actions-cool/maintain-one-comment actions
- **Cloudflare Containers and Sandboxes**: Workers Paid account environments on shared physical hosts (fixed)
- **Kiteworks Secure File Sharing**: All customer systems urged to shut down during specified maintenance windows
- **Windows Systems (Ukrainian-targeted)**: Compromised via fake CAPTCHA/ClickFix pages delivering Lunex Stealer
- **macOS Systems**: Targeted by updated PamStealer malware with enhanced persistence and C2 encryption

## Attack Vectors and Techniques

- **WAF Bypass via URL Encoding**: ShinyHunters using URL-encoding tricks to bypass web application firewall rules protecting Oracle PeopleSoft CVE-2026-35273, enabling continued exploitation despite mitigations
- **ClickFix-Style Social Engineering**: Fake CAPTCHA/Cloudflare verification pages on compromised Ukrainian websites tricking users into executing malicious commands (Lunex Stealer distribution)
- **AMD Driver Abuse for Defense Evasion**: Lunex Stealer leveraging legitimate AMD driver functionality to disable security monitoring tools and steal browser credentials
- **Supply Chain Compromise via GitHub Actions**: Mini Shai-Hulud campaign compromising third-party GitHub Actions, with maintainers inadvertently re-enabling malicious versions
- **Cross-Site Request Forgery (CSRF)**: Elementor WordPress plugin flaw allowing unauthenticated admin account creation when administrator visits crafted link
- **Unauthenticated Path Traversal**: Grav CMS flaw exploited to compromise Clop ransomware leak site without authentication
- **Server-Side Payload Decryption**: PamStealer using C2-controlled decryption chain to prevent static analysis of main payload
- **Multi-Layer Persistence**: PamStealer employing multiple persistence mechanisms on macOS for resilience
- **Cross-Tenant Container Data Recovery**: Cloudflare Containers flaw allowing residual data access from other tenants on shared hardware
- **Default Configuration Exploitation**: One Citrix NetScaler zero-day exploitable on default installations without special configuration

## Threat Actor Activities

- **ShinyHunters**: Extortion gang conducting widespread Oracle PeopleSoft exploitation (CVE-2026-35273) with WAF bypass techniques; compromised Clop ransomware gang's leak site via Grav CMS path traversal; linked to renewed mass exploitation campaign deploying web shells globally across multiple sectors
- **Clop Ransomware Gang**: Victim of ShinyHunters compromise; data leak server breached and defaced, forcing migration to new Tor address
- **Mini Shai-Hulud Campaign Operators**: Supply chain attackers who compromised GitHub Actions in May 2026; malicious payloads remained active after maintainer re-enabled repositories for over a week
- **Lunex MaaS Operators**: Malware-as-a-service platform distributing Psychedelic Stealer via compromised Ukrainian websites; employing novel AMD driver abuse for defense evasion and credential theft targeting Ukrainian-speaking users
- **PamStealer Developers**: Actively evolving macOS malware with server-side payload decryption, multi-layer persistence, and JXA-based delivery; modifying lures and delivery methods between variants
- **Unknown Threat Actor (Kiteworks Targeting)**: Federal intelligence authorities warned Kiteworks of imminent cyber attack potentially involving zero-day exploitation; actor unidentified
- **watchTowr**: Security firm whose research preceded Citrix's confirmation of NetScaler zero-day exploitation (referenced in The Hacker News coverage)