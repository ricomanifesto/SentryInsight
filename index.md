# Exploitation Report

## Executive Summary

Critical exploitation activity this week spans unpatched zero-day vulnerabilities, active ransomware campaigns leveraging unauthenticated RCE flaws, and novel attack techniques that abuse legitimate infrastructure. The most severe development is the active targeting of Fastjson 1.x, a widely used Java JSON library, with a critical remote code execution vulnerability that currently has no patch available—leaving Spring Boot applications exposed to arbitrary command execution via malicious JSON requests. Simultaneously, Cl0p ransomware affiliates are exploiting unauthenticated RCE flaws in internet-exposed PTC Windchill and FlexPLM deployments, while a newly published Certighost exploit allows low-privileged Active Directory users to impersonate domain controllers. These high-impact vulnerabilities are compounded by the public release of a GitLab RCE proof-of-concept six weeks after patching, creating urgency for delayed patchers.

Novel attack vectors are proliferating across multiple campaigns. The SourTrade malvertising operation pioneers a technique where victims' browsers assemble Windows executables in memory using the legitimate Bun runtime, avoiding traditional payload delivery. ClickFix social engineering has expanded to Steam forums distributing XMRig cryptominers and to North Korean BlueNoroff operations using typosquatted Zoom and Teams domains to profile cryptocurrency wallets before malware delivery. Operation BlueDash leverages Microsoft Teams-themed lures to deploy legitimate RMM tools (Level RMM and ScreenConnect), while the China-linked Cruciferra group combines BYOVD and process ghosting in a sophisticated crypter. Threat actors are also abusing Telegram for C2 (TELESHIM targeting Middle East governments), hijacking hotel Wi-Fi DNS to steal Microsoft 365 credentials, and weaponizing AI agents—including the open-source Hermes agent in "YOLO" mode—to automate post-exploitation against Thailand's Ministry of Finance.

Supply chain and identity-based threats round out the landscape. ShinyHunters breach data fuels $2,000 Bitcoin sextortion campaigns, while slopsquatting attacks exploit AI-hallucinated package names to poison developer dependencies. GitHub and PyPI have responded with time-based Dependabot cooldowns. The DevMan RaaS platform demonstrates continued ransomware-as-a-service maturation with centralized affiliate portals. Credential stuffing hit Chick-fil-A (13,000+ accounts), and insurance phishing has evolved into real-time account hijacking. These developments collectively signal an acceleration in both vulnerability exploitation speed and the sophistication of social engineering, infrastructure abuse, and AI-augmented attack chains.

## Active Exploitation Details

### Fastjson 1.x Remote Code Execution (Zero-Day / Unpatched)
- **Description**: A critical flaw in Fastjson, Alibaba's JSON library for Java, allows attackers to achieve remote code execution in affected Spring Boot applications by sending a malicious JSON request. The vulnerability stems from unsafe deserialization that can be triggered without authentication.
- **Impact**: Attackers can execute arbitrary operating system commands on the server hosting the vulnerable application, leading to full system compromise, data theft, and lateral movement.
- **Status**: Actively exploited in the wild with **no patch available** as of reporting. Security firms ThreatBook and Imperva confirm ongoing attacks. Organizations using Fastjson 1.x in Spring Boot applications should implement immediate mitigations such as WAF rules, input validation, or library replacement.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Vulnerabilities in PTC Windchill and FlexPLM product lifecycle management platforms allow unauthenticated remote code execution on internet-exposed deployments.
- **Impact**: Attackers gain full control over affected servers without requiring credentials, enabling data exfiltration, ransomware deployment, and supply chain compromise of manufacturing and engineering organizations.
- **Status**: Actively exploited by Cl0p ransomware affiliates (tracked as Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest). Organizations with internet-accessible Windchill or FlexPLM instances should prioritize patching or network isolation immediately.

