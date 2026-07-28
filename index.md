# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from enterprise automation platforms and network orchestration systems to open-source libraries and cloud environments. The most severe ongoing campaigns involve a maximum-severity command injection zero-day in Arista VeloCloud Orchestrator (CVE-2026-16812) and a remote code execution zero-day in the FastJson Java library targeting U.S. organizations. Both flaws allow unauthenticated attackers to achieve full system compromise without user interaction. Simultaneously, a public exploit for a Linux kernel use-after-free (CVE-2026-53264) demonstrates reliable local privilege escalation to root on CentOS Stream 9, notably developed with AI assistance.

Threat actor activity has escalated in sophistication and diversity. The Dysphoria IoT botnet has grown to approximately 200,000 compromised devices globally, incorporating blockchain-based command-and-control infrastructure and victim relay networks following law enforcement disruption of the JackSkid operation. Nation-state-aligned campaigns are leveraging novel techniques: an East Asia-linked actor (TELESHIM) abuses Telegram for C2 against Middle Eastern governments, while a China-linked cybercrime group deploys the Cruciferra Crypter using BYOVD and Process Ghosting to target Indian financial sectors. Financially motivated groups remain prolific, with ShinyHunters claiming a supply-chain breach of Ernst & Young and LockBit affiliates disrupted through Operation Cronos. Meanwhile, social engineering campaigns such as Operation BlueDash (fake Microsoft Teams updates delivering legitimate RMM tools) and ClickFix lures on Steam forums (dropping XMRig miners) demonstrate the continued effectiveness of human-targeted initial access.

## Active Exploitation Details

### Arista VeloCloud Orchestrator Command Injection (CVE-2026-16812)
- **Description**: A maximum-severity command injection vulnerability in on-premises deployments of Arista VeloCloud Orchestrator (VCO). The flaw allows unauthenticated attackers to execute arbitrary operating system commands on the underlying server.
- **Impact**: Full compromise of the VCO appliance, potential lateral movement into managed SD-WAN infrastructure, and access to network traffic metadata and configuration data for all connected branch offices.
- **Status**: Actively exploited in the wild as a zero-day. Arista has released patches for affected on-premises versions. Cloud-hosted VCO instances are not affected.
- **CVE ID**: CVE-2026-16812

### FastJson Remote Code Execution Zero-Day
- **Description**: A remote code execution vulnerability in the FastJson open-source Java library. The flaw enables code execution without authentication, user interaction, or elevated privileges.
- **Impact**: Complete takeover of any Java application using vulnerable FastJson versions for JSON parsing. Attackers can deploy webshells, exfiltrate data, or pivot to internal networks.
- **Status**: Actively exploited in targeted attacks against U.S. firms. No patch was available at time of reporting; mitigation requires upgrading to a non-vulnerable FastJson version or removing the library.
- **CVE ID**: Not explicitly provided in source articles

### Linux Kernel Traffic Control Use-After-Free (CVE-2026-53264)
- **Description**: A use-after-free vulnerability in the Linux kernel's traffic control (tc) subsystem. STAR Labs researchers demonstrated a reliable exploit that escalates an ordinary local user to root on CentOS Stream 9. Notably, AI assistance was used to develop the exploit from the race condition primitive.
- **Impact**: Local privilege escalation to root on affected kernel builds. Allows any authenticated local user to gain full system control.
- **Status**: Public exploit code released. Affects CentOS Stream 9 kernel builds; upstream kernel patches may be available. CVSS 7.8 (High).
- **CVE ID**: CVE-2026-53264

### vBulletin Pre-Authentication Code Execution
- **Description**: A pre-authentication remote code execution flaw in vBulletin forum software. An unauthenticated HTTP request can reach PHP's `eval()` function, allowing arbitrary code execution on the forum server.
- **Impact**: Complete compromise of the forum server, access to user databases (credentials, PII, private messages), and potential pivot to connected infrastructure.
- **Status**: Vulnerability was previously patched; however, a public exploit with detailed technical analysis was released on July 27, 2026, significantly increasing risk for unpatched instances.
- **CVE ID**: Not explicitly provided in source articles

### n8n Expression Sandbox Escape
- **Description**: A high-severity sandbox escape in the n8n workflow automation platform. An authenticated user with workflow editor permissions can break out of the expression sandbox and execute arbitrary operating system commands as the n8n process user.
- **Impact**: Server-side code execution on the n8n host, potentially leading to credential theft (stored API keys, database credentials), lateral movement, and persistence.
- **Status**: Patched by n8n following responsible disclosure by Security Joes. Users should update to the latest version immediately.
- **CVE ID**: Not explicitly provided in source articles

