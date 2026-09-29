---
schema_version: 2
report_date: 2026-09-29
generated_at: 2026-09-29T03:25:56Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-29/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity is surging across multiple vectors, with two Citrix NetScaler zero-day vulnerabilities (CVE-2026-88771 and CVE-2026-88772) now confirmed under active global exploitation and added to CISA's Known Exploited Vulnerabilities catalog. Federal agencies have been ordered to patch by Wednesday.

Simultaneously, Apple has patched a CoreGraphics flaw (CVE-2026-86950) that may have been exploited in targeted attacks against older iOS, iPadOS, and macOS versions. A high-severity zero-day in the TDengine time-series database—widely deployed across industrial, energy, automotive, and IoT environments—allows server crash with a single packet, posing immediate risk to operational technology sectors.

## Active Exploitation Details

### Citrix NetScaler ADC and Gateway RCE Zero-Days
- **Description**: Two critical remote code execution vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway. CVE-2026-88771 is an improper input validation flaw (CVSS 9.5) allowing unauthenticated attackers to execute arbitrary code. CVE-2026-88772 is a companion RCE vulnerability. One of the two affects every deployment on an affected version, including default configurations.
- **Impact**: Unauthenticated remote code execution leading to full appliance compromise, lateral movement, and data theft.
- **Status**: Actively exploited in the wild globally. Citrix has released security updates for both vulnerabilities plus six additional flaws. CISA has added both to the KEV catalog and ordered U.S. federal agencies to patch immediately.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-88771, CVE-2026-88772
- **Reporting**: [The Hacker News — CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html), [Bleeping Computer — CISA orders feds to patch exploited Citrix flaws by Wednesday](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/), [Bleeping Computer — Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/), [The Hacker News — Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

### Apple CoreGraphics Out-of-Bounds Write
- **Description**: An out-of-bounds write vulnerability in the CoreGraphics component affecting older versions of iOS, iPadOS, and macOS. Processing a maliciously crafted file can trigger arbitrary code execution.
- **Impact**: Arbitrary code execution on targeted devices via malicious file processing.
- **Status**: Apple has released security updates. Apple stated the vulnerability "may have been exploited in targeted attacks."
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-86950
- **Reporting**: [The Hacker News — Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks](https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html)

### TDengine Time-Series Database Zero-Day
- **Description**: A high-severity zero-day vulnerability in the TDengine time-series database used across industrial, IoT, energy, and automotive environments. A single malformed packet can crash OT servers.
- **Impact**: Denial of service against critical operational technology infrastructure; potential for further exploitation.
- **Status**: Zero-day with no patch mentioned in reporting. Actively exploitable with minimal complexity (one packet).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — One Packet Can Crash OT Servers in Industrial Sectors](https://www.darkreading.com/ics-ot-security/one-packet-crash-servers-tdengine)

### Carbonato Botnet Docker Daemon Compromise
- **Description**: The Carbonato botnet targets exposed Docker daemons to deploy the open-source Hermes Agent AI framework. The implant overwrites the framework's SOUL.md persona file with a 39-line prompt directing it to execute tasks received through Telegram and steal AI API keys.
- **Impact**: Full compromise of Docker hosts, theft of AI API keys, persistent backdoor via Telegram-controlled AI agent.
- **Status**: Active botnet campaign observed by ThreatDown researchers. No vendor patch required; exploitation relies on exposed Docker daemons.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Carbonato Botnet Puts an AI Agent on Hacked Docker Hosts](https://www.darkreading.com/identity-access-management-security/carbonato-botnet-ai-agent-hacked-docker-hosts), [The Hacker News — Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

### NeedyMantis Persistent Access Malware
- **Description**: A malware family used by hackers to maintain long-term access in already-breached networks. Observed in a small number of targeted intrusions against telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors. Activity dates back to at least 2022.
- **Impact**: Persistent foothold enabling extended espionage, data exfiltration, and lateral movement.
- **Status**: Active use in targeted intrusions. Microsoft tracks this activity.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks](https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html)

