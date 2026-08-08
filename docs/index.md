# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are being actively exploited in the wild across diverse technology stacks. Metabase business intelligence software faces a maximum-severity SQL injection zero-day enabling unauthenticated administrative access and data theft, with confirmed breaches at Framework and Tally. Progress Kemp LoadMaster appliances have seen 792 exploit attempts, prompting CISA to add the flaw to its Known Exploited Vulnerabilities catalog. The Head Mare hacktivist group has compromised TrueConf video conferencing servers to trojanize client installers with backdoors, while N-able's N-central RMM platform undergoes active exploitation requiring emergency hotfixes.

Supply chain and social engineering campaigns are escalating in sophistication. Nearly 800 malicious npm packages deliver cross-platform remote access trojans and infostealers targeting Windows, macOS, and Linux systems. ClickFix-style attacks now deploy Go-based macOS stealers capable of draining cryptocurrency wallets, harvesting browser credentials, and accessing Apple iCloud Keychain data. The UNC6671 extortion group—linked to BlackFile ransomware—conducts vishing campaigns against financial services, private equity, and hedge funds to steal SaaS data. Microsoft 365 adversary-in-the-middle phishing campaigns hijack accounts to harvest payroll and finance emails at scale.

Novel attack techniques are expanding the exploitation landscape. CSS-based attacks break webmail defenses across Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail to exfiltrate passwords and tokens. The NatJack attack class manipulates NAT tables to hijack TCP sessions and spoof DNS responses. An 18-year-old Linux SCTP use-after-free flaw enables local root escalation and container escapes. AI-assisted research uncovered new HTTP desynchronization techniques and an Apache zero-day, while Windows Hello for Business keys can be abused for persistent Entra ID access. GitHub Issues in AI coding agent repositories (Claude Code, Gemini CLI) can reach CI workflow secrets without repository privileges.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A maximum-severity SQL injection vulnerability in Metabase business intelligence and data visualization software allows unauthenticated attackers to achieve administrative access and extract sensitive data.
- **Impact**: Full administrative control of Metabase instances, unauthorized access to connected databases, and exfiltration of customer data. Confirmed breaches at Framework and Tally resulting in data theft.
- **Status**: Actively exploited as a zero-day. Metabase has issued warnings; patches or mitigations should be applied immediately.
- **CVE ID**: Not explicitly provided in source articles

### Progress Kemp LoadMaster Critical Flaw
- **Description**: A critical-severity vulnerability affecting Progress Kemp LoadMaster load balancing appliances.
- **Impact**: Remote exploitation leading to potential system compromise. CISA has recorded 792 exploit attempts against this vulnerability.
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog, mandating federal agency remediation. Patches available from Progress.
- **CVE ID**: Not explicitly provided in source articles

### TrueConf Video Conferencing Server Vulnerabilities
- **Description**: Unpatched vulnerabilities in TrueConf video conferencing servers allow attackers to compromise the server infrastructure and replace legitimate client installers with trojanized versions containing backdoors.
- **Impact**: Supply chain compromise delivering backdoors to any user downloading client installers. Persistent access to victim networks through malicious software updates.
- **Status**: Actively exploited by Head Mare hacktivist group. TrueConf users should verify installer integrity and patch servers immediately.
- **CVE ID**: Not explicitly provided in source articles

### N-able N-central RMM Exploitation
- **Description**: A recently disclosed security flaw in N-able's N-central Remote Monitoring and Management (RMM) platform is being actively exploited to reach managed systems and establish persistence.
- **Impact**: Attackers can access all systems managed through compromised N-central instances, potentially spanning multiple customer environments. Persistence mechanisms survive reboots and updates.
- **Status**: Ongoing exploitation. N-able has released Hotfix 2 as part of continued investigation and remediation.
- **CVE ID**: Not explicitly provided in source articles

### Atlassian Rovo Data Exfiltration
- **Description**: Attacker-controlled instructions can manipulate Atlassian's Rovo AI assistant to collect Jira and Confluence data accessible to a signed-in user and send it to an external server.
- **Impact**: Unauthorized access to sensitive project data, credentials, and internal documentation stored in Jira and Confluence. Exploits the AI assistant's legitimate data access capabilities.
- **Status**: Discovered by two security firms. Atlassian has been notified; mitigation guidance pending.
- **CVE ID**: Not explicitly provided in source articles

### WordPress Pre-Authentication XSS
- **Description**: A reflected cross-site scripting (XSS) flaw in the WordPress login screen affects every version of the CMS. Research by pwn.ai demonstrates the vulnerability can be chained to achieve PHP code execution.
- **Impact**: Pre-authentication compromise of WordPress sites, leading to full server takeover through PHP code execution. Affects all WordPress installations.
- **Status**: WordPress has released a fix. Immediate patching recommended due to pre-auth nature and code execution potential.
- **CVE ID**: Not explicitly provided in source articles

### Linux SCTP Use-After-Free (18-Year-Old Flaw)
- **Description**: A use-after-free bug in Linux's SCTP (Stream Control Transmission Protocol) networking code that has existed for 18 years. Tencent researchers demonstrated exploitation for local root privilege escalation and container escape.
- **Impact**: Local users can gain root access on the host and escape containers to compromise the underlying host system. Affects containerized environments and multi-tenant systems.
- **Status**: Vulnerability disclosed with proof-of-concept exploit. Kernel patches expected.
- **CVE ID**: Not explicitly provided in source articles

