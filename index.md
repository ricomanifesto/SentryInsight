---
schema_version: 2
report_date: 2026-09-27
generated_at: 2026-09-27T11:49:54Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-27/
---
# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are underway across diverse technology stacks. Two unpatched zero-day vulnerabilities in Citrix NetScaler ADC and Gateway appliances are being actively exploited for remote code execution, with no vendor fix available and administrators resorting to taking systems offline. Simultaneously, the ShinyHunters extortion group is conducting mass exploitation of a critical Oracle PeopleSoft flaw (CVE-2026-35273) using a novel WAF bypass technique, while CISA has added actively exploited SharePoint and MikroTik RouterOS vulnerabilities to its Known Exploited Vulnerabilities catalog. A suspected North Korean operation compromised cryptocurrency exchange Bitget for $351.6 million, and the Mini Shai-Hulud supply chain campaign has resurfaced with malicious GitHub Actions executing in CI/CD pipelines.

Additional active threats include the Lunex stealer malware abusing a legitimate AMD driver to disable security monitoring on Ukrainian targets, a new PamStealer macOS variant with enhanced persistence and encrypted C2 communications, and an unpatched Grav CMS path traversal flaw used to compromise the Clop ransomware gang's leak site. CISA also warns of active exploitation of a critical WSO2 authentication bypass (CVE-2026-5430) and Adobe Commerce flaws. Kiteworks has taken the extraordinary step of urging customers to shut down systems based on credible threat intelligence of an imminent zero-day attack.

## Active Exploitation Details

### Citrix NetScaler ADC/Gateway RCE Zero-Days
- **Description**: Two unpatched zero-day vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway appliances that allow unauthenticated remote code execution. Discovered by watchTowr on September 26, 2026, with Citrix yet to confirm the flaws or publish fixes.
- **Impact**: Full remote code execution on exposed NetScaler appliances, potentially leading to complete network compromise, data exfiltration, and lateral movement.
- **Status**: Actively exploited in the wild; no patches available. Some administrators have taken appliances offline as a precaution.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### Oracle PeopleSoft Unauthenticated RCE (CVE-2026-35273)
- **Description**: Critical security flaw in Oracle PeopleSoft (CVSS 9.8) allowing unauthenticated remote code execution. First exploited as a zero-day, now subject to renewed mass exploitation globally across multiple sectors.
- **Impact**: Unauthenticated attackers achieve remote code execution on PeopleSoft servers, enabling web shell deployment, data theft, and system compromise.
- **Status**: Actively exploited at scale. ShinyHunters using URL-encoding trick to bypass WAF mitigations. Oracle patches likely available given zero-day status has passed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint Code Injection (CVE-2026-65660)
- **Description**: Code injection vulnerability in Microsoft Office SharePoint (CVSS 8.8) added to CISA KEV catalog with evidence of active exploitation.
- **Impact**: Attackers can inject and execute arbitrary code on SharePoint servers, leading to full server compromise and access to organizational documents and data.
- **Status**: Actively exploited; added to CISA KEV on September 26, 2026. Patches available from Microsoft.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html), [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### MikroTik RouterOS Vulnerability
- **Description**: Security flaw in MikroTik RouterOS added to CISA KEV catalog citing active exploitation. Specific vulnerability details not disclosed in reporting.
- **Impact**: Compromise of MikroTik networking equipment, potentially enabling traffic interception, network pivoting, and persistent access.
- **Status**: Actively exploited; added to CISA KEV on September 26, 2026.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### WSO2 Authentication Bypass (CVE-2026-5430)
- **Description**: Critical authentication bypass vulnerability affecting multiple products from enterprise software provider WSO2. CISA warns of active exploitation in attacks.
- **Impact**: Attackers bypass authentication controls on WSO2 products (API Manager, Identity Server, etc.), gaining unauthorized administrative access.
- **Status**: Actively exploited per CISA. Patches available from WSO2.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Adobe Commerce Exploitation
- **Description**: Vulnerability in Adobe Commerce (formerly Magento) actively exploited in attacks, per CISA warning. Specific CVE not identified in available reporting.
- **Impact**: Compromise of e-commerce platforms, potential access to customer payment data, order information, and administrative controls.
- **Status**: Actively exploited; CISA warning issued.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Elementor WordPress Plugin CSRF
- **Description**: Cross-site request forgery vulnerability in Elementor Website Builder WordPress plugin (CVSS 8.8) allowing unauthenticated attackers to create rogue administrator accounts when an admin clicks a crafted link. No CVE assigned yet.
- **Impact**: Full site takeover via administrator account creation, enabling malware injection, data theft, and site defacement.
- **Status**: Proof-of-concept exists; no confirmed active exploitation reported. Vendor patch status unclear.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### Grav CMS Path Traversal
- **Description**: Unauthenticated path traversal vulnerability in Grav CMS, unpatched at time of exploitation. Used by ShinyHunters to compromise and deface the Clop ransomware gang's data leak site.
- **Impact**: Arbitrary file read/write on affected Grav CMS installations, leading to full site compromise.
- **Status**: Observed exploitation in targeted attack against Clop infrastructure. No patch available at time of reporting.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Mini Shai-Hulud GitHub Actions Supply Chain Compromise
- **Description**: Two third-party GitHub Actions (actions-cool/issues-helper and actions-cool/maintain-one-comment) compromised during May 2026 Mini Shai-Hulud campaign. Repositories re-enabled by maintainer but still pointing to malicious code, executing in CI/CD pipelines for over a week.
- **Impact**: Malicious code execution in CI/CD pipelines of any repository using the compromised actions, enabling credential theft, supply chain poisoning, and artifact tampering.
- **Status**: Active malicious execution confirmed; actions disabled for second time.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/), [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

### Lunex Stealer AMD Driver Abuse
- **Description**: Psychedelic Stealer malware (part of Lunex MaaS platform) abuses a legitimate AMD driver to disable security monitoring and steal browser credentials. Distributed via compromised Ukrainian websites using ClickFix-style fake Cloudflare verification pages.
- **Impact**: Security tool disablement, browser credential theft, potential follow-on compromise. Four-stage attack chain targeting Ukrainian-speaking users.
- **Status**: Active malware campaign observed by Ontinue.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html)