### JADEPUFFER (Storm-3168) Azure Destructive Attacks
- **Description**: The threat actor JADEPUFFER (tracked by Microsoft as Storm-3168) conducts agent-driven attacks against Azure tenants using compromised service principals. Operations include reconnaissance, credential theft, and destructive deletion of core cloud components—storage, applications, and databases. A observed attack in early June 2026 lasted approximately 18 hours.
- **Impact**: Complete destruction of Azure resources, data loss, service disruption, potential extortion.
- **Status**: Active destructive campaign. Microsoft has published technical analysis.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — JadePuffer agentic AI attacks target Azure, destroy cloud resources](https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/), [Dark Reading — JadePuffer AI Actor Compromises Azure Tenant in Destructive Cloud Attack](https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-azure-tenant-destructive-cloud-attack), [The Hacker News — JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources](https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html)

### Bitget Third-Party Security Product Exploitation
- **Description**: Attackers exploited a vulnerability in a third-party security product used by cryptocurrency exchange Bitget to obtain high-level internal credentials, then issued fraudulent withdrawal commands stealing approximately $388 million. Suspected North Korean attribution.
- **Impact**: Massive financial theft ($388M), credential compromise, potential supply chain risk for other users of the unnamed security product.
- **Status**: Exploitation confirmed by Bitget. Withdrawals resumed after investigation. Third-party product vendor not publicly identified.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Bitget Says Attacker Exploited Third-Party Security Product Flaw to Steal $388M](https://thehackernews.com/2026/09/bitget-says-attacker-exploited-third.html), [Bleeping Computer — Bitget resumes Bitcoin withdrawals after $387.5 million crypto heist](https://www.bleepingcomputer.com/news/security/bitget-resumes-bitcoin-withdrawals-after-3875-million-crypto-heist/)

### ShinyHunters Data Theft and Extortion Campaign
- **Description**: The ShinyHunters hacking group continues large-scale data theft and extortion operations. Following the arrest of a 23-year-old alleged member in the Netherlands, remaining members dramatically escalated attacks, stealing highly sensitive data from the FBI and extorting the Russian ransomware group Cl0p.
- **Impact**: High-value data breaches, extortion of government and criminal entities, ongoing credential and PII theft.
- **Status**: Active and escalating campaign. Dutch authorities investigating; one arrest made.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Dutch police confirm arrest in ShinyHunters hacking investigation](https://www.bleepingcomputer.com/news/security/dutch-police-confirm-arrest-in-shinyhunters-hacking-investigation/), [Krebs on Security — Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/)

### RatHat Android Banking Trojan (Malware-as-a-Service)
- **Description**: RatHat operators build and publish an Android banking trojan controlled via a web console that uses Google's Gemini AI to identify higher-value victims. Nearly 100 console deployments traced since April 2026, operating under a malware-as-a-service model where each customer runs a separate copy.
- **Impact**: Financial theft, credential harvesting, PII exfiltration from Android devices; AI-enhanced victim prioritization.
- **Status**: Active MaaS operation with growing deployment count.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims](https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html)

### Poper Blocker Chrome Extension Spyware
- **Description**: A purported ad-blocker extension hosted on the Chrome Web Store exfiltrates sensitive user data while benefiting from Google's implied approval. Downloaded by millions of users despite researcher warnings.
- **Impact**: Mass surveillance of browsing activity, credential theft, PII exfiltration affecting millions of users.
- **Status**: Active in Chrome Store at time of reporting. Google's response not detailed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Chrome Store Hosts 'Poper Blocker' Spyware Downloaded by Millions](https://www.darkreading.com/application-security/chrome-store-poper-blocker-spyware-downloaded-millions)

### Cloudflare Containers Cross-Tenant Data Exposure
- **Description**: A vulnerability in Cloudflare Containers and Sandboxes allowed customers with a Workers Paid account to recover residual data from other customers' containers on the same physical host.
- **Impact**: Cross-tenant data leakage exposing customer secrets, code, and configurations.
- **Status**: Cloudflare has fixed the vulnerability.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/)

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: All deployments on affected versions, including default configurations. Critical infrastructure, enterprise remote access, and application delivery controllers globally.
- **Apple iOS, iPadOS, macOS**: Older versions prior to the security updates addressing CVE-2026-86950. Specific version ranges not detailed in reporting.
- **TDengine Time-Series Database**: Versions deployed across industrial control systems, IoT platforms, energy sector SCADA/historian systems, automotive telemetry, and manufacturing OT environments.
- **Docker Daemons**: Exposed Docker Engine APIs (TCP port 2375/2376) without authentication or TLS, allowing unauthenticated container deployment.
- **Microsoft Azure**: Tenants with compromised service principals, particularly those with excessive permissions or lacking conditional access policies.
- **Third-Party Security Product (unnamed)**: Used by Bitget and potentially other cryptocurrency exchanges and enterprises; vendor and product not publicly disclosed.
- **Android Devices**: Devices installing applications from untrusted sources or compromised legitimate apps delivering the RatHat banking trojan.
- **Google Chrome Browser**: Users who installed the "Poper Blocker" extension from the Chrome Web Store.
- **Cloudflare Containers and Sandboxes**: Customers using Workers Paid plans with containers deployed prior to the fix.
- **Supabase Database Instances**: Over 16,000 misconfigured projects exposing readable tables with PII, passwords, and authentication tokens due to anonymous access enabled.

