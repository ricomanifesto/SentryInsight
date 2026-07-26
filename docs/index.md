# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are targeting diverse attack surfaces ranging from developer tools and enterprise software to consumer platforms and AI-assisted workflows. The Cl0p ransomware affiliates are conducting unauthenticated RCE attacks against internet-exposed PTC Windchill and FlexPLM deployments, while North Korean BlueNoroff operators deploy sophisticated Zoom phishing kits that profile cryptocurrency wallets before delivering malware. Simultaneously, malvertising operations like SourTrade have evolved to fragment malware delivery and leverage legitimate browser runtimes such as Bun to assemble executables directly in victim memory, bypassing traditional network-based detection.

A new class of AI-enabled attacks is emerging across multiple fronts. Threat actors are weaponizing AI coding agents to automate post-exploitation activities—exemplified by the Hermes AI agent deployed in "YOLO" mode against Thailand's Ministry of Finance—while supply chain risks manifest through "slopsquatting" campaigns where hallucinated package names from AI assistants are registered as malicious dependencies. Critical vulnerabilities in widely deployed infrastructure including Fastjson 1.x (with no patch available), GitLab (recently patched but now with public PoC), and Microsoft's Bing Images processing pipeline (allowing SYSTEM-level command execution via crafted SVGs) are either actively exploited or have weaponized proof-of-concept code circulating.

Credential theft and identity-focused attacks remain prevalent with novel techniques. Attackers are hijacking hotel Wi-Fi DNS infrastructure to serve fake Microsoft 365 login pages, exploiting Azure Automation's default configuration for cross-tenant identity takeover, and leveraging ShinyHunters-breached data for large-scale sextortion campaigns. The Golden Chickens MaaS ecosystem has resurfaced with four new malware families, while the DevMan RaaS platform demonstrates increasing operational maturity with centralized affiliate management. These developments collectively indicate adversaries are rapidly adopting automation, AI, and legitimate cloud services to scale operations and evade detection.

## Active Exploitation Details

### Cl0p Affiliates Exploiting PTC Windchill and FlexPLM
- **Description**: Threat actors linked to the Cl0p ransomware campaign are exploiting flaws in internet-exposed PTC Windchill and FlexPLM deployments. The vulnerabilities allow unauthenticated remote code execution, providing initial access for ransomware deployment.
- **Impact**: Full system compromise of product lifecycle management and PLM systems, enabling data theft, ransomware deployment, and lateral movement within victim networks.
- **Status**: Actively exploited in the wild by Cl0p affiliates. No patch status mentioned in source.
- **CVE ID**: Not provided in source article

### Fastjson 1.x Remote Code Execution
- **Description**: A critical flaw in Fastjson, Alibaba's JSON library for Java, allows malicious JSON requests to execute arbitrary commands in affected Spring Boot applications. The vulnerability stems from unsafe deserialization of attacker-controlled JSON input.
- **Impact**: Unauthenticated remote code execution in Java applications using Fastjson 1.x, potentially affecting a vast number of enterprise Spring Boot deployments.
- **Status**: Actively targeted in attacks with no patch available from the vendor. Security firms ThreatBook and Imperva have observed exploitation activity.
- **CVE ID**: Not provided in source article

### GitLab RCE (Patched, PoC Published)
- **Description**: A vulnerability in GitLab's self-managed instances allows authenticated users to execute commands as the `git` system user. The flaw was patched on June 10, but working exploit code was published on July 24 by researchers at depthfirst.
- **Impact**: Authenticated attackers can run arbitrary commands with the privileges of the git user on the underlying server, enabling full compromise of the GitLab instance and potential pivot to the host system.
- **Status**: Patched in versions after June 10 release; however, public PoC availability significantly increases exploitation risk for unpatched instances. Affects self-managed versions 18.11.3 and earlier.
- **CVE ID**: Not provided in source article

### Certighost Active Directory Privilege Escalation
- **Description**: Researchers H0j3n and Aniq Fakhrul published a working exploit (dubbed Certighost) that allows low-privileged Active Directory users to obtain a certificate for a Domain Controller and authenticate as that machine account.
- **Impact**: Domain escalation from standard user to Domain Controller equivalence, enabling complete Active Directory compromise, credential theft, and persistence.
- **Status**: Working exploit code publicly available as of July 24. Relies on Active Directory Certificate Services misconfigurations.
- **CVE ID**: Not provided in source article

