---
schema_version: 2
report_date: 2026-09-28
generated_at: 2026-09-28T21:19:41Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-28/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity this period centers on two actively exploited Citrix NetScaler zero-day vulnerabilities (CVE-2026-88771 and CVE-2026-88772), which CISA has added to its Known Exploited Vulnerabilities catalog and mandated federal agencies to patch immediately. These remote code execution flaws affect default configurations and are under active global exploitation. Simultaneously, Apple has patched a CoreGraphics vulnerability (CVE-2026-86950) that may have been exploited in targeted attacks against older iOS, iPadOS, and macOS versions.

Ransomware and data theft campaigns continue to impact major organizations across sectors. Keio Corporation, a major Japanese railway operator, confirmed a ransomware attack disrupting business systems, while the Times Car car-sharing service disclosed a breach of 6.6 million user accounts. The Bitget cryptocurrency exchange suffered a $387.5 million theft attributed to North Korean actors exploiting a third-party security product flaw. The ShinyHunters extortion group has escalated operations following a Dutch arrest, exfiltrating FBI data and targeting Oracle PeopleSoft servers (CVE-2026-35273) using a WAF bypass technique.

Emerging threats feature AI-powered attack frameworks. The Carbonato botnet compromises exposed Docker hosts to deploy the Hermes AI agent for credential theft and command execution via Telegram. The JadePuffer (Storm-3168) threat actor leverages agentic AI and compromised Azure service principals for destructive cloud resource deletion. Infostealer campaigns have harvested AI credentials from over 80,000 organizations, enabling LLMjacking, while the RatHat Android banking trojan uses Gemini AI to prioritize high-value victims. The Poper Blocker Chrome extension, downloaded by millions, was revealed as spyware exfiltrating sensitive data.

## Active Exploitation Details

