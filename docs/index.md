# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively underway across diverse technology stacks, ranging from enterprise collaboration platforms and business intelligence tools to supply chain infrastructure and AI-assisted development environments. The Head Mare hacktivist group has compromised TrueConf video conferencing servers to distribute backdoored client installers, while a critical Metabase zero-day SQL injection flaw has been exploited in data theft attacks against Framework and Tally. Simultaneously, the UNC6671 extortion group—linked to the BlackFile threat actor—is conducting vishing campaigns targeting financial services and private equity firms, and a widespread Microsoft 365 adversary-in-the-middle phishing operation is hijacking accounts to harvest payroll and finance communications.

Critical infrastructure remains under heavy pressure: CISA has added a Progress Kemp LoadMaster vulnerability to its Known Exploited Vulnerabilities catalog after 792 reported exploit attempts, N-able has issued emergency hotfixes for N-central RMM as attackers persist in managed environments, and an 18-year-old Linux SCTP use-after-free flaw enables local root escalation and container escapes. Supply chain attacks have surged with nearly 800 malicious npm packages delivering cross-platform RATs and infostealers, while TeamPCP has been linked to Redis compromises dating back to 2020 and a subsequent supply chain campaign. Novel attack research reveals CSS-based webmail escape techniques affecting major providers, AI-discovered HTTP desynchronization vulnerabilities in Apache, and NatJack attacks manipulating NAT tables to hijack TCP sessions and spoof DNS.

## Active Exploitation Details

### TrueConf Server Compromise and Supply Chain Backdooring
- **Description**: The Head Mare hacktivist group is exploiting vulnerabilities in unpatched TrueConf video conferencing servers to gain access and replace legitimate client installers with trojanized versions containing backdoors.
- **Impact**: Attackers achieve persistent access to victim networks through software supply chain compromise; downstream users installing the malicious clients receive backdoored software granting remote access.
- **Status**: Active exploitation of unpatched servers; organizations running TrueConf should verify installer integrity and apply server patches immediately.

### Metabase Zero-Day SQL Injection (Data Theft Campaign)
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence software is being exploited as a zero-day to achieve unauthenticated administrative access and exfiltrate customer data.
- **Impact**: Full administrative control over Metabase instances without authentication; confirmed data theft from Framework and Tally customer environments.
- **Status**: Actively exploited in the wild; Metabase has issued warnings; emergency patching required for all exposed instances.

### N-able N-central RMM Exploitation
- **Description**: Attackers are actively exploiting a recently disclosed security flaw in N-able's N-central Remote Monitoring and Management platform to reach managed systems and establish persistence.
- **Impact**: Compromise of managed service provider infrastructure enables lateral access to all downstream client systems under management.
- **Status**: Ongoing exploitation; N-able has released Hotfix 2 as part of active investigation; immediate application recommended for all N-central deployments.

### Progress Kemp LoadMaster Critical Flaw
- **Description**: A critical-severity vulnerability in Progress Kemp LoadMaster application delivery controllers is under active exploitation with significant volume.
- **Impact**: Pre-authentication remote code execution potential on load balancers controlling traffic for critical applications.
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog after 792 reported exploit attempts; emergency patching mandated for federal agencies and strongly advised for all users.

### WordPress Pre-Authentication Reflected XSS
- **Description**: A reflected cross-site scripting vulnerability in the WordPress login screen affects every version of the CMS and can be chained to achieve PHP code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary JavaScript in victim browsers; researcher pwn.ai demonstrated escalation to remote code execution.
- **Status**: WordPress has released patches; all versions prior to the fixed release are affected; immediate update required.

### Linux SCTP Use-After-Free (18-Year-Old Flaw)
- **Description**: A use-after-free vulnerability in the Linux kernel's SCTP networking subsystem, present for approximately 18 years, allows local users to gain root privileges and escape containers.
- **Impact**: Full host root compromise from unprivileged local access; container escape to underlying host confirmed by Tencent researchers.
- **Status**: Publicly disclosed with exploit demonstration; kernel patches in progress; high urgency for containerized and multi-tenant environments.

