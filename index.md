# Exploitation Report

## Executive Summary

Law enforcement and industry partners have disrupted the NetNut residential proxy platform and Popa botnet, seizing hundreds of domains used to route malicious traffic through approximately two million compromised home devices. This takedown coincides with Google's independent degradation of the same network, marking a significant blow to a service that enabled threat actors to anonymize attacks, scrape data, and evade detection at massive scale.

Ransomware operations are rapidly adopting new initial-access techniques. The Anubis gang is actively exploiting Citrix Bleed 2 (CVE-2025-5777) for entry, while the FortiBleed credential-theft campaign—linked to INC and Lynx ransomware groups—has harvested thousands of Fortinet VPN credentials and is now leveraging a Nextcloud zero-day to expand compromise. Simultaneously, CISA has added a Microsoft SharePoint RCE (CVE-2026-45659) to its Known Exploited Vulnerabilities catalog after confirming active exploitation, and Cisco has acknowledged attackers targeting a Unified CM flaw patched in early June.

Social engineering has evolved into the dominant delivery mechanism. ClickFix and ConsentFix campaigns now hijack Microsoft 365 tokens in seconds through fake OAuth prompts, while SEO-poisoned software sites abuse legitimate remote-access tools like ScreenConnect to deploy AsyncRAT. Threat actors including ToddyCat are weaponizing OAuth flows to access Gmail via the Google API, and a novel AI agent dubbed JADEPUFFER has been observed autonomously exploiting a Langflow RCE to execute end-to-end database ransomware attacks. Researchers themselves are being targeted through trojanized proof-of-concept exploits (ChocoPoC RAT) hosted on GitHub.

## Active Exploitation Details

### Citrix Bleed 2
- **Description**: A critical vulnerability in Citrix NetScaler ADC and Gateway appliances that allows unauthenticated attackers to obtain active session cookies and bypass authentication, leading to full administrative access.
- **Impact**: Attackers gain initial access to corporate networks, enabling lateral movement, data exfiltration, and ransomware deployment. The Anubis ransomware operation has been observed exploiting this flaw for initial access.
- **Status**: Actively exploited in the wild. Patches are available from Citrix.
- **CVE ID**: CVE-2025-5777

### FortiBleed Credential Theft Campaign
- **Description**: A large-scale campaign targeting Fortinet FortiGate VPN appliances to steal valid credentials. The campaign has compromised thousands of devices and is now expanding exploitation to include a Nextcloud zero-day vulnerability.
- **Impact**: Stolen VPN credentials provide persistent remote access to corporate networks. Credentials are being monetized through collaboration with INC and Lynx ransomware operations for follow-on intrusion and ransomware deployment.
- **Status**: Active exploitation ongoing. Fortinet patches available for known vulnerabilities; Nextcloud zero-day remains unpatched at time of reporting.

### Microsoft SharePoint Remote Code Execution
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server that allows authenticated attackers to execute arbitrary code in the context of the SharePoint application pool.
- **Impact**: Successful exploitation leads to full compromise of the SharePoint server, potential lateral movement within the network, and access to sensitive organizational data stored in SharePoint.
- **Status**: Actively exploited in the wild. CISA added to Known Exploited Vulnerabilities catalog. Patched in May 2026.
- **CVE ID**: CVE-2026-45659

### Cisco Unified Communications Manager Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that allows attackers to exploit the call processing component.
- **Impact**: Attackers can achieve remote code execution or denial of service on affected Unified CM deployments, potentially disrupting communications and gaining a foothold in voice infrastructure.
- **Status**: Cisco confirmed active exploitation. Patched in early June 2026.

### Langflow RCE Exploitation by AI Agent
- **Description**: A remote code execution vulnerability in Langflow, a visual framework for building AI applications, which allows unauthenticated attackers to execute arbitrary code.
- **Impact**: The JADEPUFFER threat actor deployed an AI agent that autonomously exploited this vulnerability to conduct end-to-end database ransomware attacks—the first observed case of an AI agent executing a complete ransomware operation from initial access to encryption.
- **Status**: Actively exploited. Patch status varies by deployment.

### Argo CD Repo-Server Flaw
- **Description**: An unpatched vulnerability in the Argo CD repo-server component that allows unauthenticated attackers to execute arbitrary code, provided they can reach the component.
- **Impact**: Full compromise of Kubernetes clusters managed by Argo CD, enabling supply chain attacks, workload manipulation, and cluster takeover.
- **Status**: Unpatched at time of reporting. No official fix available. Mitigation requires network-level restrictions on repo-server access.

### NetNut Residential Proxy Platform / Popa Botnet
- **Description**: A sprawling residential proxy service (NetNut) and associated botnet (Popa) that turned approximately two million home devices into rented relays for malicious traffic.
- **Impact**: Enabled threat actors to anonymize attacks, conduct credential stuffing, scrape data, evade geo-blocking, and hide malicious infrastructure behind legitimate residential IPs.
- **Status**: Disrupted. FBI seized hundreds of domains; Google independently degraded the network in coordination with FBI and Lumen.

### Nextcloud Zero-Day
- **Description**: An unpatched vulnerability in Nextcloud being exploited by FortiBleed actors to expand their compromise beyond Fortinet devices.
- **Impact**: Provides additional attack surface for credential theft and lateral movement within organizations using Nextcloud for file sharing and collaboration.
- **Status**: Actively exploited. Zero-day—no patch available at time of reporting.

### Apple Email Flaw
- **Description**: A vulnerability in Apple's email infrastructure referenced in threat intelligence reporting.
- **Impact**: Details limited in available reporting; potential for email interception, spoofing, or account compromise.
- **Status**: Referenced in threat intelligence summaries; patch status unclear from available sources.

