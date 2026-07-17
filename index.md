# Exploitation Report

## Executive Summary

A significant wave of active exploitation activity has emerged across multiple platforms, with CISA adding two critical zero-day vulnerabilities to its Known Exploited Vulnerabilities catalog. Microsoft SharePoint Server faces active exploitation of a remote code execution flaw (CVE-2026-58644), while two Fortinet FortiSandbox vulnerabilities are being leveraged in the wild, prompting emergency patching directives for federal agencies. Simultaneously, a newly disclosed Windows zero-day exploit dubbed LegacyHive enables privilege escalation to SYSTEM on fully patched systems, with proof-of-concept code publicly released by a researcher operating under the "Nightmare Eclipse" handle.

The threat landscape continues to evolve with sophisticated malware frameworks and novel attack techniques targeting both traditional and AI-augmented environments. Multiple infostealer families—including ACR Stealer, ClickLock, TELEPUZ, and the OkoBot framework—are actively harvesting credentials, browser tokens, cryptocurrency wallets, and Microsoft 365 data using ClickFix social engineering lures and innovative macOS persistence mechanisms. A China-linked threat actor has resurfaced the Daxin malware alongside a previously undocumented Stupig pre-login SYSTEM backdoor in Taiwanese manufacturing networks, while the PhantomEnigma campaign has compromised over 20 Brazilian government websites for malware distribution. Notably, the Scattered Spider cybercrime collective has faced legal consequences with two members sentenced for the 2024 Transport for London breach, though the group's broader activity persists.

Emerging attack vectors now explicitly target AI agents and LLM-integrated systems, with researchers demonstrating data injection attacks that can manipulate autonomous agents into executing unintended actions—including unauthorized purchases and code execution. Phishing campaigns at scale are employing text salting techniques to evade AI-powered security filters, with over one million malicious emails observed using hidden text manipulation. Meanwhile, vulnerabilities in AI-adjacent tooling such as the Claude Chrome extension and n8n workflow automation platform reveal expanding attack surface in the AI supply chain. Organizations must prioritize patching of the actively exploited Fortinet and SharePoint vulnerabilities while deploying behavioral detection for the novel infostealer techniques and AI-agent manipulation methods now observed in active campaigns.

## Active Exploitation Details

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A Windows zero-day exploit dubbed "LegacyHive" allows attackers to escalate privileges to SYSTEM on up-to-date Windows systems. The exploit was publicly released by a security researcher using the "Nightmare Eclipse" handle, providing attackers with immediate weaponization capability.
- **Impact**: Attackers can achieve full administrative control over affected Windows systems, bypassing security controls and enabling persistence, lateral movement, and deployment of additional payloads.
- **Status**: Actively exploitable with public proof-of-concept code available. No patch mentioned in source articles at time of reporting.

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform are being actively exploited in the wild. CISA has issued an emergency directive ordering federal civilian executive branch agencies to prioritize patching.
- **Impact**: Exploitation of these flaws in a security appliance designed to detect threats could allow attackers to compromise network monitoring infrastructure, evade detection, and pivot to internal networks.
- **Status**: Actively exploited. CISA mandated immediate patching for federal agencies. Patches presumed available from Fortinet.

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that has been exploited in the wild as a zero-day. CISA added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog following confirmation of active exploitation.
- **Impact**: Remote attackers can execute arbitrary code on SharePoint servers, potentially leading to full server compromise, data exfiltration, and lateral movement within organizational networks.
- **Status**: Actively exploited zero-day. Microsoft has released patches. CISA KEV inclusion mandates federal agency remediation.
- **CVE ID**: CVE-2026-58644

### n8n Token Exchange Authentication Bypass
- **Description**: A flaw in the n8n workflow automation platform's token exchange mechanism on Enterprise instances configured with multiple external token issuers. The vulnerability causes improper JWT matching, allowing authentication as users from different identity providers.
- **Impact**: Attackers can authenticate as arbitrary users across trusted identity providers, leading to unauthorized access to workflows, credentials, and automated processes.
- **Status**: Vulnerability disclosed. Patch status not specified in source articles.

### Claude Chrome Extension Click Simulation Flaw
- **Description**: A vulnerability in Anthropic's Claude for Chrome browser extension that allows malicious extensions to simulate user clicks and trigger predefined AI actions, potentially abusing Claude's access to browser content and permissions.
- **Impact**: Malicious extensions can invoke AI actions without user consent, potentially accessing sensitive page content, executing automated workflows, or exfiltrating data through Claude's capabilities.
- **Status**: Vulnerability disclosed. Remediation status not specified in source articles.

## Affected Systems and Products

