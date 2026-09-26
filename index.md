---
schema_version: 2
report_date: 2026-09-26
generated_at: 2026-09-26T11:09:28Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-26/
---
# Exploitation Report

## Executive Summary

CISA has added multiple critical vulnerabilities to its Known Exploited Vulnerabilities catalog, confirming active exploitation of Microsoft SharePoint (CVE-2026-65660), WSO2 products (CVE-2026-5430), Adobe Commerce/Magento, and MikroTik RouterOS. The Canadian Centre for Cyber Security separately warned that a pre-authentication SQL injection in Roundcube Webmail (CVE-2026-48842) is being actively exploited in the wild. These represent confirmed, weaponized vulnerabilities requiring immediate patching across enterprise environments.

A high-severity CSRF flaw in the Elementor Website Builder WordPress plugin (CVSS 8.8, no CVE assigned) enables unauthenticated attackers to create rogue administrator accounts when an admin clicks a crafted link. Meanwhile, threat intelligence prompted Kiteworks to urge customers to shut down systems for six to nine hours over a potential zero-day targeting their secure file-sharing platform. The Clop ransomware gang's leak site was compromised via an unpatched Grav CMS path traversal flaw by ShinyHunters, demonstrating attacker-on-attacker activity and the risk of unpatched CMS installations.

Financially motivated and state-sponsored threat actors remain highly active. Suspected North Korean hackers stole $351.6 million from cryptocurrency exchange Bitget through a backend compromise. The Mini Shai-Hulud campaign resurfaced via compromised GitHub Actions repositories, while new macOS malware families (PamStealer, MacSync) and the Carbonato botnet leverage AI agents to hijack exposed Docker hosts. Russian hybrid cyber-physical operations continue targeting European nations supporting Ukraine.

## Active Exploitation Details

### Microsoft SharePoint Code Injection (CVE-2026-65660)
- **Description**: A code injection vulnerability in Microsoft Office SharePoint that allows remote code execution. Added to CISA KEV catalog based on evidence of active exploitation.
- **Impact**: Attackers can achieve remote code execution on affected SharePoint servers, potentially leading to full system compromise and lateral movement.
- **Status**: Actively exploited in the wild; patch available from Microsoft.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### WSO2 Path Traversal / Authentication Bypass (CVE-2026-5430)
- **Description**: A critical path traversal vulnerability in WSO2 API Control Plane (also described as an authentication bypass affecting multiple WSO2 products) with a CVSS score of 9.8. Added to CISA KEV catalog based on evidence of active exploitation.
- **Impact**: Attackers can bypass authentication and traverse file systems, potentially leading to unauthorized access, data exfiltration, and system compromise across WSO2 deployments.
- **Status**: Actively exploited in the wild; patches available from WSO2.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html), [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/), [The Hacker News — WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)

### Roundcube Webmail Pre-Auth SQL Injection (CVE-2026-48842)
- **Description**: A pre-authentication SQL injection in the virtuser_query plugin of Roundcube Webmail versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1. The issue stems from a preg_replace() backslash handling flaw. Canadian Centre for Cyber Security warns of active exploitation.
- **Impact**: Unauthenticated attackers can execute arbitrary SQL commands, leading to database compromise, data theft, and potential remote code execution.
- **Status**: Actively exploited in the wild; patched in versions 1.6.16 and 1.7.1.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-48842
- **Reporting**: [The Hacker News — Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)

### MikroTik RouterOS Vulnerability
- **Description**: A security flaw in MikroTik RouterOS added to CISA KEV catalog citing evidence of active exploitation. Specific vulnerability details not fully disclosed in source articles.
- **Impact**: Compromise of MikroTik networking devices, enabling network interception, pivoting, and persistence.
- **Status**: Actively exploited in the wild; patch status should be verified with MikroTik advisories.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### Adobe Commerce / Magento Vulnerability
- **Description**: A critical security flaw impacting Adobe Commerce and Magento added to CISA KEV catalog based on evidence of active exploitation. Specific CVE not fully disclosed in source articles.
- **Impact**: Potential compromise of e-commerce platforms, payment data theft, and customer information exposure.
- **Status**: Actively exploited in the wild; patches available from Adobe.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/), [The Hacker News — WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)

