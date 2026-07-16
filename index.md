# Exploitation Report

## Executive Summary

Critical zero-day exploitation activity surged this period with active attacks targeting SonicWall SMA 1000 appliances, Microsoft Windows and SharePoint Server, and Mozilla Firefox. CISA issued an urgent warning for three actively exploited SharePoint vulnerabilities affecting internet-exposed on-premises servers, while SonicWall confirmed two zero-days (CVE-2026-15409 and CVE-2026-15410) under active exploitation—one enabling arbitrary command execution. Microsoft's record-breaking Patch Tuesday addressed 622 vulnerabilities including two zero-days already under attack, and Mozilla warned that exploit code has been published for CVE-2026-15718 in Firefox.

Simultaneously, supply chain and identity-based attacks continue to dominate the threat landscape. A compromise of AsyncAPI npm packages delivered multi-stage botnet malware through the Node Package Manager, while credential theft and MFA bypass have overtaken exploits as the leading ransomware root cause—with MFA present in 97% of compromised credential incidents. Threat actors are increasingly weaponizing AI tools, evidenced by the "bandcampro" group's use of Google's Gemini CLI as a hacking agent and botnet operator, and the emergence of LLM-assisted IoT botnet development in TuxBot v3 Evolution.

Law enforcement actions disrupted major cybercrime infrastructure: Dutch police dismantled a €100 million investment fraud ring with tens of thousands of victims, Spanish authorities took down a €140 million cyber fraud operation combining investment scams and business email compromise, and U.S. prosecutors charged three Russian nationals for operating bulletproof hosting services that facilitated over $62 million in ransomware damage. Meanwhile, researchers disclosed a Windows User Profile Service zero-day (LegacyHive PoC), critical flaws in Zoom and Cursor IDE enabling account takeover and developer environment compromise, and a Secure Boot bypass via revoked but still-trusted UEFI shim bootloaders.

## Active Exploitation Details

### SonicWall SMA 1000 Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting SonicWall Secure Mobile Access (SMA) 1000 series appliances. One vulnerability enables arbitrary command execution with administrative privileges.
- **Impact**: Attackers can achieve full administrative control over affected SMA 1000 appliances, potentially compromising VPN access and network segmentation.
- **Status**: Actively exploited in zero-day attacks. SonicWall has released patches and urges immediate installation.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Microsoft SharePoint Server Vulnerabilities
- **Description**: Three vulnerabilities affecting internet-exposed on-premises SharePoint Server installations.
- **Impact**: Attackers are actively exploiting these flaws to compromise SharePoint servers, potentially leading to data theft, lateral movement, and persistent access.
- **Status**: Actively exploited in the wild. CISA has issued an urgent warning for administrators to patch immediately.
- **CVE ID**: [CVE IDs not specified in source article snippets]

### Microsoft Windows Zero-Days (Patch Tuesday July 2026)
- **Description**: Two zero-day vulnerabilities among 622 total CVEs patched in Microsoft's largest Patch Tuesday on record. Over 60 vulnerabilities rated critical.
- **Impact**: Active exploitation confirmed for two zero-days; critical vulnerabilities across Windows components, Office, and other Microsoft products.
- **Status**: Patches released. Two zero-days were under active attack at time of patch release.
- **CVE ID**: [Specific zero-day CVE IDs not provided in source article snippets]

### Mozilla Firefox Critical Vulnerability
- **Description**: Critical vulnerability in Firefox for which exploit code has been published. Mozilla warned of active exploit availability.
- **Impact**: Remote code execution potential through crafted web content.
- **Status**: Exploit code published. Mozilla has released updates addressing this and another critical flaw.
- **CVE ID**: CVE-2026-15718

### Zoom Account Takeover Vulnerability
- **Description**: Critical vulnerability in Zoom desktop client and software development kit for Windows allowing unauthenticated account hijacking.
- **Impact**: Unauthenticated attackers can take over user accounts, potentially accessing meetings, recordings, and contact lists.
- **Status**: Zoom has issued warnings; patch status should be verified.
- **CVE ID**: [CVE ID not specified in source article snippet]

### Windows User Profile Service Zero-Day (LegacyHive)
- **Description**: Proof-of-concept exploit called "LegacyHive" released by researcher Chaotic Eclipse (Nightmare-Eclipse) targeting Windows User Profile Service arbitrary hive loading.
- **Impact**: Potential privilege escalation and persistence through malicious profile hive manipulation.
- **Status**: PoC released publicly hours after July Patch Tuesday; exploitation risk elevated.
- **CVE ID**: [CVE ID not specified in source article snippet]

