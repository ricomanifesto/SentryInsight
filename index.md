---
schema_version: 2
report_date: 2026-09-10
generated_at: 2026-09-10T11:47:56Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-10/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from network infrastructure and browser engines to endpoint security agents and AI gateways. CISA has confirmed ransomware groups are exploiting a WatchGuard Firebox RCE flaw, while Cisco has acknowledged active attacks against a maximum-severity authentication bypass in Secure Firewall Management Center (CVE-2026-20079). Google patched its seventh Chrome zero-day of the year (CVE-2026-87491), an out-of-bounds write in V8 enabling sandbox escape, and Microsoft Defender faces a new zero-day dubbed "ShieldCrash" that grants SYSTEM access and bypasses the recent ShieldBreak patch (CVE-2026-69414).

A previously undocumented exploit kit named BlueMoon—chaining Chrome and Windows vulnerabilities—has been deployed by four espionage-motivated threat groups within a single week, with initial attribution to China-aligned APT31. Simultaneously, AI infrastructure is under sustained assault: nearly 10% of internet-exposed LiteLLM gateways accept a documented default admin key, infostealers are harvesting replayable AI tokens to bypass MFA, and U.S. agencies accuse six Chinese firms of industrial-scale model distillation against frontier systems from OpenAI, Anthropic, Google, and xAI.

Healthcare and cryptocurrency sectors face acute threats. The ShinyHunters group exposed 4.1 million records in the AdaptHealth breach, while the Gentlemen ransomware gang claims a Veradigm compromise via a third-party vendor. Over 36,000 unpatched Plex servers remain exposed, Alby Hub Bitcoin wallets are vulnerable to takeover when internet-accessible, and a critical cPanel flaw allows mail-privileged accounts to execute code as root across all supported versions. Memory-resident malware on F5 BIG-IP APM appliances demonstrates advanced evasion techniques, injecting PHP web shells that survive disk forensics.

## Active Exploitation Details

### Cisco Secure Firewall Management Center Authentication Bypass
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Secure Firewall Management Center (FMC) software allows unauthenticated attackers to bypass authentication controls and gain administrative access to the management platform.
- **Impact**: Attackers can achieve full administrative control over the Secure Firewall Management Center, potentially compromising firewall policies, network configurations, and managed devices across the enterprise.
- **Status**: Actively exploited in attacks; Cisco has confirmed exploitation and released patches.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20079
- **Reporting**: [Bleeping Computer — Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/)

### Chrome V8 Zero-Day (CVE-2026-87491)
- **Description**: An out-of-bounds write vulnerability in the V8 JavaScript and WebAssembly engine of Google Chrome. The medium-severity flaw enables code execution within the browser sandbox and has been confirmed under active exploitation in the wild.
- **Impact**: Attackers can execute arbitrary code inside the Chrome sandbox, potentially escaping the sandbox through additional vulnerabilities or leveraging the sandboxed context for data theft, credential harvesting, or further browser-based attacks.
- **Status**: Actively exploited in the wild; Google released emergency patches as part of a 230-vulnerability update. This is the seventh Chrome zero-day patched in 2026.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87491
- **Reporting**: [The Hacker News — Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html), [Bleeping Computer — Google warns of new Chrome zero-day bug exploited in attacks](https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/)

### WatchGuard Firebox RCE Exploited in Ransomware Attacks
- **Description**: A critical remote code execution vulnerability in WatchGuard Firebox firewall appliances. CISA added this flaw to its Known Exploited Vulnerabilities catalog in December and has now confirmed ransomware gangs are actively leveraging it in intrusion campaigns.
- **Impact**: Remote code execution on perimeter firewall devices, enabling network infiltration, lateral movement, and ransomware deployment across compromised environments.
- **Status**: Actively exploited by ransomware groups; CISA-confirmed exploitation; patches available from WatchGuard.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA: WatchGuard RCE flaw now exploited in ransomware attacks](https://www.bleepingcomputer.com/news/security/cisa-watchguard-rce-flaw-now-exploited-in-ransomware-attacks/)

### Microsoft Defender ShieldCrash Zero-Day
- **Description**: A zero-day vulnerability in Microsoft Defender, codenamed "ShieldCrash," that grants SYSTEM-level access on affected Windows systems. The vulnerability functions as a patch bypass for CVE-2026-69414 (ShieldBreak, CVSS 7.8), which Microsoft addressed in a prior update but failed to fully remediate.
- **Impact**: Local privilege escalation to SYSTEM, enabling complete compromise of the endpoint, disablement of security controls, and persistence establishment.
- **Status**: Proof-of-concept exploit publicly released by researcher Nightmare Eclipse (also tracked as Chaotic Eclipse) immediately following September 2026 Patch Tuesday. Active exploitation status unconfirmed but exploit code is available.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access](https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/), [The Hacker News — Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed](https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html)