### Bing Images SVG RCE
- **Description**: Crafted SVG files submitted to Bing's image search service achieve remote code execution on Microsoft's production image-processing workers. The exploit runs commands as NT AUTHORITY\SYSTEM on Windows workers and as root on Linux workers in the same fleet.
- **Impact**: Server-side code execution on Microsoft's infrastructure with SYSTEM/root privileges, demonstrating a critical flaw in SVG parsing and processing pipelines.
- **Status**: Demonstrated by XBOW researchers; Microsoft presumably addressing. No public exploitation reported beyond research.
- **CVE ID**: Not provided in source article

### ChatGPT AgentForger Vulnerability
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents allows a single phishing link to stealthily build, authorize, and deploy rogue workspace agents without user awareness.
- **Impact**: Attackers can deploy persistent AI agents with access to the victim's workspace data, tools, and permissions, enabling automated data exfiltration and further attacks.
- **Status**: Disclosed by researchers; described as "could have allowed" suggesting potential patch or mitigation.
- **CVE ID**: Not provided in source article

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A public-by-default configuration in Azure Automation combined with a chain of code flaws enables attackers to seize another tenant's identity and access their data, credentials, and resources.
- **Impact**: Cross-tenant compromise in Azure environments, allowing unauthorized access to other organizations' automation resources, managed identities, and connected systems.
- **Status**: Microsoft has addressed the configuration and code flaws.
- **CVE ID**: Not provided in source article

### ClickFix Attacks on Steam Forums
- **Description**: Attackers abuse Steam discussion forums to post fake "fixes" for game and computer problems. These ClickFix-style social engineering attacks trick users into executing malicious commands that install XMRig cryptominers.
- **Impact**: Cryptomining malware installation on gamer systems, resource theft, potential additional payload delivery.
- **Status**: Active campaign leveraging Steam's legitimate forum infrastructure for distribution.
- **CVE ID**: Not provided in source article

### SourTrade Malvertising (Browser-Built Executables)
- **Description**: The SourTrade malvertising operation fragments malware delivery and uses the legitimate Bun JavaScript runtime in victims' browsers to assemble the final Windows executable locally, rather than serving a complete malicious binary.
- **Impact**: Evasion of network-based malware detection and sandbox analysis; delivery of fully functional Windows malware through seemingly benign JavaScript code.
- **Status**: Active malvertising campaign observed in the wild.
- **CVE ID**: Not provided in source article

### In-Browser JavaScript Malware Assembly
- **Description**: A massive malvertising campaign uses fake Solana, Luno, and TradingView webpages with malicious JavaScript that instructs browsers to assemble malware directly in memory, avoiding disk writes.
- **Impact**: Fileless malware execution in browser memory, bypassing traditional AV/EDR detection that focuses on disk artifacts.
- **Status**: Active large-scale campaign targeting cryptocurrency and trading platform users.
- **CVE ID**: Not provided in source article

### BlueNoroff Zoom Phishing Kit
- **Description**: North Korean threat actors operate an active phishing kit using typosquatted Zoom and Microsoft Teams domains. The kit profiles victims' cryptocurrency wallets before delivering tailored malware.
- **Impact**: Credential theft, cryptocurrency wallet compromise, and targeted malware delivery to high-value targets in crypto/finance sectors.
- **Status**: Active phishing infrastructure with ClickFix-style social engineering techniques.
- **CVE ID**: Not provided in source article

### Hotel Wi-Fi DNS Hijacking for M365 Credential Theft
- **Description**: Attackers compromise Wi-Fi infrastructure at hotels and conference centers to modify DNS settings, redirecting users to fake Microsoft 365 login pages that harvest credentials.
- **Impact**: Corporate Microsoft 365 account compromise for travelers, enabling business email compromise, data access, and further phishing.
- **Status**: Active campaign targeting business travelers at hospitality venues.
- **CVE ID**: Not provided in source article

### Hermes AI Agent Automated Post-Exploitation
- **Description**: A threat actor deployed the open-source Hermes AI agent on a rented server in unattended "YOLO" mode (permissionless command execution) to automate post-exploitation activities during an alleged breach of Thailand's Ministry of Finance.
- **Impact**: Automated, scalable post-exploitation including lateral movement, data discovery, and exfiltration without human operator intervention.
- **Status**: Observed in real-world intrusion; demonstrates weaponization of legitimate AI tools for offensive operations.
- **CVE ID**: Not provided in source article

