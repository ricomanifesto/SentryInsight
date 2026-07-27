# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively targeting organizations across diverse sectors, with threat actors leveraging unpatched vulnerabilities, novel malware delivery techniques, and sophisticated social engineering. A zero-day remote code execution flaw in Fastjson 1.x is being actively exploited in the wild with no patch available, affecting Spring Boot applications globally. Simultaneously, Cl0p ransomware affiliates are conducting mass exploitation of internet-exposed PTC Windchill and FlexPLM instances through unauthenticated RCE vulnerabilities, while North Korean actors behind BlueNoroff deploy advanced phishing kits that profile cryptocurrency wallets before delivering malware via typosquatted Zoom and Microsoft Teams domains.

Novel attack vectors are emerging that bypass traditional detection mechanisms. The SourTrade malvertising campaign uses a legitimate Bun runtime to force victims' browsers to assemble Windows executables in memory from fragmented payloads, while ClickFix attacks on Steam forums and hotel Wi-Fi DNS hijacking demonstrate the continued effectiveness of social engineering combined with infrastructure manipulation. In the identity space, the Certighost exploit enables low-privileged Active Directory users to impersonate Domain Controllers through certificate abuse, and a default Azure Automation configuration allows cross-tenant identity takeover. Supply chain defenses are evolving with GitHub and PyPI implementing time-based Dependabot cooldowns to counter poisoned package adoption, though AI-driven hallucination attacks like slopsquatting present new risks for development pipelines.

## Active Exploitation Details

### Fastjson 1.x Remote Code Execution (Zero-Day)
- **Description**: A critical flaw in Fastjson, Alibaba's JSON library for Java, allows attackers to execute arbitrary commands through malicious JSON requests in affected Spring Boot applications. The vulnerability stems from unsafe deserialization of attacker-controlled JSON input.
- **Impact**: Full remote code execution on vulnerable Spring Boot applications, enabling complete server compromise, data theft, lateral movement, and deployment of additional payloads such as ransomware or cryptominers.
- **Status**: Actively exploited in the wild by threat actors monitored by ThreatBook and Imperva. No official patch is available from the maintainers as of the reporting date. Organizations using Fastjson 1.x in Spring Boot applications are at immediate risk.
- **CVE ID**: Not provided in source articles

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Vulnerabilities in internet-exposed deployments of PTC Windchill (referred to as "Windmill" in reporting) and FlexPLM product lifecycle management software allow unauthenticated remote code execution.
- **Impact**: Attackers gain initial access to internal networks without credentials, enabling deployment of Cl0p ransomware, data exfiltration, and persistent footholds in manufacturing, engineering, and critical infrastructure environments.
- **Status**: Actively exploited by Cl0p affiliates (Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest) as part of ongoing ransomware campaigns. Internet-exposed instances are being systematically scanned and compromised.
- **CVE ID**: Not provided in source articles

### GitLab RCE (Patched - PoC Published)
- **Description**: A vulnerability in GitLab self-managed instances allows authenticated users to execute arbitrary commands as the `git` system user. The flaw was patched on June 10, but working exploit code was publicly released on July 24 by depthfirst researchers.
- **Impact**: Authenticated attackers achieve code execution on the underlying server with the privileges of the GitLab service account, potentially leading to source code theft, supply chain compromise, and lateral movement.
- **Status**: Patch available since June 10 for versions 18.11.3 and later. Public PoC increases exploitation risk for unpatched instances. Organizations should verify patch deployment immediately.
- **CVE ID**: Not provided in source articles

### Certighost Active Directory Certificate Abuse
- **Description**: An exploit technique (dubbed Certighost) allows low-privileged Active Directory users to obtain a certificate for a Domain Controller and authenticate as that machine account, effectively impersonating the DC.
- **Impact**: Privilege escalation from standard domain user to Domain Controller equivalence, enabling full domain compromise, credential theft, Golden Ticket creation, and persistence.
- **Status**: Working exploit published on July 24 by researchers H0j3n and Aniq Fakhrul. Active Directory environments with misconfigured certificate templates or overly permissive enrollment rights are vulnerable.
- **CVE ID**: Not provided in source articles

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A default public configuration in Azure Automation combined with a chain of code flaws allows attackers to seize another tenant's identity and access their data, credentials, and resources.
- **Impact**: Cross-tenant compromise in multi-tenant Azure environments, enabling unauthorized access to subscription resources, managed identities, and sensitive configuration data across organizational boundaries.
- **Status**: Microsoft has addressed the public-by-default configuration and underlying code flaws. Organizations should audit Azure Automation account configurations and managed identity assignments.
- **CVE ID**: Not provided in source articles

