---
schema_version: 2
report_date: 2026-09-26
generated_at: 2026-09-26T04:26:45Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-26/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across enterprise software, web applications, and cloud infrastructure. CISA has added two high-severity flaws—CVE-2026-5430 in WSO2 products and a critical Adobe Commerce vulnerability—to its Known Exploited Vulnerabilities catalog based on confirmed attack activity. Simultaneously, a pre-authentication SQL injection in Roundcube Webmail (CVE-2026-48842) is being actively exploited in the wild, prompting urgent patching advisories from the Canadian Centre for Cyber Security.

Threat actors are diversifying their techniques beyond traditional vulnerability exploitation. North Korean operators compromised Bitget's backend infrastructure to steal $351.6 million in cryptocurrency, while the ShinyHunters group leveraged an unpatched Grav CMS path traversal flaw to breach the Clop ransomware gang's leak site. A new botnet dubbed Carbonato is weaponizing AI agents to hijack exposed Docker daemons, and compromised GitHub Actions from the Mini Shai-Hulud campaign have reactivated to deliver malware. These developments signal a shift toward supply chain compromise, AI-assisted automation, and cross-platform credential abuse.

Several vendors have issued emergency mitigations ahead of patches. Kiteworks took the extraordinary step of urging global customers to shut down servers for a six-hour window based on threat intelligence signaling an imminent zero-day attack. OnePlus devices remain vulnerable to a two-flaw chain granting root access to any installed app without permissions, with no patch yet available. Organizations should prioritize the CISA KEV-listed vulnerabilities, the Roundcube flaw, and any internet-facing Kiteworks or Roundcube deployments while monitoring for indicators of compromise tied to the North Korean and ShinyHunters campaigns.

## Active Exploitation Details

### WSO2 Authentication Bypass / Path Traversal (CVE-2026-5430)
- **Description**: A critical path traversal vulnerability in WSO2 API Control Plane that allows authentication bypass. The flaw carries a CVSS score of 9.8 and affects multiple WSO2 enterprise products.
- **Impact**: Attackers can bypass authentication controls and potentially achieve remote code execution or unauthorized administrative access to affected WSO2 deployments.
- **Status**: Actively exploited in the wild; added to CISA KEV catalog on September 25, 2026. Patches are available from WSO2.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/), [The Hacker News — WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)

### Roundcube Webmail Pre-Auth SQL Injection (CVE-2026-48842)
- **Description**: A pre-authentication SQL injection vulnerability in the virtuser_query plugin of Roundcube Webmail. The flaw stems from improper handling of backslash characters in a preg_replace() call, allowing unauthenticated attackers to inject arbitrary SQL.
- **Impact**: Unauthenticated remote attackers can execute arbitrary SQL commands, leading to data theft, authentication bypass, and potential remote code execution on the underlying database server.
- **Status**: Actively exploited in the wild per Canadian Centre for Cyber Security advisory. Patched in Roundcube 1.6.16 and 1.7.1.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-48842
- **Reporting**: [The Hacker News — Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)

### Adobe Commerce / Magento Critical Flaw
- **Description**: A critical vulnerability affecting Adobe Commerce and Magento platforms. Specific technical details were not disclosed in the source material, but CISA has confirmed active exploitation.
- **Impact**: Based on CISA KEV inclusion, exploitation likely enables significant compromise such as remote code execution, authentication bypass, or customer data theft.
- **Status**: Actively exploited; added to CISA KEV catalog alongside the WSO2 flaw. Adobe has released security updates.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/), [The Hacker News — WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)

### Grav CMS Unauthenticated Path Traversal
- **Description**: An unpatched unauthenticated path traversal vulnerability in Grav CMS. The Clop ransomware gang's leak site was compromised and defaced through this flaw by the ShinyHunters group.
- **Impact**: Allows unauthenticated attackers to traverse the filesystem, potentially leading to arbitrary file read, write, or remote code execution depending on server configuration.
- **Status**: Unpatched at time of reporting; actively exploited against at least one high-value target (Clop leak site). No vendor patch mentioned in source.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — ShinyHunters hacked Clop leak site using Grav CMS path traversal flaw](https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/)

### Elementor WordPress CSRF to Admin Account Creation
- **Description**: A cross-site request forgery (CSRF) vulnerability in the Elementor plugin for WordPress that allows unauthenticated attackers to create administrator accounts.
- **Impact**: Attackers can trick authenticated administrators into executing actions that create new admin accounts, leading to full site takeover.
- **Status**: Vulnerability disclosed; exploitation potential is high given the popularity of Elementor. Patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Elementor WordPress flaw lets attackers create admin accounts](https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/)

