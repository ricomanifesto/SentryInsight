---
schema_version: 2
report_date: 2026-08-19
generated_at: 2026-08-19T01:40:31Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-19/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are undergoing active exploitation across diverse technology stacks, from AI platforms and DevOps tools to enterprise software and consumer applications. CISA has added two high-impact flaws—affecting the Ray distributed computing framework and Windows Task Host—to its Known Exploited Vulnerabilities catalog, confirming ransomware gangs and other threat actors are leveraging them in the wild. Simultaneously, a critical GitLab zero-click vulnerability (CVE-2026-19478) and a severe Forminator WordPress plugin flaw (CVE-2026-15748) present immediate risk to internet-facing assets, with the latter affecting over 600,000 installations.

Threat actor activity shows increased sophistication and diversification. A China-linked operator demonstrated near-autonomous AI-driven attacks against APAC government targets, while the Clop ransomware gang deployed a custom Java web shell purpose-built for PTC Windchill and FlexPLM environments. The TWINLOOT framework operates entirely within Microsoft's trusted cloud services—SharePoint and Teams—for stealthy credential theft and lateral movement. Meanwhile, the "City Forum" campaign has silently scraped Salesforce and ServiceNow portals since 2025 from a single server, and a typosquatting operation dubbed "StubMaker" seeded 16 malicious RubyGems packages to steal browser credentials and cryptocurrency wallets.

New attack vectors center on AI system manipulation and supply chain compromise. Researchers disclosed the "CoSnitch" technique exploiting undocumented parameters in Microsoft Copilot Personal to exfiltrate data from connected applications with a single click, while separate work demonstrated self-propagating "mind viruses" spreading between AI agents via persistent prompt files. Attackers are actively exploiting SSRF flaws in MLflow and FUXA to harvest cloud credentials, and a crafted GitHub Issue in Snowflake's repository triggered command injection with internal Jira credentials. These developments signal a shift toward exploiting trust boundaries in AI workflows, CI/CD pipelines, and cloud identity providers.

## Active Exploitation Details

### CVE-2026-19478 — Critical GitLab Zero-Click/GraphQL Flaw
- **Description**: A critical vulnerability in GitLab Community Edition and Enterprise Edition that, under certain conditions, allows unauthenticated attackers to remotely modify or delete public projects and user data. The flaw resides in GraphQL handling and requires zero user interaction. GitLab rates it Critical with a CVSS score of 9.4.
- **Impact**: Unauthenticated attackers can delete or modify public projects and user data on affected GitLab instances, potentially destroying source code, CI/CD configurations, and project metadata.
- **Status**: Security updates released by GitLab. Organizations running self-managed versions face mitigation challenges due to limited technical details released, making exploitation detection difficult.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [Dark Reading — Critical GitLab Zero-Click Flaw Poses Mitigation Challenges](https://www.darkreading.com/application-security/critical-gitlab-zero-click-flaw-mitigation-challenges), [The Hacker News — Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

### CVE-2026-15748 — Forminator WordPress Plugin Unauthenticated RCE
- **Description**: A critical security flaw in Forminator Forms, a WordPress plugin with more than 600,000 active installations. The vulnerability allows unauthenticated remote code execution via malicious PHP file uploads.
- **Impact**: Attackers can achieve arbitrary code execution on susceptible WordPress sites without authentication, leading to full site compromise, data theft, and potential lateral movement.
- **Status**: Vulnerability disclosed and tracked as CVE-2026-15748 with CVSS 9.8. Patch availability not explicitly stated in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-15748
- **Reporting**: [The Hacker News — Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

### Ray Distributed Computing Framework Browser-Based RCE
- **Description**: A critical flaw in Ray, an open-source Python-native distributed computing framework for scaling AI and machine learning workloads. The vulnerability can trigger browser-based remote code execution.
- **Impact**: Attackers can achieve remote code execution through browser-based vectors, compromising AI/ML workloads and potentially the underlying infrastructure.
- **Status**: CISA added to Known Exploited Vulnerabilities (KEV) catalog citing evidence of active exploitation. GitHub project has significant adoption.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE](https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html)

### Windows Task Host Vulnerability
- **Description**: A high-severity Windows Task Host vulnerability that CISA flagged as actively exploited in April 2026. Ransomware gangs are now confirmed to be exploiting this flaw.
- **Impact**: Provides ransomware operators with a pathway for privilege escalation, persistence, or lateral movement on Windows systems, facilitating ransomware deployment.
- **Status**: Actively exploited by ransomware gangs per CISA confirmation. Added to KEV catalog.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA: Windows Task Host flaw now exploited by ransomware gangs](https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/)

