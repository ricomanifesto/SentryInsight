# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple vectors this reporting period, with zero-day vulnerabilities in widely deployed enterprise software driving high-impact breaches. The Metabase business intelligence platform faces active zero-day exploitation via a maximum-severity SQL injection flaw that grants unauthenticated administrative access, resulting in confirmed data theft at Framework and Tally. Simultaneously, the Head Mare hacktivist group has compromised TrueConf video conferencing servers to trojanize client installers in a supply chain attack, while the Progress Kemp LoadMaster vulnerability has attracted 792 exploit attempts and earned a CISA KEV listing. These incidents underscore the accelerating tempo of exploitation against authentication bypass and pre-authentication flaws in internet-facing infrastructure.

The threat landscape further reveals sophisticated social engineering and credential-theft campaigns operating at scale. ClickFix attacks have expanded to macOS with a Go-based stealer draining cryptocurrency wallets and harvesting iCloud Keychain data, while UNC6671 conducts vishing operations against financial services and private equity firms to exfiltrate SaaS data. Microsoft 365 adversary-in-the-middle phishing campaigns are hijacking accounts to target payroll and finance communications. On the supply chain front, nearly 800 malicious npm packages deliver cross-platform RATs and infostealers, and the TeamPCP threat actor has been linked to Redis compromises dating back to 2020 with subsequent supply chain activity.

Emerging attack techniques demonstrate novel bypasses of traditional defenses. CSS-based attacks are breaking webmail message boundaries across Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail to steal credentials. The NatJack attack class manipulates NAT connection state to hijack TCP sessions and spoof DNS responses. An 18-year-old Linux SCTP use-after-free enables local root escalation and container escape. AI-assisted research has uncovered new HTTP desynchronization techniques and an Apache zero-day, while malware now abuses Windows Hello for Business keys for persistent Entra ID access. These developments indicate adversaries are increasingly targeting identity, session integrity, and supply chain trust relationships.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A maximum-severity security flaw in Metabase business intelligence and data visualization software allows unauthenticated attackers to execute arbitrary SQL commands, granting full administrative access without authentication.
- **Impact**: Attackers achieve complete administrative control over Metabase instances, enabling data exfiltration, credential theft, and potential lateral movement into connected data sources. Confirmed data theft attacks have impacted Framework and Tally customer instances.
- **Status**: Actively exploited in the wild as a zero-day. Metabase has issued warnings; patching is urgently required.

### TrueConf Video Conferencing Server Vulnerabilities
- **Description**: Unpatched vulnerabilities in TrueConf video conferencing servers allow attackers to compromise the server infrastructure and replace legitimate client installers with trojanized versions containing backdoors.
- **Impact**: Supply chain compromise delivering backdoored installers to downstream clients, enabling persistent access to victim networks through trusted software distribution channels.
- **Status**: Actively exploited by the Head Mare hacktivist group. Organizations running unpatched TrueConf servers are at immediate risk.

### Progress Kemp LoadMaster Critical Flaw
- **Description**: A critical-severity vulnerability in Progress Kemp LoadMaster application delivery controllers that has attracted significant exploitation activity.
- **Impact**: Successful exploitation could allow attackers to compromise load balancer appliances, potentially enabling traffic interception, service disruption, or network pivoting.
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog after 792 reported exploit attempts. Patching is mandated for federal agencies and strongly advised for all users.

### N-able N-central RMM Vulnerability
- **Description**: A recently disclosed security flaw in the N-able N-central Remote Monitoring and Management (RMM) platform that allows attackers to reach managed systems and establish persistence.
- **Impact**: Compromise of the RMM platform grants attackers access to all managed endpoints, enabling widespread deployment of malware, data theft, and persistent footholds across customer environments.
- **Status**: Ongoing exploitation reported. N-able has released Hotfix 2 as part of its investigation; immediate application is critical for MSPs and their clients.

### WordPress Pre-Authentication Reflected XSS
- **Description**: A pre-authentication reflected cross-site scripting vulnerability in the WordPress login screen affecting every version of the CMS. Researchers demonstrated how the flaw can lead to PHP code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary JavaScript in victim browsers, potentially leading to account takeover, credential theft, and demonstrated paths to remote code execution.
- **Status**: WordPress has released a fix. All versions prior to the patched release are affected; immediate update is recommended.

### Linux Kernel SCTP Use-After-Free
- **Description**: An 18-year-old use-after-free vulnerability in the Linux kernel's SCTP (Stream Control Transmission Protocol) networking subsystem that allows local users to gain root privileges and escape containers.
- **Impact**: Local privilege escalation to root on the host system, with demonstrated container escape capability allowing breakout to the underlying host machine.
- **Status**: Vulnerability disclosed by Tencent researchers with proof-of-concept exploit. Patches are being developed for affected kernel versions.

### Apache HTTP Desynchronization Zero-Day
- **Description**: A zero-day vulnerability in Apache HTTP Server discovered through AI-assisted research (HTTP Terminator system) that enables HTTP request smuggling/desynchronization attacks.
- **Impact**: HTTP desynchronization can lead to cache poisoning, request hijacking, authentication bypass, and exposure of internal endpoints.
- **Status**: Disclosed by PortSwigger via AI-assisted research; Apache has been notified. Patch status pending.

## Affected Systems and Products

