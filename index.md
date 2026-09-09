---
schema_version: 2
report_date: 2026-09-09
generated_at: 2026-09-09T11:49:35Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-09/
---
# Exploitation Report

## Executive Summary

September 2026 Patch Tuesday delivered a record-breaking 974 vulnerability fixes from Microsoft, including two actively exploited Windows zero-days that demand immediate attention. Google simultaneously addressed its seventh Chrome zero-day of the year (CVE-2026-87491), an out-of-bounds write in the V8 engine enabling sandbox escape, while a separate Chrome zero-day was also patched.

CISA added the critical N-able N-central pre-authentication RCE (CVE-2026-86218, CVSS 10.0) to its Known Exploited Vulnerabilities catalog, mandating federal agency patching by September 11. SAP addressed a maximum-severity kernel memory corruption flaw (CVE-2026-44756, CVSS 10.0) enabling unauthenticated remote code execution.

## Active Exploitation Details

### Chrome V8 Zero-Day (CVE-2026-87491)
- **Description**: An out-of-bounds write vulnerability in V8, Chrome's JavaScript and WebAssembly engine, affecting Google Chrome prior to the September 2026 stable channel update. The flaw allows code execution within the sandbox.
- **Impact**: Attackers can achieve code execution inside the Chrome sandbox, potentially enabling further privilege escalation or sandbox escape chains.
- **Status**: Actively exploited in the wild. Google released patches on September 9, 2026, addressing this vulnerability among 230 total fixes.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87491
- **Reporting**: [The Hacker News — Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html)

### Microsoft Defender ShieldCrash Zero-Day (CVE-2026-69414 bypass)
- **Description**: A zero-day exploit named "ShieldCrash" released by researcher Nightmare Eclipse that bypasses the patch for CVE-2026-69414 (ShieldBreak, CVSS 7.8). The vulnerability resides in Microsoft Defender and grants SYSTEM-level access. Researcher Chaotic Eclipse published a proof-of-concept demonstrating the patch bypass.
- **Impact**: Attackers can achieve SYSTEM-level code execution on Windows systems by bypassing the ShieldBreak patch, effectively rendering the previous fix ineffective.
- **Status**: Zero-day exploit publicly released; patch bypass confirmed via PoC. Microsoft's September 2026 Patch Tuesday updates were released prior to the disclosure.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access](https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/), [The Hacker News — Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed](https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html)

### SAP Kernel OVERPASS Vulnerability (CVE-2026-44756)
- **Description**: A maximum-severity memory corruption flaw in SAP Extended Passport (EPP) Processing within the SAP Kernel code. The vulnerability allows unauthenticated remote code execution.
- **Impact**: Unauthenticated attackers can achieve full remote code execution, compromising confidentiality, integrity, and availability of affected SAP applications.
- **Status**: Patched in SAP September 2026 security updates addressing 20 vulnerabilities across multiple products.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-44756
- **Reporting**: [The Hacker News — SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution](https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html), [Bleeping Computer — SAP warns of maximum severity 'OVERPASS' kernel vulnerability](https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/)

### N-able N-central Pre-Auth RCE (CVE-2026-86218)
- **Description**: A pre-authentication remote code execution vulnerability in N-able N-central management software with a CVSS score of 10.0. Added to CISA's Known Exploited Vulnerabilities catalog on September 9, 2026.
- **Impact**: Unauthenticated remote attackers can execute arbitrary code on affected N-central servers, leading to full system compromise.
- **Status**: Actively exploited in the wild per CISA KEV catalog entry. Federal Civilian Executive Branch agencies required to apply fixes by September 11, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86218
- **Reporting**: [The Hacker News — N-able N-central Pre-Auth RCE Flaw Exploited in the Wild](https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html)