### CVE-2026-88771 - Citrix NetScaler ADC/Gateway Improper Input Validation
- **Description**: An improper input validation vulnerability in Citrix NetScaler ADC and NetScaler Gateway that allows an unauthenticated attacker to achieve remote code execution. The flaw affects every deployment on an affected version, including those in the default configuration.
- **Impact**: Unauthenticated remote code execution leading to full system compromise, lateral movement, and potential data exfiltration or ransomware deployment.
- **Status**: Actively exploited in the wild globally. Citrix has released security updates. CISA added to KEV catalog and ordered federal agencies to patch by September 30, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771
- **Reporting**: [The Hacker News — CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html), [Bleeping Computer — CISA orders feds to patch exploited Citrix flaws by Wednesday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/), [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### CVE-2026-88772 - Citrix NetScaler ADC/Gateway Remote Code Execution
- **Description**: A critical remote code execution vulnerability in Citrix NetScaler ADC and NetScaler Gateway. Citrix confirmed this flaw is being exploited in attacks alongside CVE-2026-88771.
- **Impact**: Remote code execution enabling attackers to take control of NetScaler appliances, pivot into internal networks, and deploy follow-on payloads.
- **Status**: Actively exploited in the wild. Citrix released security updates addressing this flaw along with six other vulnerabilities.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88772
- **Reporting**: [The Hacker News — CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html), [Bleeping Computer — CISA orders feds to patch exploited Citrix flaws by Wednesday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/), [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### CVE-2026-86950 - Apple CoreGraphics Out-of-Bounds Write
- **Description**: An out-of-bounds write vulnerability in the CoreGraphics component affecting older versions of iOS, iPadOS, and macOS. Processing a maliciously crafted file could trigger arbitrary code execution.
- **Impact**: Arbitrary code execution on target devices when users open malicious files, potentially leading to device compromise and data theft.
- **Status**: Apple states the vulnerability "may have been exploited in targeted attacks." Security updates released for affected operating systems.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [The Hacker News — Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks](https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html)

### CVE-2026-35273 - Oracle PeopleSoft Vulnerability
- **Description**: A vulnerability in Oracle PeopleSoft that the ShinyHunters extortion group is actively exploiting. Attackers use a URL-encoding trick to bypass web application firewall (WAF) rules designed to mitigate this flaw.
- **Impact**: Exploitation of vulnerable PeopleSoft servers enabling data theft and extortion. WAF bypass allows attacks to resume against previously protected servers.
- **Status**: Actively exploited by ShinyHunters in widespread campaigns against vulnerable servers.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-35273
- **Reporting**: [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)

### Keio Corporation Ransomware Attack
- **Description**: Ransomware attack targeting Keio Corporation, a major private railway operator in Japan, disrupting business systems over a weekend.
- **Impact**: Business system disruption affecting operations of a critical transportation infrastructure provider.
- **Status**: Active ransomware incident confirmed by the organization. Specific ransomware variant and initial access vector not disclosed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Japan's Keio confirms ransomware attack disrupted business systems](https://www.bleepingcomputer.com/news/security/japans-keio-confirms-ransomware-attack-disrupted-business-systems/)

### Times Car Data Breach
- **Description**: Cyberattack on Japanese car-sharing service Times Car resulting in compromise of approximately 6.6 million user accounts.
- **Impact**: Exposure of personal data for 6.6 million users including account credentials and potentially PII.
- **Status**: Breach confirmed by the organization. Attack vector and specific vulnerability not publicly disclosed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Times Car confirms data breach affecting 6.6 million user accounts](https://www.bleepingcomputer.com/news/security/times-car-confirms-data-breach-affecting-66-million-user-accounts/)

### Carbonato Botnet Docker Host Compromise
- **Description**: Botnet malware targeting exposed Docker daemons to deploy the open-source Hermes Agent AI framework. The implant installs the framework unchanged, then overwrites its SOUL.md persona file with a 39-line prompt directing it to execute tasks received through Telegram and steal AI API keys.
- **Impact**: Full compromise of Docker hosts, theft of AI API keys, persistent remote access via Telegram C2, and potential lateral movement to containerized workloads.
- **Status**: Active campaign disclosed by ThreatDown researchers. No patch required—mitigation involves securing Docker daemon exposure.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Carbonato Botnet Puts an AI Agent on Hacked Docker Hosts](https://www.darkreading.com/identity-access-management-security/carbonato-botnet-ai-agent-hacked-docker-hosts), [The Hacker News — Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

### NeedyMantis Persistent Access Malware
- **Description**: Malware family used by attackers to maintain long-term access in already-breached networks. Observed in targeted intrusions across telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors.
- **Impact**: Persistent foothold enabling extended espionage, data exfiltration, and follow-on exploitation over months or years.
- **Status**: Active use documented by Microsoft in targeted intrusions dating back to at least early 2026.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks](https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html)

### Bitget Third-Party Security Product Exploitation
- **Description**: Attackers exploited a vulnerability in a third-party security product used by Bitget cryptocurrency exchange to obtain high-level internal credentials, then sent fraudulent withdrawal commands to the wallet system, stealing approximately $387.5 million.
- **Impact**: Massive financial theft ($387.5M), compromise of exchange withdrawal systems, attribution to North Korean threat actors.
- **Status**: Attack completed September 24, 2026. Bitget has resumed Bitcoin withdrawals. The specific third-party product and CVE not disclosed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Says Attacker Exploited Third-Party Security Product Flaw to Steal $388M](https://thehackernews.com/2026/09/bitget-says-attacker-exploited-third.html), [Bleeping Computer — Bitget resumes Bitcoin withdrawals after $387.5 million crypto heist](https://www.bleepingcomputer.com/news/security/bitget-resumes-bitcoin-withdrawals-after-3875-million-crypto-heist/)

### RatHat Android Banking Trojan with AI Targeting
- **Description**: Android banking trojan distributed via malware-as-a-service model. Operators use a web console integrated with Google's Gemini AI to analyze stolen device data and identify higher-value victims. Nearly 100 console deployments traced since April 2026.
- **Impact**: Financial theft from Android users, credential harvesting, AI-enhanced victim prioritization increasing attack efficiency.
- **Status**: Active MaaS operations with ongoing deployments.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims](https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html)

