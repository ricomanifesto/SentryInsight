# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors leveraging both newly disclosed vulnerabilities and refined social engineering techniques. The most critical activity centers on Microsoft SharePoint Server, where CISA has confirmed active exploitation of a high-severity remote code execution flaw (CVE-2026-45659) patched in May, leading to its addition to the Known Exploited Vulnerabilities catalog. Simultaneously, Cisco has acknowledged that attackers are exploiting a Unified Communications Manager vulnerability patched in early June, demonstrating rapid weaponization of recently disclosed flaws.

Social engineering has evolved into a dominant initial access methodology, with ClickFix and ConsentFix techniques now characterized as the "rule rather than the exception" for malware delivery. These attacks hijack Microsoft 365 accounts in seconds by abusing OAuth consent flows and fake verification prompts to bypass multi-factor authentication. A parallel campaign by the ToddyCat threat actor deploys the Umbrij malware to abuse Google OAuth for surreptitious Gmail access, while SEO-poisoned software download sites leverage ScreenConnect to deploy AsyncRAT at scale. An aggressive password-spraying operation generated over 81 million login attempts against Microsoft 365 environments in just two weeks.

Emerging threats include the first observed ransomware attack fully automated by an AI agent—dubbed JADEPUFFER—exploiting a Langflow RCE vulnerability to execute database ransomware operations. Vulnerability researchers are being directly targeted through trojanized proof-of-concept exploits (ChocoPoC RAT) hosted on GitHub, while the FortiBleed credential theft campaign has been linked to INC and Lynx ransomware operations, indicating stolen Fortinet credentials are fueling follow-on intrusions. An unpatched Argo CD repo-server flaw exposes Kubernetes clusters to unauthenticated code execution, and the VEIL#DROP malware chain abuses the Blogger platform to deliver the PureLogs information stealer.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server that was patched in May 2026. The flaw allows authenticated attackers to execute arbitrary code on affected SharePoint servers.
- **Impact**: Attackers can achieve full server compromise, enabling data theft, lateral movement, and persistence within organizational networks. Successful exploitation grants the attacker the same permissions as the SharePoint service account.
- **Status**: Actively exploited in the wild. CISA added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog on July 16, 2026, mandating federal agencies to patch by August 6, 2026. Microsoft released patches in May 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that Cisco confirmed is being actively exploited by attackers. The flaw was patched in early June 2026.
- **Impact**: Exploitation could allow attackers to compromise the Unified CM platform, potentially leading to interception of communications, unauthorized access to voicemail, call detail records, and lateral movement into connected voice and video infrastructure.
- **Status**: Actively exploited. Cisco has released patches and confirmed exploitation activity. Organizations running affected versions should prioritize immediate patching.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### Langflow Remote Code Execution
- **Description**: A remote code execution vulnerability in Langflow, a visual framework for building AI applications and agents. The vulnerability was exploited by an AI agent to automate a complete ransomware attack chain.
- **Impact**: Attackers can achieve remote code execution on Langflow servers, enabling deployment of ransomware, data exfiltration, and full system compromise. The JADEPUFFER operator demonstrated end-to-end automation from initial access to database encryption.
- **Status**: Actively exploited in the wild by the JADEPUFFER threat actor. This represents the first documented case of an AI agent autonomously executing a complete ransomware attack.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### Argo CD Repo-Server Unpatched Flaw
- **Description**: An unpatched vulnerability in the repo-server component of Argo CD, a widely used GitOps continuous delivery tool for Kubernetes. The flaw allows unauthenticated attackers to execute code if they can reach the repo-server component.
- **Impact**: Successful exploitation grants attackers the ability to take over Kubernetes clusters, deploy malicious workloads, access secrets, and achieve full control over containerized infrastructure.
- **Status**: Unpatched as of the reporting date. No official fix has been released. Mitigation requires network segmentation to restrict access to the repo-server component.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### FortiBleed Credential Theft Campaign
- **Description**: A large-scale credential theft campaign targeting Fortinet devices, resulting in verified stolen credentials that have been linked to INC and Lynx ransomware operations.
- **Impact**: Stolen Fortinet VPN and firewall credentials enable initial access for ransomware deployment, network reconnaissance, lateral movement, and data exfiltration. The linkage to active ransomware groups indicates credentials are being rapidly operationalized.
- **Status**: Active campaign with confirmed attribution to INC and Lynx ransomware affiliates. Organizations using Fortinet VPN solutions should audit logs for unauthorized access and rotate credentials.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

## Affected Systems and Products

- **Microsoft SharePoint Server**: Versions affected by CVE-2026-45659 (patched in May 2026 updates). On-premises SharePoint Server deployments.
- **Cisco Unified Communications Manager (Unified CM)**: Versions prior to the June 2026 security patch. On-premises and virtualized deployments.
- **Langflow**: AI application framework installations exposed to network access. Specific affected versions not detailed in source articles.
- **Argo CD**: All versions with exposed repo-server component. Kubernetes clusters using Argo CD for GitOps deployments.
- **Fortinet FortiGate / FortiClient VPN**: Devices targeted in the FortiBleed credential harvesting campaign. Specific firmware versions not detailed.
- **Microsoft 365 / Entra ID**: Tenants targeted by ConsentFix, ClickFix, and password-spraying campaigns (81M+ login attempts).
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat's Umbrij malware via OAuth abuse.
- **ScreenConnect**: Remote access tool abused via SEO-poisoned software download sites to deploy AsyncRAT.
- **Kubota North America Corporation network systems**: Compromised for over a month earlier in 2026.
- **DHS Homeland Security Information Network (HSIN)**: Sensitive information-sharing platform breached by unknown actors.
- **Adobe ColdFusion and Campaign Classic**: Seven CVSS 10.0 flaws patched in July 2026; no active exploitation reported in source articles.
- **Banking users in Spain and Portugal**: Targeted by Ousaban banking trojan via fake PDF lures.
- **Vulnerability researchers**: Targeted via trojanized PoC exploits (ChocoPoC RAT) on GitHub.

