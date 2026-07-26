# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are targeting diverse attack surfaces ranging from developer tools and enterprise software to consumer platforms and AI systems. The Cl0p ransomware operation's affiliates are exploiting unauthenticated RCE vulnerabilities in internet-exposed PTC Windchill and FlexPLM deployments, while a critical Fastjson 1.x deserialization flaw in Java applications remains unpatched and actively targeted. Simultaneously, novel browser-based malware assembly techniques—exemplified by the SourTrade malvertising operation and massive campaigns using fake cryptocurrency and trading sites—are delivering payloads by instructing victims' browsers to construct executables in memory using legitimate runtimes like Bun.

Social engineering continues to evolve with ClickFix-style attacks compromising Steam forum users to deploy XMRig cryptominers, while North Korean BlueNoroff actors employ typosquatted videoconferencing domains and phishing kits that profile cryptocurrency wallets before malware delivery. Credential theft operations have escalated to real-time account hijacking via hotel Wi-Fi DNS manipulation targeting Microsoft 365 credentials, and credential stuffing waves hit Chick-fil-A customers. In the identity space, the Certighost exploit enables low-privileged Active Directory users to impersonate Domain Controllers, and a default Azure Automation configuration allowed cross-tenant identity takeover. AI-assisted attacks are emerging, with threat actors leveraging the Hermes AI agent in unattended mode for post-exploitation against Thailand's Ministry of Finance, while Golden Chickens MaaS operators deploy four new modular malware families.

## Active Exploitation Details

### Fastjson 1.x RCE Vulnerability
- **Description**: A critical deserialization flaw in Alibaba's Fastjson JSON library for Java that allows remote code execution via malicious JSON requests in affected Spring Boot applications
- **Impact**: Attackers can execute arbitrary code on the server by sending crafted JSON payloads, leading to full application server compromise
- **Status**: Actively exploited in the wild with no patch currently available from the vendor; security firms ThreatBook and Imperva confirm ongoing targeting

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Unauthenticated remote code execution vulnerabilities in internet-exposed deployments of PTC Windchill (PLM software) and FlexPLM
- **Impact**: Attackers gain initial access to enterprise PLM systems without authentication, enabling data theft, lateral movement, and ransomware deployment
- **Status**: Actively exploited by Cl0p ransomware affiliates as part of their current campaign; internet-exposed instances are primary targets

### GitLab RCE (Patched June 10, PoC Published July 24)
- **Description**: A vulnerability in GitLab self-managed instances that allows authenticated users to execute commands as the `git` user on the underlying system
- **Impact**: Authenticated attackers can run arbitrary commands with the privileges of the GitLab service account, potentially leading to source code theft, supply chain compromise, and lateral movement
- **Status**: Patched by GitLab on June 10; working proof-of-concept exploit code published by depthfirst researchers on July 24, increasing exploitation risk for unpatched instances
- **CVE ID**: Not specified in source article

### Certighost Active Directory Exploit
- **Description**: An exploit allowing low-privileged Active Directory users to obtain a certificate for a Domain Controller and authenticate as that machine account
- **Impact**: Privilege escalation from standard domain user to Domain Controller-level access, enabling full domain compromise, credential theft, and persistence
- **Status**: Working exploit code published on July 24 by researchers H0j3n and Aniq Fakhrul; active exploitation likely given public PoC availability
- **CVE ID**: Not specified in source article

### ChatGPT AgentForger Workspace Agents Vulnerability
- **Description**: A critical flaw in OpenAI's ChatGPT Workspace Agents that could allow a single phishing link to stealthily build, authorize, and deploy rogue autonomous agents
- **Impact**: Attackers could deploy persistent AI agents with access to the victim's workspace, data, and connected tools without user interaction beyond clicking a link
- **Status**: Disclosed by cybersecurity researchers; patch status not specified in source
- **CVE ID**: Not specified in source article

### Bing Images SVG Processing Flaw
- **Description**: Crafted SVG files submitted to Bing's image search execute commands as `NT AUTHORITY\SYSTEM` on Microsoft's Windows production image-processing workers and as `root` on Linux machines in the same fleet
- **Impact**: Remote code execution on Microsoft's infrastructure with highest system privileges, potentially enabling access to internal systems and data
- **Status**: Demonstrated by XBOW researchers; Microsoft response not detailed in source
- **CVE ID**: Not specified in source article

