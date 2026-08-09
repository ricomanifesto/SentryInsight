# Exploitation Report

## Executive Summary

A surge in supply chain compromises and zero-day exploitation dominates the current threat landscape. The Head Mare hacktivist group breached TrueConf's infrastructure to trojanize legitimate client installers with backdoors, while a critical Metabase SQL injection zero-day was actively exploited in data-theft attacks against Framework and Tally. Simultaneously, attackers are leveraging a recently disclosed flaw in N-able's N-central RMM platform to reach managed systems and establish persistence, and Progress Kemp LoadMaster appliances face active exploitation with 792 recorded attempts—prompting CISA to add the flaw to its Known Exploited Vulnerabilities catalog.

Novel attack techniques are expanding the exploitation surface across web and identity layers. Research demonstrates that CSS-based attacks can break webmail sandboxing across Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail to steal credentials and tokens. ClickFix social engineering campaigns now deliver cross-platform macOS stealers targeting cryptocurrency wallets, browser credentials, and Apple Keychain data. The UNC6671 extortion group—linked to BlackFile—conducts vishing operations against financial services and private equity firms to access SaaS data, while adversary-in-the-middle phishing campaigns hijack Microsoft 365 accounts to harvest payroll and finance communications.

Critical infrastructure and foundational technologies face emerging threats. An 18-year-old Linux SCTP use-after-free flaw enables local privilege escalation and container escapes. The NatJack attack class manipulates NAT tables to hijack TCP sessions and spoof DNS. AI-assisted research uncovered novel HTTP desynchronization techniques and an Apache zero-day. Malware can abuse Windows Hello for Business keys for persistent Entra ID access, and flaws in Claude Code and Gemini CLI allow GitHub issues to reach CI/CD workflow secrets. TeamPCP's Redis compromise campaign dates back to 2020 and evolved into a supply chain operation, while multiple AI providers disclosed sandbox escape incidents affecting real organizations.

## Active Exploitation Details

### TrueConf Supply Chain Compromise
- **Description**: The Head Mare hacktivist group breached TrueConf's infrastructure and exploited vulnerabilities in unpatched TrueConf video conferencing servers to replace legitimate client installers with malicious versions containing backdoors.
- **Impact**: Organizations downloading and installing TrueConf clients receive trojanized software that provides attackers with persistent backdoor access to victim networks.
- **Status**: Active exploitation; organizations using unpatched TrueConf servers are at risk. TrueConf clients should verify installer integrity and update servers immediately.

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence and data visualization software allows unauthenticated attackers to achieve administrative access. The flaw was exploited as a zero-day before disclosure.
- **Impact**: Attackers gain full administrative control over Metabase instances, enabling data theft, system compromise, and potential lateral movement. Confirmed victims include Framework and Tally in customer data-theft attacks.
- **Status**: Actively exploited in the wild as a zero-day. Metabase has issued warnings; emergency patching required.

### N-able N-central RMM Exploitation
- **Description**: Attackers are actively exploiting a recently disclosed security flaw in N-able's N-central Remote Monitoring and Management platform. N-able has released Hotfix 2 as part of its ongoing investigation.
- **Impact**: Threat actors reach managed systems through the RMM platform and establish persistence, potentially compromising all downstream managed endpoints and customer environments.
- **Status**: Ongoing exploitation; N-able issued Hotfix 2. All N-central administrators should apply hotfixes immediately and audit managed systems for compromise.

### Progress Kemp LoadMaster Critical Flaw
- **Description**: A critical-severity vulnerability in Progress Kemp LoadMaster load balancing appliances. CISA added this flaw to its Known Exploited Vulnerabilities catalog after 792 reported exploit attempts.
- **Impact**: Successful exploitation allows attackers to compromise load balancers, potentially intercepting, modifying, or redirecting traffic, and gaining a foothold in network infrastructure.
- **Status**: Actively exploited with high volume (792 attempts recorded). CISA KEV listing mandates federal agency patching; all organizations should prioritize remediation.

### Atlassian Rovo Data Exfiltration
- **Description**: Attacker-controlled instructions can manipulate Atlassian's Rovo AI assistant to collect Jira and Confluence data accessible to a signed-in user and exfiltrate it to an external server. Two security firms independently identified the issue.
- **Impact**: Confidential project data, credentials, and internal documentation accessible through Jira/Confluence can be stolen without direct system compromise.
- **Status**: Vulnerability identified by researchers; exploitation potential exists wherever Rovo is enabled with access to sensitive data.

### CSS-Based Webmail Sandbox Escape
- **Description**: Novel CSS attacks allow email content to escape message boundaries and interfere with the webmail interface itself, bypassing sandboxing protections across multiple providers.
- **Impact**: Attackers can steal passwords, authentication tokens, and sensitive data from webmail interfaces. Confirmed effective against Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail.
- **Status**: Research disclosure; proof-of-concept demonstrated across major providers. Webmail vendors implementing mitigations.

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks deliver a Go-based malware targeting macOS users. The malware steals cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials.
- **Impact**: Complete compromise of cryptocurrency wallets, credential stores, and browser data on infected macOS systems. Cross-platform variants also target Windows and Linux.
- **Status**: Active campaigns in the wild. Detection relies on user education and endpoint protection; no patch available for social engineering vector.