### MLflow SSRF and FUXA Vulnerabilities
- **Description**: Two critical vulnerabilities impacting MLflow (open-source AI platform) and FUXA (open-source web-based SCADA/HMI software for OT/industrial automation). Both are witnessing malicious scanning and exploitation efforts.
- **Impact**: Attackers exploit SSRF in MLflow to steal cloud credentials and secrets. FUXA flaws expose industrial control systems to compromise.
- **Status**: Independent reports from watchTowr and VulnCheck confirm malicious scanning and active exploitation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

### Clop Custom Web Shell for Windchill/FlexPLM
- **Description**: A custom Java web shell linked to the Clop ransomware gang, designed specifically for PTC Windchill and FlexPLM servers. Includes built-in features to decrypt credentials, enumerate file repositories, and steal files.
- **Impact**: Targeted data theft from product lifecycle management (PLM) systems, exposing intellectual property, credentials, and proprietary design data.
- **Status**: Actively used in Clop data theft attacks against Windchill and FlexPLM deployments.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Clop created custom web shell for Windchill data theft attacks](https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/)

### TWINLOOT Python Implant Framework
- **Description**: A modular, PyArmor-hardened Python implant that operates its entire command-and-control infrastructure inside trusted Microsoft services (SharePoint Online, Teams). Tasking flows through SharePoint file operations and Teams messages.
- **Impact**: Stealthy credential theft, persistence, and lateral movement entirely within Microsoft 365 trusted boundaries, evading traditional network defenses.
- **Status**: Active operations observed; framework disclosed by Ontinue researchers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Silent 'TwinLoot' Cyber Threat Operates Entirely From Microsoft's Cloud](https://www.darkreading.com/cloud-security/silent-twinloot-threat-operates-microsoft-cloud), [The Hacker News — TWINLOOT Abuses SharePoint and Teams to Steal Credentials and Move Across Networks](https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html)

### Unisoc Modem Video Call Exploit Chain
- **Description**: Two vulnerabilities in Unisoc modems that can be chained to take over an Android device by delivering a payload via a video call and getting the victim to answer.
- **Impact**: Remote compromise of Android devices through incoming video calls, requiring only that the victim answers the call.
- **Status**: Researchers demonstrated the exploit chain; active exploitation status not explicitly confirmed but technique is weaponizable.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Dark Reading — Video Call Exploit Chains Two Flaws in Unisoc Modems](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)

### Microsoft Copilot Personal "CoSnitch" Flaws
- **Description**: Three vulnerabilities in Microsoft Copilot Personal (collectively named CoSnitch) that turn on an undocumented URL parameter surfaced by the assistant itself. A single click on a crafted link can silently exfiltrate data from connected apps and the victim's Copilot session.
- **Impact**: One-click data exfiltration from all applications connected to the victim's Copilot session, including emails, documents, and chat history.
- **Status**: Disclosed by Varonis Threat Labs; exploitation potential demonstrated. Active exploitation not explicitly confirmed.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Dark Reading — 'CoSnitch' Attack Tricked Copilot into Mapping Out Architecture](https://www.darkreading.com/vulnerabilities-threats/cosnitch-attack-copilot-mapping-out-architecture), [The Hacker News — Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps](https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html)

### StubMaker Typosquatting Campaign (RubyGems)
- **Description**: A typosquatting campaign on RubyGems distributing 16 malicious packages (ubnuler, ubnlder, ri18nr, reaker, rakier, orakw, joxn, and others) containing a Windows-based information stealer targeting browser credentials and cryptocurrency wallets.
- **Impact**: Developers installing typosquatted packages suffer credential theft from browsers and crypto wallet drainage.
- **Status**: Active campaign discovered August 15, 2026 by OpenSourceMalware; packages published and available for download.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — 16 Typosquatted RubyGems Packages Steal Browser Credentials and Crypto Wallets](https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html)

