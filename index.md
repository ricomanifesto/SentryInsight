# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse technology stacks, ranging from enterprise Java libraries and DevOps platforms to AI-powered development tools and cloud infrastructure. The Fastjson 1.x remote code execution flaw remains unpatched while under active attack, and Cl0p ransomware affiliates are leveraging unauthenticated RCE vulnerabilities in internet-exposed PTC Windchill and FlexPLM deployments. Simultaneously, researchers have published proof-of-concept exploits for recently patched flaws in GitLab and Active Directory (Certighost), creating immediate risk for organizations that have not yet applied updates.

Novel attack techniques are proliferating rapidly. North Korean threat actors (BlueNoroff) have operationalized ClickFix-style social engineering through typosquatted video-conferencing domains, while the SourTrade malvertising campaign and related advertising operation pioneers a browser-native malware assembly technique using the legitimate Bun runtime. Attackers are also weaponizing AI agents—specifically the open-source Hermes framework in unattended "YOLO" mode—to automate post-exploitation activity against high-value targets such as Thailand's Ministry of Finance. Credential theft campaigns continue to evolve, with hotel Wi-Fi DNS hijacking redirecting victims to convincing Microsoft 365 phishing pages and Chick-fil-A suffering a large-scale credential stuffing incident affecting over 13,000 customers.

Supply chain and identity-based threats round out the landscape. GitHub and PyPI have deployed time-based defenses in Dependabot to mitigate supply chain attack impact, while a default-public Azure Automation configuration enabled cross-tenant identity takeover before Microsoft's remediation. The Golden Chickens malware-as-a-service ecosystem has resurfaced with four new modular families, the DevMan RaaS platform continues to professionalize affiliate operations, and AI hallucination-driven "slopsquatting" attacks target developers through phantom package names. The ShinyHunters extortion group's data leaks are fueling sextortion campaigns, and a porous API in the Vatican's official prayer application exposed 700,000+ users' personally identifiable information.

## Active Exploitation Details

### Fastjson 1.x Remote Code Execution
- **Description**: A critical deserialization flaw in Alibaba's Fastjson library for Java allows remote code execution in affected Spring Boot applications when processing malicious JSON requests. The vulnerability stems from unsafe auto-type deserialization behavior.
- **Impact**: Attackers achieve full remote code execution on the application server by sending a single crafted JSON payload, leading to complete system compromise, data exfiltration, and lateral movement.
- **Status**: Actively exploited in the wild by threat actors tracked by ThreatBook and Imperva. No official patch is currently available for the 1.x branch, leaving users dependent on mitigations such as disabling auto-type or upgrading to Fastjson 2.x where feasible.

### GitLab Authenticated Remote Code Execution
- **Description**: A vulnerability in GitLab's self-managed instances (versions 18.11.3 and later) allows authenticated users to execute arbitrary commands as the `git` system user. The flaw was patched by GitLab on June 10, 2026.
- **Impact**: Any authenticated user—including low-privilege accounts—can run commands with the permissions of the Git service account, enabling repository manipulation, secret theft, supply chain poisoning, and potential privilege escalation.
- **Status**: GitLab released a patch on June 10, 2026. On July 24, 2026, security researchers at depthfirst published a working proof-of-concept exploit, significantly increasing exploitation risk for unpatched instances.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Unauthenticated remote code execution vulnerabilities affect internet-exposed deployments of PTC Windchill (PLM software) and FlexPLM. The flaws allow remote attackers to execute code without authentication.
- **Impact**: Full server compromise, intellectual property theft from product lifecycle management systems, ransomware deployment, and lateral movement into connected engineering and manufacturing environments.
- **Status**: Actively exploited by Cl0p ransomware affiliates (also tracked as Chubby Scorpius, FIN11, Graceful Spider, and Lace Tempest) as part of their ongoing campaign targeting internet-facing enterprise applications.

