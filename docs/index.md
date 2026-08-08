# Exploitation Report

## Executive Summary

A significant wave of active exploitation activity has been observed across multiple vectors, with zero-day vulnerabilities in enterprise software and novel attack techniques dominating the threat landscape. The Head Mare hacktivist group has compromised TrueConf video conferencing servers to trojanize client installers with backdoors, while a critical Metabase SQL injection zero-day has been actively exploited in data theft attacks against Framework and Tally customers. Simultaneously, the Progress Kemp LoadMaster vulnerability has been added to CISA's Known Exploited Vulnerabilities catalog following 792 reported exploit attempts, and N-able has issued emergency hotfixes for N-central as attackers achieve persistence on managed systems.

Novel attack methodologies are expanding the exploitation surface beyond traditional vulnerabilities. Research has uncovered CSS-based attacks that break webmail defenses across major providers including Outlook, Gmail, and Proton Mail, while the NatJack technique manipulates NAT tables to hijack TCP sessions and spoof DNS responses. AI-assisted research has discovered new HTTP desynchronization techniques and an Apache zero-day, and malware operators are abusing Windows Hello for Business keys to maintain persistent Entra ID access. Supply chain threats continue to escalate, with nearly 800 malicious npm packages delivering cross-platform RATs and infostealers, and the TeamPCP group linked to Redis compromises dating back to 2020.

Threat actor activity shows increased sophistication in social engineering and identity-focused attacks. The UNC6671 extortion group, linked to BlackFile ransomware, is conducting vishing campaigns targeting financial services and hedge funds through personal phone compromise. ClickFix attacks have expanded to macOS with Go-based stealers draining cryptocurrency wallets and harvesting iCloud Keychain data, while adversary-in-the-middle phishing campaigns hijack Microsoft 365 accounts to harvest payroll and finance emails. Traditional social engineering remains effective, as demonstrated by the Levi Strauss breach where three employees were manipulated to expose corporate data.

## Active Exploitation Details

### TrueConf Video Conferencing Server Compromise
- **Description**: Hackers are exploiting vulnerabilities in unpatched TrueConf video conferencing servers to gain access and replace legitimate client installers with trojanized versions containing backdoors
- **Impact**: Attackers achieve supply chain compromise, delivering backdoors to any user downloading the client installer from compromised servers
- **Status**: Actively exploited; requires server patching and installer verification
- **CVE ID**: Not specified in source

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence and data visualization software allowing unauthenticated administrative access
- **Impact**: Full administrative access to Metabase instances without authentication, enabling data theft from customer deployments
- **Status**: Actively exploited as zero-day; confirmed breaches at Framework and Tally
- **CVE ID**: Not specified in source

### Progress Kemp LoadMaster Critical Flaw
- **Description**: Critical-severity vulnerability in Progress Kemp LoadMaster application delivery controllers
- **Impact**: 792 reported exploit attempts observed; added to CISA KEV catalog mandating federal agency remediation
- **Status**: Actively exploited in the wild; patches available
- **CVE ID**: Not specified in source

### N-able N-central RMM Exploitation
- **Description**: Security flaw in N-able N-central Remote Monitoring and Management platform allowing attackers to reach and persist on managed systems
- **Impact**: Attackers gain access to all systems managed through compromised N-central instances, establishing persistent footholds
- **Status**: Ongoing exploitation; Hotfix 2 released as part of continued investigation
- **CVE ID**: Not specified in source

### WordPress Pre-Authentication XSS
- **Description**: Reflected cross-site scripting vulnerability in WordPress login screen affecting all versions, demonstrable as part of exploit chain leading to PHP code execution
- **Impact**: Pre-authentication compromise vector; chained with other flaws to achieve remote code execution
- **Status**: Patched in latest release; exploit demonstration published by pwn.ai
- **CVE ID**: Not specified in source

### Linux Kernel SCTP Use-After-Free
- **Description**: 18-year-old use-after-free vulnerability in Linux Stream Control Transmission Protocol (SCTP) networking code
- **Impact**: Local privilege escalation to root and container escape; demonstrated by Tencent researchers to break out of containers to host
- **Status**: Long-standing flaw with published exploit technique; patch status varies by distribution
- **CVE ID**: Not specified in source

### Apache HTTP Desynchronization Zero-Day
- **Description**: Novel HTTP request smuggling/desynchronization techniques discovered through AI-assisted research, including a zero-day affecting Apache
- **Impact**: Request smuggling leading to cache poisoning, credential theft, and bypass of security controls
- **Status**: Zero-day discovered via HTTP Terminator AI system; 30,000 candidate techniques explored
- **CVE ID**: Not specified in source

## Affected Systems and Products

- **TrueConf Video Conferencing Server**: Unpatched server versions; client installers distributed from compromised servers
- **Metabase Business Intelligence Platform**: All unpatched instances; confirmed impact on Framework and Tally customer deployments
- **Progress Kemp LoadMaster**: Affected LoadMaster ADC versions; 792 exploit attempts reported across internet-facing deployments
- **N-able N-central RMM**: N-central management platform; managed endpoints downstream of compromised servers
- **WordPress CMS**: All versions prior to latest patch; login screen XSS affects entire install base
- **Linux Kernel**: Versions with vulnerable SCTP implementation; container hosts and multi-tenant environments at elevated risk
- **Apache HTTP Server**: Versions vulnerable to newly discovered desynchronization techniques; specifics pending disclosure
- **npm Registry**: Nearly 800 malicious packages published; affects Windows, macOS, and Linux development environments
- **Redis Instances**: Internet-facing Redis servers compromised by TeamPCP since 2020; supply chain impact through compromised infrastructure
- **Microsoft 365 / Entra ID**: Accounts targeted via AitM phishing; Windows Hello for Business keys abused for persistent access
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail vulnerable to CSS-based boundary escape attacks
- **Atlassian Rovo / Jira / Confluence**: Rovo assistant manipulated to exfiltrate accessible data via prompt injection
- **macOS Systems**: Targeted by ClickFix-delivered Go-based infostealer (AMOS/Atomic Stealer variant)
- **Network Infrastructure**: NAT devices vulnerable to NatJack TCP session hijacking and DNS spoofing via connection table manipulation

