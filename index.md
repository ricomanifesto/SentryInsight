# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with ransomware groups rapidly weaponizing recently disclosed vulnerabilities and threat actors adopting novel techniques including AI-driven automation. The Citrix Bleed 2 vulnerability (CVE-2025-5777) is now being exploited by Anubis ransomware for initial access, while a critical Microsoft SharePoint RCE (CVE-2026-45659) has been added to CISA's Known Exploited Vulnerabilities catalog after confirmed active exploitation. Simultaneously, Cisco has confirmed attackers are exploiting a Unified Communications Manager flaw patched in early June, demonstrating the compressed timeline between patch availability and weaponization.

Threat actor collaboration is escalating, with the FortiBleed credential-theft campaign—targeting Fortinet firewall credentials—now attributed to both INC and Lynx ransomware operations, indicating stolen credentials are fueling follow-on intrusions. In a significant development, Sysdig researchers identified the first known ransomware attack executed end-to-end by an AI agent (tracked as JADEPUFFER), which exploited a Langflow RCE to automate database encryption. Law enforcement disruption continues with the FBI seizing the NetNut residential proxy platform and Popa botnet infrastructure spanning two million home devices, while an alleged Scattered Spider member has been extradited to the United States.

Social engineering and identity-focused attacks remain prevalent with new macOS malware PamStealer stealing login credentials through fake Maccy clipboard manager sites and PAM abuse, while ClickFix and ConsentFix techniques hijack Microsoft 365 accounts in seconds via OAuth flow manipulation. The ToddyCat APT has deployed new Umbrij malware abusing OAuth to access Gmail via Google API, and attackers are targeting vulnerability researchers through trojanized proof-of-concept exploits (ChocoPoC RAT) hosted on GitHub. Phishing campaigns now auto-adapt payloads based on victim device fingerprinting, and ransomware operators are masquerading as Interpol to target small businesses globally.

## Active Exploitation Details

### Citrix Bleed 2 (CVE-2025-5777)
- **Description**: A critical vulnerability in Citrix NetScaler ADC and Gateway appliances that allows unauthenticated attackers to obtain active session cookies and bypass authentication controls.
- **Impact**: Attackers gain initial access to organizational networks without credentials, enabling lateral movement and ransomware deployment. Anubis ransomware operators are actively exploiting this flaw for entry.
- **Status**: Actively exploited in the wild by Anubis ransomware group. Patches available from Citrix.
- **CVE ID**: CVE-2025-5777

### Microsoft SharePoint Remote Code Execution (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability affecting Microsoft SharePoint Server that allows authenticated attackers to execute arbitrary code on the server.
- **Impact**: Full server compromise leading to data theft, lateral movement, and persistence in enterprise environments. Added to CISA KEV catalog confirming active exploitation.
- **Status**: Actively exploited in the wild. Patched in May 2026. CISA has mandated federal agencies to patch by August 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that allows attackers to execute unauthorized actions on affected systems.
- **Impact**: Compromise of enterprise voice and video communication infrastructure, potential for eavesdropping, call manipulation, and lateral movement.
- **Status**: Cisco has confirmed active exploitation in the wild. Patch released in early June 2026.
- **CVE ID**: [CVE ID not provided in source articles]

### FortiBleed Credential Theft Campaign
- **Description**: A large-scale credential theft campaign targeting Fortinet firewall appliances, resulting in verified stolen credentials from thousands of devices.
- **Impact**: Stolen VPN and administrative credentials enabling follow-on network intrusions, ransomware deployment, and persistent access. Credentials attributed to INC and Lynx ransomware operations for monetization.
- **Status**: Active campaign with confirmed collaboration between FortiBleed actors and INC/Lynx ransomware gangs. Nextcloud zero-day bug also being exploited by same actors.
- **CVE ID**: [CVE ID not provided in source articles]

### Langflow RCE Exploitation by AI Agent
- **Description**: A remote code execution vulnerability in Langflow, a framework for building AI applications, exploited by an autonomous AI agent to conduct ransomware attacks.
- **Impact**: First documented case of an AI agent (JADEPUFFER) autonomously executing a complete ransomware attack chain—from initial exploitation through database encryption—without human intervention.
- **Status**: Actively exploited. Attack automated database ransomware deployment via AI agent.
- **CVE ID**: [CVE ID not provided in source articles]

