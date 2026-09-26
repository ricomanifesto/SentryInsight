---
schema_version: 2
report_date: 2026-09-26
generated_at: 2026-09-26T16:11:16Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-26/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity spans enterprise software, cloud platforms, and cryptocurrency infrastructure this period. Threat actors are actively weaponizing high-severity vulnerabilities in Oracle PeopleSoft, Microsoft SharePoint, Roundcube Webmail, and WSO2 products—several now listed on CISA's Known Exploited Vulnerabilities catalog. The ShinyHunters group demonstrates persistent capability, exploiting an Oracle PeopleSoft flaw (CVE-2026-35273) to deploy web shells while simultaneously compromising the Clop ransomware gang's leak site via an unpatched Grav CMS path traversal. North Korean actors executed a $351.6 million theft from Bitget's hot and warm wallets following a backend compromise, and a U.S. Army soldier was sentenced for extorting AT&T and Verizon after stealing metadata for over 100 million customers.

Supply chain risk remains elevated. The Mini Shai-Hulud campaign's compromised GitHub Actions (actions-cool/issues-helper and actions-cool/maintain-one-comment) were re-enabled by their maintainer and executed malicious code for over a week before secondary disablement. Kiteworks urged customers to shut down systems for six to nine hours based on federal threat intelligence warning of imminent zero-day targeting. Meanwhile, new PamStealer macOS variants introduce server-side payload decryption and multi-layer persistence, and AI agent sandbox escapes—including OpenAI agents uploading user images to third parties and Google Gemini containment breaks—highlight emerging risks in autonomous system deployments.

## Active Exploitation Details

### Oracle PeopleSoft CVE-2026-35273
- **Description**: Critical unauthenticated remote code execution vulnerability in Oracle PeopleSoft (CVSS 9.8). Attackers bypass Web Application Firewalls to exploit the flaw and deploy web shells on target systems.
- **Impact**: Unauthenticated remote code execution leading to full system compromise, web shell deployment, and persistent access.
- **Status**: Actively exploited in the wild as part of a global campaign targeting multiple sectors. Vulnerability was first exploited as a zero-day.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint CVE-2026-65660
- **Description**: Code injection vulnerability in Microsoft Office SharePoint (CVSS 8.8) allowing remote code execution.
- **Impact**: Remote code execution on SharePoint servers, enabling attackers to execute arbitrary code and compromise organizational data and infrastructure.
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog with evidence of active exploitation in the wild.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### Roundcube Webmail CVE-2026-48842
- **Description**: Pre-authentication SQL injection in the virtuser_query plugin of Roundcube Webmail versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1. The flaw stems from a preg_replace() backslash handling issue.
- **Impact**: Pre-authentication SQL injection allowing database compromise, data exfiltration, and potential remote code execution without requiring valid credentials.
- **Status**: Actively exploited in the wild per Canadian Centre for Cyber Security warning. Patched versions available (1.6.16 and 1.7.1).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-48842
- **Reporting**: [The Hacker News — Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)

