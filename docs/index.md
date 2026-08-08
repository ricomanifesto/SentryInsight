# Exploitation Report

## Executive Summary

A critical zero-day SQL injection vulnerability in Metabase was actively exploited to breach customer instances at Framework and Tally, resulting in data theft. The attacks demonstrate continued targeting of business intelligence platforms with pre-authentication flaws that allow direct database access. Simultaneously, a massive supply chain campaign involving nearly 800 malicious npm packages delivered cross-platform remote access trojans and infostealers across Windows, macOS, and Linux environments, highlighting the persistent risk of software supply chain compromise.

Threat actor UNC6671, linked to the BlackFile extortion group, conducted a wave of vishing and social engineering attacks targeting financial services, hedge funds, private equity firms, and professional services organizations. The group leverages voice phishing against personal phones to gain initial access to SaaS environments, followed by data extortion. A Canadian threat actor pleaded guilty to orchestrating the Snowflake extortion campaign that compromised over 165 organizations in 2024, marking a significant law enforcement milestone against cloud-focused cybercrime.

New attack techniques continue to emerge across the stack: ClickFix social engineering delivers macOS infostealers targeting cryptocurrency wallets and credential stores; the NatJack attack class manipulates NAT tables to hijack TCP sessions and spoof DNS; AI-assisted research uncovered novel HTTP desynchronization techniques and an Apache zero-day; and the 18-year-old Linux SCTP flaw enables local privilege escalation and container escape. Meanwhile, the Swiss government suffered a SharePoint breach compromising 200 accounts, North Carolina Ports experienced operational disruption from a cyberattack, and Levi Strauss fell victim to employee-targeted social engineering.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical pre-authentication SQL injection vulnerability in Metabase business intelligence software that allows unauthenticated attackers to execute arbitrary SQL queries against the backend database.
- **Impact**: Full database access leading to customer data theft, including sensitive business analytics, user credentials, and proprietary information. Confirmed breaches at Framework and Tally.
- **Status**: Actively exploited in the wild as a zero-day. Patches or mitigations should be applied immediately. No CVE ID was provided in the source reporting.

### Malicious npm Supply Chain Campaign
- **Description**: A cluster of nearly 800 malicious packages published to the npm registry designed to deliver cross-platform malware. The packages target developers and build systems across Windows, macOS, and Linux.
- **Impact**: Remote access trojan (RAT) and infostealer deployment, leading to credential theft, cryptocurrency wallet drainage, system compromise, and potential lateral movement in development environments.
- **Status**: Active campaign with packages distributed via the official npm registry. Organizations should audit dependencies and implement supply chain security controls.

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks that trick macOS users into executing malicious commands, delivering a Go-based infostealer payload.
- **Impact**: Theft of cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials. Targets both individual users and potentially enterprise macOS environments.
- **Status**: Actively deployed in ongoing campaigns. No CVE ID involved as this is a social engineering technique rather than a software vulnerability.

### UNC6671 Vishing and Data Extortion Campaign
- **Description**: A data extortion group conducting voice phishing (vishing) attacks against personal phones of employees at financial services, private equity, hedge funds, and professional services firms to gain initial access to SaaS environments.
- **Impact**: Unauthorized access to SaaS data, data exfiltration, and extortion demands. Linked to the BlackFile threat ecosystem.
- **Status**: Active wave of attacks reported across multiple financial sector verticals. Attribution to UNC6671 with BlackFile association.

### Snowflake Extortion Campaign
- **Description**: Large-scale compromise of Snowflake cloud data warehouse instances across more than 165 organizations, followed by data theft and extortion demands.
- **Impact**: Massive data exposure affecting numerous enterprises, with stolen data used for extortion. One of the most consequential cybercrime campaigns of 2024.
- **Status**: Canadian threat actor (26-year-old) pleaded guilty to computer fraud and conspiracy charges. Campaign activity appears disrupted by law enforcement action.

### Swiss Government SharePoint Breach
- **Description**: Exploitation of vulnerabilities in Microsoft SharePoint servers operated by Switzerland's federal IT office.
- **Impact**: Compromise of approximately 200 accounts within Swiss government infrastructure.
- **Status**: Confirmed breach by federal IT office. Specific vulnerabilities exploited not disclosed in public reporting.

### North Carolina Ports Cyberattack
- **Description**: Cyberattack disrupting IT systems and operations at Port of Wilmington, Port of Morehead City, and Charlotte Inland Port.
- **Impact**: Operational slowdown at critical maritime infrastructure, IT system disruption.
- **Status**: Confirmed by North Carolina Ports Authority. Attack vector and attribution not publicly disclosed.

### Levi Strauss Social Engineering Attack
- **Description**: Social engineering attacks targeting three employees to gain access to corporate data stored on their machines.
- **Impact**: Theft of corporate data from compromised employee systems.
- **Status**: Confirmed by Levi Strauss & Co. No technical vulnerability exploited; pure social engineering.

## Affected Systems and Products

