# Exploitation Report

## Executive Summary

A surge in active exploitation activity spans multiple vectors this period, with ransomware affiliates, nation-state actors, and cybercriminal groups leveraging both novel techniques and unpatched vulnerabilities. The Cl0p ransomware operation continues its data-theft extortion campaign against internet-exposed PTC Windchill and FlexPLM instances using unauthenticated remote code execution, while North Korean-aligned BlueNoroff operators deploy a sophisticated phishing kit that profiles cryptocurrency wallets before delivering malware through typosquatted Zoom and Microsoft Teams domains. Simultaneously, a massive malvertising campaign assembles malware directly in browser memory via malicious JavaScript on fake Solana, Luno, and TradingView pages, bypassing traditional file-based detection.

Critical infrastructure and identity systems face direct targeting. Researchers published a working exploit for the "Certighost" vulnerability allowing low-privileged Active Directory users to impersonate domain controllers, while a default Azure Automation configuration enables cross-tenant identity takeover. Microsoft's own Bing image processing pipeline was shown to execute arbitrary commands as SYSTEM/root via crafted SVG uploads. In the AI supply chain, the Hermes AI agent was deployed in unattended "YOLO" mode to automate post-exploitation against Thailand's Ministry of Finance, and the ChatGPT AgentForger flaw demonstrates how a single phishing link could deploy rogue workspace agents. The Fastjson 1.x library remains actively exploited with no patch available, and GitLab's recently patched RCE now has public proof-of-concept code.

## Active Exploitation Details

### Cl0p Ransomware Unauthenticated RCE in PTC Windchill and FlexPLM
- **Description**: Cl0p ransomware affiliates (tracked as Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest) are exploiting flaws in internet-exposed PTC Windchill and FlexPLM deployments to conduct data theft extortion campaigns. The vulnerability allows unauthenticated remote code execution.
- **Impact**: Attackers gain full control over affected Windchill and FlexPLM instances, enabling data exfiltration for double-extortion ransomware operations. Organizations using these PLM solutions for product development and manufacturing data are primary targets.
- **Status**: Actively exploited in the wild. No patch information provided in source articles; organizations should restrict internet exposure of these systems immediately.

### Fastjson 1.x Remote Code Execution
- **Description**: A critical flaw in Fastjson, Alibaba's widely used JSON library for Java, allows malicious JSON requests to execute arbitrary code in affected Spring Boot applications. Security firms ThreatBook and Imperva confirm active targeting.
- **Impact**: Full remote code execution on application servers processing untrusted JSON input. Given Fastjson's prevalence in Java enterprise applications, the attack surface is extensive.
- **Status**: Actively exploited with no patch available. Users of Fastjson 1.x should implement mitigations such as input validation and consider migration to patched alternatives.

### GitLab Authenticated RCE (Patched June 10, PoC Published July 24)
- **Description**: A vulnerability in GitLab self-managed instances version 18.11.3 and later allows authenticated users to execute commands as the git user. Researchers at depthfirst published working exploit code six weeks after the patch release.
- **Impact**: Authenticated attackers can run arbitrary commands with the privileges of the git system user, potentially leading to repository compromise, supply chain attacks, and lateral movement.
- **Status**: Patched on June 10; public PoC now available. Unpatched instances are at immediate risk of exploitation.

### Certighost Active Directory Privilege Escalation
- **Description**: Researchers H0j3n and Aniq Fakhrul published a working exploit on July 24 that enables a low-privileged Active Directory user to obtain a certificate for a Domain Controller and authenticate as that machine account.
- **Impact**: Complete domain compromise through machine account impersonation. Attackers can escalate from any standard domain user to Domain Controller equivalence, bypassing traditional privilege boundaries.
- **Status**: Public exploit available as of July 24. Organizations should review AD CS configurations and monitor for anomalous certificate requests.

