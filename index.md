# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple fronts, with threat actors leveraging novel techniques to bypass modern defenses. AI-assisted development tools have emerged as a critical attack surface—Cursor IDE remains vulnerable to poisoned repository attacks that auto-execute malicious code since December, while Grok Build was found exfiltrating entire Git repositories. Simultaneously, Microsoft 365 faces a surge in sophisticated phishing operations: two new kits (Jalisco and OmegaLord) defeat MFA, the Forg365 PhaaS platform combines device code phishing with adversary-in-the-middle session theft, and OAuth client ID spoofing enables at least two distinct threat actors to validate stolen Entra ID credentials while evading telemetry.

Supply chain compromise continues to accelerate. A campaign of 148 malicious npm packages masquerading as student proxies converted browsers into a DDoS botnet for two weeks in May. The Jscrambler client-side security package was backdoored with an infostealer downloaded nearly 1,500 times. ModHeader, a browser extension with 1.6 million installs, harbored a dormant browsing-history collector. On the infrastructure front, CISA warns of active exploitation of RCE flaws in Joomla extensions (iCagenda and Balbooa Forms), while 11 legacy Microsoft-signed UEFI shims threaten Secure Boot integrity across Linux systems. ShinyHunters has spent a year infiltrating Salesforce environments through configuration abuse rather than vulnerabilities, and the modular GigaWiper implant blends backdoor persistence with destructive wiper capabilities.

## Active Exploitation Details

### Cursor IDE Poisoned Repository Code Execution
- **Description**: Cursor IDE automatically executes malicious code embedded in poisoned repositories without user interaction. The vulnerability allows attackers to craft repositories that trigger code execution when opened or analyzed by the AI coding assistant.
- **Impact**: Full code execution on developer machines, potential supply chain compromise, theft of source code and credentials, lateral movement into production environments.
- **Status**: Reported to Cursor in December 2025; remains unpatched as of July 2026. Actively exploitable via poisoned repository attacks.

### Jalisco and OmegaLord Phishing Kits Targeting Microsoft 365
- **Description**: Two new phishing-as-a-service kits specifically designed to target Microsoft 365 accounts with advanced MFA evasion capabilities. Both kits implement techniques to defeat multi-factor authentication protections.
- **Impact**: Complete account takeover of Microsoft 365 users, bypass of MFA controls, access to email, SharePoint, Teams, and connected cloud resources.
- **Status**: Actively deployed in campaigns targeting Microsoft 365 users. MFA evasion techniques are operational.

### OAuth Client ID Spoofing for Entra ID Credential Validation
- **Description**: A novel evasion technique where attackers spoof legitimate OAuth client IDs to validate stolen Microsoft Entra ID credentials without triggering security telemetry. The method allows silent enumeration of valid credentials.
- **Impact**: Stealth validation of compromised credential verification, evasion of detection systems, facilitation of large-scale credential stuffing and account takeover campaigns.
- **Status**: Actively weaponized by at least two distinct threat actors in ongoing cloud campaigns.

### 148 Malicious npm Packages: Browser-Based DDoS Botnet
- **Description**: A coordinated campaign published 148 npm packages disguised as student web proxies. When installed or executed, these packages converted visitors' browsers into nodes of a distributed denial-of-service botnet.
- **Impact**: Unwitting participation in DDoS attacks, browser resource hijacking, potential data exfiltration from compromised browsers, supply chain contamination.
- **Status**: Active for approximately two weeks in May 2026. Packages identified and analyzed by JFrog researchers.

### Jscrambler npm Package Supply Chain Compromise
- **Description**: Threat actors published a malicious version of the legitimate Jscrambler client-side security npm package containing infostealer malware. The backdoored package was downloaded nearly 1,500 times before detection.
- **Impact**: Credential theft, session hijacking, cryptocurrency wallet compromise, exfiltration of sensitive browser data from developers and end users.
- **Status**: Malicious version identified and disclosed by Jscrambler. Downloaded ~1,500 times.

