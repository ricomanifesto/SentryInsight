# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited in the wild, with CISA issuing an emergency directive for federal agencies to patch an Oracle E-Business Suite flaw under active attack. Zoom has released patches for a critical account takeover vulnerability (CVE-2026-53412) affecting Windows clients, while Mozilla confirmed exploit code has been published for a Firefox flaw (CVE-2026-15718). These actively exploited vulnerabilities span enterprise applications, browsers, and communication platforms, requiring immediate patching.

Threat actor activity remains high across multiple fronts. The Scattered Spider cybercrime collective saw two members sentenced for the 2024 Transport for London breach, while a Russian financially motivated actor (UAT-11795) is distributing the new Starland RAT through trojanized WebEx and Zoom installers. The PhantomEnigma campaign compromised over 20 Brazilian government websites for malware delivery, and China-linked Daxin malware has resurfaced in Taiwan alongside a previously unknown Stupig backdoor. A new ransomware actor, Spirals, demonstrates alarming speed—completing full intrusion-to-encryption cycles in under 24 hours.

Novel attack vectors are emerging rapidly. The ClickFix social engineering technique continues to evolve, now delivering the modular TELEPUZ malware and the ClickLock macOS stealer that forcibly kills applications until victims surrender passwords. AI agents face new "Agent Data Injection" attacks that can hijack autonomous behavior, while the "PromptFiction" vulnerability in Claude demonstrated cross-exploit potential. Supply chain compromise hit the npm ecosystem via malicious AsyncAPI packages, and an IoT botnet framework (TuxBot v3) shows evidence of LLM-assisted development. Even hardware devices are at risk—an unpatched Shark vacuum flaw allows cross-device control via extracted certificates.

## Active Exploitation Details

### Oracle E-Business Suite Critical Vulnerability
- **Description**: A critical vulnerability in Oracle E-Business Suite financial application that is being actively exploited in the wild. CISA has added this to the Known Exploited Vulnerabilities catalog and issued an emergency directive.
- **Impact**: Attackers can compromise federal systems running Oracle E-Business Suite, potentially leading to financial data theft, unauthorized transactions, and lateral movement within enterprise networks.
- **Status**: Actively exploited. CISA ordered federal civilian executive branch agencies to secure systems by Saturday (July 2026). Patch availability implied by CISA directive.
- **CVE ID**: Not specified in source article

### Zoom Workplace for Windows Account Takeover (CVE-2026-53412)
- **Description**: A critical security flaw in Zoom Workplace for Windows and the Zoom SDK for Windows that could allow an unauthenticated attacker to hijack user accounts.
- **Impact**: Full account takeover without authentication, enabling attackers to access meetings, recordings, contacts, and potentially pivot to other systems.
- **Status**: Patched. Zoom has released security updates addressing the vulnerability. Exploit code publication status not explicitly confirmed but severity suggests urgent patching required.
- **CVE ID**: CVE-2026-53412

### Firefox Critical Vulnerability (CVE-2026-15718)
- **Description**: An invalid pointer dereference vulnerability in Firefox that Mozilla has rated critical. Mozilla explicitly warned that exploit code has been published for this flaw.
- **Impact**: Remote code execution potential through crafted web content. Published exploit code significantly increases risk to unpatched systems.
- **Status**: Patched in Firefox updates. Exploit code publicly available—immediate patching critical.
- **CVE ID**: CVE-2026-15718

### PhantomEnigma Campaign – Brazilian Government Website Compromise
- **Description**: Active campaign where more than 20 Brazilian government websites were hijacked and converted into malware delivery channels. Discovered by ANY.RUN interactive malware analysis platform.
- **Impact**: Visitors to legitimate government domains exposed to drive-by downloads and malware installation. High trust factor increases infection rates.
- **Status**: Active campaign uncovered. Remediation status of individual sites not specified.
- **CVE ID**: Not specified in source article

### Daxin Malware and Stupig Backdoor in Taiwan
- **Description**: Advanced malware previously attributed to a China-linked threat actor (Daxin) resurfaced after four years within a Taiwan manufacturing firm, accompanied by a previously unreported backdoor dubbed "Stupig" with pre-login SYSTEM privileges.
- **Impact**: Persistent SYSTEM-level access before authentication, enabling full system control, credential theft, and lateral movement in critical manufacturing infrastructure.
- **Status**: Active intrusion discovered. Daxin resurgence indicates continued operator investment. Stupig represents new capability.
- **CVE ID**: Not specified in source article

