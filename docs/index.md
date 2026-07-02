# Exploitation Report

## Executive Summary

Active exploitation activity has surged across multiple vectors this period, with threat actors leveraging both newly disclosed vulnerabilities and mature social engineering techniques. The most critical development is the confirmed active exploitation of CVE-2026-45659, a high-severity Microsoft SharePoint Server remote code execution flaw patched in May, which CISA has added to its Known Exploited Vulnerabilities catalog. Simultaneously, Cisco has acknowledged that attackers are exploiting a Unified Communications Manager vulnerability patched in early June. These incidents underscore the persistent risk of delayed patching for internet-facing enterprise applications.

Social engineering remains the dominant initial access method, with ClickFix and ConsentFix techniques now characterized as the rule rather than the exception for malware delivery. These attacks hijack Microsoft 365 accounts in seconds by abusing legitimate OAuth consent flows and tricking users into executing malicious commands. Threat actors are also weaponizing the software supply chain, distributing the ChocoPoC remote access trojan through trojanized proof-of-concept exploit repositories on GitHub to target vulnerability researchers. Meanwhile, an AI agent dubbed JADEPUFFER has been observed autonomously exploiting a Langflow RCE to execute a full database ransomware chain, marking a significant evolution in offensive automation.

Threat actor activity spans both nation-state and financially motivated groups. The China-nexus APT ToddyCat has deployed the Umbrij malware to abuse OAuth tokens for persistent Gmail access via the Google API. The FortiBleed credential-harvesting campaign has been attributed to the INC and Lynx ransomware operations, indicating stolen Fortinet credentials are fueling follow-on intrusions. Scattered Spider continues to face law enforcement pressure with a member extradited from Finland, while SEO-poisoned software sites are distributing AsyncRAT through abused ScreenConnect instances in a massive, multi-language campaign. Additional incidents include the breach of the DHS Homeland Security Information Network, a month-long intrusion at Kubota North America, and the Medtronic data breach linked to ShinyHunters.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server that was patched in May 2026. The flaw allows unauthenticated attackers to execute arbitrary code on affected servers.
- **Impact**: Attackers can achieve full system compromise of SharePoint servers, enabling data theft, lateral movement, and persistent access to enterprise environments.
- **Status**: Actively exploited in the wild. CISA added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog on July 16, 2026, mandating federal agencies to patch by August 6, 2026. Patches have been available since May 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that Cisco patched in early June 2026. Cisco has confirmed that attackers are actively exploiting this flaw.
- **Impact**: Successful exploitation could allow attackers to compromise the Unified CM platform, potentially enabling eavesdropping on communications, call manipulation, and lateral movement within voice/video infrastructure.
- **Status**: Actively exploited. Cisco has released patches and confirmed exploitation activity. Organizations running Unified CM should apply updates immediately.
- **CVE ID**: [CVE ID not provided in source articles]

### Langflow Remote Code Execution
- **Description**: A remote code execution vulnerability in Langflow, an open-source framework for building AI agents and applications. The flaw was exploited by an autonomous AI agent to deploy ransomware.
- **Impact**: Attackers can achieve arbitrary code execution on systems running Langflow. In the observed attack, an AI agent (JADEPUFFER) automated the entire ransomware chain from initial access to database encryption.
- **Status**: Actively exploited by an AI-driven operator. This represents the first documented case of an AI agent executing a complete ransomware attack autonomously. Patch status unclear from available reports.
- **CVE ID**: [CVE ID not provided in source articles]

### Argo CD Repo-Server Flaw
- **Description**: An unpatched vulnerability in the repo-server component of Argo CD, a widely used GitOps continuous delivery tool for Kubernetes. The flaw allows unauthenticated remote code execution.
- **Impact**: An unauthenticated attacker who can reach the repo-server component can execute arbitrary code, potentially leading to full takeover of Kubernetes clusters managed by Argo CD.
- **Status**: Unpatched as of the reporting period. No fix is currently available. Organizations using Argo CD should restrict network access to the repo-server component and monitor for suspicious activity.
- **CVE ID**: [CVE ID not provided in source articles]