- **Metabase Business Intelligence Platform**: All versions prior to patched release; exploited at Framework and Tally customer instances
- **npm Registry / Node.js Ecosystem**: Nearly 800 malicious packages affecting Windows, macOS, and Linux development environments
- **macOS Systems**: Targeted via ClickFix social engineering for infostealer deployment (cryptocurrency wallets, browsers, Keychain)
- **Microsoft SharePoint**: Swiss federal government instances compromised (~200 accounts)
- **Snowflake Cloud Data Warehouse**: 165+ organizations compromised in extortion campaign
- **Microsoft 365 / Entra ID**: Targeted by AitM phishing campaigns harvesting payroll and finance emails; Windows Hello for Business keys abused for persistent access
- **Cisco Catalyst SD-WAN and IOS XE Software**: 12 vulnerabilities patched (three 9.9 CVSS), though active exploitation not confirmed
- **WordPress CMS**: All versions affected by pre-authentication reflected XSS in login screen (potential PHP code execution chain demonstrated)
- **Linux Kernel**: Multiple flaws including 18-year-old SCTP use-after-free (local root + container escape), Zapscape KVM escape (L1 guest to host), and TONTOU CPU side-channel bypassing Spectre v2 mitigations
- **Apache HTTP Server**: Zero-day discovered via AI-assisted HTTP desynchronization research
- **Anthropic Claude Code, Google Gemini CLI, OpenAI Codex**: CI/CD workflow secret exposure via GitHub issue interaction flaws
- **Redis Instances**: Internet-facing infrastructure compromised by TeamPCP since 2020
- **North Carolina Ports IT Systems**: Operational technology and IT infrastructure at three port facilities
- **Levi Strauss Employee Endpoints**: Corporate data stolen from three compromised employee machines

## Attack Vectors and Techniques

- **SQL Injection (Pre-Authentication)**: Metabase zero-day allowing unauthenticated database query execution
- **Software Supply Chain Compromise**: Malicious npm packages masquerading as legitimate dependencies delivering cross-platform RAT/infostealer
- **ClickFix Social Engineering**: User-interaction-based technique tricking victims into executing malicious commands via fake error pages or verification prompts
- **Voice Phishing (Vishing)**: UNC6671 calling personal phones to social engineer credentials or MFA approval for SaaS access
- **Adversary-in-the-Middle (AitM) Phishing**: Real-time proxy phishing capturing Microsoft 365 session tokens and credentials targeting payroll/finance emails
- **NAT Table Manipulation (NatJack)**: Exploiting NAT connection state to hijack active TCP sessions and spoof DNS responses
- **HTTP Request Smuggling / Desynchronization**: Novel AI-discovered techniques for request smuggling leading to Apache zero-day
- **Windows Hello for Business Key Abuse**: Malware leveraging signed-in user's hardware-bound keys for persistent Entra ID authentication
- **GitHub Issue CI/CD Injection**: Low-privilege GitHub issues triggering code execution on CI runners in AI coding agent repositories
- **Redis Exploitation**: Long-running compromise of internet-facing Redis instances for infrastructure access
- **Container Escape via Kernel Flaws**: Linux SCTP use-after-free and Zapscape KVM vulnerabilities enabling host escape from containers/VMs
- **CPU Side-Channel (TONTOU)**: Bypassing Spectre v2 mitigations to leak Linux password hashes and secrets
- **Clipboard Hijacking**: Banking malware campaign manipulating clipboard content for payment diversion
- **Browser Manipulation**: Compromised business inboxes used with browser manipulation for financial fraud
- **Cross-Site Scripting (Pre-Auth Reflected)**: WordPress login screen XSS with demonstrated PHP code execution chain

## Threat Actor Activities

- **UNC6671 / BlackFile-Linked Extortion Group**: Active vishing campaign targeting financial services, hedge funds, private equity, and professional services. Uses voice phishing against personal phones for initial SaaS access, followed by data theft and extortion. Confirmed in multiple reporting sources.
- **TeamPCP**: Long-running threat actor compromising internet-facing Redis instances since at least 2020, later expanding to supply chain campaigns. Demonstrates persistence and evolution from opportunistic infrastructure targeting to software supply chain attacks.
- **Canadian Snowflake Extortion Actor**: 26-year-old individual described as one of 2024's most consequential cybercrime actors. Pleaded guilty to compromising and extorting 165+ organizations via Snowflake cloud data warehouse attacks.
- **ClickFix Operators**: Ongoing campaigns delivering macOS infostealers (Go-based) for cryptocurrency theft and credential harvesting. Technique adopted by multiple threat groups.
- **Malicious npm Publishers**: Coordinated campaign publishing nearly 800 packages to npm registry. Attribution not specified; likely financially motivated cybercrime group.
- **Metabase Zero-Day Exploiters**: Unknown actors exploiting critical SQLi in Metabase instances at Framework and Tally for data theft. Sophistication suggests targeted operation.
- **Microsoft 365 AitM Phishing Operators**: Widespread email-driven campaign using adversary-in-the-middle infrastructure to hijack accounts and harvest payroll/finance communications.

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
