---
schema_version: 2
report_date: 2026-09-17
generated_at: 2026-09-17T11:24:52Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-17/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with several maximum-severity zero-days receiving emergency patches. Cisco's Identity Services Engine, ConnectWise ScreenConnect, the Issabel Framework, WSO2 API Manager, and WooCommerce Wholesale Lead Capture are all confirmed targets of in-the-wild attacks, while Google has addressed an actively exploited Pixel modem zero-day and a separate Android zero-day on Pixel devices.

Threat actors ranging from Chinese espionage group FamousSparrow to Iranian state-linked operators and North Korean APTs are deploying novel malware families—including SparroWocky, CHOSEN BRICK, and a previously undocumented Linux toolkit—alongside sophisticated techniques such as AI assistant hijacking, browser extension injection via the KREMLIN toolkit, and AI coding assistant session compromise to spread the Shai-Hulud worm across software supply chains.

## Active Exploitation Details

### Cisco Identity Services Engine Zero-Day
- **Description**: A maximum-severity vulnerability in Cisco Identity Services Engine (ISE) that attackers are actively exploiting in the wild. Cisco has released security updates to address the flaw.
- **Impact**: Full compromise of the ISE appliance, potentially enabling network access control bypass, authentication manipulation, and lateral movement within enterprise networks.
- **Status**: Actively exploited zero-day; security updates available from Cisco.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Cisco warns of max severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/)

### Issabel Framework Unauthenticated RCE (CVE-2026-89026)
- **Description**: A critical security flaw in Issabel Framework, a web-based framework for open-source unified communications PBX software. The vulnerability stems from a hard-coded credential that allows unauthenticated remote attackers to execute arbitrary operating system commands.
- **Impact**: Unauthenticated remote code execution as the application user, leading to full server compromise, call interception, and potential pivot to internal telephony infrastructure.
- **Status**: Actively exploited in the wild; patch information should be sought from Issabel project maintainers.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-89026
- **Reporting**: [The Hacker News — Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html)

### WSO2 API Manager JWT Bypass (CVE-2026-5430)
- **Description**: A critical improper verification of cryptographic signature vulnerability in WSO2 API Manager that enables attackers to forge admin tokens and achieve account takeover. The flaw allows bypassing JWT authentication by exploiting signature validation weaknesses.
- **Impact**: Full administrative account takeover of the API Manager, enabling API manipulation, data exfiltration, and potential lateral movement to backend services.
- **Status**: Active exploitation in the wild confirmed by watchTowr; patches available from WSO2.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-5430
- **Reporting**: [The Hacker News — Active Exploitation Attempts Target WSO2 API Manager JWT Bypass With Forged Admin Tokens](https://thehackernews.com/2026/09/active-exploitation-attempts-target.html)

### Acronis cPanel Backup Plugin Privilege Escalation (CVE-2026-87886)
- **Description**: A high-severity local privilege escalation vulnerability in the Acronis Backup plugin for cPanel and Web Host Manager (WHM) caused by insecure file permissions. The flaw affects Linux deployments of the plugin.
- **Impact**: Local attackers can escalate privileges to root on the hosting server, compromising all hosted websites, databases, and backup data.
- **Status**: Exploited in targeted attacks in the wild; Acronis has released updates.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-87886
- **Reporting**: [The Hacker News — Acronis cPanel Backup Plugin Vulnerability Exploited in Targeted Attacks](https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html)

### Google Pixel Cellular Modem Privilege Escalation (CVE-2026-58704)
- **Description**: A high-severity privilege escalation flaw in the Pixel Cellular Modem caused by a logic error enabling permission bypass. Google has disclosed signs of limited targeted exploitation in the wild.
- **Impact**: Local privilege escalation on Pixel devices, potentially enabling baseband compromise, call/text interception, and persistence below the OS layer.
- **Status**: Limited targeted exploitation observed; patched in September 2026 Pixel security updates.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-58704
- **Reporting**: [The Hacker News — Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation](https://thehackernews.com/2026/09/google-patches-pixel-modem-flaw-amid.html)

### ConnectWise ScreenConnect Critical Flaw
- **Description**: A critical-severity vulnerability in ConnectWise ScreenConnect that CISA has confirmed is actively exploited in the wild. The flaw enables remote compromise of the remote access solution.
- **Impact**: Attackers can gain unauthorized access to ScreenConnect servers, potentially hijacking remote sessions, deploying implants, and accessing all connected endpoints.
- **Status**: Actively exploited per CISA advisory; patches available from ConnectWise.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Critical ScreenConnect flaw now actively exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-critical-screenconnect-flaw/)

### WooCommerce Wholesale Lead Capture Unauthenticated File Upload
- **Description**: A critical security flaw in the WooCommerce Wholesale Lead Capture WordPress plugin (6,000+ active installations) that allows unauthenticated attackers to upload arbitrary files, including PHP web shells, achieving remote code execution.
- **Impact**: Unauthenticated remote code execution on WordPress sites, leading to full site compromise, data theft, and use as a platform for further attacks.
- **Status**: Actively exploited; Wordfence has blocked numerous attempts. Plugin updates should be applied immediately.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Exploit WooCommerce Wholesale Lead Capture Flaw to Plant PHP Web Shells](https://thehackernews.com/2026/09/attackers-exploit-woocommerce-wholesale.html)

### Google Android Zero-Day on Pixel Devices
- **Description**: An actively exploited zero-day vulnerability in Android on Pixel devices, addressed as part of the September 2026 security patches covering 110 vulnerabilities total.
- **Impact**: Targeted attacks against Pixel users; specific impact depends on the vulnerability class but likely enables privilege escalation or sandbox escape.
- **Status**: Actively exploited in targeted attacks; patch available in September 2026 Pixel security bulletin.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Google fixes actively exploited Android zero-day on Pixel devices](https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-android-zero-day-on-pixel-devices/)