### PamStealer macOS Malware Evolution
- **Description**: New version of PamStealer macOS malware featuring live C2 payload decryption via server-side chain and multi-layer persistence mechanisms. Continues using JavaScript for Automation (JXA) dropper with modified lure and delivery.
- **Impact**: Persistent macOS compromise with encrypted payload delivery evading static analysis, credential theft, and sustained access.
- **Status**: New variant actively observed by Jamf Threat Labs.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — PamStealer macOS Malware Adds Live C2 Payload Decryption and Multi-Layer Persistence](https://thehackernews.com/2026/09/pamstealer-macos-malware-adds-live-c2.html)

### Kiteworks Imminent Zero-Day Threat
- **Description**: Kiteworks (formerly Accellion) received credible threat intelligence from federal authorities indicating imminent cyberattack potentially leveraging a zero-day vulnerability. Urged customers to shut down systems for 6-9 hours as precaution.
- **Impact**: Potential zero-day exploitation of Kiteworks secure file-sharing appliances, risking sensitive file transfer data.
- **Status**: Threat intelligence indicates imminent attack; no confirmed exploitation yet. Preventive shutdown recommended.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyber Attack](https://thehackernews.com/2026/09/kiteworks-urges-customers-to-shut-down.html), [Bleeping Computer — Kiteworks urges 6-hour server shutdown over potential zero-day attacks](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)

### Bitget Cryptocurrency Exchange Compromise
- **Description**: Suspected North Korean threat actors compromised Bitget's backend systems, stealing $351.6 million from hot and warm wallets on September 24, 2026. Cold wallets and majority of assets reportedly unaffected.
- **Impact**: Massive cryptocurrency theft, backend infrastructure compromise, potential ongoing access.
- **Status**: Confirmed breach with attributed threat actor; funds stolen.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Says Suspected North Korean Hackers Stole $351.6M After Backend Compromise](https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All versions potentially affected; no patch available. Appliances exposed to internet at highest risk.
- **Oracle PeopleSoft**: Versions vulnerable to CVE-2026-35273; widespread deployment across enterprise HR/finance systems.
- **Microsoft SharePoint**: Versions affected by CVE-2026-65660; on-premises and potentially cloud deployments.
- **MikroTik RouterOS**: Affected versions not specified; widely deployed in ISP and enterprise networking.
- **WSO2 Products**: Multiple products affected by CVE-2026-5430 including API Manager, Identity Server, and Enterprise Integrator.
- **Adobe Commerce (Magento)**: Affected versions not specified; e-commerce platforms globally.
- **Elementor Website Builder WordPress Plugin**: Versions prior to patched release; over 10 million active WordPress installations.
- **Grav CMS**: Unpatched versions vulnerable to path traversal; flat-file CMS deployments.
- **GitHub Actions (actions-cool/issues-helper, actions-cool/maintain-one-comment)**: Compromised versions still in use; any repository referencing these actions.
- **AMD Graphics Drivers**: Legitimate driver abused by Lunex stealer; Windows systems with AMD GPUs.
- **macOS Systems**: Targeted by PamStealer malware; versions supporting JXA execution.
- **Kiteworks Secure File Sharing Appliances**: All customer deployments; precautionary shutdown advised.
- **Bitget Cryptocurrency Exchange Backend**: Hot/warm wallet infrastructure compromised; cold storage unaffected.

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Direct exploitation of Citrix NetScaler zero-days, Oracle PeopleSoft (CVE-2026-35273), and SharePoint (CVE-2026-65660) without authentication.
- **WAF Bypass via URL Encoding**: ShinyHunters using double/multi-layer URL encoding to evade WAF rules blocking PeopleSoft exploit payloads.
- **Supply Chain Compromise**: Mini Shai-Hulud campaign compromising legitimate GitHub Actions maintainers to inject malicious code into downstream CI/CD pipelines.
- **ClickFix Social Engineering**: Fake Cloudflare verification/CAPTCHA pages tricking users into executing malicious PowerShell commands (Lunex distribution).
- **Legitimate Driver Abuse (BYOVD)**: Lunex stealer leverages signed AMD driver to disable security monitoring tools (EDR/AV) via kernel-level operations.
- **Server-Side Payload Encryption**: PamStealer uses live C2 decryption chain where payload key material only exists on attacker server, defeating static analysis.
- **Path Traversal**: Unauthenticated directory traversal in Grav CMS enabling arbitrary file access and site takeover.
- **Cross-Site Request Forgery (CSRF)**: Elementor flaw tricks authenticated admins into executing state-changing requests (admin account creation).
- **Authentication Bypass**: WSO2 CVE-2026-5430 allows circumventing authentication entirely on multiple enterprise integration products.
- **Backend Infrastructure Compromise**: North Korean actors targeting cryptocurrency exchange backend systems for wallet key access.
- **JavaScript for Automation (JXA) Droppers**: PamStealer uses macOS-native JXA for payload delivery and execution without traditional binaries.
- **Web Shell Deployment**: Post-exploitation persistence via web shells on compromised PeopleSoft and SharePoint servers.

## Threat Actor Activities

- **ShinyHunters**: Extortion gang conducting multi-faceted campaigns: (1) Mass exploitation of Oracle PeopleSoft CVE-2026-35273 with novel WAF bypass; (2) Compromise of Clop ransomware gang's leak site via Grav CMS path traversal; (3) Linked to renewed PeopleSoft exploitation per Google threat intelligence.
- **North Korean Threat Actors (suspected Lazarus Group)**: Backend compromise of Bitget cryptocurrency exchange resulting in $351.6M theft from hot/warm wallets on September 24, 2026. Demonstrates continued focus on cryptocurrency sector for revenue generation.
- **Mini Shai-Hulud Operators**: Supply chain threat actors who compromised GitHub Actions maintainers in May 2026. Malicious code persisted in repositories and re-activated when maintainer re-enabled access, affecting downstream CI/CD pipelines.
- **Lunex MaaS Operators**: Malware-as-a-service platform distributing Psychedelic Stealer via compromised Ukrainian websites. Four-stage attack chain using ClickFix social engineering, AMD driver abuse for defense evasion, and credential theft targeting Ukrainian-speaking users.
- **PamStealer Developers**: Active macOS malware development with evolving tradecraft: server-side payload encryption, multi-layer persistence, and JXA-based delivery. Indicates sustained investment in macOS targeting.
- **Unknown Actor (Citrix NetScaler)**: watchTowr discovered active exploitation of two NetScaler zero-days; actor identity not attributed. Exploitation suggests sophisticated capability given zero-day status.
- **Unknown Actor (Kiteworks Threat)**: Federal intelligence authorities provided credible threat intelligence of imminent attack on Kiteworks systems; actor not publicly identified. Potential zero-day exploitation anticipated.
- **Clop Ransomware Gang**: Victim of ShinyHunters attack; their leak site compromised and defaced via unpatched Grav CMS, forcing migration to new Tor address.