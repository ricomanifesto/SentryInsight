# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are being actively exploited across diverse technology stacks, from business intelligence platforms and video conferencing systems to webmail interfaces and AI coding assistants. The Metabase SQL injection zero-day stands out as a maximum-severity flaw enabling unauthenticated administrative access and data theft, with confirmed breaches at Framework and Tally. Simultaneously, the Head Mare hacktivist group has compromised TrueConf video conferencing servers to distribute trojanized client installers, while researchers have uncovered novel CSS-based attacks that bypass webmail defenses across major providers including Outlook, Gmail, and Proton Mail.

Supply chain threats continue to escalate with nearly 800 malicious npm packages delivering cross-platform remote access trojans and infostealers, and the TeamPCP threat actor linked to Redis compromises dating back to 2020. The UNC6671 extortion group—associated with BlackFile ransomware—is conducting vishing campaigns targeting financial services and hedge funds, while ClickFix social engineering attacks now deploy macOS stealers capable of draining cryptocurrency wallets and harvesting Apple Keychain credentials. Progress Kemp LoadMaster appliances face active exploitation with 792 reported attempts, earning a CISA KEV listing, and N-able N-central RMM platforms are under sustained attack despite hotfix releases.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence and data visualization software that allows unauthenticated attackers to achieve administrative access. The flaw is being exploited as a zero-day in the wild.
- **Impact**: Attackers gain full administrative control over Metabase instances and can exfiltrate customer data. Confirmed breaches include Framework and Tally, with data theft as the primary objective.
- **Status**: Actively exploited as a zero-day; patch availability not specified in source articles

### TrueConf Video Conferencing Server Vulnerabilities
- **Description**: Vulnerabilities in unpatched TrueConf video conferencing servers that allow attackers to breach the infrastructure and replace legitimate client installers with malicious versions containing backdoors.
- **Impact**: Compromised servers distribute trojanized installers to clients, delivering persistent backdoors. The Head Mare hacktivist group is leveraging this for supply chain-style compromise of TrueConf users.
- **Status**: Actively exploited; requires server patching to prevent installer replacement

### CSS-Based Webmail Escape Attacks
- **Description**: Novel attack technique where malicious content inside emails escapes message boundaries and interferes with the webmail interface itself, bypassing traditional sanitization defenses.
- **Impact**: Attackers can steal passwords and authentication tokens across multiple webmail platforms. Demonstrated effective against Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail.
- **Status**: Research-proven attack chains; no specific patch mentioned as fixes require webmail provider implementation

### Atlassian Rovo Data Exfiltration
- **Description**: Attacker-controlled instructions can manipulate Atlassian's Rovo AI assistant into collecting Jira and Confluence data accessible to a signed-in user and sending it to an external server.
- **Impact**: Unauthorized access to sensitive project management and wiki data including issues, documents, and configuration details accessible through the compromised user's permissions.
- **Status**: Discovered by two security firms; Atlassian response not detailed in source

### Progress Kemp LoadMaster Critical Flaw
- **Description**: Critical-severity vulnerability in Progress Kemp LoadMaster load balancing appliances that has attracted significant exploitation activity.
- **Impact**: 792 reported exploit attempts recorded, prompting CISA to add this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog, mandating federal agency remediation.
- **Status**: Actively exploited; added to CISA KEV catalog indicating confirmed in-the-wild exploitation

### N-able N-central RMM Exploitation
- **Description**: Recently disclosed security flaw in the N-able N-central Remote Monitoring and Management platform that attackers are actively exploiting to reach managed systems and establish persistence.
- **Impact**: Attackers gain access to managed client systems through the RMM platform, enabling lateral movement and persistent access across customer environments.
- **Status**: Ongoing exploitation; N-able has released Hotfix 2 as part of investigation

### WordPress Pre-Authentication XSS
- **Description**: Reflected cross-site scripting vulnerability in the WordPress login screen that requires no authentication and affects every version of the CMS.
- **Impact**: Can be chained to achieve PHP code execution on the server. Researcher pwn.ai demonstrated the exploit chain from XSS to remote code execution.
- **Status**: WordPress has released a fix; immediate patching recommended

### Linux SCTP Use-After-Free Vulnerability
- **Description**: An 18-year-old use-after-free bug in Linux's SCTP (Stream Control Transmission Protocol) networking code that allows local users to escalate privileges to root.
- **Impact**: Full root access on the host system; Tencent researchers demonstrated container escape capabilities, allowing breakout from containerized environments to the underlying host.
- **Status**: Long-standing vulnerability; patch status not specified in source

### Apache HTTP Desynchronization Zero-Day
- **Description**: Novel HTTP request smuggling/desynchronization techniques discovered by AI-assisted research system HTTP Terminator, including a zero-day affecting Apache HTTP Server.
- **Impact**: HTTP desync attacks can lead to request smuggling, cache poisoning, and bypass of security controls. The Apache zero-day represents active risk to web infrastructure.
- **Status**: Zero-day disclosed by PortSwigger research; Apache patch status not specified

## Affected Systems and Products

