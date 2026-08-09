# Exploitation Report

## Executive Summary

A surge in supply chain compromises and zero-day exploitation has dominated recent threat activity, with the Head Mare hacktivist group breaching TrueConf's video conferencing infrastructure to trojanize legitimate client installers with backdoors. Simultaneously, a critical Metabase SQL injection zero-day has been actively exploited in data theft attacks against customer instances including Framework and Tally, while Progress Kemp LoadMaster appliances face widespread exploitation with 792 reported attempts driving CISA KEV inclusion. These campaigns demonstrate adversaries' increasing focus on trusted software distribution channels and internet-facing enterprise appliances as initial access vectors.

Social engineering and identity-focused attacks have evolved in sophistication, with UNC6671 conducting vishing campaigns targeting financial services and private equity firms to steal SaaS credentials, and a widespread Microsoft 365 adversary-in-the-middle (AitM) phishing operation harvesting payroll and finance emails. The ClickFix technique has expanded to macOS with a Go-based infostealer draining cryptocurrency wallets, browser credentials, and Apple Keychain data. Meanwhile, nearly 800 malicious npm packages were published in a coordinated supply chain campaign delivering cross-platform remote access trojans and infostealers across Windows, macOS, and Linux environments.

Research disclosures reveal novel attack classes with immediate defensive implications: CSS-based attacks breaking webmail sandbox isolation across Outlook, Gmail, Proton Mail, Yahoo Mail, and Fastmail; the NatJack technique manipulating NAT connection tables to hijack TCP sessions and spoof DNS; and AI-assisted discovery of HTTP desynchronization vulnerabilities including an Apache zero-day. Long-standing vulnerabilities continue to prove potent, with an 18-year-old Linux SCTP use-after-free enabling container escapes to host root, and a pre-authentication WordPress XSS affecting all versions demonstrating a path to PHP code execution. Threat actors including TeamPCP have been linked to Redis compromise campaigns dating back to 2020, indicating persistent infrastructure targeting.

## Active Exploitation Details

### TrueConf Supply Chain Compromise
- **Description**: The Head Mare hacktivist group exploited vulnerabilities in unpatched TrueConf video conferencing servers to gain access to the software distribution infrastructure. Attackers replaced legitimate client installers with trojanized versions containing backdoors, creating a supply chain attack vector targeting TrueConf's user base.
- **Impact**: Organizations downloading and installing TrueConf client software receive malicious installers that deploy backdoors, granting attackers persistent access to victim networks. The compromise of a trusted video conferencing platform's distribution channel amplifies impact across enterprise environments.
- **Status**: Active exploitation ongoing. TrueConf users should verify installer integrity and apply server patches immediately.

### Metabase SQL Injection Zero-Day
- **Description**: A critical SQL injection vulnerability in Metabase business intelligence and data visualization software allows unauthenticated attackers to achieve administrative access. The flaw has been exploited as a zero-day in targeted data theft campaigns.
- **Impact**: Attackers gain full administrative access to Metabase instances without authentication, enabling exfiltration of sensitive business intelligence data, customer information, and analytics. Confirmed victims include Framework and Tally.
- **Status**: Actively exploited in the wild as a zero-day. Metabase has issued warnings; emergency patching required for all exposed instances.

### Progress Kemp LoadMaster Exploitation
- **Description**: A critical-severity vulnerability affecting Progress Kemp LoadMaster application delivery controllers has seen widespread exploitation with 792 reported exploit attempts, prompting CISA to add it to the Known Exploited Vulnerabilities catalog.
- **Impact**: Successful exploitation provides attackers with access to load balancing infrastructure, potentially enabling traffic interception, service disruption, and lateral movement within network segments.
- **Status**: Actively exploited with high volume. CISA KEV listing mandates federal agency patching; all organizations should prioritize remediation.

### N-able N-central RMM Exploitation
- **Description**: Attackers are actively exploiting a recently disclosed security flaw in N-able's N-central Remote Monitoring and Management (RMM) platform. N-able has released a second hotfix (Hotfix 2) as part of ongoing investigation into the campaign.
- **Impact**: Compromise of RMM infrastructure grants attackers administrative control over all managed endpoints, enabling mass deployment of malware, persistence mechanisms, and data exfiltration across customer environments.
- **Status**: Ongoing exploitation with evidence of attacker persistence. Hotfix 2 released; all N-central instances require immediate update.