### Kiteworks Potential Zero-Day
- **Description**: Kiteworks issued an urgent advisory urging all customers worldwide to temporarily shut down their servers for a six-hour window on Saturday after receiving threat intelligence warning of a potentially imminent cyberattack targeting a zero-day vulnerability.
- **Impact**: Unknown specific impact, but the severity of the mitigation (full server shutdown) suggests potential for remote code execution or catastrophic data exposure.
- **Status**: Threat intelligence indicates imminent exploitation; no patch available at time of advisory. Kiteworks investigating.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Kiteworks urges 6-hour server shutdown over potential zero-day attacks](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)

### SharePoint Flaw Exploited in Attacks
- **Description**: CISA warned that hackers are exploiting a vulnerability affecting Microsoft SharePoint. Specific CVE and technical details were not provided in the source material.
- **Impact**: Active exploitation confirmed by CISA; likely enables privilege escalation, data access, or remote code execution in SharePoint environments.
- **Status**: Actively exploited per CISA; added to KEV catalog (implied). Microsoft patches expected.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-sharepoint-wso2-adobe-commerce-flaws-exploited-in-attacks/)

### Cloudflare Containers Cross-Customer Data Leak
- **Description**: A flaw in Cloudflare Containers allowed a paying customer to read leftover disk data from other customers' containers on the same server. The data came from disk space previously used and released by other containers, not from live workloads.
- **Impact**: Cross-tenant data exposure in a multi-tenant container environment. Attackers could not target specific customers but could access residual sensitive data.
- **Status**: Fixed by Cloudflare. No evidence of malicious exploitation; discovered by researchers.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data](https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html)

### OnePlus / OPPO OxygenOS Root Access Chain
- **Description**: Two chained flaws in OnePlus's OxygenOS allow a malicious app installed by the user—requesting no special permissions—to gain root access on OnePlus 15 and "many more" OnePlus and OPPO devices.
- **Impact**: Full device compromise (root access) via a seemingly benign app install. Bypasses Android permission model entirely.
- **Status**: Unpatched at time of reporting. OnePlus acknowledged the flaws affect multiple devices but has not released fixes.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions](https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html)

