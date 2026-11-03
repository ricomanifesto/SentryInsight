---
schema_version: 2
report_date: 2026-08-18
generated_at: 2026-08-18T18:55:02Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-18/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from AI/ML platforms and enterprise software to cloud infrastructure and industrial systems. CISA has added two high-impact flaws to its Known Exploited Vulnerabilities catalog—a critical Ray distributed computing framework vulnerability enabling browser-based remote code execution and a high-severity Windows Task Host vulnerability now leveraged by ransomware gangs. Simultaneously, critical unauthenticated RCE vulnerabilities in GitLab (CVE-2026-19478, CVSS 9.4) and the widely deployed Forminator WordPress plugin (CVE-2026-15748, CVSS 9.8) have been patched but require immediate deployment given their exploitation potential.

Threat actor activity shows increasing sophistication in living-off-the-land and cloud-native tradecraft. The Clop ransomware gang has developed a custom Java web shell targeting PTC Windchill and FlexPLM servers with built-in credential decryption and repository enumeration capabilities. A novel Python implant framework dubbed TWINLOOT operates its entire command-and-control infrastructure within trusted Microsoft services including SharePoint Online and Teams, while the Iranian-linked Cavern C2 framework leverages DNS and Google Apps Script to blend into legitimate traffic. The "City Forum" campaign has scraped Salesforce and ServiceNow portals across multiple industries for over a year from a single infrastructure IP, and a typosquatting campaign on RubyGems ("StubMaker") has deployed 16 malicious packages stealing browser credentials and cryptocurrency wallets.

Emerging attack surfaces in AI ecosystems are being actively researched and exploited. Microsoft Copilot Personal contains three vulnerabilities ("CoSnitch") enabling single-click data exfiltration from connected applications via an undocumented URL parameter. Researchers have demonstrated self-propagating "mind viruses" spreading between AI agents through persistent prompt files, while the MLflow AI platform and FUXA SCADA software face active scanning and exploitation of critical SSRF flaws. A credential-based intrusion campaign claims 3.6 million Azure account records stolen from Fortune 500 companies, and the Certighost vulnerability (CVE-2026-54121) allows standard domain users to escalate Enterprise Certificate Authorities to Domain Controller equivalence, highlighting persistent PKI trust boundary failures.

## Active Exploitation Details

### Microsoft Copilot Personal CoSnitch Vulnerabilities
- **Description**: Three vulnerabilities in Microsoft Copilot Personal collectively named CoSnitch that leverage an undocumented URL parameter surfaced by the assistant itself. A single click on a crafted link can silently exfiltrate data from connected apps and other information available to the victim's Copilot session.
- **Impact**: Silent data exfiltration from all connected applications and Copilot-accessible information without user interaction beyond clicking a link.
- **Status**: Disclosed by Varonis Threat Labs; patch status not specified in source.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps](https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html)

### MLflow Critical SSRF Vulnerability
- **Description**: Critical Server-Side Request Forgery vulnerability in MLflow, an open-source AI/ML platform, allowing attackers to steal cloud credentials and secrets through malicious scanning and exploitation.
- **Impact**: Theft of cloud credentials and secrets from MLflow deployments; active exploitation campaigns observed.
- **Status**: Actively exploited in the wild per watchTowr and VulnCheck reports; patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

### FUXA SCADA/HMI Critical Vulnerability
- **Description**: Critical vulnerability in FUXA, an open-source web-based SCADA/HMI software for operational technology and industrial automation, subject to malicious scanning and exploitation.
- **Impact**: Potential compromise of OT/industrial automation systems; active exploitation campaigns observed.
- **Status**: Actively exploited in the wild per watchTowr and VulnCheck reports; patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

### Clop Custom Windchill Web Shell
- **Description**: Custom Java web shell specifically designed for PTC Windchill and FlexPLM servers with built-in features to decrypt credentials, enumerate file repositories, and steal files, likely linked to the Clop ransomware gang.
- **Impact**: Targeted data theft from Windchill/FlexPLM installations including credential decryption, repository enumeration, and file exfiltration.
- **Status**: Active deployment in Clop ransomware operations; no vendor patch mentioned for the web shell itself.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Clop created custom web shell for Windchill data theft attacks](https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/)

