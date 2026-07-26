# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are underway across diverse vectors, ranging from supply chain and software vulnerability exploitation to social engineering and AI-assisted attacks. The Cl0p ransomware affiliates are actively targeting internet-exposed PTC Windchill and FlexPLM instances with unauthenticated remote code execution, while a critical Fastjson 1.x RCE vulnerability is being exploited in the wild with no patch currently available. Simultaneously, malvertising operations such as SourTrade have evolved to deliver malware in fragments that victims' browsers reassemble using legitimate runtimes, and ClickFix-style social engineering continues to spread cryptominers through gaming forums and typosquatted collaboration platforms.

Threat actors are increasingly leveraging legitimate tools and AI agents to automate post-exploitation activity. The Hermes AI agent was deployed in unattended mode against Thailand's Ministry of Finance, while North Korean BlueNoroff operators employ sophisticated phishing kits that profile cryptocurrency wallets before payload delivery. Golden Chickens malware-as-a-service has resurfaced with four new modular families, and the DevMan ransomware-as-a-service platform demonstrates continued maturation of criminal infrastructure. Credential theft campaigns have escalated to real-time account hijacking, with hotel Wi-Fi DNS manipulation and sextortion schemes fueled by ShinyHunters breach data.

Several high-impact vulnerabilities have been disclosed with proof-of-concept code, including a GitLab RCE (patched six weeks prior to PoC release), the Certighost Active Directory privilege escalation, a ChatGPT AgentForger flaw enabling rogue workspace agent deployment, and Bing Images processing flaws allowing SYSTEM-level command execution via crafted SVGs. Azure Automation's default configuration was found to enable cross-tenant identity takeover, while AI hallucination-driven supply chain attacks—slopsquatting, phantom domains, and HalluSquatting—represent an emerging class of dependency confusion threats.

## Active Exploitation Details

### Fastjson 1.x Remote Code Execution
- **Description**: A critical flaw in Fastjson, Alibaba's JSON library for Java, allows malicious JSON requests to execute arbitrary code in affected Spring Boot applications. The vulnerability stems from unsafe deserialization behavior in the 1.x branch.
- **Impact**: Attackers achieve remote code execution on servers running vulnerable Fastjson versions, enabling full system compromise, data theft, and lateral movement.
- **Status**: Actively exploited in the wild by threat actors. No patch is available for the 1.x branch as of the reporting period; users are advised to upgrade to Fastjson 2.x or implement mitigations.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Unauthenticated remote code execution vulnerabilities in PTC Windchill and FlexPLM product lifecycle management software exposed to the internet.
- **Impact**: Attackers gain full control over affected PLM systems without authentication, enabling intellectual property theft, supply chain compromise, and ransomware deployment.
- **Status**: Actively exploited by Cl0p ransomware affiliates as part of their ongoing campaign. Patches may be available from the vendor; internet-exposed instances remain at high risk.

### GitLab Remote Code Execution (Patched)
- **Description**: A flaw in GitLab self-managed instances allows authenticated users to execute arbitrary commands as the `git` user. The vulnerability affects versions prior to the June 10 patch.
- **Impact**: Authenticated attackers—including compromised developer accounts—can run commands on the GitLab server, potentially accessing source code, secrets, and CI/CD pipelines.
- **Status**: Patched on June 10. A working proof-of-concept exploit was published on July 24, increasing risk for unpatched instances.

### Certighost Active Directory Privilege Escalation
- **Description**: An exploit allowing low-privileged Active Directory users to obtain a certificate for a Domain Controller and authenticate as that machine account.
- **Impact**: Attackers escalate from standard domain user to Domain Controller-level privileges, enabling full domain compromise, credential theft, and persistence.
- **Status**: Working exploit published on July 24 by researchers H0j3n and Aniq Fakhrul. Mitigation requires AD CS configuration hardening and monitoring for anomalous certificate requests.

### ChatGPT AgentForger Workspace Agent Deployment
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents that allows a single phishing link to stealthily build, authorize, and deploy autonomous agents within a victim's workspace.
- **Impact**: Attackers gain persistent, automated access to the victim's ChatGPT workspace, enabling data exfiltration, further social engineering, and potential API abuse.
- **Status**: Disclosed by cybersecurity researchers; patch status from OpenAI not specified in source material.

