# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors leveraging both novel malware frameworks and proven social engineering techniques to compromise targets at speed. The ClickLock macOS infostealer demonstrates a coercive new approach—forcing credential entry by terminating user applications every 210 milliseconds—while the OkoBot framework deploys over twenty payloads to harvest cryptocurrency wallets and credentials. Ransomware operations continue to accelerate, with the Spirals actor completing full intrusion-to-encryption cycles in under twenty-four hours, and a Fairlife (Coca-Cola subsidiary) attack halting U.S. dairy production. Meanwhile, supply-chain and software supply-chain compromises are expanding: Russian actor UAT-11795 is distributing trojanized WebEx and Zoom installers to deliver the Starland RAT, and more than twenty Brazilian government websites have been hijacked into malware delivery channels via the PhantomEnigma campaign.

Critical vulnerabilities in widely deployed enterprise and consumer software are under active exploitation or pose imminent risk. CISA has ordered federal agencies to patch an actively exploited Oracle E-Business Suite flaw by an emergency deadline, and Zoom has released fixes for CVE-2026-53412, a critical Windows vulnerability enabling unauthenticated account takeover. An n8n token-exchange flaw allows cross-issuer authentication bypass on enterprise instances, while an unpatched Shark robot vacuum vulnerability permits region-wide remote control via extracted certificates. The Daxin malware—attributed to a China-linked actor—has resurfaced in Taiwan after four years alongside the previously undocumented Stupig pre-login SYSTEM backdoor, signaling persistent advanced persistent threat activity.

Identity-centric attacks have overtaken exploitation as the leading ransomware root cause, with multifactor authentication failing to prevent compromise in 97% of credential-based incidents. AI-driven threat surfaces are expanding rapidly: over one million phishing emails have used hidden-text salting to evade LLM-based filters, a Claude Chrome extension flaw permits malicious extensions to simulate clicks and trigger AI actions, and new agent data-injection techniques can manipulate AI agents into executing attacker-controlled commands. Law enforcement actions have disrupted major fraud operations—including a €140 million Spanish ring and a €100 million Dutch investment scheme—while two Scattered Spider members received 5.5-year sentences for the £29 million Transport for London breach.

## Active Exploitation Details

### ClickLock macOS Infostealer
- **Description**: A new macOS information-stealing malware that terminates all visible user processes in a tight loop (every 210 milliseconds) to coerce victims into entering their system login password. The malware arrives as a command pasted into Terminal and refuses to release the system until credentials are provided.
- **Impact**: Attackers obtain the victim's macOS login password, which can unlock keychains, enable privilege escalation, and provide access to encrypted data and authentication tokens stored on the system.
- **Status**: Actively deployed in the wild. No patch available; defense relies on user awareness and endpoint detection of rapid process termination patterns.
- **CVE ID**: Not assigned (malware behavior, not a software vulnerability)

### OkoBot Multi-Payload Framework
- **Description**: A modular malicious framework delivering more than twenty distinct payloads in campaigns focused on stealing cryptocurrency wallet seed phrases, credentials, and other sensitive data.
- **Impact**: Broad data theft including crypto wallet credentials, browser-stored passwords, session tokens, and personally identifiable information. Modular design allows operators to customize payloads per target.
- **Status**: Active campaigns observed. No vendor patch; detection requires behavioral analysis and payload-specific signatures.
- **CVE ID**: Not assigned (malware framework, not a software vulnerability)

### Spirals Ransomware
- **Description**: A new ransomware actor completing full attack chains—from initial access through data exfiltration to encryption—in under twenty-four hours.
- **Impact**: Rapid network-wide encryption, data theft for double-extortion leverage, and minimal dwell time for detection and response.
- **Status**: Active intrusions reported. No decryptor available; recovery depends on backups.
- **CVE ID**: Not assigned (ransomware operation, not a specific vulnerability)

### PhantomEnigma Government Website Compromise
- **Description**: More than twenty Brazilian government websites hijacked and repurposed as malware delivery channels in an active campaign uncovered by ANY.RUN.
- **Impact**: Visitors to trusted government domains exposed to drive-by downloads and malicious payloads; undermines trust in public-sector digital services.
- **Status**: Campaign active at time of discovery. Affected sites require forensic cleanup and credential rotation.
- **CVE ID**: Not assigned (compromise method not specified in source)

