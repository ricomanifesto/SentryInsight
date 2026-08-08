# Exploitation Report

## Executive Summary

A critical zero-day SQL injection vulnerability in Metabase business intelligence software has been actively exploited in targeted data theft attacks against customer instances, with confirmed breaches at financial services firm Framework and fintech company Tally. This exploitation represents a significant supply chain risk as Metabase is widely deployed for internal analytics and dashboarding across organizations of all sizes.

Multiple threat actors are conducting diverse campaigns spanning social engineering, supply chain compromise, and infrastructure targeting. The UNC6671 extortion group—linked to BlackFile ransomware operations—has escalated vishing attacks against financial services, private equity, and professional services firms, leveraging voice-based social engineering to compromise SaaS credentials. Simultaneously, a massive npm supply chain campaign has deployed nearly 800 malicious packages delivering cross-platform remote access trojans and infostealers across Windows, macOS, and Linux environments. ClickFix-style social engineering attacks have evolved to target macOS users with Go-based malware capable of draining cryptocurrency wallets, stealing browser credentials, and exfiltrating Apple iCloud Keychain data.

Critical infrastructure and enterprise systems face mounting pressure from both novel attack techniques and long-standing vulnerabilities. The 18-year-old Linux SCTP kernel flaw has been weaponized for container escape and privilege escalation, while new research demonstrates NAT manipulation attacks (NatJack) capable of hijacking TCP sessions and spoofing DNS responses. Microsoft 365 environments are under sustained adversary-in-the-middle phishing campaigns targeting payroll and finance communications, and Swiss government SharePoint servers were compromised through vulnerability exploitation affecting approximately 200 accounts. These developments underscore the expanding attack surface across cloud identities, containerized workloads, and network infrastructure.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase open-source business intelligence platform that allows unauthenticated attackers to execute arbitrary SQL commands on the backend database
- **Impact**: Full database access leading to customer data theft, potential lateral movement within compromised networks, and exposure of sensitive business analytics data
- **Status**: Actively exploited as a zero-day against Framework and Tally customer instances; patches or mitigations not specified in available reporting

### npm Supply Chain Malware Campaign
- **Description**: A cluster of nearly 800 malicious packages published to the npm registry designed to deliver cross-platform malware targeting Windows, macOS, and Linux systems
- **Impact**: Remote access trojan (RAT) capabilities and infostealer functionality across all major operating systems, enabling persistent access, credential theft, and data exfiltration from developer environments
- **Status**: Active campaign with packages published to the official npm registry; discovery and takedown status not specified

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks delivering Go-based malware targeting macOS users through fake browser verification prompts and CAPTCHA pages
- **Impact**: Theft of cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials; potential for financial fraud and identity theft
- **Status**: Active exploitation targeting macOS users; malware delivery via social engineering rather than vulnerability exploitation

### Linux SCTP Kernel Vulnerability Exploitation
- **Description**: An 18-year-old use-after-free bug in Linux's SCTP (Stream Control Transmission Protocol) networking code that can be exploited for local privilege escalation to root and container escape
- **Impact**: Full root access on host systems from unprivileged local users; container escape from Kubernetes and other containerized environments to the underlying host
- **Status**: Researchers at Tencent demonstrated successful exploitation for container escape; patch availability not specified in reporting

### Swiss Government SharePoint Exploitation
- **Description**: Exploitation of vulnerabilities in Microsoft SharePoint servers operated by Switzerland's federal IT office
- **Impact**: Compromise of approximately 200 accounts with potential access to government communications and documents
- **Status**: Confirmed breach; specific vulnerabilities exploited not disclosed in available reporting

### Microsoft 365 Adversary-in-the-Middle Phishing
- **Description**: Widespread email-driven phishing campaign employing adversary-in-the-middle (AitM) techniques to bypass multi-factor authentication and hijack Microsoft 365 accounts
- **Impact**: Account takeover with focus on payroll and finance email communications; potential for business email compromise, financial fraud, and further lateral phishing
- **Status**: Active campaign; targets Microsoft 365 users across organizations

### AI Coding Agent Supply Chain Vulnerabilities
- **Description**: Flaws in Anthropic's Claude Code and Google's Gemini CLI that allow a GitHub issue opened by an unprivileged account to execute code on CI runners and access workflow secrets
- **Impact**: Potential supply chain compromise through AI-assisted development tools; access to CI/CD secrets and build pipelines
- **Status**: Demonstrated against Anthropic, Google, and OpenAI repositories; mitigation status not specified

## Affected Systems and Products