### Apache HTTP Server Zero-Day (AI-Discovered)
- **Description**: PortSwigger's AI-assisted HTTP Terminator research system discovered novel HTTP request desynchronization techniques and an Apache zero-day vulnerability after exploring 30,000 candidates.
- **Impact**: HTTP desynchronization enables request smuggling, cache poisoning, and potential bypass of security controls on affected Apache deployments.
- **Status**: Zero-day disclosed by research team; Apache patch timeline pending; monitoring for active exploitation advised.

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks deliver a Go-based malware targeting macOS users, stealing cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials.
- **Impact**: Comprehensive credential and cryptocurrency theft from compromised macOS endpoints; bypasses traditional email security through user-interaction deception.
- **Status**: Active campaigns observed; multiple security vendors reporting detections; user awareness and endpoint detection critical.

### Microsoft 365 Adversary-in-the-Middle Phishing
- **Description**: A widespread email-driven phishing campaign employs adversary-in-the-middle (AitM) techniques to hijack Microsoft 365 session tokens and take full control of victim accounts.
- **Impact**: Complete account takeover with persistent access; targeted collection of payroll and finance emails for business email compromise and financial fraud.
- **Status**: Active widespread campaign; traditional MFA bypassed via token theft; phishing-resistant authentication (FIDO2, certificate-based) recommended.

### UNC6671 Vishing and Data Extortion
- **Description**: The UNC6671 data extortion group, reportedly linked to the BlackFile threat actor, conducts voice phishing (vishing) attacks targeting personal phones of employees at financial services, private equity, and professional services firms.
- **Impact**: Credential theft and SaaS data exfiltration through social engineering; subsequent extortion operations leveraging stolen data.
- **Status**: Active campaign confirmed against hedge funds and financial organizations; employee training on vishing and privileged access controls advised.

### TeamPCP Redis and Supply Chain Campaign
- **Description**: Threat actor TeamPCP has been compromising internet-facing Redis instances since at least 2020, later expanding into a supply chain campaign affecting downstream software consumers.
- **Impact**: Long-term persistent access to Redis infrastructure; supply chain compromise enabling broader victim targeting through trusted software distribution channels.
- **Status**: Historical activity confirmed through 2020; recent supply chain linkage discovered; Redis exposure audit and supply chain integrity verification recommended.

### Malicious npm Package Campaign (Cross-Platform RAT/Infostealer)
- **Description**: Nearly 800 malicious packages published to the npm registry deliver cross-platform remote access trojans and infostealers targeting Windows, macOS, and Linux systems.
- **Impact**: Developer machine compromise leading to source code theft, CI/CD credential harvesting, and potential software supply chain poisoning.
- **Status**: Active cluster detected; npm takedowns in progress; dependency scanning and lockfile verification essential for all Node.js projects.

### CSS-Based Webmail Escape Attacks
- **Description**: Novel CSS injection techniques allow email content to escape message boundaries and interfere with webmail interface rendering, enabling credential and token theft across major providers.
- **Impact**: Cross-provider attack chains affecting Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail; bypasses traditional content security policies through CSS manipulation.
- **Status**: Research disclosure with proof-of-concept across multiple providers; vendor mitigations in progress; content security policy hardening recommended.

### Atlassian Rovo Data Exfiltration
- **Description**: Attacker-controlled instructions can manipulate Atlassian's Rovo AI assistant to collect Jira and Confluence data accessible to a signed-in user and exfiltrate it to an external server.
- **Impact**: Unauthorized access to sensitive project management and wiki data through AI assistant prompt injection; leverages legitimate user permissions.
- **Status**: Discovered by two security firms; Atlassian mitigation status pending; prompt injection defenses and Rovo access controls advised.

### Windows Hello for Business Key Abuse
- **Description**: Malware running in a signed-in Windows session can silently use the victim's Windows Hello for Business cryptographic key to authenticate to Microsoft Entra ID, achieving persistent cloud identity access.
- **Impact**: Persistent Entra ID authentication without credential theft; bypasses conditional access and MFA by leveraging hardware-bound keys already authenticated.
- **Status**: Proof-of-concept demonstrated by researcher Dirk-jan Mollema; detection via anomalous Entra ID sign-in patterns; endpoint isolation controls recommended.

