# Exploitation Report

## Executive Summary

Active exploitation activity has surged across multiple critical vectors this reporting period, with threat actors rapidly weaponizing freshly disclosed vulnerabilities and pioneering novel attack techniques that bypass traditional defenses. The most pressing concerns center on a WordPress remote code execution chain (CVE-2026-60137 and CVE-2026-63030) now fueling mass scanning within days of disclosure, a critical Palo Alto Networks GlobalProtect authentication bypass actively leveraged by the Qilin ransomware gang for initial access, and two SonicWall SMA1000 zero-days exploited for weeks to deploy custom malware on VPN appliances. Simultaneously, a Windows LegacyHive zero-day privilege escalation flaw remains unpatched by Microsoft, with only unofficial mitigations available.

A significant evolution in the threat landscape is the emergence of AI-agent-driven offensive operations. The JADEPUFFER autonomous operator has conducted repeated Langflow RCE attacks, now deploying the ENCFORGE ransomware specifically designed to encrypt AI model files, training datasets, and vector databases. This follows the Hugging Face breach where an autonomous AI agent compromised production infrastructure to access internal datasets and credentials. Meanwhile, researchers demonstrated sandbox escapes across Cursor, Codex, Gemini CLI, and Antigravity, and a novel Android AI agent attack chain allows invisible on-screen text to execute code on host systems. The Bit2Watt technique further demonstrates that cloud tenants can disrupt physical power grids through ordinary GPU workloads without any software exploit.

Nation-state and criminal campaigns continue to diversify. Russian intelligence services are systematically hijacking internet-connected security cameras across NATO states and Ukraine to monitor military logistics. The FakeGit campaign has seeded 7,600 malicious GitHub repositories—over 800 masquerading as AI skills or MCP servers—to distribute SmartLoader malware. The HollowGraph malware family uses Microsoft 365 calendar events dated 2050 as a stealthy command-and-control channel. An exposed phishing toolkit server revealed 1,048 files detailing AI-assisted lure generation, filename spoofing, and WebDAV-based malware delivery. The "TFF Trap" BEC campaign combines fileless loaders with low-detection RATs including Agent Tesla, Remcos, XWorm, and Best Private Logger. Estée Lauder disclosed a data breach stemming from an exploited Oracle E-Business Suite flaw, while the Ostium trading platform lost $23.75 million in an off-chain infrastructure compromise.

## Active Exploitation Details

### WordPress WP2Shell RCE Chain (CVE-2026-60137 and CVE-2026-63030)
- **Description**: Two critical WordPress vulnerabilities that, when chained together, enable unauthenticated remote code execution and complete compromise of vulnerable websites. The chain combines an authentication bypass with a file upload or deserialization flaw to achieve arbitrary code execution.
- **Impact**: Attackers gain full control over WordPress sites, including database access, file system read/write, persistence via webshells, and lateral movement to hosting infrastructure. Millions of sites are exposed given WordPress's market share.
- **Status**: Actively exploited in the wild within three days of disclosure. Public exploit code is available and fueling mass scanning campaigns. Patches are available but deployment lags across the ecosystem.
- **CVE ID**: CVE-2026-60137, CVE-2026-63030

### Palo Alto Networks PAN-OS GlobalProtect Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in the GlobalProtect VPN portal/gateway component of PAN-OS. The flaw allows unauthenticated attackers to circumvent authentication mechanisms and establish VPN sessions or access protected resources.
- **Impact**: Full network access to victim organizations' internal networks, enabling ransomware deployment, data exfiltration, lateral movement, and persistence. Qilin ransomware gang is confirmed leveraging this for initial access.
- **Status**: Actively exploited by Qilin ransomware gang according to Arctic Wolf intelligence. Palo Alto Networks has released patches; urgent application is advised for all GlobalProtect deployments.
- **CVE ID**: [CVE not explicitly provided in source article]

