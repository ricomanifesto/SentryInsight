# Exploitation Report

## Executive Summary

A critical Metabase SQL injection zero-day vulnerability has been actively exploited in targeted data theft attacks against customer instances, with confirmed breaches at Framework and Tally. This zero-day exploitation represents the most immediate risk, as attackers leveraged the flaw to exfiltrate sensitive customer data before patches were available. Organizations running Metabase instances should prioritize emergency patching and conduct immediate compromise assessments.

Supply chain attacks have surged with the discovery of nearly 800 malicious npm packages delivering cross-platform remote access trojans and infostealers targeting Windows, macOS, and Linux systems. Simultaneously, the TeamPCP threat actor has been linked to Redis compromise campaigns dating back to 2020, evolving into sophisticated supply chain operations. These campaigns demonstrate the increasing maturity of software supply chain attacks as a primary initial access vector.

Social engineering and identity-focused attacks remain dominant, with ClickFix-style attacks delivering Go-based macOS infostealers that drain cryptocurrency wallets and harvest browser credentials, iCloud Keychain data, and cached credentials. The UNC6671 extortion group—linked to BlackFile—has intensified vishing campaigns targeting financial services, private equity, and professional services firms, using voice phishing against personal phones to steal SaaS credentials. Microsoft 365 adversary-in-the-middle phishing campaigns are simultaneously hijacking accounts to harvest payroll and finance emails at scale.

## Active Exploitation Details

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence software that allows unauthenticated attackers to execute arbitrary SQL commands on the backend database. The flaw was exploited as a zero-day before public disclosure.
- **Impact**: Full database access enabling customer data theft, potential privilege escalation, and lateral movement within compromised environments. Confirmed breaches resulted in exfiltration of sensitive customer data from Framework and Tally instances.
- **Status**: Actively exploited in the wild as a zero-day. Patches have been released following coordinated disclosure by Framework and Tally. Organizations must apply updates immediately and investigate for signs of compromise.

### Malicious npm Package Supply Chain Campaign
- **Description**: A cluster of nearly 800 malicious packages published to the npm registry as part of a coordinated campaign delivering cross-platform malware. The packages target developers and build systems across Windows, macOS, and Linux.
- **Impact**: Remote access trojan (RAT) capabilities and infostealer functionality enabling credential theft, cryptocurrency wallet drainage, system enumeration, and persistent access to development environments and CI/CD pipelines.
- **Status**: Active campaign with packages identified and removal underway. Developers and organizations must audit dependency trees, rotate compromised credentials, and scan build artifacts for indicators of compromise.

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks tricking macOS users into executing malicious commands that deploy a Go-based infostealer. The malware specifically targets cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials.
- **Impact**: Complete compromise of user credentials, cryptocurrency wallet theft, browser session hijacking, and potential access to iCloud-synced data across Apple devices.
- **Status**: Active exploitation targeting macOS users. No patch available as this is a social engineering technique; mitigation requires user awareness training and endpoint detection capabilities.

### UNC6671 Vishing and Data Extortion Campaign
- **Description**: Voice phishing (vishing) attacks targeting personal phone numbers of employees at financial services, private equity, and professional services firms. Attackers impersonate IT support to steal SaaS credentials and access sensitive data for extortion.
- **Impact**: Unauthorized access to SaaS platforms (Microsoft 365, Salesforce, etc.), data exfiltration for extortion, business email compromise, and potential regulatory violations from exposed financial and client data.
- **Status**: Active campaign attributed to UNC6671, an extortion group linked to BlackFile. Ongoing targeting of hedge funds and financial organizations.