### CrashStealer macOS Information Stealer
- **Description**: A new macOS malware family posing as Apple's crash reporting tool. Uses a notarized dropper to pass Gatekeeper checks, enabling installation without security warnings. Harvests credentials, keychain data, and cryptocurrency wallets.
- **Impact**: Full compromise of macOS systems, theft of authentication credentials, financial assets from crypto wallets, persistent access via keychain extraction.
- **Status**: Active in the wild. Notarized dropper allows bypass of Apple's Gatekeeper protections.

### Actively Exploited RCE in Joomla Extensions (CISA Warning)
- **Description**: CISA has issued a warning that attackers are actively exploiting remote code execution vulnerabilities in the iCagenda and Balbooa Forms extensions for Joomla CMS.
- **Impact**: Full remote code execution on Joomla servers, complete site compromise, data theft, use as pivot for internal network access, malware hosting.
- **Status**: Actively exploited in the wild. CISA emergency directive recommends immediate patching or mitigation.

### Forg365 Phishing-as-a-Service Platform
- **Description**: A new PhaaS operation combining device code phishing, adversary-in-the-middle (AitM) session theft, anti-bot evasion, and AI-assisted targeting against Microsoft 365 accounts.
- **Impact**: Session hijacking bypassing MFA, credential harvesting, persistent access via stolen session tokens, scalable phishing infrastructure.
- **Status**: Active PhaaS offering targeting Microsoft 365 environments.

### GigaWiper Modular Destructive Implant
- **Description**: A modular implant that combines backdoor persistence with wiper functionality, borrowing code from multiple malware families. Allows threat actors to choose between espionage and destructive attack modes.
- **Impact**: Flexible attack capability—persistent access for data theft or complete system destruction, maximizing operational flexibility and impact.
- **Status**: Active deployment observed. Modular design enables tailored attack objectives.

### MemGhost AI Agent Memory Poisoning Attack
- **Description**: A novel attack vector targeting AI agents with memory capabilities. A single malicious email can plant persistent false "memories" that the AI agent recalls and acts upon in future interactions.
- **Impact**: Persistent manipulation of AI assistant behavior, potential data exfiltration through confused deputy attacks, long-term compromise of AI-mediated workflows.
- **Status**: Newly discovered attack technique. Demonstrates fundamental risk in AI memory systems.

### ShinyHunters Salesforce Configuration Abuse Campaign
- **Description**: The data-extortion group ShinyHunters has spent a year accessing corporate Salesforce environments through three distinct attack paths—none exploiting platform vulnerabilities. Instead, they abuse legitimate features and misconfigurations.
- **Impact**: Large-scale data exfiltration from Salesforce instances, access to sensitive customer and business data, extortion leverage.
- **Status**: Year-long active campaign mapped by Microsoft. Three distinct attack paths identified.

## Affected Systems and Products

- **Cursor IDE**: All versions vulnerable to poisoned repository auto-execution; AI coding assistant platform used by developers
- **Microsoft 365 / Entra ID**: Targeted by Jalisco, OmegaLord, Forg365 phishing kits; OAuth client ID spoofing affects credential validation
- **npm Ecosystem**: 148 malicious packages (student proxy lures); Jscrambler package backdoored; ModHeader extension (1.6M installs) with hidden collector
- **macOS Systems**: CrashStealer malware bypassing Gatekeeper via notarized dropper; targets credentials, keychain, crypto wallets
- **Joomla CMS**: Sites using iCagenda and Balbooa Forms extensions actively exploited for RCE
- **Linux Systems with Secure Boot**: 11 legacy Microsoft-signed UEFI shims enable Secure Boot bypass on most modern systems
- **Salesforce Environments**: ShinyHunters targeting via configuration abuse across three attack paths
- **SAP NetWeaver, Commerce Cloud, AppRouter**: Three critical flaws addressed in July 2026 patches (16 total vulnerabilities)
- **Crypto Wallet Browser Extensions**: 85 popular extensions leak address data enabling cross-site tracking and user linking
- **Grok Build (xAI)**: CLI tool uploading entire Git repositories with full commit history to xAI cloud storage

