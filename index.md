# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors leveraging both novel techniques and unpatched critical vulnerabilities. Social engineering remains a dominant initial access method, as evidenced by widespread ClickFix campaigns targeting Steam forum users and typosquatted Zoom/Teams domains deployed by North Korean actors. Simultaneously, a new class of malvertising attacks—SourTrade and related campaigns—is bypassing traditional payload delivery by instructing victims' browsers to assemble malware in memory using legitimate runtimes like Bun, evading static detection entirely.

Critical software vulnerabilities are being actively weaponized faster than patches can be deployed. The Fastjson 1.x RCE flaw is under active exploitation with no vendor patch available, while Cl0p affiliates are scanning for and exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM instances. In the identity and cloud layer, researchers have published working exploits for GitLab (patched but with public PoC), Active Directory (Certighost, allowing DC impersonation), Azure Automation (default configuration enabling cross-tenant takeover), and Bing Images (SVG-based RCE as SYSTEM/root). AI-assisted tooling is now appearing in post-exploitation, with the Hermes agent used in unattended mode against Thailand's Ministry of Finance, and AI pentesting agents discovering eight high-severity flaws in NodeBB.

## Active Exploitation Details

### ClickFix Social Engineering Campaigns
- **Description**: Attackers abuse legitimate platform features—Steam discussion forums and typosquatted Zoom/Microsoft Teams domains—to present fake "fixes" for game or system issues. Victims are tricked into copying and executing malicious PowerShell commands that deploy XMRig cryptominers or profile cryptocurrency wallets before delivering payloads.
- **Impact**: Arbitrary code execution on victim machines, cryptomining resource theft, cryptocurrency wallet enumeration and theft, and potential follow-on malware deployment.
- **Status**: Actively exploited in the wild across multiple campaigns. No software vulnerability to patch; mitigation requires user education and endpoint detection.

### SourTrade Malvertising (Browser-Assembled Malware)
- **Description**: A malvertising operation dubbed SourTrade delivers malicious JavaScript via fake Solana, Luno, and TradingView webpages. The script instructs the victim's browser to download legitimate Bun runtime components and assemble a Windows executable directly in memory, avoiding disk-based payload delivery.
- **Impact**: Evasion of traditional AV/EDR static scanning, arbitrary code execution, deployment of information stealers and remote access trojans.
- **Status**: Active large-scale campaign. No CVE; exploits browser capability to execute JavaScript and fetch resources.

### Fastjson 1.x Remote Code Execution
- **Description**: A critical deserialization flaw in Alibaba's Fastjson library for Java allows unauthenticated attackers to send malicious JSON requests that execute arbitrary code in affected Spring Boot applications.
- **Impact**: Full server compromise, data theft, lateral movement, ransomware deployment.
- **Status**: Actively exploited in the wild by multiple threat groups. **No patch available** for Fastjson 1.x line; mitigation requires upgrading to 2.x or applying WAF rules.

### GitLab RCE (Authenticated User to Command Execution)
- **Description**: A flaw in GitLab's self-managed instances (versions ≤ 18.11.3) allows authenticated users to execute arbitrary commands as the `git` system user. GitLab patched the vulnerability on June 10; a working PoC was published by depthfirst researchers on July 24.
- **Impact**: Command execution on GitLab server, source code theft, supply chain compromise, CI/CD pipeline manipulation.
- **Status**: Patched (June 10), but public PoC increases exploitation risk for unpatched instances.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Internet-exposed deployments of PTC Windchill and FlexPLM contain unauthenticated remote code execution vulnerabilities. Cl0p affiliates are actively scanning for and exploiting these instances.
- **Impact**: Initial access to enterprise PLM environments, data exfiltration, ransomware deployment, supply chain compromise.
- **Status**: Actively exploited by Cl0p affiliates. Patch status varies by deployment; internet exposure is a critical risk factor.

### Certighost Active Directory Privilege Escalation
- **Description**: The Certighost exploit allows a low-privileged Active Directory user to obtain a certificate for a Domain Controller and authenticate as that machine account, achieving full domain compromise.
- **Impact**: Domain administrator equivalence, persistent access, credential theft, lateral movement across the forest.
- **Status**: Working exploit published July 24 by researchers H0j3n and Aniq Fakhrul. Active exploitation expected.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A public-by-default configuration in Azure Automation combined with a chain of code flaws allows attackers to seize another tenant's identity and access their data, credentials, and resources.
- **Impact**: Cross-tenant data breach, credential theft, resource hijacking in multi-tenant Azure environments.
- **Status**: Microsoft has addressed the configuration and underlying flaws.

### ChatGPT AgentForger Workspace Agent Hijacking
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents allows a single phishing link to stealthily build, authorize, and deploy a rogue agent within a victim's workspace.
- **Impact**: Persistent AI agent with access to workspace data and tools, data exfiltration, automated malicious actions.
- **Status**: Disclosed by researchers; patch status not specified in article.

### Bing Images SVG Remote Code Execution
- **Description**: Crafted SVG files submitted to Bing's image search are processed by backend workers, achieving command execution as `NT AUTHORITY\SYSTEM` on Windows and `root` on Linux production image-processing fleets.
- **Impact**: Server compromise on Microsoft's infrastructure, potential supply chain impact on Bing search results.
- **Status**: Demonstrated by XBOW researchers; Microsoft response not detailed in article.

### NodeBB Forum Platform Vulnerabilities (Eight Flaws)
- **Description**: Eight high-severity security flaws in NodeBB forum software, discovered by Aikido Security's AI pentesting agents in a six-hour run, expose admin access and private chats. Exploit code was published alongside the disclosure.
- **Impact**: Administrative takeover, private message disclosure, user data compromise.
- **Status**: Patched by NodeBB; public exploit code available.

