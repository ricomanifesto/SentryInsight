# Exploitation Report

## Executive Summary

Active exploitation activity has intensified across multiple vectors, with ransomware operations aggressively leveraging recently disclosed vulnerabilities for initial access. The Anubis ransomware group is actively exploiting Citrix Bleed 2 (CVE-2025-5777) to breach corporate networks, while Microsoft SharePoint Server faces ongoing attacks targeting CVE-2026-45659, a critical remote code execution flaw now listed on CISA's Known Exploited Vulnerabilities catalog. Simultaneously, Cisco has confirmed active exploitation of a Unified Communications Manager vulnerability patched in early June, demonstrating the rapid weaponization of disclosed flaws.

Supply chain attacks have evolved to target developers and researchers directly. North Korea-linked actors published malicious npm packages masquerading as Rollup polyfill tooling to steal secrets from development environments, while a new campaign dubbed ChocoPoC distributes a data-stealing RAT through fake proof-of-concept exploit repositories on GitHub, specifically targeting vulnerability researchers. These campaigns highlight a growing trend of compromising the software supply chain at its source.

Phishing-as-a-Service ecosystems continue to mature, with the ARToken platform exposing the extensive EvilTokens Microsoft 365 toolkit that enables rapid account takeover through ConsentFix and ClickFix techniques—bypassing MFA and hijacking tokens in seconds via malicious OAuth flows. Meanwhile, state-sponsored espionage remains persistent, as evidenced by Pegasus spyware compromising a European Parliament member investigating spyware abuse, and the ToddyCat-linked Umbrij malware abusing OAuth to access Gmail via Google APIs. New threat actors like Armored Likho are emerging, targeting government and critical infrastructure sectors across multiple countries with the BusySnake stealer.

## Active Exploitation Details

### Citrix Bleed 2 (CVE-2025-5777)
- **Description**: A critical vulnerability in Citrix NetScaler ADC and Gateway appliances that allows unauthenticated remote code execution. The flaw enables attackers to obtain initial access to organizational networks without valid credentials.
- **Impact**: Attackers achieve full system compromise, enabling lateral movement, credential harvesting, and ransomware deployment. The Anubis ransomware operation has been observed leveraging this vulnerability for initial access.
- **Status**: Actively exploited in the wild by Anubis ransomware affiliates. Patches are available from Citrix.
- **CVE ID**: CVE-2025-5777

### Microsoft SharePoint Server Remote Code Execution (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability affecting Microsoft SharePoint Server. The flaw allows authenticated attackers to execute arbitrary code on the server.
- **Impact**: Successful exploitation grants attackers code execution in the context of the SharePoint application pool, potentially leading to full server compromise, data exfiltration, and lateral movement within the corporate network.
- **Status**: Actively exploited in the wild. Added to CISA's Known Exploited Vulnerabilities (KEV) catalog on July 2026. Patched in May 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that was patched in early June 2026. Cisco has confirmed that attackers are actively exploiting this flaw.
- **Impact**: Exploitation could allow attackers to compromise the unified communications infrastructure, potentially enabling call interception, voicemail access, and lateral movement to connected systems.
- **Status**: Actively exploited. Patches released in early June 2026.

### Nextcloud Zero-Day Vulnerability
- **Description**: An undisclosed zero-day vulnerability in Nextcloud being exploited by FortiBleed campaign actors in conjunction with their Fortinet firewall credential theft operations.
- **Impact**: Provides attackers with additional attack surface after gaining initial access through compromised Fortinet credentials, enabling further lateral movement and data access.
- **Status**: Actively exploited as a zero-day. No patch information available in source materials.