### Microsoft 365 Adversary-in-the-Middle Phishing
- **Description**: Widespread email-driven phishing campaign employing adversary-in-the-middle (AitM) techniques to bypass multi-factor authentication and hijack Microsoft 365 accounts. Attackers use proxy infrastructure to capture session tokens in real-time.
- **Impact**: Full account takeover with persistent access, targeted collection of payroll and finance emails for business email compromise and financial fraud, potential lateral movement to connected services.
- **Status**: Active, widespread campaign. Standard MFA is bypassed; phishing-resistant authentication (FIDO2, certificate-based) required for effective mitigation.

### Swiss Government SharePoint Exploitation
- **Description**: Hackers exploited vulnerabilities in Microsoft SharePoint servers operated by Switzerland's federal IT office, compromising approximately 200 accounts.
- **Impact**: Unauthorized access to government SharePoint environments, potential exposure of sensitive federal data, credential theft enabling further lateral movement.
- **Status**: Breach confirmed; specific vulnerabilities exploited not publicly disclosed. Swiss federal IT office conducting investigation and remediation.

### North Carolina Ports Cyberattack
- **Description**: Cyberattack disrupting IT systems and operations at the North Carolina Ports Authority, affecting Port of Wilmington, Port of Morehead City, and Charlotte Inland Port.
- **Impact**: Operational disruption to critical port infrastructure, slowed cargo operations, potential supply chain impacts. Specific data theft or ransomware deployment not confirmed in available reporting.
- **Status**: Active incident response underway. Attack vector and specific exploitation details not publicly disclosed.

### Levi Strauss Social Engineering Breach
- **Description**: Hackers used social engineering against three employees to gain access to and steal corporate data stored on their machines.
- **Impact**: Theft of corporate data from employee endpoints, potential exposure of proprietary business information, supply chain partner data, and employee PII.
- **Status**: Breach confirmed; no specific malware or vulnerability exploited beyond human manipulation.

## Affected Systems and Products

- **Metabase**: All versions prior to emergency security patches released following zero-day disclosure. Impacts Framework, Tally, and any organization self-hosting Metabase instances.
- **npm Registry / Node.js Ecosystem**: Nearly 800 malicious packages affecting developers and organizations using npm dependencies across Windows, macOS, and Linux platforms. Supply chain risk extends to all downstream consumers of compromised packages.
- **macOS**: ClickFix social engineering attacks targeting macOS users with Go-based infostealer malware capable of draining crypto wallets and stealing Keychain credentials.
- **Microsoft 365 / Entra ID**: Adversary-in-the-middle phishing campaigns bypassing standard MFA; Windows Hello for Business keys can be abused by malware for persistent Entra ID access.
- **Microsoft SharePoint**: Swiss federal government on-premises SharePoint servers exploited; specific versions and patch status not disclosed.
- **Linux Kernel (SCTP)**: 18-year-old use-after-free vulnerability in SCTP networking code allowing local privilege escalation to root and container escape. Affects all Linux distributions with unpatched kernels.
- **Linux Kernel (KVM / Zapscape)**: Vulnerability allowing privileged L1 guest code to escape KVM isolation and execute code on the host. Impacts virtualized environments using KVM hypervisor.
- **Apache HTTP Server**: Zero-day vulnerability discovered via AI-assisted HTTP desynchronization research; specific versions and exploitation status not fully disclosed.
- **WordPress**: All versions affected by pre-authentication reflected XSS in login screen demonstrated to lead to PHP code execution; patch available.
- **Cisco Catalyst SD-WAN and IOS XE**: Twelve vulnerabilities patched including three critical 9.9 CVSS flaws; no active exploitation reported but immediate patching advised.
- **Anthropic Claude Code / Google Gemini CLI**: Flaws allowing unprivileged GitHub issues to execute code on CI runners, affecting the organizations' own coding-agent repositories.
- **Redis Instances**: Internet-facing Redis instances compromised by TeamPCP threat actor since 2020, evolving into supply chain campaigns.

## Attack Vectors and Techniques