### Bing Images SVG Remote Code Execution
- **Description**: Crafted SVG files submitted to Bing's image search execute commands as `NT AUTHORITY\SYSTEM` on Microsoft's production image-processing workers (Windows) and as `root` on Linux machines in the same fleet.
- **Impact**: Remote code execution on Microsoft's internal infrastructure with high privileges, demonstrating a critical flaw in image processing pipeline sandboxing.
- **Status**: Demonstrated by XBOW researchers; remediation status not specified in source material.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A public-by-default configuration in Azure Automation combined with a chain of code flaws allows attackers to seize another tenant's identity and access their data, credentials, and resources.
- **Impact**: Cross-tenant compromise in multi-tenant Azure environments, enabling unauthorized access to subscription resources, managed identities, and automation assets.
- **Status**: Microsoft has addressed the configuration default and underlying flaws; tenants should review Azure Automation configurations.

### ClickFix Social Engineering (Steam Forums)
- **Description**: Attackers abuse Steam discussion forums to post fake "fixes" for game and computer problems that instruct victims to run malicious PowerShell commands, installing XMRig cryptominers.
- **Impact**: Victims' systems are enrolled in cryptomining botnets, consuming resources and potentially enabling additional payload delivery.
- **Status**: Active campaign ongoing; relies on user interaction rather than software vulnerability.

### BlueNoroff Zoom Phishing Kit
- **Description**: North Korean threat actors operate a phishing kit impersonating Zoom and Microsoft Teams via typosquatted domains that profiles victims' cryptocurrency wallets before delivering malware.
- **Impact**: Targeted theft of cryptocurrency assets and credentials from individuals and organizations in the crypto and finance sectors.
- **Status**: Active campaign; kit includes wallet profiling logic to maximize theft efficiency.

### SourTrade Malvertising (Browser-Assembled Malware)
- **Description**: A malvertising operation delivers malware in fragments that victims' browsers reassemble into a Windows executable using the legitimate Bun JavaScript runtime, evading traditional payload inspection.
- **Impact**: Stealthy malware delivery that bypasses network and endpoint controls expecting complete executable payloads; final payload capabilities not fully detailed.
- **Status**: Active campaign dubbed "SourTrade"; leverages legitimate runtime to avoid detection.

### Browser Memory Malware Assembly (Fake Solana/Luno/TradingView)
- **Description**: Massive malvertising campaign uses fake cryptocurrency and trading platform webpages with malicious JavaScript that instructs browsers to assemble malware directly in memory.
- **Impact**: Fileless malware execution that avoids disk-based detection; targets users of Solana, Luno, and TradingView platforms for credential theft and financial fraud.
- **Status**: Active large-scale campaign; leverages brand trust in crypto/trading services.

### Hermes AI Agent Post-Exploitation Automation
- **Description**: A threat actor deployed the open-source Hermes AI agent in unattended "YOLO" mode (permission prompts disabled) on a rented server to automate post-exploitation activity against Thailand's Ministry of Finance.
- **Impact**: Accelerated and scalable post-exploitation including enumeration, lateral movement, and data collection without manual operator intervention.
- **Status**: Observed in alleged breach of Thai Finance Ministry; demonstrates emerging AI-assisted offensive capability.

### Golden Chickens Malware-as-a-Service Expansion
- **Description**: The Golden Chickens MaaS operators have resurfaced with four new malware families featuring modular implants, indicating continued development and affiliate support.
- **Impact**: Diversified malware portfolio available to affiliates for tailored intrusions; modular design enables flexible payload selection and evasion.
- **Status**: Active MaaS operation; new families observed in recent campaigns.

### DevMan Ransomware-as-a-Service Platform
- **Description**: DevMan RaaS operators maintain a dedicated web portal for affiliates to build payloads, manage victims, track earnings, and coordinate payouts.
- **Impact**: Lowers barrier to ransomware deployment; professionalized affiliate management increases attack volume and operational security for operators.
- **Status**: Active RaaS platform; represents maturation of ransomware ecosystem tooling.

