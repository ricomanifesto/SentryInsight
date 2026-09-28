---
schema_version: 2
report_date: 2026-09-28
generated_at: 2026-09-28T15:21:57Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-28/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity this week centers on two Citrix NetScaler zero-day vulnerabilities (CVE-2026-88771 and CVE-2026-88772) that enable unauthenticated remote code execution across all affected deployments. CISA has added both flaws to its Known Exploited Vulnerabilities catalog and ordered federal civilian agencies to patch immediately, confirming global active exploitation. Simultaneously, the ShinyHunters extortion group has escalated operations following the arrest of an alleged member, bypassing web application firewalls to exploit the critical Oracle PeopleSoft vulnerability (CVE-2026-35273) at scale and compromising the Cl0p ransomware gang's leak site through an unpatched Grav CMS path traversal flaw.

Microsoft SharePoint (CVE-2026-65660) and MikroTik RouterOS vulnerabilities have also been added to the CISA KEV catalog with confirmed active exploitation, while a new Carbonato botnet campaign targets exposed Docker daemons to deploy an AI agent framework controlled via Telegram. Threat actors continue to abuse legitimate cloud identities—JADEPUFFER (Storm-3168) leveraged compromised Azure service principals for destructive operations, and infostealer campaigns have harvested AI service credentials from over 80,000 organizations, fueling a growing LLMjacking ecosystem. North Korean actors are attributed to the $387 million Bitget cryptocurrency exchange heist, and a U.S. Army soldier received a 70-month sentence for extorting AT&T, Verizon, and other major telecommunications firms.

## Active Exploitation Details

### Citrix NetScaler ADC and Gateway RCE Zero-Days (CVE-2026-88771, CVE-2026-88772)
- **Description**: Two critical remote code execution vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway. CVE-2026-88771 is an improper input validation flaw (CVSS 9.5) allowing unauthenticated attackers to execute arbitrary code. CVE-2026-88772 is a companion RCE flaw. One vulnerability affects every deployment on an affected version, including default configurations.
- **Impact**: Unauthenticated remote code execution leading to full system compromise, data theft, and lateral movement within networks.
- **Status**: Actively exploited in the wild globally. Citrix has released security updates for both vulnerabilities along with six other flaws. CISA added both to the KEV catalog on September 28, 2026, and ordered federal agencies to patch by October 1, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771, CVE-2026-88772
- **Reporting**: [The Hacker News — CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html), [Bleeping Computer — CISA orders feds to patch exploited Citrix flaws by Wednesday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/), [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### Oracle PeopleSoft Unauthenticated RCE (CVE-2026-35273)
- **Description**: Critical security flaw in Oracle PeopleSoft (CVSS 9.8) allowing unauthenticated remote code execution. The vulnerability was first exploited as a zero-day and has seen renewed mass exploitation.
- **Impact**: Unauthenticated remote code execution on PeopleSoft servers, enabling web shell deployment, data exfiltration, and persistent access.
- **Status**: Actively exploited in a global campaign targeting multiple sectors. ShinyHunters-linked actors are using a URL-encoding trick to bypass web application firewall rules that mitigate this flaw, allowing widespread exploitation to resume on vulnerable servers.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint Code Injection (CVE-2026-65660)
- **Description**: Code injection vulnerability in Microsoft Office SharePoint (CVSS 8.8) that enables remote code execution.
- **Impact**: Remote code execution in SharePoint environments, potentially leading to data compromise and further network intrusion.
- **Status**: Actively exploited in the wild. Added to CISA KEV catalog on September 26, 2026, citing evidence of active exploitation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### MikroTik RouterOS Vulnerability
- **Description**: Security flaw in MikroTik RouterOS added to CISA KEV catalog with evidence of active exploitation.
- **Impact**: Compromise of network infrastructure devices, enabling traffic interception, lateral movement, and persistent access.
- **Status**: Actively exploited in the wild. Added to CISA KEV catalog on September 26, 2026.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### Elementor Website Builder CSRF Flaw
- **Description**: High-severity cross-site request forgery (CSRF) vulnerability in the Elementor Website Builder WordPress plugin (CVSS 8.8) that allows unauthenticated attackers to create rogue administrator accounts and take control of sites. The flaw requires an administrator to click a crafted link.
- **Impact**: Full site takeover through creation of unauthorized administrator accounts.
- **Status**: Vulnerability disclosed with no CVE identifier assigned yet. Affects specific versions of the Elementor plugin.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html)