### Elementor Website Builder CSRF (WordPress Plugin)
- **Description**: A cross-site request forgery (CSRF) vulnerability in the Elementor Website Builder WordPress plugin (CVSS 8.8) that allows unauthenticated attackers to create rogue administrator accounts when an admin clicks a crafted link. No CVE identifier assigned yet.
- **Impact**: Full site takeover via administrator account creation, leading to content manipulation, malware distribution, and persistence.
- **Status**: Vulnerability disclosed with proof-of-concept; exploitation risk high due to social engineering vector; patch status should be verified with Elementor updates.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### Grav CMS Path Traversal
- **Description**: An unauthenticated path traversal vulnerability in Grav CMS that was unpatched at time of exploitation. Used by ShinyHunters to compromise and deface the Clop ransomware gang's data leak site.
- **Impact**: Arbitrary file read/write leading to site compromise, defacement, and potential server takeover.
- **Status**: Actively exploited (Clop leak site compromise); patch status unclear as flaw described as unpatched.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Kiteworks Potential Zero-Day
- **Description**: Kiteworks (formerly Accellion) received credible threat intelligence from federal authorities indicating a threat actor may attempt to target Kiteworks systems, prompting a 6-9 hour shutdown recommendation. Suggests a potential zero-day vulnerability.
- **Impact**: Potential compromise of secure file-sharing systems, data exfiltration, and supply chain impact.
- **Status**: Threat intelligence indicates imminent attack; no confirmed exploitation or patch at time of reporting.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyber Attack](https://thehackernews.com/2026/09/kiteworks-urges-customers-to-shut-down.html), [Bleeping Computer — Kiteworks urges 6-hour server shutdown over potential zero-day attacks](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)

### Mini Shai-Hulud GitHub Actions Supply Chain
- **Description**: Two compromised actions-cool GitHub Actions repositories (actions-cool/issues-helper and actions-cool/maintain-one-comment) were re-enabled and resumed executing Mini Shai-Hulud malware months after initial May 2026 compromise.
- **Impact**: Supply chain compromise affecting CI/CD pipelines using these actions; potential credential theft, code injection, and further repository compromise.
- **Status**: Active malware execution observed after repositories became accessible; GitHub has disabled the actions.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)

### Cloudflare Containers Data Leakage
- **Description**: A flaw in Cloudflare Containers allowed a paying customer to read leftover disk data from other customers' containers on the same server. Data came from disk space previously used and released by other containers.
- **Impact**: Cross-tenant data exposure in shared container infrastructure; sensitive data leakage between customers.
- **Status**: Fixed by Cloudflare; no evidence of malicious exploitation reported.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: monitor
- **Reporting**: [The Hacker News — Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data](https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html)

## Affected Systems and Products

- **Elementor Website Builder WordPress Plugin**: Affected versions not fully specified in sources; all versions prior to patched release potentially vulnerable.
- **Microsoft SharePoint**: Versions affected by CVE-2026-65660; consult Microsoft security advisories for specific build numbers.
- **WSO2 Products**: Multiple products including WSO2 API Control Plane affected by CVE-2026-5430; consult WSO2 security advisories for complete list.
- **Adobe Commerce / Magento**: E-commerce platform versions affected by the CISA KEV-listed flaw; consult Adobe security bulletins.
- **MikroTik RouterOS**: RouterOS versions affected by the CISA KEV-listed vulnerability; consult MikroTik security announcements.
- **Roundcube Webmail**: Versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1 affected by CVE-2026-48842.
- **Grav CMS**: Versions with unpatched path traversal flaw; specific versions not identified in sources.
- **Kiteworks Secure File Sharing**: All customer systems potentially targeted; shutdown recommended as precaution.
- **GitHub Actions**: Repositories using actions-cool/issues-helper or actions-cool/maintain-one-comment during compromise window.
- **Cloudflare Containers**: Multi-tenant container infrastructure; flaw fixed by provider.

## Attack Vectors and Techniques

