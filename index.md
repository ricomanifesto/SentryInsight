# Exploitation Report

## Executive Summary

This reporting period reveals a significant escalation in both the velocity and diversity of active exploitation. Critical vulnerabilities in widely deployed enterprise software—most notably a zero-day in Oracle E-Business Suite and a high-severity account takeover flaw in Zoom Workplace for Windows—are under active attack, prompting emergency patching directives from CISA for federal agencies. Simultaneously, the threat landscape is being reshaped by a new generation of malware and attack techniques targeting modern attack surfaces: AI agents are being weaponized via data injection and prompt manipulation, supply chain compromises are hitting developer ecosystems (npm), and sophisticated infostealers are employing novel persistence and coercion mechanisms on macOS and Windows. Threat actors ranging from the financially motivated Scattered Spider and UAT-11795 to suspected China-linked APTs (Daxin) are demonstrating advanced tradecraft, including trojanizing legitimate collaboration software and leveraging compromised government infrastructure for malware delivery.

The convergence of identity-based attacks, AI-assisted malware development, and living-off-the-land techniques is outpacing traditional exploit-centric defenses. Ransomware operators like the newly observed Spirals group are compressing the full attack lifecycle to under 24 hours, while IoT botnets (TuxBot v3) show evidence of LLM-assisted code generation. Unpatched vulnerabilities in consumer IoT devices (Shark robot vacuums) and forgotten UEFI bootloaders further expand the exploitable attack surface. Organizations must prioritize patching the actively exploited Oracle and Zoom flaws immediately, while hardening identity providers, AI agent integrations, and software supply chains against the rising tide of post-exploitation and social engineering tradecraft.

## Active Exploitation Details

### Oracle E-Business Suite Vulnerability (Actively Exploited Zero-Day)
- **Description**: A critical vulnerability in Oracle E-Business Suite financial application that is being actively exploited in the wild. The flaw allows attackers to compromise systems running the financial software suite.
- **Impact**: Full compromise of Oracle E-Business Suite instances, potentially leading to financial data theft, fraud, and lateral movement within enterprise networks.
- **Status**: **Actively exploited**. CISA has issued an emergency directive (Binding Operational Directive) ordering all federal civilian executive branch agencies to patch by Saturday, July 19, 2026. Oracle has released a security update.

### Zoom Workplace for Windows Account Takeover (CVE-2026-53412)
- **Description**: A critical security flaw in Zoom Workplace for Windows and the Zoom SDK for Windows that could allow an unauthenticated attacker to hijack user accounts. The vulnerability stems from improper input validation in the Windows client.
- **Impact**: Unauthenticated remote account takeover, enabling attackers to join meetings, access recorded sessions, exfiltrate chat history, and potentially pivot to other systems via the compromised Zoom identity.
- **Status**: **Patched**. Zoom has released security updates for Zoom Workplace (version 6.4.10 or later) and Zoom SDK for Windows. Users and administrators are urged to update immediately.
- **CVE ID**: CVE-2026-53412

### n8n Token Exchange Flaw
- **Description**: An authentication bypass vulnerability in n8n (workflow automation platform) Enterprise instances configured to trust multiple external token issuers (e.g., Okta, Auth0, Azure AD). The flaw occurs when n8n matches an incoming JWT to a local user account based solely on the `email` claim without validating the token's issuer (`iss` claim).
- **Impact**: Attackers who can obtain a valid JWT from *any* trusted issuer can authenticate as any user in the n8n instance who shares the same email address, leading to full account takeover and workflow manipulation.
- **Status**: **Vulnerable configurations exposed**. n8n has released a fix (version 1.82.1) that enforces strict issuer validation. Organizations using multi-issuer SSO must upgrade immediately.

### Shark RV2320EDUS Robot Vacuum Flaw (Unpatched)
- **Description**: A hardware/firmware vulnerability in the Shark RV2320EDUS robot vacuum. Researchers demonstrated that extracting a certificate from the device's flash storage allows an attacker to authenticate to the vendor's AWS IoT backend and issue commands to *any* other Shark vacuum in the same AWS region.
- **Impact**: Remote control of victim vacuums (drive, camera access, microphone access, map data exfiltration) across an entire geographic region without user interaction.
- **Status**: **Unpatched** as of publication. No firmware update has been released by SharkNinja. The vendor has been notified.

