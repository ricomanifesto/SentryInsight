# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-value targets this reporting period, with active zero-day attacks against SonicWall SMA 1000 appliances, Mozilla Firefox, and Microsoft SharePoint servers. CISA has issued emergency directives for three actively exploited SharePoint vulnerabilities, while SonicWall confirmed exploitation of two zero-days (CVE-2026-15409 and CVE-2026-15410) enabling arbitrary command execution. Mozilla disclosed that exploit code has been published for CVE-2026-15718, a critical Firefox flaw. Microsoft's record-breaking Patch Tuesday addressed 622 vulnerabilities including two zero-days under active attack, though a new Windows User Profile Service zero-day (LegacyHive) emerged hours after patches were released.

Supply chain attacks and AI-enabled threats represent escalating vectors. A sustained npm supply chain compromise delivered multi-stage botnet malware through compromised AsyncAPI packages, while a Russian-speaking actor ("bandcampro") weaponized Google's Gemini CLI as both a hacking agent and botnet controller. The TuxBot v3 IoT botnet shows evidence of LLM-assisted development, and the OkoBot framework targets hardware wallet recovery phrases. Meanwhile, Cursor IDE vulnerabilities allow automatic code execution via malicious cloned repositories, and a "PromptFiction" flaw in Claude could enable end-to-end AI agent compromise when chained with other exploits.

Law enforcement actions disrupted major financial crime infrastructure. Dutch police dismantled an investment fraud ring with tens of thousands of victims and €100M+ in losses, while Spanish authorities took down a €140M cyber fraud operation combining investment fraud and business email compromise. U.S. prosecutors charged three Russian nationals for operating bulletproof hosting services that facilitated over $62M in ransomware damage. Identity-based attacks have now surpassed exploits as the primary ransomware root cause, with MFA failing to prevent compromise in 97% of credential-based incidents.

## Active Exploitation Details

### SonicWall SMA 1000 Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting SonicWall Secure Mobile Access (SMA) 1000 series appliances. One vulnerability enables arbitrary command execution with administrative privileges.
- **Impact**: Attackers can achieve full administrative control over affected VPN appliances, potentially accessing internal networks, stealing credentials, and pivoting to connected systems.
- **Status**: Actively exploited in the wild. SonicWall has released emergency patches and urges immediate installation.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Mozilla Firefox Critical Vulnerability
- **Description**: An invalid pointer dereference flaw in Firefox that Mozilla has confirmed has published exploit code available.
- **Impact**: Remote code execution potential through malicious web content, allowing attackers to compromise user systems via browser exploitation.
- **Status**: Exploit code publicly available. Mozilla has released emergency updates addressing this and another critical flaw.
- **CVE ID**: CVE-2026-15718

