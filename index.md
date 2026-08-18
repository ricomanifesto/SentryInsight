---
schema_version: 2
report_date: 2026-08-18
generated_at: 2026-08-18T15:44:53Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-18/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with CISA confirming two high-impact flaws— a Windows Task Host vulnerability leveraged by ransomware gangs and a critical Ray framework flaw enabling browser-based remote code execution— have been added to the Known Exploited Vulnerabilities catalog.

Simultaneously, a critical GitLab GraphQL vulnerability (CVE-2026-19478, CVSS 9.4) allows unauthenticated deletion of public projects, and a Forminator WordPress plugin flaw (CVE-2026-15748, CVSS 9.8) enables unauthenticated remote code execution on over 600,000 sites. A Certighost privilege escalation (CVE-2026-54121) lets standard domain users compromise Enterprise Certificate Authorities.

## Active Exploitation Details

### Windows Task Host Vulnerability
- **Description**: High-severity Windows Task Host vulnerability originally flagged as actively exploited in April 2026, now confirmed by CISA to be exploited by ransomware gangs
- **Impact**: Ransomware deployment and system compromise on affected Windows systems
- **Status**: Actively exploited by ransomware groups; patch status not specified in source
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA: Windows Task Host flaw now exploited by ransomware gangs](https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/)

### Ray Framework Browser-Based RCE
- **Description**: Critical flaw in Ray, an open-source Python-native distributed computing framework for AI/ML workloads, enabling browser-based remote code execution
- **Impact**: Remote code execution through browser vectors targeting AI/ML infrastructure
- **Status**: Added to CISA KEV catalog with evidence of active exploitation; GitHub project has 30k+ stars
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE](https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html)

### GitLab GraphQL Unauthenticated Project Deletion
- **Description**: Critical vulnerability in GitLab Community Edition and Enterprise Edition GraphQL API allowing unauthenticated attackers to remotely modify or delete public projects and user data
- **Impact**: Unauthorized deletion/modification of public projects and user data without authentication
- **Status**: Security updates released by GitLab; tracked as CVE-2026-19478 with CVSS 9.4
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [The Hacker News — Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

### Forminator WordPress Plugin Unauthenticated RCE
- **Description**: Critical security flaw in Forminator Forms WordPress plugin (600,000+ active installations) enabling arbitrary code execution via malicious PHP uploads
- **Impact**: Full remote code execution on susceptible WordPress sites without authentication
- **Status**: Disclosed and tracked as CVE-2026-15748 with CVSS 9.8; patch status not specified in source
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-15748
- **Reporting**: [The Hacker News — Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

### Certighost Enterprise CA Privilege Escalation
- **Description**: Vulnerability allowing a standard domain user to turn an Enterprise Certificate Authority into a Domain Controller, compromising PKI Tier 0 identity infrastructure
- **Impact**: Complete domain compromise through Certificate Authority subversion and standing privilege abuse
- **Status**: Patch available; tracked as CVE-2026-54121
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-54121
- **Reporting**: [Bleeping Computer — Certighost and the Privilege Hiding in Your Certificate Authority](https://www.bleepingcomputer.com/news/security/certighost-and-the-privilege-hiding-in-your-certificate-authority/)

### Unisoc VoLTE Video Call Exploit Chain
- **Description**: Two-stage exploit chain achieving full Android kernel access on devices running Unisoc modem firmware through a VoLTE video call, with no fix from the chipset maker
- **Impact**: Complete kernel-level compromise of Android devices via silent video call delivery
- **Status**: Second stage published August 17, 2026; first stage disclosed March 2026; no vendor fix available
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Dark Reading — Video Call Exploit Chains Two Flaws in Unisoc Modems](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems), [The Hacker News — Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access](https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html)

### TWINLOOT Microsoft Cloud Implant Framework
- **Description**: Modular, PyArmor-hardened Python implant operating entire C2 infrastructure inside trusted Microsoft services (SharePoint Online, Teams) for credential theft and lateral movement
- **Impact**: Credential theft, persistence, and network lateral movement using legitimate Microsoft cloud services as C2 channels
- **Status**: Active threat disclosed by Ontinue; operates entirely within Microsoft 365 ecosystem
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Silent 'TwinLoot' Cyber Threat Operates Entirely From Microsoft's Cloud](https://www.darkreading.com/cloud-security/silent-twinloot-threat-operates-microsoft-cloud), [The Hacker News — TWINLOOT Abuses SharePoint and Teams to Steal Credentials and Move Across Networks](https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html)

### City Forum Campaign (Salesforce/ServiceNow Scraping)
- **Description**: Single infrastructure (158.220.87.79) scraping records from Salesforce and ServiceNow customer portals across multiple industries since 2025
- **Impact**: Unauthorized access to CRM and ITSM data across multiple industries for over a year
- **Status**: Ongoing campaign attributed to one server hosted on cloud infrastructure; named "City Forum" by Reco
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — One Attacker Has Scraped Both Salesforce and ServiceNow Portals Since 2025](https://thehackernews.com/2026/08/one-attacker-has-scraped-both.html)

### StubMaker RubyGems Typosquatting Campaign
- **Description**: 16 typosquatted RubyGems packages deploying Windows-based information stealer targeting browser credentials and cryptocurrency wallets
- **Impact**: Credential theft and cryptocurrency wallet compromise for Ruby developers installing malicious packages
- **Status**: Discovered August 15, 2026; packages include ubnuler, ubnlder, ri18nr, reaker, rakier, orakw, joxn, and others
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — 16 Typosquatted RubyGems Packages Steal Browser Credentials and Crypto Wallets](https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html)

### Evooo1Bot Linux Botnet
- **Description**: Mirai-derived botnet expanded with exploitation modules, credential theft capabilities, and reverse SOCKS relays turning compromised devices into persistent attacker infrastructure
- **Impact**: DDoS, credential theft, and persistent network access via compromised Linux/IoT devices
- **Status**: Active evolution beyond original Mirai capabilities with new exploitation modules
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — Linux Botnet Evooo1Bot Expands Mirai Capabilities Well Beyond DDoS](https://www.darkreading.com/cyber-risk/linux-botnet-evooo1bot-mirai-capabilities-beyond-ddos)

### Cavern C2 Framework (Iranian Nation-State)
- **Description**: Command-and-control framework using DNS tunneling and Google Apps Script to blend into legitimate traffic, deployed by Iranian nation-state hackers targeting Israeli entities
- **Impact**: Stealthy C2 communications, credential theft, and persistent access via trusted Google services
- **Status**: Active since December 2025; new components discovered by Kaspersky; attributed to Iranian threat actors
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic](https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html)

