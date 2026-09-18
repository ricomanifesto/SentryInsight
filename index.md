---
schema_version: 2
report_date: 2026-09-18
generated_at: 2026-09-18T10:58:24Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-18/
---
# Exploitation Report

## Executive Summary

A critical Cisco Identity Services Engine zero-day (CVE-2026-76460) with a maximum CVSS 10.0 score is under active exploitation in the wild, allowing unauthenticated remote attackers to bypass authentication on a core network access control platform. Cisco has released emergency patches, and organizations running ISE must prioritize immediate updating. Simultaneously, supply-chain attacks have surged: the Brevo marketing platform compromise injected ClickFix malware delivery scripts onto customer websites via a stolen Cloudflare API key, while 13 malicious npm packages distributed the novel WeaselBiscuit stealer targeting Chrome extension storage, and a separate PhantomRaven npm stealer was likely authored with LLM assistance. On the infrastructure front, a critical Docker Sandboxes escape (CVE-2026-77179) on macOS and a critical Unbound DNS resolver heap overflow (CVE-2026-81642) enable remote code execution, though active exploitation has not been confirmed for either.

Nation-state activity remains intense. The China-aligned FamousSparrow APT has deployed the previously unknown modular C++ backdoor SparroWocky against government targets across Latin America since at least August 2025. Iran-linked hacktivist persona Handala Hack operates the HEAVYGRAM Telegram backdoor and CRUDEEXCLUDE utility for surveillance, credential theft, and DLL sideloading. The DPRK-continued Contagious Interview campaign now leverages the WeaselBiscuit stealer, showing functional overlap with BeaverTail. Meanwhile, the RatHat Android malware—attributed to China-based actors—uses an AI-powered subsystem to automate device control and abuses ADB to persist shell access even after uninstallation, delivered via smishing and malvertising.

## Active Exploitation Details

### Cisco ISE Authentication Bypass Zero-Day
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Identity Services Engine (ISE) caused by insufficient authentication control on an API endpoint. An unauthenticated, remote attacker can bypass authentication entirely and gain access to the ISE administration interface.
- **Impact**: Full administrative control over the Identity Services Engine, which governs network access policies, guest access, device profiling, and policy enforcement across the enterprise network. Attackers can manipulate authentication policies, create rogue admin accounts, and pivot to connected network segments.
- **Status**: Actively exploited in the wild. Cisco has released security updates addressing the flaw.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76460
- **Reporting**: [Bleeping Computer — Cisco warns of max severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/), [The Hacker News — Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)

### WeaselBiscuit Stealer npm Supply-Chain Campaign
- **Description**: A cluster of 13 malicious npm packages distributing a previously undocumented JavaScript information stealer codenamed WeaselBiscuit. The malware specifically targets Chrome extension storage to harvest credentials, session tokens, and other sensitive data. Functional overlaps exist with BeaverTail malware associated with the DPRK's Contagious Interview campaign.
- **Impact**: Theft of browser-stored credentials, session cookies, cryptocurrency wallet data, and extension-specific secrets from developers and users who install the compromised packages. Potential lateral movement into development environments and CI/CD pipelines.
- **Status**: Active distribution via npm registry. Packages have been identified and reported; removal status varies.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage](https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html)

### PhantomRaven npm Stealer Campaign
- **Description**: A JavaScript-based information stealer distributed via the npm package registry by a financially motivated threat actor assessed to have used a large language model (LLM) to author the malware, evidenced by verbose comments, placeholder code, and statistical token-analysis patterns.
- **Impact**: Credential theft, exfiltration of environment variables, and potential compromise of development workflows for any project installing the malicious packages.
- **Status**: Active distribution via npm. Attribution to a claimed bug bounty hunter persona.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer](https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html)

### Brevo Supply-Chain ClickFix Injection
- **Description**: Attackers compromised a Cloudflare API key belonging to Brevo (marketing/email platform) and used it to inject malicious ClickFix scripts into Brevo's websites and JavaScript files embedded on customer sites. The ClickFix technique tricks users into executing malicious PowerShell commands via fake verification dialogs.
- **Impact**: Malware distribution to visitors of Brevo customer websites. The supply-chain nature amplifies impact across an unknown number of downstream sites. ClickFix leads to information stealer and loader deployment.
- **Status**: Active campaign confirmed by Brevo. Cloudflare API key rotated; injected scripts removed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Brevo supply-chain attack injected ClickFix scripts on customer sites](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)

