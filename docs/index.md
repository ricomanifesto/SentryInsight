# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with several critical zero-day vulnerabilities under active attack in the wild. The most severe activity centers on a maximum-severity SQL injection flaw in Metabase business intelligence software, which has been exploited as a zero-day to achieve unauthenticated administrative access and exfiltrate customer data from organizations including Framework and Tally. Simultaneously, a critical Progress Kemp LoadMaster vulnerability has been added to CISA's Known Exploited Vulnerabilities catalog following 792 reported exploit attempts, while attackers continue to leverage a recently disclosed flaw in N-able N-central RMM software to reach managed systems and establish persistence across downstream environments.

Threat actors are diversifying their initial access techniques beyond traditional vulnerability exploitation. The Head Mare hacktivist group has compromised TrueConf video conferencing servers to trojanize client installers with backdoors, representing a software supply chain attack. UNC6671, a data extortion group, is conducting vishing campaigns targeting personal phones of employees in financial services, private equity, and professional services to steal SaaS credentials. A widespread adversary-in-the-middle phishing campaign is hijacking Microsoft 365 accounts to harvest payroll and finance emails, while ClickFix social engineering attacks deliver cross-platform infostealers targeting cryptocurrency wallets and credential stores on macOS.

New attack research reveals expanding threat surfaces in web applications and infrastructure. CSS-based attacks can now break webmail defenses across major providers including Outlook, Gmail, and Proton Mail to steal passwords and tokens. The NatJack technique manipulates NAT connection state to hijack TCP sessions and spoof DNS responses. AI-assisted research has uncovered novel HTTP desynchronization techniques and an Apache zero-day, while malware demonstrates the ability to abuse Windows Hello for Business keys for persistent Entra ID access. A cluster of nearly 800 malicious npm packages delivers cross-platform remote access trojans and infostealers, and CI/CD pipeline vulnerabilities in Claude Code and Gemini CLI allow GitHub issues to reach workflow secrets.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A maximum-severity SQL injection vulnerability in Metabase business intelligence and data visualization software allows unauthenticated attackers to achieve administrative access. The flaw resides in the application's database query handling and can be exploited without any prior authentication.
- **Impact**: Attackers gain full administrative control over Metabase instances, enabling complete access to connected databases, customer data exfiltration, and potential lateral movement within compromised environments. Confirmed data theft attacks have impacted Framework and Tally.
- **Status**: Actively exploited in the wild as a zero-day. Metabase has issued warnings and patches; immediate updating is critical for all exposed instances.
- **CVE ID**: CVE-2025-XXXX (referenced in source articles as a zero-day exploited in wild)

### Progress Kemp LoadMaster Critical Flaw
- **Description**: A critical-severity security flaw affecting Progress Kemp LoadMaster application delivery controllers and load balancers. The vulnerability allows remote attackers to execute arbitrary code or gain unauthorized access to the management interface.
- **Impact**: Full compromise of load balancer appliances, potential traffic interception, credential theft, and network pivoting. The flaw's presence on internet-facing infrastructure makes it highly attractive for initial access.
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog after 792 reported exploit attempts. Patches available; federal agencies required to remediate per binding operational directive.
- **CVE ID**: CVE-2025-XXXX (added to CISA KEV catalog)

### N-able N-central RMM Exploitation
- **Description**: A recently disclosed security flaw in N-able N-central Remote Monitoring and Management (RMM) platform is being actively exploited by threat actors to access managed systems and establish persistence.
- **Impact**: Attackers leveraging RMM access can reach all downstream managed endpoints, deploy malware, exfiltrate data, and maintain persistent access across customer environments. The trusted nature of RMM tools makes detection difficult.
- **Status**: Ongoing exploitation campaign. N-able has released Hotfix 2 as part of continued investigation and response. All N-central administrators should apply updates immediately and audit for signs of compromise.
- **CVE ID**: CVE-2025-XXXX (referenced as recently disclosed flaw under active exploitation)

