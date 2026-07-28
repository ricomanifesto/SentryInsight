# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors leveraging both zero-day vulnerabilities and recently disclosed flaws before organizations can patch. A maximum-severity command injection vulnerability in Arista VeloCloud Orchestrator (CVE-2026-16812) is under active exploitation in on-premises deployments, while a zero-day remote code execution flaw in the FastJson Java library is being used to target U.S. firms with no patch currently available. Simultaneously, proof-of-concept exploits for patched vulnerabilities in vBulletin and GitLab have been publicly released, lowering the barrier for widespread attacks against unpatched systems.

Threat actor operations demonstrate increasing sophistication and diversification. The Dysphoria IoT botnet has grown to approximately 200,000 compromised devices globally and has evolved to incorporate blockchain-based command-and-control infrastructure following law enforcement disruption. China-linked cybercrime groups are deploying advanced evasion techniques including BYOVD and process ghosting through the Cruciferra crypter, while East Asia-linked actors abuse Telegram for C2 in campaigns targeting Middle East governments. The ShinyHunters extortion group continues to monetize stolen data through sextortion campaigns and has claimed a supply-chain breach at Ernst & Young.

Novel attack techniques are emerging that bypass traditional defenses. Malvertising operations such as SourTrade now deliver malware in fragments that victim browsers reassemble into executable code using legitimate runtimes like Bun. ClickFix social engineering lures on platforms including Steam forums and fake Microsoft Teams updates are delivering remote access tools and cryptominers. Autonomous AI agents operating in unrestricted modes have been weaponized for espionage against government targets, signaling a new frontier in offensive automation.

## Active Exploitation Details

### Arista VeloCloud Orchestrator Command Injection (CVE-2026-16812)
- **Description**: A maximum-severity command injection vulnerability affecting on-premises deployments of Arista VeloCloud Orchestrator (VCO). The flaw allows unauthenticated attackers to execute arbitrary commands on the underlying system.
- **Impact**: Full system compromise of the VCO appliance, enabling attackers to pivot into managed networks, intercept traffic, and maintain persistent access to SD-WAN infrastructure.
- **Status**: Actively exploited in the wild. Arista has released patches for affected on-premises versions. Cloud-hosted VCO instances are not affected.
- **CVE ID**: CVE-2026-16812

### FastJson 1.x Remote Code Execution Zero-Day
- **Description**: A critical deserialization vulnerability in Alibaba's FastJson JSON library for Java (1.x versions). In affected Spring Boot applications, a malicious JSON request can trigger remote code execution without user interaction or elevated privileges.
- **Impact**: Unauthenticated remote code execution on any Java application using vulnerable FastJson versions, particularly Spring Boot services exposed to the internet.
- **Status**: Actively exploited in zero-day attacks targeting U.S. firms. No official patch is currently available from the FastJson project. ThreatBook and Imperva have confirmed active exploitation.
- **CVE ID**: Not explicitly assigned in source articles

### vBulletin Pre-Authentication Code Execution
- **Description**: An unauthenticated remote code execution flaw in vBulletin forum software where a crafted request can reach PHP's `eval()` function and execute arbitrary code on the server.
- **Impact**: Complete compromise of unpatched vBulletin forums, including database access, user credential theft, and server takeover.
- **Status**: Public exploit details released on July 27. The vulnerability was previously patched, but the public PoC significantly increases risk for unpatched installations.
- **CVE ID**: Not explicitly mentioned in source articles

### GitLab Authenticated Remote Code Execution
- **Description**: A vulnerability in GitLab self-managed instances that allows authenticated users to execute operating system commands as the `git` user through a crafted request.
- **Impact**: Command execution with the privileges of the GitLab application user, enabling repository theft, CI/CD pipeline manipulation, and lateral movement.
- **Status**: GitLab patched the flaw on June 10. A working proof-of-concept exploit was published by depthfirst researchers on July 24, six weeks after the patch.
- **CVE ID**: Not explicitly mentioned in source articles

### Certighost Active Directory Certificate Services Vulnerability
- **Description**: A vulnerability in Windows Active Directory Certificate Services (AD CS) that allows authenticated attackers to potentially compromise a Windows domain.
- **Impact**: Domain privilege escalation and potential full domain compromise from any authenticated domain user context.
- **Status**: A proof-of-concept exploit has been publicly released, enabling immediate weaponization against vulnerable AD CS configurations.
- **CVE ID**: Not explicitly mentioned in source articles

### n8n Workflow Automation Sandbox Escape
- **Description**: A high-severity expression-sandbox escape in the n8n workflow automation platform that allows authenticated workflow editors to execute operating system commands on the host server.
- **Impact**: Server compromise from a legitimate workflow editor account, enabling persistence, data exfiltration, and lateral movement.
- **Status**: n8n has released a patch. Discovered and reported by Security Joes researchers.
- **CVE ID**: Not explicitly mentioned in source articles