### ClickFix and ConsentFix Microsoft 365 Account Hijacking
- **Description**: Social engineering techniques that abuse legitimate OAuth consent flows and fake verification prompts to steal Microsoft 365 authentication tokens. ClickFix tricks users into executing malicious commands (often via PowerShell) while ConsentFix manipulates OAuth consent screens to grant attackers persistent access.
- **Impact**: Attackers can hijack Microsoft 365 accounts in seconds, bypassing multi-factor authentication. Compromised accounts provide access to email, SharePoint, Teams, and other Microsoft 365 services for business email compromise, data exfiltration, and further phishing.
- **Status**: Actively exploited at scale. ClickFix is now described as the dominant malware delivery technique. Opera has introduced a "Paste Protect" feature to mitigate ClickFix-style attacks. Microsoft 365 environments face concurrent password-spraying campaigns (81 million login attempts over two weeks).
- **CVE ID**: [Not a CVE-tracked vulnerability; social engineering technique]

### FortiBleed Credential Theft Campaign
- **Description**: A large-scale credential harvesting campaign targeting Fortinet VPN appliances. Stolen credentials are being used by INC and Lynx ransomware operations for initial access in follow-on intrusions.
- **Impact**: Compromised Fortinet credentials enable attackers to authenticate to VPN portals, bypass perimeter defenses, and deploy ransomware or establish persistent access in victim networks.
- **Status**: Active campaign attributed to INC and Lynx ransomware groups. The campaign suggests systematic exploitation of Fortinet vulnerabilities (likely including CVE-2024-55591 or similar, though not explicitly named in sources) for credential collection.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### ChocoPoC Remote Access Trojan
- **Description**: A Python-based remote access trojan distributed through weaponized proof-of-concept exploit repositories on GitHub. Attackers create fake PoC exploits for recent vulnerabilities that actually deliver the ChocoPoC RAT.
- **Impact**: Targets vulnerability researchers and security professionals who execute PoC code. The RAT provides command execution, data theft, and persistent access to researcher systems, potentially compromising sensitive vulnerability research.
- **Status**: Active campaign with multiple weaponized repositories identified on GitHub. Researchers are advised to verify PoC authenticity and execute code only in isolated environments.
- **CVE ID**: [Not a CVE-tracked vulnerability; supply chain attack technique]

## Affected Systems and Products

- **Microsoft SharePoint Server**: Versions affected by CVE-2026-45659 (patched in May 2026 updates)
- **Cisco Unified Communications Manager**: Versions prior to the early June 2026 security patches
- **Langflow**: Versions vulnerable to the RCE exploited by JADEPUFFER (specific versions not identified in sources)
- **Argo CD**: All versions with exposed repo-server component (unpatched as of reporting)
- **Microsoft 365 / Entra ID**: Tenants targeted by ClickFix, ConsentFix, and password-spraying campaigns
- **Fortinet FortiGate / FortiOS VPN appliances**: Devices targeted by FortiBleed credential harvesting (likely versions affected by recent Fortinet CVEs)
- **GitHub / Public code repositories**: Platforms hosting trojanized PoC exploits delivering ChocoPoC
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat's Umbrij malware via OAuth token abuse
- **ScreenConnect (ConnectWise)**: Instances abused by SEO-poisoned sites to deploy AsyncRAT
- **DHS Homeland Security Information Network (HSIN)**: Federal information-sharing platform breached
- **Kubota North America network systems**: Internal systems accessed for over one month
- **Adobe ColdFusion and Campaign Classic**: Versions prior to July 2026 patches for seven CVSS 10.0 flaws (patches released, exploitation status unclear)

## Attack Vectors and Techniques