### Daxin Malware and Stupig Backdoor Resurgence
- **Description**: The advanced Daxin malware—previously attributed to a China-linked threat actor—has resurfaced after more than four years within a Taiwan manufacturing firm, accompanied by a previously unreported backdoor dubbed Stupig that achieves pre-login SYSTEM-level persistence.
- **Impact**: Long-term stealthy access to high-value targets, pre-authentication SYSTEM privileges, and potential lateral movement across air-gapped or segmented networks.
- **Status**: Active intrusion discovered in Taiwan. Indicators of compromise available for hunting.
- **CVE ID**: Not assigned (malware and backdoor, not a specific vulnerability)

### UAT-11795 Trojanized Software Supply Chain
- **Description**: Financially motivated Russian threat actor UAT-11795 is distributing trojanized installers for WebEx and Zoom applications to deploy the Starland RAT backdoor.
- **Impact**: Credential theft, cryptocurrency wallet compromise, and persistent remote access via legitimate-appearing software updates.
- **Status**: Active distribution campaigns. Users downloading from unofficial or compromised sources at risk.
- **CVE ID**: Not assigned (supply-chain compromise, not a software vulnerability)

### Fairlife Ransomware Attack
- **Description**: Ransomware attack on Fairlife, a Coca-Cola subsidiary, disrupting operations and temporarily suspending production of Fairlife products across the United States.
- **Impact**: Operational disruption to dairy production and supply chain; potential data exfiltration for extortion.
- **Status**: Incident disclosed by Coca-Cola; recovery underway. Ransomware variant not publicly identified.
- **CVE ID**: Not assigned (initial access vector not specified in source)

### CVE-2026-53412 — Zoom Workplace for Windows Account Takeover
- **Description**: Critical vulnerability in Zoom Workplace for Windows and the Zoom Windows SDK that allows an unauthenticated attacker to hijack user accounts.
- **Impact**: Full account takeover without user interaction, enabling access to meetings, recordings, contacts, and potential lateral movement via Zoom integration tokens.
- **Status**: Patched by Zoom. CISA and vendors urge immediate updating. Actively exploitable prior to patch.
- **CVE ID**: CVE-2026-53412

### Oracle E-Business Suite Actively Exploited Flaw
- **Description**: Critical vulnerability in Oracle E-Business Suite financial application under active exploitation, prompting CISA to issue an emergency directive for federal agencies to patch by a Saturday deadline.
- **Impact**: Potential compromise of financial systems, data exfiltration, and unauthorized transactions in enterprise ERP environments.
- **Status**: Actively exploited in the wild. Oracle patch available; emergency patching mandated for U.S. federal agencies.
- **CVE ID**: Not explicitly provided in source articles

### n8n Token Exchange Authentication Bypass
- **Description**: Flaw in the n8n workflow automation platform's Enterprise edition where instances configured to trust multiple external token issuers incorrectly match an incoming JWT to a local user account, allowing authentication as another issuer's user.
- **Impact**: Cross-tenant account takeover on multi-issuer n8n deployments, enabling unauthorized workflow execution and data access.
- **Status**: Vulnerability disclosed; patch status not specified in source. Affects Enterprise instances with multiple trusted token issuers.
- **CVE ID**: Not explicitly provided in source articles

### Claude Chrome Extension Click-Simulation Flaw
- **Description**: Vulnerability in Anthropic's Claude for Chrome browser extension allowing a malicious extension to simulate user clicks and trigger predefined AI actions, potentially abusing Claude's access to page content and user data.
- **Impact**: Unauthorized AI actions on behalf of the user, data exfiltration via prompted responses, and potential chain attacks with other browser permissions.
- **Status**: Flaw disclosed; patch status not specified in source.
- **CVE ID**: Not explicitly provided in source articles

### Shark RV2320EDUS Robot Vacuum Certificate Extraction Flaw
- **Description**: Unpatched vulnerability allowing attackers to extract a certificate from the flash memory of a Shark RV2320EDUS robot vacuum and use it to execute root commands on other Shark vacuums within the same AWS region.
- **Impact**: Remote camera access, robot movement control, data reading, and potential network pivoting across regionally co-located devices.
- **Status**: Unpatched at time of reporting. No vendor fix announced.
- **CVE ID**: Not explicitly provided in source articles