- **SQL Injection (Zero-Day)**: Unauthenticated database query manipulation in Metabase enabling direct data exfiltration without authentication bypass.
- **Software Supply Chain Compromise**: Malicious package publishing to npm registry with typosquatting, dependency confusion, or legitimate package hijacking techniques to achieve developer machine compromise.
- **ClickFix Social Engineering**: Browser-based manipulation tricking users into copying and executing malicious PowerShell or terminal commands under the guise of verification steps or error resolution.
- **Voice Phishing (Vishing)**: Direct phone calls to personal numbers impersonating IT support, leveraging urgency and authority impersonation to harvest SaaS credentials and MFA codes.
- **Adversary-in-the-Middle (AitM) Phishing**: Proxy-based phishing infrastructure capturing authentication credentials and session tokens in real-time, defeating standard multi-factor authentication.
- **Container Escape via Kernel Exploit**: Linux SCTP use-after-free vulnerability exploited from within container to achieve host root access, demonstrating container isolation bypass.
- **KVM Virtual Machine Escape**: Zapscape vulnerability allowing L1 guest with kernel privileges to break KVM isolation and execute code on hypervisor host.
- **NAT Table Manipulation (NatJack)**: Manipulation of network address translation connection state to hijack active TCP sessions and spoof DNS responses, enabling traffic interception and manipulation.
- **HTTP Request Smuggling / Desynchronization**: Novel HTTP desync techniques discovered via AI-assisted research, enabling request smuggling, cache poisoning, and bypass of security controls.
- **Windows Hello for Business Key Abuse**: Malware leveraging authenticated user's hardware-bound credentials to silently authenticate to Entra ID without user interaction or consent.
- **CI/CD Pipeline Injection via GitHub Issues**: Exploitation of coding agent CLI flaws (Claude Code, Gemini CLI) to execute arbitrary code on CI runners through seemingly benign GitHub issue interactions.
- **Redis Unauthorized Access**: Exploitation of internet-facing Redis instances without authentication for initial access, persistence, and lateral movement.
- **Clipboard Hijacking**: Malware monitoring and replacing cryptocurrency wallet addresses in clipboard to redirect transactions to attacker-controlled wallets.
- **Browser Manipulation / Session Hijacking**: Compromised business email inboxes used to manipulate browser sessions for banking malware delivery and financial fraud.
- **CPU Side-Channel (TONTOU)**: Novel speculative execution attack bypassing Spectre v2 mitigations to leak Linux password hashes and other secrets from memory.

## Threat Actor Activities

- **UNC6671 (BlackFile-linked)**: Data extortion group conducting vishing campaigns targeting financial services, private equity, hedge funds, and professional services. Uses voice phishing against personal phones to steal SaaS credentials for data theft and extortion. Active since at least 2024 with Canadian operator pleaded guilty in Snowflake extortion case.
- **TeamPCP**: Cybercrime actor compromising internet-facing Redis instances since 2020, evolving into supply chain campaigns. Demonstrates long-term infrastructure access and operational maturity.
- **ClickFix Operators**: Threat actors deploying Go-based cross-platform infostealers via ClickFix social engineering, with specific macOS variant targeting cryptocurrency assets and Apple Keychain data.
- **AitM Phishing Operators**: Widespread campaign operators using adversary-in-the-middle infrastructure to hijack Microsoft 365 accounts at scale, specifically targeting payroll and finance email access for business email compromise.
- **Snowflake Extortion Actor**: 26-year-old Canadian national (pleaded guilty) described as one of 2024's most consequential cybercrime actors, responsible for hacking and extorting over 165 organizations via Snowflake credential abuse.
- **Malicious npm Package Publisher**: Unknown operator(s) behind coordinated publication of ~800 malicious npm packages delivering cross-platform RAT and infostealer payloads.
- **State-Aligned / APT Actors (Implied)**: Swiss government SharePoint breach and North Carolina Ports attack suggest potential state-aligned or sophisticated criminal actors targeting critical infrastructure and government entities, though attribution not confirmed in available reporting.

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