### RatHat Android Malware with AI-Powered Control
- **Description**: A new Android malware family attributed to China-based threat actors featuring an AI-powered subsystem that automates navigation and control of compromised devices. Distributed via targeted smishing and malvertising leading to deceptive third-party download portals. Abuses Android Debug Bridge (ADB) to retain shell access even after the application is uninstalled.
- **Impact**: Persistent remote control of infected Android devices, credential theft, message interception, contact exfiltration, and potential use as a pivot for further attacks. ADB persistence survives app removal.
- **Status**: Active distribution campaigns observed. No patch available for the ADB abuse technique; requires user awareness and MDM controls.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — RatHat Android Malware Abuses ADB to Retain Shell Access After Uninstall](https://thehackernews.com/2026/09/rathat-android-malware-abuses-adb-to.html), [Bleeping Computer — New RatHat Android malware uses AI to automate device control](https://www.bleepingcomputer.com/news/security/new-rathat-android-malware-uses-ai-to-automate-device-control/)

### Handala Hack HEAVYGRAM Telegram Backdoor
- **Description**: Iran-linked hacktivist persona Handala Hack operates HEAVYGRAM, a Telegram-based surveillance backdoor with built-in commands for remote command execution, system/network/process discovery, data and Telegram session file exfiltration, screenshot capture, and DLL sideloading. A companion Delphi utility, CRUDEEXCLUDE, supports operations.
- **Impact**: Full surveillance and control of compromised Windows systems, credential theft from browsers and Telegram, lateral movement via DLL sideloading, and persistent access through Telegram C2.
- **Status**: Active operations attributed to Handala Hack. No vendor patch; detection and blocking of Telegram-based C2 required.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Iran-Linked Handala Hack Tied to HEAVYGRAM Telegram Backdoor That Can Steal Passwords](https://thehackernews.com/2026/09/iran-linked-handala-hack-tied-to.html)

### FamousSparrow SparroWocky Backdoor Espionage Campaign
- **Description**: The China-aligned state-sponsored actor FamousSparrow deploys SparroWocky, a previously unreported modular C++ backdoor, in attacks targeting government organizations across multiple Latin American countries since at least August 2025.
- **Impact**: Persistent access to government networks, credential theft, lateral movement, data exfiltration, and long-term espionage. Modular design allows plugin-based capability extension.
- **Status**: Active espionage campaign ongoing. ESET technical analysis published. No specific CVE exploited; likely leverages spear-phishing or vulnerability exploitation for initial access.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America](https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html), [Bleeping Computer — Chinese hackers use SparroWocky malware in govt espionage attacks](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/), [Dark Reading — China's FamousSparrow APT Spies on US Politics in Latin America](https://www.darkreading.com/cyberattacks-data-breaches/china-famoussparrow-spies-latin-america)

### Docker Sandboxes macOS Container Escape
- **Description**: A critical vulnerability in Docker Sandboxes on macOS where malicious code running inside a virtual machine can escape the shared project directory and read or modify arbitrary files on the host filesystem with the privileges of the host user account running the VM.
- **Impact**: Full host filesystem compromise from within a supposedly isolated container. Affects developers and CI/CD systems using Docker Sandboxes on macOS.
- **Status**: Patch available in updated Docker Sandboxes versions. No indication of active exploitation in the wild.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-77179
- **Reporting**: [The Hacker News — Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files](https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html)

### Unbound DNSSEC Validator Heap Overflow
- **Description**: A critical heap overflow in the DNSSEC validator of the Unbound DNS resolver affecting every release before 1.26.1. An attacker controlling a malicious DNS zone can trigger the overflow by querying a vulnerable resolver, achieving remote code execution.
- **Impact**: Remote code execution on any recursive resolver running vulnerable Unbound versions, potentially compromising DNS infrastructure and enabling cache poisoning, interception, or further network attacks.
- **Status**: Fixed in Unbound 1.26.1 released same day as advisory. No indication of active exploitation.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-81642
- **Reporting**: [The Hacker News — Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)

### Check Point Management Server RCE
- **Description**: A critical vulnerability in Check Point Security Management and Log Servers allowing unauthenticated remote attackers to execute code as root over the network. The Security Management Server controls firewall policy and administrator access.
- **Impact**: Complete compromise of the central firewall management platform, enabling policy modification, log tampering, and pivot to managed firewalls.
- **Status**: Fix released via LivePatch update channel. Check Point states it has no indication the flaw has been exploited.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — New Check Point flaw lets hackers execute code with root privileges](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/), [The Hacker News — Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html)

### BIND 9 DNS-over-HTTPS Crash
- **Description**: One of 14 flaws fixed in BIND 9.20.29 and 9.21.26 allows an unauthenticated sender to crash the `named` server process with a single DNS-over-HTTPS request carrying an invalid SIG record.
- **Impact**: Denial of service for any BIND server answering DoH queries. Remote, unauthenticated, single-request crash.
- **Status**: Patches available in BIND 9.20.29 and 9.21.26. No mention of active exploitation.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS](https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html)

## Affected Systems and Products

