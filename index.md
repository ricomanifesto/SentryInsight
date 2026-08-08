# Exploitation Report

## Executive Summary

A critical Metabase SQL injection zero-day vulnerability has been actively exploited in data theft attacks targeting customer instances at Framework and Tally, demonstrating the ongoing risk of unpatched business intelligence platforms. Simultaneously, a widespread ClickFix campaign is delivering Go-based infostealers to macOS users to drain cryptocurrency wallets, harvest browser credentials, and exfiltrate Apple iCloud Keychain data, highlighting the evolution of social engineering techniques beyond traditional phishing.

Multiple high-severity vulnerabilities have been disclosed or patched with evidence of exploitability, including a pre-authentication XSS in all WordPress versions that can lead to PHP code execution, an 18-year-old Linux SCTP use-after-free enabling container escapes, and three 9.9 CVSS flaws in Cisco Catalyst SD-WAN and IOS XE Software. Threat actor UNC6671, linked to the BlackFile extortion group, is conducting vishing campaigns against financial services and private equity firms, while TeamPCP has been tied to Redis compromises dating back to 2020 and a subsequent supply chain campaign. A Canadian operator has pleaded guilty to the Snowflake extortion campaign impacting over 165 organizations.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence software was exploited as a zero-day before any patch was available. Attackers leveraged the flaw to breach customer instances and exfiltrate data.
- **Impact**: Full database access enabling customer data theft, potentially including sensitive business analytics, user credentials, and proprietary information.
- **Status**: Actively exploited in the wild against Framework and Tally. Patch status not specified in source article.
- **CVE ID**: Not provided in source article

### WordPress Pre-Authentication Reflected XSS
- **Description**: A reflected cross-site scripting vulnerability in the WordPress login screen affects every version of the CMS. The flaw is pre-authentication, meaning attackers do not need valid credentials to exploit it.
- **Impact**: Can lead to PHP code execution when chained with other techniques. Researcher pwn.ai demonstrated the exploit path from XSS to code execution.
- **Status**: Patched by WordPress; urgent patching recommended for all installations.
- **CVE ID**: Not provided in source article

### Linux SCTP Use-After-Free (18-Year-Old Flaw)
- **Description**: A use-after-free bug in Linux's SCTP (Stream Control Transmission Protocol) networking code has existed for 18 years. Tencent researchers demonstrated successful exploitation to gain root privileges and escape container isolation.
- **Impact**: Local privilege escalation to root on the host system and container escape, allowing attackers to break out of containerized environments and compromise the underlying host.
- **Status**: Vulnerability disclosed; patch status not specified in source article. Actively demonstrated by researchers.
- **CVE ID**: Not provided in source article

### Zapscape KVM VM Escape Vulnerability
- **Description**: A Linux kernel vulnerability (dubbed Zapscape) in the KVM hypervisor allows an attacker with kernel privileges inside an L1 guest virtual machine to escape isolation and execute code on the host.
- **Impact**: Full VM escape from guest to host, compromising the hypervisor and potentially all other VMs on the same physical host.
- **Status**: Disclosed; affects Linux kernel KVM implementation. Patch status not specified in source article.
- **CVE ID**: Not provided in source article

### TONTOU CPU Speculative Execution Attack
- **Description**: A new attack technique (TONTOU) bypasses existing Spectre v2 mitigations on modern CPUs to leak secrets from Linux machines, including password hashes.
- **Impact**: Speculative execution side-channel attack that defeats current hardware and software mitigations, enabling extraction of sensitive memory contents such as credential hashes.
- **Status**: Research disclosure; demonstrates bypass of deployed Spectre v2 fixes. No patch mentioned in source article.
- **CVE ID**: Not provided in source article

### NatJack NAT Manipulation Attacks
- **Description**: A new attack class (NatJack) disclosed by researcher Malcolm Stagg manipulates network address translation (NAT) connection state tables to hijack active TCP sessions and spoof DNS responses.
- **Impact**: TCP session hijacking and DNS spoofing without requiring position on the network path, exploiting stateful NAT behavior.
- **Status**: Research disclosure; affects NAT implementations broadly. No vendor patches mentioned in source article.
- **CVE ID**: Not provided in source article

