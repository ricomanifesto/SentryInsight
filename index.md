# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple vectors this reporting period, with federal agencies ordered to patch an actively exploited Oracle E-Business Suite flaw under emergency CISA directive. A new macOS information stealer called ClickLock employs aggressive process termination every 210 milliseconds to coerce victims into surrendering login credentials, while the OkoBot framework deploys over 20 payloads targeting cryptocurrency wallets and sensitive data. Ransomware operations continue accelerating, with the new Spirals actor completing full intrusion-to-encryption cycles in under 24 hours, and a Fairlife ransomware attack halting Coca-Cola's US dairy production.

Multiple critical vulnerabilities have been identified in widely deployed software. Zoom patched CVE-2026-53412, a critical account takeover flaw in Zoom Workplace for Windows. The n8n workflow automation platform contains a token exchange vulnerability allowing cross-issuer authentication bypass on Enterprise instances. Russian threat actor UAT-11795 distributes the Starland RAT through trojanized WebEx and Zoom installers, while China-linked actors have resurfaced the Daxin malware alongside a novel Stupig pre-login SYSTEM backdoor in Taiwan manufacturing environments.

Threat actor accountability advances with two Scattered Spider members sentenced to 5.5 years each for the £29 million Transport for London breach. Law enforcement disrupted a €140 million cyber fraud ring in Spain and a €100 million investment fraud operation in the Netherlands. Meanwhile, over 20 Brazilian government websites were hijacked into malware delivery channels by the PhantomEnigma campaign, and more than one million phishing emails leveraged hidden text salting to evade AI security filters.

## Active Exploitation Details

### Oracle E-Business Suite Critical Vulnerability
- **Description**: A critical vulnerability in Oracle E-Business Suite financial application is being actively exploited in the wild. CISA issued an emergency directive ordering all federal civilian executive branch agencies to secure their systems by Saturday.
- **Impact**: Attackers can exploit this flaw to compromise financial systems, potentially leading to unauthorized access, data theft, and financial fraud within federal agencies and other organizations running vulnerable versions.
- **Status**: Actively exploited; CISA emergency directive issued requiring immediate patching by federal agencies. Patch availability confirmed through Oracle security updates.

### ClickLock macOS Information Stealer
- **Description**: A new macOS malware family dubbed ClickLock terminates all visible user processes in a continuous loop (every 210 milliseconds) to force victims into entering their system login password. The malware arrives via a command pasted into Terminal and presents a fake authentication prompt that captures credentials.
- **Impact**: Full system credential theft enabling persistent access, privilege escalation, and potential lateral movement. The aggressive process-killing technique renders the system unusable until compliance, creating high-pressure social engineering.
- **Status**: Actively distributed; no patch required as this is malware behavior rather than a software vulnerability. Detection signatures being deployed by macOS security tools.

### OkoBot Multi-Payload Framework
- **Description**: A modular malicious framework delivering more than 20 distinct payloads in coordinated attacks. The framework focuses on stealing cryptocurrency wallet seed phrases, credentials, and other sensitive data through a flexible plugin architecture.
- **Impact**: Comprehensive data theft including crypto assets, authentication credentials, browser data, and system information. Modular design allows rapid adaptation and payload customization per target.
- **Status**: Active deployment in the wild; framework actively maintained with new payloads added regularly.

### TELEPUZ Modular Malware
- **Description**: A full-featured modular malware spreading via ClickFix social engineering lures on compromised websites since late April 2026. TELEPUZ steals data and executes arbitrary commands through a plugin-based architecture.
- **Impact**: Persistent remote access, data exfiltration, command execution, and potential lateral movement. ClickFix delivery leverages fake browser error pages to trick users into running malicious PowerShell commands.
- **Status**: Active campaigns observed since April 2026; ClickFix delivery vector remains highly effective.

