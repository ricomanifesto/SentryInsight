# Exploitation Report

## Executive Summary

Multiple active exploitation campaigns are targeting diverse attack surfaces ranging from developer supply chains and enterprise software to consumer platforms and cloud infrastructure. Threat actors are leveraging novel techniques including browser-based malware assembly via JavaScript, ClickFix social engineering on gaming forums, and AI-assisted post-exploitation automation. Critical vulnerabilities in widely deployed components such as Fastjson 1.x and PTC Windchill/FlexPLM are being exploited with no patches available, while ransomware-as-a-service operations like DevMan and Golden Chickens continue to professionalize their affiliate ecosystems.

North Korean actor BlueNoroff is deploying sophisticated phishing kits that profile cryptocurrency wallets before payload delivery, and Cl0p affiliates are actively scanning for internet-exposed PLM systems. Meanwhile, credential stuffing and data breach fallout from ShinyHunters leaks are fueling sextortion campaigns, and hotel Wi-Fi DNS hijacking is being used to harvest Microsoft 365 credentials. The Certighost exploit enables low-privileged Active Directory users to impersonate domain controllers, representing a significant privilege escalation risk for on-premises environments.

New attack patterns are emerging around AI-generated hallucinations (slopsquatting/phantom domains), malicious browser-based executable construction using legitimate runtimes like Bun, and automation of post-exploitation via AI agents such as Hermes. Cloud identity boundaries are under pressure from Azure Automation misconfigurations enabling cross-tenant takeover, while supply chain risks extend to forum software (NodeBB) and collaboration platforms (GitLab). These developments collectively indicate a threat landscape where exploitation speed, automation, and supply chain reach are accelerating.

## Active Exploitation Details

### Fastjson 1.x Remote Code Execution
- **Description**: A critical flaw in Fastjson, Alibaba's JSON library for Java, allows attackers to execute arbitrary code via malicious JSON requests in affected Spring Boot applications. The vulnerability stems from unsafe deserialization of attacker-controlled input.
- **Impact**: Full remote code execution on the target application server, enabling attackers to take complete control of the host, access sensitive data, and pivot within the network.
- **Status**: Actively exploited in the wild by threat actors tracked by ThreatBook and Imperva. No patch is currently available for Fastjson 1.x, leaving users dependent on mitigation strategies such as blocking malicious payloads via WAF rules or upgrading to Fastjson 2.x where feasible.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Vulnerabilities in internet-exposed deployments of PTC Windchill and FlexPLM product lifecycle management software allow unauthenticated remote code execution. Cl0p affiliates are scanning for and exploiting these flaws as part of their ransomware operations.
- **Impact**: Unauthenticated attackers achieve full system compromise, enabling data theft, ransomware deployment, and lateral movement within victim networks. Targets include manufacturing, aerospace, and defense organizations using these PLM platforms.
- **Status**: Active exploitation by Cl0p affiliates (also known as Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest). Organizations with internet-facing Windchill or FlexPLM instances are at immediate risk.

### GitLab RCE (Patched June 10, 2026)
- **Description**: A vulnerability in GitLab self-managed instances version 18.11.3 and earlier allows authenticated users to execute commands as the `git` system user. Researchers at depthfirst published a working proof-of-concept exploit on July 24, six weeks after the patch was released.
- **Impact**: Authenticated attackers can run arbitrary commands with the privileges of the GitLab service account, potentially accessing repositories, configuration secrets, and underlying infrastructure.
- **Status**: Patched by GitLab on June 10, 2026. Public PoC exploit code is now available, increasing risk for unpatched instances. Organizations should verify patch deployment immediately.

### Certighost Active Directory Privilege Escalation
- **Description**: The Certighost exploit allows a low-privileged Active Directory user to obtain a certificate for a Domain Controller and authenticate as that machine account. Researchers H0j3n and Aniq Fakhrul published a working exploit on July 24.
- **Impact**: Attackers with any valid domain credentials can escalate to Domain Controller-level privileges, effectively compromising the entire Active Directory forest. This enables persistence, credential theft, and unrestricted lateral movement.
- **Status**: Working exploit code is publicly available. Mitigation requires AD CS configuration hardening and monitoring for suspicious certificate enrollment activity.

