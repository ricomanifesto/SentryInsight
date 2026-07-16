# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple vectors this reporting period, from actively exploited enterprise software flaws to novel AI-targeted attacks and supply chain compromises. CISA has issued an emergency directive for federal agencies to patch an actively exploited Oracle E-Business Suite vulnerability by Saturday, signaling ongoing real-world attacks against financial applications. Simultaneously, Mozilla confirmed exploit code publication for a critical Firefox flaw (CVE-2026-15718), while Zoom patched a critical account takeover vulnerability (CVE-2026-53412) in its Windows client. These enterprise-focused exploits coincide with a surge in identity-centric attacks, as threat actors increasingly leverage social engineering, trojanized legitimate software, and AI-assisted tooling to bypass traditional defenses.

Threat actor activity remains diverse and sophisticated. The Scattered Spider collective faces legal consequences for the 2024 Transport for London breach, while a Russian financially motivated group tracked as UAT-11795 deploys the new Starland RAT through trojanized WebEx and Zoom installers. The PhantomEnigma campaign compromised over 20 Brazilian government websites for malware delivery, and China-linked Daxin malware resurfaced in Taiwan alongside the previously undocumented Stupig backdoor. A Russian-speaking operator "bandcampro" weaponized Google's Gemini CLI as both a hacking agent and botnet controller, marking a notable escalation in AI tool abuse for offensive operations.

Emerging attack surfaces center on AI agents, development environments, and IoT ecosystems. Researchers demonstrated an "Agent Data Injection" technique where poisoned data sources manipulate AI agents into executing attacker commands, while the "PromptFiction" vulnerability in Claude enabled malicious prompt injection (now patched). A 2-click exploit against Cursor allows developer environment takeover, and the Shark robot vacuum flaw permits cross-device command execution within AWS regions. New malware families—TELEPUZ (ClickFix distribution), ClickLock (macOS credential theft), Spirals ransomware (sub-24-hour encryption), TuxBot v3 (LLM-assisted IoT botnet), and OkoBot (hardware wallet phishing)—demonstrate rapid innovation in stealth, persistence, and monetization strategies.

## Active Exploitation Details

### Oracle E-Business Suite Financial Application Vulnerability
- **Description**: A critical vulnerability in Oracle E-Business Suite financial application that is being actively exploited in the wild. CISA has added this to the Known Exploited Vulnerabilities catalog and issued an emergency directive.
- **Impact**: Attackers can compromise federal financial systems, potentially leading to unauthorized access to sensitive financial data, fraudulent transactions, and persistent access to enterprise ERP environments.
- **Status**: Actively exploited. CISA ordered federal civilian executive branch agencies to secure systems by Saturday (July 19, 2026). Patch availability implied by remediation order.
- **CVE ID**: Not specified in source article

### Zoom Workplace for Windows Account Takeover Flaw
- **Description**: A critical security flaw in Zoom Workplace for Windows desktop client and SDK that could be exploited by an unauthenticated party to hijack user accounts.
- **Impact**: Full account takeover without authentication, enabling attackers to access meetings, contacts, recorded sessions, and potentially pivot to connected enterprise systems.
- **Status**: Patched. Zoom released security updates addressing the vulnerability.
- **CVE ID**: CVE-2026-53412

### Firefox Critical Vulnerability with Published Exploit Code
- **Description**: Mozilla released updates addressing two critical flaws in Firefox, with explicit warning that exploit code has been published for at least one vulnerability.
- **Impact**: Remote code execution potential through crafted web content, allowing attackers to escape sandbox and execute arbitrary code on victim systems.
- **Status**: Patched in Firefox updates. Exploit code publicly available increases urgency for deployment.
- **CVE ID**: CVE-2026-15718

### Shark Robot Vacuum Cross-Device Control Flaw
- **Description**: An unpatched vulnerability in Shark RV2320EDUS robot vacuums where extracting a certificate from one device's flash storage enables root command execution on other Shark vacuums within the same AWS region.
- **Impact**: Attackers can watch cameras, drive robots, read sensors, and execute arbitrary root commands across an entire regional fleet of devices from a single compromised unit.
- **Status**: Unpatched as of reporting. No vendor fix announced.
- **CVE ID**: Not specified in source article

### Claude "PromptFiction" AI Agent Vulnerability
- **Description**: A vulnerability in Anthropic's Claude that could automatically send malicious prompts to AI agents, enabling end-to-end attacks when combined with another exploit.
- **Impact**: Attackers could manipulate AI agents into performing unauthorized actions, accessing sensitive data, or executing commands on connected systems.
- **Status**: Fixed. The vulnerability has been patched by Anthropic.
- **CVE ID**: Not specified in source article

### AsyncAPI npm Supply Chain Attack
- **Description**: Five malicious versions of AsyncAPI packages published to npm registry delivering a remote access trojan with info-stealing capabilities.
- **Impact**: Credential theft, persistent remote access, and potential lateral movement for any developer or CI/CD system that installed compromised packages.
- **Status**: Malicious packages identified and presumably removed from npm. Affected versions: specific version numbers not detailed in source.
- **CVE ID**: Not specified in source article

## Affected Systems and Products

