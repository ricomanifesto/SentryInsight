# Exploitation Report

## Executive Summary

A critical Metabase SQL injection vulnerability has been actively exploited as a zero-day in data theft campaigns targeting customer instances, with confirmed breaches at Framework and Tally. Simultaneously, a massive supply chain attack involving nearly 800 malicious npm packages has been discovered delivering cross-platform remote access trojans and infostealers across Windows, macOS, and Linux environments. These campaigns demonstrate the accelerating pace of both application-layer exploitation and software supply chain compromise.

Multiple threat actors are leveraging social engineering at scale. The UNC6671 extortion group—linked to the BlackFile operation—has conducted vishing campaigns targeting financial services, private equity, and hedge funds to steal SaaS data, while ClickFix-style attacks deliver Go-based macOS stealers capable of draining cryptocurrency wallets and harvesting iCloud Keychain credentials. Microsoft 365 environments face widespread adversary-in-the-middle phishing campaigns specifically targeting payroll and finance communications. Meanwhile, the TeamPCP threat actor has been linked to Redis compromise activity dating back to 2020, evolving into a broader supply chain campaign.

Researchers have disclosed several high-impact vulnerability classes with exploitation potential: an 18-year-old Linux SCTP use-after-free flaw enabling local root privilege escalation and container escape; the NatJack attack class manipulating NAT tables to hijack TCP sessions and spoof DNS; a pre-authentication WordPress XSS flaw demonstrated to achieve PHP code execution; the TONTOU CPU attack bypassing Spectre v2 mitigations to leak Linux password hashes; and a new Zapscape KVM vulnerability allowing L1 guest escape to the host. Cisco has released emergency patches for twelve SD-WAN and IOS XE vulnerabilities, including three carrying maximum 9.9 CVSS scores.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence software that allows unauthenticated attackers to execute arbitrary SQL commands against the backend database.
- **Impact**: Full database access leading to customer data theft, including sensitive business analytics, user credentials, and proprietary information. Confirmed breaches at Framework and Tally.
- **Status**: Actively exploited as a zero-day before disclosure. Patches should be applied immediately; all self-hosted Metabase instances are at risk.

### Malicious npm Package Supply Chain Campaign
- **Description**: A cluster of nearly 800 malicious packages published to the npm registry designed to deliver cross-platform malware.
- **Impact**: Deployment of remote access trojans (RATs) and infostealers across Windows, macOS, and Linux systems. Developers and CI/CD pipelines consuming compromised packages face credential theft, environment compromise, and lateral movement.
- **Status**: Active campaign discovered in the npm registry. Affected packages have been reported for takedown; organizations must audit dependencies and rotate secrets.

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks tricking users into executing malicious commands via fake verification prompts, delivering a Go-based infostealer.
- **Impact**: Theft of cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials on macOS systems.
- **Status**: Active campaigns targeting macOS users. No patch required—mitigation relies on user awareness and endpoint detection.

### UNC6671 Vishing and Data Extortion Operations
- **Description**: Voice phishing (vishing) campaigns by the UNC6671 extortion group targeting employees at financial services, private equity, and professional services firms to gain SaaS access.
- **Impact**: Unauthorized access to SaaS platforms, data exfiltration, and subsequent extortion demands. Linked to hedge fund breaches and the BlackFile threat ecosystem.
- **Status**: Active ongoing campaigns. Mitigation requires MFA hardening, vishing awareness training, and SaaS access monitoring.

### Microsoft 365 Adversary-in-the-Middle Phishing
- **Description**: Widespread email-driven phishing campaign employing adversary-in-the-middle (AitM) techniques to bypass multi-factor authentication and hijack Microsoft 365 sessions.
- **Impact**: Account takeover with persistent access to payroll, finance, and sensitive corporate communications. Attackers maintain access through stolen session tokens.
- **Status**: Active large-scale campaign. Phishing-resistant MFA (FIDO2/WebAuthn) and Conditional Access policies are critical mitigations.

### WordPress Pre-Authentication Reflected XSS
- **Description**: A reflected cross-site scripting vulnerability in the WordPress login screen affecting all versions, demonstrated by pwn.ai to achieve PHP code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary JavaScript in victim browsers, with a demonstrated chain to remote code execution on the server.
- **Status**: Patched in recent WordPress releases. All sites must update immediately; the vulnerability is exploitable pre-authentication.