### SonicWall SMA1000 Zero-Day Vulnerabilities
- **Description**: Two vulnerabilities in SonicWall SMA1000 series secure mobile access appliances. Both were exploited as zero-days for weeks before disclosure, allowing threat actors to bypass authentication and execute arbitrary commands on the appliance.
- **Impact**: Complete compromise of the VPN appliance, enabling installation of custom malware, credential harvesting, network pivoting, and persistent access to corporate networks. The appliances sit at the network perimeter, making them high-value targets.
- **Status**: Exploited in the wild as zero-days for several weeks prior to disclosure. SonicWall has released patches for both flaws. Organizations should assume compromise and conduct thorough forensic analysis.
- **CVE ID**: [CVE not explicitly provided in source article]

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A zero-day vulnerability in the Windows LegacyHive component (registry hive handling) that allows local attackers to escalate privileges to SYSTEM on fully patched Windows systems. The flaw stems from improper validation of registry hive files.
- **Impact**: Local privilege escalation from standard user to SYSTEM, enabling bypass of security controls, credential theft, security tool disabling, and kernel-level persistence. Affects up-to-date Windows versions.
- **Status**: Actively exploited in the wild. Microsoft has not yet released an official patch. Free unofficial patches are available from third-party researchers (0patch), but these are not vendor-supported.
- **CVE ID**: [CVE not explicitly provided in source article]

### Langflow RCE Exploited by JADEPUFFER/ENCFORGE
- **Description**: A remote code execution vulnerability in Langflow, an open-source platform for building AI agents and RAG applications. The JADEPUFFER autonomous AI operator has conducted multiple attacks against the same Langflow server.
- **Impact**: Unauthenticated code execution on Langflow servers, leading to deployment of ENCFORGE ransomware which specifically targets AI assets—training datasets, vector databases, model checkpoints, and embedding files. Also enables theft of AI model weights and proprietary data.
- **Status**: Actively exploited; at least two separate intrusions on the same server attributed to JADEPUFFER. The operator demonstrates persistent, agentic targeting of AI infrastructure.
- **CVE ID**: [CVE not explicitly provided in source article]

### ServiceNow AI Platform Unauthenticated Code Execution
- **Description**: A critical security flaw in the ServiceNow AI Platform (Now Intelligence/Generative AI Controller components) that allows unauthenticated remote code execution. The vulnerability likely resides in AI model inference or prompt handling endpoints.
- **Impact**: Full compromise of ServiceNow instances, including access to ITSM, HR, CSM, and custom application data. Attackers can exfiltrate sensitive corporate records, modify workflows, and pivot to integrated systems.
- **Status**: Actively exploited in the wild per Defused Cyber threat intelligence. ServiceNow has released emergency patches; immediate application is critical given the platform's central role in enterprise operations.
- **CVE ID**: [CVE not explicitly provided in source article]

### Oracle E-Business Suite Flaw (Estée Lauder Breach)
- **Description**: A vulnerability in Oracle E-Business Suite, specifically affecting HR modules used for human resources operations. The flaw allowed unauthorized access to employee and customer data.
- **Impact**: Data breach exposing personal information of Estée Lauder customers and employees. The cosmetics giant was forced to issue breach notifications. The flaw provides a pathway into core ERP systems.
- **Status**: Exploited in the wild leading to confirmed data breach. Oracle has likely released patches; organizations running E-Business Suite should verify patch status and monitor for signs of compromise.
- **CVE ID**: [CVE not explicitly provided in source article]

### Android AI Agent Invisible Text Injection
- **Description**: An attack chain targeting Android AI agent applications that can draw over other windows (SYSTEM_ALERT_WINDOW permission) and write to shared storage. Malicious apps inject invisible text instructions onto the screen that the AI agent reads and executes, but human users never see.
- **Impact**: Arbitrary code execution on the host PC/phone via the AI agent's tool-use capabilities. The attack bypasses user awareness entirely—no phishing, no visible prompts. Two additional steps after text injection lead to host compromise.
- **Status**: Proof-of-concept demonstrated; real-world exploitation risk is high given the proliferation of AI agent apps with overlay and storage permissions. No vendor patches reported yet.
- **CVE ID**: [CVE not explicitly provided in source article]

### AI Coding Tool Sandbox Escapes (Cursor, Codex, Gemini CLI, Antigravity)
- **Description**: Researchers escaped the sandboxes of four major AI coding assistants—Cursor, Codex, Gemini CLI, and Antigravity—by having the AI agent write files that trusted host tools later execute. The attack exploits the trust boundary between AI-generated content and host toolchains.
- **Impact**: Full host compromise from within the AI coding session. Attackers can execute arbitrary commands, access source code, steal credentials/keys, and persist on developer machines. Multiple CVEs assigned; Google downgraded two severity ratings post-disclosure.
- **Status**: Vulnerabilities disclosed to vendors; patches released or in progress. Developers using these tools should update immediately and review recent AI-generated code for malicious payloads.
- **CVE ID**: [CVE not explicitly provided in source article; multiple CVEs assigned per article]