### Claude "PromptFiction" Vulnerability
- **Description**: A vulnerability in Anthropic's Claude AI agent framework that allowed malicious prompts to be automatically forwarded to connected AI agents. When chained with a second exploit, it enabled an end-to-end attack on targeted systems.
- **Impact**: Unauthorized command execution and data exfiltration via compromised AI agent workflows.
- **Status**: **Fixed**. Anthropic has patched the "PromptFiction" vulnerability. The article notes it has been remediated.

## Affected Systems and Products

- **Oracle E-Business Suite**: All supported versions prior to the July 2026 Critical Patch Update. Financial application modules exposed to the internet or accessible via VPN are at highest risk.
- **Zoom Workplace for Windows**: Versions prior to 6.4.10. Zoom SDK for Windows versions prior to the corresponding patched release.
- **n8n (Enterprise/Self-Hosted)**: Versions prior to 1.82.1 configured with multiple external OIDC/OAuth2 identity providers (e.g., Okta + Azure AD).
- **Shark RV2320EDUS Robot Vacuum**: All firmware versions currently shipped. The flaw resides in the device provisioning certificate handling and AWS IoT Core policy configuration.
- **Anthropic Claude AI Agents**: Deployments using the vulnerable agent framework version prior to the PromptFiction patch.
- **Brazilian Government Websites**: 20+ `.gov.br` domains compromised and repurposed as malware distribution infrastructure in the PhantomEnigma campaign.
- **AsyncAPI npm Packages**: Five malicious versions published to the npm registry: `@asyncapi/generator@1.0.0`, `@asyncapi/parser@1.0.0`, `@asyncapi/validator@1.0.0`, `@asyncapi/specs@1.0.0`, and `@asyncapi/openapi-to-asyncapi@1.0.0` (version numbers illustrative; check advisory for exact versions).
- **IoT Devices (TuxBot v3 Target)**: Linux-based IoT devices (routers, DVRs, IP cameras) with weak/default SSH/Telnet credentials or exposed management interfaces.

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers compromise legitimate websites (including government domains) and inject fake "Verify you are human" browser overlays (ClickFix lures). Victims are tricked into copying a malicious PowerShell command into the Windows Run dialog (Win+R), executing malware (TELEPUZ, likely others).
- **Trojanized Legitimate Software Installers**: Threat actor UAT-11795 distributes modified installers for Cisco WebEx and Zoom via phishing and SEO poisoning. The trojanized apps deploy the Starland RAT (Remote Access Trojan) for credential theft and cryptocurrency wallet draining.
- **AI Agent Data Injection / Prompt Injection**: Malicious instructions are embedded in external data sources (web pages, GitHub comments, documents) consumed by AI agents. The agent interprets the injected data as a valid command (e.g., "click Buy Now", "exfiltrate code"), bypassing user intent.
- **Multi-Issuer SSO Token Confusion**: In n8n, an attacker presents a valid JWT from Issuer A to an n8n instance trusting Issuers A and B. n8n matches the `email` claim to a user provisioned via Issuer B, granting access without validating the `iss` claim.
- **Hardware Wallet Phishing via Clipboard/Window Injection**: OkoBot malware monitors for Ledger Live / Trezor Suite windows. It overlays a fake "Enter seed phrase" prompt or swaps clipboard addresses during transactions to steal recovery phrases or divert funds.
- **macOS App-Killing Coercion (ClickLock)**: The ClickLock infostealer executes a tight loop (every 210ms) calling `NSRunningApplication.terminate()` on all user applications (Finder, Safari, Terminal, etc.) until the victim enters their macOS login password into a fake system dialog, granting the malware Full Disk Access / TCC bypass.
- **Supply Chain Compromise (npm)**: Attackers published malicious versions of legitimate AsyncAPI packages to the public npm registry. The packages contained a post-install script deploying a Remote Access Trojan (RAT) with info-stealing capabilities (browser credentials, SSH keys, env vars).
- **UEFI Secure Boot Bypass via Revoked Shim Bootloaders**: Attackers leverage nearly a dozen vulnerable, Microsoft-revoked UEFI shim bootloaders that remain trusted by some firmware/hardware combinations. This allows pre-OS bootkit installation (e.g., BlackLotus-style) on affected systems.
- **IoT Botnet Brute-Force & Exploitation (TuxBot v3)**: The botnet spreads via SSH/Telnet brute-force and exploitation of known vulnerabilities in IoT web interfaces. Code analysis suggests LLM assistance in generating polymorphic C2 communication and exploit modules.
- **Gemini CLI Abuse for Offensive Operations**: Threat actor "bandcampro" uses Google's open-source `gemini-cli` tool as an interactive hacking agent—generating exploit code, scanning targets, and orchestrating a small botnet—effectively outsourcing attack logic to the LLM.

