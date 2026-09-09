---
schema_version: 2
report_date: 2026-09-09
generated_at: 2026-09-09T11:06:30Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-09/
---
# Exploitation Report

## Executive Summary

September 2026 has seen an extraordinary surge in active exploitation across multiple critical platforms. Microsoft's record-breaking Patch Tuesday addressed 974 vulnerabilities, including two actively exploited Windows zero-days, while Google patched its seventh Chrome zero-day of the year (CVE-2026-87491) enabling sandbox escape via a V8 out-of-bounds write. Simultaneously, CISA added a maximum-severity pre-authentication RCE in N-able N-central (CVE-2026-86218, CVSS 10.0) to its Known Exploited Vulnerabilities catalog, mandating federal agency remediation by September 11.

Critical infrastructure and enterprise software are under sustained attack. SAP disclosed a maximum-severity kernel memory corruption flaw (CVE-2026-44756, CVSS 10.0) enabling unauthenticated remote code execution in Extended Passport Processing. F5 BIG-IP APM appliances are being compromised to deploy fileless Linux rootkits that inject PHP web shells directly into memory, evading disk-based detection. A cPanel vulnerability allows any hosting account with mail privileges to achieve root code execution across all supported versions. Over 36,000 internet-exposed Plex Media Servers remain unpatched against recently disclosed flaws.

Threat actor activity is diversifying across financial crime, espionage, and extortion. The Brazil-based financially motivated group Slim Spider has targeted Brazilian financial institutions since March 2026, demonstrating deep knowledge of local payment infrastructure. The ShinyHunters extortion gang claims a breach of Florida's DAVID DMV database, exfiltrating over 200,000 driver records. The DoppelCart fraud network operates 119,000 fake e-commerce domains to harvest payment cards. Meanwhile, researchers Nightmare Eclipse and Chaotic Eclipse have disclosed Microsoft Defender zero-days (ShieldCrash/ShieldBreak bypass), and phishing campaigns now leverage multi-hop Google redirects and ClickFix social engineering to deliver ScreenConnect and achieve persistent access.

## Active Exploitation Details

### Chrome V8 Zero-Day (CVE-2026-87491)
- **Description**: An out-of-bounds write vulnerability in V8, Chrome's JavaScript and WebAssembly engine, affecting Google Chrome prior to the September 2026 stable channel update. The flaw allows attackers to corrupt memory within the renderer process.
- **Impact**: Attackers can achieve arbitrary code execution inside the Chrome sandbox, providing a foothold for sandbox escape chains or data theft from the renderer process.
- **Status**: Actively exploited in the wild. Google released patches on September 2026 Patch Tuesday as part of 230 vulnerabilities fixed. The vulnerability is rated medium severity by Google.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87491
- **Reporting**: [The Hacker News — Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html), [Bleeping Computer — Google warns of new Chrome zero-day bug exploited in attacks](https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/)

### Microsoft Defender ShieldCrash / ShieldBreak Bypass (CVE-2026-69414)
- **Description**: A patch bypass for CVE-2026-69414 (ShieldBreak, CVSS 7.8) in Microsoft Defender. The original vulnerability allowed elevation to SYSTEM. Researcher Chaotic Eclipse demonstrated that Microsoft's September 2026 patch for ShieldBreak is incomplete, releasing a proof-of-concept exploit codenamed ShieldCrash. A separate researcher, Nightmare Eclipse, also released a ShieldCrash exploit granting SYSTEM access immediately after Patch Tuesday.
- **Impact**: Local attackers can bypass Defender protections and achieve SYSTEM-level code execution, effectively disabling the primary endpoint protection on Windows systems.
- **Status**: Proof-of-concept exploit publicly available; active exploitation of the bypass demonstrated. Microsoft has not yet released a complete fix for the bypass as of the reporting date.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access](https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/), [The Hacker News — Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed](https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html)