### TrueConf Supply Chain Compromise
- **Description**: The Head Mare hacktivist group exploited vulnerabilities in unpatched TrueConf video conferencing servers to gain access to the software distribution infrastructure. Attackers replaced legitimate client installers with trojanized versions containing backdoors.
- **Impact**: Organizations downloading and installing TrueConf clients received malicious software granting attackers persistent remote access. The supply chain nature means compromise occurs at installation time, bypassing many perimeter defenses.
- **Status**: Active campaign by Head Mare group. TrueConf has been notified; organizations using TrueConf should verify installer integrity and reinstall from trusted sources after patching servers.
- **CVE ID**: CVE-2025-XXXX (vulnerabilities in unpatched TrueConf servers exploited)

### Microsoft 365 Adversary-in-the-Middle Phishing Campaign
- **Description**: A widespread, active email-driven phishing campaign employs adversary-in-the-middle (AitM) techniques using reverse proxy phishing kits to intercept authentication tokens and bypass multi-factor authentication for Microsoft 365 accounts.
- **Impact**: Attackers gain full control of compromised Microsoft 365 accounts with persistent access via stolen session tokens. Campaign specifically targets payroll and finance emails for business email compromise and financial fraud.
- **Status**: Active and widespread. Traditional MFA is bypassed; phishing-resistant authentication (FIDO2, certificate-based) required for effective mitigation.
- **CVE ID**: N/A (technique-based exploitation, not a single CVE)

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks trick macOS users into executing malicious commands via fake verification prompts (e.g., "I'm not a robot" CAPTCHA pages). The delivered Go-based malware steals cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials.
- **Impact**: Complete credential theft from macOS keychains and browsers, cryptocurrency wallet drainage, and persistent access to victim's online identities. Cross-platform variants also target Windows and Linux.
- **Status**: Active campaign with ongoing delivery infrastructure. Relies on social engineering rather than vulnerability exploitation; user awareness and endpoint detection critical.

### UNC6671 Vishing and Data Extortion
- **Description**: Data extortion group UNC6671 conducts voice phishing (vishing) attacks targeting personal phone numbers of employees in financial services, private equity, and professional services firms. Attackers impersonate IT support to steal SaaS credentials and MFA codes.
- **Impact**: Access to SaaS applications (Salesforce, Slack, GitHub, etc.), intellectual property theft, data exfiltration for extortion, and potential supply chain compromise through compromised vendor accounts.
- **Status**: Active campaign with evolving tactics. Personal phone targeting bypasses corporate security controls; requires identity-focused defenses and employee training on vishing.

### Malicious npm Supply Chain Campaign
- **Description**: Nearly 800 malicious packages published to the npm registry as part of a coordinated campaign delivering cross-platform remote access trojans (RATs) and infostealers targeting Windows, macOS, and Linux systems.
- **Impact**: Developers and build systems installing compromised packages execute malware with full system privileges. Potential for widespread compromise through dependency chains, CI/CD poisoning, and persistent access to development environments.
- **Status**: Active campaign; packages identified and removal underway. Organizations should audit npm dependencies, verify package integrity, and monitor for indicators of compromise.

## Affected Systems and Products

- **Metabase Business Intelligence Platform**: All versions prior to security patch; business intelligence and data visualization software used for database querying and dashboarding
- **Progress Kemp LoadMaster**: Application delivery controllers and load balancers (virtual and hardware appliances); internet-facing management interfaces at highest risk
- **N-able N-central RMM**: Remote Monitoring and Management platform used by MSPs and IT departments; all managed endpoints downstream of compromised N-central servers
- **TrueConf Video Conferencing Server**: On-premises video conferencing servers; client installers distributed from compromised servers
- **Microsoft 365 / Entra ID**: Cloud identity and productivity suite; accounts targeted via AitM phishing with session token theft
- **macOS Systems**: Apple macOS endpoints targeted by ClickFix social engineering delivering Go-based infostealers (cross-platform variants affect Windows/Linux)
- **npm Registry / Node.js Ecosystem**: JavaScript package registry; nearly 800 malicious packages affecting development environments and build pipelines
- **Atlassian Rovo / Jira / Confluence**: Atlassian's AI assistant Rovo and connected Jira/Confluence instances; data exfiltration via prompt injection
- **Major Webmail Providers**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail; vulnerable to CSS-based boundary escape attacks
- **WordPress CMS**: All versions affected by pre-authentication reflected XSS in login screen; potential PHP code execution chain demonstrated
- **Linux Kernel (SCTP Subsystem)**: 18-year-old use-after-free in Stream Control Transmission Protocol; container escape to host root demonstrated
- **Apache HTTP Server**: Zero-day discovered via AI-assisted HTTP desynchronization research; details pending coordinated disclosure
- **Windows Hello for Business / Entra ID**: Enterprise authentication system; malware can abuse WHfB keys for persistent cloud identity access
- **Claude Code / Gemini CLI**: AI coding agents; CI/CD workflow secret exposure via GitHub issue interactions
- **Redis Instances**: Internet-facing Redis servers compromised by TeamPCP since 2020; used for supply chain campaigns