### ShinyHunters Breach Data Sextortion
- **Description**: Threat actors use email addresses from data breaches leaked by the ShinyHunters extortion group to send sextortion emails demanding $2,000 in Bitcoin.
- **Impact**: Financial extortion and psychological harm to breach victims; demonstrates downstream abuse of stolen datasets.
- **Status**: Active campaign; fueled by continued ShinyHunters leak publications.

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Phishing
- **Description**: Attackers modify DNS settings on Wi-Fi devices at hotels and conference centers to redirect users to fake Microsoft 365 login pages.
- **Impact**: Credential theft from business travelers and conference attendees; bypasses network-level protections by compromising infrastructure upstream of victims.
- **Status**: Active technique; targets high-value victims in transient locations.

### Chick-fil-A Credential Stuffing
- **Description**: Credential stuffing attacks targeting Chick-fil-A's website and mobile app between June 17–19 compromised over 13,000 customer accounts.
- **Impact**: Account takeover, potential payment method abuse, and personal data exposure for affected customers.
- **Status**: Confirmed breach; attributed to credential reuse from prior breaches.

### AI Hallucination Supply Chain Attacks (Slopsquatting/Phantom Domains/HalluSquatting)
- **Description**: AI coding agents hallucinate package, repository, or domain names that attackers register to hijack dependencies—a late-binding attack pattern exploiting AI trust in generated identifiers.
- **Impact**: Supply chain compromise when developers or AI agents install attacker-controlled packages matching hallucinated names; affects software build pipelines.
- **Status**: Emerging attack class; ActiveState analysis confirms unified mechanism across slopsquatting, phantom domains, and HalluSquatting variants.

### Vatican Prayer App API Data Leak
- **Description**: A porous API endpoint in the Vatican's official prayer app exposes names, email addresses, countries, and site status for 700,000+ global users without authentication.
- **Impact**: Mass PII exposure enabling phishing, identity theft, and targeted social engineering against religious community members.
- **Status**: Vulnerable endpoint identified; remediation status not specified in source material.

### OnTrac Corporate Network Breach
- **Description**: Hackers breached OnTrac's corporate network and may have accessed customer personal details.
- **Impact**: Potential exposure of shipping and customer data; full scope under investigation.
- **Status**: Breach notification issued; forensic investigation ongoing.

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON library for Java)**: All 1.x versions in Spring Boot applications; no patch available, upgrade to 2.x required
- **PTC Windchill and FlexPLM**: Internet-exposed deployments of product lifecycle management software; specific versions not disclosed
- **GitLab Self-Managed**: Versions prior to June 10 patch (18.11.3 and earlier referenced in PoC context)
- **Active Directory Certificate Services (AD CS)**: Domains with vulnerable certificate template configurations enabling Certighost
- **ChatGPT Workspace Agents**: OpenAI's agent framework; vulnerability in agent authorization/deployment flow
- **Bing Image Processing Pipeline**: Microsoft's production image workers (Windows and Linux) processing SVG uploads
- **Azure Automation**: Tenants using default public configuration; cross-tenant identity features
- **Steam Discussion Forums**: Platform abused for ClickFix social engineering content hosting
- **Zoom/Microsoft Teams Typosquatted Domains**: Infrastructure used by BlueNoroff for phishing kit delivery
- **Bun JavaScript Runtime**: Legitimate runtime leveraged by SourTrade for in-browser malware assembly
- **Hermes AI Agent**: Open-source AI assistant; risk when deployed with safety controls disabled
- **Golden Chickens MaaS Implants**: Four new modular malware families; specific technical details not disclosed
- **DevMan RaaS Platform**: Web-based affiliate portal for ransomware payload building and management
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network devices vulnerable to unauthorized modification
- **Chick-fil-A Website and Mobile App**: Customer authentication systems targeted by credential stuffing
- **AI Coding Agents (GitHub Copilot, etc.)**: Tools that hallucinate package/domain names enabling slopsquatting
- **Vatican Prayer App (Click To Pray)**: Official mobile application with unauthenticated API endpoint
- **OnTrac Corporate Network**: Parcel delivery company internal systems

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Direct exploitation of internet-exposed applications (Fastjson, PTC Windchill/FlexPLM) without credentials
- **Authenticated RCE via Compromised Accounts**: GitLab exploitation requiring valid user session; Certighost requiring low-privileged AD access
- **Social Engineering - ClickFix**: Fake technical solutions tricking users into executing malicious commands (PowerShell) on their own systems
- **Phishing Kit with Dynamic Profiling**: BlueNoroff kit identifies cryptocurrency wallets before delivering tailored malware
- **Malvertising with Fragmented Payloads**: SourTrade delivers malware pieces reassembled by victim's browser using legitimate runtime (Bun)
- **Fileless In-Browser Malware Assembly**: JavaScript constructs executable in memory on fake brand pages (Solana, Luno, TradingView)
- **AI Agent Unattended Automation**: Hermes AI run in "YOLO" mode for hands-off post-exploitation at scale
- **Supply Chain - AI Hallucination Exploitation**: Attackers register packages/domains matching AI-hallucinated identifiers (slopsquatting, phantom domains, HalluSquatting)
- **DNS Hijacking at Network Edge**: Compromise of hotel/conference Wi-Fi DNS to redirect authentication traffic
- **Credential Stuffing**: Automated login attempts using breached credential pairs against Chick-fil-A services
- **Sextortion via Breach Data**: ShinyHunters leak data repurposed for Bitcoin extortion campaigns
- **Ransomware-as-a-Service Affiliate Management**: DevMan portal centralizes payload generation, victim tracking, and cryptocurrency payouts
- **Malware-as-a-Service Modular Expansion**: Golden Chickens releases four new families with pluggable implant architecture
- **Cross-Tenant Identity Confusion**: Azure Automation default settings allowing identity assumption across tenant boundaries
- **SVG-Based Code Execution**: Crafted vector graphics exploiting image processing pipeline to achieve SYSTEM/root RCE
- **Unauthenticated API Data Exposure**: Open API endpoint leaking 700K+ user records without access controls