### NodeBB Forum Software Vulnerabilities (Eight Flaws)
- **Description**: Eight high-severity security flaws in NodeBB forum software discovered by AI pentest agents, exposing admin access and private chats
- **Impact**: Attackers can gain administrative control over forums, access private messages, and compromise user data
- **Status**: Patched by NodeBB; exploit code published alongside disclosure on July 24 by Aikido Security
- **CVE ID**: Not specified in source article

### Steam Forum ClickFix Campaign
- **Description**: Attackers abuse Steam discussion forums to post fake "fixes" for game and computer problems that actually deliver XMRig cryptominers via ClickFix social engineering
- **Impact**: Gamers' systems infected with cryptocurrency mining malware, consuming resources and potentially enabling further payload delivery
- **Status**: Active campaign observed on Steam forums; no software vulnerability—pure social engineering exploitation

### SourTrade Malvertising / Browser-Assembled Malware
- **Description**: Malvertising operation delivering malware in pieces and using victims' browsers to build the final Windows executable via the legitimate Bun JavaScript runtime
- **Impact**: Evasion of traditional network and endpoint detection by assembling payloads client-side; delivers final executable without serving malicious binaries directly
- **Status**: Active campaign dubbed "SourTrade" observed in the wild

### Fake Crypto/Trading Site Malvertising Campaign
- **Description**: Massive malvertising campaign using fake Solana, Luno, and TradingView webpages with malicious JavaScript that instructs browsers to assemble malware directly in memory
- **Impact**: Fileless malware execution in browser memory, bypassing disk-based detection; targets cryptocurrency users and traders
- **Status**: Active large-scale campaign observed

### BlueNoroff Phishing Kit with Crypto Wallet Profiling
- **Description**: North Korean threat actors operate a phishing kit impersonating Zoom and Microsoft Teams via typosquatted domains that profiles victims' cryptocurrency wallets before delivering malware
- **Impact**: Targeted credential theft and malware delivery focused on cryptocurrency holders; combines ClickFix-style social engineering with wallet reconnaissance
- **Status**: Active phishing kit operation observed

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Credential Theft
- **Description**: Attackers modify DNS settings on hotel and conference center Wi-Fi devices to redirect users to fake Microsoft 365 login pages
- **Impact**: Harvesting of Microsoft 365 credentials from traveling professionals; enables business email compromise and further intrusion
- **Status**: Active attacks reported at hotels and conference centers

### Hermes AI Agent Automated Post-Exploitation
- **Description**: Threat actor deployed the open-source Hermes AI agent in unattended "YOLO" mode (auto-approving risky commands) to automate post-exploitation activity against Thailand's Ministry of Finance
- **Impact**: AI-accelerated post-exploitation including reconnaissance, lateral movement, and data staging without continuous operator attention
- **Status**: Observed in alleged breach of Thai Finance Ministry; demonstrates emerging AI-assisted attack methodology

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON library for Java)**: Spring Boot applications using vulnerable Fastjson versions; no patched version available
- **PTC Windchill and FlexPLM**: Internet-exposed deployments of PTC's Product Lifecycle Management software; all unpatched versions susceptible
- **GitLab Self-Managed**: Versions 18.11.3 and later prior to June 10 patch; Community and Enterprise editions affected
- **Microsoft Active Directory**: Domain environments with Active Directory Certificate Services; low-privileged users can exploit Certighost
- **Azure Automation**: Tenants with default public configuration enabling cross-tenant identity takeover chains; addressed by Microsoft
- **OpenAI ChatGPT Workspace Agents**: Workspace Agents feature vulnerable to AgentForger phishing-based rogue agent deployment
- **Microsoft Bing Image Processing Infrastructure**: Production workers processing SVG uploads; Windows (SYSTEM) and Linux (root) hosts affected
- **NodeBB Forum Software**: All versions prior to July 24 security release; eight high-severity flaws affecting admin panels and private messaging
- **Steam Discussion Forums**: Platform abused for ClickFix social engineering delivery; no software vulnerability in Steam itself
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network devices hijacked to serve phishing pages
- **Thailand Ministry of Finance Systems**: Targeted by Hermes AI agent automated post-exploitation; specific systems not detailed
- **Chick-fil-A Website and Mobile App**: Credential stuffing attacks against customer accounts June 17-19
- **OnTrac Corporate Network**: Parcel delivery company network breached; customer personal details potentially accessed
- **Vatican Official Prayer App (Click To Pray)**: Porous API endpoint exposing 700K+ users' PII including names, emails, countries, and site status