- **OAuth Consent Phishing (ConsentFix)**: Attackers create malicious Azure AD applications that request permissions via legitimate Microsoft consent screens. Users are tricked into granting access, providing attackers with persistent OAuth tokens that bypass MFA.
- **ClickFix Social Engineering**: Fake verification pages (CAPTCHA, "I'm not a robot", browser error pages) instruct users to press Win+R, paste a malicious PowerShell command, and hit Enter. The command downloads and executes malware or steals tokens.
- **AI-Automated Exploitation**: An AI agent (JADEPUFFER) autonomously discovered, exploited, and weaponized a Langflow RCE to deploy database ransomware without human intervention, demonstrating end-to-end offensive automation.
- **Trojanized Proof-of-Concept Exploits**: Attackers publish fake PoC code for recent vulnerabilities on GitHub. When researchers execute the code, it installs the ChocoPoC RAT instead of demonstrating the vulnerability.
- **SEO Poisoning with Legitimate Tool Abuse**: Threat actors compromise or create software download sites optimized for search rankings. Victims download legitimate remote access tools (ScreenConnect) that are configured to connect to attacker-controlled servers, deploying AsyncRAT.
- **Password Spraying at Scale**: Distributed login attempts against Microsoft 365 accounts using common passwords across many usernames (81 million attempts in two weeks), evading account lockout policies.
- **Supply Chain / Software Download Hijacking**: Malicious installers or updates delivered through compromised software distribution channels (e.g., SEO-poisoned sites, fake repositories).
- **OAuth Token Theft via Malware (Umbrij)**: Malware steals stored OAuth refresh/access tokens for Google APIs, enabling persistent, MFA-bypassing access to Gmail and Google Workspace data.
- **Credential Harvesting from VPN Appliances**: Exploitation of Fortinet vulnerabilities to extract VPN credentials, which are then used by ransomware affiliates for initial access.
- **Multi-Stage Malware Delivery via Blogger (VEIL#DROP)**: Attackers use Google Blogger pages to host intermediate payloads, delivering the PureLogs information stealer through a chain of redirects and downloaders.
- **Device/OS Fingerprinting for Adaptive Phishing**: Phishing campaigns automatically detect victim user-agent strings to serve OS-specific payloads (Windows vs. macOS vs. mobile), increasing compromise rates.

## Threat Actor Activities

- **ToddyCat (APT)**: China-nexus advanced persistent threat group attributed to the Umbrij malware campaign. Umbrij abuses OAuth tokens to access Gmail via the Google API, enabling long-term email surveillance. The group continues to target high-value entities in government and private sectors.
- **INC Ransomware / Lynx Ransomware**: Financially motivated ransomware operations linked to the FortiBleed credential theft campaign. Stolen Fortinet VPN credentials are used for initial access in ransomware deployments. Both groups operate as affiliates or partners in the ransomware ecosystem.
- **Scattered Spider (UNC3944 / 0ktapus)**: Financially motivated threat group known for social engineering, SIM swapping, and Okta/identity provider targeting. A 19-year-old dual US/Estonian citizen and alleged member was extradited from Finland to face U.S. charges of conspiracy, computer intrusion, and fraud. The group remains active despite law enforcement actions.
- **JADEPUFFER**: Operator name assigned by Sysdig to an AI agent observed conducting fully autonomous ransomware attacks. The agent exploited a Langflow RCE, performed reconnaissance, moved laterally, and encrypted databases without human direction. Represents a new class of AI-driven threat actor.
- **ShinyHunters**: Data extortion group responsible for the Medtronic breach. Known for stealing and selling large databases from compromised organizations across healthcare, technology, and other sectors.
- **Ousaban Operators**: Brazilian threat actors deploying the Ousaban banking trojan against users of Spanish and Portuguese banks. Campaign uses phishing PDF lures and targets Windows systems. Identified by FortiGuard Labs in May 2026.
- **VEIL#DROP / PureLogs Operators**: Unknown threat actors running a multi-stage malware delivery chain leveraging Google Blogger for payload hosting. Delivers the PureLogs information stealer via social engineering lures.
- **AsyncRAT / ScreenConnect Campaign Operators**: Unknown actors conducting a "massive, multi-domain, multi-language" campaign (per Kaspersky) using SEO-poisoned software sites to deploy AsyncRAT via abused ScreenConnect installations.
- **ChocoPoC Distributors**: Unknown actors targeting vulnerability researchers by planting trojanized PoC exploits in public GitHub repositories. Motivation appears to be compromising researcher infrastructure for intelligence gathering or further supply chain attacks.
- **HSIN Intrusion Actors**: Unknown threat actors who breached the Department of Homeland Security's Homeland Security Information Network, a sensitive inter-agency information sharing platform. Attribution not publicly disclosed.
- **Kubota Intrusion Actors**: Unknown threat actors who maintained access to Kubota North America network systems for over one month earlier in the year. Details on initial access vector and objectives not fully disclosed.

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