## Attack Vectors and Techniques

- **Unauthenticated RCE via Single Packet**: Citrix NetScaler flaws (CVE-2026-88771/88772) and TDengine zero-day allow pre-authentication remote code execution or crash with minimal network interaction.
- **Exposed Management Interfaces**: Carbonato botnet scans for and exploits unauthenticated Docker daemon APIs—a persistent cloud/container misconfiguration pattern.
- **Compromised Service Principals**: JADEPUFFER/Storm-3168 leverages stolen or leaked Azure service principal credentials for initial access and destructive operations.
- **AI-Agent Weaponization**: Carbonato deploys Hermes Agent AI framework controlled via Telegram; JadePuffer uses "agentic" automation for reconnaissance and destruction; RatHat console uses Gemini AI for victim triage.
- **Malicious File Parsing**: Apple CoreGraphics flaw triggered by processing crafted image/font files—classic client-side exploitation via messaging, email, or web.
- **Supply Chain / Third-Party Product Exploitation**: Bitget breach originated from a vulnerability in a security product the exchange relied upon, highlighting transitive trust risk.
- **Malware-as-a-Service (MaaS)**: RatHat operates affiliate model with per-customer console deployments; Carbonato uses off-the-shelf AI framework as implant.
- **Browser Extension Supply Chain**: Poper Blocker masquerades as legitimate ad-blocker in official Chrome Store, abusing extension permissions for data exfiltration.
- **Cross-Tenant Container Escape**: Cloudflare flaw allowed residual data recovery from shared physical hosts—a cloud multi-tenancy boundary violation.
- **Infostealer-Driven Credential Harvesting**: Over 80,000 organizations had AI platform credentials (OpenAI, Anthropic, etc.) stolen via infostealer logs, enabling LLMjacking and shadow AI abuse.

## Threat Actor Activities

- **JADEPUFFER / Storm-3168**: Destructive Azure-focused threat actor using compromised service principals for automated reconnaissance, credential theft, and resource deletion. Microsoft attributes June 2026 attack to this group. Evolution of tradecraft toward "agentic" AI-driven operations.
- **ShinyHunters**: Prolific data theft and extortion group. Despite Dutch arrest of a 23-year-old member, remaining operators escalated to breach FBI systems and extort Cl0p ransomware group. High-profile targeting of government and criminal entities alike.
- **Carbonato Botnet Operators**: Campaign targeting exposed Docker hosts globally to deploy Telegram-controlled Hermes AI agents for API key theft and persistent access. Technical sophistication in repurposing legitimate AI frameworks.
- **RatHat MaaS Operators**: Android banking trojan distributors using AI-enhanced victim selection (Gemini) and web-based C2 consoles. Nearly 100 affiliate deployments since April 2026.
- **North Korean Actors (suspected)**: Attributed by Bitget and industry analysts to the $388M cryptocurrency exchange heist via third-party security product exploit. Consistent with Lazarus Group tradecraft targeting crypto financial infrastructure.
- **NeedyMantis Operators**: Targeted intrusion actors maintaining long-term access in telecommunications, education, healthcare, intergovernmental, and defense industrial base sectors since at least 2022. Microsoft-tracked activity.
- **Poper Blocker Developers**: Malicious extension publishers abusing Chrome Web Store trust to deploy spyware to millions of users under guise of ad-blocking functionality.
- **Unknown Actor (Keio Railway Ransomware)**: Ransomware attack disrupting business systems of major Japanese private railway operator Keio Corporation. Attribution not established.
- **Unknown Actor (Times Car Breach)**: Compromise of 6.6 million user accounts at Japanese car-sharing service Times Car. Method and attribution not disclosed.
- **U.S. Army Soldier (convicted)**: Former soldier sentenced to 70 months for hacking and extorting 10+ U.S. technology and telecommunications companies (2023-2024). Insider threat / lone actor case.