# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively targeting enterprise infrastructure, collaboration platforms, and developer ecosystems. The Head Mare hacktivist group has compromised TrueConf video conferencing servers to distribute trojanized client installers, while a maximum-severity Metabase zero-day vulnerability is being exploited in the wild to achieve unauthenticated administrative access and steal customer data from organizations including Framework and Tally. Simultaneously, the Progress Kemp LoadMaster flaw has been added to CISA's Known Exploited Vulnerabilities catalog after nearly 800 exploit attempts, and N-able's N-central RMM platform faces ongoing exploitation requiring emergency hotfixes.

Attackers are increasingly leveraging legitimate platform features and supply chain vectors. A novel CSS-based attack technique breaks webmail defenses across major providers including Outlook, Gmail, and Proton Mail to steal credentials and tokens. Nearly 800 malicious npm packages deliver cross-platform remote access trojans and infostealers targeting Windows, macOS, and Linux systems. The UNC6671 extortion group—linked to BlackFile ransomware—conducts vishing campaigns against financial services and private equity firms, while ClickFix social engineering attacks deploy Go-based macOS stealers that drain cryptocurrency wallets and harvest Apple Keychain data.

Research reveals expanding attack surfaces in AI-assisted development tools and authentication systems. GitHub Issues in Anthropic's Claude Code and Google's Gemini CLI repositories can trigger CI workflow secret exfiltration without repository privileges. Malware with local Windows session access can abuse Windows Hello for Business keys to maintain persistent Entra ID authentication. An AI-assisted fuzzing system discovered novel HTTP desynchronization techniques and an Apache zero-day, while an 18-year-old Linux SCTP flaw enables container escape to host root. WordPress has patched a pre-authentication XSS flaw affecting all versions that researchers demonstrated could lead to PHP code execution.

## Active Exploitation Details

### TrueConf Video Conferencing Server Compromise
- **Description**: Hackers are exploiting vulnerabilities in unpatched TrueConf video conferencing servers to gain access and replace legitimate client installers with malicious versions containing backdoors
- **Impact**: Attackers achieve persistent access to victim networks through trojanized software updates, enabling lateral movement and data exfiltration
- **Status**: Active exploitation by Head Mare hacktivist group; organizations running unpatched TrueConf servers are at immediate risk

### Metabase Zero-Day Authentication Bypass
- **Description**: A maximum-severity security flaw in Metabase business intelligence and data visualization software allows unauthenticated attackers to gain administrative access
- **Impact**: Full administrative control over Metabase instances, enabling data theft from customer databases; confirmed breaches at Framework and Tally
- **Status**: Actively exploited in the wild as a zero-day; emergency patching required

### Metabase SQL Injection Data Theft
- **Description**: Critical SQL injection vulnerability in Metabase exploited in zero-day attacks targeting customer instances for data theft
- **Impact**: Unauthorized access to and exfiltration of sensitive customer data stored in Metabase-backed databases
- **Status**: Active exploitation confirmed against Framework and Tally; patch deployment urgent

### Progress Kemp LoadMaster Critical Flaw
- **Description**: Critical-severity vulnerability in Progress Kemp LoadMaster application delivery controllers
- **Impact**: 792 reported exploit attempts recorded; allows attackers to compromise load balancer infrastructure
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog; federal agencies required to remediate, all organizations should patch immediately

### N-able N-central RMM Exploitation
- **Description**: Recently disclosed security flaw in N-able N-central Remote Monitoring and Management platform under active exploitation
- **Impact**: Attackers reach managed systems and establish persistence across MSP customer environments
- **Status**: Hotfix 2 released as part of ongoing investigation; active exploitation continuing

### WordPress Pre-Authentication XSS
- **Description**: Reflected cross-site scripting flaw in WordPress login screen affecting every version of the CMS
- **Impact**: Pre-authentication attack vector; researchers demonstrated chaining to achieve PHP code execution
- **Status**: Patch available; immediate update recommended for all WordPress installations

## Affected Systems and Products