### Bing Images SVG Remote Code Execution
- **Description**: Crafted SVG files submitted to Bing's image search execute commands as NT AUTHORITY\SYSTEM on Microsoft's production Windows image-processing workers and as root on Linux machines in the same fleet. Discovered by XBOW during testing.
- **Impact**: Remote code execution on Microsoft's internal infrastructure with highest system privileges. Demonstrates critical flaws in SVG parsing and sandboxing within cloud image processing pipelines.
- **Status**: Reported to Microsoft; patch status not disclosed in source article. Highlights systemic risk in automated image processing services.

### ChatGPT AgentForger Workspace Agent Deployment
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents allows a single phishing link to stealthily build, authorize, and deploy rogue autonomous agents within a victim's workspace without user interaction beyond clicking the link.
- **Impact**: Attackers gain persistent, autonomous AI agents operating within the victim's ChatGPT environment with access to workspace data, tools, and connected integrations.
- **Status**: Disclosed by researchers; remediation status not specified in source article. Represents emerging class of AI agent supply chain vulnerabilities.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A public-by-default configuration combined with a chain of code flaws in Azure Automation allows attackers to seize another tenant's identity and access their data, credentials, and resources across tenant boundaries.
- **Impact**: Complete cross-tenant compromise in multi-tenant Azure environments. Attackers can pivot from a compromised tenant to target other organizations sharing the same Automation infrastructure.
- **Status**: Microsoft has addressed the configuration default and code flaws. Organizations should verify Azure Automation settings and review cross-tenant access logs.

### Malvertising In-Browser Malware Assembly
- **Description**: A massive malvertising campaign uses fake Solana, Luno, and TradingView webpages containing malicious JavaScript that instructs browsers to assemble malware directly in memory, avoiding disk writes and traditional file-based detection.
- **Impact**: Drive-by compromise of visitors to malicious ad-serving pages. Memory-resident malware evades antivirus scanning and forensic analysis of disk artifacts.
- **Status**: Active campaign ongoing. Browser isolation, script blocking, and memory scanning defenses recommended.

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Credential Theft
- **Description**: Attackers modify DNS settings on Wi-Fi infrastructure at hotels and conference centers to redirect users to convincing fake Microsoft 365 login pages, harvesting credentials from business travelers.
- **Impact**: Targeted credential theft from high-value individuals (executives, government personnel, conference attendees). Bypasses network-level protections by compromising the local network infrastructure.
- **Status**: Active attacks reported. Users should verify TLS certificates and use hardware security keys; venues must secure network equipment.

### BlueNoroff Cryptocurrency Phishing Kit
- **Description**: North Korean threat actors (BlueNoroff) operate an active phishing kit impersonating Zoom and Microsoft Teams through typosquatted domains. The kit profiles victims' cryptocurrency wallets before delivering tailored malware.
- **Impact**: Precision targeting of cryptocurrency holders and organizations. Wallet profiling enables attackers to prioritize high-value targets and customize payloads.
- **Status**: Active campaign with ClickFix-style social engineering. Domain monitoring and user education on meeting invitation verification critical.

### Hermes AI Agent Unattended Post-Exploitation
- **Description**: A threat actor deployed the open-source Hermes AI agent on a rented server in unattended "YOLO" mode (auto-approving risky commands) to automate post-exploitation activities during an alleged breach of Thailand's Ministry of Finance.
- **Impact**: Demonstration of AI agents as force multipliers for offensive operations, enabling automated reconnaissance, lateral movement, and data staging at machine speed without human operators.
- **Status**: Incident reported; attribution not confirmed. Signals paradigm shift in post-exploitation tooling.

### Golden Chickens Malware-as-a-Service Expansion
- **Description**: The Golden Chickens MaaS ecosystem has resurfaced with four new malware families and modular implants, indicating continued development and operator activity despite previous disruptions.
- **Impact**: Lowers barrier to entry for affiliates with modular, updated tooling. New families likely incorporate improved evasion, persistence, and data theft capabilities.
- **Status**: Active development and distribution. Threat intelligence tracking of new indicators essential.