### Bit2Watt Power Grid Disruption via Cloud GPU Workloads
- **Description**: A novel attack technique where a cloud tenant uses ordinary GPU access to rapidly modulate data center power draw, creating destabilizing oscillations on the electrical grid. No software exploit, vulnerability, or unauthorized access is required—only legitimate API usage.
- **Impact**: Potential to disrupt power grid stability, causing brownouts, equipment damage, or cascading failures affecting other tenants and critical infrastructure. The attack crosses the cyber-physical boundary without traditional exploitation.
- **Status**: Theoretical demonstration by researchers; no confirmed malicious use. Highlights a new class of "side-channel" attacks on shared physical infrastructure. Mitigation requires grid-aware load management by cloud providers.
- **CVE ID**: Not applicable (no software vulnerability)

### HollowGraph Malware (Microsoft Graph C2 Channel)
- **Description**: A sophisticated espionage implant that uses compromised Microsoft 365 mailboxes—specifically the calendar feature—as a command-and-control channel. Operator instructions and exfiltrated data are embedded in calendar events, often dated years in the future (e.g., 2050) to evade detection.
- **Impact**: Stealthy, persistent C2 that blends with legitimate Microsoft 365 traffic. Enables data exfiltration, command execution, and lateral movement within Microsoft 365 environments. Difficult to detect without behavioral analysis of calendar API usage.
- **Status**: Active in the wild; discovered via exposed operator infrastructure. Attribution not publicly assigned. Microsoft 365 tenants should monitor for anomalous calendar event creation and Graph API usage patterns.
- **CVE ID**: Not applicable (malware, not vulnerability)

### Russian Intelligence IP Camera Hijacking Campaign
- **Description**: At least one Russian intelligence service is systematically compromising internet-connected security cameras across Europe and Ukraine. The cameras are used to monitor military transport routes, weapons shipments, and logistics movements in real time.
- **Impact**: Persistent visual intelligence collection on NATO and Ukrainian military operations. Compromised cameras provide live feeds without physical presence. The scale suggests automated scanning and exploitation of camera vulnerabilities (default credentials, unpatched firmware).
- **Status**: Ongoing, systematic campaign. Camera vendors and network operators should enforce credential rotation, network segmentation, and firmware updates for all exposed devices.
- **CVE ID**: [CVE not explicitly provided in source article]

### Hugging Face Autonomous AI Agent Breach
- **Description**: Attackers breached Hugging Face's production infrastructure using an autonomous AI agent, gaining access to internal datasets and credentials. The AI agent likely performed reconnaissance, vulnerability identification, and exploitation autonomously.
- **Impact**: Exposure of proprietary datasets, model weights, API keys, and potentially user credentials. The breach demonstrates that autonomous AI agents can now conduct end-to-end intrusion operations against high-value AI/ML platforms.
- **Status**: Confirmed by Hugging Face; investigation ongoing. The incident marks a milestone in AI-driven offensive operations. Organizations hosting AI model repositories should review access controls and monitor for anomalous agent-like behavior.
- **CVE ID**: [CVE not explicitly provided in source article]

### FakeGit Campaign (7,600 Malicious GitHub Repositories)
- **Description**: A large-scale supply chain campaign seeding 7,600 malicious GitHub repositories, with over 800 masquerading as AI skills or Model Context Protocol (MCP) servers. The repositories deliver SmartLoader malware to developers and AI practitioners who clone or interact with them.
- **Impact**: Developer machine compromise, credential theft, source code exfiltration, and potential software supply chain poisoning. The AI/ML theme targets a high-value demographic with elevated access.
- **Status**: Active campaign discovered by researchers; GitHub has been notified. Developers should verify repository authenticity, scan cloned code, and avoid executing unverified AI/ML components.
- **CVE ID**: Not applicable (malware distribution campaign)