### Spirals Ransomware – Sub-24-Hour Encryption
- **Description**: New ransomware actor "Spirals" demonstrating extremely rapid intrusion-to-encryption timeline, completing initial access, data theft, and full network encryption in under 24 hours.
- **Impact**: Near-zero dwell time for detection and response. Organizations have minimal window to interrupt attack chain before encryption.
- **Status**: Active ransomware operations. New actor with high operational tempo.
- **CVE ID**: Not specified in source article

## Affected Systems and Products

- **Oracle E-Business Suite**: Financial application modules; federal agency deployments specifically targeted per CISA directive; enterprise on-premises and hosted instances
- **Zoom Workplace for Windows**: Versions prior to security update release; Zoom SDK for Windows integrations; all Windows desktop client users
- **Mozilla Firefox**: Versions prior to July 2026 security update; Firefox ESR branches; exploit code published for CVE-2026-15718
- **Google Chrome**: Included in multi-vendor critical update cycle; specific CVEs not detailed in source
- **Adobe Products**: Multiple critical flaws addressed in July 2026 update cycle; specific products not enumerated in source
- **VMware Products**: Critical security flaws patched in July 2026 updates; specific components not detailed in source
- **Brazilian Government Websites**: 20+ .gov.br domains across multiple agencies; web servers hosting public-facing services; AWS/cloud and on-premises hosting
- **Taiwan Manufacturing Firm Systems**: Windows endpoints in manufacturing environment; domain controllers and privileged access workstations; OT/IT convergence points
- **Shark RV2320EDUS Robot Vacuum**: IoT device with certificate-based authentication flaw; AWS region-wide control potential; camera, mobility, and sensor access
- **Ledger and Trezor Hardware Wallets**: Windows host machines running Ledger Live and Trezor Suite; seed phrase extraction via injected phishing interfaces
- **Cursor IDE/Editor**: Development environments vulnerable to 2-click exploit; source code and secret access; Electron-based application framework
- **AsyncAPI npm Packages**: Five malicious versions published to npm registry; Node.js/JavaScript development environments; CI/CD pipelines pulling compromised dependencies
- **WebEx and Zoom Installers**: Trojanized legitimate installers distributed via attacker-controlled channels; Windows endpoints executing modified binaries

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Malicious websites present fake verification prompts (CAPTCHA, "I'm not a robot") that copy PowerShell commands to clipboard; victims tricked into pasting into Run dialog or Terminal; delivers TELEPUZ modular malware and ClickLock macOS stealer
- **ClickLock macOS Forced Authentication**: Infostealer arrives as Terminal command; kills user applications every 210ms in infinite loop until victim enters login password; captures credentials for keychain access and system persistence
- **Agent Data Injection**: Malicious data planted in sources AI agents consume (product reviews, GitHub threads, documentation); causes autonomous agents to execute attacker-chosen actions (click "Buy Now," apply malicious code changes); exploits trust in retrieved content
- **PromptFiction Cross-Exploit**: Vulnerability in Claude allowing automatic malicious prompt injection to connected AI agents; when combined with second exploit enables end-to-end system compromise; fixed but demonstrates AI supply chain risk
- **Trojanized Legitimate Software**: UAT-11795 modifies WebEx and Zoom installer binaries to include Starland RAT backdoor; distributed via typosquatting, phishing, or compromised download sites; valid signatures bypass initial trust checks
- **Supply Chain Compromise (npm)**: Malicious AsyncAPI package versions published to official registry; credential-stealing RAT with remote access capabilities; developers install via standard `npm install`; CI/CD systems propagate to build artifacts
- **Certificate Extraction and Reuse (IoT)**: Physical access to single Shark RV2320EDUS extracts device certificate; certificate used to authenticate as legitimate device across same AWS region; enables camera surveillance, robot control, sensor data theft on other owners' devices
- **Hardware Wallet Phishing Injection**: OkoBot malware framework monitors for Ledger Live/Trezor Suite execution; injects fake seed phrase entry screens into legitimate app windows; captures recovery phrases for cryptocurrency theft
- **2-Click Developer Environment Takeover**: Cursor IDE vulnerability chain requiring only two user clicks; exploits "age-old bugs" in Electron/framework handling; extracts secrets, source code, and repository credentials
- **LLM-Assisted Botnet Development**: TuxBot v3 Evolution IoT framework shows code patterns consistent with LLM-generated code; modular architecture for DDoS, proxy, and credential harvesting; targets exposed IoT devices via default/weak credentials
- **AI Tool Abuse for Offensive Operations**: Russian-speaking actor "bandcampro" leverages Google Gemini CLI as automated hacking agent; directs vulnerability scanning, exploitation, and botnet C2 operations; demonstrates dual-use AI capability misuse