- **Cisco Identity Services Engine (ISE)**: All versions prior to the September 2026 security updates. Network access control and policy enforcement platform.
- **npm Package Registry / Node.js Projects**: Developers and CI/CD pipelines consuming packages from npm. Specific malicious packages identified in WeaselBiscuit (13 packages) and PhantomRaven campaigns.
- **Brevo Platform Customers**: Websites embedding Brevo JavaScript files or using Brevo services. Compromise via stolen Cloudflare API key allowed script injection.
- **Android Devices**: Devices installing applications from third-party sources via smishing/malvertising links. RatHat malware abuses ADB for post-uninstall persistence.
- **Docker Sandboxes on macOS**: Versions prior to the security fix for CVE-2026-77179. Developer workstations and macOS-based CI runners using Docker Sandboxes.
- **Unbound DNS Resolver**: All releases before 1.26.1. Recursive DNS servers validating DNSSEC.
- **Check Point Security Management Server and Log Server**: Versions prior to LivePatch update. Centralized firewall management infrastructure.
- **BIND 9 DNS Server**: Versions prior to 9.20.29 and 9.21.26. Authoritative and recursive DNS servers, particularly those enabling DNS-over-HTTPS.
- **Windows Systems**: Targets of HEAVYGRAM backdoor (Handala Hack) and SparroWocky backdoor (FamousSparrow).
- **Chrome/Chromium Browsers**: Targeted by WeaselBiscuit stealer for extension storage harvesting.

## Attack Vectors and Techniques

- **Supply-Chain Compromise via Stolen API Credentials**: Attackers stole a Cloudflare API key from Brevo and injected malicious ClickFix scripts into production JavaScript served to customer sites. Vector: compromised third-party service credentials.
- **Malicious Package Publishing to Public Registry**: Threat actors published 13 npm packages (WeaselBiscuit) and additional packages (PhantomRaven) to the public npm registry. Vector: typosquatting, dependency confusion, or social engineering to drive installs.
- **ClickFix Social Engineering**: Fake browser verification dialogs (CAPTCHA, "verify you are human") trick users into copying and executing malicious PowerShell commands. Vector: compromised legitimate websites serving injected scripts.
- **AI-Authored Malware**: PhantomRaven stealer shows high-confidence indicators of LLM-assisted development (verbose comments, placeholder code, token patterns). Vector: lowered barrier to malware creation.
- **AI-Powered Automated Device Control**: RatHat Android malware uses an AI subsystem to navigate UI, automate actions, and control compromised devices without constant operator attention. Vector: smishing and malvertising delivering APKs.
- **ADB Persistence Post-Uninstall**: RatHat enables ADB debugging and retains shell access via ADB even after the malicious app is removed by the user. Vector: Android Debug Bridge authorized during install.
- **Telegram-Based C2**: HEAVYGRAM uses Telegram Bot API for command-and-control, blending with legitimate traffic. Vector: Telegram messaging infrastructure.
- **Modular Backdoor Deployment**: SparroWocky (FamousSparrow) is a modular C++ backdoor allowing dynamic plugin loading for extensible espionage capabilities. Vector: initial access via unknown means (likely spear-phishing or exploit).
- **DNSSEC Validation Exploitation**: Malicious DNS zone triggers heap overflow in Unbound resolver during DNSSEC validation. Vector: attacker-controlled authoritative zone queried by vulnerable resolver.
- **Container Escape via Shared Filesystem**: Docker Sandboxes macOS flaw allows breaking out of the VM's project directory mount to access host filesystem. Vector: malicious code executed inside container.
- **Unauthenticated API Endpoint Abuse**: Cisco ISE flaw (CVE-2026-76460) and Check Point Management flaw both stem from insufficient authentication on network-exposed APIs. Vector: direct network access to management interfaces.

## Threat Actor Activities

- **FamousSparrow (China-aligned APT)**: Deploying the SparroWocky modular backdoor against government entities in Latin America since at least August 2025. Campaign focuses on political and eco-colonial influence interests. Technical analysis by ESET confirms modular C++ architecture.
- **Handala Hack (Iran-linked hacktivist)**: Operating the HEAVYGRAM Telegram backdoor and CRUDEEXCLUDE utility for surveillance, credential theft, DLL sideloading, and screenshot capture. Persona presents as hacktivist; infrastructure and tooling indicate sophisticated operations.
- **DPRK Contagious Interview Campaign Operators**: Extending tooling with WeaselBiscuit stealer (functional overlap with BeaverTail). Targeting developers via npm supply chain to harvest Chrome extension storage—likely aiming at cryptocurrency and DevOps credentials.
- **Financially Motivated npm Actor (PhantomRaven)**: Distributing LLM-assisted JavaScript stealer via npm. Actor claims bug bounty hunter persona; telemetry suggests financial motivation through credential theft and resale.
- **China-Based RatHat Operators**: Deploying AI-enhanced Android malware via smishing and malvertising. ADB persistence mechanism indicates focus on long-term device control. AI automation reduces operator workload.
- **NightmareStresser Operators (DDoS-for-hire)**: Infrastructure seized by FBI/DOJ. Platform linked to hundreds of thousands of DDoS attacks. Domains nightmare-stresser.com and nightmarestresser.org seized; operators disrupted.
- **Unknown/Unattributed (Brevo Supply Chain)**: Actor stole Cloudflare API key from Brevo and injected ClickFix scripts. Attribution not publicly assigned; technique overlaps with known ClickFix campaigns (e.g., TA571, ClearFake).