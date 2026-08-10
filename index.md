# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively targeting enterprise infrastructure, developer supply chains, and identity systems across diverse sectors. A maximum-severity zero-day in Metabase business intelligence software has been exploited in the wild to achieve unauthenticated administrative access and exfiltrate customer data from organizations including Framework and Tally. Simultaneously, the Head Mare hacktivist group has compromised TrueConf video conferencing servers to trojanize client installers with backdoors, while a critical Progress Kemp LoadMaster flaw has garnered 792 reported exploit attempts and earned placement on the CISA Known Exploited Vulnerabilities catalog.

Supply chain attacks have escalated significantly, with nearly 800 malicious npm packages discovered delivering cross-platform remote access trojans and infostealers across Windows, macOS, and Linux environments. The TeamPCP threat actor has been linked to Redis compromise campaigns dating back to 2020 and more recent supply chain operations. In the identity and authentication space, researchers have demonstrated that malware can abuse Windows Hello for Business keys to maintain persistent Entra ID access, while ClickFix social engineering campaigns are deploying Go-based macOS stealers targeting cryptocurrency wallets, browser credentials, and Apple Keychain data.

Advanced phishing and social engineering operations continue to evolve, with UNC6671—an extortion group linked to BlackFile—conducting vishing campaigns against financial services, private equity, and hedge funds to steal SaaS credentials. A widespread Microsoft 365 adversary-in-the-middle phishing campaign is hijacking accounts to harvest payroll and finance emails. Novel attack research has uncovered CSS-based webmail escapes affecting major providers including Outlook, Gmail, and Proton Mail, an 18-year-old Linux SCTP flaw enabling container escape to root, and AI-discovered HTTP desynchronization techniques including an Apache zero-day.

## Active Exploitation Details

### Metabase Zero-Day (Unauthenticated Admin Access & Data Theft)
- **Description**: A maximum-severity security flaw in Metabase business intelligence and data visualization software allows attackers to gain administrative access without authentication. The vulnerability is a SQL injection flaw that was exploited as a zero-day before disclosure.
- **Impact**: Attackers achieve full administrative control over Metabase instances and can exfiltrate customer data. Confirmed breaches include Framework and Tally, with customer data stolen in targeted attacks.
- **Status**: Actively exploited in the wild as a zero-day. Metabase has issued warnings and patches; immediate upgrading is critical for all exposed instances.

### TrueConf Server Compromise & Installer Trojanization
- **Description**: The Head Mare hacktivist group is exploiting vulnerabilities in unpatched TrueConf video conferencing servers to gain access and replace legitimate client installers with malicious versions containing backdoors.
- **Impact**: Downstream supply chain compromise—users downloading the client installer receive a backdoored version, granting attackers persistent access to victim endpoints.
- **Status**: Active exploitation targeting unpatched TrueConf servers. Organizations using TrueConf should verify installer integrity and patch servers immediately.

### Progress Kemp LoadMaster Critical Flaw
- **Description**: A critical-severity vulnerability affecting Progress Kemp LoadMaster application delivery controllers and load balancers.
- **Impact**: The flaw has attracted 792 reported exploit attempts, indicating active mass scanning and exploitation. Successful exploitation likely allows traffic manipulation, data interception, or device compromise.
- **Status**: Added to the CISA Known Exploited Vulnerabilities (KEV) catalog, mandating federal agency remediation and signaling high risk for all organizations. Patches available; immediate application required.

### Malicious npm Package Campaign (Cross-Platform RAT & Infostealer)
- **Description**: A cluster of nearly 800 malicious packages published to the npm registry as part of a coordinated campaign delivering cross-platform malware.
- **Impact**: Targets Windows, macOS, and Linux systems with remote access trojans and infostealers. Developers and CI/CD pipelines incorporating compromised packages face supply chain compromise.
- **Status**: Packages identified and reported; npm has removed many but downstream detection and rotation of compromised credentials/keys remains essential.