### City Forum Campaign (Salesforce/ServiceNow Scraping)
- **Description**: A single infrastructure (158.220.87.79) has been scraping records from Salesforce and ServiceNow customer portals across multiple industries since 2025, using compromised credentials for access.
- **Impact**: Long-term unauthorized access to CRM and ITSM data, including customer records, support tickets, and internal communications.
- **Status**: Active since 2025; attributed to one server infrastructure by Reco researchers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — One Attacker Has Scraped Both Salesforce and ServiceNow Portals Since 2025](https://thehackernews.com/2026/08/one-attacker-has-scraped-both.html)

### Snowflake GitHub Actions Command Injection
- **Description**: A GitHub Actions workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository. A crafted GitHub issue can execute commands in a workflow containing internal Jira credentials.
- **Impact**: Command execution in CI/CD pipeline with access to internal Jira credentials, potentially leading to further supply chain compromise.
- **Status**: Disclosed by Wiz researchers; vulnerability present in .github/workflows/jira_issue.yml.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)

### SafePal Authorization Flaw
- **Description**: An authorization flaw in an order-tracking plug-in exposed names, email addresses, shipping addresses, phone numbers, and purchase details of approximately 39,798 customers.
- **Impact**: PII and order history exposure for hardware wallet customers, enabling targeted phishing and physical threat risks.
- **Status**: Disclosed by SafePal; all affected customers notified individually on August 16, 2026.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [The Hacker News — SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers](https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html)

### China-Linked AI-Driven APAC Attack
- **Description**: A Chinese-language operator used a complex AI framework to conduct a purported "near-autonomous" attack targeting government agencies, likely in Taiwan. Represents the first reported near-autonomous nation-state attack.
- **Impact**: Compromise of government systems through AI-orchestrated operations with minimal human intervention.
- **Status**: Active campaign reported; details on specific vulnerabilities used not disclosed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — China-Linked Hacker Shows AI Capabilities in APAC Attack](https://www.darkreading.com/cyberattacks-data-breaches/china-linked-hacker-ai-capabilities-apac-attack)

### Azure Credential Theft Campaign
- **Description**: A threat actor claims to have stolen 3.6 million Azure account records from multiple Fortune 500 companies by accessing Microsoft Azure infrastructure using compromised credentials.
- **Impact**: Massive exposure of employee databases and Azure resource access across major enterprises.
- **Status**: Actor selling databases; access achieved via compromised credentials (initial vector unspecified).
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hacker claims 3.6 million Azure account records stolen from major companies](https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/)

