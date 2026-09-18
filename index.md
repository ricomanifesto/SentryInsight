---
schema_version: 2
report_date: 2026-09-18
generated_at: 2026-09-18T04:06:15Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-18/
---
# Exploitation Report

## Executive Summary

Three critical vulnerabilities with confirmed active exploitation demand immediate attention. Cisco's Identity Services Engine (ISE) zero-day (CVE-2026-76460, CVSS 10.0) is being actively exploited in the wild to bypass authentication on a widely deployed network access control platform. A critical container escape flaw in Docker Sandboxes on macOS (CVE-2026-77179) allows malicious guest code to read and modify host files with the privileges of the host account. Additionally, a critical heap overflow in the Unbound DNSSEC validator (CVE-2026-81642) enables remote code execution via a malicious DNS zone, affecting all Unbound resolver versions prior to 1.26.1.

State-sponsored espionage campaigns are intensifying across Latin America. China-aligned FamousSparrow has deployed the previously unknown modular C++ backdoor SparroWocky against government organizations since at least August 2025. Iran-linked actors are leveraging the HEAVYGRAM Telegram-based backdoor and CHOSEN BRICK Windows malware to target dissidents, activists, and journalists globally. Meanwhile, the Handala Hack persona has been attributed to both HEAVYGRAM and the CRUDEEXCLUDE Delphi utility, demonstrating shared tooling across Iranian-aligned operations.

Supply-chain and AI-enabled threats are emerging as significant force multipliers. The Brevo supply-chain attack demonstrated how a stolen Cloudflare API key can be weaponized to inject ClickFix scripts across customer sites for malware distribution. The RatHat Android malware incorporates an AI-powered subsystem to automate remote device navigation, while the KREMLIN toolkit enables banking malware to bypass browser security controls and forcibly install malicious Chrome and Edge extensions. Law enforcement disrupted the NightmareStresser DDoS-for-hire platform, seizing domains linked to hundreds of thousands of attacks.

## Active Exploitation Details

### Cisco ISE Authentication Bypass Zero-Day
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Identity Services Engine (ISE) caused by insufficient authentication control on an API endpoint. An unauthenticated, remote attacker can exploit this flaw to bypass authentication entirely.
- **Impact**: Full administrative access to the ISE platform, which controls network access policies, guest access, and device administration across enterprise networks. Compromise enables network persistence, lateral movement, and policy manipulation.
- **Status**: Cisco has released security updates addressing the vulnerability. Active exploitation confirmed in the wild.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76460
- **Reporting**: [The Hacker News — Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html), [Bleeping Computer — Cisco warns of max severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/)

### Docker Sandboxes Container Escape on macOS
- **Description**: A critical flaw in Docker Sandboxes for macOS where malicious code running inside a virtual machine can escape the project directory shared into it and read or change files anywhere else on the host system. The escape executes with the rights of the host account running the virtual machine.
- **Impact**: Complete host filesystem compromise from within a supposedly isolated container environment. Attackers can steal sensitive data, modify system files, and establish persistence on the macOS host.
- **Status**: Docker has issued a security announcement. Patched versions should be deployed immediately.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **CVE IDs**: CVE-2026-77179
- **Reporting**: [The Hacker News — Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files](https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html)

### Unbound DNSSEC Validator Heap Overflow
- **Description**: A critical heap overflow in the DNSSEC validator of the Unbound DNS resolver. An attacker who controls a malicious DNS zone and queries a vulnerable resolver can trigger the overflow, enabling remote code execution.
- **Impact**: Remote code execution on any DNS resolver running a vulnerable Unbound version. Given Unbound's widespread deployment as a validating resolver, this could affect ISPs, enterprises, and critical infrastructure relying on DNSSEC validation.
- **Status**: Fixed in Unbound 1.26.1 released by NLnet Labs. All versions prior to 1.26.1 are affected.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **CVE IDs**: CVE-2026-81642
- **Reporting**: [The Hacker News — Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)

### Check Point Security Management Server Unauthenticated RCE
- **Description**: A critical vulnerability in Check Point's Security Management and Log Servers allowing unauthenticated attackers to execute code as root over the network. The Security Management Server controls firewall policy and administrator access.
- **Impact**: Full root compromise of the central management plane for Check Point firewall infrastructure, enabling policy modification, log tampering, and lateral movement to managed gateways.
- **Status**: Check Point has released a fix through its LivePatch update channel. The vendor reports no indication of exploitation in the wild.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html)