### Windows Task Host Vulnerability (CISA KEV)
- **Description**: High-severity Windows Task Host vulnerability confirmed by CISA as actively exploited by ransomware gangs, originally flagged as actively exploited in April.
- **Impact**: Ransomware deployment and system compromise via Windows Task Host exploitation.
- **Status**: CISA-confirmed active exploitation by ransomware gangs; added to KEV catalog.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA: Windows Task Host flaw now exploited by ransomware gangs](https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/)

### Ray Critical Browser-Based RCE (CISA KEV)
- **Description**: Critical flaw in Ray, an open-source Python-native distributed computing framework for AI/ML workloads, that can trigger browser-based remote code execution. CISA added to KEV catalog citing evidence of active exploitation.
- **Impact**: Browser-based remote code execution affecting Ray distributed computing clusters used for AI/ML workloads.
- **Status**: CISA-confirmed active exploitation; added to KEV catalog; patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE](https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html)

### Unisoc Modem Video Call Exploit Chain
- **Description**: Two vulnerabilities in Unisoc modems that can be chained to take over an Android device by delivering a payload when the victim answers a video call.
- **Impact**: Full Android device compromise via video call interaction; zero-click or one-click exploitation depending on implementation.
- **Status**: Proof-of-concept demonstrated by researchers; active exploitation status not confirmed in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Dark Reading — Video Call Exploit Chains Two Flaws in Unisoc Modems](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)

### GitLab GraphQL Critical Vulnerability (CVE-2026-19478)
- **Description**: Critical vulnerability in GitLab Community Edition and Enterprise Edition GraphQL implementation allowing unauthenticated attackers to remotely modify or delete public projects and user data under certain conditions.
- **Impact**: Unauthenticated remote modification or deletion of public projects and user data; CVSS 9.4.
- **Status**: Security updates released by GitLab; exploitation in wild not explicitly confirmed.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-19478
- **Reporting**: [The Hacker News — Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

### Forminator WordPress Plugin RCE (CVE-2026-15748)
- **Description**: Critical unauthenticated remote code execution vulnerability in Forminator Forms WordPress plugin (600,000+ active installations) via malicious PHP file uploads.
- **Impact**: Unauthenticated arbitrary code execution on vulnerable WordPress sites; CVSS 9.8.
- **Status**: Disclosed by security researcher; patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-15748
- **Reporting**: [The Hacker News — Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

### Certighost Enterprise CA Privilege Escalation (CVE-2026-54121)
- **Description**: Vulnerability allowing a standard domain user to turn an Enterprise Certificate Authority into a Domain Controller, exposing fundamental PKI trust boundary failures.
- **Impact**: Full domain compromise via PKI privilege escalation; standard user to Domain Controller equivalence.
- **Status**: Patch available; described as "the easy part" with deeper architectural lessons needed.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-54121
- **Reporting**: [Bleeping Computer — Certighost and the Privilege Hiding in Your Certificate Authority](https://www.bleepingcomputer.com/news/security/certighost-and-the-privilege-hiding-in-your-certificate-authority/)

### Snowflake GitHub Actions Workflow Injection
- **Description**: GitHub Actions workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository (.github/workflows/jira_issue.yml) allowing crafted GitHub issues to execute commands with internal Jira credentials.
- **Impact**: Command execution in CI/CD pipeline with access to internal Jira credentials; supply chain compromise vector.
- **Status**: Disclosed by Wiz researchers; patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)

### SafePal Authorization Flaw
- **Description**: Authorization flaw in an order-tracking plug-in exposing names, email addresses, shipping addresses, phone numbers, and purchase details of approximately 39,798 customers.
- **Impact**: PII and order data exposure for nearly 40,000 hardware wallet customers.
- **Status**: Disclosed by SafePal; affected customers notified individually via email on August 16.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [The Hacker News — SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers](https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html)

### TWINLOOT Microsoft Cloud Implant Framework
- **Description**: Modular, PyArmor-hardened Python implant framework operating its entire command-and-control infrastructure inside trusted Microsoft services (SharePoint Online, Teams) for credential theft and lateral movement.
- **Impact**: Stealthy credential theft, persistence, and network lateral movement entirely within legitimate Microsoft cloud infrastructure.
- **Status**: Active deployment documented by Ontinue researchers; no vendor patch applicable.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Silent 'TwinLoot' Cyber Threat Operates Entirely From Microsoft's Cloud](https://www.darkreading.com/cloud-security/silent-twinloot-threat-operates-microsoft-cloud), [The Hacker News — TWINLOOT Abuses SharePoint and Teams to Steal Credentials and Move Across Networks](https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html)

### City Forum Salesforce/ServiceNow Scraping Campaign
- **Description**: Long-running campaign scraping records from Salesforce and ServiceNow customer portals across multiple industries since 2025, traced to single infrastructure IP 158.220.87.79.
- **Impact**: Unauthorized access to customer portal data across multiple industries; sustained access for over one year.
- **Status**: Active campaign documented by Reco researchers; ongoing as of publication.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — One Attacker Has Scraped Both Salesforce and ServiceNow Portals Since 2025](https://thehackernews.com/2026/08/one-attacker-has-scraped-both.html)

### StubMaker RubyGems Typosquatting Campaign
- **Description**: Typosquatting campaign on RubyGems with 16 malicious packages (ubnuler, ubnlder, ri18nr, reaker, rakier, orakw, joxn, and others) deploying Windows-based information stealer targeting browser credentials and cryptocurrency wallets.
- **Impact**: Credential and cryptocurrency wallet theft from developers installing typosquatted packages.
- **Status**: Active campaign discovered August 15, 2026 by OpenSourceMalware; packages published to RubyGems.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — 16 Typosquatted RubyGems Packages Steal Browser Credentials and Crypto Wallets](https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html)

### Cavern C2 Framework (Iranian Nation-State)
- **Description**: Evolving Cavern/Cav3rn command-and-control framework used by Iranian nation-state hackers targeting entities in Israel, leveraging DNS and Google Apps Script to blend into legitimate traffic.
- **Impact**: Stealthy persistent access to Israeli targets; C2 infrastructure camouflaged within legitimate Google/DNS traffic.
- **Status**: Active since December 2025 per Kaspersky monitoring; new components discovered.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic](https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html)

