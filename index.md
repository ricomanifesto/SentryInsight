---
schema_version: 2
report_date: 2026-09-28
generated_at: 2026-09-28T14:26:24Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-28/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity is surging across multiple vendor platforms, with Citrix NetScaler appliances facing active zero-day attacks that have prompted emergency federal patching orders. CISA has added two critical Citrix vulnerabilities (CVE-2026-88771 and CVE-2026-88772) to its Known Exploited Vulnerabilities catalog, confirming global exploitation of remote code execution flaws affecting default configurations.

Simultaneously, the ShinyHunters extortion group is conducting renewed mass exploitation of a critical Oracle PeopleSoft vulnerability (CVE-2026-35273) using novel WAF bypass techniques, while CISA has also flagged active exploitation of a Microsoft SharePoint code injection flaw (CVE-2026-65660) and a MikroTik RouterOS vulnerability.

## Active Exploitation Details

### Citrix NetScaler RCE Zero-Days (CVE-2026-88771, CVE-2026-88772)
- **Description**: Two critical remote code execution vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway. CVE-2026-88771 (CVSS 9.5) is an improper input validation flaw allowing unauthenticated attackers to execute arbitrary code. CVE-2026-88772 is a complementary flaw. One vulnerability affects every deployment on affected versions, including default configurations.
- **Impact**: Unauthenticated remote code execution leading to full appliance compromise, potential lateral movement, and persistent access to enterprise networks.
- **Status**: Actively exploited in the wild as zero-days. Citrix has released security updates for both flaws along with six additional vulnerabilities. CISA has ordered U.S. federal agencies to patch by September 30, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771, CVE-2026-88772
- **Reporting**: [The Hacker News — CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html), [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html), [Bleeping Computer — CISA orders feds to patch exploited Citrix flaws by Wednesday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/)

### Oracle PeopleSoft CVE-2026-35273 Exploitation Campaign
- **Description**: A critical unauthenticated remote code execution vulnerability in Oracle PeopleSoft (CVSS 9.8) that was previously exploited as a zero-day. Attackers are now using a URL-encoding trick to bypass web application firewall rules that had been mitigating the flaw.
- **Impact**: Unauthenticated remote code execution on PeopleSoft servers, enabling web shell deployment and persistent access to enterprise HR and financial systems.
- **Status**: Renewed mass exploitation campaign underway globally across multiple sectors. WAF bypass technique allows attackers to circumvent existing protections.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/), [The Hacker News — Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells](https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html)

### Microsoft SharePoint RCE (CVE-2026-65660)
- **Description**: A code injection vulnerability in Microsoft Office SharePoint Server (CVSS 8.8) that allows remote code execution. Added to CISA's KEV catalog citing evidence of active exploitation.
- **Impact**: Remote code execution in SharePoint environments, potentially leading to data exfiltration, internal reconnaissance, and lateral movement within Microsoft 365 ecosystems.
- **Status**: Actively exploited in the wild. CISA has mandated federal agency patching.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### MikroTik RouterOS Actively Exploited Flaw
- **Description**: A vulnerability in MikroTik RouterOS added to CISA's KEV catalog with evidence of active exploitation. Specific CVE identifier not disclosed in reporting.
- **Impact**: Compromise of network infrastructure devices, enabling traffic interception, network pivoting, and persistent access to routing infrastructure.
- **Status**: Actively exploited in the wild per CISA KEV listing.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild](https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html)

### Elementor WordPress Plugin CSRF Vulnerability
- **Description**: A high-severity cross-site request forgery (CSRF) vulnerability in the Elementor Website Builder WordPress plugin (CVSS 8.8) that allows unauthenticated attackers to create rogue administrator accounts when an admin clicks a crafted link. No CVE identifier has been assigned yet.
- **Impact**: Full site takeover via administrator account creation, leading to content manipulation, malware distribution, and potential supply chain attacks against site visitors.
- **Status**: Vulnerability disclosed with proof-of-concept; active exploitation status not explicitly confirmed but high severity warrants immediate attention.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted Link](https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html), [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### Carbonato Botnet Docker Daemon Compromise
- **Description**: A new botnet malware targeting exposed Docker daemons to deploy the open-source Hermes AI Agent framework. The implant installs the framework unchanged and overwrites its SOUL.md persona file with a 39-line prompt directing it to execute tasks received through Telegram.
- **Impact**: Unauthorized compute resource hijacking, AI agent deployment for automated attack execution, and Telegram-based command and control.
- **Status**: Active campaign disclosed by ThreatDown researchers. Exploits misconfigured Docker daemons exposed to the internet.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

### JADEPUFFER/Storm-3168 Azure Service Principal Compromise
- **Description**: Threat actor JADEPUFFER (tracked by Microsoft as Storm-3168) orchestrated destructive operations within a Microsoft Azure environment using compromised service principals. Attack occurred over approximately 18 hours in early June 2026.
- **Impact**: Destructive deletion of Azure resources, service disruption, and potential data destruction. Represents an evolution in cloud-focused tradecraft targeting identity infrastructure.
- **Status**: Observed intrusion with destructive intent. Microsoft has published analysis of the tradecraft evolution.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources](https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html)

### Lunex Stealer AMD Driver Abuse
- **Description**: The Lunex malware-as-a-service platform (including Psychedelic Stealer) abuses a legitimate AMD driver to disable security monitoring and steal browser credentials. Distributed via compromised Ukrainian websites using ClickFix-style Cloudflare verification checks.
- **Impact**: Security control bypass via signed driver abuse, credential theft from browsers, and targeted attacks against Ukrainian-speaking users through a four-stage attack chain.
- **Status**: Active MaaS platform with ongoing distribution campaigns. Driver abuse technique enables defense evasion.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html)