### BlueMoon Exploit Kit Campaign
- **Description**: A previously undocumented exploit kit chaining multiple vulnerabilities in Google Chrome and Microsoft Windows. The kit enables remote code execution through browser exploitation followed by local privilege escalation. First in-the-wild use attributed to APT31; three additional espionage groups deployed the same kit within one week.
- **Impact**: Full system compromise via drive-by download or targeted delivery, establishing persistent access for espionage operations. The rapid adoption by four distinct threat clusters suggests exploit kit availability on shared infrastructure or rapid reverse-engineering.
- **Status**: Actively exploited by at least four threat activity clusters; no vendor patches specifically addressing the kit's chained vulnerabilities have been announced.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week](https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html)

### LiteLLM Default Admin Key Exposure
- **Description**: Nearly 1 in 10 internet-exposed LiteLLM AI gateway instances accept the default administrator API key "sk-1234" documented in the project's own setup guide. LiteLLM serves as a proxy between applications and model providers, making it a high-value target.
- **Impact**: Full administrative control over the AI gateway, including access to all routed prompts, responses, model provider credentials, usage logs, and configuration. Attackers can intercept sensitive data, inject malicious prompts, or pivot to upstream model provider accounts.
- **Status**: Widespread exposure confirmed by Wiz Research scanning in February 2026; no authentication bypass vulnerability per se, but a critical configuration default being exploited at scale.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [The Hacker News — Nearly 1 in 10 Exposed LiteLLM Gateways Accepted the Example "sk-1234" Admin Key](https://thehackernews.com/2026/09/nearly-1-in-10-exposed-litellm-gateways.html)

### Skullcandy Dime 3 Bluetooth Hijacking
- **Description**: Skullcandy Dime 3 wireless earbuds accept Bluetooth pairing requests from nearby unpaired devices without requiring user interaction or confirmation, as warned by the Carnegie Mellon University CERT Coordination Center.
- **Impact**: Unauthorized device pairing enabling audio eavesdropping, injection of malicious audio, or potential exploitation of the Bluetooth stack on connected host devices.
- **Status**: Vulnerability disclosed by CERT/CC; no patch information provided; exploitation potential high in proximity-based scenarios.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Skullcandy Dime 3 earbuds expose users to Bluetooth hijacking](https://www.bleepingcomputer.com/news/security/skullcandy-dime-3-earbuds-expose-users-to-bluetooth-hijacking/)

### DeepSeek Harness Sandbox Escape
- **Description**: A flaw in DeepSeek Harness, the open-source tool for running AI coding agents in an OS-level sandbox, allows a sandboxed agent to disable its own sandbox restrictions with a single command via the tool's web API.
- **Impact**: AI agents executing untrusted code can break out of the intended containment, achieving full access to the developer's filesystem, environment variables, and local services.
- **Status**: Vulnerability disclosed; exploitation requires agent execution of a specific command; no reports of in-the-wild abuse.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval](https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html)

### Alby Hub Bitcoin Wallet Takeover
- **Description**: A critical flaw in Alby Hub (versions v1.7.0 through latest at time of disclosure) allows attackers to take over internet-exposed self-hosted Lightning wallets and transfer funds. The vulnerability is only exploitable when the Hub is reachable from the internet.
- **Impact**: Complete wallet compromise and fund theft for users who have exposed their Alby Hub instance to the internet without additional authentication layers.
- **Status**: Vulnerability disclosed by Alby; exploitation requires internet exposure; no confirmed exploitation reports.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets](https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html)

### cPanel Root Code Execution via Mail Privileges
- **Description**: An authenticated hosting account with mail-related privileges can create arbitrary files on the server through the EmailTrack feature and execute code as the root user. Every supported version of cPanel and WHM is affected.
- **Impact**: Full server compromise from a single compromised hosting account, affecting all tenants on shared infrastructure. Attackers can escalate from limited mail privileges to root access.
- **Status**: Patched by cPanel on September 8, 2026; active exploitation status unknown but high risk given shared hosting prevalence.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html)

### Plex Media Server Unpatched Vulnerabilities
- **Description**: Over 36,000 internet-exposed Plex Media Server instances remain unpatched against multiple recently disclosed security vulnerabilities, leaving them vulnerable to remote attacks.
- **Impact**: Depending on the specific vulnerabilities, attackers may achieve remote code execution, information disclosure, or authentication bypass on media servers that often have access to local networks and sensitive media libraries.
- **Status**: Mass exposure confirmed; patches available but widely unapplied; active exploitation not explicitly confirmed but highly probable given exposure scale.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Over 36,000 exposed Plex servers vulnerable to recent flaws](https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/)

## Affected Systems and Products

