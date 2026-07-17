# Exploitation Report

## Executive Summary

CISA has added a critical Microsoft SharePoint Server zero-day vulnerability (CVE-2026-58644) to its Known Exploited Vulnerabilities catalog, confirming active exploitation of this remote code execution flaw. Federal agencies have been ordered to patch this vulnerability immediately, alongside two actively exploited Fortinet FortiSandbox flaws and a critical Oracle E-Business Suite vulnerability that is also under active attack.

Multiple new malware families and attack campaigns are targeting diverse platforms. The ClickFix social engineering technique continues to proliferate, now delivering ACR Stealer, TELEPUZ, and PhantomEnigma payloads across Windows and macOS. A new macOS infostealer called ClickLock employs aggressive process termination to coerce victims into entering credentials, while the GoSerpent malware conducts espionage against Southeast Asian governments. The Scattered Spider cybercrime group saw two members sentenced for the 2024 Transport for London breach, and Russian threat actor UAT-11795 is distributing the Starland RAT through trojanized WebEx and Zoom installers.

Ransomware operations remain aggressive with the new Spirals ransomware completing full intrusion-to-encryption cycles in under 24 hours, and a Fairlife (Coca-Cola subsidiary) attack halting U.S. dairy production. Supply chain and infrastructure risks are emerging through the OkoBot framework deploying 20+ payloads, hijacked Brazilian government websites serving as malware delivery channels, and an unpatched Shark robot vacuum vulnerability enabling cross-device control within AWS regions.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that allows unauthenticated attackers to execute arbitrary code on affected servers. The vulnerability was patched in Microsoft's July 2026 Patch Tuesday release.
- **Impact**: Full server compromise, potential lateral movement within enterprise networks, data exfiltration, and persistence establishment.
- **Status**: Actively exploited in the wild. CISA added to KEV catalog on July 17, 2026. Federal agencies ordered to apply patches immediately.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that are being actively exploited by threat actors. Specific vulnerability details were not disclosed in the advisory.
- **Impact**: Compromise of threat detection infrastructure, potential bypass of security controls, and access to sandboxed malware analysis data.
- **Status**: Actively exploited. CISA ordered federal agencies to prioritize patching by Sunday following the advisory.
- **CVE ID**: Not specified in source articles

### Oracle E-Business Suite Critical Vulnerability
- **Description**: A critical vulnerability in Oracle E-Business Suite financial application that is being actively exploited in ongoing attacks against federal systems.
- **Impact**: Potential compromise of financial systems, unauthorized access to sensitive financial data, and disruption of enterprise resource planning operations.
- **Status**: Actively exploited. CISA ordered federal agencies to secure systems by Saturday following the advisory.
- **CVE ID**: Not specified in source articles

### n8n Token Exchange Flaw
- **Description**: An authentication bypass vulnerability in n8n workflow automation platform's Enterprise edition. When configured to trust multiple external token issuers, the platform incorrectly matches an incoming JWT to a local user account, allowing attackers to log in as users from another trusted issuer.
- **Impact**: Unauthorized access to n8n instances, potential workflow manipulation, credential theft, and lateral movement within automation infrastructure.
- **Status**: Vulnerability disclosed; patch availability not specified in source.
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **Microsoft SharePoint Server**: All versions affected by CVE-2026-58644; patched in July 2026 Patch Tuesday
- **Fortinet FortiSandbox**: Threat detection platform; specific affected versions not disclosed in advisory
- **Oracle E-Business Suite**: Financial application suite; specific versions not disclosed in advisory
- **n8n Workflow Automation Platform**: Enterprise instances configured with multiple external token issuers
- **Windows Systems**: Targeted by ACR Stealer, TELEPUZ, OkoBot, ClickFix lures, and PhantomEnigma campaigns
- **macOS Systems**: Targeted by ClickLock infostealer (terminates apps every 210ms to coerce password entry)
- **Brazilian Government Websites**: 20+ hijacked sites repurposed as malware delivery channels
- **Shark RV2320EDUS Robot Vacuum**: Unpatched flaw allowing cross-device control within same AWS region
- **Claude for Chrome Extension**: Vulnerable to malicious extension triggering AI actions via simulated clicks
- **WebEx and Zoom Applications**: Trojanized installers distributing Starland RAT

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers compromise legitimate websites or create fake pages that display fraudulent error messages prompting users to run PowerShell commands or paste scripts into Terminal (macOS), leading to malware installation. Used by ACR Stealer, TELEPUZ, and PhantomEnigma campaigns.
- **Process Termination Coercion (ClickLock)**: Malware terminates all visible applications every 210 milliseconds, rendering the system unusable until the victim enters their system login password, which is then captured.
- **Trojanized Legitimate Software**: Russian threat actor UAT-11795 distributes Starland RAT through modified WebEx and Zoom installers, stealing credentials and cryptocurrency.
- **Hijacked Government Websites**: PhantomEnigma campaign compromised 20+ Brazilian government websites to serve as malware delivery channels, leveraging trust in official domains.
- **Token Issuer Confusion (n8n)**: Exploitation of multi-issuer JWT validation logic to authenticate as users from a different trusted identity provider.
- **AI Agent Data Injection**: Malicious data planted in sources consumed by AI agents (product reviews, GitHub threads) causes agents to execute unintended actions like clicking "Buy Now" or applying attacker-controlled code changes.
- **Chrome Extension Cross-Triggering**: Malicious Chrome extensions simulate user clicks to trigger predefined AI actions in the Claude extension, abusing its access to browser data and APIs.
- **Rapid Ransomware Deployment (Spirals)**: Full intrusion lifecycle—initial access, data theft, and encryption—completed in under 24 hours.
- **Certificate Extraction for Cross-Device Control**: Pulling certificates from Shark vacuum flash memory enables root command execution on other vacuums in the same AWS region.

