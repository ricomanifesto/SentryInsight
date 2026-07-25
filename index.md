# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple high-impact vectors this period, with several zero-day and recently disclosed vulnerabilities under active attack. Most notably, a zero-day RCE in Fastjson 1.x—Alibaba's widely used Java JSON library—is being exploited in the wild with no patch available, placing Spring Boot applications at immediate risk. Simultaneously, Cl0p ransomware affiliates are conducting unauthenticated RCE attacks against internet-exposed PTC Windchill and FlexPLM deployments for data theft extortion, while researchers have published working exploits for GitLab (patched six weeks prior), Active Directory (Certighost), Bing Images (SYSTEM/root RCE via SVG), and Redis (seven emergency releases addressing authenticated RCE chains discovered by AI agents).

Threat actor operations show increased sophistication in automation and supply chain deception. North Korean BlueNoroff operators deploy ClickFix-style phishing kits on typosquatted Zoom and Teams domains that profile cryptocurrency wallets before malware delivery. The UAC-0099 group distributes MATCHBOIL.V2 via a trojanized Notepad++ plugin. Meanwhile, an unknown actor leveraged the open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation against Thailand's Ministry of Finance, marking a notable escalation in AI-assisted offensive operations. Credential stuffing, DNS hijacking on hotel Wi-Fi, and AI hallucination-driven supply chain attacks (slopsquatting) round out a diverse threat landscape.

## Active Exploitation Details

### Fastjson 1.x Zero-Day RCE
- **Description**: A critical remote code execution vulnerability in Fastjson 1.x, Alibaba's JSON library for Java. In affected Spring Boot applications, a malicious JSON request can execute arbitrary code on the server.
- **Impact**: Full remote code execution on Spring Boot applications using Fastjson 1.x for JSON deserialization. Attackers can achieve complete server compromise through crafted JSON payloads.
- **Status**: Actively exploited in the wild by threat actors. Security firms ThreatBook and Imperva confirm targeting. No patch is currently available for the 1.x branch, leaving users without a direct mitigation path beyond upgrading to Fastjson 2.x or implementing WAF rules.

### GitLab Authenticated RCE (CVE-2024-XXXX)
- **Description**: A remote code execution flaw in GitLab self-managed instances that allows authenticated users to execute commands as the `git` system user. The vulnerability was patched by GitLab on June 10, 2026.
- **Impact**: Authenticated attackers can run arbitrary commands with the privileges of the `git` user on the underlying server, potentially leading to full compromise of the GitLab host, source code theft, and supply chain poisoning.
- **Status**: Working proof-of-concept exploit code was published by depthfirst researchers on July 24, 2026, six weeks after the patch. All self-managed versions 18.11.3 and earlier are affected. Organizations that have not applied the June 10 patch are at immediate risk.
- **CVE ID**: CVE-2024-XXXX

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Unauthenticated remote code execution vulnerabilities in PTC Windchill and FlexPLM product lifecycle management platforms. The flaws allow remote attackers to execute code without authentication on internet-exposed deployments.
- **Impact**: Full server compromise, data exfiltration, and deployment of ransomware or extortion tooling. Cl0p affiliates are actively exploiting these flaws in a data theft extortion campaign.
- **Status**: Actively exploited by Cl0p (aka Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest) ransomware affiliates. Internet-exposed instances are being systematically targeted for initial access and data theft.

### Certighost Active Directory Privilege Escalation
- **Description**: An exploit technique allowing low-privileged Active Directory users to obtain a certificate for a Domain Controller and authenticate as that machine account. Researchers H0j3n and Aniq Fakhrul published a working exploit on July 24, 2026.
- **Impact**: Domain Controller impersonation leading to full domain compromise. Attackers can escalate from any standard domain user to effectively Domain Admin equivalent privileges by obtaining a machine certificate for a DC.
- **Status**: Working exploit code publicly available as of July 24, 2026. Affects environments with Active Directory Certificate Services (AD CS) configured in vulnerable configurations. No patch required—mitigation involves AD CS hardening and certificate template security.

### ChatGPT AgentForger Workspace Agent Deployment
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents that allows a single phishing link to stealthily build, authorize, and deploy a rogue autonomous agent within a victim's workspace.
- **Impact**: Attackers can deploy persistent, authorized AI agents that operate within the victim's ChatGPT environment with access to workspace data, tools, and connected integrations—all triggered by a single click.
- **Status**: Disclosed by cybersecurity researchers. The flaw enables phishing-driven AI agent compromise without traditional malware delivery.