### Cursor IDE Code Execution Flaws
- **Description**: Two distinct vulnerabilities in Cursor IDE on Windows: (1) a "2-click" exploit enabling developer environment takeover, and (2) automatic execution of `git.exe` if placed in a cloned repository root—no user interaction required.
- **Impact**: Attackers can steal developer secrets, source code, and execute arbitrary code via malicious repositories.
- **Status**: Active exploitation vector; developers opening cloned repositories at risk.
- **CVE ID**: [CVE IDs not specified in source article snippets]

### AsyncAPI npm Supply Chain Attack
- **Description**: Five malicious versions of AsyncAPI packages published to npm delivering a remote access trojan with credential-stealing and botnet capabilities. Four packages in the `@asyncapi` namespace confirmed compromised.
- **Impact**: Multi-stage botnet loader installation, credential theft, persistent access to development environments and CI/CD pipelines.
- **Status**: Malicious packages identified and reported by OX Security, SafeDep, Socket, and StepSecurity; removal from npm in progress.
- **CVE ID**: [CVE IDs not specified in source article snippets]

### UEFI Secure Boot Bypass via Revoked Shim Bootloaders
- **Description**: Nearly a dozen vulnerable and revoked UEFI shim bootloaders remained trusted in UEFI databases for years, creating a persistent Secure Boot bypass path.
- **Impact**: Attackers with physical or administrative access can boot unsigned code, deploy bootkits, and persist below the OS level despite Secure Boot being enabled.
- **Status**: Bootloaders now revoked; however, historical trust creates risk for systems not updated with latest dbx revocations.
- **CVE ID**: [CVE IDs not specified in source article snippet]

### OkoBot Hardware Wallet Phishing Framework
- **Description**: Malware framework active since April 2025 with a module that injects seed phrase phishing prompts into Ledger Live and Trezor Suite applications on infected Windows machines.
- **Impact**: Theft of cryptocurrency wallet recovery phrases, leading to complete wallet compromise and fund drainage.
- **Status**: Active malware campaign targeting hardware wallet users.
- **CVE ID**: [CVE ID not specified in source article snippet]

### Google Gemini CLI Abuse by Threat Actor
- **Description**: Russian-speaking threat actor "bandcampro" weaponized Google's open-source Gemini CLI AI tool as an autonomous hacking agent and botnet command-and-control mechanism.
- **Impact**: AI-assisted vulnerability scanning, exploitation, and botnet operations at scale with reduced operator overhead.
- **Status**: Active misuse of legitimate AI tooling; demonstrates emerging trend of LLM-assisted offensive operations.
- **CVE ID**: [CVE ID not applicable—abuse of legitimate tool]

### TuxBot v3 Evolution IoT Botnet
- **Description**: Previously unreported IoT botnet framework showing indicators of LLM-assisted development, targeting Internet-of-Things devices for botnet recruitment.
- **Impact**: Compromise of IoT devices for DDoS, proxy networks, and lateral movement into adjacent networks.
- **Status**: Active development and deployment; represents evolution of AI-augmented malware authoring.
- **CVE ID**: [CVE IDs not specified in source article snippet]

### Claude "PromptFiction" Vulnerability
- **Description**: Fixed vulnerability in Anthropic's Claude that could automatically send malicious prompts to connected AI agents, enabling end-to-end attack chains when combined with other exploits.
- **Impact**: Prompt injection leading to unauthorized actions by AI agents with system access.
- **Status**: Patched by Anthropic; demonstrates emerging AI agent attack surface.
- **CVE ID**: [CVE ID not specified in source article snippet]

## Affected Systems and Products