### Certighost Active Directory Privilege Escalation
- **Description**: The Certighost exploit allows a low-privileged Active Directory user to obtain a certificate for a Domain Controller machine account and authenticate as that Domain Controller, effectively achieving domain admin equivalence.
- **Impact**: Complete Active Directory compromise from any standard domain user account, enabling credential theft, persistence, and lateral movement across the domain.
- **Status**: Working exploit code published by researchers H0j3n and Aniq Fakhrul on July 24. No patch information provided in source; mitigation requires AD CS configuration hardening and monitoring for anomalous certificate requests.

### GitLab RCE (Authenticated)
- **Description**: A flaw in GitLab's self-managed instances allows authenticated users to execute arbitrary commands as the `git` system user. The vulnerability affects versions up to and including 18.11.3.
- **Impact**: Authenticated attackers (including low-privilege users) can achieve remote code execution on the GitLab server, accessing source code, CI/CD secrets, and potentially pivoting to underlying infrastructure.
- **Status**: Patched by GitLab on June 10; however, a working proof-of-concept exploit was publicly released by depthfirst researchers on July 24, significantly increasing exploitation risk for unpatched instances.

### n8n Expression-Sandbox Escape
- **Description**: A high-severity sandbox escape in n8n's expression evaluation system allows authenticated workflow editors to break out of the sandbox and execute arbitrary operating system commands on the host server.
- **Impact**: Workflow editors—potentially including compromised low-privilege accounts—can achieve full server compromise, accessing all workflows, credentials, and data processed by the automation platform.
- **Status**: Patched by n8n following responsible disclosure by Security Joes. Organizations should update to the latest version immediately.

### Check Point Exploit
- **Description**: Referenced in weekly threat recap as an actively exploited Check Point vulnerability. Specific technical details not provided in source article.
- **Impact**: Potential compromise of Check Point security appliances or management infrastructure.
- **Status**: Actively exploited per The Hacker News weekly recap. Administrators should check Check Point security advisories and apply any available patches.

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON Library for Java)**: All versions in the 1.x series when used in Spring Boot applications; no patched version available
- **PTC Windchill**: Internet-exposed deployments; specific vulnerable versions not disclosed in source
- **PTC FlexPLM**: Internet-exposed deployments; specific vulnerable versions not disclosed in source
- **Microsoft Active Directory**: Environments with Active Directory Certificate Services (AD CS) configured in vulnerable ways; all supported versions potentially affected
- **GitLab Self-Managed**: Versions 18.11.3 and earlier; patched in versions released after June 10
- **n8n Workflow Automation Platform**: Versions prior to the security patch released following Security Joes disclosure; specific version numbers not provided in source
- **Check Point Security Appliances/Management**: Specific products and versions not detailed in source; consult Check Point advisories
- **Steam Discussion Forums**: Platform abused as delivery mechanism for ClickFix attacks (not a software vulnerability in Steam itself)
- **Hotel/Conference Center Wi-Fi Infrastructure**: DNS configuration on network devices hijacked to redirect Microsoft 365 authentication

## Attack Vectors and Techniques