## Attack Vectors and Techniques

- **SQL Injection (Zero-Day)**: Unauthenticated database query manipulation in Metabase leading to administrative bypass and data exfiltration
- **Supply Chain Compromise (Software Distribution)**: Server compromise → installer trojanization → client infection (TrueConf/Head Mare)
- **Adversary-in-the-Middle (AitM) Phishing**: Reverse proxy phishing kits intercepting MFA tokens and session cookies for Microsoft 365
- **ClickFix Social Engineering**: Fake verification prompts (CAPTCHA, "verify you're human") tricking users into executing malicious PowerShell/terminal commands
- **Voice Phishing (Vishing)**: Phone-based social engineering targeting personal devices to steal SaaS credentials and MFA approvals
- **Malicious Package Publishing (Typosquatting/Supply Chain)**: Bulk publication of malware-laden npm packages targeting developer workflows
- **Prompt Injection / AI Assistant Abuse**: Attacker-controlled instructions exfiltrating data via Atlassian Rovo AI assistant
- **CSS Injection / Boundary Escape**: Email content escaping message boundaries to manipulate webmail DOM and exfiltrate credentials/tokens
- **NAT State Manipulation (NatJack)**: Manipulating NAT connection tracking tables to hijack TCP sessions and spoof DNS responses
- **HTTP Request Smuggling / Desynchronization**: AI-discovered novel techniques for request smuggling affecting Apache and other servers
- **Windows Hello for Business Key Abuse**: Malware leveraging WHfB private keys for silent Entra ID authentication and persistence
- **CI/CD Pipeline Poisoning**: Low-privilege GitHub issues triggering code execution on CI runners to access workflow secrets
- **Container Escape via Kernel Flaw**: Linux SCTP use-after-free enabling root privilege escalation and container breakout
- **Pre-Auth XSS to RCE Chain**: WordPress login screen reflected XSS chained to PHP code execution via researcher demonstration
- **RMM/Lateral Movement**: Exploited RMM platforms used to deploy payloads across managed endpoint fleets

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Active compromise of TrueConf servers for supply chain trojanization; politically motivated targeting with backdoored installers
- **UNC6671 (Data Extortion Group)**: Vishing campaigns targeting financial services, private equity, and professional services; personal phone targeting to bypass corporate controls; SaaS credential theft for data extortion
- **TeamPCP (Cybercrime Actor)**: Redis server compromise campaigns dating back to 2020; evolved into supply chain attacks; persistent infrastructure compromise
- **ClickFix Operators (Unattributed)**: Ongoing social engineering campaigns delivering cross-platform infostealers; cryptocurrency-focused; macOS, Windows, and Linux variants
- **AitM Phishing Operators (Unattributed)**: Widespread Microsoft 365 credential harvesting campaign; finance/payroll email targeting; phishing kit infrastructure
- **Malicious npm Campaign Operators (Unattributed)**: Coordinated publication of ~800 packages; cross-platform RAT/infostealer delivery; developer supply chain targeting
- **Metabase Zero-Day Exploiters (Unattributed)**: Active exploitation for data theft; confirmed victims include Framework and Tally; likely financially motivated
- **Kemp LoadMaster Exploiters (Unattributed)**: 792+ exploit attempts recorded; automated scanning and exploitation; opportunistic targeting of internet-facing appliances
- **N-central Exploiters (Unattributed)**: Ongoing access to managed systems via RMM; persistence establishment; likely MSP-focused threat actor

## Source Attribution

- **OpenAI's Next AI Model Astra Shows Cyber Performance Strong Enough to Trigger Pause**: The Hacker News - https://thehackernews.com/2026/08/openais-next-ai-model-astra-shows-cyber.html
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
