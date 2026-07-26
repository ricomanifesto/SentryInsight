# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors leveraging both novel techniques and unpatched vulnerabilities to compromise targets at scale. Ransomware affiliates linked to Cl0p are actively exploiting unauthenticated RCE flaws in internet-exposed PTC Windchill and FlexPLM deployments, while a critical Fastjson 1.x deserialization vulnerability remains unpatched and under active attack in Java Spring Boot applications. Simultaneously, researchers have published working exploit code for a GitLab RCE (patched six weeks prior) and the Certighost Active Directory privilege escalation, lowering the barrier for widespread abuse.

A significant shift in malware delivery is evident through "in-browser compilation" malvertising campaigns—dubbed SourTrade and related operations—that use legitimate runtimes like Bun and malicious JavaScript to assemble executables directly in victim browser memory, evading traditional network and endpoint inspections. ClickFix-style social engineering continues to proliferate, now appearing on Steam forums to deliver XMRig cryptominers and in North Korean BlueNoroff phishing kits that profile cryptocurrency wallets before payload deployment. Credential theft operations have evolved to include real-time account hijacking via phishing, DNS manipulation on hotel Wi-Fi networks targeting Microsoft 365, and large-scale credential stuffing against consumer brands.

Threat actors are increasingly weaponizing AI agents for offensive operations. The open-source Hermes AI agent was run in unattended "YOLO" mode to automate post-exploitation during an alleged breach of Thailand's Ministry of Finance, while a critical flaw in ChatGPT Workspace Agents (AgentForger) could have enabled rogue agent deployment via a single phishing link. Meanwhile, established MaaS and RaaS ecosystems—Golden Chickens and DevMan—are expanding with new modular malware families and centralized affiliate portals, signaling sustained industrialization of cybercrime.

## Active Exploitation Details

### Fastjson 1.x Critical RCE Vulnerability
- **Description**: A critical deserialization flaw in Fastjson 1.x, Alibaba's widely used JSON library for Java. In affected Spring Boot applications, a malicious JSON request can execute arbitrary code without authentication.
- **Impact**: Remote code execution leading to full server compromise, data exfiltration, and lateral movement within enterprise environments.
- **Status**: Actively exploited in the wild by multiple threat actors. No official patch is available for the 1.x branch; users are urged to migrate to Fastjson 2.x or apply mitigations such as disabling autoType support.

### GitLab Authenticated RCE (Self-Managed Instances)
- **Description**: A remote code execution vulnerability in GitLab self-managed instances that allows authenticated users to execute commands as the `git` system user.
- **Impact**: Authenticated attackers can achieve full control over the GitLab server, access repositories, modify code, and pivot to internal infrastructure.
- **Status**: GitLab patched the vulnerability on June 10. A working proof-of-concept exploit was publicly released on July 24 by depthfirst researchers, significantly increasing exploitation risk for unpatched instances version 18.11.3 and later.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Unauthenticated remote code execution vulnerabilities affecting internet-exposed deployments of PTC Windchill (PLM) and FlexPLM (retail PLM) software.
- **Impact**: Attackers can achieve initial access and execute arbitrary code without any credentials, enabling ransomware deployment, data theft, and persistence.
- **Status**: Actively exploited by Cl0p ransomware affiliates (also known as Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest) as part of their ongoing campaign targeting manufacturing and retail sectors.

### Certighost Active Directory Privilege Escalation
- **Description**: An exploit allowing low-privileged Active Directory users to obtain a certificate for a Domain Controller and authenticate as that machine account, effectively impersonating the DC.
- **Impact**: Full domain compromise—attackers gain Domain Admin equivalent rights, enabling credential theft, Group Policy modification, and persistent access across the AD forest.
- **Status**: Working exploit code published on July 24 by researchers H0j3n and Aniq Fakhrul. No patch information provided in source; mitigation requires AD CS configuration hardening and monitoring for anomalous certificate requests.

