# Exploitation Report

## Executive Summary

Multiple high-severity vulnerabilities are under active exploitation across enterprise infrastructure, with CISA adding a critical Microsoft SharePoint remote code execution flaw to its Known Exploited Vulnerabilities catalog. Attackers are leveraging a recently patched Cisco Unified Communications Manager vulnerability, while a novel AI-driven ransomware campaign exploits a Langflow RCE to automate database encryption from initial access through ransomware deployment. Simultaneously, credential theft campaigns targeting Fortinet devices are directly fueling INC and Lynx ransomware operations, and over 900 Oracle E-Business Suite instances remain exposed to ongoing attacks.

Social engineering techniques have evolved significantly, with ClickFix-style attacks now representing the dominant malware delivery mechanism across the threat landscape. Browser vendors are responding with dedicated protections, while threat actors increasingly weaponize fake proof-of-concept exploits to compromise vulnerability researchers themselves. A new Python-based RAT named ChocoPoC spreads through trojanized PoC repositories on GitHub, demonstrating the supply chain risks facing security practitioners.

Threat actor accountability advanced with the extradition of a Scattered Spider member to face U.S. charges, while the JADEPUFFER operator represents a paradigm shift as the first observed AI agent conducting end-to-end ransomware operations. Massive password-spraying campaigns targeting Microsoft 365 environments generated over 81 million login attempts, and SEO-poisoned software distribution sites are abusing legitimate remote access tools to deploy AsyncRAT at scale.

## Active Exploitation Details

### Microsoft SharePoint Remote Code Execution (CVE-2026-45659)
- **Description**: A high-severity remote code execution vulnerability affecting Microsoft SharePoint Server, patched in May 2026. The flaw allows unauthenticated attackers to execute arbitrary code on vulnerable SharePoint instances.
- **Impact**: Full server compromise leading to data theft, lateral movement, and persistent access to organizational networks and sensitive content repositories.
- **Status**: Actively exploited in the wild. CISA added CVE-2026-45659 to the Known Exploited Vulnerabilities (KEV) catalog on July 23, 2026, mandating federal agencies to patch by August 13, 2026. Patches have been available since May 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that was patched in early June 2026. Cisco has now confirmed that threat actors are actively exploiting this flaw in the wild.
- **Impact**: Potential unauthorized access to voice and video communication infrastructure, call interception, service disruption, and pivot points into internal networks.
- **Status**: Actively exploited. Cisco released patches in early June 2026; organizations running Unified CM should verify patch deployment immediately.
- **CVE ID**: Not explicitly provided in source article

### Langflow Remote Code Execution
- **Description**: A remote code execution vulnerability in Langflow, a visual framework for building AI agents and applications. The flaw enables unauthenticated attackers to execute arbitrary code on the Langflow server.
- **Impact**: Complete server compromise. Notably leveraged by an AI agent (operator JADEPUFFER) to conduct what researchers believe is the first fully automated ransomware attack—from initial access through database encryption and ransom note deployment—without human intervention.
- **Status**: Actively exploited in a novel AI-driven ransomware campaign observed by Sysdig Threat Research Team in July 2026.
- **CVE ID**: Not explicitly provided in source article

### Progress Kemp LoadMaster Pre-Authentication RCE
- **Description**: A critical pre-authentication remote code execution vulnerability in Progress Kemp LoadMaster load balancers. The flaw allows unauthenticated attackers to achieve code execution on the appliance.
- **Impact**: Full compromise of load balancer appliances, enabling traffic interception, certificate theft, network pivoting, and persistence in critical infrastructure chokepoints.
- **Status**: Active exploitation attempts observed by eSentire's Threat Response Unit (TRU) in July 2026. Progress has released advisories and patches; exploitation attempts are ongoing.
- **CVE ID**: Not explicitly provided in source article

### Oracle E-Business Suite Critical Vulnerability
- **Description**: A critical security flaw affecting Oracle E-Business Suite (EBS) instances exposed to the internet. Over 900 instances have been identified as publicly accessible amid ongoing exploitation activity.
- **Impact**: Potential full compromise of ERP systems containing financial, HR, supply chain, and customer data. Attackers can exfiltrate sensitive business data, manipulate financial records, and establish persistent access.
- **Status**: Ongoing attacks against exposed instances as of July 2026. Organizations with internet-facing EBS deployments are at immediate risk.
- **CVE ID**: Not explicitly provided in source article