- **Cisco Secure Firewall Management Center (FMC)**: All versions vulnerable to CVE-2026-20079 authentication bypass; network security management appliances and virtual appliances.
- **Google Chrome**: All versions prior to the emergency update addressing CVE-2026-87491; Windows, macOS, Linux, ChromeOS, Android, and iOS platforms.
- **WatchGuard Firebox**: Firebox appliance models running vulnerable firmware versions; specific versions detailed in WatchGuard security advisory and CISA KEV entry.
- **Microsoft Defender / Windows**: Windows 10, Windows 11, Windows Server 2019/2022/2025 with Microsoft Defender Antivirus; ShieldCrash affects post-Patch Tuesday September 2026 builds.
- **LiteLLM**: Open-source AI gateway deployments exposed to the internet; all versions using default configuration with unchanged admin key.
- **Skullcandy Dime 3 Wireless Earbuds**: Hardware devices running vulnerable firmware; Bluetooth-enabled consumer audio products.
- **DeepSeek Harness**: Open-source AI agent sandboxing tool; developer workstations and CI/CD systems running the Harness runtime.
- **Alby Hub**: Self-hosted Lightning Network wallet software versions v1.7.0 through latest; Linux, macOS, Windows, Docker, and Raspberry Pi deployments.
- **cPanel & WHM**: All supported versions across shared hosting, VPS, and dedicated server environments; Linux-based web hosting control panels.
- **Plex Media Server**: All unpatched versions exposed to the internet; Windows, macOS, Linux, NAS devices (Synology, QNAP, ASUSTOR), Docker, and FreeBSD.
- **F5 BIG-IP Access Policy Manager (APM)**: Appliances compromised by memory-resident malware; specific versions targeted by the PHP web shell injection technique.
- **Frontier AI Models (OpenAI, Anthropic, Google, xAI)**: Model APIs and endpoints targeted by industrial-scale distillation extraction campaigns.

## Attack Vectors and Techniques

- **Exploit Kit Chaining (BlueMoon)**: Multi-vulnerability chains targeting Chrome renderer/V8 and Windows kernel/win32k components for remote code execution and privilege escalation in a single exploit flow.
- **Default Credential Exploitation**: Automated scanning and exploitation of documented default administrative credentials (LiteLLM "sk-1234") against internet-exposed management interfaces.
- **AI Token Theft via Infostealers**: Lumma Stealer, Vidar, and similar malware harvesting API keys, session tokens, and credentials from compromised endpoints to replay against AI provider APIs, bypassing MFA.
- **Model Distillation/Extraction**: Systematic, high-volume querying of frontier model APIs to extract reasoning traces, logits, and behavioral patterns for training competitor models—conducted at industrial scale by attributed threat groups.
- **Workflow Identity Hijacking**: Unauthenticated requests sent through identity propagation paths in AI/agent workflows to bypass authorization controls and access enterprise data stores.
- **Account Recovery Social Engineering**: Targeting service desk and automated recovery flows to reset MFA enrollments, leveraging weak identity verification procedures.
- **Memory-Resident Web Shell Injection**: Malware hooking Apache/PHP internals on F5 BIG-IP APM to inject PHP web shells exclusively in memory, evading file-based detection and forensic disk analysis.
- **Bluetooth Unauthorized Pairing**: Exploiting missing user confirmation in Bluetooth pairing protocol implementations to establish unauthorized connections to audio devices.
- **AI Agent Sandbox Escape**: Leveraging privileged tool APIs exposed to sandboxed AI agents to disable containment mechanisms from within the sandbox.
- **Ransomware Exploitation of Perimeter Devices**: Using RCE vulnerabilities in firewall/VPN appliances (WatchGuard) as initial access vectors for ransomware deployment.
- **Third-Party Vendor Compromise**: Supply chain attacks targeting email providers, healthcare vendors, and service providers to access downstream customer data (Trezor, Veradigm, AdaptHealth).

## Threat Actor Activities

- **APT31 (Bronze Vinewood / Judgement Panda / JungleBamboo)**: China-aligned state-sponsored group attributed as the first operator of the BlueMoon exploit kit, targeting Chrome and Windows vulnerabilities for espionage.
- **Three Additional Unnamed Spy Groups**: Deployed the same BlueMoon exploit kit within one week of initial APT31 activity, indicating shared exploit infrastructure, rapid reverse-engineering, or coordinated campaign.
- **ShinyHunters**: Data extortion group attributed to the AdaptHealth breach exposing 4.1 million individuals' data in a July 2026 cyberattack.
- **Gentlemen Ransomware Gang**: Claimed responsibility for a cybersecurity incident at a Veradigm third-party vendor resulting in patient data exposure.
- **Six Chinese AI Companies**: Accused by U.S. cybersecurity and intelligence agencies of conducting systematic, industrial-scale distillation attacks against OpenAI, Anthropic, Google Gemini, and xAI Grok models since late 2024.
- **Nightmare Eclipse / Chaotic Eclipse**: Security researcher(s) who developed and released the ShieldCrash zero-day exploit for Microsoft Defender and demonstrated a patch bypass for CVE-2026-69414 (ShieldBreak).
- **Lumma Stealer / Vidar Operators**: Information stealer malware campaigns harvesting AI provider API keys, session tokens, and credentials from infected endpoints for resale or direct use in AI account takeover.
- **Ransomware Affiliates (Unspecified Groups)**: Actively exploiting the WatchGuard Firebox RCE vulnerability (per CISA) for initial access in ransomware intrusion campaigns.
- **Xinbi Guarantee Operators**: Chinese organized crime groups operating a scam marketplace with Telegram infrastructure and cryptocurrency wallets, disrupted by U.S. DoJ with $52.8M seized and operations in Madagascar dismantled.