### Linux SCTP Use-After-Free (18-Year-Old Flaw)
- **Description**: A use-after-free bug in the Linux kernel's SCTP (Stream Control Transmission Protocol) networking code present for approximately 18 years.
- **Impact**: Local privilege escalation to root and container escape. Tencent researchers demonstrated successful container breakout to the underlying host.
- **Status**: Vulnerability disclosed with proof-of-concept. Kernel patches required; containerized environments at elevated risk.

### NatJack NAT Manipulation Attack Class
- **Description**: A novel attack technique manipulating network address translation (NAT) connection state tables to hijack active TCP sessions and spoof DNS responses.
- **Impact**: Session hijacking, traffic interception, and DNS spoofing without requiring direct network position between victims.
- **Status**: Research disclosure by Malcolm Stagg. Mitigations involve NAT configuration hardening and encrypted transport enforcement.

### TONTOU CPU Speculative Execution Attack
- **Description**: A new speculative execution side-channel attack bypassing existing Spectre v2 mitigations to leak secrets from Linux systems.
- **Impact**: Extraction of password hashes and other sensitive data from kernel memory on affected CPU architectures.
- **Status**: Research disclosure with exploit demonstration. Microcode and kernel mitigations under development.

### Zapscape KVM Guest Escape Vulnerability
- **Description**: A Linux kernel vulnerability in KVM (Kernel-based Virtual Machine) allowing privileged L1 guest code to escape isolation and execute code on the host.
- **Impact**: Full host compromise from a compromised nested virtual machine. Affects virtualized and cloud environments using KVM.
- **Status**: Disclosed with technical details. Kernel patches required for host systems.

### Cisco Catalyst SD-WAN and IOS XE Critical Vulnerabilities
- **Description**: Twelve security vulnerabilities in Cisco Catalyst SD-WAN and IOS XE Software identified during an internal security review, including three rated 9.9 CVSS.
- **Impact**: Remote code execution, authentication bypass, and device takeover on critical network infrastructure.
- **Status**: Patches released. Immediate application recommended for all affected deployments.

### Snowflake Data Extortion Campaign
- **Description**: Large-scale credential-based attacks against Snowflake customer instances resulting in data theft and extortion of over 165 organizations.
- **Impact**: Massive data exfiltration from cloud data warehouses, subsequent extortion demands, and regulatory exposure for affected entities.
- **Status**: Canadian threat actor pleaded guilty; campaign attributed to compromised credentials and lack of MFA on service accounts.

### Swiss Government SharePoint Breach
- **Description**: Exploitation of vulnerabilities in Microsoft SharePoint servers operated by Switzerland's federal IT office.
- **Impact**: Compromise of approximately 200 accounts with access to government systems and data.
- **Status**: Breach confirmed; investigation ongoing. Patch management and SharePoint hardening required.

### TeamPCP Redis and Supply Chain Attacks
- **Description**: Threat actor TeamPCP compromising internet-facing Redis instances since at least 2020, later leveraging access for supply chain campaigns.
- **Impact**: Persistent infrastructure compromise, potential software supply chain poisoning, and lateral movement into connected environments.
- **Status**: Historical activity uncovered; ongoing risk from compromised infrastructure and supply chain artifacts.

### Windows Hello for Business Key Abuse
- **Description**: Malware running in a signed-in Windows session can silently use the victim's Windows Hello for Business key to authenticate to Microsoft Entra ID.
- **Impact**: Persistent, MFA-bypassing access to Entra ID resources without requiring credential theft or phishing.
- **Status**: Research demonstration by Dirk-jan Mollema. Mitigations require TPM-backed key protections and session monitoring.

### Claude Code and Gemini CLI CI/CD Vulnerabilities
- **Description**: Flaws in Anthropic's Claude Code and Google's Gemini CLI allowing a GitHub issue opened by an unprivileged account to execute code on CI runners and access workflow secrets.
- **Impact**: Supply chain compromise through CI/CD pipeline hijacking, secret exfiltration, and potential artifact poisoning.
- **Status**: Disclosed with proof-of-concept. Configuration hardening and least-privilege CI runners recommended.

### AI Agent Sandbox Escapes
- **Description**: Multiple sandbox escape events affecting OpenAI, Anthropic, and Meta AI agents, including a researcher demonstration of C2-style control over ChatGPT's isolated sandbox at Black Hat USA 2026.
- **Impact**: Potential breakout from AI execution environments to underlying infrastructure, with implications for AI-assisted development and autonomous agent deployments.
- **Status**: Disclosed by affected vendors and researchers. Sandbox architecture reviews underway.

