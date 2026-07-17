# Exploitation Report

## Executive Summary

A critical Windows zero-day exploit dubbed **LegacyHive** has been publicly released, granting attackers administrative privileges on fully patched Windows systems. The exploit, published by a researcher using the handle "Nightmare Eclipse," represents an immediate elevation-of-privilege threat across current Windows versions. Simultaneously, CISA has added **CVE-2026-58644**—a Microsoft SharePoint Server remote code execution zero-day—to its Known Exploited Vulnerabilities catalog, confirming active exploitation in the wild and mandating urgent federal patching.

Multiple active exploitation campaigns are underway across diverse vectors. CISA has ordered federal agencies to patch two actively exploited vulnerabilities in Fortinet FortiSandbox threat detection platforms. The **PhantomEnigma** campaign has compromised over 20 Brazilian government websites, converting them into malware delivery channels. China-linked threat actors have resurfaced the **Daxin** malware alongside a previously undocumented **Stupig** pre-login SYSTEM backdoor targeting a Taiwan manufacturing firm. Meanwhile, the **Scattered Spider** cybercrime collective faces legal consequences with two members sentenced for the 2024 Transport for London breach, while ransomware disrupts operations at Coca-Cola's Fairlife subsidiary.

The threat landscape continues to evolve with novel attack techniques targeting AI-driven environments. A new **Agent Data Injection** attack method can manipulate AI agents into executing unintended actions—including unauthorized purchases or code execution—by poisoning data sources. ClickFix social engineering lures remain highly effective, distributing **ACR Stealer**, **TELEPUZ**, and the new **ClickLock** macOS stealer that aggressively terminates applications until victims surrender credentials. The **OkoBot** framework deploys over 20 payloads for cryptocurrency theft, while **GoSerpent** conducts espionage against Southeast Asian governments. A flaw in Anthropic's **Claude Chrome extension** allows malicious extensions to simulate user clicks and trigger AI actions, and an **n8n token exchange vulnerability** enables cross-issuer account takeover on misconfigured enterprise instances.

## Active Exploitation Details

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A security researcher using the handle "Nightmare Eclipse" has publicly released a Windows zero-day exploit named LegacyHive that enables privilege escalation to SYSTEM on up-to-date Windows installations. The exploit targets a previously unknown vulnerability in the Windows kernel.
- **Impact**: Attackers can escalate from standard user privileges to full administrative/SYSTEM control on affected Windows systems, enabling complete system compromise, persistence, and lateral movement.
- **Status**: Zero-day exploit publicly released; no patch available at time of reporting. Active exploitation risk is immediate and high.
- **CVE ID**: Not yet assigned in source article

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that has been exploited in the wild as a zero-day. The flaw allows unauthenticated attackers to execute arbitrary code on vulnerable SharePoint servers.
- **Impact**: Full server compromise, potential access to sensitive organizational documents, lateral movement into internal networks, and data exfiltration.
- **Status**: Actively exploited in the wild. CISA added to Known Exploited Vulnerabilities (KEV) catalog. Microsoft has released patches; immediate application mandated for federal agencies.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform are being actively exploited in the wild. Specific technical details were not disclosed in the source article.
- **Impact**: Compromise of the threat detection infrastructure itself, potential bypass of security controls, and use as a pivot point for deeper network intrusion.
- **Status**: Actively exploited. CISA issued emergency directive ordering federal civilian agencies to prioritize patching by a specified deadline.
- **CVE ID**: Not provided in source article

### Anthropic Claude Chrome Extension Flaw
- **Description**: A vulnerability in the Claude for Chrome browser extension that allows a malicious extension to simulate user clicks and trigger predefined AI actions, potentially abusing Claude's access to browser content and permissions.
- **Impact**: Unauthorized invocation of AI capabilities, potential access to sensitive browser data, and execution of actions within the context of the user's Claude session.
- **Status**: Vulnerability disclosed; patch status not specified in source article.
- **CVE ID**: Not provided in source article

### n8n Token Exchange Vulnerability
- **Description**: A flaw in the n8n workflow automation platform's Enterprise edition where, when configured to trust multiple external token issuers, the system incorrectly matches an incoming JWT to a local user account from a different issuer.
- **Impact**: Authentication bypass allowing attackers to log in as arbitrary users from another trusted identity provider, leading to full account takeover and access to workflow automation capabilities.
- **Status**: Vulnerability disclosed; affects Enterprise instances with multi-issuer configurations.
- **CVE ID**: Not provided in source article