## Attack Vectors and Techniques

- **Browser-Assembled Malware (SourTrade)**: Malware delivered in fragments; victim's browser uses legitimate Bun runtime to compile final executable in memory, evading network inspection and static file analysis
- **In-Browser Memory Malware Construction**: Malicious JavaScript on fake cryptocurrency/trading sites assembles payloads directly in browser memory (fileless), leveraging WebAssembly and JavaScript engines
- **ClickFix Social Engineering**: Fake error messages and "fixes" on trusted platforms (Steam forums, typosquatted Zoom/Teams domains) trick users into executing PowerShell commands that deploy malware
- **Unauthenticated RCE via Deserialization**: Fastjson and PTC Windchill/FlexPLM exploits leverage deserialization flaws in internet-accessible services for initial access without credentials
- **Certificate-Based AD Privilege Escalation (Certighost)**: Low-privileged users request certificates for Domain Controller machine accounts, then authenticate as DC via PKINIT for full domain compromise
- **AI-Agent-Automated Post-Exploitation**: Hermes AI agent configured in unattended mode executes post-exploitation tasks (recon, enumeration, data collection) autonomously
- **DNS Hijacking on Public Wi-Fi**: Attackers compromise hotel/conference center network devices to poison DNS, redirecting Microsoft 365 authentication to credential harvesting pages
- **Typosquatted Videoconferencing Domains**: BlueNoroff registers domains mimicking Zoom and Microsoft Teams to deliver phishing kits that profile crypto wallets pre-exploitation
- **Credential Stuffing at Scale**: Automated login attempts using breach-derived credentials against Chick-fil-A customer accounts over 48-hour window
- **Malvertising via Fake Brand Pages**: Threat actors create convincing replicas of Solana, Luno, and TradingView sites served through ad networks to reach targeted demographics
- **RaaS/MaaS Platform Operations**: DevMan ransomware portal and Golden Chickens malware-as-a-service provide affiliates with payload builders, victim management, and modular implants (four new families)
- **Supply Chain / Developer Targeting**: NodeBB flaws expose admin access; GitLab RCE targets source code repositories; Fastjson hits Java build pipelines

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM as initial access vector for ransomware operations; ongoing campaign targeting enterprise PLM deployments
- **BlueNoroff (North Korean State-Sponsored)**: Operating ClickFix-style campaigns with typosquatted Zoom/Teams domains; maintaining active phishing kit that profiles cryptocurrency wallets before delivering malware; targeting crypto holders and organizations
- **ShinyHunters (Extortion Group)**: Data breaches leaked by this group fuel sextortion email campaigns demanding $2,000 in Bitcoin; breached datasets used for credential reuse and social engineering
- **Golden Chickens Operators (MaaS)**: Resurfaced with four new malware families and modular implants; providing affiliates with updated tooling for diverse intrusion scenarios
- **DevMan RaaS Operators**: Maintaining centralized web portal for affiliates featuring payload building, victim management, earnings tracking, and payout automation
- **Hermes AI Agent Operator (Unattributed)**: Deployed Hermes AI agent in unattended mode against Thailand's Ministry of Finance; demonstrates AI-assisted post-exploitation tradecraft
- **Certighost Researchers (H0j3n and Aniq Fakhrul)**: Published working exploit for AD certificate abuse on July 24; enabling widespread privilege escalation capability
- **depthfirst Researchers**: Published GitLab RCE PoC on July 24, six weeks after vendor patch; accelerating exploitation timeline for unpatched instances
- **Aikido Security (AI Pentest)**: Discovered eight high-severity NodeBB flaws using AI pentest agents in six-hour run; coordinated disclosure with exploit code release
- **XBOW Researchers**: Demonstrated Bing Images SVG flaw achieving SYSTEM/root RCE on Microsoft production infrastructure
- **Credential Stuffing Operators (Unattributed)**: Automated attacks against Chick-fil-A customer accounts June 17-19, compromising 13,000+ accounts
- **OnTrac Network Intruders (Unattributed)**: Breached corporate network of parcel delivery company; accessed customer personal details
- **Hotel Wi-Fi Attackers (Unattributed)**: Compromising network infrastructure at hotels and conference centers for DNS-based Microsoft 365 phishing
- **Snapchat Account Hacker (Convicted Individual)**: Illinois man sentenced to 76 months for hacking 750+ women's Snapchat accounts to steal nude photos via credential theft

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
