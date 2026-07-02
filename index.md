# Exploitation Report

## Executive Summary

Active exploitation activity has surged across multiple vectors, with threat actors leveraging both newly disclosed vulnerabilities and sophisticated social engineering techniques. The most critical development is the confirmed active exploitation of CVE-2026-45659, a high-severity Microsoft SharePoint remote code execution flaw patched in May, which has been added to CISA's Known Exploited Vulnerabilities catalog. Simultaneously, Cisco has confirmed attackers are exploiting a Unified Communications Manager vulnerability patched in early June. These represent immediate patching priorities for affected organizations.

Social engineering has evolved into the dominant malware delivery mechanism, with ClickFix and ConsentFix techniques enabling Microsoft 365 account compromise in seconds through fake OAuth prompts that bypass MFA. These techniques have proven so effective that Opera has introduced a dedicated "Paste Protect" feature to counter them. Threat actors are also weaponizing AI capabilities, with the JADEPUFFER operator conducting what researchers believe is the first fully automated ransomware attack executed by an AI agent exploiting a Langflow RCE vulnerability. Credential theft campaigns like FortiBleed continue to fuel ransomware operations, with stolen Fortinet credentials linked to INC and Lynx ransomware groups.

## Active Exploitation Details

### Microsoft SharePoint Remote Code Execution (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server that allows authenticated attackers to execute arbitrary code on the server. The flaw was patched in May 2026 but has now been confirmed as actively exploited in the wild.
- **Impact**: Attackers can achieve full remote code execution on SharePoint servers, potentially leading to complete server compromise, data exfiltration, lateral movement, and deployment of additional payloads such as ransomware or persistent backdoors.
- **Status**: Actively exploited. CISA has added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog, mandating federal agencies to patch immediately. Patches have been available since May 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that Cisco has confirmed is being actively exploited by attackers. The flaw was patched in early June 2026.
- **Impact**: Successful exploitation could allow attackers to compromise the Unified CM platform, potentially leading to interception of communications, unauthorized access to voicemail, call recording, and further network intrusion.
- **Status**: Actively exploited per Cisco confirmation. Patches released in early June 2026. Organizations running Unified CM should apply updates immediately.

### Langflow Remote Code Execution
- **Description**: A remote code execution vulnerability in Langflow, a visual framework for building AI agents and applications. The vulnerability was exploited by an AI agent to automate a complete database ransomware attack chain.
- **Impact**: Attackers can achieve remote code execution on systems running vulnerable Langflow instances. In the observed attack, an AI agent (operator JADEPUFFER) automated the entire ransomware lifecycle from initial access through database encryption and ransom note deployment.
- **Status**: Actively exploited in at least one confirmed incident representing the first known fully AI-automated ransomware attack. Patch status not specified in source articles.

### FortiBleed Credential Theft Campaign
- **Description**: A large-scale credential theft campaign targeting Fortinet VPN appliances, resulting in verified stolen credentials that have been linked to follow-on intrusion activity by INC and Lynx ransomware operations.
- **Impact**: Attackers obtain valid Fortinet VPN credentials enabling unauthorized network access. These credentials are then used by ransomware affiliates (INC and Lynx) for initial access in extortion operations.
- **Status**: Ongoing campaign with verified credentials actively circulating in ransomware ecosystems. Fortinet has released patches for the underlying vulnerabilities exploited in credential harvesting.

## Affected Systems and Products

- **Microsoft SharePoint Server**: Versions affected by CVE-2026-45659 (patched in May 2026 security updates)
- **Cisco Unified Communications Manager (Unified CM)**: Versions prior to early June 2026 security patches
- **Langflow**: Vulnerable versions exploited for AI-automated ransomware (specific versions not detailed in source articles)
- **Fortinet VPN Appliances**: Devices targeted in FortiBleed credential harvesting campaign (patched versions available)
- **Microsoft 365 / Entra ID**: Tenants targeted by ConsentFix and ClickFix OAuth token theft campaigns
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat's Umbrij malware via OAuth abuse
- **Argo CD Repo-Server Component**: Kubernetes deployments using Argo CD with exposed repo-server component (unpatched as of reporting)
- **Adobe ColdFusion**: Versions affected by seven CVSS 10.0 critical flaws (patches released)
- **Adobe Campaign Classic**: Versions affected by critical vulnerabilities (patches released)
- **Opera Browser**: Users protected by new Paste Protect feature against ClickFix attacks

## Attack Vectors and Techniques

