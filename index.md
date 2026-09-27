---
schema_version: 2
report_date: 2026-09-27
generated_at: 2026-09-27T16:46:55Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-27/
---
# Exploitation Report

## Executive Summary

Two unpatched Citrix NetScaler zero-day vulnerabilities enabling remote code execution are under active exploitation, prompting urgent warnings from security researchers and agencies for administrators to consider taking appliances offline until patches arrive. Citrix has not yet confirmed the flaws or released fixes, creating a critical exposure window for NetScaler ADC and Gateway deployments worldwide.

Multiple high-severity vulnerabilities have been added to CISA's Known Exploited Vulnerabilities catalog, confirming active exploitation of Microsoft SharePoint (CVE-2026-65660), MikroTik RouterOS, WSO2 products (CVE-2026-5430), and Adobe Commerce flaws. Simultaneously, the ShinyHunters extortion group has resumed mass exploitation of Oracle PeopleSoft (CVE-2026-35273, CVSS 9.8) using a URL-encoding technique to bypass WAF protections and deploy web shells across multiple sectors globally.

Supply chain and infrastructure threats continue to escalate: the Mini Shai-Hulud campaign compromised GitHub Actions that were subsequently re-enabled while still serving malicious code; Kiteworks urged emergency server shutdowns over credible threat intelligence of imminent zero-day attacks; and suspected North Korean actors stole $351.6 million from Bitget through a backend compromise. Meanwhile, the Lunex MaaS platform leverages an AMD driver abuse to disable security monitoring and steal credentials via ClickFix-style lures targeting Ukrainian users.

## Active Exploitation Details