- **Browser-Assembled Malware (SourTrade Malvertising)**: Malicious advertisements deliver JavaScript that instructs the victim's browser to download legitimate Bun runtime components and assemble a Windows executable directly in memory, bypassing traditional file-based detection. Fake Solana, Luno, and TradingView pages used as lures.
- **ClickFix Social Engineering**: Attackers present fake error messages or "fixes" that trick users into copying and executing malicious PowerShell commands. Deployed via Steam forums (XMRig cryptominers), typosquatted Zoom/Teams domains (BlueNoroff), and Microsoft Teams-themed lures (Operation BlueDash).
- **BYOVD (Bring Your Own Vulnerable Driver)**: Cruciferra crypter loads a legitimate but vulnerable kernel driver to gain kernel-level privileges, then exploits it to disable security controls and execute shellcode.
- **Process Ghosting**: Technique used by Cruciferra to execute malware by deleting the executable file before the process creation callback fires, evading file-based security monitoring.
- **Legitimate RMM Tool Abuse**: Operation BlueDash delivers Level RMM and ScreenConnect—legitimate remote monitoring and management tools—via phishing, giving attackers persistent remote access without deploying custom malware.
- **Telegram C2 (TELESHIM)**: Threat actor uses Telegram bot API for command-and-control communications, blending malicious traffic with legitimate messaging infrastructure to evade detection.
- **DNS Hijacking on Public Wi-Fi**: Attackers compromise hotel/conference center Wi-Fi devices to modify DNS responses, redirecting Microsoft 365 login attempts to credential-harvesting pages.
- **AI Agent Automation (Hermes/YOL0 Mode)**: Threat actor uses open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation tasks including reconnaissance, credential access, and lateral movement during alleged breach of Thai Finance Ministry.
- **Slopsquatting / HalluSquatting**: Attackers register package, repository, or domain names hallucinated by AI coding assistants, waiting for developers or automated tools to reference these non-existent dependencies.
- **Time-Delayed Supply Chain Poisoning**: Malicious packages published to PyPI/npm; GitHub and PyPI now enforce 3-day Dependabot cooldowns to prevent immediate automated adoption.
- **Crypto Wallet Profiling Before Payload Delivery**: BlueNoroff phishing kit identifies and profiles cryptocurrency wallet browser extensions before delivering targeted malware.
- **Real-Time Phishing Account Hijacking**: Insurance-sector phishing evolved to proxy credentials in real-time, bypassing MFA by relaying authentication tokens instantly to attacker-controlled infrastructure.

## Threat Actor Activities

- **Cl0p Affiliates (Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest)**: Actively exploiting unauthenticated RCE in internet-exposed PTC Windchill and FlexPLM deployments as part of ransomware operations. Demonstrates continued focus on supply chain and manufacturing sector targets.
- **BlueNoroff (North Korean State-Sponsored)**: Operating ClickFix-style campaigns using typosquatted Zoom and Microsoft Teams domains; maintains active phishing kit that profiles cryptocurrency wallet extensions before delivering malware. Part of broader DPRK revenue-generation operations.
- **TELESHIM Operator (East Asia Nexus)**: Targeting government entities in the Middle East with custom malware using Telegram for C2. Fresh activity indicates ongoing espionage campaign.
- **Cruciferra Group (China-Linked Cybercrime)**: Deploying sophisticated crypter combining BYOVD and process ghosting; uses income tax-themed phishing lures targeting Indian taxpayers, tax professionals, and corporate finance teams.
- **ShinyHunters (Extortion Group)**: Data breaches attributed to this group are being leveraged by downstream actors for sextortion campaigns demanding $2,000 in Bitcoin per victim.
- **DevMan RaaS Operators**: Maintaining a dedicated web platform for ransomware-as-a-service affiliates, providing payload building, victim management, earnings tracking, and payout administration—indicating mature RaaS ecosystem.
- **Hermes AI Agent Operator (Unknown Attribution)**: Used open-source Hermes AI agent in autonomous "YOLO" mode to automate post-exploitation during alleged breach of Thailand's Ministry of Finance. Represents first reported use of AI agent for operational attack automation.
- **Operation BlueDash Operators (Unknown Attribution)**: Microsoft Teams-themed phishing campaign delivering legitimate RMM tools (Level RMM, ScreenConnect) via "secure document" lures. Infrastructure and attribution not publicly linked to known groups.
- **Hotel Wi-Fi DNS Hijackers (Unknown Attribution)**: Compromising network infrastructure at hotels and conference centers to redirect Microsoft 365 authentication to credential harvesting pages. Targets traveling executives and conference attendees.
- **Chick-fil-A Credential Stuffing Actors (Unknown Attribution)**: Automated credential stuffing against website and mobile app between June 17–19, compromising 13,000+ customer accounts using leaked credential pairs.

## Source Attribution

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
- **Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/
- **Vatican's Official Prayer App Leaks 700K+ Global Users' PII**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/vatican-official-prayer-app-leaks-700k-pii
- **Europol flags 4,340 URLs for removal in 'The Com' crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/europol-flags-4-340-urls-for-removal-in-the-com-crackdown/