### Bing Images SVG RCE
- **Description**: Crafted SVG files submitted to Bing's image search triggered remote code execution as NT AUTHORITY\SYSTEM on Microsoft's production image-processing workers, and as root on Linux machines in the same fleet. Discovered by XBOW during testing.
- **Impact**: Successful exploitation yields SYSTEM/root access on Microsoft's internal infrastructure, potentially allowing access to sensitive processing pipelines and adjacent systems.
- **Status**: Reported to Microsoft via responsible disclosure. The vulnerability demonstrates the risk of complex parser logic in cloud-scale image processing pipelines.

### ChatGPT AgentForger Vulnerability
- **Description**: A critical flaw in OpenAI's ChatGPT Workspace Agents could allow a single phishing link to stealthily build, authorize, and deploy an automated rogue agent within a victim's workspace.
- **Impact**: Attackers could gain persistent, automated access to a victim's ChatGPT workspace, enabling data exfiltration, prompt injection, and abuse of connected tool execution without further user interaction.
- **Status**: Disclosed by cybersecurity researchers. OpenAI has been notified; patch status should be monitored.

### NodeBB Forum Vulnerabilities (Eight High-Severity Flaws)
- **Description**: Eight security flaws in NodeBB forum software expose admin access and private chats. Aikido Security's AI pentest agents discovered all eight vulnerabilities in a six-hour run, with exploit code publicly released.
- **Impact**: Attackers can achieve administrative takeover of NodeBB instances, read private messages, and potentially pivot to connected systems. High severity ratings indicate reliable exploitability.
- **Status**: NodeBB has released patches. Administrators should apply updates immediately given public exploit availability.