### Microsoft SharePoint Server Vulnerabilities
- **Description**: Three vulnerabilities affecting Internet-exposed on-premises SharePoint Server installations that CISA has confirmed are under active exploitation.
- **Impact**: Remote code execution and system compromise of SharePoint servers, providing attackers footholds in organizational networks.
- **Status**: Actively exploited. CISA has added these to the Known Exploited Vulnerabilities catalog and mandated immediate patching for federal agencies.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Microsoft Windows Zero-Days (Patch Tuesday)
- **Description**: Two zero-day vulnerabilities among 622 flaws patched in Microsoft's largest Patch Tuesday release on record, both confirmed under active attack at time of patching.
- **Impact**: System compromise, privilege escalation, and potential domain takeover depending on specific vulnerability.
- **Status**: Patched as of July 2026 Patch Tuesday. Two additional zero-days were disclosed but not actively exploited at release.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Windows LegacyHive Zero-Day
- **Description**: A Windows User Profile Service arbitrary hive load vulnerability dubbed "LegacyHive," with proof-of-concept exploit code released by researcher Chaotic Eclipse (Nightmare-Eclipse) hours after Patch Tuesday.
- **Impact**: Local privilege escalation and potential system compromise through manipulation of user profile hive loading.
- **Status**: Public PoC available. No patch available at time of disclosure; mitigation guidance pending.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Zoom Desktop Client Account Takeover
- **Description**: Critical vulnerability in Zoom's desktop client and Windows SDK allowing unauthenticated account hijacking.
- **Impact**: Full account takeover without authentication, potentially enabling meeting hijacking, data theft, and further social engineering.
- **Status**: Zoom has issued warnings and is deploying fixes. Exploitation status in wild not explicitly confirmed but risk assessed as critical.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Cursor IDE Code Execution Vulnerabilities
- **Description**: Two distinct flaws in Cursor IDE on Windows: a "2-click" exploit enabling dev environment takeover, and automatic execution of any `git.exe` file present in a cloned repository's root directory without user interaction.
- **Impact**: Arbitrary code execution on developer machines, theft of source code, credentials, and secrets, supply chain compromise potential.
- **Status**: Publicly disclosed with technical details. Patch status unclear from reporting.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### AsyncAPI npm Supply Chain Attack
- **Description**: Five malicious versions of AsyncAPI packages published to npm delivering a multi-stage botnet loader with remote access and information-stealing capabilities.
- **Impact**: Compromise of development environments, credential theft, persistent botnet enrollment, potential downstream supply chain contamination.
- **Status**: Malicious packages identified and reported by multiple security firms (OX Security, SafeDep, Socket, StepSecurity). Removal from npm underway.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### UEFI Shim Bootloader Secure Boot Bypass
- **Description**: Nearly a dozen vulnerable and revoked UEFI shim bootloaders remained trusted in the UEFI revocation database (dbx) for years, creating a persistent Secure Boot bypass vector.
- **Impact**: Bootkit installation, pre-OS persistence, evasion of Secure Boot protections, firmware-level compromise.
- **Status**: Bootloaders now revoked, but window of exposure spanned years. Affected systems require firmware/dbx updates.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Claude "PromptFiction" Vulnerability
- **Description**: A flaw in Anthropic's Claude that automatically sends malicious prompts to AI agents, which when combined with another exploit could enable end-to-end system compromise.
- **Impact**: AI agent hijacking, potential lateral movement through agent-enabled systems, automated attack chain execution.
- **Status**: Fixed by Anthropic. Exploitation requires chaining with additional vulnerability.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

## Affected Systems and Products

- **SonicWall SMA 1000 Series Appliances**: All firmware versions prior to emergency patch release; Secure Mobile Access VPN appliances exposed to internet
- **Mozilla Firefox**: All versions prior to emergency security update; affects desktop and potentially ESR releases
- **Microsoft SharePoint Server**: On-premises installations (2016, 2019, Subscription Edition) exposed to internet; SharePoint Online unaffected
- **Microsoft Windows**: All supported versions (Windows 10, 11, Server 2016/2019/2022) for Patch Tuesday flaws; LegacyHive affects User Profile Service across versions
- **Zoom Desktop Client for Windows**: Versions prior to security update; Zoom SDK for Windows integrations
- **Cursor IDE (Windows)**: All versions exhibiting the git.exe auto-execution behavior and 2-click exploit path
- **AsyncAPI npm Packages**: `@asyncapi` namespace packages versions 2.6.0, 2.6.1, 3.0.0, 3.0.1, 3.0.2 published during compromise window
- **UEFI Shim Bootloaders**: Multiple third-party shim bootloaders (Canonical, Red Hat, SUSE, Debian, and others) with revoked but previously trusted signatures
- **Anthropic Claude**: Versions prior to PromptFiction fix; AI agent integrations using Claude API
- **IoT Devices (TuxBot v3)**: Linux-based IoT devices with exposed SSH/Telnet, weak credentials, unpatched vulnerabilities
- **Hardware Wallet Users (OkoBot)**: Windows users of Ledger Live and Trezor Suite applications
- **Google Gemini CLI**: Open-source Gemini CLI tool installations used in development environments

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active targeting of unpatched vulnerabilities in perimeter appliances (SonicWall SMA 1000), browsers (Firefox), and enterprise servers (SharePoint) before or immediately after patch availability
- **Supply Chain Compromise**: Malicious package publishing to npm registry under legitimate `@asyncapi` scope, delivering multi-stage botnet loader with RAT and info-stealer capabilities
- **AI Tool Weaponization**: Google Gemini CLI repurposed as autonomous hacking agent for reconnaissance, exploitation, and botnet command-and-control by threat actor "bandcampro"
- **LLM-Assisted Malware Development**: TuxBot v3 IoT botnet framework shows code patterns and complexity suggesting large language model assistance in development
- **IDE Auto-Execution**: Cursor IDE automatically executes `git.exe` from cloned repository root without prompt, enabling supply chain attacks via malicious repositories
- **Developer Environment Targeting**: 2-click exploit chain in Cursor leverages "age-old bugs" to access secrets, source code, and credentials in developer workstations
- **AI Agent Prompt Injection**: "PromptFiction" vulnerability in Claude enables malicious prompt forwarding to connected AI agents, creating chained exploitation paths
- **Secure Boot Bypass via Revoked Bootloaders**: Exploitation of UEFI dbx trust failures where revoked shim bootloaders remained usable for years
- **Hardware Wallet Phishing Injection**: OkoBot malware injects seed phrase phishing overlays into legitimate Ledger Live and Trezor Suite application windows
- **Bulletproof Hosting Infrastructure**: Russian-operated hosting services providing resilient infrastructure for ransomware gangs, enabling $62M+ in documented damages
- **Identity-Based Ransomware Access**: Credential theft, MFA bypass (97% failure rate in preventing compromise), and business email compromise as primary ransomware entry vectors
- **Investment Fraud & BEC Operations**: Large-scale social engineering campaigns combining fake investment platforms with business email compromise for financial theft (€100M+ and €140M+ rings)
- **Automated Frequency Coordination Spoofing**: 6 GHz Wi-Fi AFC system vulnerabilities allowing client-side location data spoofing to disrupt critical wireless systems