### AI-Generated Patch Reliability Concerns
- **Description**: Study of over 6,000 AI-generated patches finding that even functionally correct patches frequently introduce new bugs, break existing functionality, or contain bypassable fixes.
- **Impact**: Risk of incomplete or harmful remediation when relying on automated vulnerability patching without human review.
- **Status**: Research finding; not an active exploitation vector but relevant to vulnerability management processes.

## Affected Systems and Products

- **Metabase**: All self-hosted versions prior to emergency patch; Framework and Tally confirmed breached
- **npm Registry**: Nearly 800 malicious packages affecting Node.js projects across Windows, macOS, and Linux
- **macOS**: Systems targeted by ClickFix-delivered Go-based infostealer (cryptocurrency wallets, browsers, iCloud Keychain)
- **Microsoft 365 / Entra ID**: Tenants targeted by AitM phishing; Windows Hello for Business keys exploitable for persistent access
- **WordPress**: All versions affected by pre-auth reflected XSS in login screen; PHP code execution demonstrated
- **Linux Kernel**: SCTP subsystem (18-year-old use-after-free); KVM hypervisor (Zapscape guest escape); Spectre v2 mitigations bypassed by TONTOU
- **Network Infrastructure**: Cisco Catalyst SD-WAN and IOS XE Software (12 vulnerabilities, three 9.9 CVSS)
- **Cloud Data Platforms**: Snowflake customer instances (165+ organizations extorted via credential compromise)
- **Microsoft SharePoint**: Swiss federal government servers breached (~200 accounts compromised)
- **Redis**: Internet-facing instances compromised by TeamPCP since 2020
- **CI/CD Pipelines**: GitHub Actions runners for Anthropic Claude Code, Google Gemini CLI, and OpenAI repositories
- **AI Sandboxes**: OpenAI ChatGPT, Anthropic, and Meta AI agent execution environments

## Attack Vectors and Techniques

- **SQL Injection (Zero-Day)**: Unauthenticated database command execution via Metabase vulnerability
- **Software Supply Chain Compromise**: Malicious package publication to npm registry targeting developer dependencies
- **ClickFix Social Engineering**: Fake verification prompts tricking users into executing malicious PowerShell/terminal commands
- **Voice Phishing (Vishing)**: Telephone-based social engineering to harvest credentials and MFA codes for SaaS access
- **Adversary-in-the-Middle (AitM) Phishing**: Reverse proxy toolkits intercepting credentials and session tokens in real-time
- **Reflected Cross-Site Scripting**: Pre-authentication XSS in login forms chained to server-side code execution
- **Local Privilege Escalation**: Kernel use-after-free in SCTP subsystem for root access
- **Container Escape**: SCTP flaw and Zapscape KVM vulnerability enabling breakout from containerized/VM environments
- **NAT Table Manipulation (NatJack)**: Connection state hijacking and DNS spoofing via NAT side-channel
- **Speculative Execution Side-Channel (TONTOU)**: CPU microarchitectural attack bypassing Spectre v2 mitigations
- **Network Device Exploitation**: Critical RCE and auth bypass in SD-WAN and routing platforms
- **Credential Stuffing / Credential Reuse**: Snowflake extortion campaign leveraging compromised credentials without MFA
- **Windows Hello Key Abuse**: Malware leveraging TPM-backed authentication keys for silent Entra ID persistence
- **CI/CD Pipeline Injection**: Unprivileged GitHub issues triggering code execution on privileged runners
- **AI Sandbox Escape**: Adversarial inputs achieving C2-style control over isolated AI execution environments

## Threat Actor Activities

- **UNC6671 / BlackFile-Linked Extortion Group**: Active vishing campaigns targeting financial services, private equity, hedge funds, and professional services; data theft followed by extortion; Canadian operator pleaded guilty in Snowflake campaign
- **TeamPCP**: Long-term Redis infrastructure compromise since 2020; evolved into software supply chain campaign; persistent access to internet-facing databases
- **ClickFix Operators**: Ongoing campaigns delivering cross-platform malware via social engineering; macOS-focused infostealer for crypto theft and credential harvesting
- **Microsoft 365 AitM Phishing Actors**: Large-scale email campaigns targeting payroll and finance departments; session token theft for persistent access
- **Snowflake Extortion Actor**: Canadian individual (pleaded guilty) responsible for compromising 165+ organizations via credential reuse
- **Malicious npm Package Publishers**: Coordinated publication of ~800 packages delivering RATs and infostealers; cross-platform targeting
- **Metabase Zero-Day Exploiters**: Unknown actors exploiting SQLi before disclosure; confirmed data theft from Framework and Tally instances

## Source Attribution