### UEFI Shim Bootloader Secure Boot Bypass
- **Description**: Nearly a dozen vulnerable and revoked UEFI shim bootloaders remained trusted by the Microsoft UEFI CA for years, providing a persistent path to bypass Secure Boot protections.
- **Impact**: Bootkit installation, pre-OS persistence, and evasion of Secure Boot attestation on affected hardware.
- **Status**: Bootloaders now revoked; however, systems with outdated revocation lists (DBX) remain vulnerable. Requires firmware/DBX updates.
- **CVE ID**: Not explicitly provided in source articles

### TELEPUZ Modular Malware via ClickFix
- **Description**: New modular malware (TELEPUZ) spreading since late April 2026 via ClickFix social-engineering lures on compromised websites, delivering full-featured data theft and command execution capabilities.
- **Impact**: Credential harvesting, cryptocurrency theft, arbitrary command execution, and persistent access via modular plugin architecture.
- **Status**: Active campaigns. ClickFix technique remains effective against unaware users.
- **CVE ID**: Not assigned (malware delivery technique, not a software vulnerability)

### Agent Data Injection Attacks on AI Agents
- **Description**: Novel attack technique where planted data (e.g., malicious reviews, poisoned GitHub threads) causes AI agents to misclick UI elements or execute attacker-supplied commands during autonomous operation.
- **Impact**: Unauthorized purchases, code execution, data exfiltration, and privilege escalation via compromised AI agent actions.
- **Status**: Emerging technique demonstrated in research; real-world exploitation risk rising with agentic AI adoption.
- **CVE ID**: Not assigned (attack technique, not a specific vulnerability)

### Hidden-Text Salting Evading AI Phishing Filters
- **Description**: Over one million phishing emails observed using "text salting" (hidden characters, zero-width spaces, CSS tricks) to deceive LLM-based security filters while rendering normally to human recipients.
- **Impact**: Bypass of AI-driven email security gateways, increased phishing delivery rates to inboxes.
- **Status**: Active technique at scale. Requires updated filter training and rendering-based analysis.
- **CVE ID**: Not assigned (evasion technique, not a software vulnerability)

## Affected Systems and Products

- **macOS (ClickLock Infostealer)**: All macOS versions supporting Terminal command execution; no version-specific mitigation identified.
- **Windows Zoom Workplace & SDK (CVE-2026-53412)**: Zoom Workplace for Windows and Zoom Windows SDK versions prior to the July 2026 security update.
- **Oracle E-Business Suite**: Financial application modules; specific versions not detailed in source—refer to Oracle Critical Patch Update advisory.
- **n8n Enterprise (Multi-Issuer Configurations)**: Enterprise instances configured with more than one external token issuer (OIDC/SAML/JWT providers).
- **Anthropic Claude for Chrome Extension**: All versions prior to vendor fix; Chrome browser on Windows, macOS, Linux.
- **Shark RV2320EDUS Robot Vacuum**: Specific model RV2320EDUS; potentially other models sharing certificate infrastructure in same AWS region.
- **UEFI Systems with Microsoft CA Trust**: Any system booting with UEFI Secure Boot using Microsoft UEFI CA and outdated DBX revocation lists; affects diverse hardware vendors.
- **Brazilian Government Websites (PhantomEnigma)**: 20+ .gov.br domains compromised; underlying CMS/web server software not specified.
- **WebEx & Zoom Installers (Trojanized)**: Unofficial or supply-chain-compromised installers for Cisco WebEx and Zoom; legitimate vendor binaries not affected.
- **n8n Workflow Automation Platform**: Enterprise edition with multi-issuer authentication configuration.
- **AI Agent Platforms (Data Injection)**: Any LLM-driven agent with autonomous UI interaction capabilities (browser, IDE, API clients) processing untrusted external content.

## Attack Vectors and Techniques