## Threat Actor Activities

- **Scattered Spider (UNC3944/0ktapus)**: Two leading members sentenced to 5.5 years each for 2024 Transport for London (TfL) intrusion; known for SIM-swapping, MFA fatigue, and SaaS credential theft; financially motivated; English-speaking collective with global targeting
- **UAT-11795 (Russian Financially Motivated Actor)**: Distributes Starland RAT via trojanized WebEx and Zoom installers; targets credentials and cryptocurrency; uses legitimate software trust to bypass defenses; active campaign as of July 2026
- **PhantomEnigma**: Campaign operator compromising Brazilian government websites for malware delivery; leverages high-trust .gov.br domains; discovered via ANY.RUN malware analysis; infrastructure and attribution details not fully disclosed
- **China-Linked APT (Daxin/Stupig Operators)**: Resurfaced Daxin malware after 4+ year hiatus in Taiwan manufacturing sector; deployed new Stupig pre-login SYSTEM backdoor; indicates long-term access maintenance and capability development; espionage-motivated
- **Spirals Ransomware Group**: New ransomware actor achieving full attack chain in <24 hours; high operational tempo suggests experienced operators or automated tooling; victimology not specified in source
- **"bandcampro" (Russian-Speaking Actor)**: Abuses Google Gemini CLI as hacking agent and botnet operator; directs automated vulnerability discovery and exploitation; operates small-scale botnet; demonstrates AI tool misuse for offensive cyber operations
- **TuxBot v3 Operators**: IoT botnet developers showing LLM-assisted code patterns; framework supports DDoS, traffic proxying, credential harvesting; targets poorly secured IoT devices globally; evolution from prior TuxBot versions
- **OkoBot Framework Operators**: Active since April 2025; targets cryptocurrency holders via hardware wallet phishing; Windows malware with modular architecture; specific actor attribution not provided
- **AsyncAPI Supply Chain Attacker**: Published five malicious npm package versions; credential-stealing RAT with remote access; identity and motivation not disclosed in source

## Source Attribution

- **23andMe to pay $18 million in new genetics data breach settlement**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/23andme-to-pay-18-million-in-new-genetics-data-breach-settlement/
- **New TELEPUZ Malware Spreads via ClickFix to Steal Data and Run Commands**: The Hacker News - https://thehackernews.com/2026/07/new-telepuz-malware-spreads-via.html
- **New ClickLock macOS Stealer Kills Apps Every 210ms Until Victims Type Their Password**: The Hacker News - https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html
- **Scattered Spider members behind TfL hack get five years in prison**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison/
- **Windows 11 24H2 Home and Pro reach end of support in 90 days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-11-24h2-home-and-pro-reach-end-of-support-in-90-days/
- **20+ Hijacked Government Websites Became an Attack Channel**: The Hacker News - https://thehackernews.com/2026/07/20-hijacked-government-websites.html
- **New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands**: The Hacker News - https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html
- **Daxin Resurfaces in Taiwan Alongside Stupig Pre-Login SYSTEM Backdoor**: The Hacker News - https://thehackernews.com/2026/07/daxin-resurfaces-in-taiwan-alongside.html
- **CISA orders feds to patch actively exploited Oracle flaw by Saturday**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-flaw-by-saturday/
- **Russian hackers trojanize WebEx, Zoom apps to push Starland malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/russian-hackers-trojanize-webex-zoom-apps-to-push-starland-malware/
- **AI Can Find Bugs, But Human Knowledge Still Proves Them**: The Hacker News - https://thehackernews.com/2026/07/ai-can-find-bugs-but-human-knowledge.html
- **New Spirals ransomware encrypts victim network in under 24 hours**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-spirals-ransomware-encrypts-victim-network-in-under-24-hours/
- **Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide**: The Hacker News - https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html
- **OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol**: The Hacker News - https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html
- **Zoom Patches Critical Windows Flaw That Could Enable Account Takeover**: The Hacker News - https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html
- **Police Disrupt a €140M Cyber Fraud Ring in Spain**: Dark Reading - https://www.darkreading.com/threat-intelligence/police-disrupt-140m-euro-cyber-fraud-ring-spain
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