### DevMan Ransomware-as-a-Service Platform
- **Description**: DevMan RaaS operators maintain a dedicated web portal providing affiliates with payload building, victim management, earnings oversight, and affiliate payout automation.
- **Impact**: Professionalized ransomware operations with scalable affiliate management. Centralized portal indicates mature criminal enterprise structure.
- **Status**: Platform active. Represents continued industrialization of ransomware ecosystem.

### NodeBB High-Severity Vulnerabilities (Patched)
- **Description**: Eight high-severity security flaws in NodeBB forum software were disclosed with exploit code. Aikido Security's AI pentest agents discovered all eight in a six-hour run, exposing admin access and private chats.
- **Impact**: Administrative takeover of forum instances, private message disclosure, and potential user data compromise. AI-accelerated vulnerability discovery demonstrates shifting threat landscape.
- **Status**: Patches released; exploit code public. Forum administrators should update immediately.

### Vatican Prayer App API Data Exposure
- **Description**: A porous API endpoint in the Vatican's official prayer application exposes names, email addresses, countries, and site status for over 700,000 global users without authentication.
- **Impact**: Mass PII exposure enabling phishing, identity theft, and targeted social engineering against religious community members globally.
- **Status**: Exposure confirmed; remediation timeline not specified. Highlights risks of unauthenticated APIs in public-facing applications.

### ShinyHunters Data Leaks Fueling Sextortion Campaigns
- **Description**: Threat actors are leveraging email addresses from data breaches leaked by the ShinyHunters extortion group to conduct sextortion campaigns demanding $2,000 in Bitcoin.
- **Impact**: Large-scale harassment and financial extortion using credible personal data from prior breaches. Demonstrates long-tail impact of data breaches.
- **Status**: Active campaigns ongoing. Recipients should ignore demands; law enforcement reporting recommended.

### Slopsquatting/HalluSquatting AI Supply Chain Attack
- **Description**: AI coding agents' tendency to hallucinate package, repository, or domain names creates a late-binding attack pattern where attackers register the hallucinated identifiers to inject malicious code into AI-generated software.
- **Impact**: Supply chain compromise through AI-assisted development workflows. As AI coding adoption grows, this attack vector scales automatically with developer usage.
- **Status**: Active attack pattern identified by ActiveState. Mitigation requires package verification and AI output validation in CI/CD pipelines.

## Affected Systems and Products

- **PTC Windchill and FlexPLM**: Internet-exposed deployments targeted by Cl0p affiliates for unauthenticated RCE and data theft
- **Fastjson 1.x**: Alibaba's Java JSON library used in Spring Boot applications; no patch available for actively exploited RCE
- **GitLab Self-Managed**: Versions 18.11.3 and later vulnerable to authenticated RCE; patched June 10
- **Active Directory with Certificate Services**: Domain controllers vulnerable to Certighost machine account impersonation
- **Microsoft Bing Image Processing**: Production workers (Windows and Linux) executing commands from crafted SVGs as SYSTEM/root
- **OpenAI ChatGPT Workspace Agents**: Critical flaw allowing rogue agent deployment via phishing link
- **Azure Automation**: Cross-tenant identity takeover via default public configuration and code flaw chain
- **Hotel/Conference Wi-Fi Infrastructure**: DNS settings hijacked for Microsoft 365 credential phishing
- **Zoom/Microsoft Teams Domains**: Typosquatted domains used by BlueNoroff for crypto wallet profiling and malware delivery
- **Hermes AI Agent**: Open-source agent deployed in unattended mode for automated post-exploitation
- **Golden Chickens MaaS**: Four new malware families with modular implants distributed to affiliates
- **DevMan RaaS**: Web portal for payload building, victim management, and affiliate operations
- **NodeBB Forum Software**: Eight high-severity flaws exposing admin access and private chats; patches available
- **Vatican Click To Pray App**: API endpoint exposing 700,000+ users' PII without authentication
- **AI Coding Agents**: Hallucinated package/repo/domain names enabling slopsquatting supply chain attacks

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Direct exploitation of internet-facing PTC Windchill/FlexPLM instances without credentials
- **Malicious JSON Deserialization**: Crafted JSON payloads triggering RCE in Fastjson-dependent Spring Boot applications
- **Authenticated Command Injection**: Legitimate GitLab user sessions leveraged to execute commands as git system user
- **Active Directory Certificate Abuse**: Low-privileged users obtaining Domain Controller certificates for machine account impersonation
- **SVG-Based Server-Side Template Injection**: Malicious vector graphics exploiting parser flaws in cloud image processing pipelines
- **AI Agent Supply Chain Compromise**: Phishing links triggering autonomous rogue agent deployment in AI workspaces
- **Cross-Tenant Identity Confusion**: Default cloud configurations enabling unauthorized access across tenant boundaries
- **In-Browser Malware Assembly**: JavaScript reconstructing malicious binaries directly in browser memory to evade disk scanning
- **Network Infrastructure Compromise**: DNS hijacking on physical Wi-Fi hardware for credential harvesting
- **Typosquatting with Dynamic Profiling**: Lookalike collaboration domains that fingerprint crypto wallets before payload delivery
- **AI-Automated Post-Exploitation**: Unattended AI agents executing offensive workflows at machine speed
- **Ransomware-as-a-Service Platform Centralization**: Web portals streamlining affiliate operations from payload generation to payout
- **AI-Accelerated Vulnerability Discovery**: Automated pentest agents finding multiple high-severity flaws in single sessions
- **Unauthenticated API Enumeration**: Public endpoints exposing mass PII without access controls
- **Breach Data Weaponization**: Leaked credentials from prior incidents fueling targeted extortion campaigns
- **Hallucination-Driven Supply Chain Injection**: Attackers registering AI-hallucinated identifiers to poison generated code