### Langflow Remote Code Execution
- **Description**: A remote code execution vulnerability in Langflow, a framework for building AI applications. This flaw was exploited by an AI agent (designated JADEPUFFER) to automate a complete database ransomware attack.
- **Impact**: Represents the first observed case of an AI agent autonomously executing a ransomware attack from initial access through encryption. Enables unauthorized code execution and database compromise.
- **Status**: Actively exploited by AI-driven automation. Patch status not specified in source materials.

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: Appliances vulnerable to CVE-2025-5777 (Citrix Bleed 2); all unpatched versions prior to Citrix security bulletin fixes
- **Microsoft SharePoint Server**: On-premises SharePoint Server versions affected by CVE-2026-45659; patched in May 2026 cumulative updates
- **Cisco Unified Communications Manager**: Unified CM versions prior to the early June 2026 security patches; specific version details in Cisco advisory
- **Nextcloud**: Self-hosted Nextcloud instances targeted by zero-day exploitation; version specifics not disclosed
- **Langflow**: AI application framework installations vulnerable to RCE; affected versions not specified in reporting
- **npm Ecosystem / Rollup Users**: Developers using Rollup polyfill tooling targeted by malicious npm packages mimicking legitimate packages
- **GitHub / Python PoC Repositories**: Vulnerability researchers downloading proof-of-concept exploits from fake repositories distributing ChocoPoC RAT
- **Fortinet FortiGate Firewalls**: Devices compromised in FortiBleed campaign; credential theft affects administrative and VPN accounts
- **Microsoft 365 / Azure AD**: Tenants targeted by ARToken/EvilTokens PhaaS platform using OAuth-based token theft
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat's Umbrij malware abusing OAuth tokens via Google API
- **macOS Systems**: Users targeted by PamStealer via fake Maccy clipboard manager websites
- **iOS/Android Devices**: Targets of Pegasus spyware deployment against high-value individuals
- **Residential IoT/Router Devices**: Millions of home devices ensnared in NetNut/Popa residential proxy botnet

## Attack Vectors and Techniques

- **Citrix Bleed 2 Exploitation (CVE-2025-5777)**: Unauthenticated remote code execution on exposed NetScaler appliances; used by Anubis ransomware for initial access
- **SharePoint RCE Exploitation (CVE-2026-45659)**: Authenticated remote code execution against on-premises SharePoint servers; leveraged for network foothold
- **Cisco Unified CM Exploitation**: Active exploitation of patched vulnerability in voice/video infrastructure; attack specifics not fully disclosed
- **Nextcloud Zero-Day Exploitation**: Undisclosed vulnerability used post-exploitation after FortiBleed credential theft; enables lateral movement
- **Langflow RCE Automation by AI Agent**: First known case of AI agent (JADEPUFFER) autonomously exploiting RCE to deploy database ransomware end-to-end
- **npm Supply Chain Attack (Rollup Polyfill Impersonation)**: Malicious packages published to npm registry mimicking legitimate Rollup polyfill tooling; steals developer secrets and enables remote access
- **Fake PoC Repository Supply Chain Attack (ChocoPoC)**: Python proof-of-concept exploit repositories on GitHub weaponized with data-stealing RAT; targets vulnerability researchers specifically
- **Phishing-as-a-Service (ARToken/EvilTokens)**: Turnkey Microsoft 365 phishing toolkit with templates, credential harvesting, and token capture capabilities
- **ConsentFix / ClickFix OAuth Token Theft**: Malicious OAuth consent prompts and "ClickFix" social engineering trick users into authorizing attacker-controlled apps; hijacks M365 tokens in seconds, bypassing MFA
- **Pegasus Spyware Deployment**: Zero-click or one-click exploitation targeting mobile devices; used against high-profile political targets
- **Umbrij OAuth Abuse**: Malware steals OAuth tokens to access Gmail via Google API without triggering traditional credential theft alerts
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware groups loading vulnerable drivers to disable security tools and escalate privileges
- **PamStealer macOS Credential Theft**: Fake Maccy websites deliver malware that abuses PAM (Pluggable Authentication Modules) to extract login passwords
- **Interpol-Themed Social Engineering**: Ransomware campaigns impersonating law enforcement to lure small businesses into opening malicious content
- **Residential Proxy Botnet (NetNut/Popa)**: Millions of compromised home devices rented as exit nodes for malicious traffic anonymization
- **FortiBleed Credential Harvesting**: Large-scale theft of verified Fortinet firewall credentials; monetized through collaboration with INC and Lynx ransomware gangs
- **BusySnake Information Stealer**: Custom malware deployed by Armored Likho against government and energy sector targets for data exfiltration

## Threat Actor Activities