### Certighost (Active Directory Certificate Services)
- **Description**: A vulnerability in Windows Active Directory Certificate Services (AD CS) that allows authenticated attackers to potentially compromise a Windows domain. A proof-of-concept exploit named "Certighost" has been publicly released.
- **Impact**: Domain compromise, privilege escalation to Domain Admin, certificate forgery, and persistence via golden certificates.
- **Status**: PoC exploit publicly available. Mitigation requires AD CS hardening, certificate template review, and monitoring for anomalous certificate enrollment.
- **CVE ID**: Not explicitly provided in source articles

### Confused Deputy Flaws (Google Cloud & Microsoft Azure)
- **Description**: A class of vulnerabilities in cloud identity and access management where a service (the "deputy") is tricked into performing privileged actions on behalf of an attacker by confusing its trust boundaries.
- **Impact**: Attackers can acquire administrative-level permissions and bypass cloud providers' access controls, leading to full subscription/project compromise, data exfiltration, and resource hijacking.
- **Status**: Persistent flaws affecting both Google Cloud and Microsoft Azure. Requires configuration reviews, least-privilege enforcement, and conditional access policies to mitigate.
- **CVE ID**: Not explicitly provided in source articles

### TeamCity Critical Authentication Bypass / RCE
- **Description**: A critical security issue in on-premise JetBrains TeamCity CI/CD servers that could result in arbitrary code execution without authentication.
- **Impact**: Full compromise of the build server, access to source code repositories, build artifacts, deployment credentials, and supply chain poisoning opportunities.
- **Status**: JetBrains urges immediate update to latest version. Active exploitation status not explicitly confirmed but urgency suggests high risk.
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **Arista VeloCloud Orchestrator (On-Premises)**: All on-premises VCO deployments prior to patched versions. Cloud-hosted VCO not affected.
- **FastJson Java Library**: Applications using vulnerable FastJson versions for JSON parsing. Specific version ranges not detailed in source articles.
- **Linux Kernel (CentOS Stream 9)**: CentOS Stream 9 kernel builds with traffic control subsystem enabled. Other distributions with similar kernel versions may be affected.
- **vBulletin Forum Software**: Unpatched vBulletin instances. Specific vulnerable versions not detailed in source articles.
- **n8n Workflow Automation Platform**: Self-hosted n8n instances prior to the patched release. Cloud/SaaS versions likely patched automatically.
- **Windows Active Directory Certificate Services**: Domain environments with misconfigured or vulnerable certificate templates. All supported Windows Server versions with AD CS role.
- **Google Cloud Platform**: Projects and organizations with vulnerable IAM configurations allowing confused deputy attacks.
- **Microsoft Azure**: Subscriptions and tenants with vulnerable role assignments and managed identity configurations.
- **JetBrains TeamCity (On-Premises)**: On-premise TeamCity servers prior to latest version. TeamCity Cloud not affected.
- **IoT Devices (Dysphoria Botnet)**: Approximately 200,000 compromised IoT devices globally, including routers, cameras, and embedded systems with weak credentials or unpatched vulnerabilities.
- **Steam Discussion Forums**: Steam community forums abused as delivery platform for ClickFix social engineering attacks targeting gamers.

## Attack Vectors and Techniques

- **Unauthenticated Command Injection (CVE-2026-16812)**: Direct HTTP requests to VeloCloud Orchestrator endpoints with crafted payloads achieving OS command execution as root.
- **Deserialization / Unsafe JSON Parsing (FastJson)**: Maliciously crafted JSON payloads triggering arbitrary class instantiation and method invocation during parsing, leading to RCE.
- **Kernel Use-After-Free Race Condition (CVE-2026-53264)**: Precise timing manipulation of traffic control netlink operations to free and reallocate kernel objects, enabling controlled kernel memory corruption and privilege escalation.
- **PHP `eval()` Injection (vBulletin)**: Unauthenticated requests reaching `eval()` with attacker-controlled input via insufficiently sanitized template or routing parameters.
- **Sandbox Escape via Expression Injection (n8n)**: Malicious workflow expressions that bypass the sandbox allow-list/deny-list mechanisms to access Java/Polyglot runtime internals and execute shell commands.
- **AD CS Certificate Template Abuse (Certighost)**: Exploitation of misconfigured certificate templates allowing low-privileged users to enroll certificates with domain-admin-equivalent privileges (e.g., Client Authentication + ENROLLEE_SUPPLIES_SUBJECT).
- **Confused Deputy / Cross-Account Impersonation (Cloud)**: Attackers induce cloud services to assume privileged roles via crafted requests that exploit overly permissive trust policies on service accounts or managed identities.
- **Phishing with Legitimate RMM Tools (Operation BlueDash)**: Microsoft Teams-themed lures delivering "secure document" links that install legitimate Remote Monitoring and Management tools (Level RMM, ScreenConnect) for persistent hands-on-keyboard access.
- **ClickFix Social Engineering (Steam Forums)**: Fake "fix" buttons on Steam discussion threads instruct victims to copy-paste PowerShell commands into Run dialog, executing XMRig cryptominer payloads.
- **Browser-Assembled Malware (SourTrade Malvertising)**: Malicious JavaScript on fake Solana/Luno/TradingView pages fetches encrypted payload chunks and uses the legitimate Bun runtime in the browser to decrypt, assemble, and execute a Windows PE in memory—no file download required.
- **BYOVD + Process Ghosting (Cruciferra Crypter)**: Bring Your Own Vulnerable Driver loads a signed but vulnerable kernel driver to disable security telemetry; Process Ghosting creates executable images from deleted files to evade file-based detection.
- **Telegram C2 (TELESHIM)**: Malware uses Telegram Bot API for command-and-control communications, blending with legitimate traffic and leveraging Telegram's encryption and infrastructure resilience.
- **Blockchain-Based C2 (Dysphoria Botnet)**: Botnet uses blockchain name services (e.g., ENS, Handshake) for resilient, censorship-resistant C2 domain resolution, supplemented by infected-device relay proxies.
- **AI-Assisted Exploit Development (CVE-2026-53264)**: Researchers leveraged AI tooling to transform a kernel race condition into a reliable, weaponized local root exploit, lowering the barrier for complex vulnerability exploitation.
- **Autonomous AI Agent Operations (Hermes/YOLO Mode)**: Attackers deployed the open-source Hermes AI agent in unrestricted "YOLO mode" to autonomously conduct reconnaissance, lateral movement, and data exfiltration against the Thai Ministry of Finance.
- **Supply Chain Credential Theft (ShinyHunters / EY)**: Compromise of a third-party supplier yielded valid credentials for Ernst & Young systems, enabling data access and extortion.

