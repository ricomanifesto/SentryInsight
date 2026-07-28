# Exploitation Report

## Executive Summary

Threat actors are leveraging a diverse arsenal of zero-day vulnerabilities, newly released proof-of-concept exploits, and sophisticated social engineering campaigns to compromise high-value targets across multiple sectors. Notably, an autonomous AI agent operating in unrestricted "YOLO mode" conducted espionage against Thailand's Ministry of Finance, marking a significant evolution in AI-driven offensive operations. Simultaneously, critical zero-day vulnerabilities in widely deployed infrastructure—including FastJson Java library, Arista VeloCloud Orchestrator, and PTC Windchill/FlexPLM—are under active exploitation with limited or no patches available, exposing enterprises to immediate remote code execution risk.

The exploitation landscape is further complicated by the rapid weaponization of recently disclosed flaws. Public exploit code for vBulletin pre-authentication code execution and GitLab RCE vulnerabilities has lowered the barrier for opportunistic attacks, while the Certighost Active Directory Certificate Services PoC enables domain compromise by authenticated users. Threat actors including Cl0p affiliates, China-linked cybercrime groups, and East Asian state-aligned operators are actively scanning for and exploiting internet-exposed vulnerable systems, often combining technical exploits with advanced evasion techniques such as BYOVD, process ghosting, and blockchain-based command-and-control infrastructure.

Ransomware and extortion operations continue to evolve, with LockBit disrupted through affiliate trust manipulation while ShinyHunters leverages breached data for sextortion campaigns and supply-chain intrusions. Emerging attack vectors—including browser-based malware assembly via malvertising, ClickFix social engineering on gaming platforms, and AI agent abuse—demonstrate adversaries' adaptability in bypassing traditional defenses. Organizations must prioritize patching of actively exploited vulnerabilities, implement strict controls on autonomous AI tools, and enhance monitoring for living-off-the-land and browser-based attack techniques.

## Active Exploitation Details