### SourTrade Malvertising / In-Browser Malware Assembly
- **Description**: A malvertising operation that delivers malware in fragments and uses the victim's browser—leveraging the legitimate Bun JavaScript runtime—to assemble the final Windows executable in memory.
- **Impact**: Bypasses network-based malware detection and traditional endpoint antivirus by never transmitting a complete malicious binary; delivers payloads such as information stealers and loaders.
- **Status**: Active campaign observed across malicious advertising networks; no patch applicable as technique abuses legitimate browser and runtime functionality.

### JavaScript In-Memory Malware Construction (Fake Solana/Luno/TradingView Pages)
- **Description**: A massive malvertising campaign using typosquatted cryptocurrency and trading platform pages that execute malicious JavaScript to assemble malware directly in browser memory.
- **Impact**: Fileless malware delivery evading disk-based scanning; final payloads include remote access trojans and credential stealers.
- **Status**: Ongoing campaign; defenders must rely on behavioral browser isolation, script blocking, and memory scanning.

### ClickFix Social Engineering (Steam Forums & BlueNoroff Kits)
- **Description**: Attackers post fake "fixes" for game or computer problems on Steam discussion forums and in typosquatted Zoom/Microsoft Teams phishing pages, tricking users into executing PowerShell commands that deploy malware.
- **Impact**: Delivery of XMRig cryptominers (Steam) and targeted credential theft/crypto wallet profiling followed by malware deployment (BlueNoroff).
- **Status**: Active across multiple platforms; user education and application control (blocking unauthorized PowerShell) are primary mitigations.

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Credential Theft
- **Description**: Attackers compromise hotel and conference center Wi-Fi infrastructure to modify DNS settings, redirecting victims to convincing fake Microsoft 365 login pages.
- **Impact**: Harvesting of corporate Microsoft 365 credentials, enabling business email compromise, data access, and further phishing.
- **Status**: Active campaign; mitigation requires DNS-over-HTTPS/TLS enforcement, certificate validation training, and MFA deployment.

### Hermes AI Agent Unattended Post-Exploitation
- **Description**: A threat actor deployed the open-source Hermes AI agent on a rented server, disabled its safety confirmation prompts ("YOLO" mode), and directed it to automate post-exploitation tasks against Thailand's Ministry of Finance.
- **Impact**: Automated, rapid post-exploitation including enumeration, lateral movement, and data collection without human operator latency.
- **Status**: Confirmed incident; highlights emerging risk of AI agents as offensive automation tools when safety controls are disabled.

### ChatGPT AgentForger Workspace Agent Vulnerability
- **Description**: A critical flaw in OpenAI's ChatGPT Workspace Agents that could allow a single phishing link to silently build, authorize, and deploy a rogue autonomous agent within a victim's workspace.
- **Impact**: Persistent, autonomous access to the victim's ChatGPT environment, enabling data exfiltration, social engineering, and further automation of attacks.
- **Status**: Disclosed by researchers; patch status not specified in source. Users should avoid clicking untrusted links and monitor workspace agent activity.

### Bing Images SVG RCE on Microsoft Infrastructure
- **Description**: Crafted SVG files submitted to Bing Image Search achieved remote code execution as `NT AUTHORITY\SYSTEM` on Windows image-processing workers and as `root` on Linux workers in Microsoft's production fleet.
- **Impact**: Potential compromise of Microsoft's internal image processing pipeline; demonstrates high-severity parser vulnerabilities in cloud services.
- **Status**: Reported by XBOW researchers; Microsoft remediation status not specified in source.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A default public configuration in Azure Automation combined with a chain of code flaws allowed attackers to seize another tenant's managed identity and access their data, credentials, and resources.
- **Impact**: Full cross-tenant compromise in multi-tenant Azure environments, bypassing isolation boundaries.
- **Status**: Microsoft addressed the configuration and code flaws; organizations should audit Azure Automation account settings and managed identity permissions.

### Golden Chickens MaaS Expansion
- **Description**: The Golden Chickens malware-as-a-service operators have released four new malware families with modular implants, expanding their MaaS portfolio.
- **Impact**: Provides affiliates with updated tooling for initial access, persistence, data theft, and ransomware deployment; indicates sustained operator investment.
- **Status**: Active development and distribution through underground markets.

