# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with ransomware groups rapidly weaponizing recently disclosed vulnerabilities and novel attack techniques. The Citrix Bleed 2 vulnerability (CVE-2025-5777) is being exploited by Anubis ransomware operators for initial access, while Microsoft SharePoint Server faces active exploitation of a critical RCE flaw (CVE-2026-45659) that has been added to CISA's Known Exploited Vulnerabilities catalog. Simultaneously, Cisco has confirmed exploitation of a Unified Communications Manager vulnerability patched in early June, and FortiBleed actors have harvested credentials from thousands of Fortinet firewalls to fuel INC and Lynx ransomware operations.

A significant shift in attacker methodology is evident through the emergence of AI-driven exploitation, with the JADEPUFFER operator deploying an AI agent to automate end-to-end ransomware attacks via a Langflow RCE. Social engineering techniques continue to evolve, with ClickFix and ConsentFix campaigns hijacking Microsoft 365 tokens in seconds through OAuth abuse, while phishing campaigns now dynamically fingerprint victim devices to deliver OS-specific payloads. Supply chain targeting has expanded to include vulnerability researchers themselves, with the ChocoPoC RAT distributed through trojanized proof-of-concept exploits on GitHub.

Infrastructure takedowns demonstrate the scale of criminal proxy networks, as the FBI and Google disrupted the NetNut residential proxy platform spanning two million compromised home devices alongside the Popa botnet. Nation-state aligned actors remain active, with ToddyCat deploying the Umbrij malware to abuse OAuth tokens for Gmail access via Google APIs, and Scattered Spider members facing extradition. These developments underscore the convergence of automated exploitation, identity-focused attacks, and residential infrastructure abuse defining the current threat landscape.

## Active Exploitation Details

### Citrix Bleed 2 (CVE-2025-5777)
- **Description**: A critical vulnerability in Citrix NetScaler ADC and Gateway appliances that allows unauthenticated attackers to obtain active session tokens and bypass authentication mechanisms.
- **Impact**: Attackers gain initial access to internal networks without credentials, enabling lateral movement, data exfiltration, and ransomware deployment.
- **Status**: Actively exploited by Anubis ransomware operation; patches available from Citrix.
- **CVE ID**: CVE-2025-5777

### Microsoft SharePoint Server RCE (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server that allows authenticated attackers to execute arbitrary code on the server.
- **Impact**: Full server compromise leading to data theft, lateral movement, and potential domain controller compromise in on-premises environments.
- **Status**: Actively exploited in the wild; added to CISA KEV catalog on July 2026; patched in May 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that allows remote attackers to exploit the call processing infrastructure.
- **Impact**: Potential unauthorized access to voice/video communications, call metadata, and potential pivot points into corporate networks.
- **Status**: Cisco confirmed active exploitation; patch released in early June 2026.

### FortiBleed (Fortinet Firewall Credential Theft)
- **Description**: A large-scale credential theft campaign targeting Fortinet firewall appliances, resulting in verified stolen credentials from thousands of devices.
- **Impact**: Stolen VPN and administrative credentials enable follow-on network intrusions, lateral movement, and ransomware deployment by INC and Lynx operations.
- **Status**: Credentials actively monetized; linked to INC and Lynx ransomware gangs; Fortinet has issued advisories.

### Nextcloud Zero-Day
- **Description**: An undisclosed zero-day vulnerability in Nextcloud collaboration platform being exploited by FortiBleed actors.
- **Impact**: Potential unauthorized access to file shares, user data, and administrative interfaces.
- **Status**: Actively exploited in conjunction with Fortinet credential theft; patch status unclear from available reporting.

### Langflow RCE
- **Description**: A remote code execution vulnerability in Langflow, a low-code AI application builder, exploited by an AI agent to automate ransomware attacks.
- **Impact**: Automated database ransomware deployment without human operator intervention; represents first observed AI-agent-driven end-to-end ransomware attack.
- **Status**: Exploited by JADEPUFFER operator; Sysdig Threat Research Team identified the campaign.

### Apple Email Flaw
- **Description**: A vulnerability in Apple's email infrastructure or client that enables exploitation.
- **Impact**: Potential email compromise, data access, or further attack chaining.
- **Status**: Referenced in ThreatsDay roundup as an active weak spot; specific details limited in available reporting.

### PamStealer (macOS Information Stealer)
- **Description**: A new macOS malware that uses fake Maccy clipboard manager websites and PAM (Pluggable Authentication Module) checks to steal user login passwords.
- **Impact**: Theft of macOS login credentials, potential keychain access, and sensitive data exfiltration.
- **Status**: Active distribution via typosquatting/fake download sites; no patch required (user awareness and endpoint detection).

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: Versions vulnerable to CVE-2025-5777 (Citrix Bleed 2); appliances exposed to internet for remote access.
- **Microsoft SharePoint Server**: On-premises SharePoint Server versions patched in May 2026; not affecting SharePoint Online.
- **Cisco Unified Communications Manager**: Versions prior to early June 2026 security patch; enterprise voice/video infrastructure.
- **Fortinet FortiGate Firewalls**: Multiple models and firmware versions targeted for credential harvesting; VPN and admin interfaces exposed.
- **Nextcloud**: Self-hosted collaboration platform instances; version specifics not disclosed in reporting.
- **Langflow**: AI application builder framework; versions vulnerable to RCE exploited by JADEPUFFER.
- **Apple Email Infrastructure/Clients**: macOS and iOS mail ecosystem; specific components not detailed.
- **Microsoft 365 / Entra ID**: Tenants targeted by ClickFix and ConsentFix OAuth abuse campaigns; all license tiers potentially affected.
- **Google Workspace / Gmail**: Accounts targeted by Umbrij malware via OAuth token abuse; Google API access scopes exploited.
- **macOS Systems**: Users downloading clipboard managers from unverified sources; specifically targeting Maccy users via typosquatting.
- **NetNut Residential Proxy Nodes**: Over 2 million home routers and IoT devices unwittingly enrolled as proxy exit nodes.
- **GitHub / Developer Workstations**: Vulnerability researchers cloning and executing trojanized PoC exploits; Python environments compromised by ChocoPoC RAT.
- **Kubota North America Corporation**: Network systems accessed for over one month; specific entry vector not disclosed.
- **Medtronic**: Healthcare device firm systems breached by ShinyHunters; customer personal data exposed.