## Attack Vectors and Techniques

### Supply Chain Compromise via Server Takeover
- **Technique**: Compromise legitimate software distribution servers to replace authentic installers with trojanized versions
- **Vector**: Exploited vulnerabilities in TrueConf video conferencing servers → modified client installers → backdoor delivery to end users

### Zero-Day SQL Injection for Unauthenticated Admin Access
- **Technique**: SQL injection in Metabase allowing authentication bypass and administrative privilege escalation
- **Vector**: Direct exploitation of internet-exposed Metabase instances; no credentials required

### RMM Platform Abuse for Lateral Access
- **Technique**: Exploit vulnerability in central management platform to reach all downstream managed endpoints
- **Vector**: N-central flaw → persistent access to managed systems → lateral movement across customer environments

### CSS Injection Escaping Email Boundaries
- **Technique**: Malicious CSS in email content breaks out of message sandbox to manipulate webmail DOM and exfiltrate data
- **Vector**: Crafted emails sent to targets; exploits inconsistent sanitization across Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail

### NAT Table Manipulation (NatJack)
- **Technique**: Manipulate NAT connection tracking state to hijack established TCP sessions and inject spoofed DNS responses
- **Vector**: Local network access or compromised adjacent host → NAT state exhaustion/injection → session hijacking

### Adversary-in-the-Middle (AitM) Phishing
- **Technique**: Proxy-based phishing capturing credentials and session tokens in real-time, bypassing MFA
- **Vector**: Phishing emails with proxy links → victim authenticates to legitimate service through attacker proxy → session hijack

### ClickFix Social Engineering
- **Technique**: Fake error messages instruct users to run malicious commands (PowerShell/Terminal) to "fix" non-existent issues
- **Vector**: Compromised websites or malvertising → fake verification prompts → user-executed payload delivery (now targeting macOS)

### Vishing for SaaS Credential Theft
- **Technique**: Voice-based social engineering targeting personal phones to bypass corporate controls and access SaaS platforms
- **Vector**: Direct phone calls to employees → social engineering → credential harvesting → SaaS data exfiltration

### Windows Hello for Business Key Abuse
- **Technique**: Malware with local access silently uses hardware-bound WHfB keys to authenticate to Entra ID as the user
- **Vector**: Post-exploitation on compromised Windows endpoint → key material access → persistent cloud identity compromise

### Prompt Injection in AI Coding Assistants
- **Technique**: Malicious GitHub issues trigger autonomous AI agents (Claude Code, Gemini CLI) to execute code in CI environments
- **Vector**: Public issue creation → AI agent processes issue → CI workflow execution with secret access → secret exfiltration

### Malicious Package Typosquatting/Supply Chain
- **Technique**: Publish malicious packages to npm registry mimicking legitimate libraries; deliver cross-platform RAT/infostealer
- **Vector**: Developer dependency installation → automatic execution via install scripts → persistent malware deployment

### HTTP Request Desynchronization
- **Technique**: Crafted HTTP requests exploit parsing inconsistencies between front-end proxies and back-end servers
- **Vector**: Direct requests to vulnerable endpoints → request smuggling → cache poisoning, credential theft, access control bypass

### Container Escape via Kernel Vulnerability
- **Technique**: Exploit Linux kernel SCTP use-after-free from within container to achieve root on host
- **Vector**: Container with NET_RAW/NET_ADMIN capabilities or SCTP access → kernel exploit → host compromise

## Threat Actor Activities

### Head Mare (Hacktivist Group)
- **Activities**: Exploiting unpatched TrueConf servers to trojanize client installers with backdoors
- **Campaign**: Supply chain compromise targeting video conferencing software users; politically motivated hacktivist operations

### UNC6671 (Data Extortion Group / BlackFile-Linked)
- **Activities**: Vishing campaigns targeting financial services, private equity, hedge funds, and professional services via personal phone compromise
- **Campaign**: SaaS data theft and extortion; linked to BlackFile ransomware operations; leverages voice social engineering to bypass technical controls

### TeamPCP (Cybercrime Group)
- **Activities**: Compromising internet-facing Redis instances since at least 2020; evolved to supply chain campaigns
- **Campaign**: Long-term infrastructure compromise; Redis server takeover as initial access vector for broader supply chain attacks

### ClickFix Operators (Multiple Threat Actors)
- **Activities**: Deploying Go-based macOS infostealers (AMOS/Atomic Stealer variants) via ClickFix social engineering
- **Campaign**: Cryptocurrency theft, browser credential harvesting, iCloud Keychain exfiltration, cached credential theft; expanded from Windows to macOS

### AitM Phishing Campaign Operators
- **Activities**: Widespread email-driven phishing using adversary-in-the-middle techniques against Microsoft 365
- **Campaign**: Account takeover targeting payroll and finance emails; real-time session hijacking bypassing MFA

### Malicious npm Package Publishers
- **Activities**: Published nearly 800 malicious packages to npm registry delivering cross-platform RAT and infostealer
- **Campaign**: Broad supply chain targeting of developers across Windows, macOS, and Linux; automated publication infrastructure

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