### SAP Kernel OVERPASS Memory Corruption (CVE-2026-44756)
- **Description**: A maximum-severity memory corruption vulnerability in the SAP Kernel code, specifically within SAP Extended Passport (EPP) Processing. Tracked as CVE-2026-44756 with a CVSS score of 10.0. The flaw is also referred to as "OVERPASS" in SAP advisories.
- **Impact**: Unauthenticated remote attackers can achieve arbitrary code execution, leading to complete compromise of the confidentiality, integrity, and availability of the affected SAP application.
- **Status**: Patched in SAP September 2026 security updates (20 vulnerabilities addressed). No evidence of exploitation in the wild reported in the source articles, but the maximum CVSS score and unauthenticated attack vector make it a critical patching priority.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-44756
- **Reporting**: [The Hacker News — SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution](https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html), [Bleeping Computer — SAP warns of maximum severity 'OVERPASS' kernel vulnerability](https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/)

### N-able N-central Pre-Auth RCE (CVE-2026-86218)
- **Description**: A pre-authentication remote code execution vulnerability in N-able N-central remote monitoring and management software. Rated CVSS 10.0 (maximum severity). CISA added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog on September 2026 Patch Tuesday.
- **Impact**: Unauthenticated remote attackers can execute arbitrary code on the N-central server, potentially compromising the management plane for all monitored endpoints and enabling supply-chain-style attacks against managed service providers and their customers.
- **Status**: Actively exploited in the wild (per CISA KEV inclusion). Federal Civilian Executive Branch agencies required to apply fixes by September 11, 2026. N-able has released patches.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-86218
- **Reporting**: [The Hacker News — N-able N-central Pre-Auth RCE Flaw Exploited in the Wild](https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html)

### Windows Zero-Days (Two Actively Exploited)
- **Description**: Two distinct zero-day vulnerabilities in Microsoft Windows that Microsoft confirmed have been actively exploited in the wild. Specific CVE identifiers were not disclosed in the source articles. These were addressed in the record-breaking September 2026 Patch Tuesday release of 974 vulnerabilities (966 per Bleeping Computer's count).
- **Impact**: Varies by vulnerability; both allow attackers to compromise Windows systems. Given active exploitation, they likely provide elevation of privilege, remote code execution, or security feature bypass.
- **Status**: Patched in September 2026 Patch Tuesday updates (KB5122878 for Windows 10, KB5124008/KB5122880 for Windows 11). Over 110 vulnerabilities in the batch rated critical.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html), [Krebs on Security — Microsoft Plugs Nearly 1,000 Security Holes](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/), [Dark Reading — Patch Tuesday Sets Another Record With 974 CVEs](https://www.darkreading.com/vulnerabilities-threats/patch-tuesday-another-record-974-cves), [Bleeping Computer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/), [Bleeping Computer — Microsoft releases Windows 10 KB5122878 extended security update](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-10-kb5122878-extended-security-update/), [Bleeping Computer — Windows 11 cumulative updates KB5124008 & KB5122880 released](https://www.bleepingcomputer.com/news/microsoft/windows-11-cumulative-updates-kb5124008-and-kb5122880-released/)

### cPanel EmailTrack Root Code Execution
- **Description**: A vulnerability in cPanel and WHM that allows an authenticated hosting account holder with mail-related privileges to create arbitrary files on the server via the EmailTrack feature, subsequently achieving code execution as the root user. Every supported version of cPanel and WHM is affected.
- **Impact**: Compromise of a single hosting account leads to full server takeover (root access), affecting all other accounts on the shared hosting infrastructure.
- **Status**: Patched by cPanel on September 8, 2026. No specific CVE identifier provided in the source article.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html)