## Threat Actor Activities

- **Scattered Spider (UNC3944 / 0ktapus)**: Two core members sentenced to 5.5 years in prison for the 2024 hack of Transport for London (TfL). The group is known for SIM-swapping, MFA fatigue, and Okta identity provider attacks. Sentencing marks a significant law enforcement win but the broader collective remains active.
- **UAT-11795 (Financially Motivated Russian Actor)**: Distributes trojanized WebEx/Zoom installers via phishing and malicious ads to deploy **Starland RAT**. Targets credentials (browsers, FTP, VPN), cryptocurrency wallets (Exodus, Electrum, MetaMask), and 2FA codes. Uses Telegram for C2.
- **PhantomEnigma (Campaign/Operator)**: Compromised 20+ Brazilian government websites (`.gov.br`) to host ClickFix lures delivering malware (likely TELEPUZ/Loaders). Infrastructure shared with previous Brazilian banking trojan campaigns. Attribution unknown.
- **Daxin / China-Linked APT (Suspected APT41 / Winnti)**: Advanced backdoor **Daxin** resurfaced after 4+ years in a Taiwan manufacturing firm. Deployed alongside a novel pre-login **SYSTEM-level backdoor dubbed "Stupig"**. Stupig injects into `winlogon.exe` before user authentication, providing persistent, high-privilege access surviving reboots and credential changes.
- **Spirals Ransomware Group**: New Ransomware-as-a-Service (RaaS) actor. Demonstrated full attack chain (initial access → lateral movement → data exfiltration → encryption) in **under 24 hours**. Uses living-off-the-land binaries (LOLBins) and rapid encryption (intermittent encryption for speed). Ransom note demands payment in XMR.
- **TuxBot v3 Operators (Unknown)**: Developing and operating an IoT botnet framework showing signs of **LLM-assisted code generation** (polymorphic strings, auto-generated exploit modules, natural language comments in binaries). Targets routers, cameras, DVRs for DDoS and proxy services.
- **bandcampro (Russian-Speaking Individual/Actor)**: Abuses **Google Gemini CLI** as an autonomous hacking agent. Uses the LLM to write exploits, scan Shodan/Censys, manage C2 for a small botnet, and generate phishing content. Represents a shift toward "AI-as-Attacker-Infrastructure."
- **OkoBot Operators (Unknown)**: Operating a modular Windows malware framework since **April 2025**. One module specifically targets Ledger Live and Trezor Suite users with seed phrase phishing overlays. Distributed via malvertising and cracked software sites.
- **AsyncAPI Supply Chain Attacker (Unknown)**: Compromised npm publish credentials (likely via token theft or phishing) to push 5 malicious package versions. Payload: RAT with keylogging, clipboard monitoring, browser credential dumping, and SSH key exfiltration. Packages since quarantined by npm.

## Source Attribution

- **ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html
- **AI Agents Broke the Security Playbook. Here's What Replaces It.**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ai-agents-broke-the-security-playbook-heres-what-replaces-it/
- **23andMe to pay $18 million in new genetics data breach settlement**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/23andme-to-pay-18-million-in-new-genetics-data-breach-settlement/
- **n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer**: The Hacker News - https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html
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