### Windows Hello for Business Key Abuse for Entra ID Persistence
- **Description**: Researcher Dirk-jan Mollema demonstrated that malware running in a signed-in Windows session can silently use the victim's Windows Hello for Business cryptographic key to authenticate to Microsoft Entra ID (formerly Azure AD).
- **Impact**: Persistent, stealthy access to Entra ID resources without requiring user interaction or credential theft, bypassing MFA protections tied to Windows Hello.
- **Status**: Proof-of-concept demonstrated; no patch mentioned in source article. Mitigation requires configuration changes.
- **CVE ID**: Not provided in source article

### Claude Code and Gemini CLI CI Workflow Vulnerabilities
- **Description**: Flaws in Anthropic's Claude Code and Google's Gemini CLI allowed a GitHub issue opened by an account with no repository privileges to execute code on the CI runners behind their coding-agent repositories.
- **Impact**: Unauthorized code execution in CI/CD pipelines, potentially exposing workflow secrets, supply chain compromise, and lateral movement to production environments.
- **Status**: Disclosed; affected Anthropic, Google, and OpenAI repositories. Remediation status not specified in source article.
- **CVE ID**: Not provided in source article

### Apache HTTP Server Zero-Day (HTTP Terminator Discovery)
- **Description**: An AI-assisted research system (HTTP Terminator) discovered novel HTTP desynchronization techniques and an Apache HTTP Server zero-day vulnerability through automated exploration of 30,000 candidate techniques.
- **Impact**: HTTP request smuggling/desynchronization leading to cache poisoning, credential theft, and bypass of security controls.
- **Status**: Zero-day disclosed by PortSwigger/James Kettle; patch status not specified in source article.
- **CVE ID**: Not provided in source article

### Cisco Catalyst SD-WAN and IOS XE Critical Vulnerabilities
- **Description**: Cisco released patches for 12 security vulnerabilities in Catalyst SD-WAN and IOS XE Software, including three flaws rated 9.9 CVSS (critical).
- **Impact**: Remote code execution, privilege escalation, and denial of service on critical network infrastructure devices.
- **Status**: Patches available; urgent deployment recommended given critical severity scores.
- **CVE ID**: Not provided in source article

### Swiss Government SharePoint Vulnerability Exploitation
- **Description**: Hackers exploited vulnerabilities in Microsoft SharePoint servers operated by Switzerland's federal IT office, compromising approximately 200 accounts.
- **Impact**: Unauthorized access to government SharePoint environment, potential data exfiltration, and lateral movement within federal systems.
- **Status**: Breach confirmed; specific vulnerabilities not identified in source article. Investigation ongoing.
- **CVE ID**: Not provided in source article

## Affected Systems and Products