## Attack Vectors and Techniques

- **Poisoned Repository Attack**: Malicious code embedded in repositories auto-executed by AI coding assistants (Cursor IDE)
- **MFA-Bypassing Phishing Kits**: Jalisco and OmegaLord implement advanced techniques to defeat Microsoft 365 multi-factor authentication
- **OAuth Client ID Spoofing**: Attackers impersonate legitimate OAuth applications to silently validate stolen Entra ID credentials
- **Device Code Phishing**: Forg365 leverages OAuth device authorization flow for credential harvesting without traditional phishing pages
- **Adversary-in-the-Middle (AitM) Session Theft**: Real-time proxying of authentication sessions to steal MFA-bypassed tokens
- **Supply Chain Compromise via npm**: Malicious packages typosquatting or masquerading as legitimate utilities (student proxies, security tools)
- **Notarized Malware Droppers**: CrashStealer uses Apple-notarized components to bypass Gatekeeper on macOS
- **UEFI Secure Boot Bypass**: Legacy Microsoft-signed shims abused to disable Secure Boot protections on Linux
- **AI Agent Memory Poisoning (MemGhost)**: Single email implants persistent false memories in AI assistants with memory access
- **Salesforce Configuration Abuse**: Exploitation of legitimate features (reports, APIs, sharing settings) rather than vulnerabilities
- **Modular Wiper/Backdoor Hybrid**: GigaWiper combines persistent access with selective destruction capabilities
- **Browser Extension Data Harvesting**: ModHeader and crypto wallet extensions silently collecting browsing history and address data
- **RCE via CMS Extensions**: Exploitation of Joomla third-party extensions (iCagenda, Balbooa Forms) for server compromise

## Threat Actor Activities

- **ShinyHunters**: Data-extortion group conducting year-long campaign against Salesforce environments. Uses three distinct attack paths abusing legitimate platform features. No platform vulnerabilities exploited—relies on configuration weaknesses and feature misuse.
- **Two Unnamed Threat Actors (OAuth Spoofing)**: Distinct groups actively weaponizing OAuth client ID spoofing for Entra ID credential validation. Operating in cloud campaigns with telemetry evasion.
- **Forg365 Operators**: PhaaS providers offering device code phishing, AitM session theft, anti-bot evasion, and AI-assisted targeting as a service targeting Microsoft 365.
- **Jalisco & OmegaLord Kit Operators**: Developers and distributors of advanced MFA-bypassing phishing kits targeting Microsoft 365 accounts.
- **npm Campaign Operators**: Published 148 coordinated packages disguised as student proxies to build browser-based DDoS botnet (active May 2026).
- **Jscrambler Supply Chain Attacker**: Compromised legitimate security tool's npm package with infostealer; ~1,500 downloads before detection.
- **CrashStealer Developers**: Created macOS info-stealer with notarized dropper bypassing Gatekeeper; masquerades as Apple crash reporter.
- **GigaWiper Operators**: Deploying modular implant combining backdoor and wiper functionality for flexible espionage/destruction.
- **Russian Coms Platform Operators**: Five individuals charged by UK authorities for operating caller ID spoofing platform used for 1.8M scam calls.
- **Sanctioned Ransomware Enablers**: Two individuals and one entity (VPN service + malware cryptor) sanctioned by OFAC for enabling ransomware attacks against US organizations.
- **Nihon Kotsu Attackers**: Compromised Japan's largest taxi operator, forcing partial infrastructure shutdown.
- **Lidl Service Provider Attackers**: Breached third-party provider to steal customer personal data across Germany, Belgium, Netherlands.

## Source Attribution

