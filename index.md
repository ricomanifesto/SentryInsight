# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are targeting diverse attack surfaces ranging from enterprise software and cloud infrastructure to AI-driven development workflows and consumer platforms. Critical unauthenticated remote code execution vulnerabilities in widely deployed enterprise applications—including Fastjson, PTC Windchill/FlexPLM, and GitLab—are being actively weaponized by ransomware affiliates and threat actors, with several flaws lacking available patches. Simultaneously, novel attack techniques are emerging that abuse legitimate browser capabilities and AI agents to assemble malware in memory, automate post-exploitation, and hijack identities across cloud tenants, signaling a shift toward fileless, infrastructure-agnostic intrusion methods.

Threat actor activity remains high across financially motivated and state-aligned groups. Cl0p affiliates continue exploiting internet-exposed enterprise software for initial access, while North Korean actors (BlueNoroff) refine ClickFix-style social engineering with crypto-targeted phishing kits. The Golden Chickens malware-as-a-service ecosystem has expanded with four new modular families, and the DevMan RaaS platform demonstrates increasing operational maturity. Notably, the first observed use of an AI agent (Hermes) in unattended "YOLO" mode for automated post-exploitation against a government ministry marks a significant evolution in offensive automation.

Credential theft and abuse remain pervasive, fueled by data breaches (ShinyHunters, OnTrac, Chick-fil-A) and novel vectors including hotel Wi-Fi DNS hijacking, malvertising campaigns that build executables in-browser via the Bun runtime, and AI-hallucinated package names (slopsquatting) entering software supply chains. Cloud identity flaws in Azure Automation and ChatGPT Workspace Agents further expand the attack surface for cross-tenant compromise and agent hijacking.

## Active Exploitation Details

### Fastjson 1.x Remote Code Execution
- **Description**: A critical deserialization flaw in Alibaba's Fastjson library for Java allows attackers to execute arbitrary code via malicious JSON requests in affected Spring Boot applications. The vulnerability stems from unsafe auto-type functionality that can be triggered through crafted JSON payloads.
- **Impact**: Unauthenticated remote code execution with the privileges of the application server, enabling full system compromise, data exfiltration, and lateral movement within enterprise environments.
- **Status**: Actively exploited in the wild by threat actors tracked by ThreatBook and Imperva. No official patch is available for Fastjson 1.x as of the reporting period; mitigation requires upgrading to Fastjson 2.x or implementing strict deserialization allowlists.

### GitLab Authenticated Remote Code Execution
- **Description**: A vulnerability in GitLab's self-managed instances (versions 18.11.3 and later) allows authenticated users to execute arbitrary commands as the `git` system user. The flaw was patched by GitLab on June 10, but a working proof-of-concept exploit was publicly released by researchers at depthfirst on July 24.
- **Impact**: Authenticated attackers can achieve remote code execution on the underlying GitLab server, potentially accessing source code, CI/CD pipelines, secrets, and infrastructure credentials.
- **Status**: Patch available since June 10. Public PoC increases exploitation risk for unpatched instances. Organizations running self-managed GitLab should prioritize immediate updating.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Flaws in internet-exposed deployments of PTC Windchill (PLM software) and FlexPLM allow unauthenticated remote code execution. Specific technical details of the vulnerabilities were not disclosed in the reporting.
- **Impact**: Complete compromise of PLM systems containing intellectual property, product designs, supply chain data, and manufacturing processes. Used as initial access vector for ransomware deployment.
- **Status**: Actively exploited by Cl0p ransomware affiliates. PTC has not been explicitly confirmed to have released patches in the source reporting; organizations should restrict internet exposure and monitor for vendor advisories.