- **Metabase**: Business intelligence platform; customer instances at Framework and Tally confirmed breached
- **WordPress**: All versions affected by pre-auth reflected XSS in login screen
- **Linux Kernel**: SCTP subsystem (18-year-old flaw), KVM hypervisor (Zapscape VM escape)
- **Cisco Catalyst SD-WAN**: Multiple critical vulnerabilities including three 9.9 CVSS flaws
- **Cisco IOS XE Software**: Multiple critical vulnerabilities including three 9.9 CVSS flaws
- **Microsoft SharePoint**: Swiss federal government servers compromised (~200 accounts)
- **Windows Hello for Business / Microsoft Entra ID**: Cryptographic key abuse for persistent authentication
- **npm Registry**: Nearly 800 malicious packages delivering cross-platform RAT and infostealer
- **macOS**: Targeted by ClickFix-delivered Go-based infostealer (crypto wallets, browser passwords, iCloud Keychain)
- **Microsoft 365**: Targeted by adversary-in-the-middle (AitM) phishing campaign harvesting payroll/finance emails
- **Apache HTTP Server**: Zero-day discovered via AI-assisted HTTP desynchronization research
- **Anthropic Claude Code / Google Gemini CLI / OpenAI**: CI/CD workflow vulnerabilities via GitHub issue interaction
- **Redis Servers**: Compromised by TeamPCP since 2020, later used in supply chain campaign
- **Snowflake**: Customer instances targeted in extortion campaign affecting 165+ organizations
- **CPU Hardware (Spectre v2 mitigations)**: TONTOU attack bypasses deployed speculative execution defenses

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers use fake verification prompts (e.g., "I'm not a robot" CAPTCHA mimics) to trick users into executing malicious PowerShell/terminal commands that download and run infostealers. Targets macOS and Windows users.
- **Vishing (Voice Phishing)**: UNC6671 operators call victims on personal phones, impersonating IT support to steal SaaS credentials and MFA codes for data extortion.
- **Adversary-in-the-Middle (AitM) Phishing**: Phishing proxies intercept Microsoft 365 authentication sessions, stealing session cookies and bypassing MFA to access payroll and finance emails.
- **Malicious npm Package Supply Chain**: Nearly 800 typosquatting/brandjacking packages published to npm registry deliver cross-platform RAT and infostealer payloads for Windows, macOS, and Linux.
- **SQL Injection (Zero-Day)**: Unauthenticated SQLi in Metabase exploited pre-patch for direct database access and data exfiltration.
- **Reflected XSS to RCE Chain**: WordPress login screen XSS chained with additional techniques to achieve PHP code execution without authentication.
- **Container Escape via Kernel Flaw**: Local SCTP use-after-free exploited from within container to gain host root privileges.
- **VM Escape via KVM Flaw**: Privileged L1 guest code exploits Zapscape to break KVM isolation and execute on host.
- **NAT Table Manipulation (NatJack)**: Attacker manipulates NAT connection tracking state to hijack TCP sessions and inject spoofed DNS responses.
- **Windows Hello Key Theft**: Malware abuses authenticated session's Windows Hello for Business private key for silent Entra ID token acquisition.
- **CI/CD Pipeline Injection**: GitHub issues with crafted content trigger code execution in CI runners for AI coding agent repositories.
- **HTTP Request Smuggling/Desynchronization**: AI-discovered techniques for desyncing frontend/backend HTTP parsing, leading to cache poisoning and credential theft.
- **Compromised Business Email + Browser Manipulation**: Attackers use hijacked legitimate email threads and browser-in-the-browser techniques for banking malware delivery.
- **Clipboard Hijacking**: Malware monitors and replaces cryptocurrency wallet addresses in clipboard during copy-paste operations.
- **Social Engineering (Employee Targeting)**: Levi Strauss breach via social engineering of three employees to access corporate data on their machines.
- **AI Sandbox Escape**: Researchers demonstrated C2-style control over ChatGPT's isolated sandbox; similar escapes reported at OpenAI, Anthropic, and Meta.

## Threat Actor Activities

- **UNC6671**: Data extortion group linked to BlackFile ransomware operation. Conducts vishing campaigns targeting financial services, private equity, hedge funds, and professional services firms. Uses personal phone calls to steal SaaS credentials and exfiltrate data for extortion. Active in H1 2026.
- **TeamPCP**: Cybercrime actor compromising internet-facing Redis instances since at least 2020. Linked to a later software supply chain campaign. Demonstrates long-term infrastructure compromise and pivot to supply chain attacks.
- **Snowflake Extortion Operator (Canadian National)**: 26-year-old Canadian man pleaded guilty to computer fraud and conspiracy for hacking and extorting more than 165 organizations via compromised Snowflake credentials. Described as one of the most consequential cybercrime actors of 2024.
- **ClickFix Campaign Operators**: Unattributed threat actors running widespread ClickFix social engineering campaigns delivering Go-based infostealers (macOS) and Windows malware for cryptocurrency theft and credential harvesting.
- **AitM Phishing Campaign Operators**: Unattributed group running "widespread email-driven phishing campaign" using adversary-in-the-middle infrastructure to hijack Microsoft 365 accounts and target payroll/finance communications.
- **Malicious npm Package Publishers**: Unattributed operators publishing nearly 800 malicious packages to npm registry in coordinated campaign for cross-platform malware distribution.

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