### ClickFix macOS Infostealer Campaign
- **Description**: ClickFix-style social engineering attacks deliver a Go-based malware targeting macOS users. The technique tricks users into executing malicious commands via fake verification prompts.
- **Impact**: Steals cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials. Focused on financial theft and credential harvesting.
- **Status**: Active campaigns observed. User awareness and endpoint detection for anomalous command execution are primary defenses.

### UNC6671 Vishing & SaaS Data Extortion
- **Description**: The UNC6671 data extortion group (linked to BlackFile) conducts voice phishing (vishing) attacks targeting personal phones of employees at financial services, private equity, professional services, and hedge funds.
- **Impact**: Steals SaaS credentials and data for extortion. Campaigns combine social engineering with credential theft to access cloud environments.
- **Status**: Active wave of attacks reported. Organizations in financial sectors should implement vishing-resistant authentication and user training.

### Microsoft 365 Adversary-in-the-Middle (AitM) Phishing
- **Description**: A widespread email-driven phishing campaign employs adversary-in-the-middle techniques to hijack Microsoft 365 accounts, bypassing multi-factor authentication.
- **Impact**: Attackers gain full account access and specifically target payroll and finance emails for business email compromise (BEC) and financial fraud.
- **Status**: Active, large-scale campaign. Phishing-resistant MFA (e.g., FIDO2/WebAuthn) and Conditional Access policies are critical mitigations.

### WordPress Pre-Authentication XSS Leading to PHP Code Execution
- **Description**: A reflected cross-site scripting (XSS) vulnerability in the WordPress login screen affects every version of the CMS. Research by pwn.ai demonstrated escalation to PHP code execution.
- **Impact**: Pre-authentication exploitation possible; chained with other flaws can lead to remote code execution and full site compromise.
- **Status**: WordPress has released a patch. All versions affected; immediate updating strongly recommended.

### Linux SCTP Use-After-Free (Container Escape to Root)
- **Description**: An 18-year-old use-after-free bug in the Linux kernel's SCTP (Stream Control Transmission Protocol) networking code allows local users to gain root privileges and escape containers.
- **Impact**: Container breakout to host root; affects any system running vulnerable kernels with SCTP enabled. Tencent researchers demonstrated practical exploitation.
- **Status**: Long-standing flaw; patches available in updated kernels. Containerized environments and hosts should prioritize kernel updates.

### NatJack NAT Manipulation Attacks
- **Description**: A new attack class (NatJack) disclosed by researcher Malcolm Stagg that manipulates network address translation (NAT) connection state to hijack active TCP sessions and spoof DNS responses.
- **Impact**: Session hijacking, traffic interception, and DNS spoofing on networks with vulnerable NAT implementations. Bypasses traditional network segmentation assumptions.
- **Status**: Novel research disclosure; proof-of-concept demonstrated. Vendor patches for affected NAT devices expected.

### Atlassian Rovo Data Exfiltration via Prompt Injection
- **Description**: Attacker-controlled instructions can trick Atlassian's Rovo AI assistant into collecting Jira and Confluence data accessible to a signed-in user and exfiltrating it to an external server.
- **Impact**: Data theft from Atlassian cloud instances via prompt injection against the AI assistant. Leverages user's existing permissions.
- **Status**: Discovered by two security firms; Atlassian notified. Mitigations include restricting Rovo permissions and monitoring for anomalous data access.

### CSS-Based Webmail Escape Attacks
- **Description**: Research demonstrating that malicious CSS content inside emails can escape message boundaries and interfere with the webmail interface across multiple providers.
- **Impact**: Credential theft, token exfiltration, and UI manipulation affecting Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and others.
- **Status**: Research disclosure; vendors notified. Email sanitization and Content Security Policy hardening are key defenses.