### Bing Images SVG RCE
- **Description**: Crafted SVG files submitted to Bing's image search achieve remote code execution as `NT AUTHORITY\SYSTEM` on Microsoft's production Windows image-processing workers and as `root` on Linux machines in the same fleet.
- **Impact**: SYSTEM/root-level code execution on Microsoft's internal image processing infrastructure. Demonstrates critical flaws in SVG parsing and sandboxing.
- **Status**: Discovered and demonstrated by XBOW researchers. Microsoft's production infrastructure was affected. Remediation status on Microsoft's side not publicly detailed.

### Redis Authenticated RCE Zero-Days (Multiple Versions)
- **Description**: Seven security releases shipped on July 23, 2026, addressing authenticated RCE chains discovered by Kimi K3 AI agents. All four exploit chains require the `RESTORE` command and affect Redis 6.2.22, 7.4.9, 8.6.4, and 8.8.0. The Streams chain and other vectors enable authenticated users to achieve RCE.
- **Impact**: Authenticated remote code execution on Redis instances. Given Redis's common deployment in internal networks with weak authentication, this poses significant lateral movement and persistence risk.
- **Status**: Patched in emergency releases July 23, 2026. PoCs for all chains published by researchers. All affected versions should upgrade immediately.
- **CVE ID**: CVE-2026-XXXX (multiple CVEs assigned across the seven releases)

### NodeBB Forum Software High-Severity Flaws (Eight Vulnerabilities)
- **Description**: Eight high-severity security flaws in NodeBB forum software discovered by Aikido Security's AI pentest agents in a six-hour run. Flaws expose admin access and private chats.
- **Impact**: Administrative account takeover, private message/chats disclosure, and potential full forum compromise.
- **Status**: Publicly disclosed with exploit code on July 23, 2026. NodeBB has released patches. All eight rated high severity by Aikido Security.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A public-by-default configuration and chain of code flaws in Azure Automation that allowed attackers to seize another tenant's identity and access their data, credentials, and resources.
- **Impact**: Cross-tenant identity compromise in multi-tenant Azure environments. Attackers could escalate from a compromised subscription to neighboring tenants' Automation accounts and managed identities.
- **Status**: Microsoft has addressed the misconfiguration and underlying code flaws. Organizations should review Azure Automation network access settings and managed identity permissions.

### Vatican Prayer App API Exposure
- **Description**: A porous API endpoint in the Vatican's official prayer application exposing names, email addresses, country, and site status for over 700,000 global users—accessible to anyone with a browser.
- **Impact**: Mass PII exposure of 700,000+ users. No authentication or rate limiting on the API endpoint.
- **Status**: Disclosed by researchers. Remediation timeline not specified in reporting.

## Affected Systems and Products

- **Fastjson 1.x**: Alibaba's JSON library for Java; all 1.x versions in Spring Boot applications. No patched 1.x release available; migration to 2.x required.
- **GitLab Self-Managed**: Versions 18.11.3 and earlier. Patched in June 10, 2026 release. SaaS/GitLab.com not affected.
- **PTC Windchill**: Product lifecycle management platform; internet-exposed deployments targeted by Cl0p affiliates.
- **PTC FlexPLM**: Product lifecycle management for retail/footwear/apparel; internet-exposed instances targeted alongside Windchill.
- **Active Directory Certificate Services (AD CS)**: Windows Server environments with vulnerable certificate template configurations enabling Certighost.
- **ChatGPT Workspace Agents**: OpenAI's autonomous agent feature in ChatGPT; vulnerability in agent authorization/deployment flow.
- **Bing Image Processing Infrastructure**: Microsoft's internal Windows and Linux image-processing worker fleet handling SVG uploads.
- **Redis**: Versions 6.2.22, 7.4.9, 8.6.4, and 8.8.0. Patched in July 23, 2026 security releases (seven total).
- **NodeBB**: Forum software; all versions prior to the July 2026 security release containing fixes for eight high-severity flaws.
- **Azure Automation**: Multi-tenant Azure environments with default public network access on Automation accounts and vulnerable managed identity chains.
- **Vatican Prayer App (Click To Pray)**: Official Vatican mobile application backend API; 700,000+ global users affected.

## Attack Vectors and Techniques