### Certighost Active Directory Privilege Escalation
- **Description**: An exploit chain in Active Directory Certificate Services (AD CS) allows a low-privileged domain user to request and obtain a certificate for a Domain Controller machine account, then authenticate as that Domain Controller using Kerberos delegation.
- **Impact**: Complete domain compromise. Attackers gain Domain Controller-level access, enabling credential theft (including KRBTGT), persistent access, and unrestricted lateral movement across the forest.
- **Status**: Researchers H0j3n and Aniq Fakhrul published a working exploit (dubbed "Certighost") on July 24, 2026. No CVE identifier was referenced in the source material. Organizations with AD CS deployments should immediately audit certificate templates and enrollment permissions.

### ChatGPT Workspace Agents AgentForger Vulnerability
- **Description**: A critical flaw in OpenAI's ChatGPT Workspace Agents feature allows an attacker to craft a phishing link that, when clicked by a target user, silently builds, authorizes, and deploys a rogue AI agent within the victim's workspace.
- **Impact**: The rogue agent inherits the victim's permissions and can access private repositories, exfiltrate code and data, modify files, and perform actions on behalf of the user—all without further interaction.
- **Status**: Disclosed by cybersecurity researchers in July 2026. OpenAI's remediation status was not specified in the source article.

### Bing Images SVG Remote Code Execution
- **Description**: Crafted SVG files submitted to Bing's image search service are processed by backend workers in a manner that allows arbitrary command execution. The vulnerability affects both Windows (running as NT AUTHORITY\SYSTEM) and Linux (running as root) image-processing fleets.
- **Impact**: Remote code execution on Microsoft's production infrastructure with highest available privileges, potentially enabling access to internal networks, source code, and customer data processed by the image pipeline.
- **Status**: Demonstrated by security researcher XBOW. Microsoft's remediation timeline was not specified in the source article.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A default-public configuration in Azure Automation combined with a chain of code flaws allows an attacker to seize another tenant's managed identity and access their data, credentials, and resources across the Azure control plane.
- **Impact**: Complete cross-tenant compromise in multi-tenant Azure environments, bypassing tenant isolation boundaries. Attackers can access subscriptions, key vaults, storage accounts, and other resources belonging to victim tenants.
- **Status**: Microsoft has addressed the public-by-default configuration and underlying code flaws. Organizations should verify their Azure Automation accounts are not publicly accessible and review managed identity assignments.

### ClickFix Social Engineering on Steam Forums
- **Description**: Attackers abuse Steam discussion forums to post fake "fixes" for game errors and computer problems. These posts instruct victims to copy-paste PowerShell commands into a Run dialog (Windows Key + R), which downloads and executes the XMRig cryptominer.
- **Impact**: Cryptojacking via XMRig, consuming victim CPU/GPU resources for Monero mining. Potential deployment of additional payloads through the same execution chain.
- **Status**: Active campaign ongoing as of July 2026. Relies entirely on social engineering; no software vulnerability is exploited.

### SourTrade Malvertising Browser-Native Malware Assembly
- **Description**: A malvertising operation dubbed "SourTrade" delivers malware in fragmented pieces through malicious advertisements. The victim's browser uses a legitimate Bun JavaScript runtime to assemble the final Windows executable in memory, bypassing traditional file-based detection.
- **Impact**: Evasion of network and endpoint security controls that inspect complete executable files. Delivery of arbitrary payloads (infostealers, loaders, ransomware) directly assembled in the browser process.
- **Status**: Active campaign observed in July 2026. Leverages legitimate web technologies (Bun runtime, WebAssembly, Fetch API) rather than exploiting a browser vulnerability.

### In-Browser Malware Assembly via Malicious JavaScript
- **Description**: A large-scale malvertising campaign uses fake Solana, Luno, and TradingView webpages containing malicious JavaScript that instructs the victim's browser to assemble malware directly in memory, avoiding disk writes.
- **Impact**: Fileless malware execution that evades traditional antivirus and EDR solutions. Payloads include information stealers and remote access trojans targeting cryptocurrency wallets and financial credentials.
- **Status**: Active massive campaign as of July 2026. Uses typosquatted domains mimicking legitimate cryptocurrency and trading platforms.