### Certighost Active Directory Privilege Escalation
- **Description**: The Certighost exploit, published by researchers H0j3n and Aniq Fakhrul on July 24, enables a low-privileged Active Directory user to request and obtain a certificate for a Domain Controller machine account, then authenticate as that Domain Controller via Kerberos delegation.
- **Impact**: Full domain compromise from any standard user account. Attackers gain SYSTEM-level access on Domain Controllers, enabling credential theft, policy modification, and persistence across the AD forest.
- **Status**: Working exploit publicly available. Mitigation requires restricting certificate templates with dangerous EKUs (Client Authentication + Domain Controller), enforcing ESC1/ESC3 mitigations, and monitoring for anomalous certificate requests.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A default public configuration in Azure Automation combined with a chain of code flaws allows attackers to hijack another tenant's managed identity and access their data, credentials, and resources. The vulnerability stems from overly permissive default settings and insufficient cross-tenant validation.
- **Impact**: Cross-tenant compromise in multi-tenant Azure environments. Attackers can access victim tenants' automation accounts, runbooks, stored credentials, and any resources accessible via the compromised managed identity.
- **Status**: Microsoft has addressed the configuration and underlying code flaws. Organizations should review Azure Automation account network access settings and managed identity permissions.

### ChatGPT AgentForger Workspace Agent Hijacking
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents allows a single phishing link to stealthily build, authorize, and deploy a rogue agent within a victim's workspace without user interaction beyond clicking the link.
- **Impact**: Attackers gain persistent, authorized access to the victim's ChatGPT workspace, enabling data exfiltration from conversations, execution of agent actions (code execution, file access, API calls), and potential lateral movement to connected integrations.
- **Status**: Disclosed by cybersecurity researchers; patch status not specified in reporting. Users should exercise caution with unsolicited workspace invitation links.

### Bing Images SVG Remote Code Execution
- **Description**: Crafted SVG images submitted to Bing's image search are processed by Microsoft's production image-processing workers, resulting in arbitrary command execution as `NT AUTHORITY\SYSTEM` on Windows hosts and `root` on Linux hosts in the same fleet.
- **Impact**: Remote code execution on Microsoft's internal infrastructure with highest system privileges. Demonstrated by security research team XBOW; potential for supply chain compromise if build or deployment pipelines share infrastructure.
- **Status**: Reported to Microsoft; remediation status not specified in reporting. Highlights risks in complex image processing pipelines handling untrusted vector formats.

### NodeBB Multiple High-Severity Vulnerabilities
- **Description**: Eight security flaws discovered by Aikido Security's AI pentest agents in the NodeBB forum platform, exposing administrative access and private chat messages. All eight rated high severity with exploit code released publicly.
- **Impact**: Full administrative takeover of NodeBB instances, access to all user data and private communications, potential platform defacement, and credential harvesting.
- **Status**: Patches released by NodeBB maintainers concurrent with disclosure. Administrators should update immediately.

## Affected Systems and Products

