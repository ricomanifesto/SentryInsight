---
schema_version: 2
report_date: 2026-09-09
generated_at: 2026-09-09T20:48:22Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-09/
---
# Exploitation Report

## Executive Summary

Microsoft's September 2026 Patch Tuesday set a historic record with 974 vulnerabilities addressed, including two actively exploited Windows zero-days and over 110 critical-severity flaws. Simultaneously, Google patched its seventh Chrome zero-day of the year (CVE-2026-87491), an out-of-bounds write in the V8 engine actively exploited in the wild. These mass patching events coincide with the discovery of BlueMoon, a previously undocumented exploit kit chaining multiple Windows and Chrome vulnerabilities that has been deployed by four distinct espionage groups—including China-aligned APT31—within a single week.

Critical infrastructure remains under direct assault. CISA added CVE-2026-86218, a pre-authentication RCE in N-able N-central (CVSS 10.0), to its Known Exploited Vulnerabilities catalog with an immediate patch deadline for federal agencies. SAP disclosed CVE-2026-44756, a maximum-severity memory corruption flaw in Extended Passport Processing enabling unauthenticated remote code execution. Meanwhile, a Microsoft Defender zero-day dubbed ShieldCrash grants SYSTEM access and demonstrates that the prior ShieldBreak patch (CVE-2026-69414) was insufficient, with a public proof-of-concept now circulating.

Beyond traditional software exploits, adversaries are weaponizing AI supply chains and identity frameworks at scale. U.S. intelligence agencies accuse six Chinese AI firms of conducting industrial-scale distillation attacks since late 2024, systematically extracting billions of tokens from frontier models including GPT, Claude, Gemini, and Grok. Concurrently, infostealers such as Lumma Stealer and Vidar are harvesting replayable AI API tokens that bypass MFA, while attackers hijack workflow identities and abuse account recovery flows to compromise enterprise environments. Financial crime operations continue to evolve, with the Xinbi Guarantee scam marketplace disrupted after facilitating Chinese organized crime and the DoppelCart network operating 119,000 fake storefronts for credit card theft.

## Active Exploitation Details

### Chrome V8 Zero-Day (CVE-2026-87491)
- **Description**: An out-of-bounds write vulnerability in V8, Google Chrome's JavaScript and WebAssembly engine, affecting versions prior to the September 2026 stable channel update. The flaw allows code execution within the Chrome sandbox.
- **Impact**: Attackers can execute arbitrary code inside the sandboxed renderer process, providing a foothold for sandbox escape chains or data theft from compromised web sessions.
- **Status**: Actively exploited in the wild; patch released as part of Google's September 2026 update addressing 230 total vulnerabilities.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87491
- **Reporting**: [The Hacker News — Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html), [Bleeping Computer — Google warns of new Chrome zero-day bug exploited in attacks](https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/)

### Microsoft Defender ShieldCrash Zero-Day
- **Description**: A zero-day vulnerability in Microsoft Defender, codenamed ShieldCrash, that grants SYSTEM-level access. The flaw represents a patch bypass for CVE-2026-69414 (ShieldBreak, CVSS 7.8), which Microsoft attempted to address in a prior update.
- **Impact**: Local privilege escalation to SYSTEM, enabling full control of the affected endpoint, tampering with Defender, and persistence.
- **Status**: Public proof-of-concept exploit released by researcher Chaotic Eclipse immediately after September 2026 Patch Tuesday; the earlier ShieldBreak patch is confirmed insufficient.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access](https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/), [The Hacker News — Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed](https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html)

### SAP Extended Passport Processing RCE (CVE-2026-44756)
- **Description**: A memory corruption vulnerability in SAP Extended Passport (EPP) Processing, rated CVSS 10.0, allowing unauthenticated remote code execution. Discovered and reported internally by SAP.
- **Impact**: Complete compromise of confidentiality, integrity, and availability of affected SAP applications without requiring authentication.
- **Status**: Security updates released by SAP; no public exploitation reported at time of disclosure.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-44756
- **Reporting**: [The Hacker News — SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution](https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html)

### N-able N-central Pre-Auth RCE (CVE-2026-86218)
- **Description**: A maximum-severity (CVSS 10.0) pre-authentication remote code execution flaw in N-able N-central remote monitoring and management software.
- **Impact**: Unauthenticated attackers can achieve full remote code execution on the N-central server, potentially compromising all managed endpoints.
- **Status**: Added to CISA KEV catalog on September 9, 2026; Federal Civilian Executive Branch agencies required to patch by September 11, 2026. Actively exploited in the wild.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86218
- **Reporting**: [The Hacker News — N-able N-central Pre-Auth RCE Flaw Exploited in the Wild](https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html)