### Atlassian Rovo Data Exfiltration
- **Description**: Attacker-controlled instructions can manipulate Atlassian's Rovo AI assistant to collect Jira and Confluence data accessible to a signed-in user and exfiltrate it to an external server. Two security firms independently identified the vulnerability.
- **Impact**: Sensitive project management data, credentials, internal documentation, and proprietary information accessible through Jira and Confluence can be stolen via prompt injection against the AI assistant.
- **Status**: Vulnerability disclosed; patching status should be verified with Atlassian advisories.

### Webmail CSS Sandbox Escape
- **Description**: New research demonstrates CSS-based attacks that allow email content to escape message boundaries and interfere with webmail interfaces across Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail. The technique enables credential theft and token extraction.
- **Impact**: Attackers can steal passwords, session tokens, and authentication credentials by crafting malicious emails that break out of sandboxed rendering contexts and interact with the parent webmail application DOM.
- **Status**: Proof-of-concept demonstrated across major webmail providers; mitigations require provider-side fixes to CSS sanitization and iframe sandboxing.

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks deliver a Go-based malware targeting macOS users. The malware steals cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials.
- **Impact**: Victims suffer financial loss through crypto wallet drainage, credential compromise across browsers and system keychains, and potential identity theft. The cross-platform Go implementation suggests Windows/Linux variants may exist.
- **Status**: Active campaign observed in the wild; delivered via ClickFix fake verification/CAPTCHA pages.

### UNC6671 Vishing and Extortion Campaign
- **Description**: The UNC6671 data extortion group conducts voice phishing (vishing) attacks targeting personal phones of employees at financial services, private equity, and professional services firms. The group is reportedly associated with the BlackFile threat actor.
- **Impact**: Attackers gain access to SaaS applications and sensitive financial data through social engineering, enabling data theft and extortion. Campaigns have targeted hedge funds and investment firms.
- **Status**: Active wave of attacks; attributed to UNC6671/BlackFile linkage.

### Malicious npm Supply Chain Campaign
- **Description**: Nearly 800 malicious packages were published to the npm registry in a coordinated campaign delivering cross-platform malware including remote access trojans (RATs) and infostealers targeting Windows, macOS, and Linux systems.
- **Impact**: Developers and CI/CD pipelines installing compromised packages introduce malware into development environments and production systems, enabling supply chain compromise at scale.
- **Status**: Packages identified and reported; npm registry cleanup underway. Organizations should audit dependencies and implement package verification.

### WordPress Pre-Auth XSS to RCE
- **Description**: A pre-authentication reflected cross-site scripting (XSS) vulnerability in the WordPress login screen affects every version of the CMS. Researcher pwn.ai demonstrated an exploitation chain leading to PHP code execution.
- **Impact**: Unauthenticated attackers can execute arbitrary PHP code on WordPress sites, achieving full server compromise. Universal version impact makes this exceptionally broad.
- **Status**: WordPress has released a fix; immediate updating required for all WordPress installations.

### Linux SCTP Container Escape
- **Description**: An 18-year-old use-after-free vulnerability in Linux's SCTP (Stream Control Transmission Protocol) networking subsystem allows local users to gain root privileges and escape containers to the host system. Tencent researchers demonstrated practical exploitation.
- **Impact**: Containerized workloads can be escaped to achieve host root access, breaking isolation guarantees critical to cloud and containerized environments. The flaw's age means it exists in most deployed Linux kernels.
- **Status**: Vulnerability disclosed with exploit demonstration; kernel patches required across all Linux distributions.

### NatJack NAT Manipulation Attacks
- **Description**: Security researcher Malcolm Stagg disclosed the NatJack attack class, which manipulates Network Address Translation (NAT) connection state tables to hijack active TCP sessions and spoof DNS responses.
- **Impact**: Attackers on the same network segment can intercept and manipulate established connections, redirect traffic, and perform DNS spoofing by exploiting NAT implementation weaknesses in routers and firewalls.
- **Status**: New attack class disclosed; mitigations require vendor patches to NAT implementations and network segmentation.

### Microsoft 365 AitM Phishing Campaign
- **Description**: A widespread email-driven phishing campaign employs adversary-in-the-middle (AitM) techniques to hijack Microsoft 365 accounts. The campaign specifically targets payroll and finance email communications.
- **Impact**: Attackers gain full account access including MFA bypass via session token theft, enabling business email compromise, financial fraud, and persistent access to sensitive communications.
- **Status**: Active campaign; phishing infrastructure observed targeting multiple organizations simultaneously.

