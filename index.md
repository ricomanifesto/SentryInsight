---
schema_version: 2
report_date: 2026-09-10
generated_at: 2026-09-10T04:03:41Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-10/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited in the wild across diverse technology stacks, from network infrastructure and endpoint security to browser engines and management platforms. Cisco has confirmed active exploitation of a maximum-severity authentication bypass in Secure Firewall Management Center (CVE-2026-20079), while Google patched its seventh Chrome zero-day of the year (CVE-2026-87491) and Microsoft addressed two actively exploited Windows zero-days among a record 974 vulnerabilities. The N-able N-central pre-authentication RCE (CVE-2026-86218) has been added to CISA's Known Exploited Vulnerabilities catalog, and a Microsoft Defender zero-day dubbed "ShieldCrash" grants SYSTEM access while bypassing the recent ShieldBreak patch (CVE-2026-69414).

Nation-state and cybercriminal activity is intensifying with novel techniques. China-aligned APT31 and three other espionage groups deployed the previously undocumented "BlueMoon" exploit kit chaining Chrome and Windows vulnerabilities within a single week. Chinese AI firms stand accused of industrial-scale distillation attacks extracting billions of tokens from frontier models including GPT, Claude, Gemini, and Grok. Meanwhile, infostealers like Lumma and Vidar are harvesting replayable AI tokens that bypass MFA, and ransomware groups including ShinyHunters and Gentlemen Gang continue targeting healthcare organizations, exposing millions of patient records.

The vulnerability management landscape faces unprecedented scale and velocity. SAP patched a CVSS 10.0 kernel flaw (CVE-2026-44756) enabling unauthenticated RCE, cPanel disclosed a root-privilege escalation affecting all supported versions, and over 36,000 internet-exposed Plex servers remain unpatched. Memory-resident malware targeting F5 BIG-IP APM appliances evades disk forensics by injecting PHP web shells directly into Apache memory. Organizations must prioritize patching of actively exploited vulnerabilities while hardening identity verification processes against account recovery abuse and AI-driven social engineering.

## Active Exploitation Details

### Cisco Secure Firewall Management Center Authentication Bypass
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Secure Firewall Management Center (FMC) software that allows attackers to bypass authentication controls.
- **Impact**: Attackers can gain unauthorized administrative access to the firewall management center, potentially compromising the entire network security infrastructure.
- **Status**: Actively exploited in the wild; patches available from Cisco.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20079
- **Reporting**: [Bleeping Computer — Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/)

### Chrome V8 Out-of-Bounds Write Zero-Day
- **Description**: An out-of-bounds write vulnerability in V8, Chrome's JavaScript and WebAssembly engine, that enables code execution inside the sandbox.
- **Impact**: Attackers can achieve code execution within the Chrome sandbox, representing the seventh actively exploited Chrome zero-day patched by Google in 2026.
- **Status**: Actively exploited in the wild; patched in Chrome updates released September 2026 addressing 230 total vulnerabilities.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87491
- **Reporting**: [The Hacker News — Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html), [Bleeping Computer — Google warns of new Chrome zero-day bug exploited in attacks](https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/)

### Microsoft Defender ShieldCrash Zero-Day
- **Description**: A zero-day vulnerability in Microsoft Defender codenamed "ShieldCrash" that grants SYSTEM-level access. The vulnerability represents a patch bypass for CVE-2026-69414 (ShieldBreak, CVSS 7.8).
- **Impact**: Attackers can achieve SYSTEM privileges on affected Windows systems, bypassing the ShieldBreak patch released in August 2026.
- **Status**: Proof-of-concept exploit released by researcher Chaotic Eclipse; Microsoft Defender zero-day actively exploitable.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access](https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/), [The Hacker News — Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed](https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html)

### SAP Extended Passport Kernel Memory Corruption
- **Description**: A maximum-severity memory corruption vulnerability in SAP Extended Passport (EPP) Processing that enables unauthenticated remote code execution.
- **Impact**: Unauthenticated attackers can achieve remote code execution with severe impact on confidentiality, integrity, and availability of SAP applications.
- **Status**: Patched by SAP in September 2026 security updates; no indication of active exploitation in the wild at time of disclosure.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-44756
- **Reporting**: [The Hacker News — SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution](https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html)

### N-able N-central Pre-Authentication RCE
- **Description**: A pre-authentication remote code execution vulnerability in N-able N-central rated CVSS 10.0, added to CISA's Known Exploited Vulnerabilities catalog.
- **Impact**: Unauthenticated attackers can achieve remote code execution on N-central management servers, compromising the entire managed infrastructure.
- **Status**: Actively exploited in the wild; CISA mandates FCEB agencies to apply fixes by September 11, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86218
- **Reporting**: [The Hacker News — N-able N-central Pre-Auth RCE Flaw Exploited in the Wild](https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html)