## Threat Actor Activities

- **Cl0p / Cl0p Affiliates (Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest)**: Conducting data theft extortion campaign against internet-exposed PTC Windchill and FlexPLM instances using unauthenticated RCE. Operating as ransomware affiliates with established extortion infrastructure.
- **BlueNoroff (North Korean State-Sponsored)**: Operating active phishing kit with typosquatted Zoom/Microsoft Teams domains. Profiling cryptocurrency wallets before delivering tailored malware. Employing ClickFix-style social engineering techniques.
- **ShinyHunters**: Extortion group whose leaked breach data fuels downstream sextortion campaigns demanding $2,000 in Bitcoin. Data from their leaks enables credential-stuffing and targeted harassment.
- **Golden Chickens Operators**: Malware-as-a-service providers resurfacing with four new malware families and modular implants. Continuing MaaS operations despite previous law enforcement attention.
- **DevMan RaaS Operators**: Maintaining centralized web platform for affiliate payload building, victim management, earnings tracking, and automated payouts. Professionalized ransomware operation structure.
- **Thai Finance Ministry Attacker**: Unknown threat actor who deployed Hermes AI agent in unattended "YOLO" mode on rented infrastructure to automate post-exploitation. Demonstrates AI-assisted offensive operations.
- **Hotel Wi-Fi Attackers**: Unknown operators compromising physical network infrastructure at hospitality venues to intercept business traveler credentials. Targeted, infrastructure-focused approach.
- **Certighost Researchers (H0j3n, Aniq Fakhrul)**: Published working exploit for AD CS privilege escalation on July 24. Responsible disclosure timeline not specified; exploit now public.
- **XBOW Researchers**: Discovered and reported Bing Images SVG RCE executing as SYSTEM/root on Microsoft production infrastructure.
- **Aikido Security AI Agents**: Automated pentest agents discovered eight high-severity NodeBB vulnerabilities in six-hour run, demonstrating AI-accelerated offensive capability.
- **Sextortion Campaign Operators**: Unknown actors leveraging ShinyHunters breach data for mass $2,000 Bitcoin extortion emails. High-volume, low-sophistication but credible due to real breach data.

## Source Attribution

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
- **Clop ransomware targets Windchill, FlexPLM in data theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/
- **Europe's Multilingual Reality Exposes AI Security Gaps**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/europes-multilingual-reality-exposes-ai-security-gaps