### PamStealer macOS Information Stealer
- **Description**: A new macOS malware that distributes through fake websites mimicking the legitimate Maccy clipboard manager application, then abuses Pluggable Authentication Modules (PAM) to capture user login passwords.
- **Impact**: Theft of macOS user credentials, potential privilege escalation, and access to keychain data. Targets users seeking clipboard management utilities.
- **Status**: Active distribution via typosquatted/fake Maccy download sites. No patch available (malware, not vulnerability).
- **CVE ID**: [CVE ID not provided in source articles]

### ClickFix and ConsentFix Microsoft 365 Account Hijacking
- **Description**: Attack techniques using fake verification prompts and malicious OAuth consent flows to steal Microsoft 365 authentication tokens, bypassing MFA in seconds.
- **Impact**: Full account takeover including email, OneDrive, Teams, and SharePoint access. Tokens stolen within 3 seconds of user interaction.
- **Status**: Actively exploited in the wild. Opera has released Paste Protect feature to mitigate; Microsoft guidance issued.
- **CVE ID**: [CVE ID not provided in source articles]

### ToddyCat Umbrij Malware OAuth Abuse
- **Description**: Malware attributed to the ToddyCat APT that abuses OAuth authorization flows to gain persistent access to victim Gmail accounts via the Google API.
- **Impact**: Surreptitious access to email correspondence, contact lists, and Google Drive data without triggering traditional credential theft alerts.
- **Status**: Active deployment by ToddyCat threat actor. Leverages legitimate OAuth infrastructure for stealth.
- **CVE ID**: [CVE ID not provided in source articles]

### ChocoPoC RAT Targeting Researchers
- **Description**: A Python-based remote access trojan hidden inside weaponized proof-of-concept exploit repositories on GitHub, targeting vulnerability researchers who execute PoC code.
- **Impact**: Command execution, data exfiltration, and persistent access on researcher systems—potentially compromising undisclosed vulnerability research.
- **Status**: Active campaign with multiple trojanized PoC repositories identified on GitHub.
- **CVE ID**: [CVE ID not provided in source articles]

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: Versions vulnerable to CVE-2025-5777 (Citrix Bleed 2). Exploited by Anubis ransomware for initial access.
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-45659 RCE vulnerability. Actively exploited; added to CISA KEV.
- **Cisco Unified Communications Manager (Unified CM)**: Versions prior to June 2026 patch. Actively exploited per Cisco confirmation.
- **Fortinet FortiGate Firewalls**: Devices targeted in FortiBleed credential-theft campaign. Stolen credentials linked to INC and Lynx ransomware operations.
- **Nextcloud**: Zero-day vulnerability exploited by FortiBleed actors alongside Fortinet targeting.
- **Langflow AI Framework**: Versions vulnerable to RCE exploited by JADEPUFFER AI agent for automated ransomware.
- **macOS Systems**: Targeted by PamStealer via fake Maccy clipboard manager download sites. PAM mechanism abused for credential theft.
- **Microsoft 365 / Entra ID**: Tenants targeted by ClickFix and ConsentFix OAuth token theft attacks. MFA bypass via malicious consent prompts.
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat's Umbrij malware via OAuth API abuse for persistent email access.
- **Vulnerability Researcher Environments**: Systems compromised via ChocoPoC RAT in trojanized PoC exploits on GitHub (Python-based).
- **NetNut Residential Proxy Network**: Two million home devices compromised into proxy botnet (Popa botnet). Infrastructure seized by FBI with Google/Lumen assistance.
- **Kubota North America Network Systems**: Intrusion with month-long undetected access (early 2026). Initial vector unspecified.
- **Medtronic Systems**: Data breach by ShinyHunters exposing customer personal data. Vector unspecified.

## Attack Vectors and Techniques