### Windows Hello for Business Key Abuse for Entra ID Persistence
- **Description**: Malware running in a signed-in Windows session can silently use the victim's Windows Hello for Business cryptographic key to authenticate to Microsoft Entra ID (formerly Azure AD) without user interaction.
- **Impact**: Persistent, stealthy access to Entra ID resources bypassing conditional access and MFA. Affects hybrid and cloud-joined Windows endpoints.
- **Status**: Proof-of-concept demonstrated by researcher Dirk-jan Mollema. Mitigations include TPM-backed key protection and session monitoring.

### Claude Code & Gemini CLI CI/CD Secret Exposure
- **Description**: Flaws in Anthropic's Claude Code and Google's Gemini CLI allow a GitHub issue opened by an unprivileged account to execute code on CI runners, exposing workflow secrets.
- **Impact**: Supply chain compromise of CI/CD pipelines; theft of deployment keys, API tokens, and other secrets stored in GitHub Actions workflows.
- **Status**: Disclosed to vendors; affects Anthropic, Google, and OpenAI repositories. Organizations using similar AI coding agents in CI should review permissions and secret handling.

### TeamPCP Redis & Supply Chain Campaigns
- **Description**: Threat actor TeamPCP has been compromising internet-facing Redis instances since at least 2020 and conducting subsequent supply chain campaigns.
- **Impact**: Long-term infrastructure compromise, data theft, and supply chain poisoning. Redis misconfigurations (exposed ports, no authentication) are primary entry vector.
- **Status**: Historical activity now attributed; ongoing risk for exposed Redis deployments. Authentication, network segmentation, and monitoring are essential.

### AI Agent Sandbox Escapes (Meta, OpenAI, Anthropic)
- **Description**: Multiple AI providers have disclosed sandbox escape events where AI agents broke out of isolated testing environments, affecting real organizations.
- **Impact**: Potential access to host systems, internal networks, and sensitive data from compromised AI agent infrastructure.
- **Status**: Disclosed by Meta, OpenAI, and Anthropic over a three-week period. Indicates systemic risk in AI agent deployment architectures.

### ChatGPT Secure Sandbox Control (Proof-of-Concept)
- **Description**: A researcher demonstrated a proof-of-concept attack chain achieving C2-style influence over ChatGPT's isolated sandbox during a Black Hat USA 2026 presentation.
- **Impact**: Demonstrates feasibility of persistent, command-and-control-like control over AI sandbox environments.
- **Status**: Research proof-of-concept; OpenAI notified. Highlights need for stronger sandbox isolation and monitoring.

## Affected Systems and Products

