# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with several zero-day or unpatched flaws posing immediate risk. Most critically, a Fastjson 1.x remote code execution vulnerability is being actively targeted in the wild with no patch currently available, affecting Spring Boot applications globally. Simultaneously, Cl0p ransomware affiliates are exploiting unauthenticated RCE flaws in internet-exposed PTC Windchill and FlexPLM deployments, while a public exploit has been released for a pre-authentication code execution vulnerability in vBulletin forums. Additional high-severity flaws in n8n, GitLab, and Active Directory (Certighost) have working exploit code publicly available, though patches exist for these.

Threat actor activity spans financially motivated ransomware groups, nation-state actors, and extortion collectives. Cl0p affiliates continue mass exploitation of enterprise PLM software, while the North Korean BlueNoroff group operates a sophisticated Zoom phishing kit targeting cryptocurrency holders. The ShinyHunters extortion gang has claimed breaches at Ernst & Young via supply-chain compromise and is leveraging stolen data for sextortion campaigns. China-linked actors deploy the Cruciferra crypter using BYOVD and process ghosting techniques, and the TELESHIM operation abuses Telegram for C2 against Middle Eastern government entities. A novel malvertising campaign (SourTrade) forces victims' browsers to assemble malware in memory using the legitimate Bun runtime, while ClickFix social engineering lures proliferate across Steam forums and fake Microsoft Teams updates.

Credential theft and identity-focused attacks remain prevalent. Attackers are hijacking hotel Wi-Fi DNS to serve fake Microsoft 365 login pages, while credential stuffing hit Chick-fil-A's customer base. The Coca-Cola subsidiary Fairlife suffered a ransomware attack with confirmed data exfiltration, and OnTrac disclosed a network intrusion exposing customer data. Meanwhile, AI-assisted offensive operations are emerging, with the Hermes AI agent used in autonomous mode to automate post-exploitation during an alleged breach of Thailand's Ministry of Finance.

## Active Exploitation Details

### Fastjson 1.x Remote Code Execution
- **Description**: A critical deserialization flaw in Alibaba's Fastjson JSON library for Java (1.x versions). In affected Spring Boot applications, a malicious JSON request can execute arbitrary code on the server without authentication.
- **Impact**: Full remote code execution on vulnerable application servers, leading to complete system compromise, data theft, and lateral movement.
- **Status**: Actively exploited in the wild by threat actors. ThreatBook and Imperva confirm targeting. **No patch is currently available** for the 1.x branch, making this a zero-day equivalent for affected users.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Unauthenticated remote code execution vulnerabilities in PTC Windchill and FlexPLM product lifecycle management software deployments exposed to the internet.
- **Impact**: Attackers achieve initial access and code execution on PLM servers without credentials, enabling data exfiltration, ransomware deployment, and supply-chain compromise.
- **Status**: Actively exploited by Cl0p ransomware affiliates (aka Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest) as part of their mass-exploitation campaign.

### vBulletin Pre-Authentication Code Execution
- **Description**: A pre-authentication remote code execution flaw in vBulletin forum software where an unauthenticated request can reach PHP's `eval()` function and execute arbitrary code.
- **Impact**: Complete takeover of unpatched forum servers, including database access, user credential theft, and use as a platform for further attacks.
- **Status**: Public exploit details released on July 27. The vulnerability is patched, but exploit availability significantly increases risk for unpatched instances.

### n8n Sandbox Escape
- **Description**: A high-severity expression-sandbox escape in the n8n workflow automation platform. An authenticated workflow editor can break out of the sandbox and execute operating-system commands on the underlying server.
- **Impact**: Privilege escalation from workflow editor to full OS command execution as the n8n process user, enabling server compromise and access to connected systems.
- **Status**: Patched by n8n. Security Joes researchers discovered and reported the flaw.

### GitLab Authenticated RCE (PoC Published)
- **Description**: A vulnerability in GitLab self-managed instances allowing authenticated users to execute commands as the `git` system user.
- **Impact**: Authenticated attackers gain command execution on the GitLab server, potentially accessing source code, CI/CD secrets, and infrastructure.
- **Status**: Patched by GitLab on June 10. Working exploit code (PoC) published by depthfirst researchers on July 24, six weeks post-patch.