### Spirals Ransomware
- **Description**: A new ransomware actor demonstrating exceptionally rapid operations, completing full corporate intrusions—from initial access through data theft to encryption—in under 24 hours.
- **Impact**: Near-total operational disruption with minimal dwell time for detection. Double extortion model with data theft preceding encryption increases leverage for ransom payment.
- **Status**: Active intrusions confirmed; speed of execution suggests highly automated or well-rehearsed playbooks.

### Zoom Workplace for Windows Account Takeover (CVE-2026-53412)
- **Description**: Critical vulnerability in Zoom Workplace for Windows and Zoom SDK for Windows allowing unauthenticated attackers to hijack user accounts. The flaw carries a high CVSS score and affects the desktop client on Windows platforms.
- **Impact**: Full account takeover enabling unauthorized meeting access, contact list theft, recorded meeting access, and potential further social engineering within the organization.
- **Status**: Patched in latest Zoom Workplace and SDK releases; active exploitation risk high prior to patch deployment.
- **CVE ID**: CVE-2026-53412

### n8n Token Exchange Authentication Bypass
- **Description**: Flaw in n8n workflow automation platform's Enterprise edition where instances configured to trust multiple external token issuers incorrectly match incoming JWTs to local users, allowing authentication as users from a different trusted issuer.
- **Impact**: Cross-tenant authentication bypass enabling unauthorized access to workflows, credentials stored in n8n, and potential lateral movement through automated processes.
- **Status**: Vulnerability disclosed; patch status pending vendor advisory. Affects Enterprise instances with multi-issuer configurations.

### Claude Chrome Extension Flaw
- **Description**: Vulnerability in Anthropic's Claude for Chrome browser extension allowing malicious extensions to simulate user clicks and trigger predefined AI actions, potentially abusing Claude's access to page content and user data.
- **Impact**: Unauthorized AI action execution, potential data exfiltration through prompted responses, and abuse of extension permissions granted by the user.
- **Status**: Flaw disclosed; mitigation requires extension update or removal pending vendor fix.

### Daxin Malware and Stupig Backdoor
- **Description**: Advanced malware previously attributed to a China-linked threat actor resurfaced after four years in a Taiwan manufacturing firm, accompanied by a previously unreported backdoor dubbed Stupig that achieves pre-login SYSTEM-level persistence.
- **Impact**: Deep system persistence surviving reboots and credential changes, pre-authentication access at SYSTEM privilege level, and long-term espionage positioning in critical manufacturing infrastructure.
- **Status**: Active intrusion identified; Stupig represents novel boot-persistence technique.

### Starland RAT via Trojanized Applications
- **Description**: Russian financially motivated threat actor UAT-11795 distributes Starland RAT through trojanized legitimate software installers for WebEx and Zoom, stealing credentials and cryptocurrency.
- **Impact**: Full remote access trojan capabilities including keylogging, screen capture, file exfiltration, crypto wallet theft, and persistent backdoor access. Legitimate application veneer evades user suspicion.
- **Status**: Active distribution campaigns; trojanized installers hosted on convincing lookalike domains.

### PhantomEnigma Government Website Compromise
- **Description**: Over 20 Brazilian government websites hijacked and converted into malware delivery channels through an active campaign uncovered by ANY.RUN interactive malware analysis.
- **Impact**: Supply chain-style compromise leveraging trust in government domains for drive-by downloads, credential harvesting, and malware distribution to citizens and government employees.
- **Status**: Active campaign; compromised sites remediated following discovery.

## Affected Systems and Products