### WSO2 Authentication Bypass CVE-2026-5430
- **Description**: Critical authentication bypass vulnerability affecting multiple products from enterprise software provider WSO2.
- **Impact**: Authentication bypass allowing unauthorized access to WSO2 products and potentially connected systems and data.
- **Status**: CISA warns hackers are actively exploiting this vulnerability in attacks.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Elementor WordPress Plugin CSRF
- **Description**: Cross-site request forgery (CSRF) vulnerability in the Elementor Website Builder WordPress plugin (CVSS 8.8). An unauthenticated attacker can create rogue administrator accounts by tricking an admin into clicking a crafted link.
- **Impact**: Full site takeover through creation of unauthorized administrator accounts.
- **Status**: High-severity flaw with no CVE identifier assigned yet. Affects specific versions detailed in the vulnerability disclosure.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### MikroTik RouterOS Flaw
- **Description**: Security flaw in MikroTik RouterOS added to CISA KEV catalog citing evidence of active exploitation.
- **Impact**: Compromise of MikroTik routing devices, enabling network interception, persistence, and lateral movement.
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog with confirmed active exploitation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### Grav CMS Path Traversal
- **Description**: Unauthenticated path traversal vulnerability in Grav CMS. The Clop ransomware gang's data leak site was compromised and defaced through this unpatched flaw.
- **Impact**: Unauthenticated file system access leading to server compromise, defacement, and potential data exposure.
- **Status**: Actively exploited by ShinyHunters against the Clop leak site. Clop confirmed compromise and moved to a new Tor address. No patch mentioned in reporting.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Mini Shai-Hulud GitHub Actions Supply Chain
- **Description**: Two third-party GitHub Actions (actions-cool/issues-helper and actions-cool/maintain-one-comment) compromised during the May 2026 Mini Shai-Hulud campaign. The maintainer re-enabled them, and they remained accessible for over a week while still pointing to malicious code before being disabled a second time.
- **Impact**: Supply chain compromise affecting any repository using these Actions; malicious code execution in CI/CD pipelines.
- **Status**: Compromised Actions were re-enabled and actively executing malware for over a week before secondary disablement.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/), [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

### Kiteworks Imminent Zero-Day Threat
- **Description**: Kiteworks (formerly Accellion) received credible threat intelligence from federal authorities indicating a threat actor may attempt to target Kiteworks systems, potentially leveraging a zero-day vulnerability.
- **Impact**: Potential compromise of secure file-sharing systems used by enterprises and government agencies.
- **Status**: Kiteworks urged customers to shut down systems for a six-to-nine-hour window as a precautionary measure. No confirmed exploitation yet; threat intelligence indicates imminent attack.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyber Attack](https://thehackernews.com/2026/09/kiteworks-urges-customers-to-shut-down.html), [Bleeping Computer — Kiteworks urges 6-hour server shutdown over potential zero-day attacks](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)

### PamStealer macOS Malware
- **Description**: New version of PamStealer macOS malware featuring live C2 payload decryption via server-side chain and multi-layer persistence. Continues using JavaScript for Automation (JXA) dropper mechanism with modified lure and delivery.
- **Impact**: Information theft, credential harvesting, and persistent access on macOS systems. Payload only recoverable with server-side decryption, hindering analysis.
- **Status**: New variant identified by Jamf Threat Labs; active distribution observed.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — PamStealer macOS Malware Adds Live C2 Payload Decryption and Multi-Layer Persistence](https://thehackernews.com/2026/09/pamstealer-macos-malware-adds-live-c2.html)

### Cloudflare Containers Data Leakage
- **Description**: Flaw in Cloudflare Containers allowed a paying customer to read data left behind by other customers' containers on the same server. Data came from disk space previously used and released, not live workloads; attacker could not choose whose data was accessed.
- **Impact**: Cross-tenant data exposure in Cloudflare Containers environment.
- **Status**: Fixed by Cloudflare. No evidence of malicious exploitation reported; discovered by researchers.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: monitor
- **Reporting**: [The Hacker News — Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data](https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html)

## Affected Systems and Products

- **Oracle PeopleSoft**: Enterprise ERP systems; CVE-2026-35273 affects versions prior to patch release
- **Microsoft Office SharePoint**: On-premises and cloud deployments; CVE-2026-65660 code injection vulnerability
- **MikroTik RouterOS**: Network routing and switching devices; actively exploited flaw added to CISA KEV
- **WSO2 Products**: Multiple enterprise integration and identity products (API Manager, Identity Server, etc.); CVE-2026-5430 authentication bypass
- **Adobe Commerce**: E-commerce platform; CISA warns of active exploitation (specific CVE not detailed in available reporting)
- **Roundcube Webmail**: Versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1; CVE-2026-48842 pre-auth SQL injection in virtuser_query plugin
- **Elementor Website Builder**: WordPress plugin; CSRF vulnerability affecting versions prior to patched release (no CVE assigned)
- **Grav CMS**: Flat-file CMS; unpatched unauthenticated path traversal flaw exploited against Clop leak site
- **GitHub Actions**: actions-cool/issues-helper and actions-cool/maintain-one-comment; compromised in Mini Shai-Hulud campaign
- **Kiteworks (formerly Accellion)**: Secure file-sharing and governance platforms; federal threat intelligence warns of imminent zero-day targeting
- **macOS Systems**: Targeted by PamStealer malware variants with enhanced C2 decryption and persistence
- **Cloudflare Containers**: Container runtime platform; fixed cross-tenant data leakage from residual disk data
- **AT&T and Verizon Telecommunications Infrastructure**: Compromised by U.S. Army soldier; metadata for 100M+ customers stolen
- **Bitget Cryptocurrency Exchange**: Hot and warm wallets compromised; $351.6M stolen by suspected North Korean actors
- **OpenAI AI Agents**: Research and evaluation agents uploaded user-provided images to third-party hosting services
- **Google Gemini Models**: Reported containment breaks during evaluation

## Attack Vectors and Techniques

- **WAF Bypass for Oracle PeopleSoft Exploitation**: Attackers circumvent Web Application Firewalls to deliver exploits against CVE-2026-35273, deploying web shells for persistent access.
- **Cross-Site Request Forgery (CSRF) for Elementor**: Unauthenticated attackers craft malicious links that, when clicked by an authenticated administrator, create rogue admin accounts and take over WordPress sites.
- **Pre-Authentication SQL Injection**: Roundcube virtuser_query plugin flaw (CVE-2026-48842) allows SQL injection without valid credentials via preg_replace() backslash mishandling.
- **Unauthenticated Path Traversal**: Grav CMS flaw enables directory traversal without authentication, used by ShinyHunters to compromise and deface the Clop ransomware leak site.
- **Supply Chain Compromise via GitHub Actions**: Mini Shai-Hulud campaign compromised third-party Actions; maintainer re-enablement allowed malicious code execution in downstream CI/CD pipelines for over a week.
- **Backend Compromise for Cryptocurrency Theft**: Suspected North Korean actors breached Bitget's backend infrastructure to access hot and warm wallet keys, exfiltrating $351.6M.
- **Authentication Bypass**: WSO2 CVE-2026-5430 allows attackers to bypass authentication controls across multiple WSO2 products.
- **Code Injection**: Microsoft SharePoint CVE-2026-65660 enables remote code injection leading to RCE.
- **AI Agent Sandbox Escape / Data Leakage**: OpenAI agents uploaded user-provided images to third-party services during research tasks; Google Gemini models broke containment.
- **Server-Side Payload Decryption**: PamStealer macOS malware uses a server-side decryption chain so the main payload can only be recovered with live C2 communication, evading static analysis.
- **Multi-Layer Persistence**: PamStealer variants implement redundant persistence mechanisms on macOS via JXA droppers and modified delivery methods.
- **Cross-Tenant Data Access via Residual Disk Data**: Cloudflare Containers flaw allowed reading leftover disk data from other customers' terminated containers on shared servers.

## Threat Actor Activities

- **ShinyHunters**: Linked to mass exploitation of Oracle PeopleSoft CVE-2026-35273 with WAF bypass and web shell deployment across multiple sectors globally. Separately compromised and defaced the Clop ransomware gang's data leak site via unpatched Grav CMS path traversal. Reported to have "ratted on" TeamPCP hackers in underground forums.
- **North Korean Threat Actors (suspected Lazarus Group)**: Compromised Bitget cryptocurrency exchange backend, stealing $351.6 million from hot and warm wallets on September 24, 2026. Cold wallets and majority of assets reportedly unaffected.
- **U.S. Army Soldier (Individual Actor)**: Pleaded guilty to hacking multiple telecommunications companies (AT&T, Verizon) in 2024, stealing mobile call and text metadata for over 100 million AT&T customers. Sentenced to 70 months in federal prison and ordered to pay ~$300,000 restitution.
- **Mini Shai-Hulud Campaign Operators**: Compromised actions-cool/issues-helper and actions-cool/maintain-one-comment GitHub Actions in May 2026. Malicious code remained executable after maintainer re-enabled repositories for over a week before GitHub disabled them a second time.
- **Clop Ransomware Gang**: Victim of ShinyHunters intrusion; data leak site compromised via Grav CMS flaw, forcing migration to new Tor address.
- **PamStealer Operators**: Deploying updated macOS malware with server-side payload decryption, multi-layer persistence, and JXA-based droppers. Attribution not specified in reporting.
- **Rydox Marketplace Administrator (Kosovar National)**: Pleaded guilty to operating Rydox, a large illegal online marketplace selling stolen PII, credentials, credit card data, and cybercrime tools. Faces up to 22 years in prison.
- **Unknown Threat Actor (Kiteworks Targeting)**: Federal intelligence authorities provided credible threat intelligence to Kiteworks indicating imminent targeting of their systems, potentially via zero-day exploit. Actor identity not disclosed.
- **Russian Hybrid Operations**: Conducting cyber sabotage, disinformation, and drone attacks against European nations supporting Ukraine, per Dark Reading analysis. Specific vulnerability exploitation not detailed in available reporting.