### Apache HTTP Desynchronization Zero-Day
- **Description**: PortSwigger's AI-assisted HTTP Terminator research system discovered novel HTTP request smuggling/desynchronization techniques and an Apache HTTP Server zero-day vulnerability after exploring 30,000 candidate techniques.
- **Impact**: HTTP desync attacks enable request smuggling, cache poisoning, and authentication bypass across Apache deployments. AI-assisted discovery suggests more variants may exist.
- **Status**: Zero-day disclosed to Apache; patch development underway. Research methodology indicates potential for additional undiscovered variants.

### Windows Hello for Business Key Abuse
- **Description**: Researcher Dirk-jan Mollema demonstrated that malware running in a signed-in Windows session can silently abuse Windows Hello for Business cryptographic keys to authenticate to Microsoft Entra ID (formerly Azure AD), achieving persistent access.
- **Impact**: Compromised endpoints can maintain persistent Entra ID authentication without user interaction, bypassing conditional access policies and enabling long-term cloud identity compromise.
- **Status**: Technique demonstrated; mitigations require Entra ID configuration changes and endpoint detection improvements.

### Claude Code and Gemini CLI CI Secret Extraction
- **Description**: Flaws in Anthropic's Claude Code and Google's Gemini CLI coding agents allow a GitHub issue opened by an unprivileged account to execute code on CI runners, accessing workflow secrets. OpenAI's infrastructure was similarly affected.
- **Impact**: Attackers can exfiltrate CI/CD secrets including API keys, deployment credentials, and signing certificates by simply opening GitHub issues against repositories using these AI coding agents.
- **Status**: Vulnerabilities disclosed to affected vendors; CI/CD pipeline hardening and agent permission reviews required.

### TeamPCP Redis and Supply Chain Campaign
- **Description**: Threat actor TeamPCP has been linked to Redis server compromise campaigns dating back to 2020, with later evolution into software supply chain attacks. The group targets internet-facing infrastructure for initial access and persistence.
- **Impact**: Long-term compromise of Redis instances enables data theft, cryptojacking, and supply chain poisoning. The 2020 origin indicates mature operational capability and infrastructure.
- **Status**: Historical campaign attributed; ongoing monitoring for TeamPCP infrastructure and TTPs recommended.

## Affected Systems and Products

- **TrueConf Video Conferencing Server**: Unpatched server versions exploited for installer trojanization; client installers distributed through official channels compromised
- **Metabase Business Intelligence Platform**: All versions vulnerable to unauthenticated SQL injection until emergency patch applied; Framework and Tally confirmed breached
- **Progress Kemp LoadMaster**: Application delivery controller appliances; critical flaw actively exploited with 792+ attempts reported to CISA
- **N-able N-central**: Remote Monitoring and Management platform; RMM servers targeted for mass endpoint compromise; Hotfix 2 required
- **Atlassian Rovo / Jira / Confluence**: AI assistant integration vulnerable to prompt injection data exfiltration; affects cloud and Data Center deployments
- **Webmail Platforms**: Microsoft Outlook, Google Gmail, Fastmail, Proton Mail, Yahoo Mail — all demonstrated vulnerable to CSS sandbox escape attacks
- **macOS Systems**: Targeted by ClickFix-delivered Go-based infostealer (crypto wallets, Keychain, browser credentials)
- **npm Registry / Node.js Ecosystem**: ~800 malicious packages published; cross-platform RAT/infostealer affecting Windows, macOS, Linux developers
- **WordPress CMS**: All versions affected by pre-auth reflected XSS on login screen; PHP code execution chain demonstrated
- **Linux Kernel**: SCTP subsystem use-after-free (18-year-old flaw); affects container hosts and Kubernetes nodes across distributions
- **NAT Devices / Routers / Firewalls**: NAT implementations vulnerable to connection table manipulation (NatJack); TCP hijacking and DNS spoofing possible
- **Microsoft 365 / Entra ID**: AitM phishing bypasses MFA; Windows Hello for Business keys abused for persistent cloud authentication
- **Apache HTTP Server**: Zero-day HTTP desynchronization vulnerability discovered via AI-assisted research
- **Anthropic Claude Code / Google Gemini CLI / OpenAI Codex**: AI coding agents with CI integration flaws enabling secret extraction via GitHub issues
- **Redis Servers**: Internet-facing instances compromised by TeamPCP since 2020; later used in supply chain campaigns
- **Unlimited Technology Systems**: Healthcare software platform breached (October 2025); 3.8 million individuals' data exposed
- **North Carolina Ports Authority**: Critical infrastructure IT systems disrupted; Port of Wilmington, Port of Morehead City, Charlotte Inland Port affected
- **Levi Strauss & Co.**: Corporate systems accessed via social engineering of three employees; corporate data exfiltrated