### Claude Code and Gemini CLI CI/CD Secret Exposure
- **Description**: Vulnerabilities in Anthropic's Claude Code and Google's Gemini CLI allow a GitHub issue opened by an unprivileged account to execute code on CI runners, exposing workflow secrets in their own repositories.
- **Impact**: CI/CD secret theft from AI coding agent repositories; potential supply chain impact through compromised build pipelines; OpenAI's similar tooling also affected.
- **Status**: Disclosed by security researchers; vendor patches in progress; GitHub Actions permission hardening and secret rotation advised.

### NatJack NAT Manipulation Attacks
- **Description**: A new attack class called NatJack manipulates network address translation (NAT) connection state tables to hijack active TCP sessions and spoof DNS responses.
- **Impact**: Session hijacking and DNS spoofing without direct network interception; exploits fundamental NAT behavior in routers and firewalls.
- **Status**: Research disclosure by Malcolm Stagg; vendor engagement for network equipment patches; network monitoring for anomalous NAT state changes recommended.

## Affected Systems and Products

- **TrueConf Video Conferencing Server**: Unpatched server versions vulnerable to exploitation enabling installer replacement; client installers distributed from compromised servers contain backdoors.
- **Metabase Business Intelligence Platform**: All versions prior to emergency patch vulnerable to unauthenticated SQL injection leading to admin access and data theft; Framework and Tally confirmed impacted.
- **N-able N-central RMM**: Affected versions prior to Hotfix 2; managed service provider infrastructure and all downstream client systems at risk.
- **Progress Kemp LoadMaster**: Vulnerable firmware versions across LoadMaster appliance and virtual deployments; critical for application delivery infrastructure.
- **WordPress CMS**: Every version prior to latest security release affected by pre-auth reflected XSS in login screen; universal impact across WordPress ecosystem.
- **Linux Kernel**: Versions with SCTP module enabled (default in most distributions) vulnerable to local root escalation and container escape; 18-year regression window.
- **Apache HTTP Server**: Versions affected by HTTP desynchronization zero-day discovered via AI research; specific version range pending vendor advisory.
- **macOS Systems**: Targeted by ClickFix-delivered Go-based infostealer; all versions supporting current browser and Keychain architectures.
- **Microsoft 365 / Entra ID**: Tenants with accounts targeted by AitM phishing; Windows Hello for Business deployments vulnerable to key reuse by local malware.
- **Redis Instances**: Internet-exposed Redis servers compromised by TeamPCP since 2020; default configurations without authentication particularly at risk.
- **npm Registry / Node.js Ecosystem**: Nearly 800 malicious packages published; all projects consuming npm dependencies without integrity verification.
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail vulnerable to CSS-based message boundary escape; client-side rendering engines affected.
- **Atlassian Rovo / Jira / Confluence**: Cloud deployments with Rovo AI assistant enabled; data accessible to signed-in users exfiltratable via prompt injection.
- **CI/CD Systems (GitHub Actions)**: Repositories using Claude Code, Gemini CLI, or similar AI coding agents with workflow secrets exposed to issue-triggered execution.
- **Network Infrastructure (NAT Devices)**: Routers, firewalls, and carrier-grade NAT equipment vulnerable to connection state manipulation enabling TCP hijacking and DNS spoofing.

## Attack Vectors and Techniques

