---
schema_version: 2
report_date: 2026-09-29
generated_at: 2026-09-29T09:30:10Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-29/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, from enterprise networking and mobile operating systems to cloud infrastructure and AI-driven attack frameworks. CISA has added two critical Citrix NetScaler flaws to its Known Exploited Vulnerabilities catalog following confirmed global exploitation, mandating emergency patching for federal agencies. Apple has patched a CoreGraphics zero-day (CVE-2026-86950) exploited in highly sophisticated targeted attacks against iOS devices, while Kiteworks lifted a system shutdown advisory after remediating a critical flaw in its platform. Simultaneously, threat actors are leveraging compromised credentials, misconfigurations, and novel AI-powered tooling—including the Carbonato botnet deploying Hermes Agent on exposed Docker hosts and the JadePuffer/Storm-3168 actor conducting destructive Azure tenant takeovers—to achieve high-impact breaches such as the $388 million Bitget cryptocurrency heist and the theft of AI credentials from over 80,000 organizations.

Ransomware and data extortion campaigns remain pervasive, with Japan's Keio Corporation railway systems disrupted, Times Car exposing 6.6 million user records, and the ShinyHunters group escalating attacks against the FBI and rival ransomware operators following a key arrest. The NeedyMantis malware family enables persistent access across telecommunications, government, and healthcare sectors, while the RatHat Android banking trojan incorporates generative AI for victim prioritization. Supply chain and third-party risks are underscored by the Bitget breach originating from a security product vulnerability and the widespread exposure of sensitive data across 16,000+ misconfigured Supabase databases. Malicious Chrome extensions with millions of downloads further demonstrate the expanding attack surface through trusted software distribution channels.

## Active Exploitation Details

### CVE-2026-86950 - Apple CoreGraphics Zero-Day
- **Description**: An out-of-bounds write vulnerability in the CoreGraphics component affecting older versions of iOS, iPadOS, and macOS. Processing a maliciously crafted file can lead to arbitrary code execution.
- **Impact**: Arbitrary code execution on targeted iOS devices through crafted file processing, enabling full device compromise in sophisticated attack chains.
- **Status**: Actively exploited in targeted attacks; Apple has released security updates addressing the flaw.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [Bleeping Computer — Apple patches CoreGraphics zero-day flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/apple-patches-coregraphics-zero-day-flaw-exploited-in-attacks/), [The Hacker News — Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks](https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html)

### CVE-2026-88771 - Citrix NetScaler ADC/Gateway Improper Input Validation
- **Description**: An improper input validation vulnerability in Citrix NetScaler ADC and Gateway that allows an unauthenticated attacker to exploit the system remotely.
- **Impact**: Unauthenticated remote compromise of critical enterprise networking infrastructure providing VPN and application delivery services.
- **Status**: Actively exploited globally; added to CISA Known Exploited Vulnerabilities catalog with emergency patching directive for federal agencies.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771
- **Reporting**: [The Hacker News — CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html), [Bleeping Computer — CISA orders feds to patch exploited Citrix flaws by Wednesday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/)

### Kiteworks Critical Vulnerability
- **Description**: A critical vulnerability in the Kiteworks platform that prompted the vendor to issue a precautionary advisory asking customers to shut down systems until a patch was deployed.
- **Impact**: Potential full compromise of Kiteworks content governance and secure file sharing systems used by enterprise customers.
- **Status**: Patched; vendor lifted shutdown advisory after deploying fixes and bringing customer systems back online.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Kiteworks patches critical flaw, brings customer systems online](https://www.bleepingcomputer.com/news/security/kiteworks-lifts-shutdown-warning-after-patching-critical-flaw/)

### MCP Python SDK OAuth Credential Theft
- **Description**: A flaw in the official Model Context Protocol (MCP) Python SDK where affected versions transmit the client secret, authorization code, and PKCE proof key to an attacker-controlled token endpoint when interacting with a malicious MCP server.
- **Impact**: Theft of OAuth credentials used to authenticate to legitimate services, enabling unauthorized access to connected applications and data.
- **Status**: Fixed in version 1.30.0 and later; maintainers issued security advisory detailing the vulnerability.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials](https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html)