## Threat Actor Activities

- **Cl0p Affiliates (aka Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest)**: Actively exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM deployments as part of ongoing ransomware campaign; leveraging PLM access for data theft and encryption
- **BlueNoroff (North Korean State-Sponsored)**: Operating sophisticated phishing kit with typosquatted Zoom/Teams domains; profiling cryptocurrency wallets before malware delivery; conducting ClickFix-style campaigns targeting finance and crypto sectors
- **ShinyHunters (Extortion Group)**: Leaking breach data that fuels downstream sextortion campaigns; $2,000 Bitcoin demands sent to exposed email addresses
- **Golden Chickens Operators (MaaS)**: Resurfaced with four new modular malware families; maintaining active malware-as-a-service ecosystem with affiliate distribution
- **DevMan RaaS Operators**: Running professionalized ransomware-as-a-service platform with web portal for payload building, victim management, earnings tracking, and affiliate payouts
- **Hermes AI Attacker (Unknown Operator)**: Deployed Hermes AI agent in unattended mode on rented infrastructure to automate post-exploitation against Thailand's Ministry of Finance; demonstrates AI-assisted offensive capability
- **SourTrade Malvertising Operators**: Running campaign that fragments malware for in-browser assembly via Bun runtime; evades traditional payload delivery detection
- **Browser Memory Malware Campaign (Unknown)**: Large-scale malvertising using fake Solana, Luno, and TradingView pages; JavaScript-based in-memory malware construction
- **Steam Forum ClickFix Actors (Unknown)**: Abusing Steam discussion forums to host fake fixes delivering XMRig cryptominers via PowerShell execution
- **Hotel Wi-Fi DNS Hijackers (Unknown)**: Compromising hospitality network infrastructure to redirect Microsoft 365 authentication to phishing pages
- **Chick-fil-A Credential Stuffers (Unknown)**: Automated credential stuffing against website and mobile app June 17–19; over 13,000 accounts compromised
- **Certighost Researchers (H0j3n and Aniq Fakhrul)**: Published working exploit for AD CS privilege escalation on July 24; enables low-privileged user to Domain Controller compromise
- **GitLab PoC Publishers (depthfirst researchers)**: Released working exploit code on July 24 for vulnerability patched June 10; increases risk for delayed patchers
- **XBOW Researchers**: Demonstrated Bing Images SVG RCE achieving SYSTEM/root on Microsoft production infrastructure; responsible disclosure implied

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