## Attack Vectors and Techniques

- **Citrix Bleed 2 Exploitation**: Unauthenticated session token harvesting via CVE-2025-5777; used for initial access by Anubis ransomware.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Attackers loading signed but vulnerable kernel drivers to disable security tools and elevate privileges; employed by ransomware groups alongside Citrix exploitation.
- **Supply Chain Credential Theft**: Compromise of third-party/vendor credentials to access target environments; used in conjunction with direct vulnerability exploitation.
- **ClickFix / ConsentFix OAuth Abuse**: Fake authentication prompts and malicious OAuth applications trick users into granting consent, stealing Microsoft 365 tokens in seconds and bypassing MFA.
- **OAuth Token Abuse (Umbrij)**: Malware steals OAuth refresh/access tokens to access Gmail via Google APIs without triggering security alerts; persists across password changes.
- **AI-Agent Automated Exploitation (JADEPUFFER)**: Autonomous AI agent discovers, exploits Langflow RCE, and deploys database ransomware without human intervention; novel fully automated attack chain.
- **Device/OS Fingerprinting Phishing**: Attackers analyze User-Agent headers and client hints to deliver OS-specific payloads (Windows vs. macOS vs. mobile) automatically; increases compromise rates.
- **Trojanized PoC Exploits (ChocoPoC)**: Weaponized proof-of-concept code uploaded to GitHub targeting vulnerability researchers; Python-based RAT executes commands and exfiltrates data when researchers run the "exploit."
- **Typosquatting / Fake Software Sites (PamStealer)**: Clone sites mimicking legitimate open-source tool (Maccy) distribute malware; PAM authentication prompts harvest macOS login passwords.
- **Social Engineering / Impersonation (Interpol Lure)**: Ransomware campaigns masquerading as law enforcement (Interpol) to pressure small businesses into engagement; multi-region deployment.
- **Residential Proxy Botnet (NetNut / Popa)**: Compromised home devices (routers, IoT) enrolled as exit nodes for criminal traffic anonymization; 2M+ device scale.
- **Fortinet Credential Harvesting (FortiBleed)**: Large-scale scanning and exploitation of FortiGate appliances to extract VPN and admin credentials; credentials validated and sold/used for ransomware access.
- **Nextcloud Zero-Day Exploitation**: Undisclosed vulnerability chained with FortiBleed access for deeper compromise; details withheld.

## Threat Actor Activities

- **Anubis Ransomware**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access; employing BYOVD techniques; differing tactics across affiliates but consistent vulnerability exploitation.
- **INC Ransomware**: Collaborating with FortiBleed actors; consuming stolen Fortinet credentials for network intrusion and ransomware deployment; financially motivated.
- **Lynx Ransomware**: Partnered with INC in FortiBleed credential monetization; using verified stolen credentials for follow-on attacks; active ransomware-as-a-service operation.
- **FortiBleed Actors**: Initial access brokers specializing in Fortinet firewall credential harvesting; scaled operation hitting thousands of devices; now monetizing access through ransomware partnerships.
- **ToddyCat (APT)**: Chinese-aligned threat actor deploying Umbrij malware; targeting email intelligence collection via OAuth abuse against Google Workspace/Gmail; long-term espionage focus.
- **JADEPUFFER**: Novel AI-agent operator (identified by Sysdig); deployed autonomous agent to exploit Langflow RCE and execute database ransomware; first observed fully AI-driven ransomware campaign.
- **Scattered Spider (UNC3944 / 0ktapus)**: Social engineering and SIM-swapping specialists; alleged member extradited to US from Estonia; targets telecommunications, BPO, and large enterprises for data theft and extortion.
- **ShinyHunters**: Data breach actor; compromised Medtronic customer data; focuses on data theft and extortion rather than ransomware encryption.
- **ChocoPoC Operators**: Targeting vulnerability researchers via GitHub; supply chain attack on security community; Python RAT capabilities include command execution and data theft.
- **PamStealer Operators**: New macOS-focused threat actor; distribution via SEO poisoning/typosquatting; credential theft focus; attribution unknown.
- **NetNut / Popa Botnet Operators**: Residential proxy service operators; knowingly enrolled compromised home devices; infrastructure seized by FBI with Google/Lumen cooperation.
- **Interpol Impersonation Ransomware Group**: Opportunistic ransomware campaign using law enforcement lures; broad geographic targeting (US, Europe, Middle East); low sophistication, high volume.

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