### Microsoft Windows Zero-Days (September 2026 Patch Tuesday)
- **Description**: Two Windows zero-day vulnerabilities among 974 total flaws patched in Microsoft's record-breaking September 2026 Patch Tuesday, confirmed as actively exploited in the wild.
- **Impact**: Attackers can exploit these vulnerabilities for privilege escalation, remote code execution, or security feature bypass on Windows systems.
- **Status**: Actively exploited; patches released as part of 974-vulnerability update (723 in Windows, 111 in Office, 62 in SQL, 22 in Developer Tools).
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html), [Krebs on Security — Microsoft Plugs Nearly 1,000 Security Holes](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/), [Dark Reading — Patch Tuesday Sets Another Record With 974 CVEs](https://www.darkreading.com/vulnerabilities-threats/patch-tuesday-another-record-974-cves)

### BlueMoon Exploit Kit (Chrome and Windows Vulnerability Chain)
- **Description**: A previously undocumented exploit kit called "BlueMoon" that chains together multiple vulnerabilities in Microsoft Windows and Google Chrome, deployed by four espionage-motivated threat groups within a single week.
- **Impact**: Enables sophisticated browser and OS compromise chains for espionage operations; first in-the-wild use attributed to APT31.
- **Status**: Actively exploited by multiple threat actors; specific component vulnerabilities not publicly disclosed with CVE identifiers.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week](https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html)

### cPanel Root Privilege Escalation via EmailTrack
- **Description**: A vulnerability in cPanel/WHM allowing an authenticated hosting account with mail-related privileges to create arbitrary files via EmailTrack and execute code as root.
- **Impact**: Complete server compromise from a single hosting account; affects every supported version of cPanel and WHM.
- **Status**: Patched by cPanel on September 8, 2026; exploitation status in wild not specified.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html)

### DeepSeek Harness Sandbox Escape
- **Description**: A flaw in DeepSeek Harness (open-source AI coding agent tool) allowing a sandboxed agent to disable its own file sandbox with a single command via the tool's web interface.
- **Impact**: AI agents working on untrusted code can escape containment and write outside their workspace on the developer's machine.
- **Status**: Flaw disclosed; patch status not specified in reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval](https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html)

### Alby Hub Bitcoin Wallet Takeover
- **Description**: A critical flaw in Alby Hub (self-hosted Lightning wallet) versions v1.7.0 through current, allowing attackers to take over internet-exposed wallets and transfer funds.
- **Impact**: Complete wallet takeover and fund theft for internet-accessible Alby Hub instances.
- **Status**: Disclosed by Alby; exploitation requires internet-exposed Hub instance.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets](https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html)

### F5 BIG-IP APM Memory-Resident PHP Web Shell
- **Description**: Malware targeting F5 BIG-IP Access Policy Manager appliances that injects a PHP web shell into Apache memory rather than writing to disk, evading traditional file-based detection.
- **Impact**: Persistent, stealthy remote access to compromised F5 appliances; three specific Apache-loaded PHP scripts are hooked to inject the memory-resident shell.
- **Status**: Observed in active intrusions; analyzed by Sophos on September 7, 2026.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans](https://thehackernews.com/2026/09/f5-big-ip-apm-malware-injects-php-web.html)

### Skullcandy Dime 3 Bluetooth Pairing Bypass
- **Description**: Skullcandy Dime 3 wireless earbuds accept Bluetooth pairing requests from nearby unpaired devices without requiring user interaction, enabling Bluetooth hijacking.
- **Impact**: Attackers in proximity can pair with and potentially control earbuds, intercept audio, or inject audio without user consent.
- **Status**: Warning issued by Carnegie Mellon University CERT/CC; no patch mentioned.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Skullcandy Dime 3 earbuds expose users to Bluetooth hijacking](https://www.bleepingcomputer.com/news/security/skullcandy-dime-3-earbuds-expose-users-to-bluetooth-hijacking/)

### Plex Media Server Unpatched Vulnerabilities
- **Description**: Over 36,000 internet-exposed Plex Media Servers remain unpatched against multiple recently disclosed security vulnerabilities.
- **Impact**: Exposed servers vulnerable to attacks leveraging undisclosed flaws in Plex Media Server software.
- **Status**: Widespread exposure; specific CVE identifiers not provided in reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Over 36,000 exposed Plex servers vulnerable to recent flaws](https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/)

## Affected Systems and Products