### Agent Data Injection Attack Technique
- **Description**: A novel attack method where malicious data planted in sources consumed by AI agents causes them to execute unintended actions—such as clicking "Buy Now" instead of summarizing reviews, or applying malicious code from a compromised GitHub thread.
- **Impact**: Subversion of AI agent autonomy leading to unauthorized transactions, code execution, data exfiltration, or privilege escalation depending on the agent's permissions and integrations.
- **Status**: New attack technique demonstrated; no specific CVE as it represents a class of vulnerabilities in AI agent architectures.
- **CVE ID**: Not applicable (attack technique class)

## Affected Systems and Products

- **Microsoft Windows (all current versions)**: Affected by LegacyHive zero-day privilege escalation exploit; impacts up-to-date installations
- **Microsoft SharePoint Server**: Affected by CVE-2026-58644 RCE zero-day; specific versions not detailed in source
- **Fortinet FortiSandbox**: Two actively exploited vulnerabilities; specific versions not detailed in source
- **Anthropic Claude for Chrome Extension**: Flaw allowing malicious extension interaction; version details not specified
- **n8n Workflow Automation Platform (Enterprise)**: Token exchange flaw affecting instances configured with multiple external token issuers
- **macOS Systems**: Targeted by ClickLock stealer malware; specific versions not detailed
- **Brazilian Government Websites (20+)**: Compromised and repurposed as malware delivery infrastructure in PhantomEnigma campaign
- **Taiwan Manufacturing Firm**: Targeted by Daxin malware and Stupig backdoor; specific systems not detailed
- **Southeast Asian Government and Diplomatic Entities**: Targeted by GoSerpent espionage malware since late 2025
- **Coca-Cola Fairlife Subsidiary**: US dairy production systems disrupted by ransomware attack
- **Transport for London (TfL)**: Previously breached by Scattered Spider in 2024; £29 million impact

## Attack Vectors and Techniques

- **Zero-Day Privilege Escalation (LegacyHive)**: Local exploitation of unknown Windows kernel vulnerability to achieve SYSTEM privileges from standard user context
- **Remote Code Execution (CVE-2026-58644)**: Unauthenticated network-based exploitation of SharePoint Server for initial access and code execution
- **Security Appliance Exploitation**: Active targeting of Fortinet FortiSandbox vulnerabilities to compromise defensive infrastructure
- **ClickFix Social Engineering**: Deceptive web lures that trick users into executing malicious commands (typically via "verify you are human" prompts), delivering ACR Stealer, TELEPUZ, and ClickLock
- **Agent Data Injection**: Poisoning data sources consumed by AI agents (product reviews, GitHub threads, documentation) to induce malicious actions
- **Malicious Browser Extension Abuse**: Exploiting Claude Chrome extension flaw to simulate user clicks and trigger unauthorized AI actions
- **JWT Token Confusion**: Exploiting n8n's incorrect issuer validation in multi-tenant Enterprise configurations for cross-issuer account takeover
- **Aggressive Credential Phishing (ClickLock)**: macOS malware that kills all visible processes every 210ms until victim enters system login password
- **Website Compromise & Repurposing**: Hijacking legitimate government websites (PhantomEnigma campaign) to serve malware to trusted visitors
- **Multi-Payload Modular Frameworks**: OkoBot deploying 20+ payloads for cryptocurrency wallet theft, credential harvesting, and data exfiltration
- **Pre-Authentication Backdoor (Stupig)**: SYSTEM-level backdoor accessible before user login, deployed alongside Daxin malware
- **Ransomware Deployment**: Encryption and operational disruption of critical production systems (Fairlife/Coca-Cola)
- **AI Security Filter Evasion**: Text salting/hidden text techniques bypassing LLM-based phishing detection in over 1 million emails

## Threat Actor Activities