- **Software Supply Chain Compromise**: Legitimate vendor infrastructure (TrueConf servers) breached to distribute trojanized installers; malicious npm packages published to public registry targeting developer environments.
- **Zero-Day Vulnerability Exploitation**: Metabase SQLi, Apache HTTP desync, Progress Kemp LoadMaster, and N-central flaws exploited before or immediately after disclosure; Linux SCTP flaw exploited after 18-year dormancy.
- **Adversary-in-the-Middle (AitM) Phishing**: Proxy-based phishing kits capturing session tokens to bypass MFA; targeting Microsoft 365 for payroll and finance email access.
- **Voice Phishing (Vishing)**: UNC6671 uses phone-based social engineering against personal devices to steal SaaS credentials; targets financial sector employees.
- **ClickFix Social Engineering**: Deceptive user interaction prompts (fake CAPTCHA, verification dialogs) deliver malware via PowerShell/clipboard commands; macOS-targeted Go binary deployment.
- **CSS Injection / Webmail Escape**: Malicious CSS in email content breaks out of message sandbox to manipulate webmail DOM; steals credentials and tokens across multiple providers.
- **Prompt Injection Against AI Assistants**: Attacker-controlled instructions manipulate Atlassian Rovo to exfiltrate accessible Jira/Confluence data; indirect injection via shared content.
- **Container Escape via Kernel Exploit**: Linux SCTP use-after-free enables breakout from containerized environments to host root; impacts multi-tenant and Kubernetes deployments.
- **NAT Connection State Manipulation (NatJack)**: Spoofed packets manipulate NAT mapping tables to hijack established TCP sessions and inject DNS responses; no MITM position required.
- **Windows Hello Key Reuse by Malware**: Local malware leverages authenticated hardware-bound keys for silent Entra ID authentication; persists across password changes and MFA.
- **CI/CD Pipeline Abuse via AI Tooling**: GitHub Issues trigger vulnerable AI coding agents (Claude Code, Gemini CLI) to execute on runners with secret access; privilege escalation from zero-permission accounts.
- **HTTP Request Desynchronization (AI-Discovered)**: Novel desync techniques enable request smuggling, cache poisoning, and WAF bypass on Apache and potentially other servers.
- **Long-Term Redis Compromise**: TeamPCP maintains persistent access to exposed Redis instances since 2020; later leveraged for supply chain attacks on software consumers.
- **Cross-Platform Malware Delivery**: Single campaign (npm packages) delivers functionally equivalent RAT/infostealer payloads across Windows, macOS, and Linux.

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Exploiting TrueConf server vulnerabilities to trojanize client installers with backdoors; supply chain targeting of video conferencing users; politically motivated destructive and espionage activity.
- **UNC6671 (Data Extortion Group / BlackFile-Linked)**: Conducting vishing campaigns against financial services, private equity, hedge funds, and professional services; stealing SaaS credentials and data for extortion; attributed to recent wave of hedge fund cyberattacks.
- **TeamPCP (Cybercrime Actor)**: Compromising internet-facing Redis instances since at least 2020; evolved into supply chain campaign affecting downstream software consumers; long-term infrastructure persistence and operational security.
- **ClickFix Operators (Unattributed)**: Running active campaigns delivering macOS infostealer (Go-based) for cryptocurrency theft, credential harvesting, and Keychain exfiltration; leveraging social engineering over email and web.
- **Microsoft 365 AitM Phishing Operators (Unattributed)**: Widespread email-driven campaign using adversary-in-the-middle frameworks to hijack session tokens; focused on payroll and finance departments for BEC enablement.
- **Malicious npm Publishers (Unattributed Cluster)**: Coordinated publication of nearly 800 packages delivering cross-platform RAT/infostealer; targeting software supply chain through developer machine compromise.
- **AI-Assisted Vulnerability Researchers (PortSwigger / James Kettle)**: HTTP Terminator system discovered novel desync techniques and Apache zero-day; demonstrates offensive AI capability for vulnerability discovery.
- **Tencent Security Researchers**: Demonstrated exploit for 18-year-old Linux SCTP flaw achieving container escape; responsible disclosure to kernel maintainers.

## Source Attribution

- **Hackers breach TrueConf to trojanize client installers with backdoors**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-breach-trueconf-to-trojanize-client-installers-with-backdoors/
- **Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to Attackers**: The Hacker News - https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
- **New CSS Attacks Can Break Webmail Defenses to Steal Passwords and Tokens**: The Hacker News - https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html
- **Metabase Zero-Day Exploited in Wild Allows Admin Access Without Authentication**: The Hacker News - https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html
- **N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist**: The Hacker News - https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html
- **Progress Kemp LoadMaster Flaw Hits CISA KEV After 792 Reported Exploit Attempts**: The Hacker News - https://thehackernews.com/2026/08/progress-kemp-loadmaster-flaw-hits-cisa.html
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