### F5 BIG-IP APM Memory-Resident PHP Web Shell / Linux Rootkit
- **Description**: Attackers breaching F5 BIG-IP Access Policy Manager appliances deploy a Linux rootkit that intercepts PHP file loading and injects a PHP web shell directly into memory (fileless). The malware hooks three specific appliance PHP scripts; when Apache loads them, the web shell is added to the in-memory copy while the on-disk file remains clean.
- **Impact**: Persistent, stealthy remote access to the F5 appliance. The fileless technique evades traditional disk-based malware scans and integrity checks. Attackers can execute arbitrary commands via the web shell.
- **Status**: Active intrusions observed. Sophos published analysis on September 7, 2026. No vendor patch mentioned in source articles; mitigation guidance not specified.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans](https://thehackernews.com/2026/09/f5-big-ip-apm-malware-injects-php-web.html), [Bleeping Computer — Hackers breach F5 BIG-IP APM devices to deploy Linux rootkit](https://www.bleepingcomputer.com/news/security/hackers-breach-f5-big-ip-apm-devices-to-deploy-linux-rootkit/)

### Plex Media Server Unpatched Exposures
- **Description**: Over 36,000 Plex Media Servers exposed to the internet remain unpatched against multiple recently disclosed security vulnerabilities. Specific CVE identifiers and vulnerability details were not provided in the source article.
- **Impact**: Attackers can exploit the unpatched flaws to compromise the servers, potentially accessing media libraries, pivoting to internal networks, or using the servers as proxies for further attacks.
- **Status**: Servers remain unpatched as of publication. No exploitation activity confirmed in the article, but the exposure scale presents high risk.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — Over 36,000 exposed Plex servers vulnerable to recent flaws](https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/)

## Affected Systems and Products

- **Google Chrome**: All versions prior to the September 2026 stable channel update (which includes the fix for CVE-2026-87491). Platform: Windows, macOS, Linux.
- **Microsoft Defender**: Windows systems running the September 2026 Patch Tuesday version where the ShieldBreak (CVE-2026-69414) patch was applied but the ShieldCrash bypass remains effective. Platform: Windows 10, Windows 11, Windows Server.
- **SAP Systems**: SAP NetWeaver / ABAP Platform and related products using SAP Kernel with Extended Passport (EPP) Processing. Specific affected kernel versions detailed in SAP Security Note for CVE-2026-44756. Platform: Any OS running vulnerable SAP Kernel.
- **N-able N-central**: All versions prior to the patched release addressing CVE-2026-86218. Platform: Windows Server (primary N-central server OS).
- **Microsoft Windows**: Windows 10 (KB5122878 extended security update), Windows 11 25H2/24H2 (KB5124008), Windows 11 23H2 (KB5122880), and corresponding Windows Server versions. Platform: x64, ARM64.
- **cPanel & WHM**: Every supported version as of September 8, 2026. Platform: Linux servers running cPanel/WHM (CentOS, AlmaLinux, Rocky Linux, Ubuntu, CloudLinux).
- **F5 BIG-IP Access Policy Manager (APM)**: Appliances running vulnerable APM firmware versions. Specific versions not listed in source articles. Platform: F5 BIG-IP hardware and virtual editions (TMOS).
- **Plex Media Server**: Versions prior to the patches for the recently disclosed flaws. Platform: Windows, macOS, Linux, NAS devices (Synology, QNAP, Asustor, etc.), Docker, FreeBSD.

## Attack Vectors and Techniques