- **SonicWall SMA 1000 Series Appliances**: Secure Mobile Access 1000 series firmware versions prior to patched releases; both CVE-2026-15409 and CVE-2026-15410 affect the appliance management interface.
- **Microsoft SharePoint Server**: On-premises SharePoint Server installations exposed to the internet; specific affected versions include SharePoint Server 2016, 2019, and Subscription Edition per CISA guidance.
- **Microsoft Windows**: Broad impact across Windows 10, Windows 11, Windows Server 2016/2019/2022; 622 CVEs patched including kernel, networking, Office, Hyper-V, and cryptographic components.
- **Mozilla Firefox**: Firefox desktop versions prior to the July 2026 security update; CVE-2026-15718 specifically affects the browser rendering engine.
- **Zoom Desktop Client and SDK**: Windows versions of Zoom Client for Meetings and the Windows SDK; unauthenticated remote attack vector.
- **Cursor IDE**: Windows versions of the Cursor AI-powered code editor; affects developers cloning untrusted repositories.
- **AsyncAPI npm Packages**: `@asyncapi` namespace packages versions 2.6.0, 2.6.1, 2.6.2, 2.6.3, 2.6.4 (malicious versions); Node.js development environments and CI/CD pipelines consuming these packages.
- **UEFI Shim Bootloaders**: Revoked shim bootloaders from multiple vendors (including but not limited to Canonical, Red Hat, SUSE, Debian) that remained in UEFI trusted databases; affects x64 and ARM64 systems with Secure Boot enabled.
- **Ledger Live and Trezor Suite**: Desktop companion applications for Ledger and Trezor hardware wallets on Windows; targeted by OkoBot's seed phrase phishing module.
- **Google Gemini CLI**: Open-source command-line interface for Google Gemini AI; abused as offensive tooling rather than vulnerability in the tool itself.
- **IoT Devices (TuxBot v3 Targets)**: Linux-based IoT devices (routers, cameras, DVRs, smart appliances) with exposed management interfaces or default credentials.
- **Anthropic Claude AI Agents**: Systems integrating Claude with agent frameworks allowing autonomous tool use; patched server-side.

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in SonicWall SMA 1000 (CVE-2026-15409, CVE-2026-15410), Microsoft Windows (two zero-days), and Firefox (CVE-2026-15718 with public exploit code).
- **Supply Chain Compromise**: Malicious publication of AsyncAPI npm packages to the official Node Package Manager registry, delivering multi-stage botnet loaders to downstream consumers.
- **AI Tool Weaponization**: Repurposing of Google's Gemini CLI as an autonomous hacking agent for vulnerability scanning, exploitation, and botnet C2 by threat actor "bandcampro."
- **LLM-Assisted Malware Development**: Use of large language models to accelerate IoT botnet framework development (TuxBot v3 Evolution), reducing time-to-weaponization.
- **Developer Environment Targeting**: Exploitation of Cursor IDE flaws via malicious cloned repositories (automatic `git.exe` execution) and 2-click attacks to steal secrets and source code.
- **Secure Boot Bypass**: Leveraging revoked but still-trusted UEFI shim bootloaders to load unsigned kernels/bootkits, persisting below OS security controls.
- **Identity-Based Attacks**: Credential theft, phishing, and MFA bypass (including MFA fatigue, token theft, and adversary-in-the-middle) now the primary ransomware initial access vector—MFA deployed in 97% of compromised credential incidents.
- **Hardware Wallet Phishing**: Malware-injected prompts in legitimate Ledger Live/Trezor Suite applications tricking users into entering seed phrases on compromised hosts.
- **Prompt Injection / AI Agent Manipulation**: "PromptFiction" vulnerability enabling malicious prompt chaining to AI agents with tool-use capabilities.
- **Bulletproof Hosting Infrastructure**: Russian-hosted resilient infrastructure (charged operators) providing ransomware gangs with attack hosting, C2, and data exfiltration services.
- **Business Email Compromise (BEC)**: Combined with investment fraud in Spanish and Dutch law enforcement cases; social engineering for financial transfer fraud.
- **Investment Fraud / Pig Butchering**: Large-scale social engineering campaigns (€100M+ and €140M+ rings) using fake investment platforms and romance/trust-building tactics.

## Threat Actor Activities

- **bandcampro**: Russian-speaking threat actor abusing Google Gemini CLI as a hacking agent and botnet operator; demonstrates AI tool repurposing for offensive automation.
- **Russian Bulletproof Hosting Operators**: Three charged Russian nationals (names not disclosed in snippets) providing bulletproof hosting services to ransomware gangs; infrastructure linked to over $62 million in ransomware damage.
- **Dutch Investment Fraud Ring**: International fraud network arrested by Dutch Police; estimated tens of thousands of victims, €100 million+ stolen through fake investment platforms.
- **Spanish Cyber Fraud Organization**: Dismantled by Spanish Police; €140 million ($160 million) from combined investment fraud and business email compromise operations; four arrests reported.
- **TuxBot v3 Developers**: Unknown operators behind LLM-assisted IoT botnet framework; code artifacts suggest AI-augmented development workflow.
- **OkoBot Operators**: Active since April 2025; Windows malware framework operators targeting cryptocurrency holders via hardware wallet seed phrase phishing.
- **AsyncAPI Supply Chain Attackers**: Unknown threat actor(s) who compromised npm publishing credentials for the `@asyncapi` scope; delivered multi-stage botnet malware to developers.
- **Chaotic Eclipse / Nightmare-Eclipse**: Security researcher who publicly released the "LegacyHive" Windows User Profile Service zero-day PoC hours after July Patch Tuesday.
- **SonicWall SMA 1000 Exploiters**: Unidentified threat actors actively exploiting CVE-2026-15409 and CVE-2026-15410 in zero-day attacks against internet-exposed appliances.
- **SharePoint Exploiters**: Unidentified actors actively targeting internet-exposed on-premises SharePoint servers per CISA alert; likely initial access brokers or ransomware affiliates.
- **Microsoft Zero-Day Exploiters**: Unidentified actors exploiting two zero-days patched in July 2026 Patch Tuesday; active exploitation confirmed prior to patch release.

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