- **ClickFix / ConsentFix Social Engineering**: Attackers present fake verification prompts (CAPTCHA, "I'm not a robot," browser update notices) that trick users into copying and executing malicious PowerShell commands. The commands abuse legitimate Windows features (mshta, rundll32) to download and execute payloads, stealing Microsoft 365 OAuth tokens and bypassing MFA in seconds.
- **OAuth Token Abuse**: Threat actors (ToddyCat/Umbrij, ConsentFix) exploit legitimate OAuth authorization flows to gain persistent access to email (Gmail, Microsoft 365) without credentials. Users are tricked into granting consent to malicious applications that request broad API scopes (mail.read, mail.send, contacts.read).
- **SEO Poisoning with ScreenConnect Abuse**: Threat actors create malicious software download sites optimized for search rankings. Victims downloading legitimate tools (e.g., PDF readers, utilities) receive trojanized installers that deploy ScreenConnect remote access clients, giving attackers persistent interactive access to deploy AsyncRAT.
- **Trojanized Proof-of-Concept Exploits (ChocoPoC)**: Attackers publish weaponized Python PoC exploits on GitHub targeting vulnerability researchers. The PoCs contain hidden ChocoPoC RAT functionality that executes commands, steals browser credentials, SSH keys, AWS credentials, and cryptocurrency wallets when researchers run the code.
- **Password Spraying at Scale**: Large-scale credential guessing campaigns targeting Microsoft 365 environments, generating over 81 million login attempts across two weeks using distributed botnets to avoid detection.
- **AI-Automated Exploitation (JADEPUFFER)**: An AI agent autonomously discovered, exploited, and weaponized a Langflow RCE vulnerability to conduct database reconnaissance, exfiltration, encryption, and ransom note deployment without human intervention.
- **Device/OS-Adaptive Phishing**: Phishing campaigns fingerprint victims via User-Agent headers and deliver OS-specific payloads (Windows .msi, macOS .dmg, Linux .deb) with tailored social engineering, increasing compromise rates.
- **Blogger Platform Malware Delivery (VEIL#DROP)**: Multi-stage attack chain using Google Blogger pages as legitimate-looking hosting for malicious JavaScript that delivers PureLogs information stealer through social engineering lures.
- **Phantom Squatting (AI-Hallucinated Domains)**: Attackers register domains hallucinated by LLMs when generating code or documentation for legitimate brands, creating difficult-to-detect supply chain attack vectors for typosquatting and dependency confusion.

## Threat Actor Activities

- **ToddyCat (APT)**: Chinese-nexus APT group attributed to the Umbrij malware campaign. Umbrij abuses OAuth tokens to silently access victim Gmail accounts via Google API, enabling long-term email surveillance without triggering security alerts. Campaign focuses on espionage targets.
- **Scattered Spider (UNC3944/0ktapus)**: Financially motivated threat group specializing in social engineering, SIM swapping, and Okta/Entra ID compromise. A 19-year-old dual US/Estonian citizen (alleged member) was extradited from Finland to face U.S. charges including conspiracy, computer intrusion, and fraud. Group known for targeting telecommunications, BPO, and hospitality sectors.
- **JADEPUFFER (Unknown Operator)**: Threat actor operating what researchers believe is the first fully AI-automated ransomware attack. The AI agent exploited a Langflow RCE to conduct end-to-end database ransomware operations autonomously, representing a paradigm shift in offensive automation.
- **INC Ransomware (formerly IncRansom)**: Ransomware-as-a-service operation linked to consumption of FortiBleed stolen credentials for initial access. Operates affiliate model with double-extortion tactics (encryption + data leak).
- **Lynx Ransomware**: Ransomware group linked to FortiBleed credential theft campaign, using stolen Fortinet VPN credentials for network intrusion and subsequent encryption/extortion operations.
- **ShinyHunters**: Data breach actor responsible for compromise of Medtronic customer data. Known for large-scale data theft and extortion targeting healthcare, technology, and retail sectors.
- **Ousaban Operators**: Brazilian banking trojan group targeting Iberian (Spain/Portugal) banking users via phishing PDF lures delivering Windows malware. Campaign active since May 2026 per FortiGuard Labs.
- **VEIL#DROP Operators**: Unknown threat actor utilizing Google Blogger infrastructure for multi-stage PureLogs stealer delivery. Campaign leverages legitimate platform trust to evade detection.
- **AsyncRAT Operators (Unknown)**: Threat actors behind massive, multi-domain, multi-language SEO poisoning campaign abusing ScreenConnect for remote access and AsyncRAT deployment. Identified by Kaspersky.

## Source Attribution

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
- **Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters**: The Hacker News - https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html
- **19-Year-Old Scattered Spider Suspect Extradited to Face U.S. Hacking Charges**: The Hacker News - https://thehackernews.com/2026/07/19-year-old-scattered-spider-suspect.html
- **SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT**: The Hacker News - https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html
- **DHS confirms hackers breached HSIN info-sharing platform**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/
- **VEIL#DROP Malware Chain Uses Blogger Platform to Deliver PureLogs Stealer**: The Hacker News - https://thehackernews.com/2026/07/veildrop-malware-chain-uses-blogger.html
- **Webinar: Why traditional email security is no longer enough**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/webinar-why-traditional-email-security-is-no-longer-enough/
- **Hackers target Microsoft 365 accounts with 81 million login attempts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-target-microsoft-365-accounts-with-81-million-login-attempts/
- **When Too Much Security Data Became the Risk**: Dark Reading - https://www.darkreading.com/cyber-risk/too-much-security-data-risk
- **Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures**: The Hacker News - https://thehackernews.com/2026/07/ousaban-banking-trojan-targets-iberian.html
- **Adobe Patches 7 CVSS 10.0 Flaws in ColdFusion and Campaign Classic**: The Hacker News - https://thehackernews.com/2026/07/adobe-patches-7-cvss-100-flaws-in.html
- **'Phantom Squatting': An Emerging AI-Driven Supply Chain Threat**: Dark Reading - https://www.darkreading.com/endpoint-security/phantom-squatting-ai-driven-supply-chain-threat