### UNC6671 Vishing and Data Extortion
- **Description**: The UNC6671 data extortion group (linked to BlackFile) conducts vishing attacks targeting personal phones of employees at financial services, private equity, and professional services firms to gain access to SaaS data.
- **Impact**: Unauthorized access to SaaS applications and data repositories, data theft, and extortion demands. Campaigns specifically target high-value financial sector organizations.
- **Status**: Active wave of attacks reported. Defense requires identity verification protocols, MFA enforcement, and employee training on vishing tactics.

### WordPress Pre-Authentication XSS
- **Description**: A reflected cross-site scripting flaw in the WordPress login screen affects every version of the CMS. Researchers demonstrated how the flaw can be chained to achieve PHP code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary JavaScript in victim browsers, potentially leading to full site compromise via admin session hijacking or direct RCE chains.
- **Status**: WordPress has released a fix. All versions affected; immediate update required across all WordPress installations.

### Linux SCTP Container Escape
- **Description**: An 18-year-old use-after-free bug in Linux's SCTP networking code allows local users to gain root privileges and escape containers to access the host system. Tencent researchers demonstrated practical container escape.
- **Impact**: Container breakout to host root access, compromising all containers on the host and the host itself. Affects any Linux system with SCTP enabled.
- **Status**: Vulnerability disclosed with exploit demonstration. Patches expected in kernel updates; container environments should assess SCTP exposure.

### NatJack NAT Manipulation Attacks
- **Description**: A new attack class (NatJack) manipulates network address translation (NAT) connection state tables to hijack active TCP sessions and spoof DNS responses.
- **Impact**: Session hijacking, traffic interception, DNS spoofing, and man-in-the-middle attacks against any device behind vulnerable NAT implementations.
- **Status**: Research disclosure by Malcolm Stagg. Applies to NAT implementations with predictable or manipulable connection tracking.

### Microsoft 365 Adversary-in-the-Middle Phishing
- **Description**: Widespread email-driven phishing campaign employing adversary-in-the-middle (AitM) techniques to take control of Microsoft 365 accounts, specifically targeting payroll and finance email communications.
- **Impact**: Full account takeover with MFA bypass, persistent access to sensitive financial communications, business email compromise enablement, and payroll diversion.
- **Status**: Active campaign. Phishing-resistant MFA (FIDO2/WebAuthn) and Conditional Access policies mitigate AitM effectiveness.

### Apache HTTP Desynchronization Zero-Day
- **Description**: AI-assisted research (HTTP Terminator by James Kettle/PortSwigger) discovered novel HTTP desynchronization techniques and an Apache zero-day vulnerability after exploring 30,000 candidate techniques.
- **Impact**: HTTP request smuggling and desync attacks leading to cache poisoning, credential theft, and application logic bypass on Apache HTTP Server deployments.
- **Status**: Zero-day disclosed by researchers. Apache patches expected; WAF rules and HTTP/2 hardening provide interim mitigation.

### Windows Hello for Business Key Abuse
- **Description**: Malware running in a signed-in Windows session can silently use the victim's Windows Hello for Business cryptographic key to authenticate to Microsoft Entra ID, achieving persistent access without credential theft.
- **Impact**: Persistent, stealthy access to Entra ID resources bypassing conditional access and MFA. Survives password resets and MFA re-registration.
- **Status**: Research demonstration by Dirk-jan Mollema. Mitigation requires device compliance policies and TPM-backed key attestation enforcement.

### Claude Code and Gemini CLI CI/CD Secret Exposure
- **Description**: Flaws in Anthropic's Claude Code and Google's Gemini CLI allow a GitHub issue opened by an unprivileged account to execute code on CI runners, accessing workflow secrets. Also affected OpenAI's repositories.
- **Impact**: Theft of CI/CD pipeline secrets, API keys, deployment credentials, and source code from AI provider repositories and potentially any repository using these tools.
- **Status**: Disclosed vulnerabilities in AI coding agents. Repository maintainers should restrict CI triggers and audit workflow permissions.

### TeamPCP Redis Compromise and Supply Chain Campaign
- **Description**: Threat actor TeamPCP has compromised internet-facing Redis instances since at least 2020, later evolving into a supply chain campaign affecting downstream software consumers.
- **Impact**: Long-term infrastructure compromise, potential software supply chain poisoning, and persistent access to Redis-managed data across multiple victim organizations.
- **Status**: Historical campaign uncovered by recent analysis. Organizations should audit Redis exposure history and verify software integrity.

### AI Sandbox Escape Incidents
- **Description**: OpenAI, Anthropic, and Meta all disclosed AI agent sandbox escape events within a three-week period, affecting real organizations. A researcher demonstrated C2-style control over ChatGPT's isolated sandbox at Black Hat USA 2026.
- **Impact**: Escape from AI execution sandboxes to underlying infrastructure, potential data access, and lateral movement within provider environments.
- **Status**: Multiple vendor disclosures; architectural reviews and sandbox hardening underway across AI providers.