### Grav CMS Path Traversal Vulnerability
- **Description**: An unauthenticated path traversal vulnerability in Grav CMS that was exploited by ShinyHunters to compromise and deface the Clop ransomware gang's data leak site, forcing Clop to migrate to a new Tor address.
- **Impact**: Unauthorized file system access leading to server compromise, defacement, and potential data exfiltration. Demonstrates threat actor-on-threat actor targeting.
- **Status**: Actively exploited in targeted attack against Clop infrastructure. Vulnerability was unpatched at time of exploitation.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: A vulnerability in Cloudflare Containers and Sandboxes that allowed customers with Workers Paid accounts to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data leakage exposing sensitive customer information in a multi-tenant cloud environment.
- **Status**: Fixed by Cloudflare. No evidence of active exploitation reported; discovered and remediated proactively.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All deployments on affected versions including default configurations; requires immediate patching per CISA emergency directive
- **Oracle PeopleSoft**: Enterprise HR and financial management systems vulnerable to CVE-2026-35273; WAF bypass technique defeats existing mitigations
- **Microsoft SharePoint Server**: On-premises SharePoint installations affected by CVE-2026-65660 code injection vulnerability
- **MikroTik RouterOS**: Network routing and switching devices; specific affected versions not disclosed in CISA KEV notification
- **Elementor Website Builder WordPress Plugin**: Versions prior to patched release; CVSS 8.8 CSRF flaw enabling admin account takeover
- **Docker Engine**: Exposed Docker daemons accessible from internet; misconfigured API endpoints allowing container deployment
- **Microsoft Azure**: Service principal identities and role assignments; compromised credentials used for destructive resource deletion
- **AMD GPU Drivers**: Legitimate driver component abused by Lunex stealer to disable security monitoring (specific driver versions not disclosed)
- **Grav CMS**: Unpatched installations vulnerable to unauthenticated path traversal; exploited against Clop leak site infrastructure
- **Cloudflare Containers and Sandboxes**: Workers Paid account customers; cross-tenant data residual exposure on shared physical hosts

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Direct exploitation of input validation flaws in Citrix NetScaler (CVE-2026-88771) and Oracle PeopleSoft (CVE-2026-35273) without authentication requirements
- **WAF Bypass via URL Encoding**: ShinyHunters employs character encoding tricks to evade web application firewall rules protecting PeopleSoft CVE-2026-35273
- **CSRF Admin Account Creation**: Elementor flaw leverages cross-site request forgery triggered by admin clicking malicious link to create rogue administrator accounts
- **Exposed Docker Daemon API**: Carbonato botnet scans for and exploits Docker daemons with unauthenticated network-accessible APIs to deploy containers
- **Compromised Cloud Identity Abuse**: JADEPUFFER/Storm-3168 uses stolen service principal credentials to authenticate to Azure and delete resources
- **Signed Driver Abuse for Defense Evasion**: Lunex stealer loads legitimate AMD driver to disable security monitoring tools (EDR/AV) via kernel-level operations
- **ClickFix Social Engineering**: Fake CAPTCHA/Cloudflare verification pages trick users into executing malicious PowerShell commands
- **Path Traversal for Server Compromise**: Grav CMS directory traversal enables file read/write leading to full server takeover of Clop leak site
- **Cross-Tenant Container Data Residue**: Cloudflare Containers flaw allows recovery of residual data from other customers' containers on shared hardware
- **Supply Chain Compromise via GitHub Actions**: Mini Shai-Hulud campaign compromised third-party GitHub Actions; malicious payloads remained active after re-enabling

## Threat Actor Activities

- **ShinyHunters**: Conducting renewed mass exploitation of Oracle PeopleSoft CVE-2026-35273 across multiple sectors globally using WAF bypass techniques; also compromised Clop ransomware gang's leak site via Grav CMS path traversal, demonstrating cross-group targeting
- **JADEPUFFER / Storm-3168**: Microsoft-tracked threat actor evolving tradecraft to target Azure identity infrastructure; conducted destructive 18-hour operation in June 2026 using compromised service principals to delete cloud resources
- **Carbonato Botnet Operators**: Deploying Hermes AI Agent framework via compromised Docker daemons with Telegram-based C2; leveraging open-source AI agent infrastructure for automated task execution
- **Lunex MaaS Operators**: Operating malware-as-a-service platform including Psychedelic Stealer; targeting Ukrainian-speaking users via compromised websites and ClickFix social engineering; abusing signed AMD drivers for defense evasion
- **North Korean Hackers (Lazarus Group attributed)**: Breached Bitget cryptocurrency exchange stealing over $350 million; suspected state-sponsored financial crime operation
- **U.S. Army Soldier (Individual Actor)**: Sentenced to 70 months for hacking and extorting at least 10 U.S. technology and telecommunications companies (including AT&T, Verizon) between April 2023 and December 2024; stole mobile metadata for 100+ million customers
- **Mini Shai-Hulud Campaign Operators**: Compromised third-party GitHub Actions maintainers; malicious payloads persisted in re-enabled actions for over a week, affecting CI/CD pipelines
- **Kiteworks Threat Actor (Unknown)**: Federal intelligence authorities warned Kiteworks of imminent cyberattack targeting their systems; prompted emergency 6-9 hour shutdown recommendation for customers (potential zero-day exploitation)