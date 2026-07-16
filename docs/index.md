# Exploitation Report

## Executive Summary

Critical exploitation activity surged in July 2026 with multiple zero-day vulnerabilities under active attack across diverse platforms. SonicWall SMA 1000 appliances face exploitation of two zero-day flaws (CVE-2026-15409 and CVE-2026-15410), with one enabling arbitrary command execution as administrator. Microsoft's record-breaking Patch Tuesday addressed 622 vulnerabilities including two actively exploited zero-days, while Mozilla confirmed exploit code exists for critical Firefox flaws including CVE-2026-15718. CISA simultaneously warned of active exploitation targeting three vulnerabilities in internet-exposed on-premises SharePoint Server instances.

Supply chain attacks and AI-enabled threat activity represent escalating risks. A compromised AsyncAPI npm package campaign delivered multi-stage botnet malware through the official registry, while a Russian-speaking actor ("bandcampro") weaponized Google's Gemini CLI as both a hacking agent and botnet command infrastructure. Researchers demonstrated an AI-powered "vulnerability vending machine" capable of automatically discovering complex flaws, and a new Windows zero-day PoC (LegacyHive) was released hours after Patch Tuesday by researcher Chaotic Eclipse.

Identity-based attacks have overtaken exploitation as the primary ransomware root cause, with MFA failing to prevent compromise in 97% of credential-based incidents. Law enforcement achieved significant victories: Dutch police dismantled a €100 million investment fraud ring, Spanish authorities took down a €140 million cyber fraud operation combining investment scams and business email compromise, and U.S. prosecutors charged three Russian nationals for operating bulletproof hosting services enabling over $62 million in ransomware damages.

## Active Exploitation Details

### SonicWall SMA 1000 Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting SonicWall Secure Mobile Access (SMA) 1000 series appliances. One vulnerability allows arbitrary command execution with administrative privileges, while the second provides an additional attack vector. Both flaws were exploited in the wild before patches were available.
- **Impact**: Attackers can achieve full administrative control over affected SMA 1000 appliances, enabling network access, traffic interception, credential theft, and lateral movement into connected environments.
- **Status**: Actively exploited in zero-day attacks. SonicWall has released emergency patches and urges immediate installation. CISA and vendor advisories recommend prioritizing deployment.
- **CVE ID**: CVE-2026-15409
- **CVE ID**: CVE-2026-15410

### Microsoft July Patch Tuesday Zero-Days
- **Description**: Two zero-day vulnerabilities among 622 total CVEs patched in Microsoft's largest Patch Tuesday release on record. Specific vulnerability types not disclosed in available reporting, but confirmed under active exploitation at time of patch release.
- **Impact**: Active exploitation confirmed; impact varies by vulnerability but includes potential for remote code execution, privilege escalation, and security feature bypass across Windows and Microsoft product ecosystem.
- **Status**: Patched in July 2026 security updates. Three total zero-days addressed in this release (two under active attack, one publicly known). More than 60 critical vulnerabilities included in the 622-fix release.
- **CVE ID**: Specific CVE IDs for the two actively exploited zero-days not provided in source articles.

### Firefox Critical Vulnerabilities with Published Exploit Code
- **Description**: Mozilla released emergency updates addressing two critical vulnerabilities in Firefox for which exploit code has been publicly published. One identified flaw involves an invalid pointer handling issue.
- **Impact**: Remote code execution potential through malicious web content. Published exploit code significantly increases risk for unpatched installations.
- **Status**: Patched in latest Firefox releases. Mozilla explicitly warned that exploit code exists for these vulnerabilities.
- **CVE ID**: CVE-2026-15718

### Actively Exploited SharePoint Server Vulnerabilities
- **Description**: Three vulnerabilities in on-premises Microsoft SharePoint Server that are being actively exploited against internet-exposed instances. CISA issued an emergency directive urging immediate patching.
- **Impact**: Compromise of SharePoint servers accessible from the internet, potentially leading to data exfiltration, credential theft, and internal network access.
- **Status**: Actively exploited per CISA warning. Patches available; administrators urged to apply immediately or restrict internet exposure.
- **CVE ID**: Specific CVE IDs not provided in source article excerpt.

### Zoom Critical Account Takeover Vulnerability
- **Description**: Critical vulnerability in Zoom's desktop client and Software Development Kit (SDK) for Windows that allows unauthenticated attackers to hijack user accounts.
- **Impact**: Full account takeover without authentication, enabling access to meetings, recordings, contacts, and potential further social engineering or data theft.
- **Status**: Zoom has issued warnings and patches. Vulnerability affects Windows desktop client and SDK implementations.