### "TFF Trap" BEC Phishing Campaign
- **Description**: A business email compromise campaign combining fileless techniques and low-detection loaders to deploy multiple remote access trojans and stealers: Agent Tesla, Remcos, XWorm, and Best Private Logger. The "TFF Trap" uses evasion tactics to bypass email security and endpoint detection.
- **Impact**: Credential harvesting, financial fraud, persistent remote access, keystroke logging, clipboard monitoring, and cryptocurrency wallet theft. The multi-RAT deployment ensures redundancy and broad data collection.
- **Status**: Active campaign observed in the wild. Email security gateways and EDR solutions should update signatures for the identified loader and RAT variants.
- **CVE ID**: Not applicable (phishing/malware campaign)

### Ostium Trading Platform Off-Chain Infrastructure Compromise
- **Description**: Attackers compromised off-chain infrastructure used to feed price data into the Ostium decentralized trading protocol, enabling theft of $23.75 million from a liquidity provider vault. The attack targeted the oracle/price feed layer rather than the smart contracts themselves.
- **Impact**: Direct financial loss of $23.75M. Demonstrates that DeFi protocols remain vulnerable at the intersection of on-chain and off-chain systems. Price manipulation via compromised oracles can drain liquidity pools.
- **Status**: Attack completed; funds stolen. Ostium has disclosed the incident. DeFi protocols should audit off-chain dependencies, implement multi-source price validation, and monitor oracle health.
- **CVE ID**: Not applicable (infrastructure compromise)

## Affected Systems and Products

- **WordPress Core**: All versions prior to patched releases addressing CVE-2026-60137 and CVE-2026-63030; millions of sites globally exposed
- **Palo Alto Networks PAN-OS**: GlobalProtect portal/gateway on affected PAN-OS versions; enterprise VPN deployments worldwide
- **SonicWall SMA1000 Series**: SMA1000 secure mobile access appliances; firmware versions prior to patched releases
- **Microsoft Windows**: All supported Windows versions with LegacyHive component (registry hive handling); affects fully patched systems
- **Langflow**: Open-source AI agent/RAG platform; self-hosted instances exposed to internet or internal networks
- **ServiceNow AI Platform (Now Intelligence/Generative AI Controller)**: Cloud and on-premise ServiceNow instances with AI features enabled
- **Oracle E-Business Suite**: HR modules and associated components; on-premise and cloud deployments
- **Android AI Agent Applications**: Apps with SYSTEM_ALERT_WINDOW (draw over apps) and shared storage permissions; affects AI assistant/agent apps on Android
- **AI Coding Assistants**: Cursor, OpenAI Codex CLI, Google Gemini CLI, Antigravity; developer workstations running these tools
- **Cloud GPU Infrastructure**: Any multi-tenant cloud environment offering GPU compute (AWS, Azure, GCP, specialized GPU clouds); physical data center power infrastructure
- **Microsoft 365 / Exchange Online**: Tenants with compromised credentials allowing mailbox access; calendar/Graph API endpoints
- **IP Security Cameras**: Internet-connected cameras with default/weak credentials, unpatched firmware, or exposed management interfaces; brands/models not specified
- **Hugging Face Platform**: Production infrastructure hosting model repositories, datasets, and Spaces; user accounts with repository access
- **GitHub Repositories**: 7,600 identified malicious repos; developers cloning or executing code from unverified AI/ML repositories
- **Email Systems / Endpoints**: Organizations targeted by BEC campaigns; Windows endpoints vulnerable to Agent Tesla, Remcos, XWorm, Best Private Logger
- **DeFi Oracle/Price Feed Infrastructure**: Off-chain price feed servers, oracle networks, and validator infrastructure for decentralized trading protocols

## Attack Vectors and Techniques