### Pokémon Center / CEVA Logistics Third-Party Breach
- **Description**: Third-party data breach at logistics provider CEVA Logistics exposed customer personal and order information for Pokémon Center customers in the United Kingdom and Germany.
- **Impact**: Customer PII and order data compromised through supply chain partner.
- **Status**: Breach confirmed; notifications sent to affected customers.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Pokémon Center data breach exposes customer info, cancels some orders](https://www.bleepingcomputer.com/news/security/pokemon-center-data-breach-exposes-customer-info-cancels-some-orders/)

## Affected Systems and Products

- **GitLab Community Edition & Enterprise Edition**: Self-managed versions vulnerable to CVE-2026-19478; zero-click exploitation possible
- **WordPress sites with Forminator Forms plugin**: 600,000+ active installations affected by CVE-2026-15748 unauthenticated RCE
- **Ray distributed computing framework**: Open-source Python AI/ML platform; browser-based RCE actively exploited
- **Windows Task Host**: All supported Windows versions; ransomware gangs actively exploiting
- **MLflow**: Open-source AI platform; SSRF flaw exploited for cloud credential theft
- **FUXA**: Open-source SCADA/HMI software for OT/industrial automation; critical vulnerabilities under active exploitation
- **PTC Windchill & FlexPLM**: PLM servers targeted by Clop custom Java web shell with credential decryption capabilities
- **Microsoft 365 (SharePoint Online, Teams)**: Used as C2 infrastructure by TWINLOOT Python implant framework
- **Android devices with Unisoc modems**: Vulnerable to video call exploit chain requiring only call answer
- **Microsoft Copilot Personal**: Three CoSnitch vulnerabilities enabling one-click data exfiltration from connected apps
- **RubyGems package registry**: 16 typosquatted packages (StubMaker campaign) stealing browser credentials and crypto wallets
- **Salesforce & ServiceNow customer portals**: Scraped via compromised credentials by City Forum campaign since 2025
- **Snowflake snowflake-connector-net repository**: GitHub Actions workflow injection via crafted issues
- **SafePal hardware wallet order-tracking system**: Authorization flaw exposed ~39,798 customer records
- **Government agency systems in APAC**: Targeted by China-linked AI-driven near-autonomous attack framework
- **Microsoft Azure infrastructure**: Fortune 500 employee databases stolen via compromised credentials
- **CEVA Logistics systems**: Third-party breach affecting Pokémon Center UK/Germany customer data

## Attack Vectors and Techniques

- **Zero-Click GraphQL Exploitation**: Unauthenticated attackers leverage CVE-2026-19478 in GitLab to delete/modify public projects without user interaction
- **Unauthenticated PHP Upload RCE**: Malicious PHP files uploaded to Forminator Forms plugin achieve arbitrary code execution on WordPress sites
- **Browser-Based RCE via AI Framework**: Ray vulnerability triggered through browser vectors to compromise distributed AI/ML workloads
- **Windows Task Host Exploitation**: Ransomware gangs leverage high-severity flaw for privilege escalation and persistence
- **SSRF for Cloud Credential Theft**: MLflow SSRF flaw exploited to access cloud metadata services and steal credentials/secrets
- **Custom Web Shell for PLM Systems**: Clop's Java web shell purpose-built for Windchill/FlexPLM with credential decryption and file enumeration
- **Living-off-the-Land in Microsoft Cloud**: TWINLOOT operates C2 entirely within SharePoint Online and Teams, using file operations and messages for tasking
- **Video Call Exploit Chain**: Two Unisoc modem flaws chained to compromise Android devices when victim answers incoming video call
- **AI Assistant Parameter Manipulation (CoSnitch)**: Undocumented URL parameter in Microsoft Copilot Personal exploited for one-click data exfiltration from connected apps
- **Typosquatting Supply Chain Attack**: 16 RubyGems packages with deceptive names deliver Windows info-stealer for browser credentials and crypto wallets
- **Long-Term Credential-Based Portal Scraping**: Single infrastructure maintains access to Salesforce/ServiceNow portals for over a year using compromised credentials
- **CI/CD Workflow Injection**: Crafted GitHub Issue triggers command injection in Snowflake's GitHub Actions workflow with internal Jira credentials
- **Authorization Bypass in Order Tracking**: SafePal plug-in flaw exposes customer PII without authentication checks
- **Near-Autonomous AI Attack Framework**: China-linked operator uses complex AI system for autonomous targeting and compromise of government agencies
- **Compromised Credential Reuse for Cloud Access**: Actor accesses Azure infrastructure of multiple Fortune 500 companies using stolen credentials
- **Third-Party Logistics Compromise**: CEVA Logistics breach exposes downstream customer data for Pokémon Center

## Threat Actor Activities

- **China-Linked Nation-State Operator**: Conducting near-autonomous AI-driven attacks against APAC government targets (likely Taiwan) using complex AI framework for autonomous targeting and compromise
- **Clop Ransomware Gang**: Deploying custom Java web shells purpose-built for PTC Windchill/FlexPLM with credential decryption, repository enumeration, and file theft capabilities for targeted IP theft
- **Ransom Busters (Ransomware Affiliate)**: Posing as incident-recovery service; proactively emailing victims offering to delete stolen data from ransomware groups' servers for $20,000–$60,000, diverting ransom payments
- **TWINLOOT Operators**: Running modular PyArmor-hardened Python implant framework with C2 entirely inside Microsoft 365 (SharePoint/Teams) for stealthy credential theft and lateral movement
- **City Forum Campaign Operator**: Single infrastructure (158.220.87.79) scraping Salesforce and ServiceNow portals across industries since 2025 using compromised credentials
- **StubMaker Group**: Typosquatting campaign publishing 16 malicious RubyGems packages delivering Windows info-stealer targeting browser credentials and cryptocurrency wallets
- **Azure Credential Theft Actor**: Selling 3.6 million employee records allegedly stolen from Fortune 500 companies' Azure infrastructure via compromised credentials
- **Ransomware Gangs (Multiple)**: Actively exploiting Windows Task Host vulnerability (per CISA) and Ray framework flaw for initial access and ransomware deployment
- **Unknown Actors (MLflow/FUXA)**: Conducting malicious scanning and exploitation of MLflow SSRF and FUXA vulnerabilities per watchTowr and VulnCheck telemetry