## Threat Actor Activities

- **bandcampro (Russian-speaking)**: Active exploitation using Google Gemini CLI as both automated hacking agent and botnet C2 operator; demonstrates AI tool dual-use for offensive operations
- **SonicWall Zero-Day Actors (Unattributed)**: Active exploitation of CVE-2026-15409 and CVE-2026-15410 against SMA 1000 appliances; capability suggests sophisticated actor with zero-day access
- **SharePoint Exploitation Groups (Unattributed)**: Active targeting of internet-exposed on-premises SharePoint servers using three confirmed exploited vulnerabilities; CISA KEV listing indicates ongoing campaign
- **Firefox Exploit Publishers (Unattributed)**: Public exploit code release for CVE-2026-15718 increases risk of drive-by and targeted browser exploitation campaigns
- **Chaotic Eclipse / Nightmare-Eclipse**: Security researcher who publicly released LegacyHive Windows zero-day PoC hours after Patch Tuesday; responsible disclosure status unclear
- **AsyncAPI Supply Chain Attackers (Unattributed)**: Compromised npm publishing credentials or CI/CD pipeline to inject malicious code into legitimate package namespace; multi-stage botnet deployment indicates financially motivated operation
- **TuxBot v3 Developers (Unattributed)**: IoT botnet operators showing LLM-assisted development patterns; targeting Linux IoT devices for DDoS, proxy, and credential harvesting capabilities
- **OkoBot Operators (Unattributed)**: Active since April 2025; Windows malware framework with specialized module for hardware wallet seed phrase phishing via application injection
- **Russian Bulletproof Hosting Operators**: Three charged Russian nationals (names per DOJ indictment) providing dedicated hosting for ransomware affiliates; enabled $62M+ in verified ransomware damages
- **Dutch Investment Fraud Network**: International organized crime group arrested by Dutch police; tens of thousands of victims, €100M+ stolen via fake investment platforms
- **Spanish Cyber Fraud Ring**: Dismantled by Spanish National Police; €140M from combined investment fraud and business email compromise operations; four arrests
- **Microsoft Zero-Day Exploiters (Unattributed)**: Two distinct zero-days under active attack at time of July 2026 Patch Tuesday; actor sophistication implied by pre-patch exploitation

## Source Attribution

