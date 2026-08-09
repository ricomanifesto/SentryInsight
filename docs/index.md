# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are under active exploitation across diverse technology stacks, with Metabase business intelligence platforms and Progress Kemp LoadMaster appliances facing confirmed in-the-wild attacks. The Metabase SQL injection flaw enables unauthenticated administrative access and has already facilitated data theft at Framework and Tally, while the LoadMaster vulnerability has generated nearly 800 exploit attempts and earned a spot on CISA's Known Exploited Vulnerabilities catalog. Simultaneously, supply chain compromise campaigns are escalating: the Head Mare hacktivist group trojanized TrueConf video conferencing installers after breaching unpatched servers, and a cluster of nearly 800 malicious npm packages delivered cross-platform remote access trojans and infostealers to developer environments.

Threat actors are diversifying initial access techniques beyond traditional vulnerability exploitation. ClickFix social engineering campaigns now target macOS users with Go-based stealers draining cryptocurrency wallets and harvesting browser credentials, while UNC6671 conducts vishing operations against financial services and private equity firms to steal SaaS credentials. Adversary-in-the-middle phishing at scale continues to hijack Microsoft 365 accounts for payroll and finance email collection. Novel attack research reveals CSS-based webmail escape techniques affecting Outlook, Gmail, Proton Mail, and others, alongside NAT manipulation attacks (NatJack) that hijack TCP sessions and spoof DNS responses.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence and data visualization software that allows unauthenticated attackers to achieve administrative access. The flaw is exploitable without any prior authentication and has been weaponized as a zero-day.
- **Impact**: Attackers gain full administrative control over Metabase instances, enabling data theft, database enumeration, and potential lateral movement into connected data sources. Confirmed breaches at Framework and Tally resulted in customer data exfiltration.
- **Status**: Actively exploited in the wild as a zero-day. Metabase has issued warnings; patching is urgently required.

### Progress Kemp LoadMaster Critical Flaw
- **Description**: A critical-severity security flaw affecting Progress Kemp LoadMaster application delivery controllers and load balancers. The vulnerability has been heavily targeted with automated and manual exploit attempts.
- **Impact**: Successful exploitation allows attackers to compromise load balancer appliances, potentially intercepting, modifying, or redirecting application traffic, and gaining a foothold in network infrastructure.
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog after 792 reported exploit attempts. Vendors have released patches; immediate application is mandated for federal agencies and strongly advised for all users.

### TrueConf Video Conferencing Server Vulnerabilities
- **Description**: Unpatched vulnerabilities in TrueConf video conferencing servers that allowed the Head Mare hacktivist group to breach the vendor's infrastructure and replace legitimate client installers with trojanized versions containing backdoors.
- **Impact**: Supply chain compromise delivering backdoored software to TrueConf clients. Victims installing the malicious updates receive persistent remote access implants.
- **Status**: Actively exploited by Head Mare. TrueConf has acknowledged the breach; users must verify installer integrity and update from trusted sources only.

### N-able N-central RMM Exploitation
- **Description**: A recently disclosed security flaw in N-able N-central Remote Monitoring and Management (RMM) platform that attackers are actively exploiting to reach managed systems and establish persistence.
- **Impact**: Compromise of the RMM platform grants attackers administrative control over all managed endpoints, enabling mass deployment of malware, data exfiltration, and persistent access across customer environments.
- **Status**: Ongoing exploitation reported. N-able has released Hotfix 2 as part of continued investigation and remediation efforts.

### WordPress Pre-Authentication Reflected XSS
- **Description**: A pre-authentication reflected cross-site scripting vulnerability in the WordPress login screen affecting every version of the CMS. The flaw can be chained to achieve PHP code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary JavaScript in victims' browsers, potentially leading to account takeover, credential theft, and through exploit chains, remote code execution on the server.
- **Status**: Patched in recent WordPress releases. All versions prior to the fix are affected; immediate updating is recommended.

### Malicious npm Package Campaign
- **Description**: A supply chain attack involving nearly 800 malicious packages published to the npm registry, designed to deliver cross-platform remote access trojans (RATs) and infostealers targeting Windows, macOS, and Linux systems.
- **Impact**: Developers installing compromised packages inadvertently execute malware that establishes persistent access, steals credentials, cryptocurrency wallets, and sensitive project data.
- **Status**: Active campaign. Malicious packages identified and removal underway; developers must audit dependencies and rotate compromised credentials.

## Affected Systems and Products