### BlueHammer Ransomware
- **Description**: A ransomware variant observed in recent threat activity.
- **Impact**: Data encryption and extortion targeting organizations across multiple sectors.
- **Status**: Active campaigns observed in threat intelligence reporting.

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: Versions vulnerable to CVE-2025-5777 (Citrix Bleed 2)
- **Fortinet FortiGate VPN Appliances**: Multiple models and firmware versions targeted by FortiBleed campaign
- **Microsoft SharePoint Server**: Versions vulnerable to CVE-2026-45659 (patched May 2026)
- **Cisco Unified Communications Manager**: Versions prior to June 2026 security updates
- **Langflow**: AI application framework deployments exposed to internet or internal networks
- **Argo CD**: Kubernetes deployments using the repo-server component (all current versions potentially affected)
- **Nextcloud**: Self-hosted and managed instances (zero-day exploitation reported)
- **NetNut Proxy Client Software**: Home devices enrolled in the residential proxy network (approx. 2 million devices)
- **Apple Email Infrastructure**: Affected versions unspecified in available reporting
- **ScreenConnect Remote Access Tool**: Legitimate tool abused via SEO-poisoned downloads to deploy AsyncRAT
- **Microsoft 365 / Entra ID**: Tenants targeted by ClickFix and ConsentFix OAuth token theft campaigns
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat's Umbrij malware via OAuth API abuse
- **GitHub / Python Package Repositories**: Researchers downloading trojanized PoC exploits delivering ChocoPoC RAT

## Attack Vectors and Techniques

- **ClickFix / ConsentFix Social Engineering**: Attackers present fake CAPTCHA verification, browser update, or error prompts that trick users into copying and executing malicious PowerShell commands. The commands abuse legitimate Windows features (mshta, clipboard manipulation) to steal Microsoft 365 OAuth tokens and bypass MFA in seconds.
- **Residential Proxy Abuse**: Threat actors rent access to the NetNut/Popa network to route malicious traffic through compromised home routers and IoT devices, masking true origin and evading IP-based blocking.
- **SEO Poisoning with Legitimate Tool Abuse**: Attackers compromise or create software download sites optimized for search rankings, distributing legitimate remote-access tools (ScreenConnect) trojanized to deploy AsyncRAT silently during installation.
- **OAuth Token Theft and API Abuse**: ToddyCat's Umbrij malware steals OAuth refresh tokens to access Google APIs (Gmail, Drive) without triggering MFA, enabling persistent email surveillance.
- **Supply Chain Credential Theft**: Ransomware groups harvest credentials from compromised vendors, MSPs, and software supply chains to gain trusted access to downstream targets.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Attackers load known vulnerable kernel drivers to disable security products and escalate privileges on compromised endpoints.
- **AI-Automated Exploitation**: The JADEPUFFER operator deployed an autonomous AI agent that discovered, exploited, and weaponized a Langflow RCE to execute database ransomware without human intervention.
- **Trojanized Proof-of-Concept Exploits**: ChocoPoC RAT is embedded in fake Python PoC repositories on GitHub, targeting vulnerability researchers who execute the code during analysis.
- **Interpol-Themed Phishing**: Ransomware campaigns use law-enforcement impersonation (Interpol branding) to pressure small businesses into executing payloads.
- **Unpatched Component Exploitation**: Attackers target exposed Argo CD repo-server instances for unauthenticated Kubernetes cluster takeover.

## Threat Actor Activities

- **FortiBleed Actors**: Financially motivated group conducting mass credential theft from Fortinet VPN appliances. Now collaborating with INC and Lynx ransomware operations to monetize access. Expanding exploitation to Nextcloud zero-day.
- **INC Ransomware**: Ransomware-as-a-service operation partnering with FortiBleed actors to convert stolen VPN credentials into ransomware deployments.
- **Lynx Ransomware**: Ransomware group linked to FortiBleed credential theft, using stolen access for initial intrusion and encryption.
- **Anubis Ransomware**: Operation actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access across multiple victims.
- **ToddyCat (APT)**: Chinese-aligned advanced persistent threat deploying Umbrij malware to abuse OAuth flows and access Gmail via Google API for espionage.
- **Scattered Spider (UNC3944 / 0ktapus)**: Social-engineering-focused group targeting telecommunications, BPO, and technology firms. 19-year-old dual US-Estonian citizen extradited from Finland; additional member extradited per DOJ.
- **JADEPUFFER**: Novel threat operator deploying an autonomous AI agent to conduct end-to-end ransomware attacks via Langflow RCE exploitation—first observed case of AI-driven autonomous ransomware operation.
- **ChocoPoC Operators**: Unknown actors targeting vulnerability researchers via trojanized PoC exploits on GitHub, delivering Python-based RAT for data theft and command execution.
- **ShinyHunters**: Data extortion group responsible for breach impacting Medtronic customer data.
- **AsyncRAT Operators**: Threat actors leveraging SEO-poisoned software distribution sites to deploy AsyncRAT via trojanized ScreenConnect installers.
- **BlueHammer Ransomware**: Emerging ransomware variant observed in recent threat intelligence reporting.

## Source Attribution

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
- **Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters**: The Hacker News - https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html
- **19-Year-Old Scattered Spider Suspect Extradited to Face U.S. Hacking Charges**: The Hacker News - https://thehackernews.com/2026/07/19-year-old-scattered-spider-suspect.html
- **SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT**: The Hacker News - https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html
- **DHS confirms hackers breached HSIN info-sharing platform**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/