### BlueNoroff North Korean Phishing Kit
- **Description**: The North Korean threat group BlueNoroff (associated with Lazarus Group) operates a sophisticated phishing kit that impersonates Zoom and Microsoft Teams via typosquatted domains. The kit profiles victims' cryptocurrency wallet holdings before delivering tailored malware.
- **Impact**: Credential theft, cryptocurrency wallet compromise, and targeted malware delivery to high-value targets in the cryptocurrency and DeFi sectors. The profiling step enables attackers to prioritize and customize follow-on exploitation.
- **Status**: Active campaign ongoing as of July 2026. Uses ClickFix-style social engineering techniques combined with infrastructure spoofing.

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Credential Theft
- **Description**: Attackers compromise Wi-Fi infrastructure at hotels and conference centers, modifying DNS settings to redirect users attempting to access Microsoft 365 services to convincing phishing pages that harvest credentials.
- **Impact**: Corporate Microsoft 365 account compromise, leading to business email compromise, data exfiltration from Exchange/SharePoint/OneDrive, and further phishing from trusted internal accounts.
- **Status**: Active attacks reported in July 2026. Targets travelers and conference attendees using untrusted networks.

### Hermes AI Agent Automated Post-Exploitation
- **Description**: A threat actor deployed the open-source Hermes AI agent on a rented server, disabled its safety confirmation prompts ("YOLO mode"), and directed it to automate post-exploitation activity against Thailand's Ministry of Finance.
- **Impact**: Automated, scalable post-exploitation including lateral movement, credential access, data discovery, and exfiltration—conducted at machine speed without human operator bottlenecks.
- **Status**: Incident reported in July 2026. Demonstrates the dual-use risk of autonomous AI agents when safety controls are deliberately disabled.

### Golden Chickens Malware-as-a-Service Expansion
- **Description**: The Golden Chickens (aka Venom Spider) MaaS operators have released four new malware families with modular implant architectures, indicating sustained investment in their criminal ecosystem.
- **Impact**: Diversified payload options for affiliates, improved evasion capabilities, and expanded targeting flexibility. Modular design allows rapid customization for specific victims.
- **Status**: Active resurgence observed in July 2026. The group shows no signs of cessation despite prior law enforcement attention.

### Chick-fil-A Credential Stuffing Campaign
- **Description**: Automated credential stuffing attacks against Chick-fil-A's website and mobile application between June 17–19, 2026, leveraging previously breached username/password pairs to compromise customer accounts.
- **Impact**: Over 13,000 customer accounts breached. Exposed data includes order history, payment methods, loyalty rewards, and personal information.
- **Status**: Incident confirmed by Chick-fil-A. Highlights ongoing risk of credential reuse and the need for mandatory multi-factor authentication on consumer-facing services.

### ShinyHunters Data Leak Sextortion Campaign
- **Description**: Threat actors are leveraging email addresses exposed in data breaches previously leaked by the ShinyHunters extortion group to send sextortion emails demanding $2,000 in Bitcoin.
- **Impact**: Psychological harm, financial loss, and potential escalation to further social engineering using the same compromised data sets.
- **Status**: Active campaign as of July 2026. ShinyHunters' historical breach data continues to fuel downstream criminal activity.

### Vatican Prayer App API Data Exposure
- **Description**: A misconfigured API endpoint in the Vatican's official "Click To Pray" mobile application exposes personally identifiable information—including names, email addresses, country, and site status—for over 700,000 global users without authentication.
- **Impact**: Mass PII harvesting for phishing, identity theft, and targeted social engineering. The religious context of the data may enable highly tailored deception campaigns.
- **Status**: Exposure identified by researchers in July 2026. Remediation status not specified in source article.