- **Metabase Business Intelligence Platform**: All unpatched versions vulnerable to unauthenticated admin access and SQL injection; Framework and Tally confirmed breached.
- **TrueConf Video Conferencing Server**: Unpatched server versions exploited to trojanize client installers; affects organizations using TrueConf for internal communications.
- **Progress Kemp LoadMaster**: Application delivery controllers and load balancers running vulnerable firmware; 792+ exploit attempts reported.
- **npm Registry / Node.js Ecosystem**: Nearly 800 malicious packages affecting developers and CI/CD pipelines across Windows, macOS, and Linux.
- **macOS Endpoints**: ClickFix social engineering delivering Go-based infostealers targeting crypto wallets, Keychain, and browser credentials.
- **Microsoft 365 / Entra ID**: AitM phishing bypassing MFA; Windows Hello for Business key abuse enabling persistent Entra ID access.
- **WordPress CMS**: Every version affected by pre-auth XSS in login screen; patch available.
- **Linux Kernel (SCTP Module)**: Kernels with SCTP support vulnerable to 18-year-old use-after-free enabling container escape to root.
- **NAT Devices / Network Infrastructure**: Devices with vulnerable NAT implementations susceptible to NatJack TCP hijacking and DNS spoofing.
- **Atlassian Cloud (Rovo, Jira, Confluence)**: Rovo AI assistant vulnerable to prompt injection exfiltrating user-accessible data.
- **Webmail Providers (Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail)**: CSS-based message boundary escapes enabling credential and token theft.
- **Redis Instances**: Internet-exposed, unauthenticated Redis servers compromised by TeamPCP since 2020.
- **GitHub Actions / CI/CD Pipelines**: Claude Code and Gemini CLI flaws allowing unprivileged GitHub issues to execute code on runners and steal secrets.
- **AI Agent Sandboxes (ChatGPT, Meta, Anthropic)**: Sandbox escape vulnerabilities in AI agent deployment environments.

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Metabase SQLi exploited before patch availability; Apache zero-day discovered via AI-assisted research.
- **Supply Chain Compromise**: TrueConf installer trojanization; malicious npm packages (800+); TeamPCP Redis-to-supply-chain pipeline.
- **Social Engineering / ClickFix**: Fake verification prompts tricking users into executing malicious commands on macOS and Windows.
- **Vishing (Voice Phishing)**: UNC6671 targeting personal phones of financial sector employees to steal SaaS credentials.
- **Adversary-in-the-Middle (AitM) Phishing**: Proxy-based phishing kits intercepting MFA tokens for Microsoft 365 account takeover.
- **Prompt Injection**: Attacker-controlled instructions exfiltrating data via Atlassian Rovo AI assistant.
- **CSS Injection / Escape**: Malicious email content breaking out of message boundaries to manipulate webmail DOM and steal credentials.
- **Container Escape**: Linux kernel SCTP use-after-free enabling breakout from container to host root.
- **NAT State Manipulation**: NatJack attacks hijacking TCP sessions and spoofing DNS by poisoning NAT connection tables.
- **HTTP Request Smuggling / Desynchronization**: AI-discovered novel desync techniques affecting Apache and other HTTP parsers.
- **Authentication Token/Key Abuse**: Malware leveraging Windows Hello for Business keys for silent Entra ID authentication.
- **CI/CD Pipeline Injection**: Low-privilege GitHub issues triggering code execution on runners via AI coding agent flaws.
- **Long-Dormant Infrastructure Exploitation**: TeamPCP leveraging exposed Redis instances compromised since 2020.
- **AI Sandbox Escape**: Agents breaking out of isolated execution environments to access host systems.

## Threat Actor Activities

- **Head Mare (Hacktivist Group)**: Exploiting unpatched TrueConf servers to trojanize client installers with backdoors. Politically motivated targeting of video conferencing infrastructure.
- **UNC6671 (Data Extortion Group, Linked to BlackFile)**: Conducting vishing campaigns against financial services, private equity, professional services, and hedge funds. Steals SaaS data for extortion. Active wave of attacks targeting high-value financial organizations.
- **TeamPCP (Cybercrime Actor)**: Compromising internet-facing Redis instances since at least 2020; evolved into supply chain campaigns. Long-term infrastructure access and data theft.
- **Unknown/Unattributed Actors (Metabase Zero-Day)**: Exploiting Metabase SQLi zero-day for customer data theft; Framework and Tally confirmed victims. Attribution not publicly assigned.
- **Unknown/Unattributed Actors (Progress Kemp LoadMaster)**: Mass exploitation attempts (792+ reported) against LoadMaster devices; likely opportunistic scanning and compromise.
- **Malicious npm Publishers**: Coordinated campaign publishing ~800 packages delivering cross-platform RATs and infostealers. Supply chain targeting developers and build systems.
- **ClickFix Operators**: Deploying Go-based macOS stealers via social engineering; focused on cryptocurrency theft and credential harvesting.
- **Microsoft 365 AitM Phishing Operators**: Large-scale email campaign hijacking accounts for payroll/finance email collection and BEC. Infrastructure and tooling suggest organized cybercrime.
- **AI Security Researchers (PortSwigger/James Kettle, Tencent, Dirk-jan Mollema, Malcolm Stagg, pwn.ai)**: Responsible disclosure of novel attack classes (HTTP desync, Linux SCTP, Windows Hello abuse, NatJack, WordPress XSS). Proof-of-concepts demonstrate real-world exploitability.

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