### DevMan RaaS Portal Operations
- **Description**: The DevMan ransomware-as-a-service operation maintains a dedicated web platform for affiliates to build payloads, manage victims, track earnings, and handle payouts.
- **Impact**: Lowers barrier to ransomware deployment; professionalizes affiliate operations with centralized tooling.
- **Status**: Active RaaS platform; monitoring for DevMan payloads and infrastructure indicators recommended.

### ShinyHunters Data Leak-Fueled Sextortion
- **Description**: Threat actors are leveraging email addresses exposed in data breaches leaked by the ShinyHunters extortion group to send sextortion emails demanding $2,000 in Bitcoin.
- **Impact**: Large-scale psychological and financial harm to breach victims; demonstrates downstream abuse of stolen data.
- **Status**: Active campaign; recipients should ignore demands, enable MFA, and monitor for credential reuse.

### Chick-fil-A Credential Stuffing Breach
- **Description**: Credential stuffing attacks against Chick-fil-A's website and mobile app between June 17–19 compromised over 13,000 customer accounts.
- **Impact**: Account takeover, potential payment card exposure, loyalty point theft, and credential reuse risk across other services.
- **Status**: Confirmed breach; Chick-fil-A forced password resets and notified affected customers.

### OnTrac Network Intrusion and Data Breach
- **Description**: Hackers breached OnTrac's corporate network, potentially accessing customer personal details.
- **Impact**: Exposure of customer PII; risk of identity theft and targeted phishing.
- **Status**: Ongoing investigation; notification letters sent to potentially affected individuals.

### Vatican Prayer App API Data Leak
- **Description**: A porous API endpoint in the Vatican's official prayer app exposed names, email addresses, country, and site status for over 700,000 global users.
- **Impact**: Mass PII exposure enabling phishing, credential stuffing, and profiling.
- **Status**: Data accessible via browser; remediation status not specified in source.

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON library for Java)**: All 1.x versions in Spring Boot applications with default deserialization settings; no patched 1.x release available.
- **GitLab Self-Managed**: Versions 18.11.3 and later prior to the June 10 security release; GitLab.com SaaS not affected.
- **PTC Windchill (PLM)**: Internet-exposed deployments; specific versions not disclosed in source.
- **PTC FlexPLM (Retail PLM)**: Internet-exposed deployments; specific versions not disclosed in source.
- **Microsoft Active Directory / AD CS**: Environments with vulnerable certificate template configurations enabling Certighost exploitation.
- **Bun JavaScript Runtime**: Legitimate runtime abused by SourTrade campaign for in-browser executable assembly.
- **Steam Discussion Forums**: Platform abused for ClickFix social engineering post distribution.
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on routers/access points hijacked for credential phishing.
- **Microsoft 365 / Entra ID**: Target of credential harvesting via fake login pages.
- **Hermes AI Agent (Open Source)**: Deployed in unattended mode for offensive automation.
- **ChatGPT Workspace Agents**: Vulnerable to AgentForger phishing-based rogue agent deployment.
- **Bing Image Search / Microsoft Production Image Processing Fleet**: Windows (SYSTEM) and Linux (root) workers processing SVG uploads.
- **Azure Automation Accounts**: Default public configuration enabling cross-tenant managed identity takeover.
- **Golden Chickens MaaS Payloads**: Four new malware families distributed to affiliates.
- **DevMan RaaS Platform**: Web portal for ransomware affiliate operations.
- **Chick-fil-A Website & Mobile App**: Targeted by credential stuffing June 17–19.
- **OnTrac Corporate Network**: Breached by unauthorized actors.
- **Vatican Official Prayer App (Click To Pray)**: API endpoint exposing 700K+ user records.

## Attack Vectors and Techniques