- **Malicious JSON Deserialization**: Crafted JSON payloads targeting Fastjson 1.x in Spring Boot applications to achieve pre-auth RCE via unsafe deserialization.
- **Authenticated Command Injection**: GitLab vulnerability allowing authenticated users to inject commands executed as the `git` system user.
- **Unauthenticated RCE via Internet Exposure**: Direct exploitation of PTC Windchill/FlexPLM management interfaces exposed to the internet without authentication requirements.
- **AD CS Certificate Theft (Certighost)**: Low-privileged domain users request certificates for Domain Controller machine accounts, then authenticate as the DC via PKINIT/Kerberos.
- **Phishing-Driven AI Agent Deployment (AgentForger)**: Single malicious link triggers OAuth-style authorization flow to deploy rogue ChatGPT Workspace Agent with persistent workspace access.
- **SVG Parser Escape to SYSTEM/root**: Malformed SVG files exploiting parsing logic in Bing's image processing pipeline to break out of sandbox and execute code as highest-privilege system user.
- **Redis RESTORE Command Abuse**: Authenticated users leverage `RESTORE` command chains (Streams and other vectors) to achieve RCE on Redis servers.
- **AI-Discovered Vulnerability Chains**: Aikido Security's AI pentest agents identified eight distinct high-severity flaws in NodeBB in six hours; Kimi K3 agents discovered Redis zero-days and built exploits autonomously.
- **Cross-Tenant Identity Takeover via Default Configuration**: Exploitation of Azure Automation's public-by-default network access combined with managed identity permission chains to compromise neighboring tenants.
- **Unauthenticated API Enumeration**: Open API endpoint with no authentication or rate limiting allowing bulk PII harvest (Vatican app).
- **Hotel Wi-Fi DNS Hijacking**: Attackers compromise hotel/conference center Wi-Fi device DNS settings to redirect Microsoft 365 login traffic to credential harvesting pages.
- **ClickFix-Style Social Engineering with Typosquatting**: BlueNoroff uses typosquatted Zoom and Microsoft Teams domains to trick users into executing malicious commands via "ClickFix" fake error dialogs.
- **AI Agent Unattended Post-Exploitation (YOLO Mode)**: Threat actor deploys Hermes AI agent on rented infrastructure with safety controls disabled ("YOLO" mode) to automate reconnaissance, lateral movement, and data collection against Thai Finance Ministry.
- **Trojanized Legitimate Software Plugin**: UAC-0099 distributes MATCHBOIL.V2 malware via fake Notepad++ plugin, leveraging trust in legitimate development tools.
- **Credential Stuffing at Scale**: Automated login attempts using breached credential pairs against Chick-fil-A website and mobile app (13,000+ accounts compromised June 17–19).
- **Real-Time Phishing Account Hijacking**: Evolution beyond credential harvesting—attackers proxy victim sessions in real-time to bypass MFA and session controls (insurance sector targeting).
- **AI Hallucination Supply Chain Attacks (Slopsquatting/Phantom Domains/HalluSquatting)**: Attackers register package, repository, or domain names hallucinated by AI coding agents, which developers then inadvertently pull into projects.
- **Ransomware-as-a-Service Platform Centralization**: DevMan RaaS provides affiliates with web portal for payload building, victim management, earnings tracking, and payout automation.

## Threat Actor Activities

- **Cl0p / Clop (Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest)**: Actively exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM deployments for data theft extortion. Affiliates conduct initial access, data exfiltration, and leverage dedicated leak sites.
- **BlueNoroff (North Korean state-sponsored)**: Operating ClickFix-style phishing campaigns using typosquatted Zoom and Microsoft Teams domains. Deploy active phishing kit that profiles cryptocurrency wallet presence before delivering tailored malware. Targets crypto holders and financial sector.
- **UAC-0099**: Ukrainian CERT-UA-tracked group distributing MATCHBOIL.V2 malware via trojanized Notepad++ plugin. Targets Windows systems through software supply chain deception.
- **Golden Chickens (Maas operators)**: Resurfaced with four new malware families and modular implants, indicating continued investment in malware-as-a-service ecosystem. No signs of operational slowdown.
- **DevMan RaaS Operators**: Maintain centralized web platform for affiliate payload generation, victim management, earnings oversight, and automated payouts—professionalizing ransomware affiliate operations.
- **Hermes AI Operator (Unknown/Unattributed)**: Actor rented server infrastructure, deployed Hermes AI agent in unattended "YOLO" mode (safety controls disabled), and directed it at Thailand's Ministry of Finance for automated post-exploitation. Notable for AI-automated offensive operations.
- **Hotel Wi-Fi DNS Hijackers (Unknown/Unattributed)**: Compromise networking equipment at hotels and conference centers to modify DNS responses, redirecting Microsoft 365 authentication to adversary-controlled phishing pages.
- **OnTrac Network Intruders (Unknown/Unattributed)**: Breached OnTrac parcel delivery corporate network; potential customer PII access. Attribution not publicly established.
- **Chick-fil-A Credential Stuffers (Unknown/Unattributed)**: Large-scale credential stuffing campaign June 17–19, 2026 compromising 13,000+ customer accounts via website and mobile app login endpoints.
- **Snapchat Account Attacker (Identified/Prosecuted)**: Illinois man sentenced to 76 months for hacking 750+ women's Snapchat accounts to steal private photos. Represents resolved threat actor.
- **depthfirst Researchers**: Published working GitLab RCE PoC on July 24, 2026, six weeks after vendor patch. Responsible disclosure timeline observed; public exploit increases urgency for patching.
- **H0j3n and Aniq Fakhrul (Researchers)**: Published Certighost exploit for AD CS privilege escalation on July 24, 2026. Working code enables low-priv to DC compromise.
- **XBOW Researchers**: Discovered and demonstrated Bing Images SVG RCE achieving SYSTEM/root on Microsoft production infrastructure.
- **Kimi K3 AI Agents (Autonomous Research)**: Discovered Redis zero-days and autonomously built RCE exploit chains across four Redis versions, prompting seven emergency security releases.
- **Aikido Security AI Pentest Agents**: Discovered eight high-severity NodeBB flaws in six-hour automated run, demonstrating AI-driven vulnerability discovery at scale.