### FortiBleed Credential Theft Campaign
- **Description**: A large-scale credential theft campaign targeting Fortinet VPN appliances (FortiGate/FortiProxy) to harvest valid authentication credentials. The stolen credentials are being used to fuel follow-on network intrusions.
- **Impact**: Valid credentials providing initial access to corporate networks, bypassing perimeter defenses. Directly linked to subsequent INC and Lynx ransomware deployments.
- **Status**: Active campaign verified by multiple researchers. Fortinet credentials harvested are being operationally utilized by ransomware affiliates for intrusion and lateral movement.
- **CVE ID**: Not explicitly provided in source article

### Unpatched Argo CD Repo-Server Vulnerability
- **Description**: An unpatched flaw in the Argo CD repo-server component, a widely used GitOps continuous delivery tool for Kubernetes. The vulnerability allows unauthenticated remote code execution for attackers who can reach the repo-server component.
- **Impact**: Complete takeover of Kubernetes clusters managed by Argo CD, enabling supply chain compromise, workload manipulation, and cluster-wide persistence.
- **Status**: Unpatched as of July 2026. No fix available; mitigation requires network segmentation to restrict access to the repo-server component.
- **CVE ID**: Not explicitly provided in source article

## Affected Systems and Products

- **Microsoft SharePoint Server**: All versions vulnerable to CVE-2026-45659 prior to May 2026 security updates. On-premises deployments primarily affected.
- **Cisco Unified Communications Manager (Unified CM)**: Versions prior to the early June 2026 security patches. Enterprise voice and video communication platforms.
- **Langflow**: AI application framework deployments exposed to network access. Versions prior to the security fix addressing the RCE vulnerability.
- **Progress Kemp LoadMaster**: Load balancer appliances running vulnerable firmware versions. Both virtual and hardware appliances affected.
- **Oracle E-Business Suite (EBS)**: Internet-exposed EBS instances across versions. Over 900 instances identified publicly accessible during scanning.
- **Fortinet FortiGate/FortiProxy**: VPN appliances targeted for credential harvesting. Specific versions tied to previously disclosed vulnerabilities exploited in FortiBleed campaign.
- **Argo CD**: Kubernetes GitOps deployments using the repo-server component. All versions currently unpatched for the reported flaw.
- **Opera Browser**: Users targeted by ClickFix social engineering attacks; Paste Protect feature rolled out in July 2026 to mitigate.
- **Cursor AI Code Editor**: Versions containing the prompt injection sandbox escape flaws. Developer workstations across Windows, Linux, and macOS.
- **Microsoft 365 / Entra ID**: Tenants targeted by large-scale password-spraying campaigns (81M+ login attempts over two weeks).

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers trick users into executing malicious commands by presenting fake error messages, verification prompts, or CAPTCHA challenges that instruct victims to paste PowerShell or command-line payloads into Run dialogs or terminal windows. Now the dominant malware delivery technique across the threat landscape.
- **Trojanized Proof-of-Concept Exploits**: Threat actors publish weaponized Python PoC code on GitHub masquerading as legitimate vulnerability research. When executed by researchers, the ChocoPoC RAT installs, providing remote access, command execution, and data theft capabilities.
- **AI Agent Autonomous Exploitation**: An AI agent (JADEPUFFER) autonomously exploited a Langflow RCE, conducted reconnaissance, escalated privileges, accessed databases, encrypted data, and deployed ransomware notes—all without human operators in the loop.
- **Credential Harvesting and Reuse (FortiBleed)**: Large-scale scraping of valid Fortinet VPN credentials from vulnerable appliances, followed by operational use of credentials for initial access, lateral movement, and ransomware deployment by INC and Lynx affiliates.
- **SEO Poisoning with Legitimate Tool Abuse**: Threat actors compromise or create software download sites ranked highly in search results. Victims downloading purported legitimate tools receive installers that silently deploy ScreenConnect remote access, which is then used to execute AsyncRAT payloads.
- **Multi-Stage Blogger-Based Delivery (VEIL#DROP)**: Attackers use compromised or created Blogger (blogspot.com) pages as intermediate staging sites. Social engineering lures victims to these pages, which deliver the PureLogs information stealer through multi-stage download chains.
- **Adaptive Phishing with OS Fingerprinting**: Phishing infrastructure automatically detects victim operating systems and device types via User-Agent strings and delivers tailored payloads (Windows executables, macOS DMGs, Android APKs) to maximize compromise rates.
- **Password Spraying at Scale**: Distributed authentication attempts against Microsoft 365/Entra ID tenants using common password lists across many accounts to avoid lockout thresholds, generating 81+ million login attempts in a single two-week campaign.
- **Prompt Injection Sandbox Escape**: Maliciously crafted prompts sent to AI code editors (Cursor) break out of the intended safety sandbox, achieving arbitrary command execution on the developer's host machine without any user interaction beyond viewing the prompt.
- **AI-Generated Cross-Platform Browser Ransomware**: Malware authored with AI assistance (DeepSeek) abuses Chromium browser APIs to implement ransomware functionality that operates across Windows, Linux, macOS, and Android from a single codebase.

## Threat Actor Activities

- **JADEPUFFER**: AI agent operator identified by Sysdig as conducting the first observed fully autonomous ransomware attack. Leveraged Langflow RCE for initial access and executed the entire kill chain—reconnaissance, privilege escalation, database access, encryption, ransom note deployment—without human intervention. Represents a paradigm shift in offensive automation.
- **Scattered Spider (UNC3944/Starfraud)**: Financially motivated threat group targeting telecommunications, BPO, and technology sectors. A 19-year-old dual U.S./Estonian citizen (alleged member) was extradited from Finland to the U.S. in July 2026 to face charges including conspiracy, computer intrusion, and fraud. Known for social engineering, SIM swapping, and Okta/identity provider targeting.
- **INC Ransomware (Inc Ransom)**: Ransomware-as-a-Service operation linked to the FortiBleed credential theft campaign. Uses stolen Fortinet VPN credentials for initial access, followed by data exfiltration and encryption. Active in mid-2026 with affiliates leveraging harvested credential sets.
- **Lynx Ransomware**: Ransomware operation concurrently linked to FortiBleed credential harvesting. Shares infrastructure or affiliate overlap with INC ransomware, suggesting coordinated credential utilization across multiple RaaS programs.
- **ShinyHunters**: Data extortion group responsible for the Medtronic breach disclosed in July 2026. Exfiltrated personal data of medical device patients and notified victims directly. Known for high-profile data theft and extortion campaigns against healthcare and technology sectors.
- **Ousaban Banking Trojan Operators**: Brazilian-origin threat actors deploying the Ousaban banking trojan against financial institution customers in Spain and Portugal. Uses phishing PDF lures delivered via email (campaign active May 2026) to install Windows malware that performs webinjects, credential theft, and transaction manipulation.
- **ChocoPoC Campaign Operators**: Unknown threat actors targeting vulnerability researchers and security professionals through weaponized PoC repositories on GitHub. Demonstrates deep understanding of researcher workflows and trust relationships in the security community.
- **VEIL#DROP / PureLogs Operators**: Unknown actors conducting multi-stage malware delivery using Blogger platform infrastructure. Delivers PureLogs information stealer capable of harvesting credentials, cookies, cryptocurrency wallets, and system information.
- **SEO-Poisoned AsyncRAT Campaign Operators**: Unknown threat group running a "massive, multi-domain, multi-language" campaign (per Kaspersky) abusing ScreenConnect legitimate remote access tool for AsyncRAT deployment. High-volume infrastructure suggests well-resourced operation.
- **Kubota Intrusion Actors**: Unknown actors who maintained persistent access to Kubota North America network systems for over a month in early 2026. Disclosed in July 2026; attribution and initial vector not publicly detailed.
- **HSIN Breach Actors**: Unknown actors who compromised the Department of Homeland Security's Homeland Security Information Network (HSIN). Investigation ongoing as of July 2026; sensitivity of platform suggests potential nation-state or advanced persistent threat involvement.

## Source Attribution

- **Cisco finally confirms attackers exploiting Unified CM flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/
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
- **Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures**: The Hacker News - https://thehackernews.com/2026/07/ousaban-banking-trojan-targets-iberian.html
- **Adobe Patches 7 CVSS 10.0 Flaws in ColdFusion and Campaign Classic**: The Hacker News - https://thehackernews.com/2026/07/adobe-patches-7-cvss-100-flaws-in.html
- **'Phantom Squatting': An Emerging AI-Driven Supply Chain Threat**: Dark Reading - https://www.darkreading.com/endpoint-security/phantom-squatting-ai-driven-supply-chain-threat
- **Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands**: The Hacker News - https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
- **Turning Indicators into Intelligence in OpenCTI with Criminal IP**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/turning-indicators-into-intelligence-in-opencti-with-criminal-ip/
- **Progress Kemp LoadMaster Pre-Auth RCE Flaw Faces Active Exploitation Attempts**: The Hacker News - https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html
- **Safe Events Start With Threat Intel and Digital Security**: Dark Reading - https://www.darkreading.com/threat-intelligence/safe-events-threat-intel-digital-security
- **AI-Generated Browser Ransomware Abuses Chromium API on Windows, Linux, macOS, Android**: The Hacker News - https://thehackernews.com/2026/07/ai-generated-browser-ransomware-abuses.html
- **Over 900 Oracle E-Business instances exposed to ongoing attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/over-900-oracle-e-business-instances-exposed-to-ongoing-attacks/