### Microsoft Windows Zero-Days (September 2026 Patch Tuesday)
- **Description**: Two actively exploited zero-day vulnerabilities in Windows addressed in Microsoft's record-breaking September 2026 Patch Tuesday (974 total vulnerabilities). Specific CVE identifiers were not disclosed in the reporting.
- **Impact**: Active exploitation confirmed by Microsoft; potential for remote code execution, privilege escalation, or security feature bypass on Windows systems.
- **Status**: Patched in September 2026 Patch Tuesday updates (KB5124008, KB5122880 for Windows 11; KB5122878 for Windows 10 ESU).
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html), [Bleeping Computer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/), [Dark Reading — Patch Tuesday Sets Another Record With 974 CVEs](https://www.darkreading.com/vulnerabilities-threats/patch-tuesday-another-record-974-cves), [Krebs on Security — Microsoft Plugs Nearly 1,000 Security Holes](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/)

### Chrome Zero-Day (Seventh of 2026)
- **Description**: An actively exploited Chrome zero-day vulnerability patched by Google in the same September 2026 release that addressed CVE-2026-87491. This marks the seventh Chrome zero-day exploited in the wild patched by Google in 2026.
- **Impact**: Active exploitation in attacks; specific technical details and impact not disclosed in reporting.
- **Status**: Patched in Chrome stable channel update released September 9, 2026.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Google warns of new Chrome zero-day bug exploited in attacks](https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/)

### cPanel EmailTrack Root Code Execution
- **Description**: A vulnerability in cPanel's EmailTrack feature that allows an authenticated hosting account holder with mail-related privileges to create arbitrary files on the server and execute code as the root user. All supported versions of cPanel and WHM are affected.
- **Impact**: Privilege escalation from a single hosting account to full root control of the entire server, enabling complete compromise of shared hosting environments.
- **Status**: Patched in cPanel advisory published September 8, 2026.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html)

### F5 BIG-IP APM Memory-Resident Web Shell and Rootkit
- **Description**: Malware targeting F5 BIG-IP Access Policy Manager appliances injects a PHP web shell directly into memory when Apache loads legitimate PHP scripts, evading disk-based detection. A Linux rootkit intercepts PHP file loading to maintain persistence without writing to disk.
- **Impact**: Attackers gain persistent, fileless remote access to compromised F5 BIG-IP APM devices with web shell capabilities, completely evading traditional file integrity monitoring and disk forensics.
- **Status**: Active breaches observed; Sophos analysis published September 7, 2026. No specific vendor patch mentioned in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans](https://thehackernews.com/2026/09/f5-big-ip-apm-malware-injects-php-web.html), [Bleeping Computer — Hackers breach F5 BIG-IP APM devices to deploy Linux rootkit](https://www.bleepingcomputer.com/news/security/hackers-breach-f5-big-ip-apm-devices-to-deploy-linux-rootkit/)

### Plex Media Server Unpatched Vulnerabilities
- **Description**: Over 36,000 internet-exposed Plex Media Server instances remain unpatched against multiple recently disclosed security vulnerabilities.
- **Impact**: Exposed servers are vulnerable to attacks leveraging the unpatched flaws; specific vulnerability details and exploitation impact not provided in reporting.
- **Status**: Servers remain unpatched as of reporting; patches available from Plex for the disclosed vulnerabilities.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Over 36,000 exposed Plex servers vulnerable to recent flaws](https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/)

### ChatGPT Prompt Injection Data Exfiltration
- **Description**: A flaw in ChatGPT's integration with Gmail allows a single planted instruction in a conversation to cause ChatGPT to silently exfiltrate the user's Gmail data to an attacker-controlled ChatGPT account through a hidden channel, while appearing to answer normally.
- **Impact**: Attackers can steal sensitive email data from users who have connected their Gmail accounts to ChatGPT, via a covert channel that bypasses user awareness.
- **Status**: Proof-of-concept demonstrated by Check Point Research; no patch status mentioned in reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account](https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html)

## Affected Systems and Products