### Grav CMS Path Traversal Flaw
- **Description**: Unauthenticated path traversal vulnerability in Grav CMS that was exploited to compromise and deface the Cl0p ransomware gang's data leak site.
- **Impact**: Unauthorized file system access leading to server compromise and defacement.
- **Status**: Actively exploited (used by ShinyHunters against Clop's leak site). The flaw was unpatched at time of exploitation; Clop has since moved its leak site to a new Tor address.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: Vulnerability in Cloudflare Containers and Sandboxes that allowed customers with a Workers Paid account to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data exposure in a shared infrastructure environment.
- **Status**: Fixed by Cloudflare. No indication of active exploitation prior to fix.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All deployments on affected versions, including default configurations. Security updates released for both CVE-2026-88771 and CVE-2026-88772.
- **Oracle PeopleSoft**: Servers running vulnerable versions of PeopleSoft. Exploitation bypasses WAF mitigations via URL-encoding trick.
- **Microsoft SharePoint**: On-premises SharePoint Server installations affected by CVE-2026-65660 code injection vulnerability.
- **MikroTik RouterOS**: RouterOS devices running vulnerable versions. Specific version details not provided in source articles.
- **Elementor Website Builder WordPress Plugin**: Specific versions affected by CSRF flaw (CVE not yet assigned). Requires admin interaction with crafted link.
- **Grav CMS**: Installations running unpatched versions vulnerable to path traversal. Exploited against Clop ransomware leak site.
- **Cloudflare Containers and Sandboxes**: Workers Paid accounts on shared physical hosts. Vulnerability fixed by Cloudflare.
- **Docker Daemons**: Exposed Docker daemon APIs targeted by Carbonato botnet for unauthorized container deployment.
- **Microsoft Azure Service Principals**: Compromised service principal credentials used by JADEPUFFER (Storm-3168) for destructive operations in Azure environments.
- **AI Service Accounts (OpenAI, Anthropic, others)**: Credentials and session tokens stolen via infostealers from over 80,000 corporate domains, enabling LLMjacking.
- **Bitget Cryptocurrency Exchange**: Systems breached by North Korean threat actors resulting in $387.5 million theft.
- **Kiteworks (formerly Accellion) Secure File Sharing**: Customers urged to shut down systems for 6-9 hours due to credible threat intelligence of imminent zero-day attacks.

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution via Input Validation Flaws**: Citrix NetScaler CVE-2026-88771 exploits improper input validation to achieve RCE without authentication on default configurations.
- **WAF Bypass via URL Encoding**: ShinyHunters uses URL-encoding tricks to bypass web application firewall rules protecting Oracle PeopleSoft CVE-2026-35273, resuming mass exploitation.
- **Compromised Cloud Identities for Destructive Operations**: JADEPUFFER (Storm-3168) leveraged compromised Azure service principals to delete resources across a victim's Azure environment over an 18-hour period.
- **Exposed Docker Daemon API Exploitation**: Carbonato botnet scans for and compromises exposed Docker daemons to deploy the Hermes AI agent framework, controlled via Telegram.
- **Infostealer-Driven AI Credential Harvesting**: Malware steals AI service credentials (API keys, session tokens) from compromised endpoints, fueling a marketplace for LLMjacking—unauthorized use of victim AI accounts.
- **Path Traversal for Server Compromise**: ShinyHunters exploited an unauthenticated path traversal flaw in Grav CMS to compromise and deface the Clop ransomware gang's Tor-hosted leak site.
- **Cross-Site Request Forgery for Privilege Escalation**: Elementor CSRF flaw allows creation of rogue administrator accounts when a site admin clicks a malicious link.
- **Code Injection in Collaboration Platforms**: Microsoft SharePoint CVE-2026-65660 enables remote code execution through code injection vectors.
- **Network Infrastructure Exploitation**: MikroTik RouterOS flaws targeted for persistent network access and traffic manipulation.
- **Cross-Tenant Data Recovery in Shared Cloud Infrastructure**: Cloudflare Containers flaw allowed recovery of residual data from other customers' containers on the same physical host.
- **Supply Chain Compromise of GitHub Actions**: Mini Shai-Hulud campaign compromised third-party GitHub Actions; malicious code remained accessible for over a week after re-enabling.
- **Fake CAPTCHA/ClickFix Social Engineering**: Lunex Stealer (Psychedelic Stealer) distributed via compromised Ukrainian websites using fake Cloudflare verification checks to deliver malware.
- **AMD Driver Abuse for Defense Evasion**: Lunex Stealer abuses a legitimate AMD driver to disable security monitoring and steal browser credentials.

## Threat Actor Activities

- **ShinyHunters**: Extortion group dramatically escalated attacks following the arrest of a 23-year-old alleged member in the Netherlands. Activities include: mass exploitation of Oracle PeopleSoft CVE-2026-35273 using WAF bypass techniques; compromise and defacement of Cl0p ransomware gang's leak site via Grav CMS path traversal; data theft from the FBI; and extortion of Cl0p operators. Linked to renewed PeopleSoft exploitation campaign globally.
- **JADEPUFFER / Storm-3168**: Microsoft-tracked threat actor orchestrated destructive operations in a Microsoft Azure environment using compromised service principals. Attack spanned ~18 hours in early June 2026, deleting resources. Described as an evolution of the actor's tradecraft.
- **North Korean Threat Actors (attributed)**: Breached Bitget cryptocurrency exchange, stealing over $350 million (total $387.5 million). Bitget suspended and later resumed Bitcoin withdrawals.
- **Carbonato Botnet Operators**: Deploying new botnet malware targeting exposed Docker daemons to install the Hermes AI agent framework (open-source), controlled via Telegram. The implant overwrites the agent's persona file with a 39-line prompt directing task execution.
- **Lunex Stealer / Psychedelic Stealer Operators**: Malware-as-a-service platform distributing stealer via compromised Ukrainian websites using ClickFix-style fake CAPTCHA pages. Four-stage attack chain abuses AMD driver to disable security monitoring and steal browser credentials. Targets Ukrainian-speaking users.
- **Cl0p Ransomware Gang**: Victim of ShinyHunters compromise; leak site defaced and moved to new Tor address. Previously a prolific ransomware and extortion operator.
- **Mini Shai-Hulud Campaign Operators**: Compromised third-party GitHub Actions; malicious payloads remained active and accessible for over a week after maintainers re-enabled the actions.
- **U.S. Army Soldier (convicted)**: Sentenced to 70 months in prison for hacking and extorting at least 10 U.S. technology and telecommunications companies (including AT&T and Verizon) between April 2023 and December 2024. Stole mobile call/text metadata for over 100 million AT&T customers. Ordered to pay nearly $300,000 in restitution.
- **Infostealer Operators (various)**: Harvested AI service credentials and sessions tied to more than 80,000 corporate domains, creating a growing market for stolen AI logins and enabling LLMjacking campaigns.
- **Kiteworks-Targeted Threat Actor (unidentified)**: Federal intelligence authorities provided credible threat intelligence indicating imminent cyberattack against Kiteworks (formerly Accellion) secure file-sharing systems, prompting 6-9 hour shutdown advisory.