- **Coercive Credential Harvesting (ClickLock)**: Rapid process termination loop (210ms interval) forces user to enter login password to regain system control.
- **Modular Payload Delivery (OkoBot)**: Framework drops 20+ specialized payloads for crypto wallets, browsers, password managers, and system enumeration.
- **Speed Ransomware (Spirals)**: Initial access → lateral movement → exfiltration → encryption in <24 hours; likely leveraging valid accounts and living-off-the-land binaries.
- **Trusted Website Compromise (PhantomEnigma)**: Legitimate government domains repurposed for drive-by malware delivery via injected scripts/iframes.
- **Pre-Login SYSTEM Backdoor (Stupig)**: Achieves kernel-level persistence before user authentication, surviving OS reinstalls and disk encryption unlock.
- **Supply-Chain Trojanization (UAT-11795/Starland)**: Legitimate software installers modified post-build to include RAT; distributed via typosquatting, compromised mirrors, or malicious ads.
- **ClickFix Social Engineering (TELEPUZ)**: Fake "verify you are human" / "fix display" prompts trick users into pasting malicious PowerShell into Run dialog or Terminal.
- **Cross-Issuer JWT Confusion (n8n)**: Platform matches incoming token to local user by identifier only, ignoring issuer claim, enabling cross-tenant impersonation.
- **Extension Click-Simulation (Claude Chrome)**: Malicious extension uses `chrome.debugger` or synthetic events to trigger AI actions in Claude extension context.
- **Certificate Extraction & Replay (Shark Vacuum)**: Physical/flash access to one device yields cert valid for regional fleet; MQTT/websocket command injection as root.
- **Revoked Bootloader Trust (UEFI Shim)**: Microsoft UEFI CA continued trusting revoked shims; attackers roll back to vulnerable shim for Secure Boot bypass.
- **Agent Data Injection (AI Agents)**: Adversarial content in reviews, docs, code comments hijacks agent reasoning → unintended clicks, commands, API calls.
- **Text Salting / Homoglyph Obfuscation (Phishing)**: Zero-width joiners, CSS `display:none`, Unicode lookalikes hide malicious text from LLMs while rendering to users.
- **Identity-Centric Ransomware Access**: Valid credentials (phished, leaked, sprayed) + MFA fatigue/bypass → initial access in 97% of credential-based ransomware cases.

## Threat Actor Activities

- **Scattered Spider (UNC3944 / Octo Tempest)**: Two members (Owen Flowers, 18; Thalha Jubair, 20) sentenced to 5.5 years each for 2024 Transport for London breach causing £29M impact and 148 system compromises. Group known for SIM-swapping, MFA bombing, and SaaS credential theft.
- **UAT-11795 (Russian Financially Motivated)**: Active trojanized WebEx/Zoom campaign delivering Starland RAT; targets credentials and cryptocurrency; operates via software supply-chain compromise.
- **PhantomEnigma (Campaign)**: Active compromise of 20+ Brazilian government websites for malware delivery; infrastructure and attribution under investigation by ANY.RUN and authorities.
- **China-Linked APT (Daxin/Stupig Operator)**: Daxin malware resurfaced in Taiwan manufacturing target after 4+ years; Stupig backdoor provides pre-login SYSTEM access; indicates long-term strategic access operation.
- **Spirals Ransomware Group**: New ransomware actor demonstrating extreme velocity (<24h full attack chain); victimology and ransom demands not fully characterized.
- **Iberian Cyber Fraud Ring (Spain)**: Dismantled by police; €140M fraud via diverse cyberattacks and complex money laundering; multiple arrests.
- **Dutch Investment Fraud Network**: International scheme with tens of thousands of victims and >€100M stolen; multiple arrests by Dutch Police.
- **Unknown/Unattributed (ClickLock, OkoBot, TELEPUZ, n8n exploitation, Shark vacuum research)**: No actor attribution in source articles; likely crimeware operators or independent researchers.

## Source Attribution

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
- **Zoom Patches Critical Windows Flaw That Could Enable Account Takeover**: The Hacker News - https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html
- **Police Disrupt a €140M Cyber Fraud Ring in Spain**: Dark Reading - https://www.darkreading.com/threat-intelligence/police-disrupt-140m-euro-cyber-fraud-ring-spain
- **Dutch police bust investment fraud ring stealing over €100 million**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/dutch-police-bust-investment-fraud-ring-stealing-over-100-million/
- **Forgotten Bootloaders Expose Secure Boot Blind Spot**: Dark Reading - https://www.darkreading.com/cyber-risk/forgotten-bootloaders-expose-secure-boot-blind-spot
- **Identity Attacks Overtake Exploits as Top Ransomware Cause**: Dark Reading - https://www.darkreading.com/identity-access-management-security/identity-attacks-overtake-exploits-top-ransomware-cause
- **Zoom warns of critical account takeover vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/zoom-warns-of-critical-account-takeover-vulnerability/