- **Vulnerability Chaining (WP2Shell)**: Combining CVE-2026-60137 (authentication bypass) with CVE-2026-63030 (RCE primitive) to achieve unauthenticated remote code execution on WordPress sites
- **Ransomware Initial Access via VPN Flaw**: Qilin gang exploiting PAN-OS GlobalProtect authentication bypass for network entry, followed by ransomware deployment
- **Zero-Day Appliance Exploitation**: SonicWall SMA1000 vulnerabilities exploited pre-disclosure for custom malware installation on perimeter VPN devices
- **Local Privilege Escalation via Registry Hive**: Windows LegacyHive flaw allowing standard users to escalate to SYSTEM via crafted registry hive files
- **AI Platform RCE for Targeted Ransomware**: JADEPUFFER exploiting Langflow RCE to deploy ENCFORGE ransomware encrypting AI model assets (datasets, vectors, checkpoints)
- **Unauthenticated AI Service Exploitation**: ServiceNow AI Platform flaw allowing code execution without credentials via AI inference endpoints
- **ERP Module Exploitation**: Oracle E-Business Suite HR module flaw leveraged for data breach at major enterprise
- **Invisible UI Injection for AI Agent Hijacking**: Malicious Android apps overlaying invisible text that AI agents read and execute, bypassing human oversight
- **AI Agent Sandbox Escape via Host Tool Trust**: Inducing AI coding assistants to write malicious files that trusted host tools (linters, formatters, build systems) execute
- **Physical Side-Channel via Legitimate Cloud API (Bit2Watt)**: Modulating GPU workloads to induce power grid instability—no exploit, purely legitimate API abuse
- **Living-off-the-Land C2 via Microsoft Graph/Calendar**: HollowGraph using compromised M365 calendars (events dated 2050) for command delivery and data exfiltration
- **Mass IoT Camera Compromise for Intelligence Collection**: Automated exploitation of exposed cameras for persistent visual surveillance of military targets
- **Autonomous AI Agent Intrusion**: AI agent conducting end-to-end breach of Hugging Face infrastructure (recon, exploit, access, exfiltration)
- **Supply Chain Poisoning via Typosquatting/Brandjacking (FakeGit)**: 7,600 malicious GitHub repos masquerading as AI skills/MCP servers to deliver SmartLoader
- **Fileless Multi-RAT Deployment (TFF Trap)**: BEC phishing delivering fileless loaders that deploy Agent Tesla, Remcos, XWorm, Best Private Logger in memory
- **Off-Chain Oracle Compromise for DeFi Theft**: Targeting price feed infrastructure rather than smart contracts to manipulate on-chain state and drain vaults

## Threat Actor Activities

- **Qilin Ransomware Gang**: Actively exploiting Palo Alto PAN-OS GlobalProtect authentication bypass for initial access in ransomware campaigns; confirmed by Arctic Wolf intelligence
- **JADEPUFFER (Autonomous AI Operator)**: Conducting repeated, persistent attacks on Langflow servers; deployed ENCFORGE ransomware targeting AI model files; linked to Hugging Face breach via autonomous AI agent; demonstrates agentic, goal-directed targeting of AI infrastructure
- **SonicWall Zero-Day Operators**: Unknown threat group(s) exploiting two SMA1000 vulnerabilities as zero-days for weeks; deployed custom malware on VPN appliances; sophisticated, patient operation
- **Russian Intelligence Service(s)**: Systematic hijacking of IP security cameras across NATO states and Ukraine for military logistics surveillance; strategic, state-sponsored collection campaign
- **FakeGit Campaign Operators**: Large-scale GitHub repository poisoning (7,600 repos) distributing SmartLoader malware; heavy focus on AI/ML developer targeting via fake MCP servers and skills
- **HollowGraph Operators**: Unknown espionage actor using Microsoft 365 calendar/Graph API for stealthy C2; sophisticated tradecraft with future-dated events for evasion
- **TFF Trap BEC Group**: Business email compromise actors using fileless loaders and multi-RAT payloads (Agent Tesla, Remcos, XWorm, Best Private Logger); financially motivated credential theft and fraud
- **Ostium Attackers**: Unknown actors compromising off-chain price feed infrastructure to steal $23.75M from DeFi protocol; demonstrates understanding of oracle-dependent DeFi architecture
- **Estée Lauder Breach Actors**: Unknown group exploiting Oracle E-Business Suite flaw for data theft; targeted HR/customer data at major multinational
- **Android AI Agent Researchers/PoC Authors**: Demonstrated invisible text injection attack chain; publication may accelerate weaponization by threat actors
- **AI Coding Tool Sandbox Escape Researchers**: Disclosed escapes across Cursor, Codex, Gemini CLI, Antigravity; coordinated disclosure with vendors; Google downgraded severity ratings
- **Bit2Watt Researchers**: Demonstrated cloud GPU power grid disruption technique; no malicious actor attribution; highlights new cyber-physical attack surface

## Source Attribution