- **In-Browser Malware Assembly (SourTrade)**: Malware delivered in fragments; victim's browser uses Bun runtime to compile final executable in memory, evading network and static file detection.
- **JavaScript In-Memory Malware Construction**: Malicious JavaScript on typosquatted pages assembles payloads directly in browser memory; fileless delivery defeats disk-based AV.
- **ClickFix Social Engineering**: Fake error messages and "fixes" trick users into copying/executing PowerShell commands; leverages trust in platform (Steam) or brand (Zoom, Teams).
- **Unauthenticated RCE Exploitation (Fastjson, PTC Windchill/FlexPLM, GitLab, Bing Images)**: Direct exploitation of deserialization, parser, and command injection flaws without credentials.
- **Active Directory Certificate Services Abuse (Certighost)**: Low-priv user requests DC certificate via vulnerable template; uses machine account authentication for domain compromise.
- **DNS Hijacking on Public Wi-Fi**: Compromise of router/AP DNS settings to redirect legitimate domains to phishing pages; targets travelers and conference attendees.
- **AI Agent Offensive Automation (Hermes)**: Disabling safety controls ("YOLO" mode) to run AI agent unattended for post-exploitation tasks.
- **Phishing-Based Rogue Agent Deployment (AgentForger)**: Single malicious link triggers autonomous agent creation/authorization in victim's ChatGPT workspace.
- **Credential Stuffing**: Automated login attempts using breached credential pairs against Chick-fil-A consumer platform.
- **Malvertising / Typosquatting**: Fake cryptocurrency/trading sites (Solana, Luno, TradingView) and Zoom/Teams domains used to deliver malicious scripts.
- **Data Leak Downstream Abuse (ShinyHunters)**: Stolen email databases reused for sextortion campaigns.
- **RaaS/MaaS Affiliate Enablement (DevMan, Golden Chickens)**: Centralized portals and modular malware lower skill barrier for affiliates.
- **Supply Chain / Dependency Trust Exploitation (Slopsquatting/HalluSquatting)**: AI hallucinated package/domain names registered by attackers and pulled by AI coding agents.

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Actively exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM for ransomware deployment; ongoing campaign targeting manufacturing and retail.
- **BlueNoroff (North Korean APT)**: Operating ClickFix-style phishing kits on typosquatted Zoom and Microsoft Teams domains; profiling cryptocurrency wallets before delivering malware; linked to financial crime and crypto theft.
- **ShinyHunters**: Extortion group leaking breached databases; data reused by downstream actors for sextortion campaigns demanding $2,000 in Bitcoin.
- **Golden Chickens Operators**: MaaS providers resurfacing with four new modular malware families; continuing affiliate distribution model.
- **DevMan RaaS Operators**: Maintaining centralized affiliate portal for payload building, victim management, and payout processing; professionalizing ransomware operations.
- **Hermes AI Agent Operator (Unattributed)**: Deployed Hermes in unattended mode against Thailand's Ministry of Finance; demonstrates AI-assisted post-exploitation.
- **SourTrade Malvertising Operators (Unattributed)**: Running in-browser compilation malvertising campaign using Bun runtime.
- **JavaScript In-Memory Malware Campaign Operators (Unattributed)**: Large-scale malvertising via fake Solana, Luno, TradingView pages.
- **Steam Forum ClickFix Actors (Unattributed)**: Abusing Steam discussions to deliver XMRig cryptominers via social engineering.
- **Hotel Wi-Fi DNS Hijackers (Unattributed)**: Targeting hospitality sector infrastructure for Microsoft 365 credential harvesting.
- **Credential Stuffing Actors (Unattributed)**: Targeted Chick-fil-A June 17–19 using breached credential lists.
- **OnTrac Intrusion Actors (Unattributed)**: Breached corporate network; data access scope under investigation.

## Source Attribution

- **GitHub, PyPI add time-absed defenses against supply chain attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/github-pypi-add-time-absed-defenses-against-supply-chain-attacks/
- **Steam forum ClickFix attacks infect gamers with XMRig cryptominers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/steam-forum-clickfix-attacks-infect-gamers-with-xmrig-cryptominers/
- **Malvertising Sends Malware in Pieces, Then Makes the Browser Build the Executable**: The Hacker News - https://thehackernews.com/2026/07/malvertising-sends-malware-in-pieces.html
- **Malicious sites use JavaScript to build malware in browser memory**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/malicious-sites-use-javascript-to-build-malware-in-browser-memory/
- **ShinyHunters data leaks fuel $2,000 sextortion email scam**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/shinyhunters-data-leaks-fuel-2-000-sextortion-email-scam/
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