### DevMan Ransomware-as-a-Service Platform
- **Description**: The DevMan RaaS operators maintain a dedicated web portal providing affiliates with payload building, victim management, earnings tracking, and payout administration—professionalizing the ransomware affiliate model.
- **Impact**: Lowered barrier to entry for ransomware deployment, accelerated time-to-exploit for affiliates, and centralized campaign optimization.
- **Status**: Platform active as of July 2026. Represents the continued industrialization of ransomware operations.

### Slopsquatting / HalluSquatting Supply Chain Attack
- **Description**: AI coding agents hallucinate non-existent package, repository, or domain names during code generation. Attackers register these phantom identifiers and publish malicious packages or typosquatted domains, which are then automatically pulled by developers trusting AI-generated recommendations.
- **Impact**: Supply chain compromise through trusted development workflows. Malicious code executes in build pipelines, CI/CD systems, and production applications.
- **Status**: Active attack pattern documented by ActiveState in July 2026. Affects npm, PyPI, GitHub, and other package repositories where AI-assisted development is prevalent.

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON Library for Java)**: All 1.x versions in Spring Boot applications with auto-type deserialization enabled; no patched 1.x release available
- **GitLab Self-Managed**: Versions 18.11.3 and later prior to June 10, 2026 patch; Community and Enterprise editions affected
- **PTC Windchill**: Internet-exposed deployments; specific version range not disclosed in source
- **PTC FlexPLM**: Internet-exposed deployments; specific version range not disclosed in source
- **Active Directory Certificate Services (AD CS)**: Windows Server environments with vulnerable certificate template configurations allowing low-privilege enrollment for Domain Controller authentication
- **ChatGPT Workspace Agents**: OpenAI's ChatGPT platform Workspace Agents feature; all users with Workspace access potentially affected
- **Bing Image Search Backend**: Microsoft's production image-processing worker fleet (Windows and Linux)
- **Azure Automation**: Accounts with default public networking configuration; all Azure tenants using Automation managed identities
- **Steam Community Forums**: Valve's Steam platform discussion forums used as delivery mechanism (not a software vulnerability in Steam itself)
- **Bun JavaScript Runtime**: Legitimate runtime leveraged as execution environment for in-browser malware assembly (not vulnerable itself)
- **Zoom / Microsoft Teams Domains**: Typosquatted domains impersonating legitimate video-conferencing services
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network equipment at hospitality venues
- **Hermes AI Agent**: Open-source AI agent framework; risk manifests when safety controls are disabled and tool access is unrestricted
- **Golden Chickens MaaS Payloads**: Four new modular malware families distributed via the Golden Chickens affiliate network
- **Chick-fil-A Website and Mobile App**: Consumer-facing authentication endpoints vulnerable to credential stuffing
- **Vatican "Click To Pray" Mobile Application**: API backend serving the official prayer application (iOS/Android)
- **DevMan RaaS Portal**: Web-based affiliate management platform for DevMan ransomware operations
- **Package Repositories (npm, PyPI, GitHub, etc.)**: Registries where AI-hallucinated package names can be registered by attackers

## Attack Vectors and Techniques