### Parallels Desktop for Mac Local Privilege Escalation
- **Description**: A flaw in Parallels Desktop for Mac that allows a non-administrator local user to execute code as root. The fix is included in Parallels Desktop 27, which cannot be installed on Intel-based Macs, leaving those systems permanently vulnerable.
- **Impact**: Local privilege escalation to root on macOS hosts running vulnerable Parallels versions, enabling full system compromise, persistence, and access to all user data and virtual machines.
- **Status**: Vulnerability disclosed with proof-of-concept; fix available only for Apple Silicon Macs (Parallels Desktop 27). Intel Macs cannot receive the fix.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Parallels Desktop Flaw Lets Non-Admin Mac Users Gain Root, but Intel Macs Can't Install Fix](https://thehackernews.com/2026/09/parallels-desktop-flaw-lets-non-admin.html)

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE)**: All versions prior to the emergency security update; enterprise network access control appliances.
- **Issabel Framework**: All versions containing the hard-coded credential flaw; open-source unified communications PBX deployments.
- **WSO2 API Manager**: Versions vulnerable to CVE-2026-5430; API gateway and management installations.
- **Acronis Backup Plugin for cPanel & WHM (Linux)**: Affected versions prior to the patched release; shared hosting and managed service provider environments.
- **Google Pixel Devices**: Pixel smartphones with vulnerable modem firmware prior to September 2026 security patch; specifically the Cellular Modem component.
- **ConnectWise ScreenConnect**: On-premises and cloud instances prior to the critical security update; remote monitoring and management platforms.
- **WooCommerce Wholesale Lead Capture Plugin**: WordPress sites running vulnerable versions of the premium plugin (6,000+ active installs); e-commerce platforms.
- **Parallels Desktop for Mac**: Versions prior to 27 on both Apple Silicon and Intel Macs; Intel Macs cannot upgrade to the fixed version 27.
- **Windows 11 (KB5124008)**: Systems with the September 2026 security update experiencing domain trust relationship failures; enterprise domain-joined endpoints.

## Attack Vectors and Techniques