## Threat Actor Activities

- **Scattered Spider (UNC3944)**: Cybercrime collective responsible for the 2024 Transport for London (TfL) hack causing £29 million in damages and disrupting services for 148 stations. Two members—Owen Flowers (18) and Thalha Jubair (20)—sentenced to 5.5 years each at Woolwich Crown Court on July 16, 2026.
- **UAT-11795 (Russian Financially Motivated Actor)**: Distributing Starland RAT via trojanized WebEx and Zoom applications to steal credentials and cryptocurrency.
- **China-Linked Threat Actor (Daxin/Stupig)**: Advanced malware Daxin resurfaced after 4+ years in a Taiwan manufacturing firm, accompanied by previously unreported Stupig pre-login SYSTEM backdoor.
- **PhantomEnigma Campaign Operators**: Compromised 20+ Brazilian government websites to create malware delivery infrastructure; uncovered by ANY.RUN interactive malware analysis.
- **GoSerpent Operators**: Previously undocumented malware targeting Southeast Asian government entities and diplomats for espionage since late 2025.
- **ACR Stealer Operators**: Infostealer active since 2024, now using ClickFix lures to harvest browser passwords, session tokens, PDFs, Microsoft 365 documents, and OneDrive-synced files.
- **TELEPUZ Operators**: New modular malware spreading via ClickFix since April 2026, featuring data theft and command execution capabilities.
- **OkoBot Framework Operators**: Deploying 20+ payloads focused on cryptocurrency wallet seed phrases, credentials, and sensitive data theft.
- **Spirals Ransomware Group**: New ransomware actor demonstrating exceptional speed—complete network encryption in under 24 hours from initial access.

## Source Attribution

- **Windows Server 2022 reach end of mainstream support in 90 days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-server-2022-reach-end-of-mainstream-support-in-90-days/
- **ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files**: The Hacker News - https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
- **New GoSerpent Malware Targets Southeast Asian Governments and Diplomats for Espionage**: The Hacker News - https://thehackernews.com/2026/07/new-goserpent-malware-targets-southeast.html
- **US charges two over laundering $43 million from investment fraud**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-two-over-laundering-43-million-from-investment-fraud/
- **CISA urges immediate action on actively exploited Fortinet flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV**: The Hacker News - https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **New ClickLock macOS malware traps users into revealing login password**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/
- **Coca-Cola says Fairlife ransomware attack halts US dairy production**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production/
- **Agentic AI Is Untamable: Ask the Right Security Questions**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/agentic-ai-untamable-ask-the-right-security-questions
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
- **CISA orders feds to patch actively exploited Oracle flaw by Saturday**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-flaw-by-saturday/
- **Russian hackers trojanize WebEx, Zoom apps to push Starland malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/russian-hackers-trojanize-webex-zoom-apps-to-push-starland-malware/
- **AI Can Find Bugs, But Human Knowledge Still Proves Them**: The Hacker News - https://thehackernews.com/2026/07/ai-can-find-bugs-but-human-knowledge.html
- **New Spirals ransomware encrypts victim network in under 24 hours**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-spirals-ransomware-encrypts-victim-network-in-under-24-hours/
- **Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide**: The Hacker News - https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html
- **OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol**: The Hacker News - https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html
