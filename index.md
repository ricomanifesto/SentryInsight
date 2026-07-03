# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with ransomware operations rapidly weaponizing recently disclosed flaws. The Citrix Bleed 2 vulnerability (CVE-2025-5777) is being leveraged by Anubis ransomware for initial access, while Microsoft SharePoint Server faces active exploitation of a remote code execution flaw (CVE-2026-45659) that CISA has added to its Known Exploited Vulnerabilities catalog. Simultaneously, the FortiBleed campaign has compromised thousands of Fortinet firewalls for credential harvesting, with stolen access now being monetized through collaboration with INC and Lynx ransomware gangs.

Social engineering techniques have evolved into the dominant malware delivery vector, with ClickFix and ConsentFix attacks hijacking Microsoft 365 accounts in seconds through OAuth flow manipulation. Threat actors are also weaponizing AI agents to automate end-to-end ransomware operations, as demonstrated by the JADEPUFFER operator exploiting a Langflow RCE for automated database encryption. Supply chain targeting has expanded to include vulnerability researchers themselves, with the ChocoPoC RAT distributed through trojanized proof-of-concept repositories on GitHub.

Law enforcement actions have disrupted significant criminal infrastructure, including the FBI seizure of the NetNut residential proxy platform spanning two million home devices and the extradition of an alleged Scattered Spider member. Meanwhile, advanced persistent threat group ToddyCat has deployed new Umbrij malware that abuses OAuth tokens to access Gmail via Google APIs, demonstrating continued innovation in cloud identity exploitation.

## Active Exploitation Details

### Citrix Bleed 2 (CVE-2025-5777)
- **Description**: A critical vulnerability in Citrix NetScaler ADC and Gateway appliances that allows unauthenticated attackers to obtain active session tokens and achieve initial access to target networks.
- **Impact**: Attackers gain valid authenticated sessions without credentials, enabling lateral movement, data exfiltration, and ransomware deployment. Anubis ransomware operators are actively exploiting this for initial access.
- **Status**: Actively exploited in the wild by Anubis ransomware operation. Patches available from Citrix.
- **CVE ID**: CVE-2025-5777

### Microsoft SharePoint Server Remote Code Execution (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server patched in May 2026.
- **Impact**: Allows unauthenticated attackers to execute arbitrary code on affected SharePoint servers, leading to full server compromise, data theft, and potential domain escalation.
- **Status**: Actively exploited in the wild. Added to CISA Known Exploited Vulnerabilities (KEV) catalog on July 2026. Federal agencies required to patch by August 2026.
- **CVE ID**: CVE-2026-45659

### FortiBleed (Fortinet Firewall Credential Theft)
- **Description**: A large-scale credential theft campaign targeting Fortinet firewall appliances, resulting in verified stolen credentials from thousands of devices.
- **Impact**: Attackers obtain valid VPN and administrative credentials enabling persistent network access, lateral movement, and follow-on ransomware deployment by INC and Lynx operations.
- **Status**: Active credential harvesting campaign with confirmed collaboration between FortiBleed actors and INC/Lynx ransomware gangs. Actors also exploiting a Nextcloud zero-day vulnerability to expand access.
- **CVE ID**: [No specific CVE identified in source articles for the primary Fortinet vulnerability; Nextcloud zero-day referenced without CVE]

### Cisco Unified Communications Manager Flaw
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) patched in early June 2026.
- **Impact**: Exploitation allows attackers to compromise Unified CM infrastructure, potentially enabling call interception, voicemail access, and pivot points into corporate networks.
- **Status**: Cisco has confirmed active exploitation in the wild. Patches released in early June 2026.
- **CVE ID**: [CVE not specified in source article]

### Langflow Remote Code Execution
- **Description**: An RCE vulnerability in Langflow, a visual framework for building AI agents and RAG applications.
- **Impact**: Enables full server compromise. Notably exploited by an AI agent (designated JADEPUFFER by Sysdig) to automate the complete ransomware attack chain from initial access through database encryption.
- **Status**: Actively exploited in the first observed case of fully AI-agent-automated ransomware deployment.
- **CVE ID**: [CVE not specified in source article]

### ClickFix and ConsentFix (Microsoft 365 Token Theft)
- **Description**: Social engineering techniques using fake prompts and manipulated OAuth consent flows to steal Microsoft 365 access tokens, bypassing MFA in seconds.
- **Impact**: Complete account takeover without credential theft, granting access to Exchange, SharePoint, OneDrive, and Teams data. Now the dominant malware delivery mechanism.
- **Status**: Actively exploited at scale. Opera has deployed "Paste Protect" feature to mitigate browser-based ClickFix attacks.
- **CVE ID**: [Not a CVE-tracked vulnerability; technique-based exploitation]

### ToddyCat Umbrij Malware (OAuth Abuse)
- **Description**: New malware attributed to APT group ToddyCat that abuses OAuth tokens to access victim Gmail accounts via Google APIs.
- **Impact**: Surreptitious email surveillance, data exfiltration, and persistent access to Google Workspace environments without triggering traditional authentication alerts.
- **Status**: Active deployment by ToddyCat (Chinese-nexus APT). Targets email correspondence for intelligence collection.
- **CVE ID**: [Technique-based exploitation of OAuth design; no CVE]