### FamousSparrow SparroWocky Backdoor Campaign
- **Description**: China-aligned APT FamousSparrow deploying a previously unreported modular C++ backdoor called SparroWocky in espionage operations targeting government organizations across multiple Latin American countries since at least August 2025.
- **Impact**: Persistent access to government networks, credential theft, lateral movement, and long-term intelligence collection on political and economic targets in Latin America.
- **Status**: Active campaign observed by ESET researchers. No specific vulnerability exploited has been publicly disclosed; initial access vector remains under investigation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America](https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html), [Bleeping Computer — Chinese hackers use SparroWocky malware in govt espionage attacks](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/), [Dark Reading — China's FamousSparrow APT Spies on US Politics in Latin America](https://www.darkreading.com/cyberattacks-data-breaches/china-famoussparrow-spies-latin-america)

### Handala Hack HEAVYGRAM and CRUDEEXCLUDE Operations
- **Description**: Iran-linked "hacktivist" persona Handala Hack attributed to a Telegram-based surveillance backdoor (HEAVYGRAM) and a Delphi-based utility (CRUDEEXCLUDE). HEAVYGRAM supports remote command execution, system/network/process discovery, data and Telegram session exfiltration, screenshot capture, and DLL sideloading.
- **Impact**: Comprehensive endpoint surveillance and control, credential harvesting from Telegram sessions, and persistent access via DLL sideloading.
- **Status**: Active deployment observed. Attribution links Handala Hack to both tools.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Iran-Linked Handala Hack Tied to HEAVYGRAM Telegram Backdoor That Can Steal Passwords](https://thehackernews.com/2026/09/iran-linked-handala-hack-tied-to.html)

### Iranian CHOSEN BRICK Windows Malware Campaign
- **Description**: Iranian state-linked hackers using a Windows malware strain named CHOSEN BRICK to target dissidents, activists, and journalists worldwide. Government agencies have issued warnings about this campaign.
- **Impact**: Espionage against high-risk individuals, including credential theft, communications monitoring, and device compromise.
- **Status**: Active targeting campaign confirmed by government advisories.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Iranian hackers use CHOSEN BRICK Windows malware to spy on targets](https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/)

### RatHat Android Malware with AI Subsystem
- **Description**: New Android malware featuring an AI-powered subsystem that helps operators remotely navigate compromised devices, automating device control tasks that previously required manual interaction.
- **Impact**: Scalable device compromise with reduced operator overhead. AI automation enables simultaneous management of larger botnets and more sophisticated on-device actions.
- **Status**: Recently discovered in the wild. Distribution vectors under analysis.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — New RatHat Android malware uses AI to automate device control](https://www.bleepingcomputer.com/news/security/new-rathat-android-malware-uses-ai-to-automate-device-control/)

### Brevo Supply-Chain ClickFix Injection
- **Description**: Attackers stole a Cloudflare API key belonging to Brevo and used it to inject malicious ClickFix scripts into Brevo's websites and JavaScript files embedded on customer sites, distributing malware to visitors.
- **Impact**: Malware delivery to customers of Brevo's platform through trusted JavaScript dependencies. ClickFix technique tricks users into executing malicious commands.
- **Status**: Brevo confirmed the breach and API key compromise. Affected scripts have been removed.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Brevo supply-chain attack injected ClickFix scripts on customer sites](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)