### Clop Ransomware Campaign
- **Description**: Clop ransomware gang claiming breaches of Philips and General Electric systems with data theft
- **Impact**: Data exfiltration and extortion targeting major industrial/technology corporations
- **Status**: Both companies investigating claims; active ransomware operation
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Philips and GE investigating Clop ransomware data theft claims](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)

### Azure Credential Theft Campaign
- **Description**: Threat actor selling 3.6 million employee records allegedly stolen from Microsoft Azure infrastructure of multiple Fortune 500 companies using compromised credentials
- **Impact**: Large-scale corporate credential compromise and data exposure across major enterprises
- **Status**: Active sales of stolen databases; initial access via compromised credentials
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hacker claims 3.6 million Azure account records stolen from major companies](https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/)

### Snowflake GitHub Actions Command Injection
- **Description**: Workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository allowing command execution via crafted GitHub issues leveraging internal Jira credentials
- **Impact**: Command execution in CI/CD pipeline with access to internal Jira credentials
- **Status**: Disclosed by Wiz researchers; present in .github/workflows/jira_issue.yml
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)

### SafePal Authorization Flaw
- **Description**: Authorization flaw in order-tracking plug-in exposing names, emails, shipping addresses, phone numbers, and purchase details of ~39,798 customers
- **Impact**: PII exposure for hardware wallet customers
- **Status**: Disclosed by SafePal; affected customers notified August 16, 2026
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [The Hacker News — SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers](https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html)