- **V8 Out-of-Bounds Write for Sandbox Code Execution**: Attackers exploit CVE-2026-87491 by crafting malicious JavaScript/WebAssembly that triggers an out-of-bounds write in the V8 engine, achieving code execution within the Chrome renderer sandbox. This serves as the initial stage in an exploit chain. **Vector**: Drive-by download or malicious link leading to a compromised or attacker-controlled website.
- **EmailTrack File Write to Root RCE**: Authenticated cPanel users with mail privileges leverage the EmailTrack feature to write controlled files to arbitrary locations on the filesystem, then execute them as root via a secondary mechanism (e.g., cron, sudo misconfiguration, or service restart). **Vector**: Compromised hosting account credentials or malicious customer on shared hosting.
- **Fileless PHP Web Shell via Memory Injection**: The Linux rootkit on F5 BIG-IP APM hooks the PHP interpreter (via LD_PRELOAD or similar) to modify the in-memory image of three specific appliance PHP scripts when loaded by Apache, appending a web shell. No files are written to disk. **Vector**: Initial access to the APM appliance (method not specified in articles—likely credential theft, VPN vulnerability, or exposed management interface).
- **Microsoft Defender ShieldCrash SYSTEM Escalation**: The ShieldCrash exploit (and ShieldBreak bypass) leverages a logic flaw or race condition in Defender's driver or user-mode service to escalate from a low-privilege context to NT AUTHORITY\SYSTEM, disabling tamper protection. **Vector**: Local access (malware execution, phishing payload, or lateral movement) on a Windows endpoint with Defender enabled.
- **Multi-Hop Google Redirect Phishing**: Threat actors chain multiple legitimate Google services (e.g., Google Docs, Google Sites, Google Forms, open redirects) to obfuscate the final phishing destination, evading URL reputation filters and secure email gateways. **Vector**: Phishing emails containing links that traverse several Google domains before landing on a credential harvester or ScreenConnect installer.
- **ClickFix Social Engineering for Persistent Access**: Attackers use the "ClickFix" technique—tricking users into copying and pasting a malicious command (often via Run dialog, PowerShell, or browser console) under the guise of fixing an error or verification step. The command downloads and executes a payload that establishes persistence via legitimate services (e.g., scheduled tasks, WMI, ScreenConnect). **Vector**: Malicious websites, fake CAPTCHA/verification pages, or error messages injected via compromised sites or malvertising.
- **AI-Generated Synthetic Media for Extortion**: Perpetrators create realistic sexually explicit images/videos of victims using generative AI, then threaten distribution to coerce payment or compliance. **Vector**: Social media reconnaissance for source images, direct messaging/email for threat delivery.
- **Fake E-Commerce Network (DoppelCart) for Card Skimming**: Operators register 119,000+ domains mimicking legitimate brands, deploy e-commerce platforms with malicious checkout pages or formjacking scripts, and harvest payment card data entered by unsuspecting shoppers. **Vector**: Search engine poisoning, social media ads, typosquatting, phishing emails linking to fake store fronts.

## Threat Actor Activities

- **Nightmare Eclipse (Researcher)**: Released a functional Microsoft Defender zero-day exploit ("ShieldCrash") granting SYSTEM access immediately after Microsoft's September 2026 Patch Tuesday. The exploit targets a vulnerability distinct from or bypassing the patched ShieldBreak (CVE-2026-69414). Activity: Public exploit disclosure; no attribution to malicious campaigns.
- **Chaotic Eclipse (Researcher)**: Published a proof-of-concept demonstrating that Microsoft's patch for ShieldBreak (CVE-2026-69414) is bypassable, naming the bypass "ShieldCrash." Reported the original ShieldBreak vulnerability to Microsoft last month. Activity: Vulnerability research, PoC release, patch quality critique.
- **ShinyHunters (Extortion Gang)**: Claimed responsibility for breaching the Florida Department of Motor Vehicles "DAVID" database platform, exfiltrating over 200,000 driver records. The group operates as an extortion gang, typically threatening to leak or sell stolen data. Activity: Data theft, extortion, public claim on breach forums.
- **Slim Spider (Brazil-based Financially Motivated Actor)**: Tracked by CrowdStrike since at least March 2026. Targets Brazilian financial institutions with deep operational knowledge of local infrastructure, including the instant payment system (PIX). Focuses on crypto custody secrets and financial credential theft. Activity: Targeted intrusion, credential access, financial fraud.
- **DoppelCart Operators (Fraud Network)**: Run a massive network of over 119,000 fake e-commerce domains to steal payment card details. The operation is highly automated, using lookalike domains and branding to deceive shoppers. Activity: Payment card harvesting, financial fraud, infrastructure deployment at scale.
- **Unknown Operators (F5 BIG-IP APM Intrusions)**: Conducted breaches of F5 BIG-IP APM appliances to deploy a custom Linux rootkit with fileless PHP web shell injection. The malware's sophistication (memory-only persistence, hooking specific appliance scripts) suggests a capable actor, possibly state-sponsored or advanced criminal group. Activity: Initial access, persistence, credential access, command and control via web shell.
- **Unknown Operators (Multi-Hop Google Redirect Phishing)**: Leverage chains of legitimate Google services to deliver credential phishing pages and ScreenConnect remote access installers. The technique demonstrates advanced evasion of email and web security controls. Activity: Credential harvesting, remote access deployment, phishing infrastructure abuse.
- **Unknown Operators (ClickFix Campaigns)**: Conduct at least two distinct campaigns using the ClickFix social engineering tactic to trick users into self-executing malicious commands that establish persistent access via legitimate system services. Activity: Initial access, persistence, defense evasion.