- **CSRF Admin Account Takeover**: Attackers craft malicious links that, when clicked by an authenticated Elementor admin, forge requests to create new administrator accounts without user consent.
- **Code Injection via SharePoint**: Remote code execution through crafted requests exploiting CVE-2026-65660 in Microsoft Office SharePoint.
- **Path Traversal Authentication Bypass**: Exploitation of CVE-2026-5430 in WSO2 products to bypass authentication controls and traverse file systems.
- **Pre-Auth SQL Injection**: Unauthenticated database queries via the virtuser_query plugin in Roundcube Webmail (CVE-2026-48842) using preg_replace() backslash manipulation.
- **Supply Chain Compromise (GitHub Actions)**: Malicious code injected into widely-used GitHub Actions repositories, executing in downstream CI/CD pipelines (Mini Shai-Hulud campaign).
- **Backend Wallet Compromise**: Direct compromise of cryptocurrency exchange backend infrastructure enabling unauthorized transfers from hot and warm wallets.
- **AI Agent Instruction Smuggling ('Salesbleed')**: Agentic AI systems manipulated to smuggle arbitrary instructions from web sources across multiple applications into trusted internal channels like Slack.
- **AI-Agent-Driven Docker Hijacking**: Carbonato botnet uses AI agents (Hermes Agent framework) to discover and compromise exposed Docker daemons.
- **Cross-Tenant Container Data Leakage**: Reading residual disk data from previously terminated containers in shared Cloudflare infrastructure.
- **JXA Dropper with Server-Side Decryption**: PamStealer macOS malware uses JavaScript for Automation (JXA) dropper with live C2 payload decryption and multi-layer persistence.
- **iCloud Calendar C2**: MacSync malware abuses public iCloud calendar events to deliver new native payloads to macOS targets.
- **Legitimate Application Hiding**: SectopRAT hides inside legitimate applications to evade detection while providing remote access.
- **Grav CMS Path Traversal for Defacement**: Unauthenticated file system traversal used to compromise and deface the Clop ransomware leak site.

## Threat Actor Activities

- **North Korean Threat Actors (Lazarus/APT38 suspected)**: Stole $351.6 million from Bitget cryptocurrency exchange via backend compromise of hot and warm wallets on September 24, 2026. Cold wallets and majority of assets reportedly unaffected.
- **ShinyHunters**: Compromised and defaced the Clop ransomware gang's data leak site using an unpatched Grav CMS path traversal flaw; also reported ratting on TeamPCP hackers. Demonstrates attacker-on-attacker operations and vulnerability exploitation for notoriety.
- **Clop Ransomware Gang**: Victim of ShinyHunters compromise; forced to move leak site to new Tor address after server compromise and defacement.
- **Mini Shai-Hulud Campaign Operators**: Maintained persistence in compromised GitHub Actions repositories (actions-cool organization) for months; malware reactivated when repositories became accessible again in September 2026.
- **PamStealer Operators**: Deploying updated macOS information stealer with server-side payload decryption, JXA dropper mechanism, and multi-layer persistence techniques.
- **Carbonato Botnet Operators**: Targeting exposed Docker daemons globally to install Hermes Agent AI framework, creating an AI-agent-controlled botnet for further exploitation.
- **MacSync Malware Operators**: Evolving macOS malware now using public iCloud calendars as a novel C2 channel for payload delivery.
- **SectopRAT Operators**: Revived remote access Trojan campaign hiding malicious functionality inside legitimate applications to evade behavioral detection.
- **Russian State-Sponsored Actors**: Conducting hybrid cyber-physical operations against European nations supporting Ukraine, combining cyber sabotage, disinformation, and drone attacks.
- **Rydox Marketplace Administrator (Kosovar National)**: Pleaded guilty to operating large illegal marketplace selling stolen PII, credentials, credit card data, and cybercrime tools; faces up to 22 years imprisonment.
- **U.S. Army Soldier (Individual Actor)**: Sentenced to 70 months for hacking AT&T and Verizon in 2024, stealing mobile call/text metadata for over 100 million customers; ordered to pay nearly $300,000 restitution.