- **Dutch police bust investment fraud ring stealing over €100 million**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/dutch-police-bust-investment-fraud-ring-stealing-over-100-million/
- **Forgotten Bootloaders Expose Secure Boot Blind Spot**: Dark Reading - https://www.darkreading.com/cyber-risk/forgotten-bootloaders-expose-secure-boot-blind-spot
- **Identity Attacks Overtake Exploits as Top Ransomware Cause**: Dark Reading - https://www.darkreading.com/identity-access-management-security/identity-attacks-overtake-exploits-top-ransomware-cause
- **Zoom warns of critical account takeover vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/zoom-warns-of-critical-account-takeover-vulnerability/
- **TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development**: The Hacker News - https://thehackernews.com/2026/07/tuxbot-v3-evolution-shows-signs-of-llm.html
- **Google Gemini CLI abused as a hacking agent, malware botnet operator**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/google-gemini-cli-abused-as-a-hacking-agent-malware-botnet-operator/
- **Guten Tag, Bonjour, Hola to Our European Cyber Defenders!**: Dark Reading - https://www.darkreading.com/threat-intelligence/guten-tag-bonjour-hola-european-cyber-defenders
- **Is 'Tech-xit' Imminent? UK Steps Up Sovereignty Push Amid AI Strife**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/tech-xit-uk-sovereignty-push-amid-ai-strife
- **AsyncAPI npm packages infected with credential-stealing malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/-asyncapi-npm-packages-infected-with-credential-stealing-malware/
- **OkoBot Malware Framework Injects Seed Phrase Phishing Into Ledger and Trezor Apps**: The Hacker News - https://thehackernews.com/2026/07/okobot-malware-framework-injects-seed.html
- **Claude Flaw Automatically Sends Malicious Prompts to AI Agents**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/claude-flaw-malicious-prompts-ai-agents
- **We built a vulnerability vending machine: AI tokens in, zero-days out**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/we-built-a-vulnerability-vending-machine-ai-tokens-in-zero-days-out/
- **Firefox, Chrome, Adobe, and VMware Updates Fix Multiple Critical Security Flaws**: The Hacker News - https://thehackernews.com/2026/07/firefox-chrome-adobe-and-vmware-updates.html
- **2-Click Cursor Exploit Enables Dev Environment Takeover**: Dark Reading - https://www.darkreading.com/application-security/2-click-cursor-exploit-dev-environment-takeover
- **SASE Has An AI Blind Spot. Inspecting Packets Is No Longer Enough.**: The Hacker News - https://thehackernews.com/2026/07/sase-has-ai-blind-spot-inspecting.html
- **Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday**: The Hacker News - https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html
- **New Webinar: Closing the Approval Gap in AI-Era Ad Tech**: The Hacker News - https://thehackernews.com/2026/07/new-webinar-closing-approval-gap-in-ai.html
- **Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution**: The Hacker News - https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html
- **CISA warns admins to patch actively exploited SharePoint flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-patch-actively-exploited-sharepoint-flaws/
- **Compromised AsyncAPI npm Packages Deliver Multi-Stage Botnet Malware**: The Hacker News - https://thehackernews.com/2026/07/compromised-asyncapi-npm-packages.html
- **Microsoft: Some Dell PCs shut down after recent Windows updates**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-some-dell-devices-shut-down-after-windows-update/
- **Nigeria Deepens Cybersecurity Efforts as Cybercriminals See More Profits**: Dark Reading - https://www.darkreading.com/cyber-risk/nigeria-cybersecurity-efforts-cybercriminals-profits
- **US charges alleged operators of Russian bulletproof hosting service**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-alleged-russian-bulletproof-hosting-service-operators/
- **Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands**: The Hacker News - https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html
- **Cribl Adds Agentic Detection Engineering \&amp; Boosts SecOps With CardinalOps Deal**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cribl-adds-agentic-detection-engineering-boosts-secops-with-cardinalops-deal
- **Records Are Made to Be Broken: Patch Tuesday Raises Triage Stakes**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/records-broken-patch-tuesday-raises-triage-stakes
- **SonicWall warns of SMA1000 flaws exploited in zero-day attacks, patch now**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-sma1000-flaws-exploited-in-zero-day-attacks-patch-now/
- **Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack**: The Hacker News - https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html
- **Spanish Police take down €140 million cyber fraud ring, arrest four**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/spanish-police-take-down-140-million-cyber-fraud-ring-arrest-four/
- **6 GHz Wi-Fi Flaws Could Disrupt Critical Systems**: Dark Reading - https://www.darkreading.com/perimeter/6-ghz-wi-fi-flaws-disrupt-critical-systems