- **TrueConf Video Conferencing Server**: Unpatched server versions vulnerable to compromise and installer trojanization; affects client installer distribution mechanism
- **Metabase Business Intelligence Platform**: All unpatched versions vulnerable to authentication bypass and SQL injection; impacts Framework, Tally, and other Metabase deployments
- **Progress Kemp LoadMaster**: Application delivery controller appliances running vulnerable firmware versions; 792 exploit attempts observed
- **N-able N-central**: RMM platform versions prior to Hotfix 2; affects MSP infrastructure and downstream managed customer systems
- **WordPress CMS**: Every version prior to security release; pre-authentication XSS in login screen (wp-login.php)
- **Major Webmail Providers**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail vulnerable to CSS-based message boundary escape attacks
- **npm Registry Ecosystem**: ~800 malicious packages published targeting Windows, macOS, and Linux development environments
- **Microsoft 365 / Entra ID**: Accounts targeted via AitM phishing; Windows Hello for Business keys exploitable for persistent access
- **Linux Kernel**: SCTP networking code with 18-year-old use-after-free flaw enabling local root and container escape
- **Apache HTTP Server**: Zero-day discovered via AI-assisted fuzzing; HTTP desynchronization vulnerabilities
- **Anthropic Claude Code & Google Gemini CLI**: CI/CD workflows vulnerable to GitHub Issue-triggered secret exfiltration
- **Redis Instances**: Internet-facing Redis servers compromised by TeamPCP since 2020; supply chain campaign infrastructure

## Attack Vectors and Techniques

- **Software Supply Chain Compromise**: Legitimate TrueConf client installers replaced with backdoored versions distributed through official update channels
- **CSS Injection / Message Boundary Escape**: Email content escapes message container to manipulate webmail DOM, stealing credentials and tokens across Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail
- **Adversary-in-the-Middle (AitM) Phishing**: Widespread campaign using reverse proxy techniques to hijack Microsoft 365 sessions, targeting payroll and finance email access
- **ClickFix Social Engineering**: Fake browser error prompts trick users into executing malicious PowerShell commands delivering Go-based macOS infostealer (crypto wallets, Keychain, browser passwords)
- **Vishing (Voice Phishing)**: UNC6671 targets personal phones of financial services employees to steal SaaS credentials and access data
- **Malicious npm Package Campaign**: ~800 typosquatting/dependency confusion packages delivering cross-platform RAT and infostealer payloads
- **Windows Hello for Business Key Abuse**: Malware in signed-in session silently uses hardware-bound keys for persistent Entra ID authentication without user interaction
- **GitHub Issue CI Injection**: Unprivileged GitHub Issues trigger CI workflow execution in Anthropic, Google, and OpenAI coding agent repositories, exfiltrating secrets
- **HTTP Request Smuggling / Desynchronization**: AI-discovered novel desync techniques targeting Apache and other HTTP parsers for request smuggling
- **Linux SCTP Use-After-Free**: Local privilege escalation to root and container escape via crafted SCTP packets; 18-year-old kernel flaw
- **NAT Table Manipulation (NatJack)**: Manipulation of NAT connection state to hijack active TCP sessions and spoof DNS responses
- **Redis Exploitation**: TeamPCP compromises internet-facing Redis instances for initial access and supply chain campaign infrastructure
- **Social Engineering**: Levi Strauss breach via social engineering of three employees; compromised business inboxes used for banking malware distribution

## Threat Actor Activities

- **Head Mare**: Hacktivist group exploiting TrueConf server vulnerabilities to trojanize client installers with backdoors; supply chain compromise for persistent access
- **UNC6671 / BlackFile-linked Extortion Group**: Data extortion group conducting vishing campaigns against financial services, private equity, and professional services; targets personal phones to access SaaS data; linked to hedge fund cyberattacks
- **TeamPCP**: Cybercrime actor active since at least 2020 compromising internet-facing Redis infrastructure; evolved into supply chain campaign operations
- **ClickFix Operators**: Threat actors deploying ClickFix-style social engineering to deliver cross-platform malware; macOS variant steals cryptocurrency, Keychain data, browser credentials
- **AitM Phishing Campaign Operators**: Widespread email-driven campaign using adversary-in-the-middle techniques to hijack Microsoft 365 accounts; focuses on payroll and finance email collection

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