### Azure Automation Cross-Tenant Identity Takeover
- **Description**: A default public configuration in Azure Automation combined with a chain of code flaws could allow attackers to seize another tenant's identity and access their data, credentials, and resources.
- **Impact**: Cross-tenant compromise in multi-tenant Azure environments, breaking isolation boundaries and enabling unauthorized access to victim tenants' automation assets, runbooks, and managed identities.
- **Status**: Microsoft has addressed the public-by-default configuration and underlying code flaws. Organizations should review Azure Automation configurations and managed identity permissions.

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON Library for Java)**: All versions in the 1.x branch; Spring Boot applications using vulnerable deserialization configurations
- **PTC Windchill**: Internet-exposed deployments; specific versions not disclosed in reporting
- **PTC FlexPLM**: Internet-exposed deployments; specific versions not disclosed in reporting
- **GitLab Self-Managed**: Versions 18.11.3 and earlier; patched in versions released after June 10, 2026
- **Microsoft Active Directory**: Environments with Active Directory Certificate Services (AD CS) configured with vulnerable templates
- **Bing Images Processing Pipeline**: Microsoft's internal image-processing workers (Windows and Linux)
- **OpenAI ChatGPT Workspace Agents**: Workspaces with Agents feature enabled
- **NodeBB Forum Software**: Versions prior to the July 2026 security release; all eight flaws rated high severity
- **Azure Automation**: Tenants with default public configurations; affects cross-tenant identity isolation
- **Steam Discussion Forums**: Valve's Steam platform community forums abused for ClickFix delivery
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network devices at hospitality venues

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Attackers post fake "fixes" for game or computer problems on Steam forums, tricking users into executing malicious PowerShell commands that deploy XMRig cryptominers. The technique abuses user trust in community-sourced troubleshooting.
- **Browser-Based Malware Assembly (SourTrade)**: Malvertising campaign delivers malware in pieces via JavaScript, using the legitimate Bun runtime to assemble the final Windows executable directly in the victim's browser memory. No single malicious binary is served, evading traditional network and endpoint detection.
- **JavaScript In-Memory Malware Construction**: Massive malvertising campaign uses fake Solana, Luno, and TradingView webpages with malicious JavaScript that instructs browsers to assemble malware directly in memory, avoiding disk writes and file-based scanning.
- **AI-Assisted Post-Exploitation (Hermes Agent)**: Threat actors deploy the open-source Hermes AI agent in unattended "YOLO" mode (permission prompts disabled) to automate post-exploitation tasks including reconnaissance, lateral movement, and data collection against targets such as Thailand's Ministry of Finance.
- **DNS Hijacking on Hospitality Wi-Fi**: Attackers compromise hotel and conference center Wi-Fi devices to modify DNS settings, redirecting users to fake Microsoft 365 login pages for credential harvesting. Targets travelers and conference attendees.
- **BlueNoroff Crypto-Wallet Profiling Phishing Kit**: North Korean actors operate a phishing kit impersonating Zoom and Microsoft Teams via typosquatted domains. The kit profiles victims' cryptocurrency wallet extensions before delivering tailored malware.
- **Credential Stuffing from Breach Data**: ShinyHunters data breach leaks fuel sextortion campaigns and credential stuffing attacks (e.g., Chick-fil-A breach affecting 13,000+ accounts between June 17–19).
- **AI Hallucination Supply Chain Attacks (Slopsquatting/Phantom Domains/HalluSquatting)**: AI coding agents generate hallucinated package, repository, or domain names that attackers register and populate with malicious code, exploiting late-binding trust in AI-generated references.
- **Unauthenticated RCE via Malicious JSON/Serialization**: Fastjson and GitLab flaws both leverage unsafe deserialization of attacker-controlled structured data (JSON, GitLab payloads) to achieve code execution.
- **Cross-Tenant Identity Abuse**: Default Azure Automation settings allow attackers to manipulate managed identities and automation resources across tenant boundaries, violating cloud isolation assumptions.

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Actively scanning for and exploiting internet-exposed PTC Windchill and FlexPLM deployments via unauthenticated RCE. Using PLM compromise as initial access for ransomware deployment and data theft across manufacturing and defense sectors.
- **BlueNoroff (North Korea-linked)**: Operating a sophisticated phishing kit using typosquatted Zoom and Microsoft Teams domains. The kit profiles installed cryptocurrency wallet browser extensions before delivering customized malware payloads. Conducting ClickFix-style social engineering campaigns.
- **ShinyHunters (Extortion Group)**: Data breaches leaked by this group are being repurposed by downstream actors for sextortion email campaigns demanding $2,000 in Bitcoin, and for credential stuffing against consumer services (e.g., Chick-fil-A).
- **DevMan RaaS Operators**: Maintaining a dedicated web portal for affiliates providing payload building, victim management, earnings tracking, and payout administration. Professionalizing ransomware-as-a-service operations with centralized tooling.
- **Golden Chickens (MaaS Operators)**: Resurfaced with four new malware families and modular implants, indicating continued development and expansion of their malware-as-a-service ecosystem despite prior disruptions.
- **Hermes AI Agent Operator (Unattributed)**: Used the open-source Hermes AI agent in unattended mode to automate post-exploitation during an alleged breach of Thailand's Ministry of Finance. Demonstrates adoption of AI tooling for offensive automation.
- **SourTrade Malvertising Group**: Operating a campaign that delivers malware in fragments and uses victims' browsers with the Bun runtime to assemble executables in memory. Evades traditional detection by avoiding complete malicious binary delivery.
- **Hotel Wi-Fi DNS Hijackers (Unattributed)**: Compromising network infrastructure at hotels and conference centers to redirect Microsoft 365 authentication traffic to credential harvesting pages. Targeting business travelers and event attendees.
- **Snapchat Account Compromise Actor**: Individual sentenced to 76 months for hacking 750+ women's Snapchat accounts to steal private photos. Demonstrates persistent targeting of personal accounts for intimate image theft.

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