### Golden Chickens MaaS New Malware Families
- **Description**: The Golden Chickens malware-as-a-service operators have resurfaced with four new malware families and modular implants, indicating continued development and operational activity.
- **Impact**: Expanded MaaS capabilities for affiliates, including new evasion techniques, payload types, and targeting options.
- **Status**: Active development and deployment; operators showing no signs of stopping despite previous disruptions.
- **CVE ID**: Not provided in source article

### NodeBB Vulnerabilities (AI-Discovered)
- **Description**: Eight high-severity security flaws in NodeBB forum software were discovered by AI pentesting agents in a six-hour run. Vulnerabilities expose admin access and private chats. Exploit code has been published.
- **Impact**: Administrative takeover of NodeBB forums, private message disclosure, user data compromise.
- **Status**: Patched by NodeBB; however, public exploit code availability puts unpatched instances at immediate risk.
- **CVE ID**: Not provided in source article

### DevMan RaaS Platform Operations
- **Description**: The DevMan ransomware-as-a-service operates a dedicated web portal providing affiliates with payload building, victim management, earnings tracking, and payout management capabilities.
- **Impact**: Lowered barrier to entry for ransomware affiliates; professionalized operations enabling scalable attacks.
- **Status**: Active RaaS platform with centralized affiliate management.
- **CVE ID**: Not provided in source article

### ShinyHunters Data Leaks Fueling Sextortion
- **Description**: Email addresses exposed in data breaches leaked by the ShinyHunters extortion group are being used to send sextortion emails demanding $2,000 in Bitcoin.
- **Impact**: Large-scale harassment, financial fraud, and psychological harm to breach victims; monetization of stolen data.
- **Status**: Active sextortion campaign leveraging previously breached datasets.
- **CVE ID**: Not provided in source article

### Chick-fil-A Credential Stuffing Attack
- **Description**: Credential stuffing attacks targeting Chick-fil-A's website and mobile app between June 17-19 compromised over 13,000 customer accounts.
- **Impact**: Account takeover, potential payment method abuse, loyalty point theft, and personal data exposure.
- **Status**: Confirmed breach; attributed to credential reuse from third-party breaches.
- **CVE ID**: Not provided in source article

### Vatican Prayer App API Data Leak
- **Description**: A porous API endpoint in the Vatican's official prayer app exposes names, email addresses, country, and site status for over 700,000 global users without authentication.
- **Impact**: Mass PII exposure of religious app users; data harvesting for phishing, profiling, or surveillance.
- **Status**: Vulnerable endpoint accessible to anyone with a browser; no authentication required.
- **CVE ID**: Not provided in source article

## Affected Systems and Products

- **PTC Windchill and FlexPLM**: Internet-exposed deployments of product lifecycle management and PLM software; versions unspecified
- **Fastjson 1.x**: Alibaba's JSON library for Java; all 1.x versions potentially affected in Spring Boot applications
- **GitLab Self-Managed**: Versions 18.11.3 and earlier; patched in post-June 10 releases
- **Active Directory Certificate Services**: Environments with vulnerable certificate template configurations enabling Certighost attack
- **Microsoft Bing Image Processing Pipeline**: Production workers processing SVG uploads; Windows (SYSTEM) and Linux (root) fleets
- **ChatGPT Workspace Agents**: OpenAI's agent framework; vulnerability in agent authorization/deployment flow
- **Azure Automation**: Default configuration across Azure tenants; cross-tenant identity boundary affected
- **Steam Discussion Forums**: Valve's community forum platform abused for ClickFix distribution
- **Bun JavaScript Runtime**: Legitimate runtime (bun.sh) weaponized for in-browser executable assembly
- **NodeBB Forum Software**: All versions prior to security patch; eight high-severity flaws
- **Zoom and Microsoft Teams**: Brand names abused via typosquatted domains in BlueNoroff phishing kit
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on hospitality network devices
- **Hermes AI Agent**: Open-source AI assistant (github.com/hermes-ai/hermes) weaponized in YOLO mode
- **Golden Chickens MaaS Infrastructure**: Malware-as-a-service platform with four new malware families
- **DevMan RaaS Portal**: Web-based affiliate management platform for ransomware operations
- **Chick-fil-A Website and Mobile App**: Customer-facing authentication systems
- **Vatican Click to Pray App**: Official prayer application API backend