### Citrix NetScaler ADC and Gateway Zero-Day RCE Vulnerabilities
- **Description**: Two unpatched zero-day vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway appliances that allow unauthenticated remote code execution. Security firm watchTowr reported active exploitation in the wild on September 26, 2026.
- **Impact**: Attackers can achieve full remote code execution on vulnerable NetScaler appliances, potentially leading to complete device compromise, lateral movement, and data exfiltration.
- **Status**: Actively exploited in the wild; Citrix has not confirmed the flaws or published fixes as of reporting. Patches expected next week. Some administrators have taken appliances offline as a precaution.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Citrix admins warned to shut down NetScalers over 2 exploited zero-days](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### Oracle PeopleSoft CVE-2026-35273
- **Description**: Critical unauthenticated remote code execution vulnerability in Oracle PeopleSoft (CVSS 9.8). Originally exploited as a zero-day, now subject to renewed mass exploitation.
- **Impact**: Unauthenticated remote code execution leading to full server compromise, web shell deployment, and potential data theft across affected PeopleSoft installations.
- **Status**: Actively exploited in widespread campaigns. ShinyHunters using URL-encoding WAF bypass technique to circumvent mitigations. Google has warned of renewed mass exploitation targeting multiple sectors globally.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint CVE-2026-65660
- **Description**: Code injection vulnerability in Microsoft Office SharePoint (CVSS 8.8) allowing remote code execution.
- **Impact**: Attackers can execute arbitrary code on SharePoint servers, leading to system compromise, data access, and potential lateral movement within organizational networks.
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog with evidence of active exploitation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html), [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### MikroTik RouterOS Vulnerability
- **Description**: Security flaw in MikroTik RouterOS actively exploited in the wild.
- **Impact**: Compromise of network routing infrastructure, potential traffic interception, network pivoting, and persistence at the network layer.
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog citing evidence of active exploitation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### WSO2 Authentication Bypass CVE-2026-5430
- **Description**: Critical authentication bypass vulnerability affecting multiple products from enterprise software provider WSO2.
- **Impact**: Attackers can bypass authentication controls on affected WSO2 products, gaining unauthorized access to administrative functions and sensitive data.
- **Status**: CISA warns hackers are actively exploiting this flaw in attacks.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Adobe Commerce Vulnerabilities
- **Description**: Security flaws in Adobe Commerce (formerly Magento) being exploited in attacks.
- **Impact**: Potential compromise of e-commerce platforms, theft of customer payment data, and injection of malicious code into storefronts.
- **Status**: CISA warns of active exploitation in attacks.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Elementor WordPress Plugin CSRF Vulnerability
- **Description**: Cross-site request forgery (CSRF) vulnerability in the Elementor Website Builder WordPress plugin (CVSS 8.8) allowing unauthenticated attackers to create rogue administrator accounts by tricking an admin into clicking a crafted link.
- **Impact**: Full site takeover through creation of unauthorized administrator accounts. No CVE identifier assigned yet.
- **Status**: Vulnerability details emerged; affects specific versions. No patch information provided in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: Vulnerability in Cloudflare Containers and Sandboxes allowing customers with Workers Paid accounts to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data leakage exposing sensitive information from other customers' container workloads.
- **Status**: Fixed by Cloudflare. No evidence of active exploitation reported.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

### Grav CMS Path Traversal Vulnerability
- **Description**: Unauthenticated path traversal vulnerability in Grav CMS used by the Clop ransomware gang's data leak site.
- **Impact**: Allowed ShinyHunters to compromise and deface the Clop leak site, forcing migration to a new Tor address.
- **Status**: Exploited in a targeted attack against Clop infrastructure. Unpatched at time of exploitation.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Kiteworks Potential Zero-Day Threat
- **Description**: Credible threat intelligence from federal authorities indicating imminent cyber attacks potentially leveraging zero-day vulnerabilities against Kiteworks (formerly Accellion) secure file-sharing systems.
- **Impact**: Potential compromise of sensitive file-sharing infrastructure used by enterprises and government agencies.
- **Status**: Kiteworks urged customers to shut down systems for 6-9 hours as precautionary measure. No confirmed exploitation or CVE assignment yet.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyber Attack](https://thehackernews.com/2026/09/kiteworks-urges-customers-to-shut-down.html), [Bleeping Computer — Kiteworks urges 6-hour server shutdown over potential zero-day attacks](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)

### GitHub Actions Mini Shai-Hulud Supply Chain Compromise
- **Description**: Two third-party GitHub Actions (actions-cool/issues-helper and actions-cool/maintain-one-comment) compromised during the May 2026 Mini Shai-Hulud campaign, re-enabled by maintainer while still pointing to malicious code for over a week.
- **Impact**: Supply chain compromise affecting any repositories using these Actions, leading to potential credential theft, code injection, and further lateral movement in CI/CD pipelines.
- **Status**: Actions disabled for second time after being accessible with malicious payload. Campaign originated May 2026.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/), [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

### Lunex Stealer / Psychedelic Stealer MaaS Platform
- **Description**: Malware-as-a-service platform (Lunex) distributing Psychedelic Stealer via compromised Ukrainian websites using ClickFix-style Cloudflare verification checks. Abuses AMD driver to disable security monitoring and steal browser credentials through a four-stage attack chain.
- **Impact**: Credential theft, security control evasion, persistent access targeting Ukrainian-speaking users.
- **Status**: Active distribution campaign observed by Ontinue. Novel AMD driver abuse technique for defense evasion.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html)