- **Oracle E-Business Suite**: Financial application modules; affected versions not specified in source. Federal civilian executive branch agencies mandated to patch.
- **Zoom Workplace for Windows**: Desktop client and Software Development Kit (SDK) for Windows; versions prior to security update release.
- **Mozilla Firefox**: All versions prior to the July 2026 security update addressing CVE-2026-15718 and companion critical flaw.
- **Shark RV2320EDUS Robot Vacuum**: IoT device communicating via AWS regional infrastructure; all units in affected regions potentially vulnerable.
- **Anthropic Claude**: AI assistant platform; versions prior to PromptFiction patch deployment.
- **AsyncAPI npm Packages**: Node.js packages published to npm registry; five specific malicious versions containing credential-stealing RAT.
- **Google Gemini CLI**: Open-source command-line AI tool; weaponized by threat actor "bandcampro" for hacking and botnet operations.
- **Cursor**: AI-powered code editor; development environments vulnerable to 2-click exploit for secrets and source code access.
- **Ledger and Trezor Hardware Wallets**: Cryptocurrency hardware wallets targeted by OkoBot malware framework's seed phrase phishing module on Windows.
- **Brazilian Government Websites**: 20+ .gov.br domains hijacked and repurposed as malware delivery channels in PhantomEnigma campaign.

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: TELEPUZ malware spreads via compromised websites displaying fake browser error messages that trick users into executing malicious PowerShell commands. Vector: Web-based social engineering → clipboard manipulation → command execution.
- **Trojanized Legitimate Software**: UAT-11795 distributes Starland RAT through modified WebEx and Zoom installers. Vector: Software supply chain → trusted application execution → credential theft and cryptocurrency stealing.
- **Hijacked Legitimate Websites**: PhantomEnigma campaign compromised 20+ Brazilian government websites to serve as malware delivery channels. Vector: Web server compromise → drive-by downloads/watering hole → malware deployment.
- **AI Agent Data Injection**: Attackers plant malicious content (reviews, code comments, documentation) that AI agents consume and act upon, causing misclicks or command execution. Vector: Data poisoning → AI agent processing → unintended privileged actions.
- **Prompt Injection (PromptFiction)**: Crafted inputs to Claude that bypass safety controls and trigger malicious prompt forwarding to connected AI agents. Vector: Malicious prompt → LLM processing → agent orchestration abuse.
- **Certificate Extraction and Cross-Device Abuse**: Physical or remote extraction of device certificate from one Shark vacuum enables authentication as legitimate device across AWS region. Vector: IoT device compromise → certificate theft → regional fleet impersonation.
- **Supply Chain Compromise (npm)**: Malicious AsyncAPI package versions published to public registry with credential-stealing RAT payload. Vector: Registry poisoning → dependency installation → RAT deployment.
- **AI Tool Weaponization**: Threat actor "bandcampro" uses Google Gemini CLI as automated hacking agent and botnet command-and-control interface. Vector: Legitimate AI tool → offensive automation → infrastructure management.
- **Relentless Credential Prompting (ClickLock)**: macOS malware kills user applications every 210ms until victim enters login password in Terminal. Vector: Terminal command execution → denial of usability → forced credential entry.
- **2-Click Developer Environment Takeover**: Simple chain exploiting Cursor IDE to access secrets and source code-rich environments. Vector: Crafted repository/content → IDE processing → credential/source code exfiltration.
- **Pre-Login SYSTEM Backdoor (Stupig)**: China-linked backdoor achieving SYSTEM privileges before user login on Windows. Vector: Boot/pre-authentication exploitation → persistent kernel-level access.
- **Hardware Wallet Phishing Injection**: OkoBot injects seed phrase phishing prompts into legitimate Ledger Live and Trezor Suite applications on infected Windows hosts. Vector: Process injection → UI manipulation → cryptocurrency wallet drainage.

## Threat Actor Activities

- **UAT-11795 (Russian Financially Motivated)**: Deploying Starland RAT via trojanized WebEx and Zoom installers targeting credentials and cryptocurrency. Active campaign using trusted software supply chain compromise.
- **PhantomEnigma (Operator Unattributed)**: Compromised 20+ Brazilian government websites (.gov.br) converting them into malware delivery infrastructure. Campaign uncovered by ANY.RUN interactive malware analysis.
- **Daxin/China-Linked APT**: Advanced malware resurfaced after 4+ years in a Taiwan manufacturing firm, accompanied by previously unreported Stupig pre-login SYSTEM backdoor. Indicates long-term persistence and advanced Windows internals expertise.
- **Scattered Spider (Cybercrime Collective)**: Two leading members sentenced to 5.5 years for 2024 Transport for London (TfL) hack. Group known for social engineering, SIM swapping, and SaaS/identity provider targeting.
- **Spirals Ransomware (New Actor)**: Completed full intrusion lifecycle—initial access, data theft, encryption—in under 24 hours. Demonstrates high operational tempo and efficient tooling.
- **bandcampro (Russian-Speaking Operator)**: Weaponized Google Gemini CLI as hacking agent and botnet controller. Represents novel use of legitimate AI developer tools for offensive automation.
- **TuxBot v3 Developers (Unknown, LLM-Assisted)**: IoT botnet framework showing signs of LLM-assisted development. Targets embedded Linux devices with modular architecture for DDoS, proxy, and data collection.
- **OkoBot Operators (Unknown)**: Malware framework active since April 2025 targeting cryptocurrency holders via hardware wallet seed phrase phishing on Windows. Module-specific design for Ledger Live and Trezor Suite.
- **AsyncAPI Supply Chain Attacker (Unknown)**: Published five malicious package versions to npm delivering credential-stealing RAT. Infrastructure and attribution not disclosed in source.

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