### Certighost Active Directory Exploit
- **Description**: An exploit allowing low-privileged Active Directory users to obtain a certificate for a Domain Controller and authenticate as that machine account.
- **Impact**: Full domain compromise via machine account impersonation, enabling DCSync attacks, Golden Ticket creation, and complete Active Directory takeover.
- **Status**: Working exploit published on July 24 by researchers H0j3n and Aniq Fakhrul. Relates to Active Directory Certificate Services (AD CS) misconfigurations/vulnerabilities.

### Cruciferra Crypter with BYOVD and Process Ghosting
- **Description**: A sophisticated crypter used by a China-linked cybercrime group that employs Bring Your Own Vulnerable Driver (BYOVD) and process ghosting techniques to evade detection and execute payloads.
- **Impact**: Stealthy malware delivery and execution, bypassing EDR/AV solutions. Used in income tax-themed phishing campaigns targeting Indian taxpayers, tax professionals, and corporate finance teams.
- **Status**: Actively deployed in ongoing campaigns. The vulnerable driver abuse indicates kernel-level exploitation capabilities.

### TELESHIM Telegram C2 Campaign
- **Description**: Malware framework (TELESHIM) that abuses Telegram's API for command-and-control communications, targeting government entities in the Middle East.
- **Impact**: Persistent, low-detection C2 channel enabling data exfiltration, lateral movement, and long-term espionage access.
- **Status**: Fresh activity reported by researchers. Threat actor attributed to East Asia-linked group.

### SourTrade Malvertising (Browser-Assembled Malware)
- **Description**: A malvertising operation delivering malware in pieces via malicious JavaScript on fake Solana, Luno, and TradingView webpages. The victim's browser assembles the final Windows executable in memory using the legitimate Bun runtime.
- **Impact**: Fileless malware delivery that evades traditional file-based detection, delivering payloads including information stealers and remote access trojans.
- **Status**: Active large-scale campaign. Uses legitimate infrastructure (Bun runtime) to avoid static signatures.

### ClickFix Social Engineering Campaigns
- **Description**: Multi-vector social engineering technique tricking users into executing malicious commands (typically PowerShell) under the guise of "fixes" for system or application issues.
- **Impact**: Direct user-initiated malware execution, bypassing email filters and exploit mitigations. Delivers XMRig cryptominers, information stealers, and RMM tools.
- **Status**: 
  - Active on Steam discussion forums targeting gamers
  - BlueNoroff (North Korea) uses ClickFix-style lures with typosquatted Zoom/Teams domains
  - Operation BlueDash employs fake Microsoft Teams updates with "secure document" lures to deploy Level RMM and ScreenConnect

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Credential Theft
- **Description**: Attackers compromise hotel and conference center Wi-Fi infrastructure to modify DNS settings, redirecting users to fake Microsoft 365 login pages.
- **Impact**: Credential harvesting from high-value targets (business travelers, conference attendees) with high success rates due to trusted network context.
- **Status**: Active campaign reported. Targets Microsoft 365 accounts specifically.

### Hermes AI Agent Automated Post-Exploitation
- **Description**: Threat actor used the open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation activities during an alleged breach of Thailand's Ministry of Finance.
- **Impact**: Accelerated and scaled post-exploitation including enumeration, lateral movement, and data staging without constant operator oversight.
- **Status**: Confirmed use in at least one government-targeted intrusion. Represents emerging AI-assisted offensive capability.

### ShinyHunters Supply-Chain and Extortion Operations
- **Description**: The ShinyHunters extortion group claims a breach of Ernst & Young via a supply-chain attack obtaining system credentials. Previously leaked data from ShinyHunters breaches is now fueling $2,000 Bitcoin sextortion email campaigns.
- **Impact**: Enterprise data theft via trusted third-party relationships; downstream victim harassment and extortion using breached data.
- **Status**: Active extortion operations. EY breach claimed recently; sextortion campaigns ongoing.

### DevMan Ransomware-as-a-Service Platform
- **Description**: A dedicated RaaS web portal providing affiliates with payload building, victim management, earnings tracking, and payout administration.
- **Impact**: Lowers barrier to entry for ransomware operators, enabling rapid campaign scaling and professionalized criminal operations.
- **Status**: Active platform maintained by DevMan operators. Represents continued RaaS ecosystem maturation.

