# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse technology stacks, ranging from business intelligence platforms and load balancers to video conferencing systems and supply chain infrastructure. The Metabase SQL injection zero-day stands out as a maximum-severity flaw enabling unauthenticated administrative access and data theft, with confirmed breaches at Framework and Tally. Simultaneously, the Progress Kemp LoadMaster vulnerability has garnered 792 reported exploit attempts and earned a CISA Known Exploited Vulnerabilities catalog entry, signaling widespread opportunistic targeting. Threat actors are also leveraging supply chain compromises—most notably the Head Mare hacktivist group's breach of TrueConf to trojanize legitimate client installers—and a massive npm campaign distributing nearly 800 malicious packages delivering cross-platform remote access trojans and infostealers.

Attack methodologies continue to evolve beyond traditional exploitation. ClickFix social engineering campaigns now target macOS users with Go-based stealers capable of draining cryptocurrency wallets and exfiltrating Apple iCloud Keychain data. Adversary-in-the-middle phishing operations hijack Microsoft 365 sessions to harvest payroll and finance communications, while the UNC6671 extortion group employs vishing against financial services and private equity targets. Novel research demonstrates CSS-based attacks breaking webmail isolation across major providers, HTTP desynchronization techniques uncovering an Apache zero-day, and NAT manipulation enabling TCP session hijacking and DNS spoofing. An 18-year-old Linux SCTP use-after-free flaw allows local privilege escalation and container escape, demonstrating the persistent risk of legacy code.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence and data visualization software that allows unauthenticated attackers to achieve administrative access and exfiltrate customer data.
- **Impact**: Full administrative control over Metabase instances; confirmed data theft attacks against Framework and Tally customer environments.
- **Status**: Actively exploited as a zero-day; Metabase has issued warnings and patches.

### Progress Kemp LoadMaster Vulnerability
- **Description**: A critical-severity security flaw affecting Progress Kemp LoadMaster application delivery controllers and load balancers.
- **Impact**: 792 reported exploit attempts observed; enables attackers to compromise load balancing infrastructure and potentially intercept or manipulate traffic.
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog; patches available from Progress.

### TrueConf Video Conferencing Server Exploitation
- **Description**: Vulnerabilities in unpatched TrueConf video conferencing servers exploited to compromise the software supply chain and replace legitimate client installers with backdoored versions.
- **Impact**: Backdoor deployment to downstream clients; persistence and remote access to victim networks through trusted software updates.
- **Status**: Active exploitation by Head Mare hacktivist group; patches available for TrueConf servers.

### N-able N-central RMM Exploitation
- **Description**: A recently disclosed security flaw in N-able's N-central Remote Monitoring and Management (RMM) platform under active exploitation.
- **Impact**: Attackers reaching managed systems and establishing persistence across MSP customer environments.
- **Status**: Ongoing exploitation; N-able has released Hotfix 2 as part of continued investigation and remediation.

### Atlassian Rovo Data Exfiltration Vulnerability
- **Description**: A flaw in Atlassian's Rovo AI assistant that allows attacker-controlled instructions to collect Jira and Confluence data accessible to a signed-in user and exfiltrate it to an external server.
- **Impact**: Unauthorized access to sensitive project management and wiki data; potential exposure of credentials, source code references, and internal communications.
- **Status**: Discovered by two security firms; mitigation guidance available from Atlassian.

### WordPress Pre-Authentication Reflected XSS
- **Description**: A reflected cross-site scripting flaw in the WordPress login screen affecting all versions, which researchers demonstrated can be chained to achieve PHP code execution.
- **Impact**: Pre-authentication compromise pathway; potential full server takeover via exploit chain.
- **Status**: Patched in latest WordPress release; immediate updating recommended.

### Linux SCTP Use-After-Free Vulnerability
- **Description**: An 18-year-old use-after-free bug in Linux's SCTP networking code that allows local users to gain root privileges and escape containers to access the underlying host.
- **Impact**: Local privilege escalation to root; container escape breaking isolation boundaries; affects containerized workloads and multi-tenant environments.
- **Status**: Demonstrated by Tencent researchers; patches available in upstream Linux kernel.

## Affected Systems and Products

