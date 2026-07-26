# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are targeting diverse platforms ranging from gaming communities and enterprise software to cloud infrastructure and AI systems. ClickFix social engineering attacks have migrated to Steam discussion forums, tricking gamers into executing malicious commands that deploy XMRig cryptominers. Simultaneously, sophisticated malvertising operations—SourTrade and a massive campaign using fake Solana, Luno, and TradingView pages—are leveraging legitimate browser runtimes and JavaScript to assemble malware directly in memory, evading traditional file-based detection.

Critical vulnerabilities in widely deployed enterprise and open-source software are being actively exploited with limited or no patch availability. Attackers are targeting an unpatched RCE in Fastjson 1.x affecting Spring Boot applications, while Cl0p ransomware affiliates exploit unauthenticated RCE flaws in internet-exposed PTC Windchill and FlexPLM deployments. A working exploit for a GitLab RCE (patched June 10) was publicly released on July 24, and the Certighost exploit enables low-privileged Active Directory users to impersonate domain controllers. Meanwhile, North Korean actors (BlueNoroff) operate a phishing kit profiling cryptocurrency wallets via typosquatted Zoom/Teams domains, and the Hermes AI agent has been weaponized in unattended mode for automated post-exploitation against Thailand's Ministry of Finance.

## Active Exploitation Details

### Steam Forum ClickFix Campaign
- **Description**: Threat actors abuse Steam discussion forums to post fake "fixes" for game and computer problems. These ClickFix-style lures trick users into copying and executing malicious PowerShell commands that download and run XMRig cryptominers.
- **Impact**: Victims' systems are enrolled in cryptocurrency mining operations, consuming CPU/GPU resources and increasing power costs while generating revenue for attackers.
- **Status**: Actively ongoing; no software vulnerability involved—relies entirely on social engineering. Steam users should avoid executing commands from forum posts.

### SourTrade Malvertising Operation
- **Description**: A malvertising campaign dubbed SourTrade delivers malware in fragments and uses the legitimate Bun JavaScript runtime within victims' browsers to assemble the final Windows executable on the fly, rather than serving a complete malicious binary.
- **Impact**: Evades static file scanning and network-based malware detection by constructing the payload client-side after the initial benign-looking script loads.
- **Status**: Active in the wild; leverages legitimate browser capabilities and a trusted runtime (Bun) to bypass defenses.

### Browser-Based Malware Assembly Campaign
- **Description**: A massive malvertising operation uses fake Solana, Luno, and TradingView webpages containing malicious JavaScript that instructs browsers to assemble malware directly in memory. No payload is written to disk during the initial stages.
- **Impact**: Fileless in-memory execution complicates forensic analysis and bypasses traditional antivirus solutions that rely on disk scanning.
- **Status**: Actively targeting users visiting compromised or typosquatted cryptocurrency and trading sites.