- **Oracle E-Business Suite**: Financial application modules; versions prior to latest security patch; enterprise ERP environments across federal agencies and private sector
- **Zoom Workplace for Windows**: Desktop client versions prior to patched release; Zoom SDK for Windows; Windows 10/11 platforms
- **n8n Workflow Automation Platform**: Enterprise edition instances configured with multiple external token issuers (OIDC/SAML); self-hosted and cloud deployments
- **macOS Systems**: All versions susceptible to ClickLock social engineering attack; Terminal access required for initial execution
- **Claude for Chrome Extension**: Browser extension versions prior to fix; Chrome and Chromium-based browsers
- **Shark RV2320EDUS Robot Vacuum**: IoT device with certificate extraction vulnerability; AWS region-wide impact potential for same-model devices
- **UEFI Shim Bootloaders**: Nearly a dozen revoked but still-trusted shim bootloaders; affects Secure Boot implementations across x86_64 and ARM64 platforms
- **WebEx and Zoom Installers**: Trojanized versions distributed via malicious domains; Windows executables masquerading as legitimate conferencing software
- **Brazilian Government Web Portals**: 20+ .gov.br domains compromised for malware hosting; citizen-facing services and internal portals

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Fake browser error pages (Chrome, Firefox, Edge) prompting users to copy-paste PowerShell commands into Run dialog or Terminal; delivers TELEPUZ and other payloads
- **Hidden Text Salting (Text Salting)**: Invisible Unicode characters and CSS-hidden text inserted into phishing emails to evade AI/LLM-based security filters while remaining invisible to human recipients; over 1 million emails observed
- **Trojanized Legitimate Software**: Malicious actors recompile or wrap genuine WebEx/Zoom installers with Starland RAT; distributed via typosquatting domains and malicious search results
- **Process Termination Coercion**: ClickLock kills all visible user processes every 210ms via macOS accessibility APIs, rendering system unusable until victim enters credentials at fake auth prompt
- **Agent Data Injection**: Malicious content planted in web pages, documents, or code repositories causes AI agents to execute unintended actions (clicks, purchases, code changes) when summarizing or processing injected content
- **Cross-Issuer Token Confusion**: n8n Enterprise matches JWT from Issuer A to user account linked to Issuer B when both are trusted, enabling authentication bypass without credential theft
- **Pre-Login SYSTEM Persistence**: Stupig backdoor achieves boot-level persistence before user authentication, surviving credential rotation and OS reinstallation via bootloader/UEFI manipulation
- **Government Website Supply Chain Compromise**: PhantomEnigma injects malicious scripts into legitimate .gov.br sites, converting trusted domains into drive-by download and credential harvesting platforms
- **Rapid Ransomware Execution**: Spirals automates reconnaissance, lateral movement, data staging, and encryption to complete full attack cycle in <24 hours, minimizing detection window
- **Extension Permission Abuse**: Malicious Chrome extensions simulate user clicks on Claude extension UI to trigger AI actions with victim's permissions and context access

## Threat Actor Activities

- **Scattered Spider (UNC3944/Scatter Swine)**: Two core members (Owen Flowers, 18; Thalha Jubair, 20) sentenced to 5.5 years each for 2024 Transport for London breach causing £29M damage and 148,000+ customer records exposed; group known for SIM-swapping, MFA fatigue, and SaaS credential theft
- **UAT-11795 (Russian Financially Motivated)**: Active distribution of Starland RAT via trojanized WebEx/Zoom installers; targets credentials and cryptocurrency; operates convincing lookalike download infrastructure
- **China-Linked APT (Daxin/Stupig Operators)**: Resurfaced Daxin malware after 4+ year hiatus in Taiwan manufacturing sector; deployed novel Stupig pre-login SYSTEM backdoor indicating advanced bootkit/UEFI capabilities; espionage-focused
- **PhantomEnigma**: Brazilian campaign compromising 20+ government websites for malware delivery; leverages trust in .gov.br domains; infrastructure supports drive-by downloads and credential harvesting
- **Spirals Ransomware Group**: New actor demonstrating sub-24-hour full intrusion cycle; highly automated or rehearsed playbook; double extortion with data theft prior to encryption
- **OkoBot Operators**: Framework developers and affiliates deploying 20+ modular payloads; focus on cryptocurrency wallet seed phrases and credential harvesting; active maintenance and payload updates
- **Iberian Cyber Fraud Ring (Spain)**: Dismantled €140M operation involving multiple attack vectors and complex money laundering networks; multiple arrests by Spanish National Police
- **Dutch Investment Fraud Network**: International scheme with tens of thousands of victims and €100M+ stolen; multiple arrests by Dutch Police; infrastructure spanned multiple countries

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