### BlueMoon Exploit Kit (Windows & Chrome Vulnerability Chain)
- **Description**: A previously undocumented exploit kit chaining multiple vulnerabilities in Microsoft Windows and Google Chrome. First in-the-wild use attributed to APT31, with three additional espionage clusters deploying it within a week.
- **Impact**: Full compromise of target systems through chained browser and OS exploits, enabling espionage, data exfiltration, and persistence.
- **Status**: Actively deployed by at least four distinct threat activity clusters; specific CVE identifiers for chained vulnerabilities not publicly disclosed in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week](https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html)

### Microsoft Windows Zero-Days (September 2026 Patch Tuesday)
- **Description**: Two distinct Windows zero-day vulnerabilities actively exploited in the wild, addressed in Microsoft's record 974-fix Patch Tuesday release. Specific CVE identifiers not provided in source reporting.
- **Impact**: Remote code execution and/or privilege escalation on affected Windows versions; exploitation confirmed by Microsoft.
- **Status**: Patches available as of September 2026 Patch Tuesday; active exploitation confirmed prior to patch release.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html), [Krebs on Security — Microsoft Plugs Nearly 1,000 Security Holes](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/), [Dark Reading — Patch Tuesday Sets Another Record With 974 CVEs](https://www.darkreading.com/vulnerabilities-threats/patch-tuesday-another-record-974-cves)

### cPanel Mail Privilege Escalation to Root
- **Description**: An authenticated hosting account with mail-related privileges can create arbitrary files via EmailTrack and execute code as root, affecting every supported version of cPanel and WHM.
- **Impact**: Complete server takeover from a single compromised hosting account; lateral movement to all hosted sites and data.
- **Status**: Advisory published September 8, 2026; patches available for all supported versions.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html)

### DeepSeek Harness Sandbox Escape
- **Description**: A flaw in DeepSeek Harness, an open-source tool for running AI coding agents, allowing a sandboxed agent to disable its own file sandbox with a single command via the tool's web API.
- **Impact**: AI agents operating on untrusted code can escape containment and write arbitrary files on the host developer machine.
- **Status**: Flaw disclosed; patch status not specified in reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval](https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html)

### Alby Hub Bitcoin Wallet Takeover
- **Description**: A critical flaw in Alby Hub (versions v1.7.0 through unspecified) allowing attackers to take over internet-exposed self-hosted Lightning wallets and transfer funds.
- **Impact**: Full theft of bitcoin funds from wallets where the owner made the Hub reachable from the internet.
- **Status**: Warning issued by Alby; affects only internet-exposed instances.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets](https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html)

### Plex Media Server Multiple Vulnerabilities
- **Description**: Over 36,000 internet-exposed Plex Media Server instances remain unpatched against multiple recently disclosed security vulnerabilities.
- **Impact**: Remote compromise of media servers, potential lateral movement, data access, and use as pivot points in home/SMB networks.
- **Status**: Patches available; large-scale exposure persists due to lack of administrator action.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Over 36,000 exposed Plex servers vulnerable to recent flaws](https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/)