### ChatGPT Workspace Agents AgentForger Vulnerability
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents feature allows a single phishing link to stealthily build, authorize, and deploy autonomous rogue agents within a victim's workspace.
- **Impact**: Attackers gain persistent, automated access to the victim's ChatGPT environment with the ability to exfiltrate conversation data, access connected tools and APIs, and perform actions on the user's behalf.
- **Status**: Disclosed by cybersecurity researchers. OpenAI remediation status not specified in source articles.
- **CVE ID**: Not provided in source articles

### Bing Images SVG RCE
- **Description**: Crafted SVG images submitted to Bing's image search service achieve remote code execution as `NT AUTHORITY\SYSTEM` on Windows production image-processing workers and as `root` on Linux machines in the same fleet.
- **Impact**: Server-side code execution on Microsoft's infrastructure through image upload functionality, demonstrating a critical flaw in SVG parsing and sandboxing.
- **Status**: Discovered by XBOW during testing. Microsoft remediation status not specified in source articles.
- **CVE ID**: Not provided in source articles

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON Library for Java)**: All versions in the 1.x series used within Spring Boot applications; no patched version available
- **PTC Windchill**: Internet-exposed deployments across all unpatched versions; Product Lifecycle Management (PLM) software used in manufacturing and engineering
- **PTC FlexPLM**: Internet-exposed deployments across all unpatched versions; PLM solution for retail, footwear, and apparel industries
- **GitLab Self-Managed**: Versions prior to 18.11.3 (patched June 10); source code management and DevOps platform
- **Microsoft Active Directory**: Domain environments with vulnerable certificate template configurations or excessive enrollment permissions
- **Microsoft Azure Automation**: Accounts with default public configuration and vulnerable managed identity chains; multi-tenant cloud environments
- **OpenAI ChatGPT Workspace Agents**: Workspaces with Agents feature enabled; AI-assisted development and productivity environments
- **Microsoft Bing Image Processing Infrastructure**: Production workers processing SVG uploads; Windows (SYSTEM) and Linux (root) execution contexts
- **Steam Discussion Forums**: Valve's community platform; Windows gamers targeted via ClickFix social engineering
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network devices; Microsoft 365 users on guest networks

## Attack Vectors and Techniques