### MCP Server Secret Exposure
- **Description**: Model Context Protocol servers exposing enterprise secrets through plaintext configuration files, over-permissioned access, and prompt injection before security teams aware of deployment
- **Impact**: Silent exposure of enterprise secrets and credentials via AI agent infrastructure
- **Status**: Emerging risk as organizations adopt AI agents; no specific exploitation reported
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — How MCP Servers Can Expose Enterprise Secrets](https://thehackernews.com/2026/08/how-mcp-servers-can-expose-enterprise.html)

### Ransomware Actor Posing as Recovery Service
- **Description**: Ransomware affiliate masquerading as incident-recovery service to divert ransom payments from victims
- **Impact**: Financial fraud and continued extortion through social engineering
- **Status**: Active tactic observed by researchers; "Ransom Busters" branding
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — 'Ransom Busters': Ransomware Actor Poses as Incident-Recovery Service](https://www.darkreading.com/cyberattacks-data-breaches/ransom-busters-ransomware-actor-incident-recovery-service)

## Affected Systems and Products

- **Windows Task Host**: Windows systems targeted by ransomware gangs exploiting Task Host vulnerability
- **Ray Framework**: Open-source Python distributed computing framework for AI/ML (30k+ GitHub stars) with critical browser-based RCE
- **GitLab CE/EE**: Community and Enterprise Editions vulnerable to unauthenticated GraphQL project deletion (CVE-2026-19478)
- **Forminator Forms WordPress Plugin**: 600,000+ active installations vulnerable to unauthenticated RCE via PHP uploads (CVE-2026-15748)
- **Enterprise Certificate Authorities**: Windows PKI infrastructure vulnerable to standard user privilege escalation (CVE-2026-54121)
- **Unisoc Modem Firmware**: Android devices with Unisoc VoLTE video call capability; no vendor patch available
- **Microsoft 365 Ecosystem**: SharePoint Online, Teams, and Microsoft cloud services abused as C2 infrastructure by TWINLOOT
- **Salesforce Customer Portals**: Records scraped across multiple industries since 2025 via City Forum campaign
- **ServiceNow Customer Portals**: Records scraped alongside Salesforce via same infrastructure
- **RubyGems Repository**: 16 typosquatted packages (ubnuler, ubnlder, ri18nr, reaker, rakier, orakw, joxn, etc.) distributing Windows info stealer
- **Linux/IoT Devices**: Mirai-vulnerable devices recruited into Evooo1Bot with expanded exploitation modules
- **Google Workspace**: Google Apps Script abused for C2 communications by Cavern framework
- **DNS Infrastructure**: DNS tunneling used by Cavern C2 for stealthy communications
- **Snowflake Connector .NET Repository**: Public GitHub repository with vulnerable GitHub Actions workflow (jira_issue.yml)
- **SafePal Order Tracking**: Hardware wallet customer data exposed via authorization flaw in plug-in
- **MCP Server Deployments**: AI agent infrastructure exposing secrets via plaintext configs and prompt injection

## Attack Vectors and Techniques

- **Ransomware Exploitation of Windows Task Host**: Ransomware gangs leveraging CISA-confirmed actively exploited vulnerability for initial access and deployment
- **Browser-Based RCE via Ray Framework**: AI/ML workload infrastructure compromised through browser-accessible remote code execution
- **Unauthenticated GraphQL API Abuse**: GitLab public projects deleted/modified without authentication via GraphQL endpoint
- **Malicious PHP Upload RCE**: WordPress sites compromised through unauthenticated file upload in Forminator plugin
- **Certificate Authority Subversion**: Standard domain users escalating to Domain Controller via Enterprise CA misconfiguration
- **VoLTE Video Call Exploit Chain**: Two-stage kernel exploit delivered through legitimate video call answering on Unisoc modems
- **Living-off-the-Land Cloud C2**: TWINLOOT using SharePoint Online file operations and Teams for tasking and data exfiltration
- **Credential-Based Portal Scraping**: Long-term unauthorized access to Salesforce/ServiceNow using compromised credentials
- **Typosquatting Supply Chain Attack**: Malicious RubyGems packages mimicking legitimate names to steal browser credentials and crypto wallets
- **Mirai Evolution with Exploitation Modules**: Evooo1Bot adding vulnerability exploitation, credential theft, and SOCKS relay capabilities
- **DNS and Google Apps Script C2**: Iranian actors blending Cavern C2 traffic into legitimate DNS and Google service communications
- **GitHub Actions Workflow Injection**: Crafted issues triggering command execution in CI/CD pipelines with internal credentials
- **Ransomware Recovery Service Impersonation**: Affiliates posing as incident responders to intercept ransom payments
- **AI Agent Prompt File Propagation**: Self-replicating payloads spreading between autonomous agents through editable system prompt files

## Threat Actor Activities

- **Ransomware Gangs (Multiple)**: Actively exploiting Windows Task Host vulnerability confirmed by CISA; deploying ransomware across compromised environments
- **TWINLOOT Operators**: Deploying modular Python implant framework operating entirely within Microsoft 365 services for credential theft and lateral movement
- **City Forum Campaign Operator**: Single infrastructure (158.220.87.79) maintaining persistent access to Salesforce and ServiceNow portals across industries since 2025
- **StubMaker Campaign**: Publishing 16 typosquatted RubyGems packages distributing Windows information stealer targeting developers
- **Evooo1Bot Operators**: Evolving Mirai-based botnet with new exploitation modules, credential theft, and reverse SOCKS capabilities
- **Iranian Nation-State Actors (Cavern/Cav3rn)**: Deploying DNS and Google Apps Script-based C2 framework targeting Israeli entities since December 2025
- **Clop Ransomware Gang**: Claiming breaches of Philips and General Electric with data theft; both companies investigating
- **Azure Credential Threat Actor**: Selling 3.6 million employee records from Fortune 500 companies accessed via compromised Azure credentials
- **Ransomware Affiliate (Ransom Busters)**: Masquerading as incident-recovery service to divert ransom payments from victims
- **Anthropic/EPFL Researchers**: Demonstrating AI "mind virus" propagation between autonomous agents through persistent prompt files (research context)