- **Microsoft Windows (all supported versions)**: LegacyHive zero-day privilege escalation affects up-to-date Windows systems; proof-of-concept exploit publicly available
- **Fortinet FortiSandbox**: Threat detection appliance with two actively exploited vulnerabilities requiring immediate patching per CISA directive
- **Microsoft SharePoint Server**: On-premises SharePoint installations vulnerable to CVE-2026-58644 remote code execution; patches released
- **n8n Workflow Automation Platform (Enterprise)**: Instances configured with multiple external token issuers (OIDC/SAML) vulnerable to authentication bypass
- **Anthropic Claude for Chrome Extension**: Browser extension users exposed to click-simulation attacks from malicious co-installed extensions
- **macOS Systems**: Targeted by ClickLock infostealer employing novel process-termination persistence techniques
- **Brazilian Government Web Infrastructure**: 20+ government websites compromised and repurposed as malware delivery channels in PhantomEnigma campaign
- **Taiwanese Manufacturing Networks**: Targeted by Daxin malware and Stupig pre-login SYSTEM backdoor attributed to China-linked threat actor
- **Transport for London (TfL) Infrastructure**: Previously compromised in 2024 by Scattered Spider cybercrime collective; perpetrators sentenced
- **Coca-Cola Fairlife Subsidiary**: US dairy production halted by ransomware attack on operational systems

## Attack Vectors and Techniques

- **ClickFix Social Engineering Lures**: Used by ACR Stealer (since 2024), TELEPUZ malware (since April 2026), and OkoBot framework to trick users into executing malicious commands via fake verification pages, CAPTCHAs, and browser-based prompts
- **LegacyHive Privilege Escalation**: Windows kernel exploit leveraging legacy hive registry handling to achieve SYSTEM privileges from standard user context; public exploit code released
- **SharePoint RCE Exploitation (CVE-2026-58644)**: Remote code execution against on-premises SharePoint Server instances; exploited in the wild prior to patching
- **FortiSandbox Appliance Exploitation**: Targeting of network security monitoring infrastructure to disable detection capabilities and establish persistence
- **n8n JWT Token Confusion**: Authentication bypass via improper token issuer validation in multi-identity-provider Enterprise configurations
- **Chrome Extension Click Simulation**: Malicious extensions simulating user interactions to trigger AI actions in Claude browser extension without consent
- **ClickLock macOS Process Persistence**: Terminates all visible processes every 210ms in a loop, forcing victims to enter system login password to regain control; delivered via Terminal command paste
- **Text Salting / Hidden Text Injection**: Over 1 million phishing emails using invisible Unicode characters and hidden text to evade AI-powered security filters and LLM-based email analysis
- **Agent Data Injection Attacks**: Malicious content planted in data sources (reviews, GitHub threads, documentation) that manipulates AI agents into executing unintended actions—clicking "Buy Now," applying malicious code changes, or exfiltrating data
- **PhantomEnigma Watering Hole / Supply Chain**: Compromise of 20+ legitimate Brazilian government websites to serve as malware distribution channels for unsuspecting visitors
- **Daxin/Stupig Pre-Login Backdoor**: China-linked advanced persistent threat deploying SYSTEM-level backdoor active before user authentication, alongside Daxin malware framework for long-term espionage
- **OkoBot Multi-Payload Framework**: Modular framework deploying 20+ payloads for cryptocurrency wallet seed phrase theft, credential harvesting, and sensitive data exfiltration
- **REvil Ransomware Operations**: Continued attribution of ransomware activity to REvil affiliates; law enforcement pursuing suspects internationally

## Threat Actor Activities

- **Scattered Spider (UNC3944/Scatter Swine)**: Cybercrime collective responsible for 2024 Transport for London breach causing £29 million in damages and disrupting services for 148 stations. Two members (Owen Flowers, 18; Thalha Jubair, 20) sentenced to 5.5 years each in July 2026. Group known for social engineering, SIM swapping, and cloud environment targeting.
- **PhantomEnigma**: Threat actor operating campaign compromising 20+ Brazilian government websites since at least early 2026, repurposing them as malware delivery channels. Uncovered by ANY.RUN interactive malware analysis platform.
- **China-Linked APT (Daxin/Stupig Operators)**: Advanced persistent threat attributed to Chinese intelligence services resurfacing Daxin malware after four-year hiatus. Deployed alongside novel "Stupig" pre-login SYSTEM backdoor in Taiwanese manufacturing firm for espionage. Demonstrates long-term access maintenance and sophisticated kernel-level tooling.
- **ACR Stealer Operators**: Infostealer campaign active since 2024 using ClickFix lures to harvest browser passwords, live session tokens, PDFs, Microsoft 365 documents, and OneDrive-synced files from enterprise networks.
- **TELEPUZ Operators**: Modular malware campaign spreading via ClickFix-infected websites since late April 2026. Full-featured backdoor capable of data theft, command execution, and persistent access.
- **OkoBot Framework Operators**: Deploying 20+ payload framework focused on cryptocurrency wallet seed phrases, credentials, and sensitive data theft. Modular architecture suggests organized development and distribution.
- **ClickLock Developers**: macOS infostealer employing novel denial-of-service persistence (killing apps every 210ms) to coerce password entry. Delivered via social engineering (Terminal command paste).
- **GoSerpent Operators**: Previously undocumented malware targeting Southeast Asian governments and diplomats for espionage since late 2025. Attribution not publicly assigned in source articles.
- **REvil Ransomware Affiliates**: Continued law enforcement action against REvil infrastructure; Russian national Aleksandr Ermakov detained in Armenia on U.S. extradition request (defense claims mistaken identity).
- **Fairlife Ransomware Actors**: Unattributed ransomware group disrupting Coca-Cola's Fairlife dairy production across US facilities. Actor identity and ransomware variant not disclosed in source articles.

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