### KREMLIN Toolkit Forced Browser Extension Installation
- **Description**: Banking malware operation active since mid-2025 using a toolkit named KREMLIN to bypass browser security checks and forcibly install malicious Chrome and Edge extensions that steal credentials, session tokens, and sensitive data.
- **Impact**: Persistent browser-level compromise surviving browser updates, credential theft from all sites visited, session hijacking, and bypass of two-factor authentication via session token theft.
- **Status**: Active campaign observed since mid-2025. Technique demonstrates reliable bypass of browser extension security controls.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Malware bypasses browser checks to force install Chrome, Edge extensions](https://www.bleepingcomputer.com/news/security/malware-bypasses-browser-checks-to-force-install-chrome-edge-extensions/)

### BIND 9 DNS Server Vulnerabilities
- **Description**: Fourteen security flaws fixed in BIND 9.20.29 and 9.21.26, including an unauthenticated crash vulnerability affecting any BIND server answering DNS-over-HTTPS (DoH) requests. A single invalid SIG record in a DoH request can crash the named process.
- **Impact**: Denial of service for DNS resolution services. Potential for additional undiscovered impacts in the remaining 13 flaws.
- **Status**: Patched versions released by ISC. No active exploitation reported for the DoH crash flaw.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS](https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html)

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE)**: All versions vulnerable to CVE-2026-76460 prior to patched releases. Network access control platform deployed across enterprise environments.
- **Docker Sandboxes for macOS**: Versions prior to the security fix. Container virtualization platform for macOS development environments.
- **Unbound DNS Resolver**: All versions prior to 1.26.1. Widely deployed validating resolver used by ISPs, enterprises, and recursive DNS infrastructure.
- **Check Point Security Management Server and Log Server**: Versions prior to LivePatch fix. Central management platform for Check Point firewall infrastructure.
- **Brevo Platform and Customer Sites**: Marketing automation platform; compromise affected embedded JavaScript on customer websites via Cloudflare API key theft.
- **Google Chrome and Microsoft Edge**: Browsers targeted by KREMLIN toolkit for forced malicious extension installation on Windows systems.
- **Android Devices**: Targeted by RatHat malware with AI-powered remote control subsystem.
- **Windows Systems**: Targeted by CHOSEN BRICK malware (Iranian campaign) and HEAVYGRAM/CRUDEEXCLUDE tooling (Handala Hack).
- **BIND 9 DNS Server**: Versions prior to 9.20.29 and 9.21.26. Authoritative and recursive DNS server software.
- **Telegram Desktop**: Targeted by HEAVYGRAM for session file exfiltration and surveillance.

## Attack Vectors and Techniques

- **Authentication Bypass via API Endpoint**: Exploitation of insufficient authentication controls on Cisco ISE API endpoints allowing unauthenticated remote access (CVE-2026-76460).
- **Container Escape via Host Filesystem Access**: Malicious guest code in Docker Sandboxes macOS VM escaping shared project directory to read/modify arbitrary host files with host account privileges (CVE-2026-77179).
- **DNSSEC Validation Heap Overflow**: Malicious DNS zone triggering heap overflow in Unbound resolver during DNSSEC validation, leading to RCE (CVE-2026-81642).
- **Supply-Chain API Key Theft**: Stolen Cloudflare API key used to inject malicious JavaScript (ClickFix scripts) into legitimate platform assets and downstream customer sites.
- **ClickFix Social Engineering**: Malicious scripts tricking users into executing attacker-controlled commands via fake verification prompts or error messages.
- **AI-Automated Device Control**: RatHat malware's AI subsystem automating remote navigation and control of compromised Android devices, reducing operator workload.
- **Browser Extension Forced Installation**: KREMLIN toolkit bypassing Chrome/Edge security checks to silently install malicious extensions with broad permissions.
- **Telegram-Based C2 and Exfiltration**: HEAVYGRAM using Telegram API for command-and-control, session hijacking, and data exfiltration.
- **DLL Sideloading Persistence**: HEAVYGRAM and CRUDEEXCLUDE leveraging DLL sideloading for persistence and privilege escalation on Windows.
- **DNS-over-HTTPS Crash**: Single malicious DoH request with invalid SIG record causing unauthenticated denial of service on BIND 9 servers.
- **Modular Backdoor Deployment**: SparroWocky's C++ modular architecture enabling plugin-based capability extension post-compromise.

## Threat Actor Activities

- **FamousSparrow (China-Aligned APT)**: Deploying SparroWocky modular backdoor in sustained espionage campaign against government entities across Latin America since August 2025. Focus on political intelligence collection amid US-China regional competition.
- **Handala Hack (Iran-Linked Hacktivist Persona)**: Operating HEAVYGRAM Telegram backdoor and CRUDEEXCLUDE Delphi utility for surveillance operations. Attributed to both tools, suggesting shared development or operational infrastructure.
- **Iranian State-Linked Actors (CHOSEN BRICK Campaign)**: Targeting dissidents, activists, and journalists globally with CHOSEN BRICK Windows malware. Government agencies have issued specific advisories naming this campaign.
- **NightmareStresser Operators**: Ran one of the world's longest-running DDoS-for-hire platforms linked to hundreds of thousands of attacks. Infrastructure seized by FBI/DOJ in coordinated takedown.
- **Banking Malware Operators (KREMLIN Toolkit)**: Active since mid-2025, leveraging novel browser extension installation bypass for credential theft and session hijacking at scale.
- **Brevo Supply-Chain Attackers**: Unknown threat actor compromising Cloudflare API key to weaponize marketing platform's JavaScript delivery for ClickFix malware distribution.
- **RatHat Malware Operators**: Unknown group deploying Android malware with AI-powered automation for scalable device compromise and control.