### TDengine Time-Series Database Zero-Day
- **Description**: A high-severity zero-day vulnerability in TDengine, a time-series database widely deployed across industrial, IoT, energy, and automotive operational technology environments. A single malicious packet can crash OT servers.
- **Impact**: Denial of service and potential instability in critical industrial control systems and operational technology infrastructure.
- **Status**: Zero-day disclosed; no patch mentioned in source reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Dark Reading — One Packet Can Crash OT Servers in Industrial Sectors](https://www.darkreading.com/ics-ot-security/one-packet-crash-servers-tdengine)

### Carbonato Botnet Docker Daemon Exploitation
- **Description**: The Carbonato botnet targets exposed Docker daemons to deploy the open-source Hermes Agent AI framework, overwriting its SOUL.md persona file with a 39-line prompt directing it to execute commands received via Telegram and steal AI API keys.
- **Impact**: Full compromise of Docker hosts, theft of AI service credentials, and persistent remote control through an AI agent framework.
- **Status**: Actively compromising exposed Docker hosts; researchers have observed deployments since April 2026.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Carbonato Botnet Puts an AI Agent on Hacked Docker Hosts](https://www.darkreading.com/identity-access-management-security/carbonato-botnet-ai-agent-hacked-docker-hosts), [The Hacker News — Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

### Bitget Third-Party Security Product Flaw
- **Description**: Attackers exploited a vulnerability in a third-party security product used by the Bitget cryptocurrency exchange to obtain high-level internal credentials, which were then used to send fraudulent withdrawal commands to the wallet system.
- **Impact**: Theft of approximately $388 million in cryptocurrency; suspected North Korean state-sponsored attribution.
- **Status**: Actively exploited in September 2026; Bitget resumed Bitcoin withdrawals after incident response.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Says Attacker Exploited Third-Party Security Product Flaw to Steal $388M](https://thehackernews.com/2026/09/bitget-says-attacker-exploited-third.html), [Bleeping Computer — Bitget resumes Bitcoin withdrawals after $387.5 million crypto heist](https://www.bleepingcomputer.com/news/security/bitget-resumes-bitcoin-withdrawals-after-3875-million-crypto-heist/)

### JadePuffer/Storm-3168 Azure Service Principal Compromise
- **Description**: The JadePuffer threat actor (tracked by Microsoft as Storm-3168) uses compromised service principals to conduct destructive operations in Microsoft Azure tenants, including reconnaissance, credential theft, and deletion of core cloud resources such as storage, applications, and databases over an 18-hour period.
- **Impact**: Destructive compromise of Azure cloud environments with data destruction and infrastructure deletion.
- **Status**: Observed in active intrusions since at least June 2026; Microsoft characterizes it as an evolution of the actor's tradecraft.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — JadePuffer agentic AI attacks target Azure, destroy cloud resources](https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/), [Dark Reading — JadePuffer AI Actor Compromises Azure Tenant in Destructive Cloud Attack](https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-azure-tenant-destructive-cloud-attack), [The Hacker News — JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources](https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html)

### NeedyMantis Persistent Access Malware
- **Description**: A malware family used to maintain long-term access in already-breached networks, observed in targeted intrusions against telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors.
- **Impact**: Persistent foothold enabling extended espionage, data exfiltration, and lateral movement across high-value targets.
- **Status**: Active use in targeted campaigns dating back to at least 2024; Microsoft technical analysis published.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks](https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html)

### RatHat Android Banking Trojan with AI Targeting
- **Description**: An Android banking trojan distributed through a malware-as-a-service model, controlled via a web console that uses Google's Gemini AI to identify higher-value victims from infected devices.
- **Impact**: Financial theft, credential harvesting, and personalized targeting of nearly 100 separate console deployments since April 2026.
- **Status**: Actively deployed and operated as a service; Cleafy traced console activity.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims](https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html)