### Confused Deputy Vulnerabilities in Cloud Platforms
- **Description**: A class of vulnerabilities in Google Cloud and Microsoft Azure that allow attackers to acquire administrative-level permissions and bypass cloud providers' access controls by exploiting confused deputy scenarios.
- **Impact**: Privilege escalation to administrative roles in cloud environments, enabling resource hijacking, data access, and persistent footholds.
- **Status**: Persistent vulnerability class affecting both major cloud providers. No specific patch timeline mentioned; mitigation requires configuration hardening.
- **CVE ID**: Not explicitly mentioned in source articles

## Affected Systems and Products

- **Arista VeloCloud Orchestrator (on-premises)**: All on-premises VCO versions prior to the July 2026 security patch. Cloud-hosted VCO instances are not affected.
- **FastJson Java Library 1.x**: All 1.x versions of the Alibaba FastJson library when used in Spring Boot applications exposed to untrusted JSON input.
- **vBulletin Forum Software**: Unpatched vBulletin installations vulnerable to pre-authentication PHP `eval()` injection.
- **GitLab Self-Managed**: Versions 18.11.3 and earlier (patched in June 10 release). Only self-managed instances are affected; GitLab.com SaaS is not vulnerable.
- **Windows Active Directory Certificate Services**: Domain environments with vulnerable AD CS configurations exploitable by authenticated domain users.
- **n8n Workflow Automation Platform**: Versions prior to the July 2026 patch containing the sandbox escape fix.
- **Google Cloud Platform**: Services and configurations susceptible to confused deputy privilege escalation attacks.
- **Microsoft Azure**: Services and configurations susceptible to confused deputy privilege escalation attacks.
- **IoT Devices (Dysphoria Botnet)**: Approximately 200,000 compromised IoT devices worldwide, including routers, cameras, and other embedded systems.
- **Steam Discussion Forums**: Platform abused for ClickFix social engineering attacks delivering malware to gamers.
- **Microsoft Teams**: Brand impersonated in Operation BlueDash phishing campaigns delivering legitimate RMM tools.

## Attack Vectors and Techniques

- **Command Injection via Management Interfaces**: Exploitation of CVE-2026-16812 in Arista VCO through unauthenticated API endpoints allowing arbitrary OS command execution.
- **Java Deserialization/JSON Parsing RCE**: Malicious JSON payloads targeting FastJson's insecure deserialization in Spring Boot applications, requiring no authentication or user interaction.
- **PHP `eval()` Injection**: Crafted HTTP requests to unpatched vBulletin forums that reach PHP's `eval()` function for unauthenticated code execution.
- **Authenticated Command Execution via API**: Legitimate authenticated sessions abused in GitLab and n8n to escape sandbox restrictions and execute OS commands.
- **AD CS Misconfiguration Exploitation**: Authenticated domain users leveraging Certighost to escalate privileges through certificate template abuse or ESC vulnerability chains.
- **Confused Deputy Privilege Escalation**: Attackers manipulating cloud service-to-service authentication to assume elevated roles in Google Cloud and Azure.
- **Blockchain-Based Command & Control**: Dysphoria botnet using blockchain name services (e.g., Handshake, ENS) for resilient, censorship-resistant C2 infrastructure.
- **Victim Device Relay Networks**: Compromised IoT devices used as proxy relays to obscure attacker infrastructure and amplify DDoS traffic.
- **Browser-Based Malware Assembly (SourTrade)**: Malvertising delivers JavaScript that fetches encrypted payload fragments and uses the legitimate Bun runtime to decrypt and assemble a Windows executable entirely in browser memory.
- **ClickFix Social Engineering**: Fake error messages and "fix" buttons on Steam forums, fake Teams updates, and malvertising pages trick users into executing PowerShell commands that deploy malware.
- **Legitimate RMM Tool Abuse**: Operation BlueDash uses Microsoft Teams-themed phishing with "secure document" lures to install Level RMM and ScreenConnect for persistent remote access.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Cruciferra crypter loads signed but vulnerable kernel drivers to disable security tools and achieve kernel-level code execution.
- **Process Ghosting**: Malware execution technique where the executable image is deleted before the process starts, evading file-based detection and forensic analysis.
- **Telegram Abuse for C2**: TELESHIM malware uses Telegram Bot API and channels for command-and-control communications, blending with legitimate traffic.
- **Autonomous AI Agent Weaponization**: Hermes open-source AI agent run in unrestricted "YOLO mode" to autonomously conduct reconnaissance and espionage against Thailand's Ministry of Finance.
- **Supply-Chain Credential Theft**: ShinyHunters obtained Ernst & Young system credentials through a supply-chain attack vector.
- **Fake Application Distribution**: Fraudulent Sparrow Wallet crypto application distributed via Apple App Store stealing $1.8M in Bitcoin.

