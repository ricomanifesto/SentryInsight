# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited in the wild, with zero-day flaws in widely deployed software enabling unauthorized administrative access, data theft, and persistent compromise. The Metabase business intelligence platform faces a maximum-severity SQL injection zero-day that has already been weaponized against customer instances including Framework and Tally, while Progress Kemp LoadMaster appliances have seen 792 reported exploit attempts, prompting CISA to add the flaw to its Known Exploited Vulnerabilities catalog. Simultaneously, supply chain attacks continue to escalate, with the Head Mare hacktivist group trojanizing TrueConf video conferencing installers and a cluster of nearly 800 malicious npm packages delivering cross-platform remote access trojans and infostealers across Windows, macOS, and Linux environments.

Threat actors are diversifying initial access techniques beyond traditional phishing, leveraging adversary-in-the-middle (AitM) frameworks to hijack Microsoft 365 sessions, vishing campaigns targeting personal phones to breach SaaS environments, and novel ClickFix social engineering lures deploying macOS stealers that drain cryptocurrency wallets and exfiltrate iCloud Keychain data. Research into CSS-based webmail exploits demonstrates how email content can escape message boundaries to steal credentials across major providers including Outlook, Gmail, and Proton Mail, while the NatJack attack class manipulates NAT connection state to hijack TCP sessions and spoof DNS responses. These developments indicate attackers are rapidly operationalizing both new vulnerability classes and sophisticated identity-focused techniques.

Long-standing vulnerabilities remain potent weapons: an 18-year-old Linux SCTP use-after-free flaw enables local privilege escalation and container escape, while the TeamPCP threat actor has maintained persistent access to internet-facing Redis infrastructure since 2020 before pivoting to supply chain compromise. AI-assisted research tooling is accelerating vulnerability discovery, with automated systems uncovering novel HTTP desynchronization techniques and an Apache zero-day. Organizations face a convergence of zero-day exploitation, identity-based attacks, and software supply chain compromise that demands immediate patching of known exploited vulnerabilities and hardened authentication controls.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence and data visualization software that allows unauthenticated attackers to achieve administrative access. The flaw resides in the application's database query handling and can be exploited without any prior authentication.
- **Impact**: Attackers gain full administrative control over Metabase instances, enabling complete data exfiltration, manipulation of business intelligence dashboards, and potential lateral movement into connected data sources. Confirmed victims include Framework and Tally, with customer data stolen in targeted attacks.
- **Status**: Actively exploited as a zero-day. Metabase has issued warnings and patches. Organizations running Metabase should apply updates immediately and audit for signs of compromise.
- **CVE ID**: Not explicitly provided in source articles

### Progress Kemp LoadMaster Vulnerability
- **Description**: A critical-severity security flaw affecting Progress Kemp LoadMaster load balancing appliances. The vulnerability has attracted significant attacker attention with 792 reported exploit attempts observed.
- **Impact**: Successful exploitation likely allows unauthenticated remote code execution or administrative bypass on load balancer appliances, providing attackers with a strategic network foothold to intercept, manipulate, or redirect traffic.
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog, mandating federal agency patching. Progress has released fixes. Active exploitation ongoing with high attempt volume.
- **CVE ID**: Not explicitly provided in source articles

### N-able N-central RMM Vulnerability
- **Description**: A recently disclosed security flaw in N-able's N-central Remote Monitoring and Management (RMM) platform that allows attackers to reach managed systems and establish persistence.
- **Impact**: Compromise of the RMM platform grants attackers administrative control over all managed endpoints, enabling mass deployment of malware, data exfiltration, and persistent access across customer environments.
- **Status**: N-able has released Hotfix 2 as part of ongoing investigation into active exploitation. Attackers have successfully reached managed systems and established persistence.
- **CVE ID**: Not explicitly provided in source articles

### TrueConf Video Conferencing Server Vulnerabilities
- **Description**: Vulnerabilities in unpatched TrueConf video conferencing servers exploited by the Head Mare hacktivist group to replace legitimate client installers with trojanized versions containing backdoors.
- **Impact**: Supply chain compromise delivering backdoored installers to TrueConf users. Attackers gain persistent remote access to systems installing the malicious client software.
- **Status**: Actively exploited by Head Mare group. TrueConf users should verify installer integrity and patch servers immediately.
- **CVE ID**: Not explicitly provided in source articles

### WordPress Pre-Authentication Reflected XSS
- **Description**: A pre-authentication reflected cross-site scripting flaw in the WordPress login screen affecting every version of the content management system. Researcher pwn.ai demonstrated how the flaw can be chained to achieve PHP code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary JavaScript in victim browsers, potentially leading to account takeover, and in demonstrated chains, full PHP code execution on the server.
- **Status**: WordPress has released a fix. All versions affected. Immediate patching recommended due to pre-auth nature and code execution potential.
- **CVE ID**: Not explicitly provided in source articles

### Linux Kernel SCTP Use-After-Free
- **Description**: An 18-year-old use-after-free vulnerability in Linux's SCTP (Stream Control Transmission Protocol) networking code. Tencent researchers demonstrated exploitation achieving full root privileges on the host and container escape.
- **Impact**: Local users can escalate to root privileges and break out of container isolation to compromise the underlying host system, affecting containerized environments and multi-tenant systems.
- **Status**: Long-standing flaw with recent exploitation demonstration. Patches likely available in updated kernel versions.
- **CVE ID**: Not explicitly provided in source articles