- **Metabase**: Business intelligence platform; customer instances at Framework and Tally confirmed compromised; versions affected not specified
- **npm Registry**: JavaScript package ecosystem; nearly 800 malicious packages published affecting Windows, macOS, and Linux development environments
- **macOS Systems**: Targeted by ClickFix-delivered Go-based infostealer malware stealing crypto wallets, browser credentials, and iCloud Keychain data
- **Linux Kernel**: SCTP subsystem vulnerability affecting all Linux distributions with SCTP support; impacts containerized environments including Kubernetes
- **Microsoft SharePoint**: Swiss federal government servers compromised; specific versions not disclosed; approximately 200 accounts affected
- **Microsoft 365**: Enterprise cloud productivity suite targeted by AitM phishing campaigns focusing on payroll and finance personnel
- **Anthropic Claude Code**: AI coding agent with GitHub integration vulnerability allowing CI workflow secret exposure via unprivileged GitHub issues
- **Google Gemini CLI**: AI coding agent with similar GitHub integration flaw enabling CI runner code execution
- **OpenAI Codex/Repository**: AI coding agent repository also affected by GitHub issue-based CI secret exposure
- **Cisco Catalyst SD-WAN and IOS XE**: Multiple critical vulnerabilities patched (three rated 9.9 CVSS); exploitation status not confirmed in reporting
- **WordPress**: All versions affected by pre-authentication reflected XSS in login screen; patch released
- **Linux KVM**: Zapscape vulnerability allowing L1 guest VM kernel-privileged code to escape to host; affects virtualized environments

## Attack Vectors and Techniques

- **SQL Injection (Zero-Day)**: Unauthenticated database query manipulation in Metabase enabling data exfiltration and potential remote code execution
- **Supply Chain Compromise (npm)**: Malicious package publishing to public registry with typosquatting and dependency confusion techniques delivering cross-platform RAT/infostealer payloads
- **ClickFix Social Engineering**: Fake browser verification/CAPTCHA pages tricking users into executing malicious commands via clipboard manipulation and Run dialog
- **Voice Phishing (Vishing)**: Telephone-based social engineering targeting personal phones to steal SaaS credentials and bypass MFA; used by UNC6671 against financial sector
- **Container Escape via Kernel Exploit**: Leveraging 18-year-old SCTP use-after-free for privilege escalation and host escape from containerized workloads
- **NAT Table Manipulation (NatJack)**: Manipulating network address translation connection state to hijack active TCP sessions and spoof DNS responses
- **Adversary-in-the-Middle (AitM) Phishing**: Real-time proxy phishing capturing MFA tokens and session cookies for Microsoft 365 account takeover
- **AI Agent Sandbox Escape**: Exploiting AI coding agent integrations with GitHub to execute unauthorized code on CI runners and access workflow secrets
- **Windows Hello for Business Key Abuse**: Malware leveraging signed-in user's Windows Hello keys for persistent Entra ID authentication without user interaction
- **HTTP Request Smuggling/Desync**: AI-discovered novel HTTP desynchronization techniques and Apache zero-day enabling request smuggling and cache poisoning
- **CPU Side-Channel (TONTOU)**: Bypassing Spectre v2 mitigations to leak Linux password hashes through speculative execution attacks
- **Clipboard Hijacking**: Malware monitoring and replacing clipboard contents for cryptocurrency address substitution and payment diversion
- **Business Email Compromise via Compromised Inboxes**: Using legitimate compromised email accounts for banking malware delivery and payment fraud

## Threat Actor Activities

- **UNC6671**: Data extortion group linked to BlackFile ransomware; conducting vishing campaigns targeting financial services, private equity, and professional services; uses voice-based social engineering to compromise SaaS credentials; attributed to hedge fund cyberattacks
- **TeamPCP**: Threat actor active since at least 2020; compromising internet-facing Redis instances; linked to later supply chain campaigns; long-term infrastructure compromise operations
- **BlackFile Ransomware Group**: Associated with UNC6671; extortion operations targeting financial organizations; data theft and encryption for ransom
- **ClickFix Operators**: Threat actors employing ClickFix social engineering framework; recently expanded from Windows to macOS targets with Go-based infostealer; focus on cryptocurrency theft
- **npm Campaign Operators**: Unknown threat actor(s) publishing nearly 800 malicious packages to npm registry; cross-platform malware distribution targeting developer ecosystems
- **Canadian Snowflake Extortionist**: 26-year-old Canadian man pleaded guilty to computer fraud and conspiracy; described as one of the most consequential cybercrime actors of 2024; extorted over 165 organizations via Snowflake data breaches
- **Levi Strauss Attackers**: Unknown threat actors using social engineering on three employees to access and steal corporate data from employee machines
- **North Carolina Ports Attackers**: Unknown threat actors disrupting IT systems and operations at Port of Wilmington, Port of Morehead City, and Charlotte Inland Port
- **Swiss Government SharePoint Attackers**: Unknown threat actors exploiting SharePoint vulnerabilities to compromise approximately 200 federal accounts
- **Microsoft 365 AitM Campaign Operators**: Unknown threat actors conducting widespread phishing campaign targeting payroll and finance emails across organizations

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