- **Cursor IDE Auto-Executes Malicious Code in Poisoned Repos**: Dark Reading - https://www.darkreading.com/application-security/cursor-ide-malicious-code-poisoned-repos
- **Microsoft Entra ID gets passkeys default authentication starting September**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-entra-id-gets-passkeys-default-authentication-starting-september/
- **New phishing kits target Microsoft 365 accounts, evade MFA**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/
- **11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot**: The Hacker News - https://thehackernews.com/2026/07/11-old-microsoft-signed-linux-uefi.html
- **Study of 85 Crypto Wallet Extensions Finds Address Leaks and Cross-Site Tracking Risks**: The Hacker News - https://thehackernews.com/2026/07/study-of-85-crypto-wallet-extensions.html
- **SAP warns of critical flaws in NetWeaver and Commerce Cloud**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sap-warns-of-critical-flaws-in-netweaver-and-commerce-cloud/
- **How Pentera Turns AI Security Workflows into Validation Engines**: The Hacker News - https://thehackernews.com/2026/07/how-pentera-turns-ai-security-workflows.html
- **OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials**: The Hacker News - https://thehackernews.com/2026/07/oauth-client-id-spoofing-lets-attackers.html
- **Microsoft starts testing cleaner Windows Search without ads**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-starts-testing-cleaner-windows-search-without-ads/
- **US sanctions VPN, malware providers for enabling ransomware attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-sanctions-vpn-malware-providers-linked-to-ransomware-gangs/
- **Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read**: The Hacker News - https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html
- **U.S. Sanctions First VPN Service and Malware Cryptor Seller Over Ransomware Support**: The Hacker News - https://thehackernews.com/2026/07/us-sanctions-first-vpn-service-and.html
- **148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet**: The Hacker News - https://thehackernews.com/2026/07/148-npm-packages-disguised-as-student.html
- **Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity**: The Hacker News - https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
- **Weak Security Continues to Fuel Russian Cyberattacks**: Dark Reading - https://www.darkreading.com/endpoint-security/weak-security-fuel-russian-cyberattacks
- **Japan's largest taxi operator shuts systems after cyberattack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/japans-largest-taxi-operator-shuts-systems-after-cyberattack/
- **Hackers backdoor Jscrambler npm package with infostealer malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/
- **New CrashStealer malware poses as Apple crash reporting tool**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-crashstealer-malware-poses-as-apple-crash-reporting-tool/
- **'Yellow Teams' Are Defining the Future of AI Security**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/yellow-teams-defining-future-ai-security
- **CrashStealer macOS Malware Uses Notarized Dropper to Pass Gatekeeper Checks**: The Hacker News - https://thehackernews.com/2026/07/crashstealer-macos-malware-uses.html
- **Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found**: The Hacker News - https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html
- **GigaWiper Lets Threat Actors Choose Their Own Destructive Attack**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/gigawiper-threat-actors-choose-their-own-destructive-attack
- **CISA warns of actively exploited RCE flaws in Joomla extensions**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-rce-flaws-in-joomla-extensions/
- **⚡ Weekly Recap: ShareFile Threat, Citrix Bleed 2 Ransomware, AI Coding Attacks, and More**: The Hacker News - https://thehackernews.com/2026/07/weekly-recap-sharefile-threat-citrix.html
- **Lessons Learned from CISA’s Recent GitHub Leak**: Krebs on Security - https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/
- **Lidl discloses online shop breach after service provider hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lidl-discloses-online-shop-breach-after-service-provider-hack/
- **Breach at the Beach: Play the Ultimate Entra ID CTF**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/breach-at-the-beach-play-the-ultimate-entra-id-ctf/
- **New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email**: The Hacker News - https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html
- **UK charges suspects linked to Russian Coms call spoofing platform**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/uk-charges-suspects-linked-to-russian-coms-call-spoofing-platform/
- **Forg365 PhaaS Targets Microsoft 365 with Device Code and AitM Session Theft**: The Hacker News - https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