- **Anubis Ransomware Operation**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access; employs BYOVD techniques and supply chain credential theft
- **INC Ransomware Gang**: Collaborating with FortiBleed operators; using stolen Fortinet credentials for follow-on ransomware deployment
- **Lynx Ransomware Gang**: Partnered with FortiBleed campaign; monetizing compromised firewall access for ransomware operations
- **FortiBleed Campaign Operators**: Financially motivated group conducting large-scale Fortinet credential theft; also exploiting Nextcloud zero-day; credentials verified and sold/shared with INC/Lynx
- **North Korea-Linked Actors (DPRK)**: Operating malicious npm supply chain campaign; packages mimic Rollup polyfills to target developers globally
- **Armored Likho**: Previously undocumented threat actor targeting government agencies and electric power sector in Russia, Brazil, and Kazakhstan; deploys BusySnake stealer
- **ToddyCat**: Chinese-aligned APT group deploying new Umbrij malware; abuses OAuth tokens to access Gmail via Google API for espionage
- **NSO Group (Pegasus)**: Spyware vendor whose Pegasus tool compromised former European Parliament member Stelios Kouloglou during spyware investigation
- **JADEPUFFER (AI Agent Operator)**: Threat actor deploying AI agent to autonomously exploit Langflow RCE and execute database ransomware attacks
- **EvilTokens / ARToken Operators**: PhaaS providers offering Microsoft 365 phishing toolkit; ARToken operates as EvilTokens affiliate; enables ConsentFix/ClickFix attacks
- **ChocoPoC Operators**: Actors targeting vulnerability researchers via fake PoC repositories on GitHub; distributes data-stealing RAT in Python exploit code
- **Scattered Spider**: Hacking collective with member recently extradited to US; known for social engineering and SIM-swapping attacks
- **NetNut / Popa Botnet Operators**: Ran residential proxy service spanning 2 million home devices; infrastructure seized by FBI with industry partners

## Source Attribution

- **North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets**: The Hacker News - https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html
- **ARToken PhaaS exposes EvilTokens' Microsoft 365 phishing toolkit**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/
- **Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer**: The Hacker News - https://thehackernews.com/2026/07/armored-likho-targets-government.html
- **Chinese LLMs Broaden the Gap Between Attackers \&amp; Defenders**: Dark Reading - https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-and-defenders
- **European Parliament Member Investigating Spyware Was Hacked With Pegasus**: The Hacker News - https://thehackernews.com/2026/07/european-parliament-member.html
- **PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords**: The Hacker News - https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
- **Claude Fable 5 isn’t permanently leaving subscriptions, Anthropic says**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/
- **Claude Fable relaunch disappoints users with nerfed performance**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/
- **Aussies Face Reduced Cybercrime Risk, as Pressure Shifts to SMBs**: Dark Reading - https://www.darkreading.com/cybersecurity-analytics/aussies-face-reduced-cybercrime-risk-pressure-shifts-smbs
- **Apple Reverses Age-Old Patch Policy to Keep Up With AI**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/apple-patch-policy-ai
- **FBI Seizes NetNut Proxy Platform, Popa Botnet**: Krebs on Security - https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/
- **FortiBleed Actors Collaborating With Inc, Lynx Ransomware Gangs**: Dark Reading - https://www.darkreading.com/threat-intelligence/fortibleed-actors-inc-lynx-ransomware-gangs
- **Google Disrupts NetNut Residential Proxy Network Spanning 2 Million Home Devices**: The Hacker News - https://thehackernews.com/2026/07/google-disrupts-netnut-residential.html
- **Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials**: The Hacker News - https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
- **Ransomware Thugs Masquerade as Interpol to Entice Small Biz**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/attackers-use-interpol-lure-target-small-businesses
- **ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html
- **Google loses final appeal to overturn €4.1 billion EU fine**: Bleeping Computer - https://www.bleepingcomputer.com/news/legal/google-loses-final-appeal-to-overturn-41-billion-eu-fine/
- **ConsentFix and ClickFix: How Microsoft 365 Accounts are Hijacked in 3 Seconds**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/consentfix-and-clickfix-how-microsoft-365-accounts-are-hijacked-in-3-seconds/
- **ToddyCat-Linked Umbrij Malware Abuses OAuth to Access Gmail via Google API**: The Hacker News - https://thehackernews.com/2026/07/toddycat-linked-umbrij-malware-abuses.html
- **Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-
- **Microsoft fixes bug that removed Copilot buttons in Outlook**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-that-removed-copilot-button-in-outlook/
- **Cisco finally confirms attackers exploiting Unified CM flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/
- **Identity Lifecycle Management Wasn't Built for AI Agents**: The Hacker News - https://thehackernews.com/2026/07/identity-lifecycle-management.html
- **CISA: Microsoft SharePoint RCE flaw now actively exploited**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
- **Opera rolls out Paste Protect feature to fight ClickFix attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/opera-rolls-out-paste-protect-feature-to-fight-clickfix-attacks/
- **AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack**: The Hacker News - https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
- **Alleged Scattered Spider hacker extradited to the United States**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/alleged-scattered-spider-hacker-extradited-to-the-united-states/
- **FortiBleed Credential Theft Linked to INC and Lynx Ransomware Operations**: The Hacker News - https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html
- **New ChocoPoC RAT Targets Vulnerability Researchers via Fake PoC Exploit Repos**: The Hacker News - https://thehackernews.com/2026/07/new-chocopoc-rat-targets-vulnerability.html
- **SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation**: The Hacker News - https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