- **Malicious JSON Deserialization**: Attackers send crafted JSON payloads to Spring Boot applications using Fastjson 1.x, triggering unsafe deserialization and arbitrary code execution without authentication
- **Unauthenticated RCE via Internet-Exposed Services**: Cl0p affiliates scan for and exploit vulnerable PTC Windchill/FlexPLM instances directly from the internet, requiring no credentials or prior access
- **Browser-Based Malware Assembly (SourTrade)**: Malvertising campaign delivers fragmented payloads to victims' browsers, which use a legitimate Bun JavaScript runtime to reconstruct and execute Windows PE files in memory—evading static file-based detection
- **In-Browser JavaScript Malware Construction**: Fake Solana, Luno, and TradingView pages execute malicious JavaScript that assembles malware directly in browser memory, avoiding disk writes and traditional AV scanning
- **ClickFix Social Engineering**: Attackers compromise Steam forums and use fake "fix" buttons that copy malicious PowerShell commands to clipboard, tricking users into self-executing XMRig cryptominers
- **DNS Hijacking on Public Wi-Fi**: Threat actors modify DNS settings on hotel/conference center Wi-Fi devices to redirect Microsoft 365 authentication traffic to credential-harvesting phishing pages
- **Typosquatted Collaboration Domains**: BlueNoroff registers domains mimicking Zoom and Microsoft Teams, delivering phishing kits that profile cryptocurrency wallet extensions before deploying malware
- **AD Certificate Template Abuse (Certighost)**: Low-privileged users exploit misconfigured certificate templates to enroll for Domain Controller certificates, enabling machine account impersonation and domain compromise
- **Cross-Tenant Identity Takeover via Default Configuration**: Attackers exploit public-by-default Azure Automation settings and chained code flaws to assume managed identities of other tenants
- **Phishing Link to Rogue AI Agent Deployment**: Single malicious link exploits ChatGPT Workspace Agents vulnerability to automatically build, authorize, and deploy persistent rogue agents in victim workspaces
- **SVG-Based Server-Side Code Execution**: Crafted SVG files exploit parsing vulnerabilities in Bing's image processing pipeline to achieve SYSTEM/root RCE on backend infrastructure
- **Credential Stuffing at Scale**: Automated login attempts using breached credential pairs compromise Chick-fil-A customer accounts via website and mobile app endpoints
- **AI Hallucination Package Attacks (Slopsquatting/HalluSquatting)**: Attackers register package, repository, or domain names hallucinated by AI coding assistants, which developers then inadvertently pull into projects
- **Supply Chain Poisoning with Rapid Publishing**: Malicious actors publish poisoned packages and rely on automated dependency update tools (Dependabot) to pull them immediately; GitHub/PyPI 3-day cooldown mitigates this window

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Conducting mass exploitation of internet-exposed PTC Windchill and FlexPLM instances via unauthenticated RCE for ransomware deployment and data extortion; ongoing campaign targeting manufacturing and engineering sectors
- **East Asia-Linked Threat Actor (TELESHIM)**: Targeting government entities in the Middle East using custom malware that abuses Telegram for command-and-control communications; fresh intrusion activity observed
- **BlueNoroff (North Korean State-Sponsored)**: Operating ClickFix-style campaigns with typosquatted Zoom/Microsoft Teams domains; maintains active phishing kit that profiles victim cryptocurrency wallets before delivering tailored malware; attributed to DPRK reconnaissance and financial theft operations
- **ShinyHunters (Extortion Group)**: Leaked data breaches fueling large-scale sextortion campaigns demanding $2,000 in Bitcoin; email addresses from prior breaches used for targeted credential-based threats
- **DevMan RaaS Operators**: Maintaining a dedicated Ransomware-as-a-Service web portal providing affiliates with payload builders, victim management dashboards, and automated payout systems; professionalizing ransomware affiliate operations
- **Hermes AI Agent Operator**: Used open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation activity during alleged breach of Thailand's Ministry of Finance; demonstrates AI-assisted offensive operations
- **Depthfirst Researchers**: Published working GitLab RCE exploit code on July 24 (six weeks after June 10 patch); responsible disclosure followed by public PoC release
- **H0j3n and Aniq Fakhrul (Researchers)**: Published Certighost exploit on July 24 enabling AD certificate abuse; working proof-of-concept for privilege escalation
- **XBOW (Security Researchers)**: Discovered and tested Bing Images SVG RCE achieving SYSTEM/root execution on Microsoft production infrastructure
- **Unidentified ClickFix Operators**: Compromising Steam discussion forums to deliver XMRig cryptominers via social engineering; targeting gaming community
- **Unidentified Hotel Wi-Fi Attackers**: Hijacking DNS on hospitality network infrastructure to harvest Microsoft 365 credentials from business travelers
- **Credential Stuffing Actors**: Automated attacks against Chick-fil-A website and mobile app (June 17-19) compromising 13,000+ customer accounts using breached credential pairs

## Source Attribution

- **TELESHIM Abuses Telegram for C2 in Attacks Against Middle East Governments**: The Hacker News - https://thehackernews.com/2026/07/teleshim-abuses-telegram-for-c2-in.html
- **GitHub Adds 3-Day Dependabot Cooldown to Limit Poisoned Package Adoption**: The Hacker News - https://thehackernews.com/2026/07/github-adds-3-day-dependabot-cooldown.html
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