### Apache HTTP Desynchronization Zero-Day
- **Description**: An Apache zero-day vulnerability discovered through AI-assisted research using the HTTP Terminator system, which explored 30,000 candidates to generate and prove novel HTTP desynchronization techniques.
- **Impact**: HTTP request smuggling/desynchronization attacks can bypass security controls, poison caches, and compromise backend systems through crafted request sequences.
- **Status**: Zero-day discovered via automated AI research. Apache patches likely forthcoming.
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **Metabase Business Intelligence Platform**: All versions prior to patched release; business intelligence and data visualization software used by Framework, Tally, and other organizations
- **Progress Kemp LoadMaster**: Load balancing appliances; critical infrastructure component for traffic management
- **N-able N-central**: Remote Monitoring and Management (RMM) platform; used by MSPs and IT departments for endpoint management
- **TrueConf Video Conferencing Server**: On-premises video conferencing servers; client installers distributed to end users
- **WordPress CMS**: All versions affected; pre-authentication reflected XSS in login screen
- **Linux Kernel**: Versions containing vulnerable SCTP implementation; 18-year-old flaw affecting containerized and multi-tenant environments
- **Apache HTTP Server**: Versions affected by HTTP desynchronization zero-day discovered via AI-assisted research
- **npm Registry**: Nearly 800 malicious packages published targeting Windows, macOS, and Linux developers
- **Microsoft 365 / Entra ID**: Cloud identity and productivity platform targeted via AitM phishing and Windows Hello for Business key abuse
- **Atlassian Rovo / Jira / Confluence**: AI assistant and collaboration platforms vulnerable to data exfiltration via prompt injection
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail affected by CSS-based email content escape attacks
- **Windows Hello for Business / Entra ID**: Authentication keys usable by malware for persistent cloud access
- **Anthropic Claude Code / Google Gemini CLI**: AI coding assistants with CI/CD integration vulnerabilities allowing secret exfiltration via GitHub issues

## Attack Vectors and Techniques

- **SQL Injection (Zero-Day)**: Unauthenticated database query manipulation in Metabase enabling administrative bypass and data theft
- **Supply Chain Compromise / Trojanized Installers**: Head Mare group replacing legitimate TrueConf client installers with backdoored versions
- **Malicious Package Publication**: Nearly 800 malicious npm packages delivering cross-platform RAT and infostealer malware
- **Adversary-in-the-Middle (AitM) Phishing**: Widespread campaign hijacking Microsoft 365 sessions to access payroll and finance emails
- **Vishing / Voice Phishing**: UNC6671 targeting personal phones to steal SaaS credentials and data
- **ClickFix Social Engineering**: Deceptive verification prompts delivering macOS Go-based stealer malware (crypto theft, credential exfiltration, iCloud Keychain access)
- **CSS-Based Webmail Escape**: Email content escaping message boundaries to interfere with webmail interface and steal credentials/tokens across major providers
- **NAT Manipulation (NatJack)**: Manipulating NAT connection state tables to hijack active TCP sessions and spoof DNS responses
- **HTTP Request Smuggling / Desynchronization**: Novel techniques discovered via AI-assisted research affecting Apache and other HTTP implementations
- **Windows Hello for Business Key Abuse**: Malware leveraging victim's hardware-bound keys for persistent Entra ID authentication
- **Prompt Injection / AI Assistant Manipulation**: Attacker-controlled instructions causing Atlassian Rovo to exfiltrate Jira/Confluence data
- **GitHub Issue CI/CD Abuse**: Low-privilege GitHub issues triggering code execution on CI runners to access workflow secrets (Claude Code, Gemini CLI)
- **Redis Server Compromise**: TeamPCP exploiting internet-facing Redis instances since 2020 for initial access and later supply chain campaigns
- **Container Escape via Kernel Flaw**: Linux SCTP use-after-free enabling breakout from container to host root access
- **Clipboard Hijacking**: Banking malware campaign manipulating clipboard content to redirect cryptocurrency transactions
- **Browser Manipulation / Business Email Compromise**: Compromised inboxes used with browser manipulation for financial fraud

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Exploiting unpatched TrueConf servers to trojanize client installers with backdoors; supply chain targeting of video conferencing users
- **UNC6671 (Data Extortion Group)**: Vishing campaigns targeting financial services, private equity, and professional services; leveraging personal phone compromise to access SaaS data
- **TeamPCP (Cybercrime Actor)**: Active since 2020 compromising internet-facing Redis infrastructure; later pivoted to supply chain campaign activity
- **ClickFix Operators (Unknown Attribution)**: Deploying Go-based macOS infostealers via ClickFix social engineering; targeting cryptocurrency assets, browser credentials, Apple Keychain data
- **Microsoft 365 AitM Phishing Actors (Unknown Attribution)**: Widespread email-driven campaign using adversary-in-the-middle techniques to hijack accounts and harvest payroll/finance emails
- **Malicious npm Package Publishers (Unknown Attribution)**: Cluster of nearly 800 packages delivering cross-platform RAT and infostealer malware across Windows, macOS, Linux
- **Metabase Zero-Day Exploiters (Unknown Attribution)**: Targeted data theft attacks against Framework and Tally customer instances; critical SQLi exploited as zero-day
- **Progress Kemp LoadMaster Attackers (Unknown Attribution)**: 792 reported exploit attempts against critical load balancer flaw; active scanning and exploitation
- **N-able N-central Intruders (Unknown Attribution)**: Reached managed systems and established persistence via RMM platform vulnerability; ongoing investigation

## Source Attribution

- **OpenAI's Next AI Model Astra Shows Cyber Performance Strong Enough to Trigger Pause**: The Hacker News - https://thehackernews.com/2026/08/openais-next-ai-model-astra-shows-cyber.html
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