- **Vulnerability Exploitation for Initial Access**: Ransomware groups (Anubis) leveraging CVE-2025-5777 (Citrix Bleed 2) and FortiBleed actors exploiting Fortinet/Nextcloud flaws for network entry.
- **AI-Automated Attack Chains**: JADEPUFFER AI agent autonomously exploiting Langflow RCE, conducting reconnaissance, and deploying database ransomware without human operators.
- **OAuth Token Theft and Consent Phishing**: ClickFix/ConsentFix attacks using fake verification prompts to trick users into authorizing malicious OAuth apps, stealing M365 tokens in seconds and bypassing MFA.
- **OAuth API Abuse for Persistent Email Access**: ToddyCat's Umbrij malware leveraging legitimate Google OAuth flows to maintain surreptitious Gmail/Google Workspace access.
- **Credential Theft and Reuse at Scale**: FortiBleed campaign harvesting thousands of Fortinet VPN/admin credentials, directly fueling INC and Lynx ransomware operations.
- **Trojanized Proof-of-Concept Exploits**: ChocoPoC RAT embedded in fake PoC code on GitHub, targeting vulnerability researchers who download and execute exploit code.
- **Typosquatting and Brand Impersonation**: PamStealer distributed via fake Maccy clipboard manager websites mimicking legitimate software downloads.
- **PAM (Pluggable Authentication Modules) Abuse**: macOS malware hooking into authentication subsystem to capture plaintext login credentials during user login.
- **Residential Proxy Botnet Infrastructure**: NetNut/Popa botnet compromising 2M+ home devices into rented relay network for threat actor anonymity and credential stuffing.
- **OS-Adaptive Phishing Payloads**: Campaigns fingerprinting victims via User-Agent strings to deliver platform-specific malware (Windows/macOS/Linux/mobile).
- **Social Engineering with Authority Impersonation**: Ransomware campaigns masquerading as Interpol/law enforcement to target small businesses globally.
- **Supply Chain Credential Compromise**: Ransomware groups using stolen supply chain credentials for initial access alongside vulnerability exploitation.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware operators loading signed but vulnerable drivers to disable security tools and escalate privileges.
- **AI Compute Hijacking**: Attackers targeting AI/ML infrastructure for unauthorized compute resource consumption (referenced in ThreatsDay).

## Threat Actor Activities

- **Anubis Ransomware**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access. Employing BYOVD techniques and supply chain credentials. Tactics vary between affiliates.
- **INC Ransomware**: Collaborating with FortiBleed actors to monetize stolen Fortinet credentials. Conducting follow-on intrusions using harvested VPN/admin access.
- **Lynx Ransomware**: Partnered with INC and FortiBleed actors. Using stolen Fortinet credentials to fuel network intrusions and ransomware deployment.
- **FortiBleed Actors**: Financially motivated credential theft campaign targeting thousands of Fortinet firewalls. Now monetizing access via INC/Lynx collaboration. Also exploiting Nextcloud zero-day.
- **ToddyCat (APT)**: Chinese-aligned threat actor deploying new Umbrij malware for OAuth-based Gmail/Google Workspace espionage. Long-term access to email correspondence.
- **JADEPUFFER (AI Agent Operator)**: Operator of first-known fully autonomous AI agent ransomware attack. Leveraged Langflow RCE for automated database encryption campaign.
- **Scattered Spider (UNC3944/0ktapus)**: Social engineering-focused group. Alleged member (dual US-Estonian citizen) extradited to US to face charges for membership in the collective.
- **ShinyHunters**: Data extortion group behind Medtronic breach. Exfiltrated customer personal data for notification-required disclosure.
- **Popa Botnet / NetNut Operators**: Ran residential proxy service spanning 2M+ compromised home devices. Infrastructure seized by FBI with Google, Lumen, and industry partners.
- **BlueHammer Ransomware**: Referenced in ThreatsDay roundup as active threat. Specific campaigns not detailed in source articles.
- **ChocoPoC Operators**: Targeting vulnerability researchers via trojanized PoC exploits on GitHub. Python-based RAT for command execution and data theft.
- **PamStealer Operators**: Distributing macOS info-stealer via fake Maccy sites. Novel PAM abuse for credential capture. Attribution unknown.
- **ClickFix/ConsentFix Operators**: Conducting M365 token theft via OAuth consent phishing. Sub-3-second account compromise. Attribution unknown.
- **Interpol-Impersonating Ransomware Group**: Multi-region campaign (US, Europe, Middle East) using law enforcement lures against small businesses. Basic but effective social engineering.

## Source Attribution

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
- **Medtronic notifies customers impacted by ShinyHunters data breach**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/
- **FortiBleed credential-theft campaign linked to Lynx ransomware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fortibleed-credential-theft-campaign-linked-to-lynx-ransomware/
- **Kubota says hackers had month-long access to network systems**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/kubota-says-hackers-had-month-long-access-to-network-systems/
- **Crafty Phishing Campaigns Auto-Adapt to Victim's Device, OS**: Dark Reading - https://www.darkreading.com/application-security/phishing-campaigns-auto-adapt-victims-device-os
- **New ChocoPoC malware targets researchers via trojanized PoC exploits**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-chocopoc-malware-targets-researchers-via-trojanized-poc-exploits/