### Credential Stuffing and Account Takeover
- **Description**: Large-scale credential stuffing attacks targeting consumer-facing applications using previously breached username/password pairs.
- **Impact**: Account takeover, personal data exposure, financial fraud, and brand reputation damage.
- **Status**: 
  - Chick-fil-A: 13,000+ customer accounts breached between June 17–19
  - Fairlife (Coca-Cola): Ransomware attack with confirmed data theft
  - OnTrac: Network intrusion exposing customer personal details

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON library for Java)**: All 1.x versions in Spring Boot applications; no patch available
- **PTC Windchill and FlexPLM**: Internet-exposed deployments; versions unspecified in reporting
- **vBulletin Forum Software**: Unpatched versions vulnerable to pre-auth RCE; patched versions available
- **n8n Workflow Automation Platform**: Versions prior to security patch; affects self-hosted deployments
- **GitLab Self-Managed**: Versions 18.11.3 and earlier; patched in June 10 release
- **Active Directory Certificate Services (AD CS)**: Environments with vulnerable certificate templates/configurations enabling Certighost
- **Windows Systems with Vulnerable Drivers**: Any system where BYOVD can load a known vulnerable driver (Cruciferra campaigns)
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network devices at hospitality venues
- **Microsoft 365 Accounts**: Credentials targeted via fake login pages
- **Steam Discussion Forums**: Platform abused for ClickFix lure distribution
- **Zoom/Microsoft Teams Domains**: Typosquatted domains used by BlueNoroff for phishing kit delivery
- **Telegram API**: Legitimate service abused for C2 by TELESHIM malware
- **Bun JavaScript Runtime**: Legitimate tooling co-opted for in-browser malware assembly (SourTrade)
- **Level RMM and ScreenConnect**: Legitimate remote management tools deployed maliciously via Operation BlueDash
- **Ernst & Young Systems**: Compromised via supply-chain attack (specific systems undisclosed)
- **Chick-fil-A Website and Mobile App**: Targeted by credential stuffing
- **Fairlife (Coca-Cola Subsidiary) Systems**: Ransomware encryption and data exfiltration
- **OnTrac Corporate Network**: Breached with customer data exposure
- **Thailand Ministry of Finance Systems**: Alleged breach with AI-automated post-exploitation

## Attack Vectors and Techniques