- **Fastjson 1.x**: Alibaba JSON library for Java; all 1.x versions in Spring Boot applications using auto-type deserialization
- **GitLab Self-Managed**: Versions 18.11.3 and later prior to June 10 patch; Community and Enterprise editions
- **PTC Windchill**: Product Lifecycle Management software; internet-exposed deployments (specific versions not disclosed)
- **PTC FlexPLM**: Retail-focused PLM solution; internet-exposed deployments (specific versions not disclosed)
- **Microsoft Active Directory**: Domain environments with vulnerable certificate templates (ESC1/ESC3 configurations); all supported Windows Server versions
- **Azure Automation**: Accounts with default public network access configuration; all regions and tiers
- **ChatGPT Workspace Agents**: OpenAI ChatGPT workspaces with agent functionality enabled; specific versions not disclosed
- **Bing Image Processing Pipeline**: Microsoft production infrastructure processing user-submitted SVG images; Windows and Linux worker fleets
- **NodeBB Forum Platform**: Versions prior to July 2026 security release; all deployment types (self-hosted, cloud)
- **Steam Discussion Forums**: Valve's Steam platform community forums; abused as delivery platform (not a software vulnerability)
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network devices; vendor-agnostic
- **Vatican Click to Pray App**: Official prayer application API endpoint; iOS and Android versions

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers post fake "fixes" on trusted community platforms (Steam forums, typosquatted Zoom/Teams domains) that instruct victims to run malicious PowerShell commands via Windows Run dialog (`Win+R`), bypassing traditional email filters and endpoint defenses.
- **Browser-Native Malware Assembly (SourTrade)**: Malvertising campaign delivers malware in encrypted chunks; victim's browser uses legitimate Bun JavaScript runtime to decrypt, assemble, and execute a Windows PE executable entirely in memory—no file written to disk until execution.
- **JavaScript In-Memory Malware Construction**: Fake cryptocurrency (Solana, Luno) and trading (TradingView) webpages execute malicious JavaScript that reconstructs malware byte-by-byte in browser memory using `ArrayBuffer` and `WebAssembly`, then executes via exploited browser APIs or social engineering.
- **AI Agent Unattended Post-Exploitation (YOLO Mode)**: Threat actors deploy open-source AI agents (Hermes) on rented infrastructure with safety controls disabled, directing them to autonomously perform reconnaissance, credential access, lateral movement, and data staging against target networks (Thai Ministry of Finance).
- **DNS Hijacking via Compromised Network Infrastructure**: Attackers modify DNS settings on hotel/conference center Wi-Fi access points or routers to redirect Microsoft 365 authentication traffic to adversary-controlled phishing pages, capturing credentials and MFA tokens in real time.
- **Real-Time Phishing Account Hijacking**: Insurance-themed phishing evolves beyond credential collection to real-time session hijacking—attackers proxy victim authentication through attacker-controlled infrastructure, intercepting MFA challenges and establishing persistent sessions.
- **Slopsquatting / HalluSquatting**: AI coding assistants hallucinate non-existent package, repository, or domain names in generated code; attackers register these names and publish malicious packages or typosquatted domains, achieving supply chain compromise when developers or AI agents blindly trust the suggestions.
- **Credential Stuffing at Scale**: Automated injection of breached credential pairs (from ShinyHunters leaks, combo lists) against target authentication endpoints (Chick-fil-A, OnTrac, Snapchat) using distributed botnets and residential proxies.
- **Malvertising with Legitimate Runtimes**: Abuse of trusted software (Bun runtime) hosted on legitimate CDNs to execute malicious logic, evading reputation-based blocking and application allowlisting.
- **SVG-Based Server-Side Template Injection**: Crafted SVG files exploit insecure parsing in server-side image processing pipelines (Bing) to achieve command execution via XML external entity (XXE) or script execution vectors inherent in the SVG specification.

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Actively exploiting internet-exposed PTC Windchill and FlexPLM instances via unauthenticated RCE for initial access in ransomware campaigns. Demonstrates continued focus on enterprise PLM/ERP software as high-value targets.
- **BlueNoroff (North Korean State-Sponsored)**: Operating ClickFix-style campaigns using typosquatted Zoom and Microsoft Teams domains; deploying a phishing kit that profiles victim cryptocurrency wallets before delivering tailored malware. Combines social engineering with financial targeting consistent with DPRK revenue generation.
- **ShinyHunters (Extortion Group)**: Data breaches attributed to this group fuel large-scale sextortion campaigns demanding $2,000 in Bitcoin. Their leak site serves as a credential source for downstream threat actors.
- **Golden Chickens Operators (MaaS)**: Resurfaced with four new malware families (names not disclosed) featuring modular implants, indicating active development and affiliate recruitment. MaaS model lowers barrier for diverse intrusion campaigns.
- **DevMan RaaS Operators**: Maintain a dedicated web portal for affiliates providing payload building, victim management, earnings tracking, and payout automation—demonstrating RaaS operational maturity and professionalization.
- **Hermes AI Agent Operator (Unattributed)**: Deployed Hermes AI agent in unattended "YOLO" mode on rented server infrastructure targeting Thailand's Ministry of Finance. First documented case of autonomous AI agent used for post-exploitation; actor identity unknown.
- **Hotel Wi-Fi DNS Hijackers (Unattributed)**: Compromising network infrastructure at hospitality venues to intercept Microsoft 365 credentials; infrastructure-focused targeting suggests capability to access physical or administrative network controls.
- **Credential Stuffing Actors (Unattributed)**: Leveraging breached datasets (ShinyHunters leaks, combo lists) against consumer platforms (Chick-fil-A, OnTrac, Snapchat) with distributed automation; volume-focused monetization via account takeover and resale.
- **SourTrade Malvertising Operators (Unattributed)**: Running browser-native malware assembly campaign using Bun runtime; technical sophistication suggests developed capability, possibly affiliate-driven or direct operator.
- **XBOW Research Team**: Identified and demonstrated Bing Images SVG RCE on Microsoft production infrastructure; responsible disclosure observed.

## Source Attribution

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
- **NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats**: The Hacker News - https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