### Evooo1Bot Linux Botnet
- **Description**: Linux botnet expanding Mirai capabilities with exploitation modules, credential theft, and reverse SOCKS relays to turn compromised devices into persistent attacker infrastructure.
- **Impact**: DDoS plus persistent access, credential theft, and proxy infrastructure from compromised Linux/IoT devices.
- **Status**: Active evolution documented; exploitation modules indicate active vulnerability targeting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — Linux Botnet Evooo1Bot Expands Mirai Capabilities Well Beyond DDoS](https://www.darkreading.com/cyber-risk/linux-botnet-evooo1bot-mirai-capabilities-beyond-ddos)

### Azure Credential Theft Campaign
- **Description**: Threat actor selling employee databases allegedly stolen from Microsoft Azure infrastructure of multiple Fortune 500 companies after gaining access using compromised credentials.
- **Impact**: 3.6 million Azure account records claimed stolen; Fortune 500 compromise via credential reuse/theft.
- **Status**: Actor actively selling data; compromise method confirmed as credential-based.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hacker claims 3.6 million Azure account records stolen from major companies](https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/)

### AI Agent Prompt Injection "Mind Viruses"
- **Description**: Self-propagating payloads spreading between AI agents through editable system prompt files that autonomous agent harnesses use to carry state between sessions.
- **Impact**: Cross-agent malware propagation in multi-agent AI systems; persistent compromise of agent memory/state.
- **Status**: Demonstrated in simulated six-agent coding environment by Anthropic and EPFL researchers; preprint released August 10, 2026.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — AI "Mind Viruses" Can Spread Between Agents Through Persistent Prompt Files](https://thehackernews.com/2026/08/ai-mind-viruses-can-spread-between.html)

### Ransom Busters Extortion Campaign
- **Description**: Ransomware affiliate posing as incident-recovery service, proactively emailing victims offering to delete stolen data from ransomware groups' servers for $20,000-$60,000.
- **Impact**: Secondary extortion of ransomware victims; potential double-dip on ransom payments; diversion of recovery funds.
- **Status**: Active campaign spotted by GuidePoint Research; anomalous incident-recovery impersonation.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Ransom Busters Claims It Hacked Ransomware Servers, Asks Victims for Up to $60,000](https://thehackernews.com/2026/08/ransom-busters-claims-it-hacked.html), [Dark Reading — 'Ransom Busters': Ransomware Actor Poses as Incident-Recovery Service](https://www.darkreading.com/cyberattacks-data-breaches/ransom-busters-ransomware-actor-incident-recovery-service)

### Pokémon Center Third-Party Breach
- **Description**: Third-party data breach via CEVA Logistics exposing customer personal and order information for Pokémon Center customers in the United Kingdom and Germany.
- **Impact**: Customer PII and order data exposure; some orders cancelled.
- **Status**: Breach confirmed; notification to UK/Germany customers in progress.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Pokémon Center data breach exposes customer info, cancels some orders](https://www.bleepingcomputer.com/news/security/pokemon-center-data-breach-exposes-customer-info-cancels-some-orders/)

## Affected Systems and Products

- **Microsoft Copilot Personal**: All versions with connected apps functionality; exploitation via undocumented URL parameter
- **MLflow**: Open-source AI/ML platform deployments; critical SSRF vulnerability under active exploitation
- **FUXA SCADA/HMI**: Open-source web-based industrial automation software; critical vulnerability in OT environments
- **PTC Windchill and FlexPLM**: Enterprise PLM servers targeted by Clop custom Java web shell with credential decryption capabilities
- **Windows Task Host**: Windows systems vulnerable to high-severity flaw exploited by ransomware gangs (CISA KEV)
- **Ray Distributed Computing Framework**: Python-native AI/ML workload clusters; critical browser-based RCE (CISA KEV)
- **Unisoc Modems**: Android devices with Unisoc baseband processors; video call exploit chain
- **GitLab CE/EE**: All versions prior to security update; GraphQL vulnerability CVE-2026-19478
- **Forminator Forms WordPress Plugin**: Versions prior to patch; 600,000+ active installations; CVE-2026-15748
- **Enterprise Certificate Authorities**: Windows Server PKI deployments; CVE-2026-54121 allows standard user to DC equivalence
- **Snowflake snowflake-connector-net Repository**: GitHub Actions workflows using vulnerable jira_issue.yml
- **SafePal Order-Tracking Plug-in**: Authorization flaw exposing ~39,798 customer records
- **Microsoft 365 (SharePoint Online, Teams)**: Abused as C2 infrastructure by TWINLOOT implant framework
- **Salesforce and ServiceNow Customer Portals**: Scraped by City Forum campaign since 2025 via IP 158.220.87.79
- **RubyGems Package Registry**: 16 typosquatted packages (StubMaker campaign) distributing Windows info stealer
- **Google Apps Script and DNS Infrastructure**: Abused by Iranian Cavern C2 framework for traffic camouflage
- **Linux/IoT Devices**: Targeted by Evooo1Bot botnet with expanded Mirai exploitation modules
- **Microsoft Azure Tenants**: Fortune 500 companies compromised via credential theft; 3.6M records claimed
- **Autonomous AI Agent Systems**: Multi-agent harnesses using editable system prompt files; vulnerable to cross-agent prompt injection
- **CEVA Logistics Systems**: Third-party breach affecting Pokémon Center UK/Germany customer data

## Attack Vectors and Techniques

- **Single-Click Data Exfiltration (CoSnitch)**: Crafted links with undocumented URL parameters trigger silent data extraction from Copilot-connected applications
- **SSRF Cloud Credential Theft**: Server-Side Request Forgery in MLflow leveraged to access cloud metadata services and steal credentials/secrets
- **Custom Industrial Web Shell**: Java web shell purpose-built for Windchill/FlexPLM with credential decryption, repository enumeration, and file theft
- **Ransomware Task Host Exploitation**: Ransomware gangs leveraging Windows Task Host vulnerability for initial access/privilege escalation
- **Browser-Based RCE via Distributed Computing**: Ray framework flaw enables remote code execution through browser interaction with AI/ML clusters
- **Zero-Click Video Call Exploit**: Chained Unisoc modem vulnerabilities enable Android takeover via incoming video call
- **Unauthenticated GraphQL Mutation**: GitLab GraphQL flaw allows project deletion/modification without authentication under specific conditions
- **Unauthenticated PHP Upload RCE**: Forminator WordPress plugin accepts malicious PHP files leading to arbitrary code execution
- **PKI Privilege Escalation (Certighost)**: Standard domain user manipulates Enterprise CA to gain Domain Controller-level privileges
- **GitHub Actions Workflow Injection**: Crafted GitHub issues trigger command execution in CI/CD pipelines with internal credentials
- **Living-Off-The-Land Cloud C2**: TWINLOOT operates entire C2 infrastructure within SharePoint Online and Teams, using legitimate Microsoft services for tasking and exfiltration
- **Long-Term Portal Scraping**: City Forum campaign maintains persistent unauthorized access to Salesforce/ServiceNow portals for over one year
- **Typosquatting Supply Chain Attack**: RubyGems packages with names similar to legitimate libraries deliver Windows information stealers
- **DNS/Google Apps Script C2 Camouflage**: Iranian Cavern framework blends malicious traffic into legitimate DNS and Google service requests
- **Mirai-Derived Botnet Expansion**: Evooo1Bot adds exploitation modules, credential theft, and reverse SOCKS to turn IoT devices into persistent infrastructure
- **Credential-Based Cloud Intrusion**: Azure compromise via stolen/reused credentials yielding 3.6M account records from Fortune 500 companies
- **Cross-Agent Prompt Injection**: Self-propagating payloads spread through editable system prompt files in multi-agent AI systems
- **Ransomware Affiliate Impersonation**: Ransom Busters poses as incident-recovery service to extort victims already hit by ransomware
- **Third-Party Logistics Breach**: CEVA Logistics compromise cascades to Pokémon Center customer data in UK/Germany
- **WMIC LOLBin Removal**: Microsoft proactively removing Windows Management Instrumentation Command-line tool abused by cybercriminals

## Threat Actor Activities

- **Clop Ransomware Gang**: Developed and deployed custom Java web shell for PTC Windchill/FlexPLM servers with advanced credential decryption and data enumeration capabilities; active data theft operations
- **TWINLOOT Operators**: Deploy modular PyArmor-hardened Python implant framework operating C2 entirely within Microsoft SharePoint Online and Teams; credential theft and lateral movement campaigns
- **City Forum Campaign Operator**: Single infrastructure (158.220.87.79) scraping Salesforce and ServiceNow portals across multiple industries since 2025; sustained unauthorized access
- **StubMaker/OpensSourceMalware Actors**: Published 16 typosquatted RubyGems packages distributing Windows information stealer targeting browser credentials and crypto wallets
- **Iranian Nation-State Actors (Cavern/Cav3rn)**: Evolving C2 framework using DNS and Google Apps Script for traffic camouflage; targeting Israeli entities since December 2025 per Kaspersky
- **Evooo1Bot Botnet Operators**: Expanding Mirai-derived Linux botnet with exploitation modules, credential theft, and reverse SOCKS relays for persistent infrastructure
- **Azure Credential Theft Actor**: Selling 3.6 million employee records allegedly stolen from Fortune 500 Microsoft Azure environments via compromised credentials
- **Ransom Busters Affiliate**: Posing as incident-recovery service to extort ransomware victims for $20K-$60K; diverting recovery payments; spotted by GuidePoint Research
- **MLflow/FUXA Exploitation Actors**: Conducting malicious scanning and exploitation of critical vulnerabilities in AI/ML platform and OT SCADA software per watchTowr and VulnCheck
- **SafePal Data Exposure**: Authorization flaw in order-tracking plug-in exposed ~39,798 customer records; not attributed to specific threat actor
- **Pokémon Center/CEVA Logistics Breach**: Third-party logistics provider compromise affecting UK/Germany customer data; actor not identified
- **Anthropic/EPFL Researchers**: Demonstrated AI "mind viruses" self-propagating between agents via prompt files; defensive research publication