- **Cisco Secure Firewall Management Center (FMC)**: All versions affected by CVE-2026-20079; network security management appliances and virtual appliances
- **Google Chrome**: Versions prior to September 2026 stable release (230 vulnerabilities patched including CVE-2026-87491); Windows, macOS, Linux platforms
- **Microsoft Defender / Windows**: Windows 10/11 with Microsoft Defender; ShieldCrash zero-day and ShieldBreak (CVE-2026-69414) patch bypass; 974 total vulnerabilities across Windows, Office, SQL, Developer Tools
- **SAP Extended Passport (EPP) Processing**: SAP application servers using EPP; kernel-level memory corruption enabling unauthenticated RCE
- **N-able N-central**: On-premises and hosted N-central management servers; pre-authentication RCE via CVE-2026-86218
- **cPanel & WHM**: All supported versions; hosting servers with EmailTrack functionality enabled
- **DeepSeek Harness**: Open-source AI coding agent tool; developer machines running sandboxed agents
- **Alby Hub**: Self-hosted Lightning Network wallet versions v1.7.0 and later; internet-exposed instances on personal computers or servers
- **F5 BIG-IP Access Policy Manager**: Appliance and virtual editions; three specific Apache-loaded PHP scripts targeted for memory injection
- **Skullcandy Dime 3 Wireless Earbuds**: Consumer Bluetooth audio devices; firmware-level pairing acceptance flaw
- **Plex Media Server**: Internet-exposed instances; over 36,000 unpatched servers identified online
- **BlueMoon Exploit Kit Targets**: Microsoft Windows and Google Chrome; specific versions not disclosed; exploited via chained vulnerability sequence

## Attack Vectors and Techniques

- **Authentication Bypass**: Cisco Secure FMC CVE-2026-20079 allows attackers to circumvent authentication entirely and gain administrative access to firewall management
- **Browser Engine Exploitation**: Chrome V8 out-of-bounds write (CVE-2026-87491) enables code execution within the sandbox; leveraged as component in BlueMoon exploit kit chains
- **Exploit Kit Chaining**: BlueMoon chains multiple Windows and Chrome vulnerabilities for reliable exploitation; deployed by APT31 and three other espionage groups within one week
- **Patch Bypass**: ShieldCrash exploits incomplete fix for CVE-2026-69414 (ShieldBreak) in Microsoft Defender, demonstrating rapid attacker adaptation to patches
- **Pre-Authentication RCE**: N-able N-central CVE-2026-86218 and SAP EPP CVE-2026-44756 both enable unauthenticated remote code execution at maximum severity
- **Privilege Escalation via Legitimate Features**: cPanel EmailTrack functionality abused to write arbitrary files and execute as root from low-privilege hosting account
- **AI Sandbox Escape**: DeepSeek Harness flaw allows AI agent to call its own web interface to disable containment sandbox with single command
- **Memory-Resident Malware**: F5 BIG-IP APM malware hooks Apache PHP script loading to inject PHP web shell directly into process memory, leaving no disk artifacts
- **Bluetooth Pairing Acceptance**: Skullcandy Dime 3 accepts pairing without user interaction, enabling proximity-based hijacking
- **AI Token Theft via Infostealers**: Lumma Stealer and Vidar harvest replayable AI API tokens/session credentials from compromised systems, bypassing MFA for model provider access
- **Account Recovery Social Engineering**: Attackers target MFA recovery processes (help desk, SMS, email) to convert account recovery into account takeover
- **Workflow Identity Hijacking**: Unauthenticated entry points exploited to send basic requests that hijack organizational data through identity-based AI attack vectors
- **Industrial-Scale AI Model Distillation**: Six Chinese AI companies systematically extract billions of tokens from frontier models (GPT, Claude, Gemini, Grok) via distillation attacks
- **Ransomware via Third-Party Compromise**: Veradigm breach originated from third-party vendor; AdaptHealth breach attributed to ShinyHunters; Gentlemen Gang claims Veradigm attack

## Threat Actor Activities

- **APT31 (Bronze Vinewood, Judgement Panda, JungleBamboo)**: China-aligned state-sponsored group; first in-the-wild user of BlueMoon exploit kit; espionage-motivated targeting
- **Three Additional Espionage Clusters**: Unnamed spy groups deployed same BlueMoon exploit kit within one week of APT31; indicates exploit kit sharing or common supplier
- **ShinyHunters**: Threat group attributed to AdaptHealth breach exposing 4.1 million people's data in July 2026 cyberattack
- **Gentlemen Gang**: Ransomware group claiming attack on Veradigm (healthcare technology company); patient data breach via third-party vendor compromise
- **Chinese AI Firms (Six Companies)**: Accused by US cybersecurity and intelligence agencies of systematic, industrial-scale distillation attacks on American frontier AI models (OpenAI, Anthropic, Google Gemini, SpaceX Grok) since late 2024
- **Xinbi Guarantee Operators**: Chinese organized crime running scam marketplace with Telegram channels and cryptocurrency wallets; disrupted by US DoJ with $52.8M frozen and Scam Center Strike Force deployed to Madagascar
- **Lumma Stealer / Vidar Operators**: Information stealer malware operators harvesting AI tokens, credentials, and session data; enabling MFA bypass for model provider access
- **Nightmare Eclipse**: Anonymous researcher who released ShieldCrash Microsoft Defender zero-day exploit after September 2026 Patch Tuesday
- **Chaotic Eclipse**: Security researcher who published ShieldCrash PoC demonstrating ShieldBreak (CVE-2026-69414) patch bypass
- **Ohio Cyberstalker**: Individual sentenced to 15 years for sextortion and cyberstalking using AI-generated sexually explicit content against numerous victims