### Fastjson 1.x Remote Code Execution
- **Description**: A critical deserialization flaw in Fastjson (Alibaba's JSON library for Java) allows unauthenticated attackers to execute arbitrary code by sending a malicious JSON request to affected Spring Boot applications.
- **Impact**: Full server compromise, data theft, lateral movement, and potential ransomware deployment.
- **Status**: Actively exploited in the wild; **no patch is currently available** for Fastjson 1.x. Users must mitigate via WAF rules, input validation, or upgrading to Fastjson 2.x (which may require code changes).

### GitLab RCE (Patched, PoC Public)
- **Description**: An authenticated remote code execution vulnerability in self-managed GitLab instances (versions 18.11.3 and later) allows attackers to run commands as the `git` user. GitLab patched the flaw on June 10; researchers at depthfirst published a working proof-of-concept exploit on July 24.
- **Impact**: Compromise of source code repositories, CI/CD pipelines, and potential supply-chain attacks.
- **Status**: Patch available since June 10; public PoC increases exploitation risk for unpatched instances. Immediate upgrading is critical.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Cl0p ransomware affiliates are exploiting unauthenticated remote code execution vulnerabilities in internet-exposed PTC Windchill and FlexPLM deployments to gain initial access for ransomware operations.
- **Impact**: Full server takeover, data exfiltration, and ransomware deployment across victim networks.
- **Status**: Actively exploited by Cl0p affiliates (aka Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest). Organizations with internet-facing Windchill/FlexPLM instances should apply vendor patches immediately and restrict network exposure.

### Certighost Active Directory Exploit
- **Description**: Researchers H0j3n and Aniq Fakhrul published a working exploit (Certighost) on July 24 that allows a low-privileged Active Directory user to obtain a certificate for a Domain Controller and authenticate as that machine account, effectively achieving domain admin equivalence.
- **Impact**: Full domain compromise, persistence, and lateral movement across the Active Directory forest.
- **Status**: Exploit code publicly available; affects environments with vulnerable AD CS (Active Directory Certificate Services) configurations. Mitigation requires certificate template hardening and monitoring for anomalous enrollment.

### BlueNoroff Cryptocurrency Phishing Kit
- **Description**: North Korean threat actors (BlueNoroff) operate an active phishing kit that impersonates Zoom and Microsoft Teams via typosquatted domains. The kit profiles victims' cryptocurrency wallet extensions and balances before delivering tailored malware.
- **Impact**: Theft of cryptocurrency assets, credential harvesting, and malware installation targeting high-value individuals in crypto and finance sectors.
- **Status**: Active campaigns observed; ClickFix-style social engineering combined with wallet fingerprinting.

### Hermes AI Agent Post-Exploitation Automation
- **Description**: A threat actor deployed the open-source Hermes AI agent on a rented server, disabled its safety confirmation prompts ("YOLO" mode), and directed it to automate post-exploitation activity during an alleged breach of Thailand's Ministry of Finance.
- **Impact**: Accelerated and scaled post-exploitation operations including reconnaissance, credential access, and data exfiltration with minimal human operator involvement.
- **Status**: Demonstrated real-world use of AI agents for offensive automation; highlights emerging risk of "agentic" attack tooling.

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Credential Theft
- **Description**: Attackers compromise Wi-Fi infrastructure at hotels and conference centers to modify DNS settings, redirecting users to convincing fake Microsoft 365 login pages that harvest credentials.
- **Impact**: Corporate account compromise, business email compromise (BEC), and access to sensitive organizational data.
- **Status**: Active targeting of traveling professionals; users should verify certificate validity and use hardware security keys or phishing-resistant MFA.

### Bing Images SVG RCE on Microsoft Infrastructure
- **Description**: A crafted SVG submitted to Bing's image search achieved remote code execution as `NT AUTHORITY\SYSTEM` on Windows image-processing workers and as `root` on Linux machines in the same fleet. Discovered by XBOW during testing.
- **Impact**: Potential compromise of Microsoft's internal image-processing pipeline; demonstrates risk of complex parser logic in cloud services.
- **Status**: Reported and presumably remediated by Microsoft; highlights attack surface in file-format processing at scale.

### Golden Chickens MaaS Expansion
- **Description**: The Golden Chickens malware-as-a-service ecosystem has resurfaced with four new malware families and modular implants, indicating continued development and operator activity despite previous disruptions.
- **Impact**: Provides affiliates with updated tooling for initial access, persistence, data theft, and payload delivery across diverse victim environments.
- **Status**: Active development and distribution; monitoring for new variants and delivery campaigns is warranted.

### DevMan Ransomware-as-a-Service Portal
- **Description**: DevMan RaaS operators maintain a dedicated web platform enabling affiliates to build custom payloads, manage victims, track earnings, and coordinate payouts—streamlining the ransomware affiliate lifecycle.
- **Impact**: Lowers barrier to entry for ransomware operators; accelerates campaign deployment and monetization.
- **Status**: Platform actively maintained; reflects maturation of RaaS business models.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A default public configuration in Azure Automation combined with a chain of code flaws allowed attackers to seize another tenant's identity and access their data, credentials, and resources cross-tenant.
- **Impact**: Full compromise of victim Azure tenants, including subscription resources, managed identities, and stored secrets.
- **Status**: Microsoft has addressed the misconfiguration and underlying flaws; organizations should review Azure Automation account settings and identity permissions.

### ChatGPT AgentForger Workspace Agent Vulnerability
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents could allow a single phishing link to stealthily build, authorize, and deploy a rogue autonomous agent within a victim's workspace without user interaction beyond clicking the link.
- **Impact**: Persistent AI-driven access to workspace data, ability to execute actions as the user, and potential lateral movement via integrations.
- **Status**: Disclosed by researchers; OpenAI presumably remediated. Highlights emerging attack surface in AI agent ecosystems.

### NodeBB Forum Software Vulnerabilities
- **Description**: Eight high-severity security flaws in NodeBB forum software were disclosed with exploit code, discovered by Aikido Security's AI pentesting agents in a six-hour run. Flaws expose admin access and private chats.
- **Impact**: Full forum takeover, user data exposure, and potential pivot to connected systems.
- **Status**: Patched by NodeBB; administrators should update immediately.

## Affected Systems and Products

- **Steam Client & Web Platform**: Discussion forums abused for ClickFix lure distribution (all platforms)
- **Fastjson 1.x (Java JSON Library)**: Spring Boot applications using vulnerable versions; no patch available
- **GitLab Self-Managed**: Versions 18.11.3 and later prior to June 10 patch
- **PTC Windchill & FlexPLM**: Internet-exposed deployments with unauthenticated RCE flaws
- **Microsoft Active Directory**: Environments with vulnerable AD CS certificate templates (Certighost)
- **Bun JavaScript Runtime**: Legitimate runtime abused client-side for malware assembly (SourTrade)
- **Hotel/Conference Wi-Fi Infrastructure**: DNS configuration hijacked for credential phishing
- **Microsoft Bing Image Search**: SVG processing pipeline (Windows and Linux workers)
- **Azure Automation**: Default public configuration enabling cross-tenant identity takeover
- **OpenAI ChatGPT Workspace Agents**: AgentForger vulnerability allowing rogue agent deployment
- **NodeBB Forum Software**: Versions prior to July 2026 security release (eight high-severity flaws)
- **Golden Chickens MaaS Payloads**: Four new malware families and modular implants
- **DevMan RaaS Platform**: Affiliate portal for payload building and victim management
- **Hermes AI Agent**: Open-source agent weaponized in unattended "YOLO" mode

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Deceptive "fix" instructions on trusted platforms (Steam forums) trick users into executing malicious PowerShell commands
- **Malvertising with In-Browser Payload Assembly**: Legitimate browser runtimes (Bun) and JavaScript used to construct executables in memory, evading file-based detection
- **Fileless In-Memory Malware Construction**: Multi-stage JavaScript on fake cryptocurrency/trading sites assembles payloads without disk writes
- **Unauthenticated Deserialization RCE**: Malicious JSON requests exploit Fastjson 1.x in Spring Boot apps for remote code execution
- **Authenticated RCE via Public PoC**: GitLab flaw exploited post-patch using publicly available exploit code
- **Unauthenticated RCE on Enterprise PLM**: Internet-exposed PTC Windchill/FlexPLM targeted for initial access by ransomware affiliates
- **AD CS Certificate Abuse (Certighost)**: Low-privileged users enroll machine certificates for Domain Controllers to achieve domain admin
- **Typosquatted Phishing with Wallet Profiling**: Fake Zoom/Teams domains deliver phishing kits that fingerprint cryptocurrency extensions before malware delivery
- **AI Agent Offensive Automation**: Open-source AI agents run in unattended mode to automate post-exploitation tasks at scale
- **Infrastructure DNS Hijacking**: Compromised hotel Wi-Fi DNS redirects to credential-harvesting Microsoft 365 phishing pages
- **Parser Exploitation via Complex File Formats**: Crafted SVGs achieve RCE in cloud image-processing pipelines (SYSTEM/root)
- **Cross-Tenant Identity Confusion**: Default public Azure Automation settings chained with code flaws for identity takeover
- **AI Agent Supply-Chain/Phishing**: Single phishing link authorizes rogue workspace agents with persistent access
- **RaaS Affiliate Platform Centralization**: Web portals streamline payload generation, victim management, and payout distribution
- **Credential Stuffing**: Automated login attempts using breached credentials (Chick-fil-A, 13,000+ accounts)
- **Data Breach Extortion**: ShinyHunters-leaked email lists fuel sextortion campaigns demanding Bitcoin payments

## Threat Actor Activities

- **Cl0p / Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest**: Ransomware affiliates actively exploiting unauthenticated RCE in PTC Windchill and FlexPLM for initial access; operate as part of broader Cl0p campaign ecosystem
- **BlueNoroff (North Korea)**: Operates active phishing kit using typosquatted Zoom/Teams domains; profiles cryptocurrency wallets before delivering tailored malware; employs ClickFix-style social engineering
- **ShinyHunters**: Extortion group whose leaked data breaches fuel sextortion campaigns demanding $2,000 in Bitcoin; email lists reused by downstream threat actors
- **Golden Chickens Operators**: Malware-as-a-service providers resurfaced with four new malware families and modular implants; continue MaaS operations despite prior disruptions
- **DevMan RaaS Operators**: Maintain centralized affiliate portal for payload building, victim management, and payout tracking; professionalized ransomware affiliate operations
- **Unknown / Unattributed Actors**:
  - Steam Forum ClickFix Campaign: Distributing XMRig via gaming community social engineering
  - SourTrade Malvertising Group: Browser-based malware assembly using Bun runtime
  - Browser Memory Assembly Campaign: Fake Solana/Luno/TradingView pages for in-memory malware construction
  - Hotel Wi-Fi DNS Hijackers: Targeting traveling professionals for Microsoft 365 credentials
  - Certighost Researchers (H0j3n, Aniq Fakhrul): Published exploit for AD CS abuse; unclear if exploited in wild prior to disclosure
  - depthfirst Researchers: Published GitLab RCE PoC six weeks post-patch
  - Thai Finance Ministry Attacker: Used Hermes AI agent in unattended mode for post-exploitation automation
  - Chick-fil-A Credential Stuffers: Breached 13,000+ accounts via credential stuffing (June 17-19)

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