## Attack Vectors and Techniques

- **ConsentFix / ClickFix OAuth Abuse**: Attackers create malicious OAuth applications or consent prompts that trick users into granting permissions to attacker-controlled apps. This bypasses MFA by leveraging legitimate Microsoft 365/Entra ID consent flows. Tokens are stolen in seconds, enabling full account takeover.
- **ClickFix Social Engineering (Dominant Malware Delivery)**: Users are tricked into copying and executing malicious commands (often PowerShell) via fake verification pages, CAPTCHA prompts, or "I'm not a robot" checks. Now the primary delivery method for multiple malware families.
- **ToddyCat Umbrij OAuth Exploitation**: Malware steals Google OAuth tokens to access Gmail via the Google API, enabling persistent, surreptitious email monitoring without triggering security alerts.
- **SEO Poisoning with ScreenConnect**: Threat actors create malicious software download sites ranked highly in search results. Victims downloading legitimate-looking tools receive ScreenConnect installers that deploy AsyncRAT.
- **Trojanized Proof-of-Concept Exploits (ChocoPoC RAT)**: Weaponized Python PoC repositories on GitHub target vulnerability researchers. When researchers execute the PoC, the ChocoPoC RAT installs, providing command execution and data theft capabilities.
- **AI-Automated Ransomware (JADEPUFFER)**: An AI agent autonomously exploited a Langflow RCE, performed reconnaissance, moved laterally, and deployed database ransomware—representing a paradigm shift in attack automation.
- **Password Spraying at Scale**: Distributed login attempts (81M+ over two weeks) against Microsoft 365 accounts using common passwords, avoiding account lockouts through low-and-slow distribution across IP addresses.
- **VEIL#DROP Multi-Stage Delivery via Blogger**: Attack chain uses social engineering to direct victims to Blogger-hosted pages that deliver the PureLogs information stealer through multiple stages.
- **Phishing with Device/OS Auto-Adaptation**: Campaigns fingerprint victims via User-Agent strings and dynamically serve OS-specific payloads (Windows, macOS, Linux, mobile), increasing compromise rates.
- **Phantom Squatting (AI-Hallucinated Domains)**: Attackers register domains hallucinated by LLAs when generating code or documentation for legitimate brands, creating difficult-to-detect supply chain typosquatting.
- **Fake PDF Lures (Ousaban Banking Trojan)**: Phishing emails with PDF attachments targeting Iberian banking users. PDFs trigger malicious payloads that steal banking credentials and 2FA codes.
- **Unpatched Argo CD Repo-Server Exploitation**: Unauthenticated RCE via the repo-server component when exposed to attacker-controlled networks or supply chain compromise.

## Threat Actor Activities

- **ToddyCat (APT)**: Chinese-aligned APT group attributed to the Umbrij malware campaign. Targets Gmail accounts via OAuth token theft for espionage purposes. Demonstrates sophisticated understanding of Google's authentication architecture.
- **Scattered Spider (UNC3944 / 0ktapus)**: Financially motivated threat group specializing in social engineering, SIM swapping, and SaaS compromise. A 19-year-old dual US/Estonian citizen was extradited from Finland to face US charges (conspiracy, computer intrusion, fraud). Group known for targeting large enterprises, casinos, and telecommunications.
- **INC Ransomware (INC Ransom)**: Ransomware operation linked to the FortiBleed credential theft campaign. Uses stolen Fortinet credentials for initial access. Operates as a RaaS affiliate model.
- **Lynx Ransomware**: Ransomware group also linked to FortiBleed credentials. Indicates credential sharing or collaboration between INC and Lynx operations.
- **JADEPUFFER**: Threat actor (or operator) behind the first fully AI-automated ransomware attack. Leveraged an AI agent to exploit Langflow RCE and execute end-to-end database ransomware. Represents a new class of AI-driven offensive operations.
- **ChocoPoC Operators**: Unknown threat actors targeting vulnerability researchers via trojanized PoC exploits on GitHub. Campaign demonstrates deep understanding of researcher workflows and trust in PoC code.
- **ShinyHunters**: Data extortion group responsible for the Medtronic breach. Known for stealing and selling/leaking large databases from healthcare and technology companies.
- **VEIL#DROP Operators**: Unknown actors behind the multi-stage malware chain using Blogger to deliver PureLogs stealer. Campaign active as of July 2026.
- **Ousaban Operators**: Brazilian banking trojan group targeting users in Spain and Portugal. Uses localized phishing lures and sophisticated anti-analysis techniques.
- **SEO-Poisoning/AsyncRAT Actors**: Unknown threat actors conducting "massive, multi-domain, multi-language" campaign abusing ScreenConnect via poisoned search results.
- **HSIN Breach Actors**: Unknown actors who compromised the DHS Homeland Security Information Network. Investigation ongoing by DHS.
- **Kubota Intrusion Actors**: Unknown actors who maintained access to Kubota North America network systems for over a month earlier in 2026.
- **Password-Spraying Campaign Operators**: Unknown actors behind the 81-million-attempt campaign against Microsoft 365. Infrastructure suggests distributed, coordinated operation.

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