- **Metabase SQLi zero-day exploited in customer data-theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/framework-tally-disclose-metabase-data-theft-attacks/
- **Unlimited Technology Systems breach impacts 3.8 million people**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/unlimited-technology-systems-breach-impacts-38-million-people/
- **Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer**: The Hacker News - https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html
- **ClickFix Attacks Deliver macOS Stealer That Can Drain Crypto Wallets**: The Hacker News - https://thehackernews.com/2026/08/clickfix-attacks-deliver-macos-stealer.html
- **UNC6671 Vishing Attacks Target Personal Phones to Steal SaaS Data**: The Hacker News - https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html
- **AI-Generated Patches Fail Half the Time**: Dark Reading - https://www.darkreading.com/application-security/ai-generated-patches-fail-half-time
- **Levi Strauss \& Co. says hackers stole corporate data in cyberattack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/levi-strauss-and-co-says-hackers-stole-corporate-data-in-cyberattack/
- **Real emails, hijacked payments: Two H1 2026 attack chains**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/real-emails-hijacked-payments-two-h1-2026-attack-chains/
- **North Carolina Ports confirms cyberattack disrupting operations**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/north-carolina-ports-confirms-cyberattack-disrupting-operations/
- **New WordPress Pre-Auth XSS Could Lead to PHP Code Execution - Patch ASAP**: The Hacker News - https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html
- **Growing Up The Hard Way**: The Hacker News - https://thehackernews.com/2026/08/growing-up-hard-way.html
- **18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers**: The Hacker News - https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html
- **New NatJack Attacks Hijack TCP Sessions and Spoof DNS by Manipulating NAT Tables**: The Hacker News - https://thehackernews.com/2026/08/new-natjack-attacks-hijack-tcp-sessions.html
- **Microsoft 365 AitM Phishing Hijacks Accounts to Collect Payroll and Finance Emails**: The Hacker News - https://thehackernews.com/2026/08/microsoft-365-aitm-phishing-hijacks.html
- **AI-Assisted HTTP Terminator Finds Novel HTTP Desync Techniques and Apache Zero-Day**: The Hacker News - https://thehackernews.com/2026/08/ai-assisted-http-terminator-finds-novel.html
- **Malware Can Abuse Windows Hello for Business Keys for Persistent Entra ID Access**: The Hacker News - https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html
- **Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets**: The Hacker News - https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html
- **TeamPCP Linked To Redis Attacks Dating Back To 2020 And Later Supply Chain Campaign**: The Hacker News - https://thehackernews.com/2026/08/teampcp-linked-to-redis-attacks-dating.html
- **OpenAI rolls out a major ChatGPT upgrade, even if you don’t pay for it**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-rolls-out-a-major-chatgpt-upgrade-even-if-you-dont-pay-for-it/
- **ClickFix attack pushes macOS infostealer for crypto theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/clickfix-attack-pushes-macos-infostealer-for-crypto-theft-attacks/
- **The Coordination Gap: How Attackers Are Outpacing Law Enforcement**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/coordination-gap-attackers-outpacing-law-enforcement
- **Déjà Vu? Meta's AI Escapes Testing Lab in Hacking Joyride**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/meta-ai-escapes-lab-hacking-joyride
- **Researcher Claims Control of ChatGPT Secure Sandbox**: Dark Reading - https://www.darkreading.com/cloud-security/researcher-claims-control-chatgpt-secure-sandbox
- **Hedge fund cyberattacks tied to BlackFile-linked UNC6671 extortion group**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hedge-fund-cyberattacks-tied-to-blackfile-linked-unc6671-extortion-group/
- **From Bobmojis to Bobbleheads: How the Democratic Party Built a Security-First Culture**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/from-bobmojis-to-bobbleheads-how-the-democratic-party-built-a-security-first-culture
- **Swiss government SharePoint breach compromised 200 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/swiss-government-sharepoint-breach-compromised-200-accounts/
- **New TONTOU CPU attack bypasses Spectre v2 fixes, leaks Linux password hashes**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-tontou-cpu-attack-bypasses-spectre-v2-fixes-leaks-linux-password-hashes/
- **New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts**: The Hacker News - https://thehackernews.com/2026/08/new-zapscape-kvm-flaw-could-let.html
- **Cisco Patches 12 SD-WAN and IOS XE Flaws, Including Three 9.9 CVSS Score Bugs**: The Hacker News - https://thehackernews.com/2026/08/cisco-patches-12-sd-wan-and-ios-xe.html
- **Canadian Man Pleads Guilty in Snowflake Extortions**: Krebs on Security - https://krebsonsecurity.com/2026/08/canadian-man-pleads-guilty-in-snowflake-extortions/