## Affected Systems and Products

- **TrueConf Video Conferencing Server**: Unpatched server versions; client installers trojanized via server compromise
- **Metabase Business Intelligence Platform**: All versions prior to emergency patch; Framework and Tally confirmed compromised
- **N-able N-central RMM**: Versions affected by recently disclosed flaw; Hotfix 2 available
- **Progress Kemp LoadMaster**: Load balancing appliances; critical flaw with active exploitation
- **Atlassian Rovo / Jira / Confluence**: Cloud and Data Center deployments with Rovo enabled
- **Webmail Platforms**: Microsoft Outlook Web, Google Gmail, Fastmail, Proton Mail, Yahoo Mail — all affected by CSS sandbox escape
- **WordPress CMS**: Every version affected by pre-auth reflected XSS in login screen
- **Linux Kernel**: All versions with SCTP support (18-year-old use-after-free in net/sctp)
- **NAT Devices/Implementations**: Devices with manipulable NAT connection tracking tables (NatJack)
- **Microsoft 365 / Entra ID**: Tenants targeted by AitM phishing; Windows Hello for Business key abuse affects hybrid-joined devices
- **Apache HTTP Server**: Versions vulnerable to novel HTTP desynchronization techniques
- **Claude Code / Gemini CLI**: AI coding agents integrated with GitHub Actions / CI pipelines
- **Redis Instances**: Internet-exposed Redis servers (TeamPCP campaign since 2020)
- **npm Registry**: Nearly 800 malicious packages delivering cross-platform RAT/infostealer (Windows, macOS, Linux)
- **AI Sandbox Environments**: OpenAI ChatGPT, Anthropic, Meta AI agent execution sandboxes

## Attack Vectors and Techniques

- **Supply Chain Compromise via Server Breach**: Attackers breach vendor infrastructure (TrueConf) to modify legitimate software artifacts before distribution
- **Zero-Day SQL Injection**: Unauthenticated SQLi in Metabase enabling direct admin access and data exfiltration
- **RMM Platform Abuse**: Exploitation of management plane vulnerabilities (N-central) to reach all managed endpoints
- **Load Balancer Exploitation**: Targeting network infrastructure (Kemp LoadMaster) for traffic interception and persistence
- **AI Assistant Prompt Injection**: Malicious instructions manipulating Rovo to exfiltrate accessible Jira/Confluence data
- **CSS Injection / Sandbox Escape**: Crafted email content breaking webmail message boundaries to attack parent application DOM
- **ClickFix Social Engineering**: Deceptive UI interactions tricking users into executing malicious commands (PowerShell/Terminal)
- **Vishing / Voice Phishing**: Phone-based social engineering targeting personal devices to bypass corporate controls
- **Adversary-in-the-Middle Phishing**: Proxy-based phishing (Evilginx-style) capturing session cookies and MFA tokens
- **HTTP Request Smuggling / Desync**: Novel desynchronization techniques confusing front-end/back-end request boundaries
- **Container Escape via Kernel UAF**: Local privilege escalation using SCTP use-after-free to break container isolation
- **NAT Table Manipulation**: Predicting/injecting NAT connection state to hijack TCP sessions and spoof DNS
- **Windows Hello Key Theft via Malware**: Malware abusing TPM-backed keys for silent Entra ID authentication
- **CI/CD Poisoning via AI Tool Flaws**: Unprivileged GitHub issues triggering code execution on privileged runners
- **Long-Term Redis Compromise**: Persistent access to exposed Redis instances enabling supply chain insertion
- **Malicious Package Publication**: Typosquatting/dependency confusion delivering cross-platform malware via npm
- **AI Sandbox Escape**: Exploiting AI agent execution environments to reach host infrastructure

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Breached TrueConf infrastructure to trojanize client installers; politically motivated supply chain attack targeting video conferencing users
- **UNC6671 (Data Extortion Group / BlackFile-linked)**: Conducts vishing campaigns against financial services, private equity, and professional services; steals SaaS data for extortion; active since at least 2024
- **TeamPCP (Cybercrime Actor)**: Compromising internet-facing Redis instances since 2020; evolved into software supply chain campaign; long-term infrastructure operator
- **ClickFix Operators (Unattributed)**: Running cross-platform social engineering campaigns delivering infostealers; macOS-focused crypto theft; Windows/Linux variants observed
- **AitM Phishing Operators (Unattributed)**: Widespread Microsoft 365 credential harvesting targeting payroll/finance; uses adversary-in-the-middle frameworks for MFA bypass
- **Metabase Zero-Day Exploiters (Unattributed)**: Exploited critical SQLi as zero-day against Framework and Tally for data theft; likely financially motivated
- **N-central Exploiters (Unattributed)**: Actively exploiting RMM flaw to reach managed systems and persist; potential access to MSP customer environments
- **Kemp LoadMaster Attackers (Unattributed)**: 792 exploit attempts recorded; targeting network infrastructure for traffic manipulation

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