### GitLab Private Email Address Exposure
- **Description**: Private GitLab project email addresses (used for issue/task submission via email) are being exposed in public READMEs, contributing guides, and support pages. Attackers can use these addresses to push code or issues to private projects.
- **Impact**: Unauthorized code pushes, issue injection, and potential supply chain compromise in GitLab projects where these email addresses are documented publicly.
- **Status**: Configuration/misuse issue rather than a code vulnerability. No patch required; remediation is operational (remove exposed addresses, rotate tokens).
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Exposed GitLab project email addresses let attackers push code](https://www.bleepingcomputer.com/news/security/exposed-gitlab-project-email-addresses-let-attackers-push-code/)

### Salesforce Agents "Salesbleed" Slack Phishing
- **Description**: A technique dubbed "Salesbleed" exploits Salesforce Agents to smuggle arbitrary instructions from the web across multiple applications into trusted internal Slack channels, enabling sophisticated phishing.
- **Impact**: Attackers can manipulate AI agents to deliver convincing phishing messages through trusted internal communication channels, bypassing traditional email security controls.
- **Status**: Technique demonstrated; active exploitation status unclear. Relates to agentic AI architecture weaknesses rather than a single CVE.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — 'Salesbleed' Exploits Salesforce Agents to Enable Slack Phishing](https://www.darkreading.com/application-security/salesbleed-exploits-salesforce-agents-slack-phishing)

## Affected Systems and Products

- **WSO2 API Control Plane and related WSO2 products**: Multiple enterprise integration and API management products affected by CVE-2026-5430
- **Adobe Commerce and Magento**: E-commerce platforms affected by critical flaw added to CISA KEV
- **Roundcube Webmail**: Versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1 affected by CVE-2026-48842
- **Grav CMS**: Unpatched versions vulnerable to unauthenticated path traversal
- **Elementor WordPress Plugin**: Versions with CSRF vulnerability allowing admin account creation
- **Kiteworks Secure File Sharing**: All customer deployments advised to shut down pending zero-day investigation
- **Microsoft SharePoint**: Versions affected by actively exploited flaw (specific versions not disclosed)
- **Cloudflare Containers**: Multi-tenant container platform; flaw fixed by provider
- **OnePlus Devices (OnePlus 15 and others) / OPPO Devices**: Running OxygenOS with unpatched root access chain
- **GitLab**: Projects with exposed private email addresses in public documentation
- **Salesforce Agents / Slack Integration**: Environments using agentic AI workflows between Salesforce and Slack
- **Docker Daemons (exposed)**: Internet-accessible Docker API endpoints targeted by Carbonato botnet
- **GitHub Actions (actions-cool/issues-helper, actions-cool/maintain-one-comment)**: Compromised during Mini Shai-Hulud campaign
- **Bitget Cryptocurrency Exchange**: Backend infrastructure compromised by North Korean actors

## Attack Vectors and Techniques

- **Pre-Authentication SQL Injection**: Unauthenticated database query manipulation via crafted input to Roundcube's virtuser_query plugin (CVE-2026-48842)
- **Authentication Bypass via Path Traversal**: Exploitation of WSO2 API Control Plane path traversal (CVE-2026-5430) to circumvent access controls
- **Unauthenticated Path Traversal**: Direct filesystem traversal in Grav CMS without authentication to compromise Clop leak site
- **Cross-Site Request Forgery (CSRF)**: Tricking authenticated WordPress admins into creating attacker-controlled admin accounts via Elementor plugin
- **Supply Chain Compromise (GitHub Actions)**: Malicious code injected into popular GitHub Actions (actions-cool repositories) during Mini Shai-Hulud campaign; repositories reactivated months later
- **Backend Infrastructure Compromise**: North Korean actors breached Bitget's hot/warm wallet infrastructure, stealing $351.6M in cryptocurrency
- **AI Agent Hijacking**: Carbonato botnet targets exposed Docker daemons to install Hermes Agent AI framework for automated command and control
- **Agentic AI Instruction Smuggling ("Salesbleed")**: Malicious web content instructs Salesforce Agents to propagate commands into internal Slack channels
- **Root Access via Chained Local Flaws**: Malicious Android app with zero permissions chains two OnePlus/OxygenOS flaws to achieve root
- **Credential/Token Exposure in Documentation**: Private GitLab project email addresses published in READMEs enable unauthorized code pushes
- **Multi-Layer Persistence with Server-Side Decryption**: PamStealer macOS malware uses JXA dropper and live C2 payload decryption for stealthy persistence
- **Public iCloud Calendar Abuse**: MacSync malware leverages public iCloud calendar events as a covert payload delivery channel
- **RAT Concealment in Legitimate Applications**: SectopRAT hides inside trusted application processes to evade detection
- **Hybrid Cyber-Physical Operations**: Russian actors combining cyber sabotage, disinformation, and drone attacks against European targets

## Threat Actor Activities

- **ShinyHunters**: Compromised and defaced the Clop ransomware gang's data leak site via Grav CMS path traversal; also referenced in context of "ratting on TeamPCP hackers"
- **Clop Ransomware Gang**: Victim of ShinyHunters intrusion; forced to migrate leak site to new Tor address
- **North Korean Threat Actors (suspected Lazarus Group)**: Compromised Bitget cryptocurrency exchange backend, stealing $351.6M from hot and warm wallets on September 24, 2026
- **Mini Shai-Hulud Campaign Operators**: Compromised actions-cool GitHub Actions repositories in May 2026; malicious code reactivated when repositories became accessible again in September 2026
- **PamStealer Operators**: Deploying updated macOS info-stealer with server-side payload decryption, JXA dropper, and multi-layer persistence
- **Rydox Marketplace Admin (Kosovar national)**: Pleaded guilty to operating large illegal marketplace for stolen PII, credentials, credit cards, and cybercrime tools
- **Carbonato Botnet Operators**: Deploying new malware targeting exposed Docker daemons to install Hermes Agent AI framework for automated control
- **Russian Hybrid Warfare Actors**: Conducting coordinated cyber sabotage, disinformation campaigns, and drone attacks against European nations supporting Ukraine
- **U.S. Army Soldier (convicted)**: Sentenced to 70 months for hacking AT&T and Verizon, stealing call/text metadata for 100M+ customers in 2024 extortion scheme
- **Rasmus Moorats (Security Researcher)**: Discovered and reported chained OnePlus/OxygenOS root flaws; disclosed affecting multiple OnePlus and OPPO devices