- **Malicious JSON Deserialization**: Crafted JSON payloads exploiting unsafe auto-type handling in Fastjson to achieve RCE in Java applications
- **Authenticated Command Injection**: Exploitation of GitLab's command execution flaw via authenticated API/web requests running as `git` user
- **Unauthenticated Remote Code Execution**: Direct exploitation of PTC Windchill/FlexPLM endpoints without credentials
- **AD CS Certificate Abuse**: Low-privilege user requests Domain Controller certificate via vulnerable template, then uses Kerberos delegation for DC impersonation
- **Phishing Link Agent Deployment**: Malicious URL triggers silent rogue agent installation in ChatGPT Workspace via OAuth/authorization flow manipulation
- **SVG Parser Exploitation**: Crafted SVG files with embedded scripts/expressions triggering command execution during image processing
- **Cross-Tenant Identity Confusion**: Exploitation of default-public Azure Automation managed identities to assume victim tenant identities
- **ClickFix Social Engineering**: Fake error fixes posted on trusted platforms (Steam forums) tricking users into executing PowerShell via Run dialog
- **Browser-Native Malware Assembly**: Fragmented payload delivery reconstructed in-browser using legitimate runtimes (Bun) and Web APIs
- **In-Memory JavaScript Malware Construction**: Malicious JavaScript on typosquatted domains assembles executable payloads directly in browser memory
- **Cryptocurrency Wallet Profiling Phishing**: Phishing kit enumerates wallet extensions/holdings before delivering targeted malware
- **DNS Hijacking on Public Wi-Fi**: Compromise of network infrastructure to redirect authentication traffic to credential harvesting pages
- **Autonomous AI Post-Exploitation**: Disabled safety controls on AI agent (Hermes YOLO mode) enabling unattended offensive operations
- **Modular MaaS Payload Delivery**: Golden Chickens affiliates deploy swappable implant modules for customized victim engagement
- **Credential Stuffing at Scale**: Automated login attempts using breached credential pairs against consumer authentication endpoints
- **Sextortion via Breach Data Leverage**: ShinyHunters breach data repurposed for psychological coercion and Bitcoin extortion
- **Unauthenticated API Enumeration**: Public API endpoint lacking access controls exposes PII via simple HTTP requests
- **RaaS Affiliate Portal Operations**: Centralized web platform for payload generation, campaign management, and cryptocurrency payout processing
- **AI Hallucination Supply Chain Poisoning**: Registration of AI-hallucinated package/domain names to intercept developer dependency resolution

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Actively exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM deployments as part of ongoing ransomware campaign; leveraging enterprise application vulnerabilities for initial access
- **BlueNoroff (North Korea / Lazarus Group)**: Operating sophisticated phishing kit with typosquatted Zoom/Teams domains; profiling cryptocurrency wallet holdings before tailored malware delivery; employing ClickFix-style social engineering techniques
- **ShinyHunters**: Extortion group whose historical data breaches (2020–2024) continue to fuel downstream sextortion campaigns demanding $2,000 in Bitcoin per victim
- **Golden Chickens / Venom Spider**: MaaS operators resurfaced in July 2026 with four new modular malware families; maintaining active affiliate ecosystem with professional tooling
- **DevMan RaaS Operators**: Running centralized affiliate portal for payload building, victim management, and payout administration; professionalizing ransomware affiliate operations
- **Depthfirst Researchers**: Published working GitLab RCE PoC on July 24, 2026 (six weeks after vendor patch); responsible disclosure timeline followed
- **H0j3n and Aniq Fakhrul**: Published Certighost AD CS exploit on July 24, 2026; demonstrated Domain Controller impersonation via certificate abuse
- **XBOW Researcher**: Demonstrated Bing Images SVG RCE achieving SYSTEM/root execution on Microsoft production infrastructure
- **SourTrade Operators**: Running innovative malvertising campaign using Bun runtime for browser-native executable assembly; active July 2026
- **In-Browser Malware Campaign Operators**: Large-scale malvertising using fake Solana/Luno/TradingView pages with JavaScript-based in-memory malware construction
- **Hermes AI Attacker**: Unknown threat actor who deployed Hermes agent in YOLO mode on rented infrastructure to automate post-exploitation against Thailand Ministry of Finance
- **Hotel Wi-Fi Attackers**: Unknown operators compromising hospitality network infrastructure for DNS-based credential harvesting targeting Microsoft 365 users
- **Chick-fil-A Credential Stuffing Actors**: Unknown operators conducting automated login attempts June 17–19, 2026 using breached credential datasets
- **Slopsquatting/HalluSquatting Registrants**: Unknown actors registering AI-hallucinated package and domain names to poison software supply chains

## Source Attribution

- **GitHub, PyPI add time-based defenses against supply chain attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/github-pypi-add-time-absed-defenses-against-supply-chain-attacks/
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