- **SparroWocky Backdoor Deployment**: China-linked APT FamousSparrow deploys a new custom backdoor (SparroWocky) against government organizations in Latin America for persistent espionage access.
- **CHOSEN BRICK Windows Malware**: Iranian state-linked actors use this previously undocumented malware to spy on dissidents, activists, and journalists worldwide, featuring surveillance capabilities.
- **KREMLIN Toolkit Forced Extension Installation**: Banking malware operators bypass browser security checks to silently install malicious Chrome and Edge extensions that steal credentials, session tokens, and sensitive data. Active since mid-2025.
- **AI-Powered Data Breach**: First reported case to Spain's AEPD of an attack allegedly carried out by an AI agent powered by a known large language model, representing a novel automated intrusion vector.
- **BragJack Browser AI Hijacking**: Attack technique that subverts the agentic AI assistant built into browsers (Chrome, Edge, Opera, etc.) to access sensitive information, execute malicious actions, and exfiltrate data.
- **Issabel Framework Hard-Coded Credential RCE**: Unauthenticated attackers exploit a static credential in the framework to achieve remote OS command execution without any authentication.
- **Browser Extension AI Assistant Hijacking**: A single malicious browser extension can take control of AI assistants across five Chromium-based products (Gemini Live, Perplexity Comet, Microsoft Edge Copilot, Opera Neon, Claude in Chrome) with one click.
- **AI Coding Assistant Session Hijacking & Supply Chain Compromise**: Attacker hijacked an active AI coding assistant session at a SaaS provider, poisoned recommendations, and spread the Shai-Hulud worm across ~100 internal repositories, stealing secrets and source code.
- **N0va Phishkit Authentication Flow Abuse**: Phishing campaigns impersonate trusted services and abuse legitimate authentication flows (OAuth, SSO) to compromise valid accounts without malware, targeting US and EU businesses.
- **WSO2 API Manager JWT Signature Forgery**: Attackers forge administrative JWT tokens by exploiting improper cryptographic signature verification, achieving account takeover and API control.
- **WooCommerce Plugin Unauthenticated PHP Shell Upload**: Remote attackers upload PHP web shells via the Wholesale Lead Capture plugin's file upload functionality, gaining RCE without authentication.
- **North Korean Linux Espionage Toolkit**: Previously undocumented toolkit used to compromise load balancers, intercept communications, and pivot deeper into South Korean media and automotive sector networks.
- **Parallels Desktop Local Root Escalation**: Non-admin macOS users exploit a vulnerability in Parallels Desktop to gain root privileges, requiring only local code execution as a normal user.

## Threat Actor Activities

- **FamousSparrow (China-linked APT)**: Conducting government-focused espionage in Latin America using the novel SparroWocky backdoor. Demonstrates continued investment in custom tooling for regional intelligence collection.
- **Iranian State-Linked Actors**: Deploying CHOSEN BRICK Windows malware globally against dissidents, activists, and journalists. Indicates transnational repression operations leveraging custom surveillance implants.
- **Banking Malware Operators (KREMLIN Toolkit)**: Running a sustained campaign since mid-2025 using forced browser extension installation to harvest financial credentials and session tokens at scale.
- **NightEagle (APT-Q-95)**: Active since at least 2023, now targeting Russian enterprises with new persistence and lateral movement techniques alongside backdoor deployment.
- **Hacking Cat**: One of three threat clusters targeting Russian enterprises, employing backdoors, ransomware, and wipers in disruptive operations.
- **Toy Ghouls**: Third threat cluster hitting Russian organizations with destructive wiper and ransomware payloads alongside backdoor access.
- **Shai-Hulud Supply Chain Operator**: Compromised an AI coding assistant session at a SaaS provider to inject malicious recommendations, then propagated a worm across ~100 internal repositories to steal secrets and source code—demonstrating AI-assisted development pipeline as an attack surface.
- **North Korean APT (Assessed)**: Likely state-sponsored group using a novel Linux espionage toolkit to compromise load balancers in South Korean media and automotive sectors, enabling communications interception and network exploitation.
- **N0va Phishkit Operators**: Running credential-harvesting campaigns across North America and Europe that abuse legitimate authentication flows (OAuth/SSO) to bypass MFA and gain persistent account access without malware deployment.