- **Google Chrome**: All versions prior to September 2026 stable channel update (130.0.6723.x or later); Windows, macOS, Linux platforms
- **Microsoft Windows**: All supported Windows 10 (ESU), Windows 11 (23H2, 24H2, 25H2), Windows Server versions; September 2026 Patch Tuesday updates required (KB5124008, KB5122880, KB5122878)
- **Microsoft Defender**: Windows systems with Defender enabled; ShieldBreak patch (CVE-2026-69414) bypassed by ShieldCrash exploit
- **SAP Systems**: SAP Kernel / Extended Passport (EPP) Processing components; all versions prior to September 2026 security patches
- **N-able N-central**: All versions affected by CVE-2026-86218; management servers exposed to pre-auth RCE
- **cPanel & WHM**: All supported versions; servers hosting accounts with mail privileges (EmailTrack feature)
- **F5 BIG-IP Access Policy Manager**: Appliances running Apache with PHP; specific versions not detailed in reporting
- **Plex Media Server**: Internet-exposed instances (36,000+ identified) unpatched against recent disclosed flaws
- **ChatGPT with Gmail Integration**: Users who have connected Gmail accounts to ChatGPT; web and API interfaces

## Attack Vectors and Techniques

- **V8 Engine Out-of-Bounds Write**: Exploitation of CVE-2026-87491 via malicious JavaScript/WebAssembly code delivered through web pages to achieve sandbox escape
- **Microsoft Defender Patch Bypass**: ShieldCrash exploit leverages incomplete patch for CVE-2026-69414 to achieve SYSTEM privileges via crafted inputs to Defender
- **SAP Kernel Memory Corruption**: Unauthenticated network-based exploitation of CVE-2026-44756 via malformed EPP packets triggering memory corruption
- **N-able N-central Pre-Auth RCE**: Unauthenticated remote code execution via network-accessible management interface (CVE-2026-86218)
- **cPanel EmailTrack File Write**: Authenticated user with mail privileges writes arbitrary files via EmailTrack functionality, escalating to root code execution
- **Memory-Resident PHP Web Shell**: Malware hooks Apache PHP script loading to inject web shell into memory only, leaving no disk artifacts (F5 BIG-IP APM)
- **Linux Rootkit PHP Interception**: Rootkit intercepts PHP file operations to inject malicious code into memory during legitimate script execution
- **Prompt Injection Data Exfiltration**: Planted instruction in ChatGPT conversation triggers covert Gmail data access and exfiltration to attacker account
- **Multi-Hop Google Service Redirects**: Attackers chain multiple Google services (redirects, AMP, etc.) to evade detection and deliver phishing/ScreenConnect payloads
- **ClickFix Social Engineering**: Legitimate services abused via social engineering to establish persistent access through user interaction

## Threat Actor Activities

- **Nightmare Eclipse**: Anonymous researcher who publicly released the ShieldCrash zero-day exploit for Microsoft Defender immediately after September Patch Tuesday
- **Chaotic Eclipse**: Security researcher who published proof-of-concept demonstrating ShieldBreak (CVE-2026-69414) patch bypass, confirming Microsoft's fix was incomplete
- **Slim Spider**: Previously undocumented financially motivated threat actor (Brazil-based) targeting Brazilian financial institutions since at least March 2026; deep knowledge of Brazilian financial infrastructure including PIX instant payment system; tracked by CrowdStrike
- **ShinyHunters**: Extortion gang claiming breach of Florida "DAVID" DMV database, allegedly stealing 200,000+ driver records
- **DoppelCart Operators**: Fraud network operating 119,000+ fake e-commerce domains to harvest payment card credentials
- **Liquid Network Attackers**: Unknown actors who exploited an Elements bug to steal ~4,000 BTC from Liquid Network (Bitcoin sidechain); returned 3,400 BTC but still hold ~$47M
- **F5 BIG-IP APM Intruders**: Unknown threat actors actively breaching F5 BIG-IP APM devices to deploy memory-resident PHP web shells and Linux rootkits
- **ClickFix Campaign Operators**: Multiple threat actor groups using ClickFix social engineering technique abusing legitimate services for initial access and persistence
- **Google Redirect Phishing Actors**: Threat actors leveraging multi-hop Google service redirects for credential harvesting and ScreenConnect remote access deployment