### Poper Blocker Chrome Extension Spyware
- **Description**: Chrome Web Store extension masquerading as an ad blocker ("Poper Blocker") that exfiltrates sensitive user data. Downloaded by millions of users benefiting from Google's store approval.
- **Impact**: Large-scale surveillance and data theft from millions of browser users including browsing history, credentials, and sensitive personal information.
- **Status**: Active in Chrome Store at time of reporting. Researchers had warned Google prior to public disclosure.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Chrome Store Hosts 'Poper Blocker' Spyware Downloaded by Millions](https://www.darkreading.com/application-security/chrome-store-poper-blocker-spyware-downloaded-millions)

### JadePuffer / Storm-3168 Agentic Azure Attacks
- **Description**: Threat actor (tracked by Microsoft as Storm-3168) conducting agentic AI-driven attacks against Azure tenants. Uses compromised service principals to conduct reconnaissance, steal credentials, and destroy core cloud resources including storage, applications, and databases over an 18-hour period in early June 2026.
- **Impact**: Destructive deletion of Azure resources, credential theft, potential data exfiltration prior to destruction, operational disruption for targeted organizations.
- **Status**: Active campaign observed by Microsoft. Initial access via exposed credentials.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — JadePuffer agentic AI attacks target Azure, destroy cloud resources](https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/), [Dark Reading — JadePuffer AI Actor Compromises Azure Tenant in Destructive Cloud Attack](https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-azure-tenant-destructive-cloud-attack), [The Hacker News — JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources](https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html)