- **Metabase**: Business intelligence and data visualization platform (all unpatched versions); exploited for unauthenticated admin access and data theft at Framework and Tally
- **Progress Kemp LoadMaster**: Application delivery controllers and load balancer appliances (vulnerable firmware versions); 792+ exploit attempts recorded, listed on CISA KEV
- **TrueConf Video Conferencing Server**: On-premises video conferencing server software (unpatched versions); breached to trojanize client installers
- **TrueConf Client Installers**: Windows, macOS, and Linux client applications; trojanized versions distributed via official update mechanisms
- **N-able N-central**: Remote Monitoring and Management platform (versions prior to Hotfix 2); exploited to access managed client systems
- **WordPress Core**: All versions prior to latest security release; pre-auth XSS in login screen with RCE exploit chain potential
- **npm Registry Packages**: Nearly 800 identified malicious packages across the ecosystem; cross-platform impact on Windows, macOS, and Linux development environments
- **Webmail Platforms**: Microsoft Outlook, Google Gmail, Fastmail, Proton Mail, Yahoo Mail; vulnerable to CSS-based message boundary escape attacks
- **Microsoft 365 / Entra ID**: Targeted via AitM phishing and Windows Hello for Business key abuse for persistent access
- **Atlassian Rovo / Jira / Confluence**: Rovo AI assistant vulnerable to prompt injection enabling data exfiltration from accessible projects
- **Linux Kernel**: SCTP subsystem (18-year-old use-after-free flaw); local privilege escalation and container escape demonstrated by researchers
- **Apache HTTP Server**: Zero-day discovered via AI-assisted HTTP desynchronization research; details pending coordinated disclosure

## Attack Vectors and Techniques

- **SQL Injection (Zero-Day)**: Unauthenticated SQL injection in Metabase administrative endpoints enabling full database control and admin account takeover
- **Supply Chain Compromise (Vendor Breach)**: Head Mare breached TrueConf infrastructure to sign and distribute trojanized client installers through legitimate update channels
- **Supply Chain Compromise (Package Repository)**: Malicious npm packages typosquatting or masquerading as legitimate libraries, executing payloads on install via lifecycle scripts
- **ClickFix Social Engineering**: Fake browser error pages or CAPTCHAs instructing victims to run PowerShell/terminal commands that download and execute malware (now targeting macOS with Go-based stealers)
- **Vishing (Voice Phishing)**: UNC6671 uses phone-based social engineering targeting personal phones of employees at financial services and private equity firms to steal SaaS credentials
- **Adversary-in-the-Middle (AitM) Phishing**: Large-scale campaigns using reverse proxy phishing kits to hijack Microsoft 365 session tokens, bypassing MFA and targeting payroll/finance emails
- **CSS Injection / Message Boundary Escape**: Malicious email content uses CSS to break out of message containers in webmail interfaces, stealing credentials and tokens via UI manipulation
- **NAT Table Manipulation (NatJack)**: Attacker manipulates NAT connection tracking state to hijack active TCP sessions and spoof DNS responses on local network segments
- **Prompt Injection / Indirect Prompt Injection**: Attacker-controlled instructions in Jira/Confluence data cause Atlassian Rovo to exfiltrate accessible data to external servers
- **HTTP Request Smuggling / Desynchronization**: Novel HTTP desync techniques discovered via AI-assisted research, enabling cache poisoning, request smuggling, and bypass of security controls
- **Windows Hello for Business Key Abuse**: Malware with local execution hijacks WHfB cryptographic keys to authenticate as the user to Entra ID, achieving persistent cloud access
- **CI/CD Pipeline Injection**: GitHub issues with crafted content trigger code execution in CI runners for Claude Code and Gemini CLI repositories, accessing workflow secrets
- **Container Escape via Kernel Use-After-Free**: Linux SCTP flaw exploited for local root privilege escalation and container breakout to host system

## Threat Actor Activities

- **Head Mare**: Hacktivist group targeting Russian-speaking entities. Breached TrueConf video conferencing infrastructure, exploited unpatched server vulnerabilities, and trojanized client installers with backdoors for persistent access to victims.
- **UNC6671**: Data extortion group linked to BlackFile threat actor. Conducts vishing campaigns targeting financial services, hedge funds, private equity, and professional services firms. Uses personal phone outreach to steal SaaS credentials and access sensitive financial data.
- **TeamPCP**: Cybercrime actor active since at least 2020. Initially compromised internet-facing Redis instances; evolved to supply chain campaigns. Demonstrates long-term infrastructure compromise and operational adaptation.
- **ClickFix Operators**: Unknown threat actors deploying ClickFix social engineering at scale. Recently expanded from Windows to macOS targets with Go-based infostealers (AMOS/Atomic Stealer variants) focusing on cryptocurrency wallets, browser credentials, and Apple Keychain data.
- **AitM Phishing Campaign Operators**: Unattributed groups running widespread email-driven adversary-in-the-middle phishing against Microsoft 365. Target payroll and finance departments for business email compromise and financial fraud.
- **Malicious npm Package Publishers**: Unattributed campaign operators publishing nearly 800 typosquatted/malicious packages to npm. Targeting software developers across Windows, macOS, and Linux for RAT and infostealer deployment.

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