- **Metabase**: Business intelligence and data visualization platform (all unpatched versions) — Exploited for unauthenticated admin access and data theft
- **TrueConf Server**: Video conferencing server software (unpatched versions) — Compromised to trojanize client installers
- **Progress Kemp LoadMaster**: Application delivery controller / load balancer appliances — 792 exploit attempts reported, CISA KEV listed
- **N-able N-central**: Remote Monitoring and Management platform — Actively exploited for managed system access and persistence
- **WordPress**: Content management system (all versions prior to security release) — Pre-auth XSS on login screen
- **Linux Kernel**: Versions containing the SCTP use-after-free bug (18+ years of kernels) — Local root escalation and container escape
- **Apache HTTP Server**: Versions affected by HTTP desynchronization zero-day — Request smuggling and cache poisoning
- **npm Registry**: Nearly 800 malicious packages published — Cross-platform RAT and infostealer delivery (Windows, macOS, Linux)
- **Microsoft 365 / Entra ID**: Cloud identity and productivity suite — AitM phishing and Windows Hello key abuse for persistent access
- **Atlassian Rovo / Jira / Confluence**: AI assistant and collaboration platforms — Data exfiltration via prompt injection
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail — CSS-based message boundary escape attacks
- **Windows Hello for Business**: Authentication keys — Abused by malware for persistent Entra ID access
- **Claude Code / Gemini CLI**: AI coding assistants — CI workflow secret extraction via GitHub issue manipulation
- **Redis Instances**: Internet-facing Redis servers — Compromised by TeamPCP since 2020 for supply chain campaigns

## Attack Vectors and Techniques

- **Supply Chain Compromise via Server Takeover**: Attackers breach software vendor build/update infrastructure (TrueConf) to inject backdoors into legitimate client installers distributed to customers.
- **Zero-Day SQL Injection for Authentication Bypass**: Unauthenticated attackers exploit Metabase SQLi to achieve administrative access without credentials, enabling immediate data theft.
- **ClickFix Social Engineering**: Users tricked into executing malicious commands (e.g., "Fix it" buttons, fake CAPTCHAs) that deploy infostealers targeting crypto wallets, browser credentials, iCloud Keychain, and cached credentials — now cross-platform (Windows, macOS).
- **Vishing for SaaS Credential Theft**: Voice phishing (UNC6671) targeting personal phones of employees at financial services, private equity, and professional services firms to harvest SaaS authentication data.
- **Adversary-in-the-Middle (AitM) Phishing**: Phishing proxies intercept Microsoft 365 authentication sessions, hijacking accounts to access payroll and finance email communications.
- **CSS Injection Breaking Webmail Boundaries**: Malicious email content uses CSS to escape message containers and manipulate the webmail interface, stealing passwords and tokens across major providers.
- **NAT Table Manipulation (NatJack)**: Attackers manipulate NAT connection state to hijack active TCP sessions and spoof DNS responses, enabling traffic interception and redirection.
- **HTTP Request Smuggling / Desynchronization**: AI-discovered techniques desynchronize HTTP request/response parsing between front-end and back-end servers, enabling cache poisoning and request hijacking.
- **Windows Hello for Business Key Abuse**: Malware with local execution silently uses victim's hardware-bound authentication keys to obtain persistent Entra ID tokens without user interaction.
- **Prompt Injection in AI Assistants**: Attacker-controlled instructions manipulate Atlassian Rovo to access and exfiltrate Jira/Confluence data accessible to the signed-in user.
- **CI/CD Pipeline Poisoning via AI Coding Tools**: Flaws in Claude Code and Gemini CLI allow unprivileged GitHub issues to execute code on CI runners, accessing workflow secrets in Anthropic, Google, and OpenAI repositories.
- **Malicious npm Package Typosquatting/Supply Chain**: Nearly 800 packages deliver cross-platform RATs and infostealers targeting developers across Windows, macOS, and Linux.
- **Container Escape via Kernel Vulnerability**: Local SCTP use-after-free in Linux kernel exploited to break out of containers and gain root on the host.
- **Redis Exploitation for Initial Access**: TeamPCP compromises internet-facing Redis instances (since 2020) as entry point for broader supply chain campaigns.

## Threat Actor Activities

- **Head Mare**: Hacktivist group actively exploiting unpatched TrueConf servers to trojanize client installers with backdoors in a supply chain operation.
- **UNC6671**: Data extortion group linked to BlackFile ransomware operations. Conducts vishing campaigns targeting financial services, hedge funds, private equity, and professional services firms to steal SaaS data. Active in H1 2026 attack wave.
- **TeamPCP**: Cybercrime actor compromising internet-facing Redis instances since at least 2020, later leveraging access for supply chain campaigns. Long-term infrastructure compromise strategy.
- **ClickFix Operators**: Threat actors deploying ClickFix social engineering at scale, now delivering cross-platform Go-based macOS infostealer (AMOS/Atomic Stealer family) for cryptocurrency theft and credential harvesting.
- **Microsoft 365 AitM Phishing Campaign Operators**: Widespread email-driven campaign using adversary-in-the-middle infrastructure to hijack accounts and target payroll/finance communications.
- **Malicious npm Campaign Operators**: Published nearly 800 packages to npm registry in coordinated campaign delivering cross-platform RAT and infostealer payloads.

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