## Attack Vectors and Techniques

- **Software Supply Chain Compromise**: Legitimate software distribution infrastructure breached to distribute trojanized installers (TrueConf, npm packages)
- **Zero-Day Exploitation**: Unpatched vulnerabilities exploited before vendor fixes available (Metabase SQLi, Apache HTTP desync, potentially TrueConf)
- **Prompt Injection Against AI Assistants**: Attacker-controlled instructions manipulate AI agents to access and exfiltrate authorized user data (Atlassian Rovo, Claude Code, Gemini CLI)
- **CSS Sandbox Escape**: Malicious email content breaks out of sandboxed rendering contexts to attack parent webmail application DOM
- **ClickFix Social Engineering**: Fake verification/CAPTCHA pages trick users into executing malicious commands (PowerShell, bash, Go binaries)
- **Voice Phishing (Vishing)**: Phone-based social engineering targeting personal devices to harvest SaaS credentials and MFA codes (UNC6671)
- **Adversary-in-the-Middle (AitM) Phishing**: Proxy-based phishing capturing session tokens to bypass MFA (Microsoft 365 campaign)
- **HTTP Request Smuggling / Desynchronization**: Protocol-level attacks exploiting parser differentials between frontend/backend servers (Apache zero-day)
- **NAT Connection Table Manipulation**: Exploiting stateful NAT implementation flaws to hijack TCP sessions and spoof DNS (NatJack)
- **Container Escape via Kernel Vulnerability**: Local privilege escalation through SCTP use-after-free breaking container isolation (Linux kernel)
- **CI/CD Pipeline Injection via GitHub Issues**: Unprivileged issue creation triggers code execution on CI runners with secret access (AI coding agents)
- **Windows Hello Key Abuse**: Malware leverages TPM-bound cryptographic keys for silent Entra ID authentication persistence
- **Long-Term Infrastructure Compromise**: Persistent access to Redis servers leveraged for later supply chain attacks (TeamPCP, 2020+)
- **Critical Infrastructure Targeting**: Disruption of port authority IT systems affecting maritime operations (North Carolina Ports)

## Threat Actor Activities

- **Head Mare**: Hacktivist group conducting supply chain attack against TrueConf video conferencing platform; exploits unpatched servers to trojanize client installers with backdoors
- **UNC6671 / BlackFile**: Data extortion group targeting financial services, private equity, hedge funds, and professional services via vishing campaigns; steals SaaS credentials for data theft and extortion; linked to BlackFile ransomware/extortion operations
- **TeamPCP**: Cybercrime actor active since at least 2020; compromises internet-facing Redis infrastructure; evolved to software supply chain attacks; demonstrates long-term operational persistence
- **ClickFix Operators**: Threat actors utilizing ClickFix social engineering framework; recently expanded to macOS with Go-based infostealer targeting cryptocurrency, credentials, and Keychain data; cross-platform capability indicated
- **Malicious npm Publishers**: Coordinated campaign publishing ~800 packages to npm registry; delivers cross-platform RAT and infostealer malware; targets software development supply chain
- **Microsoft 365 AitM Phishing Actors**: Unattributed group running widespread adversary-in-the-middle phishing campaign; focuses on payroll and finance email compromise for business email compromise (BEC) fraud
- **TrueConf Attackers (Head Mare)**: Same as Head Mare entry; hacktivist motivation suggested by group designation
- **Metabase Zero-Day Exploiters**: Unattributed actors exploiting SQL injection zero-day for targeted data theft; Framework and Tally confirmed as victims; financial/business intelligence motivation
- **Progress Kemp LoadMaster Exploiters**: Unattributed actors conducting high-volume exploitation (792+ attempts); CISA KEV inclusion confirms active threat
- **N-central Exploiters**: Unattributed actors targeting RMM platform for downstream managed service provider and customer compromise; persistence observed

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