### ChocoPoC RAT (Trojanized PoC Exploits)
- **Description**: Python-based remote access trojan hidden inside fake proof-of-concept exploit repositories on GitHub targeting vulnerability researchers.
- **Impact**: Command execution, data theft, and credential harvesting from security professionals' systems. Compromises the trust model of security research sharing.
- **Status**: Active campaign with multiple weaponized repositories identified on GitHub.
- **CVE ID**: [Supply chain / social engineering attack; no CVE for the malware itself]

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: Versions vulnerable to CVE-2025-5777 (Citrix Bleed 2); actively targeted by Anubis ransomware for initial access
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-45659 RCE; patched May 2026; added to CISA KEV with active exploitation confirmed
- **Fortinet FortiGate Firewalls**: Multiple models impacted by FortiBleed credential theft campaign; thousands of devices compromised for VPN/admin credentials
- **Cisco Unified Communications Manager (Unified CM)**: Versions patched in early June 2026; Cisco confirms active exploitation post-patch
- **Langflow AI Framework**: Visual RAG/agent building framework vulnerable to RCE; exploited by JADEPUFFER AI agent for automated ransomware
- **Microsoft 365 / Entra ID**: All tenants susceptible to ClickFix/ConsentFix OAuth token theft via social engineering; MFA bypass achieved in seconds
- **Google Workspace / Gmail**: Targeted by ToddyCat's Umbrij malware via OAuth token abuse for persistent email access
- **Nextcloud Instances**: Zero-day vulnerability exploited by FortiBleed actors as secondary access vector; CVE not yet assigned
- **Vulnerability Researcher Workstations**: Targeted via trojanized Python PoC exploits on GitHub delivering ChocoPoC RAT
- **Residential Devices (2M+)**: NetNut proxy platform compromised home routers and IoT devices for residential proxy botnet; seized by FBI/Google/Lumen

## Attack Vectors and Techniques

- **Citrix Bleed 2 Exploitation (CVE-2025-5777)**: Unauthenticated session token harvesting from NetScaler appliances for immediate authenticated access
- **SharePoint RCE Exploitation (CVE-2026-45659)**: Remote code execution on unpatched SharePoint servers for initial foothold and domain escalation
- **FortiBleed Credential Harvesting**: Large-scale scanning and exploitation of Fortinet appliances to steal valid VPN and admin credentials
- **Nextcloud Zero-Day Exploitation**: Undisclosed vulnerability in Nextcloud leveraged by FortiBleed actors for additional access vectors
- **Cisco Unified CM Exploitation**: Post-patch targeting of Unified Communications Manager for voice infrastructure compromise
- **Langflow RCE via AI Agent**: First documented case of autonomous AI agent (JADEPUFFER) executing full ransomware kill chain from exploit to encryption
- **ClickFix / ConsentFix OAuth Phishing**: Fake verification prompts and manipulated consent screens steal M365 tokens in ~3 seconds, bypassing MFA
- **Device-Adaptive Phishing**: User-agent fingerprinting delivers OS-specific payloads (Windows/macOS/Linux/mobile) for higher compromise rates
- **Interpol-Themed Social Engineering**: Ransomware lures impersonating law enforcement targeting SMBs across US, Europe, Middle East
- **OAuth Token Abuse (Umbrij)**: Stolen/phished OAuth tokens used via Google API for persistent, stealthy Gmail access without re-authentication
- **Trojanized PoC Supply Chain**: Weaponized proof-of-concept code on GitHub targets vulnerability researchers' trust in community exploits
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware groups loading signed vulnerable drivers to disable EDR and deploy payloads
- **Supply Chain Credential Theft**: Compromised vendor/service provider credentials used for downstream network intrusion
- **Residential Proxy Botnet (NetNut/Popa)**: 2M+ home devices converted to rental proxies for attack anonymization and credential stuffing

## Threat Actor Activities

- **Anubis Ransomware Operation**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access; employing BYOVD and supply chain credentials for lateral movement and deployment
- **INC Ransomware Gang**: Collaborating with FortiBleed actors to monetize stolen Fortinet credentials; follow-on intrusion and ransomware deployment
- **Lynx Ransomware Gang**: Partner in FortiBleed credential monetization; receiving verified firewall/VPN access for targeted intrusions
- **FortiBleed Actors**: Financially motivated group conducting mass Fortinet credential harvesting; now pivoting to ransomware partnerships and Nextcloud zero-day exploitation
- **ToddyCat (APT)**: Chinese-nexus advanced persistent threat deploying new Umbrij malware for OAuth-based Gmail surveillance via Google APIs
- **JADEPUFFER (AI Agent Operator)**: Threat actor utilizing autonomous AI agent to exploit Langflow RCE and execute complete ransomware attack without human intervention
- **Scattered Spider (UNC3944/0ktapus)**: Social engineering-focused group; alleged member extradited to US; known for MFA bypass, SIM swapping, and cloud identity attacks
- **ShinyHunters**: Data extortion group behind Medtronic breach; specializes in cloud misconfiguration exploitation and data theft for extortion
- **Popa Botnet Operators**: Ran NetNut residential proxy service spanning 2M+ compromised home devices; infrastructure seized by FBI with industry partners
- **ChocoPoC Campaign Operators**: Targeting vulnerability researchers via trojanized PoC exploits on GitHub; Python RAT for data theft and command execution
- **BlueHammer Ransomware**: Referenced in ThreatsDay roundup; specific targeting details not elaborated in source articles

## Source Attribution

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
- **And the Winner in Dominant Malware Delivery? ClickFix**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/winner-dominant-malware-delivery-clickfix