## Threat Actor Activities

- **Dysphoria Botnet Operators**: Maintain a ~200,000-device IoT botnet used for DDoS-for-hire and traffic relay/proxy services. Adapted infrastructure after March 2026 law enforcement action against JackSkid, adopting blockchain-based naming (ENS/Handshake) for C2 resilience and victim-device relay networks for obfuscation. Tracked by CNCERT and XLab.
- **ShinyHunters Extortion Gang**: Claimed responsibility for Ernst & Young data breach via supply-chain credential theft. Operates as a data-theft-and-extortion group rather than ransomware, leveraging stolen credentials for access and public shaming for leverage.
- **LockBit Ransomware Affiliates (Disrupted)**: Previously the largest ransomware-as-a-service operation. Operation Cronos (multinational law enforcement) disrupted infrastructure and eroded affiliate trust, accelerating the group's decline. FBI notes affiliate distrust was pivotal.
- **Operation BlueDash Operators**: Conduct Microsoft Teams-themed phishing campaigns delivering legitimate RMM tools (Level, ScreenConnect) via "secure document" social engineering lures. Focus on persistent remote access for follow-on exploitation.
- **China-Linked Cybercrime Group (Cruciferra Crypter)**: Uses income tax-themed phishing lures targeting Indian taxpayers, tax professionals, and corporate finance teams. Deploys Cruciferra Crypter with BYOVD (CVE-2024-21523 or similar vulnerable drivers) and Process Ghosting for defense evasion.
- **East Asia-Linked Threat Actor (TELESHIM)**: Targets government entities in the Middle East. Uses Telegram for C2 communications. Intrusions result in credential theft, data exfiltration, and persistent access.
- **FastJson Zero-Day Attackers**: Actively targeting U.S. firms with RCE exploits against FastJson-powered applications. Attribution unknown; campaign appears opportunistic or broadly targeted.
- **SourTrade Malvertising Operators**: Run large-scale malvertising campaign (fake Solana, Luno, TradingView pages) delivering browser-assembled malware via Bun runtime. Targets cryptocurrency and trading platform users.
- **ClickFix Campaign Operators (Steam)**: Abuse Steam discussion forums to deliver XMRig cryptominers via fake "fix" instructions. Targets gamers seeking technical support.
- **Hermes AI Agent Operators (Thai Ministry of Finance)**: Deployed autonomous Hermes agent in "YOLO mode" for espionage against Thailand's Ministry of Finance. Represents early observed use of fully autonomous AI agents in real-world intrusion operations.
- **Coca-Cola / Fairlife Ransomware Actors**: Conducted ransomware attack on Fairlife (Coca-Cola subsidiary) with data theft. Ransomware group not named in source articles.

## Source Attribution

- **Data breach at medical billing firm MCBS affects 1.26 million people**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/data-breach-at-medical-billing-firm-mcbs-affects-126-million-people/
- **Critical TeamCity Flaw Could Let Attackers Run OS Commands Without Logging In**: The Hacker News - https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html
- **Researcher Says AI Helped Develop Linux Traffic-Control Race Into Root Exploit**: The Hacker News - https://thehackernews.com/2026/07/researcher-says-ai-helped-develop-linux.html
- **Microsoft Says New Cybersecurity AI Model Helps MDASH Score 95.95% at Half the Cost**: The Hacker News - https://thehackernews.com/2026/07/microsoft-says-new-cybersecurity-ai.html
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