## Source Attribution

- **Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available**: The Hacker News - https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html
- **Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git**: The Hacker News - https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html
- **CTM360 Research Reveals How Insurance Phishing Has Evolved Into Real-Time Account Hijacking**: The Hacker News - https://thehackernews.com/2026/07/ctm360-research-reveals-how-insurance.html
- **Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE**: The Hacker News - https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
- **DevMan RaaS Portal Centralizes Payload Builds, Victim Management, and Affiliate Payouts**: The Hacker News - https://thehackernews.com/2026/07/devman-raas-portal-centralizes-payload.html
- **OpenAI confirms ChatGPT is down worldwide**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-confirms-chatgpt-is-down-worldwide/
- **CISOs vs. Boards: Myth or Misunderstanding?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cisos-vs-boards-myth-or-misunderstanding-
- **OnTrac notifies customers of data breach after network hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/
- **Escape Artists: 'Incorrigible' AI Models Resist Rehabilitation**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/incorrigible-ai-models-resist-rehabilitation
- **Hermes AI agent used to automate attack on Thai Finance Ministry**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hermes-ai-agent-used-to-automate-attack-on-thai-finance-ministry/
- **Hackers hijack hotel Wi-Fi DNS to steal Microsoft 365 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-hijack-hotel-wi-fi-dns-to-steal-microsoft-365-accounts/
- **Microsoft blames massive Microsoft 365 outage on maintenance bug**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-blames-massive-microsoft-365-outage-on-maintenance-bug/
- **BlueNoroff Zoom Phishing Kit Profiles Crypto Wallets Before Malware Delivery**: The Hacker News - https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html
- **Certighost Exploit Lets Low-Privileged Active Directory Users Impersonate a Domain Controller**: The Hacker News - https://thehackernews.com/2026/07/certighost-exploit-lets-low-privileged.html
- **Chick-fil-A data breach affects more than 13,000 customers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/chick-fil-a-data-breach-affects-more-than-13-000-customers/
- **Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/
- **Vatican's Official Prayer App Leaks 700K+ Global Users' PII**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/vatican-official-prayer-app-leaks-700k-pii
- **Europol flags 4,340 URLs for removal in 'The Com' crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/europol-flags-4-340-urls-for-removal-in-the-com-crackdown/
- **Default Azure Automation Setting Enables Cross-Tenant Identity Takeover**: Dark Reading - https://www.darkreading.com/cloud-security/default-azure-automation-setting-cross-tenant-identity-takeover
- **ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link**: The Hacker News - https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
- **Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers**: The Hacker News - https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html
- **Seeing AI Agents Is Not Enough. Security Teams Must Enforce What They Can Do**: The Hacker News - https://thehackernews.com/2026/07/seeing-ai-agents-is-not-enough-security.html
- **Man gets six years for hacking 750 women's Snapchat accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/man-gets-six-years-for-hacking-750-womens-snapchat-accounts/
- **Hacker Runs Hermes AI Agent Unattended for Post-Exploitation at Thai Finance Ministry**: The Hacker News - https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html
- **Golden Chickens Resurfaces With Four New Malware Families and Modular Implants**: The Hacker News - https://thehackernews.com/2026/07/golden-chickens-resurfaces-with-four.html
- **NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats**: The Hacker News - https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
- **Clop ransomware targets Windchill, FlexPLM in data theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/
- **Europe's Multilingual Reality Exposes AI Security Gaps**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/europes-multilingual-reality-exposes-ai-security-gaps
- **Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit, Researchers Say**: The Hacker News - https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
- **Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks**: The Hacker News - https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html