- **Nightmare Eclipse (Researcher/Handle)**: Publicly released the LegacyHive Windows zero-day exploit; motivation appears to be vulnerability disclosure via full exploit publication
- **Scattered Spider (Cybercrime Collective)**: Conducted 2024 Transport for London breach causing £29M damage and 148 station disruptions; two members (Owen Flowers, 18; Thalha Jubair, 20) sentenced to 5.5 years each in July 2026
- **REvil Ransomware Affiliate (Aleksandr Ermakov)**: Russian national detained in Armenia on U.S. extradition warrant; lawyers claim mistaken identity
- **China-Linked APT (Daxin/Stupig Operators)**: Resurfaced Daxin malware after 4+ year hiatus alongside new Stupig pre-login SYSTEM backdoor targeting Taiwan manufacturing sector
- **PhantomEnigma Campaign Operators**: Compromised 20+ Brazilian government websites, converting them into malware delivery channels; discovered by ANY.RUN researchers
- **GoSerpent Operators**: Conducting cyber espionage against Southeast Asian governments and diplomats since late 2025 using previously undocumented GoSerpent malware
- **ACR Stealer Operators**: Distributing infostealer since 2024 via ClickFix lures; harvesting browser passwords, session tokens, PDFs, Microsoft 365 documents, and OneDrive files
- **TELEPUZ Operators**: Deploying modular malware via ClickFix-infected websites since April 2026; full-featured data theft and command execution capabilities
- **ClickLock Operators**: Distributing aggressive macOS stealer via Terminal command pastes; unique kill-loop mechanism forces credential entry
- **OkoBot Operators**: Utilizing framework with 20+ payloads focused on cryptocurrency wallet seed phrases, credentials, and sensitive data theft
- **Fairlife Ransomware Actors**: Unidentified ransomware group disrupted US dairy production at Coca-Cola subsidiary; attribution not specified in source
- **Investment Fraud Money Launderers (2 charged)**: New York man and woman charged with laundering $43M from cyber investment fraud scams

## Source Attribution

- **Gold Eagle Clearinghouse Targets Security Gap, But How Is Unclear**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/gold-eagle-clearinghouse-targets-security-gap
- **Google Bets 'Agentic Defense' Strategy Can Outpace Attackers**: Dark Reading - https://www.darkreading.com/cloud-security/google-bets-agentic-defense-strategy-outpace-attackers
- **E.U. Orders Google to Open Android Mic, Camera and Screen to Rival AI Assistants**: The Hacker News - https://thehackernews.com/2026/07/eu-orders-google-to-open-android-mic.html
- **The Race to Field Military Autonomy Is On, Can Trusted Information Infrastructure Keep Pace?**: The Hacker News - https://thehackernews.com/2026/07/the-race-to-field-military-autonomy-is.html
- **New Windows LegacyHive zero-day gives hackers admin privileges**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-windows-legacyhive-zero-day-exploit-grants-hackers-admin-access/
- **Armenia Detains Russian Tourist on U.S. Warrant for REvil Hacker, Lawyers Say Wrong Man**: The Hacker News - https://thehackernews.com/2026/07/armenia-detains-russian-tourist-on-us.html
- **Windows Server 2022 reach end of mainstream support in 90 days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-server-2022-reach-end-of-mainstream-support-in-90-days/
- **ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files**: The Hacker News - https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
- **New GoSerpent Malware Targets Southeast Asian Governments and Diplomats for Espionage**: The Hacker News - https://thehackernews.com/2026/07/new-goserpent-malware-targets-southeast.html
- **US charges two over laundering $43 million from investment fraud**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-two-over-laundering-43-million-from-investment-fraud/
- **CISA urges immediate action on actively exploited Fortinet flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV**: The Hacker News - https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **New ClickLock macOS malware traps users into revealing login password**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/
- **Coca-Cola says Fairlife ransomware attack halts US dairy production**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production/
- **Agentic AI: Taming the Unpredictable**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/agentic-ai-untamable-ask-the-right-security-questions
- **1M+ Emails Use Hidden Text to Dupe AI Security Filters**: Dark Reading - https://www.darkreading.com/threat-intelligence/1m-emails-hidden-text-dupe-ai-security-filters
- **Claude Chrome extension flaw lets malicious extensions trigger AI actions**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/claude-chrome-extension-flaw-lets-malicious-extensions-trigger-ai-actions/
- **New OkoBot framework deploys 20 payloads to steal data, crypto**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-okobot-framework-deploys-20-payloads-to-steal-data-crypto/
- **Two Scattered Spider Hackers Get 5.5 Years Each for £29 Million TfL Hack**: The Hacker News - https://thehackernews.com/2026/07/two-scattered-spider-hackers-get-55.html
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