## Attack Vectors and Techniques

- **Unauthenticated RCE via Deserialization**: Fastjson 1.x unsafe JSON deserialization in Spring Boot apps; PTC Windchill/FlexPLM unspecified flaws
- **ClickFix Social Engineering**: Fake error messages/fixes on Steam forums and typosquatted Zoom/Teams domains trick users into executing malicious commands (PowerShell, Run dialog)
- **Browser-Based Malware Assembly**: Legitimate runtimes (Bun) and JavaScript used to construct PE executables in memory; fragmented delivery evades network inspection
- **Fileless In-Memory Execution**: Malware assembled directly in browser memory via JavaScript on fake crypto/trading sites; no disk artifacts
- **AI-Automated Post-Exploitation**: Hermes AI agent in unattended mode automates enumeration, lateral movement, and data collection
- **DNS Hijacking on Shared Infrastructure**: Compromise of hotel Wi-Fi DNS to redirect M365 authentication to adversary-controlled pages
- **Cross-Tenant Identity Confusion**: Azure Automation default public configuration exploited to assume other tenants' managed identities
- **Typosquatting with Pre-Attack Profiling**: BlueNoroff registers lookalike Zoom/Teams domains; phishing kit profiles crypto wallets before payload delivery
- **AD CS Certificate Theft**: Certighost exploits misconfigured certificate templates to obtain DC machine certificates for authentication relay
- **SVG Parser Exploitation**: Crafted SVGs trigger RCE in image processing pipelines (Bing Images) with elevated privileges
- **Phishing Link to AI Agent Deployment**: Single malicious link triggers unauthorized ChatGPT Workspace Agent build, authorization, and deployment
- **Credential Stuffing at Scale**: Automated login attempts using ShinyHunters-breached credentials against Chick-fil-A services
- **Unauthenticated API Enumeration**: Vatican prayer app API exposes 700K+ records without authentication or rate limiting
- **MaaS/RaaS Affiliate Enablement**: Golden Chickens and DevMan provide tooling, payloads, and management consoles to affiliates
- **Sextortion via Breach Data Monetization**: ShinyHunters leak data reused for Bitcoin extortion campaigns
- **AI Supply Chain Poisoning (Slopsquatting)**: Hallucinated package/domain names from AI coding agents registered as malicious dependencies

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Actively exploiting internet-exposed PTC Windchill and FlexPLM for initial access in ransomware campaigns; operating as affiliates of the broader Cl0p operation
- **BlueNoroff (North Korean State-Sponsored)**: Operating sophisticated Zoom/Teams phishing kit with crypto wallet profiling; conducting ClickFix-style social engineering; targeting cryptocurrency and financial sectors
- **ShinyHunters**: Extortion group whose breached datasets (email lists) fuel downstream sextortion campaigns demanding $2,000 in Bitcoin
- **Golden Chickens Operators**: MaaS providers resurfaced with four new malware families and modular implants; continuing development despite previous law enforcement attention
- **DevMan RaaS Operators**: Maintaining professional affiliate portal with payload building, victim management, and payout automation; indicative of mature RaaS ecosystem
- **Hermes AI Attacker (Unidentified)**: Deployed open-source Hermes AI agent in unattended mode against Thailand Ministry of Finance; demonstrates novel AI-assisted intrusion methodology
- **Hotel Wi-Fi Attackers (Unidentified)**: Compromising hospitality network infrastructure for DNS-based M365 credential harvesting; targeting business travelers
- **SourTrade Malvertising Group**: Operating browser-based malware assembly campaign using Bun runtime; advanced evasion through fragmented delivery
- **In-Browser Malware Campaign Operators (Unidentified)**: Large-scale malvertising via fake Solana/Luno/TradingView pages; JavaScript in-memory malware construction
- **Steam Forum ClickFix Operators (Unidentified)**: Abusing Steam discussion forums for cryptominer distribution via social engineering
- **NodeBB Vulnerability Researchers (Aikido Security / depthfirst)**: AI pentest agents discovered eight flaws; depthfirst published GitLab PoC; dual-use research/exploitation activity
- **XBOW Researchers**: Demonstrated Bing Images SVG RCE achieving SYSTEM/root on Microsoft infrastructure
- **Certighost Researchers (H0j3n and Aniq Fakhrul)**: Published working AD CS exploit enabling domain escalation

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