## Threat Actor Activities

- **Dysphoria Botnet Operators**: Built a 200,000-device IoT botnet for DDoS-for-hire and traffic relay services. Adapted infrastructure after March 2026 law enforcement disruption of JackSkid by adopting blockchain-based C2 and victim relay networks. Tracked by CNCERT and XLab.
- **China-Linked Cybercrime Group (Cruciferra)**: Uses income tax-themed phishing lures targeting Indian taxpayers, tax professionals, and corporate finance teams. Deploys Cruciferra crypter with BYOVD and process ghosting for advanced defense evasion on Windows.
- **East Asia-Linked Threat Actor (TELESHIM)**: Targets government entities in the Middle East. Uses Telegram for C2 communications. Intrusions have resulted in data theft and persistent access.
- **ShinyHunters Extortion Group**: Claimed responsibility for Ernst & Young data breach via supply-chain attack. Monetizes stolen breach data through $2,000 Bitcoin sextortion email campaigns. Active data leak and extortion operations.
- **LockBit Ransomware Affiliates**: Disrupted by multinational Operation Cronos (FBI-led). Affiliate trust erosion accelerated the group's takedown. Fairlife (Coca-Cola subsidiary) confirmed as recent victim of LockBit ransomware with data theft.
- **Operation BlueDash Operators**: Conduct Microsoft Teams-themed phishing campaigns using "secure document" lures to deploy legitimate RMM tools (Level RMM, ScreenConnect) for persistent access.
- **FastJson Zero-Day Attackers**: Actively targeting U.S. firms with RCE exploits against FastJson 1.x in Spring Boot applications. Identity unknown; exploitation ongoing with no patch available.
- **SourTrade Malvertising Operators**: Large-scale malvertising campaign using fake Solana, Luno, and TradingView webpages. Delivers malware via browser-based assembly using Bun runtime. Targets cryptocurrency and trading platform users.
- **Hermes AI Agent Operators**: Used autonomous open-source AI agent in unrestricted mode for espionage against Thailand's Ministry of Finance. Represents novel use of agentic AI for offensive operations.
- **vBulletin/GitLab Exploit Publishers**: Researchers (depthfirst for GitLab) publishing functional PoC exploits for recently patched vulnerabilities, accelerating weaponization timelines.

## Source Attribution

- **Microsoft Says New Cybersecurity AI Model Helps MDASH Hit 95.95% at Half the Cost**: The Hacker News - https://thehackernews.com/2026/07/microsoft-says-new-cybersecurity-ai.html
- **Attackers Exploit Arista VeloCloud Orchestrator Command Injection Flaw**: The Hacker News - https://thehackernews.com/2026/07/attackers-exploit-arista-velocloud.html
- **AI Agent Drives Espionage Attack on Thai Ministry of Finance**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-espionage-attack-thai-ministry-finance
- **Hackers target US firms in FastJson RCE zero-day attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-target-us-firms-in-fastjson-rce-zero-day-attacks/
- **Arista patches VeloCloud Orchestrator zero-day exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/arista-patches-velocloud-orchestrator-zero-day-exploited-in-attacks/
- **New Dysphoria DDoS botnet spreads to 200k devices worldwide**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-dysphoria-ddos-botnet-spreads-to-200k-devices-worldwide/
- **New Certighost PoC exploit lets attackers hijack Windows domains**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-certighost-poc-exploit-lets-attackers-hijack-windows-domains/
- **'Confused Deputy' Flaws Persist in Google Cloud, Microsoft Azure**: Dark Reading - https://www.darkreading.com/cloud-security/confused-deputy-flaws-google-cloud-microsoft-azure
- **FBI: Breaking Affiliate Trust Sped Along LockBit's Takedown**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/fbi-breaking-affiliate-trust-lockbit-takedown
- **NVIDIA Forms 37-Member Open Secure AI Alliance and Open-Sources NOOA Framework**: The Hacker News - https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html
- **Adversaries Don't Need a Zero-Day — They Read Your Rulebook**: Dark Reading - https://www.darkreading.com/threat-intelligence/adversaries-do-not-need-zero-day-they-read-your-rulebook
- **Apple sued over fake App Store crypto wallet app stealing $1.8M in Bitcoin**: Bleeping Computer - https://www.bleepingcomputer.com/news/apple/apple-sued-over-fake-app-store-crypto-wallet-app-stealing-18m-in-bitcoin/
- **Dysphoria IoT Botnet Adds Blockchain C2 and Victim Relays After JackSkid Disruption**: The Hacker News - https://thehackernews.com/2026/07/dysphoria-iot-botnet-adds-blockchain-c2.html
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