### FastJson RCE Zero-Day
- **Description**: A critical remote code execution vulnerability in the FastJson open-source Java library (Alibaba's JSON parser for Java) that allows unauthenticated attackers to execute arbitrary code by sending malicious JSON requests. The flaw affects FastJson 1.x versions and is exploitable in Spring Boot applications without user interaction or elevated privileges.
- **Impact**: Full remote code execution on affected Java applications, enabling complete system compromise, data theft, and lateral movement.
- **Status**: Actively exploited in the wild against US firms. No patch currently available for FastJson 1.x; mitigation requires upgrading to FastJson 2.x or implementing strict input validation.

### Arista VeloCloud Orchestrator Command Injection Zero-Day
- **Description**: A maximum-severity command injection vulnerability in on-premises deployments of Arista's VeloCloud Orchestrator (SD-WAN management platform).
- **Impact**: Unauthenticated remote command execution with root privileges on the orchestration platform, potentially compromising entire SD-WAN infrastructures.
- **Status**: Actively exploited in attacks. Arista has released patches for affected on-premises deployments.

### Certighost (Active Directory Certificate Services Vulnerability)
- **Description**: A vulnerability in Windows Active Directory Certificate Services (AD CS) that allows authenticated attackers to potentially compromise entire Windows domains. A proof-of-concept exploit has been publicly released.
- **Impact**: Domain escalation and full Active Directory compromise from any authenticated user context.
- **Status**: PoC exploit publicly available; organizations should audit AD CS configurations and apply Microsoft guidance immediately.

### vBulletin Pre-Auth Code Execution Flaw
- **Description**: An unauthenticated remote code execution vulnerability in vBulletin forum software where a crafted request reaches PHP's `eval()` function, allowing arbitrary code execution on the server.
- **Impact**: Complete compromise of unpatched vBulletin forum servers without requiring authentication.
- **Status**: Vulnerability was previously patched; public exploit details released on July 27 significantly increase exploitation risk for unpatched instances.

### n8n Sandbox Escape
- **Description**: A high-severity expression-sandbox escape in the n8n workflow automation platform that allows authenticated workflow editors to execute operating system commands on the underlying server.
- **Impact**: Remote code execution as the n8n process user, enabling server compromise and potential lateral movement.
- **Status**: Patched by n8n; Security Joes researchers discovered and reported the flaw.

### GitLab RCE (Authenticated)
- **Description**: A remote code execution vulnerability in GitLab self-managed instances (versions 18.11.3 and later) that allows authenticated users to run arbitrary commands as the `git` user.
- **Impact**: Code execution on GitLab servers with the privileges of the git user, potentially accessing source code, CI/CD pipelines, and sensitive tokens.
- **Status**: Patched by GitLab on June 10; proof-of-concept exploit published by depthfirst researchers on July 24.

### PTC Windchill and FlexPLM Unauthenticated RCE
- **Description**: Unauthenticated remote code execution vulnerabilities in internet-exposed deployments of PTC Windchill and FlexPLM product lifecycle management (PLM) software.
- **Impact**: Full server compromise without authentication, providing access to intellectual property, design data, and corporate networks.
- **Status**: Actively exploited by Cl0p ransomware affiliates; organizations with internet-exposed instances at immediate risk.

### Confused Deputy Vulnerabilities (Google Cloud, Microsoft Azure)
- **Description**: A class of vulnerabilities in cloud identity and access management systems where attackers can confuse a privileged service into performing actions on their behalf, bypassing access controls.
- **Impact**: Administrative-level permission acquisition and bypass of cloud provider security boundaries.
- **Status**: Persistent flaws affecting both Google Cloud and Microsoft Azure; requires configuration hardening and least-privilege enforcement.

## Affected Systems and Products

- **FastJson Java Library (1.x)**: All Spring Boot applications using FastJson 1.x for JSON parsing; Java-based web services and microservices
- **Arista VeloCloud Orchestrator (On-Premises)**: SD-WAN management platforms deployed on-premises; network orchestration infrastructure
- **Windows Active Directory Certificate Services (AD CS)**: Enterprise Windows domains with misconfigured or vulnerable certificate templates
- **vBulletin Forum Software**: Self-hosted vBulletin installations prior to patched versions; community forums and discussion boards
- **n8n Workflow Automation Platform**: Self-hosted n8n instances; automation and integration servers
- **GitLab Self-Managed (18.11.3+)**: On-premises GitLab deployments; source code management and CI/CD infrastructure
- **PTC Windchill and FlexPLM**: Internet-exposed PLM deployments; manufacturing, engineering, and product development environments
- **Google Cloud Platform**: IAM configurations vulnerable to confused deputy attacks; service accounts with excessive permissions
- **Microsoft Azure**: Entra ID and resource management configurations susceptible to confused deputy exploitation
- **IoT Devices (Dysphoria Botnet)**: Approximately 200,000 compromised IoT devices worldwide; routers, cameras, and embedded systems

## Attack Vectors and Techniques

- **Autonomous AI Agent Operations**: Attackers deploying Hermes open-source AI agent in unrestricted "YOLO mode" for hands-off espionage, enabling automated reconnaissance, lateral movement, and data exfiltration without human intervention.
- **Malicious JSON Deserialization**: Crafted JSON payloads exploiting FastJson's insecure deserialization to achieve RCE in Java applications; no user interaction required.
- **Command Injection via SD-WAN Management**: Exploitation of VeloCloud Orchestrator's command injection flaw for root-level access to network orchestration platforms.
- **AD CS Certificate Abuse**: Leveraging Certighost vulnerability to manipulate certificate templates and escalate to domain administrator privileges.
- **PHP eval() Injection**: Unauthenticated requests reaching PHP's `eval()` function in vBulletin for pre-authentication code execution.
- **Expression Sandbox Escape**: Authenticated workflow editors breaking out of n8n's expression sandbox to execute OS commands.
- **GitLab Command Execution**: Authenticated users exploiting GitLab flaw to run commands as the git user on self-managed instances.
- **Unauthenticated PLM Exploitation**: Cl0p affiliates scanning for and exploiting internet-exposed PTC Windchill/FlexPLM instances without credentials.
- **Confused Deputy Cloud Attacks**: Manipulating cloud services to perform privileged actions on behalf of attackers through permission confusion.
- **Blockchain-Based C2 (Dysphoria)**: Botnet using blockchain name services (e.g., Handshake) for resilient command-and-control infrastructure resistant to takedown.
- **Infected-Device Relays (Dysphoria)**: Compromised IoT devices used as traffic relays to obfuscate attack origins and bypass geo-blocking.
- **BYOVD (Bring Your Own Vulnerable Driver)**: China-linked actors loading signed but vulnerable kernel drivers to disable security tools and execute kernel-level code.
- **Process Ghosting**: Advanced evasion technique where malware executes from a deleted file image, avoiding disk-based detection.
- **Telegram C2 (TELESHIM)**: East Asian threat actors abusing Telegram's API for command-and-control communications targeting Middle Eastern governments.
- **ClickFix Social Engineering**: Fake "fix" prompts on Steam forums and other platforms tricking users into executing malicious PowerShell commands.
- **Browser-Based Malware Assembly (SourTrade)**: Malvertising delivering malware in pieces; victim's browser assembles executable using legitimate Bun runtime.
- **In-Memory JavaScript Malware Construction**: Malicious JavaScript on fake Solana/Luno/TradingView pages building malware directly in browser memory.
- **Supply-Chain Credential Theft**: ShinyHunters obtaining system credentials through supply-chain compromise for downstream extortion.
- **Fake Application Distribution**: Trojanized cryptocurrency wallet apps (Sparrow Wallet) distributed via official App Store.
- **Phishing with Legitimate RMM Tools**: Operation BlueDash using Microsoft Teams-themed lures to deploy Level RMM and ScreenConnect for persistent access.
- **Real-Time Account Hijacking**: Evolved insurance phishing enabling immediate session takeover rather than credential harvesting.

## Threat Actor Activities

- **China-Linked Cybercrime Group (Cruciferra)**: Deploying sophisticated crypter using BYOVD and process ghosting in income tax-themed phishing campaigns targeting Indian taxpayers, tax professionals, and corporate finance teams.
- **Cl0p Affiliates (Chubby Scorpius/FIN11/Graceful Spider/Lace Tempest)**: Actively scanning for and exploiting internet-exposed PTC Windchill and FlexPLM deployments via unauthenticated RCE for ransomware deployment and data theft.
- **ShinyHunters Extortion Gang**: Claimed responsibility for Ernst & Young data breach via supply-chain attack; leaked data fueling $2,000 sextortion email campaigns demanding Bitcoin payment.
- **East Asian State-Aligned Actor (TELESHIM)**: Targeting Middle Eastern government entities using Telegram for C2; conducting espionage operations with custom tooling.
- **Dysphoria Botnet Operators (tracked by CNCERT/XLab)**: Managing ~200,000 compromised IoT devices globally for DDoS attacks and traffic relay; adopted blockchain C2 and victim relays after March JackSkid law-enforcement disruption.
- **LockBit Ransomware Affiliates**: Disrupted through FBI's Operation Cronos which exploited trust breakdowns among affiliates; previously largest ransomware operation.
- **Operation BlueDash Operators**: Conducting Microsoft Teams-themed phishing with "secure document" lures to deploy legitimate RMM tools (Level RMM, ScreenConnect) for persistent remote access.
- **SourTrade Malvertising Group**: Operating browser-based malware assembly campaigns using legitimate Bun runtime to evade traditional payload delivery detection.
- **Unknown Actors (FastJson Exploitation)**: Actively targeting US firms with FastJson zero-day exploits; attribution not publicly disclosed.
- **Unknown Actors (VeloCloud Exploitation)**: Exploiting Arista zero-day before patch availability; targeting SD-WAN infrastructure.

## Source Attribution

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
- **CTM360 Research Reveals How Insurance Phishing Has Evolved Into Real-Time Account Hijacking**: The Hacker News - https://thehackernews.com/2026/07/ctm360-research-reveals-how-insurance.html
- **Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE**: The Hacker News - https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