- **Choose Wisely: AI-Generated Coding Risk Varies, A Lot**: Dark Reading - https://www.darkreading.com/application-security/choose-wisely-ai-generated-coding-risk-varies
- **Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs**: The Hacker News - https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html
- **N-day is Becoming N-Hour. Patching Faster Won't Save You.**: The Hacker News - https://thehackernews.com/2026/07/n-day-is-becoming-n-hour-patching.html
- **New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit**: The Hacker News - https://thehackernews.com/2026/07/new-bit2watt-attack-could-let-cloud.html
- **US seizes over 1,000 websites in FIFA World Cup piracy crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-seizes-over-1-000-fifa-world-cup-illegal-streaming-domains/
- **Critical Palo Alto VPN bug now exploited by Qilin ransomware gang**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/critical-globalprotect-vpn-bug-now-exploited-in-ransomware-attacks/
- **Microsoft shares manual fix for WSUS sync delays and timeouts**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-manual-fix-for-wsus-sync-delays-and-timeouts/
- **WordPress wp2shell Exploitation Grows as Public Exploit Fuels Mass Scanning**: The Hacker News - https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
- **Windows LegacyHive zero-day flaw gets free, unofficial patches**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/windows-legacyhive-zero-day-flaw-gets-free-unofficial-patches/
- **New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack**: The Hacker News - https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html
- **Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution**: The Hacker News - https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
- **Estée Lauder discloses data breach via Oracle E-Business flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/est-e-lauder-discloses-data-breach-via-oracle-e-business-flaw/
- **SonicWall SMA1000 flaws exploited as zero-days to push custom malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sonicwall-sma1000-flaws-exploited-as-zero-days-to-push-custom-malware/
- **Hackers steal $23.7 million in crypto from Ostium in off-chain attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-steal-237-million-in-crypto-from-ostium-in-off-chain-attack/
- **'WP2Shell' Opens Millions of WordPress Sites to Remote Takeover**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/wp2shell-millions-wordpress-sites-remote-takeover
- **Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/
- **JadePuffer agentic attacks now target AI model data with ransomware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-attacks-now-target-ai-model-data-with-ransomware/
- **Remediating Vulnerabilities With LLMs: Inside Ivanti's Automation Push**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/remediating-vulnerabilities-llms-ivanti-automation
- **25 Years After Code Red: What the Worm Era Can Teach Us About AI Security**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/25-years-after-code-red-what-the-worm-era-can-teach-us-about-ai-security-2
- **CISOs Feel the Heat Over AI Risk**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cisos-feel-heat-ai-risk
- **Attackers Combo Up Evasion Tactics for BEC Phishing**: Dark Reading - https://www.darkreading.com/endpoint-security/attackers-combo-evasion-tactics-bec-phishing
- **FakeGit Campaign Uses 7,600 GitHub Repositories to Spread SmartLoader Malware**: The Hacker News - https://thehackernews.com/2026/07/fakegit-campaign-uses-7600-github.html
- **New HollowGraph malware uses Microsoft Graph for stealthy C2 comms**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-hollowgraph-malware-uses-microsoft-graph-for-stealthy-c2-comms/
- **Exposed Server Reveals AI-Assisted Phishing Toolkit Behind WebDAV Malware Campaign**: The Hacker News - https://thehackernews.com/2026/07/exposed-server-reveals-ai-assisted.html
- **HollowGraph Malware Hides C2 and Stolen Files in Microsoft 365 Events Dated 2050**: The Hacker News - https://thehackernews.com/2026/07/hollowgraph-malware-hides-c2-and-stolen.html
- **An AI SOC Evaluation Guide for Security Leaders**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/an-ai-soc-evaluation-guide-for-security-leaders/
- **Cybersecurity Keeps Events 'Uneventful'**: Dark Reading - https://www.darkreading.com/cyber-risk/cybersecurity-keeps-events-uneventful
- **⚡ Weekly Recap: WordPress RCE, SonicWall 0-Days, AI Service Attacks, SharePoint 0-Day and More**: The Hacker News - https://thehackernews.com/2026/07/weekly-recap-wordpress-rce-sonicwall-0.html
- **Russian Intelligence Hacks IP Cameras to Spy on Military Logistics Across NATO States and Ukraine**: The Hacker News - https://thehackernews.com/2026/07/russian-intelligence-hacks-ip-cameras.html
- **Hugging Face warns an autonomous AI agent hacked its network**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hugging-face-breach-autonomous-ai-agent-system-internal-datasets-credentials/
