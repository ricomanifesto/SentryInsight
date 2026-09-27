---
schema_version: 2
report_date: 2026-09-27
generated_at: 2026-09-27T21:11:37Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-27/
---
# Exploitation Report

## Executive Summary

Citrix NetScaler appliances are under active exploitation via two critical remote code execution zero-days (CVE-2026-88771 and CVE-2026-88772), with one vulnerability affecting every deployment on impacted versions including default configurations. Citrix has released patches for both flaws alongside six additional vulnerabilities, and administrators are urged to apply updates immediately or take systems offline.

Simultaneously, the ShinyHunters extortion group has resumed mass exploitation of the critical Oracle PeopleSoft vulnerability CVE-2026-35273 (CVSS 9.8) using a URL-encoding technique to bypass web application firewall protections, deploying web shells across multiple sectors globally.

## Active Exploitation Details

### Citrix NetScaler RCE Zero-Days (CVE-2026-88771, CVE-2026-88772)
- **Description**: Two critical remote code execution vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway. One of the flaws affects every deployment on an affected version, including those in the default configuration. Both were exploited as zero-days before patches were available.
- **Impact**: Unauthenticated remote code execution leading to full appliance compromise, potential lateral movement, and data exfiltration.
- **Status**: Actively exploited in the wild; security updates released by Citrix on September 27 addressing both zero-days plus six additional flaws.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771, CVE-2026-88772
- **Reporting**: [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### Oracle PeopleSoft CVE-2026-35273
- **Description**: Critical unauthenticated remote code execution vulnerability in Oracle PeopleSoft (CVSS 9.8). Originally exploited as a zero-day, the flaw has seen renewed mass exploitation after threat actors developed a URL-encoding technique to bypass WAF rules that previously mitigated the issue.
- **Impact**: Unauthenticated remote code execution enabling web shell deployment, data theft, and persistent access to PeopleSoft environments.
- **Status**: Actively exploited in renewed campaign; WAF bypass technique allows exploitation despite prior mitigations.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Elementor WordPress Plugin CSRF
- **Description**: Cross-site request forgery vulnerability in the Elementor Website Builder WordPress plugin (CVSS 8.8) that allows unauthenticated attackers to create rogue administrator accounts when an admin clicks a crafted link. No CVE identifier has been assigned yet.
- **Impact**: Full site takeover via unauthorized administrator account creation.
- **Status**: Vulnerability disclosed with exploit details available; affects specific Elementor versions.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### Microsoft SharePoint RCE (CVE-2026-65660)
- **Description**: Code injection vulnerability in Microsoft Office SharePoint (CVSS 8.8) allowing remote code execution. Added to CISA's Known Exploited Vulnerabilities catalog based on evidence of active exploitation.
- **Impact**: Remote code execution in SharePoint environments leading to server compromise and potential domain escalation.
- **Status**: Actively exploited; listed in CISA KEV catalog.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html), [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### MikroTik RouterOS Flaw
- **Description**: Vulnerability in MikroTik RouterOS added to CISA's Known Exploited Vulnerabilities catalog citing evidence of active exploitation. Specific CVE identifier not provided in source articles.
- **Impact**: Router compromise enabling traffic interception, network pivoting, and persistent infrastructure access.
- **Status**: Actively exploited; listed in CISA KEV catalog.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### WSO2 Authentication Bypass (CVE-2026-5430)
- **Description**: Critical authentication bypass vulnerability affecting multiple products from enterprise software provider WSO2. CISA warns of active exploitation in attacks.
- **Impact**: Authentication bypass leading to unauthorized administrative access across WSO2 product deployments.
- **Status**: Actively exploited per CISA warning.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Adobe Commerce Flaw
- **Description**: Vulnerability in Adobe Commerce actively exploited in attacks per CISA warning. Specific CVE identifier not provided in source articles.
- **Impact**: E-commerce platform compromise enabling payment data theft, order manipulation, and customer data exposure.
- **Status**: Actively exploited per CISA warning.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: Vulnerability in Cloudflare Containers and Sandboxes allowing customers with Workers Paid accounts to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data leakage exposing sensitive customer information across shared infrastructure.
- **Status**: Fixed by Cloudflare; no indication of active exploitation in the wild.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

### Grav CMS Path Traversal
- **Description**: Unauthenticated path traversal vulnerability in Grav CMS used by the Clop ransomware gang's data leak site. Exploited by ShinyHunters to compromise and deface the leak site.
- **Impact**: File system access leading to site defacement and potential data exposure.
- **Status**: Exploited in targeted attack against Clop infrastructure; unpatched at time of exploitation.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Mini Shai-Hulud GitHub Actions Supply Chain Compromise
- **Description**: Two third-party GitHub Actions (actions-cool/issues-helper and actions-cool/maintain-one-comment) compromised during the May 2026 Mini Shai-Hulud campaign were re-enabled by their maintainer and remained accessible for over a week while still pointing to malicious code.
- **Impact**: Supply chain compromise affecting any repository using the poisoned Actions, enabling credential theft and malicious code execution in CI/CD pipelines.
- **Status**: Malicious payloads remained active after re-enabling; repositories since disabled again.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/), [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All deployments on affected versions including default configurations; patches released for CVE-2026-88771 and CVE-2026-88772 plus six additional flaws.
- **Oracle PeopleSoft**: Versions vulnerable to CVE-2026-35273; WAF mitigations bypassed via URL-encoding technique.
- **Elementor Website Builder WordPress Plugin**: Specific versions affected by unauthenticated CSRF flaw (CVSS 8.8); no CVE assigned.
- **Microsoft Office SharePoint**: Versions vulnerable to CVE-2026-65660 code injection flaw; active exploitation confirmed by CISA.
- **MikroTik RouterOS**: Versions affected by actively exploited flaw added to CISA KEV catalog.
- **WSO2 Products**: Multiple enterprise products affected by CVE-2026-5430 authentication bypass.
- **Adobe Commerce**: Versions affected by actively exploited flaw per CISA warning.
- **Cloudflare Containers and Sandboxes**: Workers Paid accounts on shared physical hosts; vulnerability fixed by Cloudflare.
- **Grav CMS**: Installations running unpatched versions vulnerable to unauthenticated path traversal.
- **GitHub Actions (actions-cool/issues-helper, actions-cool/maintain-one-comment)**: Compromised repositories in Mini Shai-Hulud supply chain campaign.

## Attack Vectors and Techniques

- **URL-Encoding WAF Bypass**: Attackers use URL-encoding tricks to evade web application firewall rules mitigating CVE-2026-35273, enabling continued exploitation of Oracle PeopleSoft servers.
- **Zero-Day Remote Code Execution**: Unauthenticated RCE against internet-facing Citrix NetScaler appliances, with one vulnerability exploitable in default configurations.
- **Cross-Site Request Forgery (CSRF)**: Crafted links trick authenticated administrators into creating rogue admin accounts in Elementor-powered WordPress sites.
- **Code Injection**: Exploitation of CVE-2026-65660 in Microsoft SharePoint for remote code execution.
- **Supply Chain Compromise**: Malicious code injected into legitimate GitHub Actions repositories, executed in downstream CI/CD pipelines when Actions are invoked.
- **Path Traversal**: Unauthenticated directory traversal in Grav CMS enabling file system access and site defacement.
- **Cross-Tenant Data Residue Recovery**: Exploitation of shared physical host isolation failure in Cloudflare Containers to access other customers' residual container data.
- **AMD Driver Abuse for Defense Evasion**: Lunex Stealer (Psychedelic Stealer) leverages AMD driver functionality to disable security monitoring and steal browser credentials via a four-stage attack chain initiated through fake CAPTCHA/ClickFix pages.
- **Server-Side Payload Decryption**: PamStealer macOS malware uses live C2 server-side decryption chains and multi-layer persistence via JXA droppers.

## Threat Actor Activities

- **ShinyHunters**: Extortion group conducting renewed mass exploitation of Oracle PeopleSoft CVE-2026-35273 using WAF bypass techniques across multiple sectors globally; also compromised Clop ransomware gang's leak site via Grav CMS path traversal flaw.
- **Mini Shai-Hulud Operators**: Supply chain campaign (May 2026) compromising third-party GitHub Actions; maintainers re-enabled compromised repositories leaving malicious payloads active for over a week.
- **Lunex MaaS Operators**: Malware-as-a-service platform distributing Psychedelic Stealer via compromised Ukrainian websites using ClickFix-style Cloudflare verification lures; targets Ukrainian-speaking users with AMD driver abuse for defense evasion.
- **PamStealer Operators**: Evolving macOS malware campaign adding live C2 payload decryption and multi-layer persistence; uses JavaScript for Automation (JXA) droppers with modified lures and delivery methods.
- **Unknown Actor Targeting Kiteworks**: Credible threat intelligence from federal authorities indicates potential imminent cyberattack against Kiteworks (formerly Accellion) secure file-sharing systems, prompting urged 6-9 hour server shutdowns.
- **Clop Ransomware Gang**: Data leak site compromised and defaced by ShinyHunters via Grav CMS vulnerability; forced migration to new Tor address.