### Cursor IDE Repository Code Execution Flaw
- **Description**: Design flaw in Cursor (AI-powered code editor) on Windows where the application automatically executes any file named `git.exe` present in a cloned repository's root directory, without user interaction, approval dialogs, or warnings.
- **Impact**: Arbitrary code execution when developers open malicious repositories. Attackers can embed malicious `git.exe` binaries in repositories distributed via GitHub, GitLab, or other sources.
- **Status**: Active exploitation vector demonstrated. Related "2-click" exploit variant also enables developer environment takeover through simple bugs.

### AsyncAPI npm Supply Chain Attack
- **Description**: Five malicious versions of AsyncAPI packages published to the npm registry under the `@asyncapi` namespace, delivering a multi-stage remote access trojan with credential-stealing and botnet capabilities.
- **Impact**: Compromise of development environments and build systems. Info-stealing capabilities target credentials, tokens, and sensitive data. Botnet functionality enables persistent access and further payload deployment.
- **Status**: Malicious packages identified and reported by OX Security, SafeDep, Socket, and StepSecurity. Four compromised packages confirmed in `@asyncapi` namespace.

### OkoBot Hardware Wallet Phishing Framework
- **Description**: Malware framework active since April 2025 targeting Windows users of Ledger and Trezor hardware wallets. Injects seed phrase phishing prompts into legitimate wallet applications to steal recovery phrases.
- **Impact**: Complete cryptocurrency wallet compromise. Recovery phrase theft enables full control of victim's digital assets across all supported blockchains.
- **Status**: Active in the wild since April 2025. Targets users of major hardware wallet vendors through application injection techniques.

### TuxBot v3 IoT Botnet with LLM-Assisted Development
- **Description**: Previously unreported IoT botnet framework showing indicators of large language model (LLM) assistance in its development. Represents evolution in automated malware creation capabilities.
- **Impact**: Compromise of Internet-of-Things devices for DDoS, proxy networks, credential harvesting, and lateral movement. LLM-assisted development suggests accelerating malware sophistication.
- **Status**: Active botnet framework under observation by researchers. Indicates emerging trend of AI-augmented threat actor tooling.

### Google Gemini CLI Weaponization
- **Description**: Russian-speaking threat actor "bandcampro" abused Google's open-source Gemini CLI (command-line interface) AI tool as both an automated hacking agent and as command-and-control infrastructure for a small-scale botnet operation.
- **Impact**: Legitimate AI development tool repurposed for vulnerability scanning, exploitation, and botnet management. Demonstrates dual-use risk of accessible AI coding agents.
- **Status**: Observed in active operations. Highlights growing threat of AI tool misuse by threat actors.

### Windows LegacyHive Zero-Day PoC
- **Description**: Security researcher Chaotic Eclipse (aka Nightmare-Eclipse) released a proof-of-concept exploit called "LegacyHive" targeting the Windows User Profile Service arbitrary hive loading functionality, hours after Microsoft's July Patch Tuesday.
- **Impact**: Potential privilege escalation and arbitrary code execution through manipulation of user profile hive loading mechanisms.
- **Status**: PoC publicly released. No patch mentioned in source; likely unpatched at time of disclosure.

### Claude "PromptFiction" AI Agent Vulnerability
- **Description**: Vulnerability dubbed "PromptFiction" in Anthropic's Claude that could automatically send malicious prompts to connected AI agents. When chained with another exploit, enables end-to-end system compromise.
- **Impact**: AI agent manipulation leading to unauthorized actions, data access, or system compromise in environments using Claude with agent frameworks.
- **Status**: Fixed per reporting. Demonstrates emerging attack surface in AI agent architectures.

## Affected Systems and Products

- **SonicWall SMA 1000 Series Appliances**: Secure Mobile Access 1000 series firmware versions prior to emergency patches for CVE-2026-15409 and CVE-2026-15410
- **Microsoft Windows and Server Ecosystem**: All supported Windows versions, SharePoint Server on-premises (internet-exposed instances), and Microsoft 365 components covered by July 2026 Patch Tuesday (622 CVEs)
- **Mozilla Firefox**: All Firefox desktop versions prior to critical security updates addressing CVE-2026-15718 and companion critical flaw
- **Zoom Desktop Client and SDK for Windows**: Zoom Windows desktop application and Software Development Kit implementations vulnerable to unauthenticated account takeover
- **Cursor AI Code Editor (Windows)**: All Windows versions of Cursor IDE that automatically execute `git.exe` from repository root directories
- **AsyncAPI npm Packages**: `@asyncapi` namespace packages versions 1.0.0 through 1.0.4 (malicious versions published to npm registry)
- **Ledger and Trezor Hardware Wallet Desktop Applications**: Windows desktop companion apps for Ledger and Trezor hardware wallets targeted by OkoBot seed phrase injection
- **IoT Devices Running Vulnerable Firmware**: Broad range of Internet-of-Things devices susceptible to TuxBot v3 botnet recruitment
- **Google Gemini CLI Users**: Developers and organizations using Google's open-source Gemini CLI tool, particularly in automated CI/CD or agent workflows
- **Anthropic Claude AI Agent Integrations**: Systems utilizing Claude with autonomous agent frameworks prior to PromptFiction fix