- **Unauthenticated Remote Code Execution**: Direct exploitation of internet-facing services (Fastjson, PTC Windchill/FlexPLM, vBulletin) without credentials
- **Authenticated Privilege Escalation**: Workflow editor to OS command execution (n8n); authenticated user to `git` user command execution (GitLab)
- **Active Directory Certificate Abuse**: Low-privileged user to Domain Controller impersonation via AD CS (Certighost)
- **Bring Your Own Vulnerable Driver (BYOVD)**: Loading known vulnerable kernel drivers to disable security tools and execute shellcode (Cruciferra)
- **Process Ghosting**: Executable image tampering technique to evade EDR callbacks and execute malicious payloads stealthily (Cruciferra)
- **Browser-Based Malware Assembly**: JavaScript fetches encrypted payload chunks and uses WebAssembly/Bun runtime to reconstruct executable in memory (SourTrade)
- **ClickFix Social Engineering**: Fake error messages and "verification" prompts trick users into pasting malicious PowerShell into Run dialog or terminal
- **DNS Hijacking / Rogue DHCP/DNS**: Compromise of network infrastructure to redirect authentication traffic to attacker-controlled phishing pages
- **Typosquatting / Domain Impersonation**: Lookalike Zoom and Microsoft Teams domains for credential harvesting and malware delivery (BlueNoroff)
- **Supply-Chain Compromise**: Breach of trusted third-party vendor to access target organization (ShinyHunters → EY)
- **Credential Stuffing**: Automated testing of breached credential pairs against target authentication endpoints
- **Ransomware-as-a-Service Affiliate Model**: Centralized platform for payload generation, victim management, and profit sharing (DevMan)
- **AI-Automated Post-Exploitation**: Autonomous AI agent execution of enumeration, lateral movement, and data collection commands (Hermes)
- **Legitimate Tool Abuse (Living-off-the-Land)**: Deployment of signed RMM tools (Level, ScreenConnect) for persistent remote access (Operation BlueDash)
- **Telegram API for C2**: Encrypted, trusted communication channel blending with legitimate traffic (TELESHIM)
- **Data Leak Extortion / Sextortion**: Monetization of breached data via direct victim threats (ShinyHunters data → $2,000 Bitcoin demands)

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Mass exploitation of internet-exposed PTC Windchill and FlexPLM instances using unauthenticated RCE. Ongoing ransomware and data theft campaign targeting enterprise PLM data.
- **BlueNoroff (North Korea / Lazarus Subgroup)**: Operates sophisticated Zoom phishing kit with typosquatted domains. Profiles cryptocurrency wallet presence before delivering malware. Uses ClickFix-style social engineering. Targets crypto holders and financial sector.
- **ShinyHunters Extortion Group**: Claims EY breach via supply-chain attack. Leaks/stolen data fuels sextortion campaigns demanding $2,000 in Bitcoin. Active data broker and extortion operator.
- **China-Linked Cybercrime Group (Cruciferra Operators)**: Deploys Cruciferra crypter with BYOVD and process ghosting. Runs income tax-themed phishing targeting Indian taxpayers, tax professionals, and corporate finance teams. Sophisticated evasion capabilities.
- **TELESHIM Operator (East Asia-Linked)**: Targets Middle East government entities. Uses Telegram for C2. Conducts espionage-focused intrusions with data exfiltration.
- **Operation BlueDash Operators**: Microsoft Teams-themed phishing with "secure document" lures. Deploys legitimate RMM tools (Level, ScreenConnect) for persistent access. Financially motivated.
- **SourTrade Malvertising Group**: Large-scale malvertising via fake crypto/trading sites. Innovative browser-based malware assembly using Bun runtime. Distributes information stealers and RATs.
- **Hermes AI Agent User (Unattributed)**: Leveraged open-source Hermes AI in "YOLO" mode for automated post-exploitation during alleged Thailand Ministry of Finance breach. Demonstrates AI-augmented offensive operations.
- **DevMan RaaS Operators**: Maintains professional affiliate portal for ransomware payload building, victim tracking, and cryptocurrency payout management. Enables criminal ecosystem scaling.
- **Hotel Wi-Fi Attackers (Unattributed)**: Compromises hospitality network infrastructure to hijack DNS and serve fake Microsoft 365 login pages. Targets business travelers for credential theft.
- **Credential Stuffing Operators (Multiple)**: Automated account takeover campaigns against Chick-fil-A (13k+ accounts), with Fairlife and OnTrac also suffering breaches likely involving credential reuse or initial access via valid accounts.

## Source Attribution

- **Coca-Cola confirms data theft in Fairlife ransomware attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coca-cola-confirms-data-theft-in-fairlife-ransomware-attack/
- **Ernst \& Young data breach claimed by ShinyHunters extortion gang**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ernst-and-young-data-breach-claimed-by-shinyhunters-extortion-gang/
- **Public Exploit Released for Patched vBulletin Pre-Auth Code Execution Flaw**: The Hacker News - https://thehackernews.com/2026/07/public-exploit-released-for-patched.html
- **⚡ Weekly Recap: Rogue AI Agents, Check Point Exploit, Slopsquatting, ClickFix Lures and More**: The Hacker News - https://thehackernews.com/2026/07/weekly-recap-rogue-ai-agents-check.html
- **Shadow AI agents are multiplying. Here's how to find and secure them.**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/shadow-ai-agents-are-multiplying-heres-how-to-find-and-secure-them/
- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process**: The Hacker News - https://thehackernews.com/2026/07/n8n-sandbox-escape-lets-workflow.html
- **Operation BlueDash Deploys Level RMM and ScreenConnect via Fake Teams Update**: The Hacker News - https://thehackernews.com/2026/07/operation-bluedash-deploys-level-rmm.html
- **Cruciferra Crypter Uses BYOVD and Process Ghosting to Hide Windows Malware**: The Hacker News - https://thehackernews.com/2026/07/cruciferra-crypter-uses-byovd-and.html
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