### PamStealer macOS Malware
- **Description**: Updated macOS information stealer featuring live C2 payload decryption via server-side chain, multi-layer persistence, and JavaScript for Automation (JXA) dropper mechanism.
- **Impact**: Credential theft, persistent access on macOS systems, evasion of static analysis through server-side decryption.
- **Status**: New variant identified by Jamf Threat Labs. Active development and deployment.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — PamStealer macOS Malware Adds Live C2 Payload Decryption and Multi-Layer Persistence](https://thehackernews.com/2026/09/pamstealer-macos-malware-adds-live-c2.html)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All versions pending vendor patch; appliances exposed to internet at highest risk
- **Oracle PeopleSoft**: Versions vulnerable to CVE-2026-35273; WAF-protected instances bypassable via URL-encoding technique
- **Microsoft SharePoint**: Versions affected by CVE-2026-65660 code injection vulnerability
- **MikroTik RouterOS**: Affected versions not specified in source; network infrastructure devices
- **WSO2 Products**: Multiple enterprise products affected by CVE-2026-5430 authentication bypass
- **Adobe Commerce**: E-commerce platform versions with actively exploited flaws
- **Elementor Website Builder WordPress Plugin**: Specific versions vulnerable to CSRF (CVE not yet assigned)
- **Cloudflare Containers and Sandboxes**: Workers Paid account customers on shared physical hosts; fixed by provider
- **Grav CMS**: Unpatched instances vulnerable to unauthenticated path traversal
- **Kiteworks (Accellion) Secure File Sharing**: All customer systems urged to shutdown; potential zero-day targeting
- **GitHub Actions**: actions-cool/issues-helper and actions-cool/maintain-one-comment repositories
- **AMD GPU Drivers**: Systems with vulnerable driver versions abused for security monitoring disablement
- **macOS Systems**: Targeted by PamStealer variant with JXA-based delivery

## Attack Vectors and Techniques

- **URL-Encoding WAF Bypass**: ShinyHunters uses URL-encoding trick to bypass web application firewall rules mitigating Oracle PeopleSoft CVE-2026-35273, allowing resumption of widespread exploitation
- **ClickFix-Style Social Engineering**: Fake CAPTCHA/Cloudflare verification pages lure victims into executing malicious commands (PowerShell, Run dialog) to deploy Lunex/Psychedelic Stealer
- **AMD Driver Abuse for Defense Evasion**: Lunex Stealer exploits legitimate AMD driver functionality to disable security monitoring tools and evade detection
- **Supply Chain Compromise via GitHub Actions**: Malicious code injected into third-party GitHub Actions (Mini Shai-Hulud campaign) executed in victim CI/CD pipelines when Actions re-enabled
- **Cross-Site Request Forgery (CSRF)**: Elementor flaw allows unauthenticated attacker to create admin accounts via crafted link clicked by legitimate administrator
- **Cross-Tenant Container Data Recovery**: Cloudflare Containers flaw allowed paid Workers customers to access residual memory/data from other tenants' containers on shared hardware
- **Unauthenticated Path Traversal**: Grav CMS flaw exploited to compromise Clop ransomware leak site infrastructure
- **Server-Side Payload Decryption**: PamStealer uses C2-controlled decryption chain so payload keys never reside on disk, evading static analysis
- **JavaScript for Automation (JXA) Droppers**: PamStealer and Lunex leverage macOS JXA for initial execution and persistence
- **Backend Infrastructure Compromise**: Suspected North Korean actors breached Bitget's backend systems to access hot/warm wallet private keys
- **Telecom Metadata Theft**: U.S. Army soldier exploited access to telecommunications infrastructure to steal call/text metadata for 100+ million AT&T customers

## Threat Actor Activities

- **ShinyHunters**: Extortion gang actively exploiting Oracle PeopleSoft CVE-2026-35273 with WAF bypass technique; compromised and defaced Clop ransomware leak site via Grav CMS path traversal; linked to renewed mass exploitation campaign targeting multiple sectors globally
- **North Korean Threat Actors (Suspected)**: Attributed to $351.6 million theft from Bitget cryptocurrency exchange via backend compromise of hot/warm wallets; cold wallets and majority assets reportedly unaffected
- **Mini Shai-Hulud Campaign Operators**: Compromised third-party GitHub Actions repositories in May 2026; malicious payloads remained accessible after maintainer re-enabled repositories; supply chain targeting of CI/CD pipelines
- **Lunex MaaS Operators**: Running malware-as-a-service platform distributing Psychedelic Stealer via compromised Ukrainian websites; employing ClickFix lures and novel AMD driver abuse for defense evasion; targeting Ukrainian-speaking users
- **PamStealer Developers**: Actively updating macOS info-stealer with advanced evasion (server-side decryption, multi-layer persistence) and JXA-based delivery; artifacts analyzed by Jamf Threat Labs
- **Unknown Actors Targeting Kiteworks**: Federal threat intelligence indicates imminent targeting of Kiteworks file-sharing systems; possible zero-day exploitation; credible enough to warrant emergency shutdown advisory
- **U.S. Army Soldier (Convicted)**: Pleaded guilty to hacking AT&T and Verizon, stealing mobile call/text metadata for 100+ million customers in 2024; sentenced to 70 months prison and $300K restitution
- **Clop Ransomware Gang**: Victim of ShinyHunters compromise; leak site defaced and forced to migrate to new Tor address after Grav CMS exploitation