## Affected Systems and Products

- **Steam Discussion Forums**: Platform abused for ClickFix social engineering; all Steam users browsing forums at risk.
- **Windows Systems (General)**: Target of XMRig cryptominers via ClickFix; browser-assembled malware via SourTrade malvertising.
- **Java Applications using Fastjson 1.x**: Spring Boot and other Java applications using vulnerable Fastjson library; no patched version available for 1.x branch.
- **GitLab Self-Managed Instances (≤ 18.11.3)**: All self-hosted GitLab versions up to 18.11.3; patched in 18.11.4 and later.
- **PTC Windchill and FlexPLM**: Internet-exposed deployments; versions not specified; unauthenticated RCE exploited by Cl0p affiliates.
- **Active Directory Environments**: All domains with Active Directory Certificate Services (AD CS) and vulnerable certificate templates; Certighost exploit allows low-privileged user to DC compromise.
- **Microsoft Azure Automation**: Tenants with default public configuration; cross-tenant identity takeover chain addressed by Microsoft.
- **OpenAI ChatGPT Workspace Agents**: Workspace users vulnerable to AgentForger phishing link; affects enterprise and individual workspaces.
- **Microsoft Bing Image Processing Fleet**: Production workers (Windows and Linux) processing SVG uploads; RCE as SYSTEM/root demonstrated.
- **NodeBB Forum Installations**: All versions prior to security patch; eight high-severity flaws with public exploits.
- **Hotel and Conference Center Wi-Fi Infrastructure**: DNS settings on network devices hijacked to redirect Microsoft 365 authentication.

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers post fake solutions on trusted platforms (Steam forums, typosquatted Zoom/Teams domains) instructing victims to run PowerShell commands from clipboard. Bypasses traditional phishing defenses by leveraging user-initiated execution.
- **Browser-Assembled Malware (SourTrade)**: Malicious JavaScript fetches legitimate Bun runtime binaries and constructs a Windows executable in browser memory using WebAssembly and File API. No malicious file touches disk until execution; evades static signatures and sandbox analysis.
- **In-Browser Malware Assembly via JavaScript**: Fake cryptocurrency/trading sites execute multi-stage JavaScript that assembles payloads directly in memory, using browser APIs to allocate, write, and execute shellcode.
- **AI Agent Unattended Post-Exploitation**: Hermes AI agent run in "YOLO" mode (auto-approve risky commands) on rented infrastructure to automate reconnaissance, lateral movement, and data collection against Thai Ministry of Finance.
- **DNS Hijacking on Public Wi-Fi**: Attackers compromise hotel/conference center Wi-Fi device DNS settings to redirect Microsoft 365 login traffic to credential-harvesting pages. Targets traveling executives and conference attendees.
- **Credential Stuffing**: Automated injection of breached username/password pairs against Chick-fil-A website and mobile app; 13,000+ accounts compromised in three-day window.
- **Typosquatting with Phishing Kits**: BlueNoroff registers Zoom/Teams lookalike domains, hosts phishing kit that profiles victim's cryptocurrency wallets before delivering tailored malware.
- **SVG-Based Server-Side Code Execution**: Malicious SVG uploads to Bing Images exploit server-side rendering/processing flaws to achieve RCE as highest-privilege accounts on heterogeneous worker fleet.
- **Slopsquatting / HalluSquatting**: AI coding agents hallucinate package, repository, or domain names; attackers register these phantom identifiers to supply malicious code when developers or agents later request them.
- **AI-Assisted Vulnerability Discovery**: Aikido Security's AI pentest agents discovered eight high-severity NodeBB flaws in six hours, demonstrating offensive AI acceleration of exploit development.

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Actively scanning for and exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM deployments. Leveraging initial access for data theft and ransomware deployment. Persistent, well-resourced ransomware operation.

- **BlueNoroff (North Korean State-Sponsored)**: Operating ClickFix-style campaigns using typosquatted Zoom and Microsoft Teams domains. Deploying active phishing kit that enumerates cryptocurrency wallets before delivering malware. Focus on financial theft and crypto asset compromise.

- **ShinyHunters**: Extortion group responsible for data breaches whose leaked email databases fuel sextortion campaigns demanding $2,000 in Bitcoin. Data leaks enable downstream social engineering at scale.

- **Golden Chickens (MaaS Operators)**: Resurfaced with four new malware families and modular implants, indicating continued development and affiliate support. Malware-as-a-service ecosystem enabling diverse threat actors.

- **DevMan RaaS Operators**: Maintaining dedicated web portal for affiliates featuring payload building, victim management, earnings tracking, and payout automation. Professionalized ransomware-as-a-service operation.

- **Hermes AI Agent Operator (Unknown)**: Deployed open-source Hermes AI agent in unattended mode against Thailand's Ministry of Finance, automating post-exploitation activity. Demonstrates adoption of AI tooling for offensive operations.

- **Hotel Wi-Fi DNS Hijackers (Unknown)**: Compromising network infrastructure at hotels and conference centers to intercept Microsoft 365 credentials from high-value targets. Opportunistic, infrastructure-focused attack.

- **XBOW Researchers**: Demonstrated SVG-based RCE on Bing Images production infrastructure, achieving SYSTEM/root execution. Responsible disclosure context implied.

- **depthfirst Researchers**: Published working GitLab RCE PoC six weeks after patch release, accelerating exploitation timeline for unpatched instances.

- **H0j3n and Aniq Fakhrul**: Published Certighost exploit for Active Directory privilege escalation, enabling low-privileged to Domain Controller compromise.

- **Aikido Security AI Agents**: Discovered and disclosed eight high-severity NodeBB vulnerabilities via automated AI pentesting, releasing exploit code publicly.

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