## Attack Vectors and Techniques

- **Zero-Day Exploitation of Network Edge Devices**: Active targeting of SonicWall SMA 1000 VPN/appliance endpoints using two previously unknown vulnerabilities (CVE-2026-15409, CVE-2026-15410) for initial access and administrative command execution
- **Supply Chain Compromise via Package Registry**: Malicious code injection into legitimate AsyncAPI npm packages published to official registry, delivering multi-stage botnet loader to downstream developers and build systems
- **AI Tool Weaponization**: Repurposing of Google Gemini CLI as autonomous hacking agent for vulnerability discovery, exploitation, and botnet command-and-control by threat actor "bandcampro"
- **Developer Environment Targeting**: Exploitation of Cursor IDE's automatic `git.exe` execution behavior to achieve code execution when developers clone malicious repositories
- **Identity-Based Ransomware Access**: Credential theft, phishing, and MFA bypass (97% failure rate in credential attacks) now surpassing vulnerability exploitation as primary ransomware initial access vector
- **Hardware Wallet Application Injection**: OkoBot malware injects phishing prompts into legitimate Ledger/Trezor desktop applications to extract cryptocurrency seed phrases
- **AI Agent Prompt Injection**: "PromptFiction" vulnerability enabling malicious prompt chaining to compromise AI agent autonomy and connected system access
- **LLM-Assisted Malware Development**: TuxBot v3 botnet shows indicators of large language model usage in code generation, accelerating IoT malware sophistication
- **Automated Vulnerability Discovery**: AI-powered "vulnerability vending machine" combining code slicing with LLMs to automatically discover complex software vulnerabilities
- **Business Email Compromise (BEC) and Investment Fraud**: Large-scale social engineering operations (€100M+ and €140M+ rings) combining impersonation, financial fraud, and money laundering
- **Bulletproof Hosting Infrastructure**: Russian-hosted resilient infrastructure enabling ransomware operations causing $62M+ in documented damages
- **Secure Boot Bypass via Revoked Bootloaders**: Exploitation of nearly a dozen vulnerable UEFI shim bootloaders that remained trusted for years despite revocation

## Threat Actor Activities

- **bandcampro (Russian-speaking)**: Weaponized Google Gemini CLI as automated hacking agent and botnet operator. Demonstrates individual actor leveraging accessible AI tools for end-to-end attack automation including vulnerability scanning, exploitation, and C2 management.
- **Chaotic Eclipse / Nightmare-Eclipse (Security Researcher)**: Released LegacyHive Windows zero-day PoC hours after Microsoft Patch Tuesday. Researcher disclosure timing raises questions about responsible disclosure vs. public weaponization.
- **OkoBot Operators (Unknown)**: Deployed persistent Windows malware framework since April 2025 targeting cryptocurrency hardware wallet users through application injection and seed phrase phishing. Financially motivated.
- **TuxBot v3 Developers (Unknown, likely LLM-assisted)**: Created sophisticated IoT botnet framework showing hallmarks of AI-assisted code generation. Represents potential shift toward automated malware development pipelines.
- **AsyncAPI Supply Chain Attackers (Unknown)**: Compromised npm publishing credentials or CI/CD pipeline to inject malicious code into legitimate `@asyncapi` packages. Multi-stage botnet deployment suggests organized operation.
- **SonicWall SMA Exploiters (Unknown)**: Actively exploiting two zero-day vulnerabilities (CVE-2026-15409, CVE-2026-15410) against internet-exposed SMA 1000 appliances. Capability suggests advanced actor with zero-day access.
- **SharePoint Exploitation Actors (Unknown)**: Targeting internet-exposed on-premises SharePoint Server instances per CISA warning. Three vulnerabilities under active exploitation.
- **Dutch Investment Fraud Ring (Dismantled)**: International operation with tens of thousands of victims, €100M+ stolen. Multiple arrests by Dutch police.
- **Spanish Cyber Fraud Organization (Dismantled)**: Combined investment fraud and business email compromise (BEC) netting €140M ($160M). Four arrests by Spanish National Police.
- **Russian Bulletproof Hosting Operators (Charged)**: Three Russian nationals charged by U.S. prosecutors for providing resilient hosting infrastructure to ransomware gangs causing $62M+ in damages. Enabler ecosystem for ransomware-as-a-service.

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