### ShinyHunters Extortion Campaign
- **Description**: Prolific hacking group conducting data theft and extortion operations. Following the arrest of a member in the Netherlands, remaining members escalated attacks—exfiltrating highly sensitive data from the FBI and extorting the Cl0p ransomware group. Also exploiting Oracle PeopleSoft CVE-2026-35273 with WAF bypass.
- **Impact**: High-profile data breaches, extortion of government and criminal entities alike, widespread exploitation of vulnerable PeopleSoft deployments.
- **Status**: Active and escalating campaign. Dutch authorities arrested a 23-year-old suspect linked to the group.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Dutch police confirm arrest in ShinyHunters hacking investigation](https://www.bleepingcomputer.com/news/security/dutch-police-confirm-arrest-in-shinyhunters-hacking-investigation/), [Krebs on Security — Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/), [Bleeping Computer — ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)

### US Soldier Multi-Company Extortion
- **Description**: Former U.S. Army soldier sentenced to 70 months for hacking and extorting at least 10 U.S. technology and telecommunications companies between April 2023 and December 2024.
- **Impact**: Compromise and extortion of 10+ tech/telecom firms over a 20-month period.
- **Status**: Perpetrator convicted and sentenced. Campaign concluded.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: none
- **Reporting**: [Bleeping Computer — US soldier gets 70 months in prison for extorting 10 tech, telecom firms](https://www.bleepingcomputer.com/news/security/us-soldier-gets-70-months-in-prison-for-extorting-10-tech-telecom-firms/)

### Infostealer AI Credential Harvesting (LLMjacking)
- **Description**: Infostealer malware campaigns harvesting AI platform credentials and session tokens from compromised systems. Over 80,000 corporate domains identified in stolen logs, enabling unauthorized AI access (LLMjacking) and conversation theft.
- **Impact**: Unauthorized use of corporate AI accounts, theft of proprietary conversations and data, financial loss from API abuse, potential pivot to further attacks.
- **Status**: Active underground market for stolen AI credentials documented by SOCRadar.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — 80,000+ Organizations Had AI Logins Stolen: From Shadow AI to LLMjacking](https://www.bleepingcomputer.com/news/security/80-000-plus-organizations-had-ai-logins-stolen-from-shadow-ai-to-llmjacking/)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: Vulnerability in Cloudflare Containers and Sandboxes allowing customers with Workers Paid accounts to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data leakage exposing sensitive information between Cloudflare customers.
- **Status**: Fixed by Cloudflare. No evidence of active exploitation reported.
- **Severity**: medium
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

### Supabase Database Misconfiguration Exposure
- **Description**: Over 16,000 misconfigured Supabase databases found exposing readable tables containing personally identifiable information, passwords, and authentication tokens.
- **Impact**: Mass exposure of sensitive authentication data and PII due to configuration errors, not software vulnerabilities.
- **Status**: Ongoing exposure at time of research. Requires configuration remediation by database owners.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Over 16,000 Supabase databases expose PII, passwords, auth tokens](https://www.bleepingcomputer.com/news/security/misconfigured-supabase-apps-expose-data-in-over-16-000-databases/)

## Affected Systems and Products

- **Citrix NetScaler ADC and NetScaler Gateway**: All versions affected by CVE-2026-88771 and CVE-2026-88772, including default configurations. Critical infrastructure, enterprise remote access, and application delivery deployments globally.
- **Apple iOS, iPadOS, macOS (older versions)**: Devices running unpatched versions vulnerable to CVE-2026-86950 CoreGraphics exploit via maliciously crafted files.
- **Oracle PeopleSoft**: Deployments vulnerable to CVE-2026-35273, particularly those relying on WAF rules that can be bypassed via URL encoding.
- **Docker Daemons**: Publicly exposed Docker API endpoints (TCP port 2375/2376) without authentication, targeted by Carbonato botnet for Hermes AI agent deployment.
- **Microsoft Azure Tenants**: Environments with exposed service principal credentials or weak identity controls, targeted by JadePuffer/Storm-3168 for destructive resource deletion.
- **Android Devices**: Users installing applications from unofficial sources or compromised legitimate apps delivering RatHat banking trojan.
- **Google Chrome Browser**: Users who installed the "Poper Blocker" extension (millions of downloads) from the Chrome Web Store.
- **Bitget Cryptocurrency Exchange**: Systems integrated with the vulnerable third-party security product (undisclosed) enabling credential theft and fraudulent withdrawals.
- **Keio Corporation Business Systems**: Internal network and business applications disrupted by ransomware.
- **Times Car Platform**: Car-sharing service infrastructure compromising 6.6 million user accounts.
- **Cloudflare Containers and Sandboxes**: Workers Paid account holders on shared physical hosts prior to the cross-tenant isolation fix.
- **Supabase PostgreSQL Databases**: Postgres instances with misconfigured Row Level Security (RLS) or overly permissive API keys exposing readable tables.
- **Enterprise AI Platforms**: Corporate accounts for OpenAI, Anthropic, and other LLM providers compromised via infostealer malware enabling LLMjacking.

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution via Input Validation Flaw**: Attackers send malicious packets to exposed Citrix NetScaler ADC/Gateway appliances exploiting CVE-2026-88771/CVE-2026-88772 for initial access without credentials.
  - **Vector**: Network-facing NetScaler management and gateway interfaces (typically port 443/8443).

- **WAF Bypass via URL Encoding**: ShinyHunters encodes attack payloads targeting Oracle PeopleSoft CVE-2026-35273 to evade web application firewall signature matching.
  - **Vector**: HTTP/HTTPS requests to PeopleSoft web applications with encoded exploit strings.

- **Exposed Docker Daemon API Exploitation**: Carbonato botnet scans for and connects to unauthenticated Docker daemon TCP sockets to deploy containers running the Hermes AI agent.
  - **Vector**: TCP ports 2375 (unencrypted) and 2376 (TLS) on internet-accessible hosts.

- **Compromised Service Principal Abuse**: JadePuffer/Storm-3168 uses stolen Azure service principal credentials (client IDs/secrets/certificates) to authenticate as legitimate automation identities.
  - **Vector**: Azure Resource Manager API, Microsoft Graph API, and Entra ID authentication endpoints.

- **Third-Party Security Product Credential Theft**: Bitget attackers exploited a flaw in a security appliance/service to harvest high-privilege internal credentials, then abused legitimate withdrawal APIs.
  - **Vector**: Vulnerable third-party security product management interface or API integration.

- **Malicious Browser Extension Data Exfiltration**: Poper Blocker extension requests broad permissions (host access, tabs, storage, webRequest) to harvest browsing data, credentials, and inject scripts.
  - **Vector**: Chrome Web Store installation → persistent browser context with elevated permissions.

- **AI-Enhanced Victim Profiling**: RatHat operators feed stolen device telemetry (contacts, SMS, app lists, wallet balances) into Gemini AI to score and prioritize high-value targets for manual fraud.
  - **Vector**: C2 console web interface with integrated LLM API calls.

- **Infostealer Credential Harvesting for AI Platform Access**: Information-stealing malware (RedLine, Lumma, Raccoon, etc.) extracts browser-stored cookies, session tokens, and saved passwords for AI service domains.
  - **Vector**: Compromised endpoint → credential store exfiltration → underground market resale → LLM API abuse.

- **Malware-as-a-Service Console Deployment**: RatHat operators deploy individualized web consoles per customer, each with independent victim databases and AI analytics.
  - **Vector**: Underground forum sales → console deployment on bulletproof hosting → victim Android infection via phishing/sideloading.

- **Agentic AI Autonomous Destruction**: JadePuffer employs AI-driven automation to enumerate Azure resources, identify high-value targets, and execute deletion commands at speed across subscriptions.
  - **Vector**: Authenticated Azure CLI/PowerShell/REST API sessions using compromised service principals.

- **Ransomware Deployment via Initial Access**: Keio Corporation attack likely began with phishing, VPN vulnerability exploitation, or valid credential abuse followed by lateral movement and encryption.
  - **Vector**: Undisclosed initial access → domain compromise → ransomware execution.

- **Supply Chain / Third-Party Compromise**: Bitget breach originated from a vulnerability in a security product vendor's software, demonstrating supply chain risk.
  - **Vector**: Trusted security product update or management channel.

## Threat Actor Activities

- **ShinyHunters**: Prolific data theft and extortion group. Recently escalated operations after Dutch law enforcement arrested a 23-year-old member (source-c919c2b059f3, source-e36cbd6c6f99). Exfiltrated sensitive FBI data and extorted the Cl0p ransomware gang. Actively exploiting Oracle PeopleSoft CVE-2026-35273 using URL-encoding WAF bypass (source-77ddfbcd4e34). Targets span government, corporate, and even criminal entities.

- **JadePuffer / Storm-3168**: Microsoft-tracked threat actor conducting "agentic" AI-driven destructive attacks against Azure tenants (source-178f19609d47, source-1820f6c11fcc, source-6170da865280). Uses compromised service principals for authentication, then deploys autonomous automation to enumerate and delete storage accounts, databases, applications, and other core resources. Campaign observed in early June 2026 lasting ~18 hours. Represents evolution toward AI-augmented destructive operations.

- **Carbonato Botnet Operators**: Threat actor(s) deploying the Carbonato botnet to compromise exposed Docker daemons globally (source-6c46ed3fad49, source-a2739f1e6c8a). Installs the open-source Hermes Agent AI framework, repurposes it via a custom SOUL.md prompt for Telegram C2 command execution and AI API key theft. Demonstrates rapid weaponization of legitimate AI agent frameworks for malicious automation.

- **North Korean Actors (attributed)**: Suspected Lazarus Group or affiliated DPRK operators behind the $387.5 million Bitget cryptocurrency exchange heist (source-cb8a6ba8d949, source-2098b2b0b957). Exploited a vulnerability in a third-party security product to steal administrative credentials, then initiated fraudulent withdrawals. Consistent with DPRK cryptocurrency theft campaigns funding state programs.

- **RatHat MaaS Operators**: Cybercriminal group running a malware-as-a-service operation for the RatHat Android banking trojan (source-4ca847aa2cb1). Deploys individualized web consoles per customer (~100 since April 2026). Innovates by integrating Google's Gemini AI to analyze victim device data and prioritize high-value targets for manual fraud. Represents AI-enhanced criminal business model.

- **NeedyMantis Operators**: Threat actor(s) deploying NeedyMantis malware for long-term persistent access in compromised networks (source-bef7f6a21fd6). Targets telecommunications, higher education, medical nonprofits, intergovernmental organizations, and defense contractors. Activity observed since at least early 2026. Focus on espionage and sustained access over immediate monetization.

- **US Army Soldier (Individual Actor)**: Former soldier convicted of hacking and extorting 10+ U.S. technology and telecommunications companies over 20 months (April 2023–December 2024) (source-55c3c36e526c). Sentenced to 70 months. Demonstrates insider threat and individual actor capability for sustained extortion campaigns.

- **Infostealer Distribution Networks**: Underground ecosystem harvesting and monetizing credentials from millions of infected endpoints (source-cdfc9fd9c096). SOCRadar identified AI platform credentials for 80,000+ corporate domains in stealer logs. Enables LLMjacking—unauthorized use of victim API keys for compute theft, data extraction, and further attacks.

- **Poper Blocker Developers**: Malicious extension authors who published spyware to the Chrome Web Store under the guise of an ad blocker (source-9ea947543a47). Achieved millions of installs leveraging Google's platform trust. Exfiltrated sensitive browsing data, credentials, and session information. Highlights supply chain risk in browser extension marketplaces.

- **Unknown Ransomware Actor (Keio Corporation)**: Unattributed ransomware group that disrupted Keio Corporation's business systems (source-ccc11f98d4a8). Targeting critical transportation infrastructure in Japan. Ransomware variant and affiliation not disclosed.

- **Unknown Actor (Times Car Breach)**: Unattributed threat actor responsible for the 6.6 million account breach at Japanese car-sharing service Times Car (source-12100c223846). Method and motive not publicly disclosed.