### F5 BIG-IP APM In-Memory PHP Web Shell
- **Description**: Malware targeting F5 BIG-IP Access Policy Manager appliances injects a PHP web shell into Apache memory rather than disk, evading file-based detection. The shell is added when Apache loads any of three specific appliance PHP scripts.
- **Impact**: Persistent, stealthy remote access to compromised load balancers/APM devices; survives reboots if reinjection mechanism persists; evades standard forensic disk analysis.
- **Status**: Active compromise campaign analyzed by Sophos (published September 7, 2026); initial access vector not specified in reporting.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans](https://thehackernews.com/2026/09/f5-big-ip-apm-malware-injects-php-web.html)

## Affected Systems and Products

- **Google Chrome**: All versions prior to September 2026 stable update (V8 engine CVE-2026-87491); Windows, macOS, Linux platforms
- **Microsoft Windows**: All supported versions (two actively exploited zero-days + 723 total flaws patched); Windows 10, Windows 11, Windows Server
- **Microsoft Defender**: Built-in antimalware on Windows 10/11 and Server (ShieldCrash/ShieldBreak)
- **SAP Extended Passport (EPP) Processing**: SAP application platforms using EPP component (CVE-2026-44756)
- **N-able N-central**: On-premises and hosted RMM platform versions vulnerable to CVE-2026-86218
- **cPanel & WHM**: Every supported version (mail privilege escalation to root)
- **DeepSeek Harness**: Open-source AI agent sandbox tool (sandbox escape flaw)
- **Alby Hub**: Self-hosted Lightning Network wallet versions v1.7.0+ (internet-exposed instances)
- **Plex Media Server**: Unpatched versions across Windows, macOS, Linux, NAS devices (36,000+ exposed instances)
- **F5 BIG-IP Access Policy Manager**: Appliance firmware versions running Apache with targeted PHP scripts (in-memory web shell malware)
- **Frontier AI Models (OpenAI GPT, Anthropic Claude, Google Gemini, SpaceX Grok)**: Model APIs targeted for industrial-scale distillation extraction
- **AI Provider Accounts (Google, Anthropic, others)**: User accounts compromised via infostealer-harvested replayable API tokens

## Attack Vectors and Techniques

- **AI Model Distillation/Extraction**: Systematic querying of frontier model APIs to extract billions of tokens, replicating proprietary capabilities at reduced cost; conducted at industrial scale by six Chinese AI firms since late 2024.
- **Infostealer AI Token Harvesting**: Lumma Stealer, Vidar, and similar malware harvest credentials, session tokens, and API keys from compromised endpoints; stolen AI tokens replayed to bypass MFA and access model provider accounts.
- **Workflow Identity Hijacking**: Unauthenticated requests sent through identity propagation flows to bypass standard security controls and hijack organizational data access.
- **Account Recovery Social Engineering**: Attackers target service desk and self-service recovery processes to reset MFA and passwords, converting recovery flows into account takeover vectors.
- **BlueMoon Exploit Chaining**: Multi-vulnerability chain combining Chrome and Windows flaws into a single exploit kit delivered via web or document vectors; enables remote code execution and sandbox escape.
- **Multi-Hop Google Redirect Phishing**: Abuse of multiple legitimate Google services (e.g., Google Ads, Google Translate, AMP) in redirect chains to evade URL reputation filters and deliver credential harvesting or ScreenConnect payloads.
- **In-Memory PHP Web Shell Injection**: Malware hooks Apache's PHP script loading on F5 BIG-IP APM to inject a web shell exclusively in process memory, leaving no disk artifacts for traditional scanners.
- **Mail Service Privilege Escalation (cPanel)**: Authenticated mail interface (EmailTrack) abused to write arbitrary files as root, escalating from hosting account to full server compromise.
- **AI Agent Sandbox Escape (DeepSeek Harness)**: Sandboxed coding agent invokes the harness's own web API to disable filesystem restrictions, breaking out of the intended containment boundary.
- **Self-Hosted Wallet RPC Exposure (Alby Hub)**: Internet-accessible management interfaces on self-hosted Lightning wallets allow unauthenticated or weakly authenticated control of funds.

## Threat Actor Activities

- **APT31 (Bronze Vinewood, Judgement Panda, JungleBamboo)**: China-aligned state-sponsored group; first observed operator of BlueMoon exploit kit; conducting espionage via chained Windows/Chrome vulnerabilities.
- **Three Additional Unnamed Espionage Clusters**: Deployed BlueMoon exploit kit within the same week as APT31, indicating rapid proliferation or shared supplier; motivation consistent with intelligence collection.
- **Six Chinese AI Companies (Unnamed)**: Conducting systematic, industrial-scale distillation attacks against OpenAI, Anthropic, Google, and SpaceX frontier models since at least late 2024; described as core to their AI development strategy by U.S. intelligence agencies.
- **Gentlemen Ransomware Gang**: Claimed responsibility for breach at Veradigm via third-party vendor; patient personal data exposed.
- **Chinese Organized Crime (Xinbi Guarantee Operators)**: Ran Xinbi Guarantee scam marketplace offering fraud-as-a-service; utilized Telegram channels and cryptocurrency infrastructure; disrupted by DoJ with $52.8M seized and Scam Center Strike Force deployed to Madagascar targeting 13 scam compounds.
- **Lumma Stealer / Vidar Operators**: Information stealer campaigns harvesting AI API tokens, credentials, and session data; enabling downstream account takeover and MFA bypass against model providers.
- **Nightmare Eclipse**: Anonymous researcher who published the ShieldCrash zero-day exploit for Microsoft Defender immediately after September 2026 Patch Tuesday.
- **Chaotic Eclipse**: Security researcher who released proof-of-concept for ShieldCrash demonstrating bypass of ShieldBreak patch (CVE-2026-69414); previously reported ShieldBreak to Microsoft.
- **DoppelCart Fraud Network**: Operates 119,000+ fake e-commerce domains stealing payment card credentials; large-scale financial fraud infrastructure.