### Apache HTTP Desynchronization Zero-Day
- **Description**: AI-assisted research (HTTP Terminator system) discovered novel HTTP request smuggling/desynchronization techniques and an Apache zero-day vulnerability.
- **Impact**: HTTP request smuggling leading to cache poisoning, credential theft, and bypass of security controls. Apache zero-day enables direct server exploitation.
- **Status**: Disclosed by PortSwigger/James Kettle. Apache patches pending.
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **Metabase**: Business intelligence and data visualization software (all unpatched versions). Confirmed impact on Framework and Tally customer instances.
- **Progress Kemp LoadMaster**: Load balancing appliances (vulnerable firmware versions). 792 confirmed exploit attempts observed.
- **TrueConf**: Video conferencing server software (unpatched versions). Client installers for Windows, macOS, and Linux trojanized.
- **N-able N-central**: Remote Monitoring and Management platform (versions prior to Hotfix 2). Managed customer systems at risk.
- **Atlassian Rovo / Jira / Confluence**: Cloud and Data Center deployments where Rovo AI assistant is enabled.
- **WordPress**: All versions prior to security release. Pre-authentication attack surface on login screen.
- **Linux Kernel**: All versions with SCTP support enabled (18-year vulnerability window). Container runtimes (Docker, containerd, Kubernetes) on vulnerable kernels.
- **Apache HTTP Server**: Versions affected by the newly discovered desynchronization zero-day.
- **npm Registry**: Nearly 800 malicious packages published, affecting any project installing compromised dependencies across Windows, macOS, and Linux.
- **Microsoft 365 / Entra ID**: Accounts targeted by AitM phishing; Windows Hello for Business keys abusable for persistent access.
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail vulnerable to CSS-based boundary escape attacks.
- **NAT Devices**: Routers, firewalls, and gateways with vulnerable NAT table handling (NatJack attack class).
- **AI Coding Agents**: Claude Code (Anthropic), Gemini CLI (Google), and OpenAI coding agent repositories with vulnerable CI workflow configurations.

## Attack Vectors and Techniques

- **SQL Injection (Zero-Day)**: Unauthenticated database query manipulation in Metabase leading to admin bypass and data exfiltration.
- **Supply Chain Compromise / Trojanized Installers**: Legitimate software build/distribution infrastructure compromised to deliver backdoored client installers (TrueConf).
- **Malicious Package Publishing**: Typosquatting and dependency confusion via ~800 npm packages delivering cross-platform RATs and infostealers.
- **ClickFix Social Engineering**: Fake CAPTCHA/verification pages tricking users into executing malicious PowerShell/terminal commands, now targeting macOS with Go-based stealers.
- **Adversary-in-the-Middle (AitM) Phishing**: Proxy-based phishing capturing MFA tokens and session cookies for Microsoft 365 account takeover.
- **Vishing (Voice Phishing)**: UNC6671 uses phone-based social engineering targeting personal phones to steal SaaS credentials and data.
- **CSS Injection / Boundary Escape**: Malicious email content escapes message boundaries to interfere with webmail DOM, stealing passwords and tokens across major providers.
- **NAT Table Manipulation (NatJack)**: Manipulating NAT connection state to hijack active TCP sessions and spoof DNS responses.
- **HTTP Request Smuggling / Desynchronization**: Novel AI-discovered techniques for request smuggling enabling cache poisoning and credential theft.
- **Windows Hello for Business Key Abuse**: Malware leverages hardware-bound keys in signed-in sessions for persistent Entra ID authentication without user interaction.
- **GitHub Issue CI Injection**: Low-privilege GitHub Issues trigger CI workflow execution exposing secrets in AI coding agent repositories.
- **Container Escape via Kernel Flaw**: SCTP use-after-free exploited for local root and container breakout to host system.
- **AI Assistant Prompt Injection**: Attacker-controlled instructions exfiltrate data accessible to Atlassian Rovo AI assistant.
- **Browser Manipulation / Clipboard Hijacking**: Compromised business inboxes combined with browser manipulation for banking malware delivery and payment hijacking.

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Exploiting unpatched TrueConf servers to trojanize client installers with backdoors. Politically motivated targeting of video conferencing infrastructure.
- **UNC6671 (Data Extortion Group / BlackFile-linked)**: Conducting vishing campaigns against financial services, private equity, hedge funds, and professional services. Uses voice calls to personal phones to steal SaaS credentials and extort data. Linked to BlackFile ransomware operations.
- **TeamPCP (Cybercrime Actor)**: Active since at least 2020 compromising internet-facing Redis instances. Evolved into supply chain campaigns. Long-term infrastructure compromise and monetization.
- **ClickFix Operators (Unknown Attribution)**: Deploying Go-based macOS infostealers (capable of crypto wallet drainage, browser credential theft, iCloud Keychain access) via social engineering. Cross-platform campaign infrastructure.
- **Microsoft 365 AitM Phishing Campaign (Unknown Attribution)**: Widespread email-driven campaign targeting payroll and finance emails. Uses adversary-in-the-middle infrastructure to bypass MFA.
- **Malicious npm Package Campaign (Unknown Attribution)**: Cluster of ~800 packages published to npm registry delivering cross-platform RATs and infostealers. Active supply chain operation.
- **AI Research Threat Actors (Theoretical/Research)**: HTTP Terminator AI system demonstrating automated discovery of HTTP desync techniques and Apache zero-day. Represents emerging AI-assisted vulnerability discovery capability.

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