- **Metabase Business Intelligence Platform**: All unpatched versions; confirmed impact on Framework and Tally customer instances.
- **Progress Kemp LoadMaster**: Affected LoadMaster appliance versions; critical infrastructure component for application delivery.
- **TrueConf Video Conferencing Server**: Unpatched server versions; client installers distributed to end users across Windows, macOS, and Linux.
- **N-able N-central RMM**: N-central management platform versions prior to Hotfix 2; impacts MSPs and their managed customer endpoints.
- **Atlassian Rovo, Jira, and Confluence**: Cloud and Data Center deployments with Rovo enabled; signed-in user data accessible to the assistant.
- **WordPress Content Management System**: Every version prior to the security release; login screen component universally exposed.
- **Linux Kernel**: Versions containing the vulnerable SCTP implementation; container runtimes and hosts using affected kernels.
- **npm Registry Packages**: Nearly 800 identified malicious packages targeting Windows, macOS, and Linux developers and build pipelines.
- **Microsoft 365 / Entra ID**: Tenants targeted by adversary-in-the-middle phishing; Windows Hello for Business keys exploitable for persistent access.
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail vulnerable to CSS-based boundary escape attacks.
- **Apache HTTP Server**: Versions affected by the newly discovered HTTP desynchronization zero-day.
- **Network Infrastructure**: NAT devices and stateful firewalls susceptible to NatJack TCP hijacking and DNS spoofing.

## Attack Vectors and Techniques

- **Supply Chain Compromise via Software Vendor Breach**: Attackers infiltrate vendor build or distribution infrastructure (TrueConf) to inject malicious code into legitimate signed installers, achieving trusted distribution to downstream customers.
- **SQL Injection for Unauthenticated Admin Access**: Direct exploitation of Metabase SQLi flaw without authentication to escalate to administrative privileges and exfiltrate databases.
- **Load Balancer Exploitation**: Targeting internet-facing Kemp LoadMaster appliances for infrastructure compromise and traffic manipulation.
- **RMM Platform Abuse**: Exploiting N-central vulnerabilities to pivot from management plane to managed endpoints, establishing broad persistence across MSP client bases.
- **AI Assistant Prompt Injection**: Crafting malicious instructions that cause Atlassian Rovo to access and exfiltrate user-authorized Jira/Confluence data.
- **Cross-Site Scripting Chains**: Leveraging reflected XSS in WordPress login as initial vector, chaining to achieve remote code execution.
- **Container Escape via Kernel Flaw**: Exploiting SCTP use-after-free from within container to break isolation and gain host root access.
- **Malicious Package Publishing**: Flooding npm registry with obfuscated packages delivering cross-platform RATs and infostealers to developer machines and CI/CD pipelines.
- **ClickFix Social Engineering**: Tricking users into executing malicious commands via fake verification prompts, delivering Go-based macOS stealers targeting crypto wallets and keychains.
- **Adversary-in-the-Middle Phishing**: Proxying Microsoft 365 authentication to capture session tokens and bypass MFA, targeting payroll and finance email access.
- **Vishing for SaaS Credential Theft**: Voice-based social engineering targeting financial services employees to obtain SaaS platform access.
- **CSS-Based Webmail Boundary Escape**: Crafting email content that breaks out of message sandbox to manipulate webmail DOM and steal credentials/tokens.
- **HTTP Request Smuggling / Desynchronization**: Novel desync techniques discovered via AI-assisted research, enabling request smuggling and cache poisoning against Apache.
- **NAT State Manipulation (NatJack)**: Exploiting NAT connection tracking tables to hijack established TCP sessions and inject spoofed DNS responses.
- **Windows Hello for Business Key Abuse**: Malware leveraging victim's authenticated session to silently use hardware-bound keys for persistent Entra ID authentication.
- **CI/CD Pipeline Injection via GitHub Issues**: Exploiting Claude Code and Gemini CLI flaws to execute unauthorized code on CI runners through unprivileged GitHub issue creation.
- **Redis Server Compromise for Supply Chain**: Long-term targeting of exposed Redis instances to establish footholds for later supply chain attacks (TeamPCP).

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Actively exploiting unpatched TrueConf servers to trojanize client installers with backdoors; politically motivated supply chain compromise.
- **UNC6671 (Data Extortion Group)**: Conducting vishing campaigns against financial services, private equity, and professional services; linked to BlackFile threat activity; steals SaaS data for extortion.
- **TeamPCP (Cybercrime Actor)**: Operating since at least 2020; compromising internet-facing Redis infrastructure; linked to later supply chain campaign activity.
- **ClickFix Operators (Unattributed)**: Running widespread ClickFix social engineering campaigns delivering macOS infostealers (Go-based) for cryptocurrency theft and credential harvesting.
- **AitM Phishing Campaign Operators (Unattributed)**: Large-scale adversary-in-the-middle phishing targeting Microsoft 365 accounts to harvest payroll and finance department emails.
- **Metabase Zero-Day Exploiters (Unattributed)**: Conducting data theft attacks against Framework and Tally via Metabase SQLi; operational details suggest financially motivated targeting.
- **Kemp LoadMaster Exploiters (Unattributed)**: High-volume exploitation attempts (792+ reported) indicating opportunistic scanning and compromise of exposed appliances.
- **npm Supply Chain Campaign Operators (Unattributed)**: Publishing nearly 800 malicious packages in coordinated campaign delivering cross-platform malware to developer ecosystems.

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