- **Metabase Business Intelligence Platform**: All versions vulnerable to SQL injection zero-day enabling unauthenticated admin access and data theft; confirmed impact on Framework and Tally customer instances
- **TrueConf Video Conferencing Server**: Unpatched server versions vulnerable to compromise enabling installer trojanization; affects client installers distributed to end users
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail vulnerable to CSS-based message boundary escape attacks stealing credentials and tokens
- **Atlassian Rovo/Jira/Confluence**: Rovo AI assistant can be manipulated to exfiltrate data accessible to signed-in users across Jira and Confluence instances
- **Progress Kemp LoadMaster**: Load balancing appliances targeted with 792 exploit attempts; critical severity flaw added to CISA KEV
- **N-able N-central**: RMM platform under active exploitation; managed service provider environments and their downstream customers at risk
- **WordPress CMS**: Every version affected by pre-authentication reflected XSS in login screen; chainable to PHP code execution
- **Linux Kernel**: SCTP subsystem contains 18-year-old use-after-free flaw affecting containerized and bare-metal deployments; enables root escalation and container escape
- **Apache HTTP Server**: Zero-day HTTP desynchronization vulnerability discovered via AI-assisted research; affects web server deployments
- **npm Registry**: Nearly 800 malicious packages published delivering cross-platform RAT and infostealer malware targeting Windows, macOS, and Linux
- **Windows Hello for Business / Entra ID**: Malware can abuse Windows Hello keys for persistent Entra ID authentication in signed-in sessions
- **Claude Code / Gemini CLI**: AI coding assistants with flaws allowing GitHub issues to execute code on CI runners and access workflow secrets
- **Redis Instances**: Internet-facing Redis servers targeted by TeamPCP since 2020, with later supply chain campaign activity

## Attack Vectors and Techniques

- **Supply Chain Compromise via Server Breach**: Attackers breach TrueConf servers to replace legitimate client installers with backdoored versions, distributing malware to downstream users through trusted update channels
- **CSS Injection / Message Boundary Escape**: Malicious email content uses CSS to break out of message containers and manipulate webmail DOM, stealing credentials and tokens across multiple providers
- **AI Assistant Prompt Injection**: Attacker-controlled instructions manipulate Atlassian Rovo into accessing and exfiltrating Jira/Confluence data accessible to the authenticated user
- **SQL Injection for Unauthenticated Admin Access**: Metabase zero-day allows direct database manipulation to escalate to administrative privileges without authentication
- **ClickFix Social Engineering**: Fake error pages and verification prompts trick users into executing malicious commands, now delivering macOS stealers (Go-based) targeting crypto wallets, browser passwords, Apple Keychain, and cached credentials
- **Vishing (Voice Phishing)**: UNC6671 uses phone-based social engineering targeting personal phones of employees at financial services, private equity, and professional services firms to steal SaaS credentials
- **Malicious Package Publication**: Nearly 800 npm packages published as part of coordinated campaign delivering cross-platform RAT and infostealer payloads
- **Adversary-in-the-Middle (AitM) Phishing**: Microsoft 365 campaign uses AitM techniques to hijack session tokens and access payroll/finance emails
- **HTTP Request Smuggling / Desynchronization**: Novel techniques for HTTP desync attacks discovered via AI-assisted fuzzing, including Apache zero-day
- **Windows Hello Key Abuse**: Malware in signed-in session silently uses Windows Hello for Business keys to authenticate to Entra ID for persistent access
- **CI/CD Pipeline Exploitation via AI Tools**: GitHub issues with no repository privileges trigger code execution on CI runners through flaws in Claude Code and Gemini CLI
- **NAT Table Manipulation (NatJack)**: Manipulation of NAT connection state to hijack active TCP sessions and spoof DNS responses
- **Redis Exploitation for Initial Access**: TeamPCP compromises internet-facing Redis instances as foothold for broader infrastructure compromise and supply chain attacks

## Threat Actor Activities

- **Head Mare**: Hacktivist group exploiting unpatched TrueConf servers to trojanize client installers with backdoors; conducting supply chain-style attacks against video conferencing users
- **UNC6671**: Data extortion group linked to BlackFile ransomware; conducting vishing campaigns targeting financial services, hedge funds, private equity, and professional services; uses personal phone targeting to steal SaaS credentials
- **TeamPCP**: Threat actor active since at least 2020 compromising internet-facing Redis instances; linked to later supply chain campaign activity; long-term infrastructure compromise operations
- **ClickFix Operators**: Threat actors deploying ClickFix social engineering technique evolved to target macOS with Go-based infostealer (dubbed "Cthulhu Stealer" in related reporting) for cryptocurrency theft and credential harvesting
- **AitM Phishing Campaign Operators**: Widespread email-driven campaign using adversary-in-the-middle infrastructure to hijack Microsoft 365 accounts and harvest payroll/finance communications
- **Malicious npm Package Publishers**: Coordinated campaign publishing nearly 800 packages to npm registry delivering cross-platform RAT and infostealer malware
- **BlackFile Ransomware Group**: Associated with UNC6671 extortion activities targeting financial sector organizations

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