### Poper Blocker Chrome Extension Spyware
- **Description**: A purported ad-blocker extension on the Chrome Web Store that exfiltrates sensitive user data while benefiting from Google's platform approval, downloaded by millions of users.
- **Impact**: Large-scale surveillance and data theft from browser activity, including potentially sensitive personal and corporate information.
- **Status**: Actively distributed through official Chrome Store with millions of installations; researcher warnings noted.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Chrome Store Hosts 'Poper Blocker' Spyware Downloaded by Millions](https://www.darkreading.com/application-security/chrome-store-poper-blocker-spyware-downloaded-millions)

### ShinyHunters Data Theft and Extortion Campaign
- **Description**: The ShinyHunters hacking group conducts large-scale data theft and extortion operations, dramatically escalating attacks—including theft of sensitive FBI data and extortion of the Cl0p ransomware group—following the arrest of a suspected member.
- **Impact**: High-profile data breaches, extortion of government and criminal entities, and continued proliferation of stolen data markets.
- **Status**: Actively escalating operations as of September 2026; Dutch authorities arrested a 23-year-old suspect linked to the group.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Dutch police confirm arrest in ShinyHunters hacking investigation](https://www.bleepingcomputer.com/news/security/dutch-police-confirm-arrest-in-shinyhunters-hacking-investigation/), [Krebs on Security — Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/)

### Supabase Database Misconfiguration Exposure
- **Description**: Over 16,000 misconfigured Supabase databases expose readable tables containing personally identifiable information, passwords, and authentication tokens due to improper access controls.
- **Impact**: Mass exposure of sensitive authentication credentials and personal data across thousands of organizations using the platform.
- **Status**: Discovered by researchers; ongoing exposure requiring configuration remediation by affected organizations.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Over 16,000 Supabase databases expose PII, passwords, auth tokens](https://www.bleepingcomputer.com/news/security/misconfigured-supabase-apps-expose-data-in-over-16-000-databases/)

### AI Credential Theft and LLMjacking
- **Description**: Infostealer malware logs have exposed AI account credentials and active sessions tied to more than 80,000 corporate domains, enabling unauthorized access to generative AI services and potential LLMjacking—hijacking of AI model access for malicious use.
- **Impact**: Compromise of enterprise AI subscriptions, theft of proprietary conversations and data, and resale of AI access on underground markets.
- **Status**: Actively harvested via infostealers; SOCRadar analysis identifies growing market for stolen AI logins.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — 80,000+ Organizations Had AI Logins Stolen: From Shadow AI to LLMjacking](https://www.bleepingcomputer.com/news/security/80-000-plus-organizations-had-ai-logins-stolen-from-shadow-ai-to-llmjacking/)

### Keio Corporation Ransomware Attack
- **Description**: A ransomware attack against Keio Corporation, a major private railway operator in Japan, disrupting business systems over a weekend period.
- **Impact**: Operational disruption to critical transportation infrastructure business systems; potential data theft alongside encryption.
- **Status**: Confirmed by victim organization; investigation ongoing.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Japan's Keio confirms ransomware attack disrupted business systems](https://www.bleepingcomputer.com/news/security/japans-keio-confirms-ransomware-attack-disrupted-business-systems/)

### Times Car Data Breach
- **Description**: A cyberattack compromising approximately 6.6 million user accounts at the Japanese car-sharing service Times Car.
- **Impact**: Large-scale exposure of customer personal data; potential credential stuffing and identity theft risks for affected users.
- **Status**: Confirmed by organization; breach disclosed late September 2026.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Times Car confirms data breach affecting 6.6 million user accounts](https://www.bleepingcomputer.com/news/security/times-car-confirms-data-breach-affecting-66-million-user-accounts/)

## Affected Systems and Products

- **Kiteworks Platform**: Enterprise content governance and secure file sharing systems; all versions prior to patched release
- **Apple iOS, iPadOS, macOS**: Older versions lacking the CoreGraphics security update (CVE-2026-86950)
- **Citrix NetScaler ADC and Gateway**: Versions affected by CVE-2026-88771 and a second critical flaw; enterprise VPN and application delivery controllers
- **MCP Python SDK**: Versions prior to 1.30.0; applications integrating with Model Context Protocol servers
- **TDengine Time-Series Database**: Deployments across industrial control systems, IoT platforms, energy sector OT, and automotive manufacturing environments
- **Docker Engine/Daemon**: Exposed Docker API endpoints accessible without authentication; hosts running container workloads
- **Bitget Cryptocurrency Exchange**: Internal wallet management systems; third-party security product integration (specific product unnamed)
- **Microsoft Azure**: Tenants with compromised service principals; Azure Resource Manager, storage accounts, databases, and application registrations
- **Android Devices**: Devices installing malicious applications delivering the RatHat banking trojan; Google Play and third-party app stores
- **Google Chrome Browser**: Installations with the "Poper Blocker" extension (millions of downloads); browser sync and stored credential data
- **Supabase PostgreSQL Databases**: Projects with misconfigured Row Level Security or public schema permissions; over 16,000 identified instances
- **Enterprise AI Platform Accounts**: Corporate subscriptions to generative AI services (OpenAI, Anthropic, etc.) compromised via infostealer malware
- **Keio Corporation IT Systems**: Business operations and potential operational technology for railway management
- **Times Car Platform**: User account database and car-sharing service infrastructure serving 6.6 million customers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Use of previously unknown vulnerabilities (CVE-2026-86950, TDengine flaw) in targeted attacks against high-value targets before patches are available
- **Credential Theft via Malicious Protocol Implementation**: MCP Python SDK flaw redirects OAuth secrets to attacker-controlled endpoints during legitimate authorization flows
- **Single-Packet Denial of Service**: One malformed network packet crashes TDengine database servers in OT environments without authentication
- **Exposed Management Interface Exploitation**: Carbonato botnet scans for and compromises unauthenticated Docker daemon APIs to deploy AI agent payloads
- **Third-Party Supply Chain Compromise**: Attackers exploit vulnerabilities in security products integrated into target environments (Bitget) to pivot to core systems
- **Cloud Identity Abuse**: JadePuffer/Storm-3168 leverages compromised service principals with excessive permissions to destroy Azure resources at scale
- **AI-Enhanced Victim Profiling**: RatHat operators use Gemini AI within their C2 console to analyze stolen device data and prioritize high-value targets
- **Malicious Browser Extension Distribution**: Poper Blocker masquerades as legitimate ad-blocking software on the official Chrome Web Store to achieve mass installation
- **Infostealer-Driven Credential Harvesting**: Mass collection of AI service credentials from infected endpoints, fueling LLMjacking and unauthorized model access
- **Ransomware Deployment**: Encryption and disruption of critical business systems (Keio) and mass data exfiltration for extortion (Times Car, ShinyHunters)
- **Service Account and Principal Compromise**: Attackers target non-human identities with broad permissions (service principals, API keys) for lateral movement and destruction
- **Malware-as-a-Service Operations**: RatHat and Carbonato demonstrate commoditized attack frameworks with AI-enhanced capabilities sold to affiliates

## Threat Actor Activities

- **JadePuffer / Storm-3168**: Agentic threat actor conducting destructive Azure tenant compromises using compromised service principals; observed in June 2026 operations lasting ~18 hours with reconnaissance, credential theft, and resource deletion; Microsoft tracks as evolution of tradecraft
- **ShinyHunters**: Prolific data theft and extortion group; Dutch authorities arrested a 23-year-old suspect in September 2026; remaining members escalated attacks against FBI systems and extorted Cl0p ransomware group in retaliation
- **Carbonato Botnet Operators**: Deploy Hermes Agent AI framework on compromised Docker hosts via Telegram C2; steal AI API keys; operate since at least April 2026 with automated AI-driven post-exploitation
- **RatHat Operators**: Run malware-as-a-service for Android banking trojan; ~100 console deployments since April 2026; integrate Gemini AI for victim value assessment; Cleafy attributes to organized cybercrime
- **North Korean State-Sponsored Actors (suspected)**: Attributed to $388M Bitget cryptocurrency heist via third-party security product exploit; used stolen credentials for fraudulent withdrawal commands
- **NeedyMantis Operators**: Maintain persistent access in telecommunications, university, medical nonprofit, intergovernmental, and government contractor networks; activity tracked by Microsoft since at least 2024
- **Poper Blocker Developers**: Distribute spyware-adware hybrid through Chrome Web Store to millions; exfiltrate browsing data, credentials, and sensitive information under guise of ad blocking
- **US Army Soldier (convicted)**: Former soldier sentenced to 70 months for hacking and extorting 10 U.S. technology and telecommunications companies between April 2023 and December 2024
- **Cl0p Ransomware Group**: Targeted by ShinyHunters for extortion following ShinyHunters member arrest; indicates cross-group conflict in cybercrime ecosystem
- **Infostealer Operators (various)**: Harvest AI credentials from 80,000+ corporate domains; feed underground markets for LLMjacking and unauthorized AI service access