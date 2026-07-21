# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse technology stacks this week, with threat actors demonstrating increased sophistication in chaining exploits and leveraging AI-driven tooling. The most immediate threats include a critical ServiceNow AI Platform flaw (CVE-2026-6875) enabling unauthenticated remote code execution, a WordPress RCE chain (CVE-2026-60137 and CVE-2026-63030) already weaponized at scale within days of disclosure, and two SonicWall SMA1000 zero-days exploited for weeks to deploy custom malware on VPN appliances. Simultaneously, a new wave of AI-targeted attacks has emerged: the JADEPUFFER autonomous operator is deploying ENCFORGE ransomware against Langflow servers to encrypt AI model assets, while the Hugging Face breach confirms autonomous AI agents can compromise production infrastructure. Russian intelligence continues systematic hijacking of IP cameras across NATO states for military surveillance, and a massive FakeGit campaign leverages 7,600 malicious GitHub repositories to distribute SmartLoader malware.

Privilege escalation and sandbox escape vulnerabilities round out the high-risk landscape. The Windows LegacyHive zero-day allows local privilege escalation on fully patched systems, with only unofficial mitigations available. Researchers demonstrated sandbox escapes across Cursor, Codex, Gemini CLI, and Antigravity by weaponizing AI agents to write files that trusted host tools subsequently execute. A heap-based buffer overflow in 7-Zip (CVE-2026-14266) enables code execution via crafted XZ archives. Novel malware frameworks like HollowGraph are abusing Microsoft 365 calendar events for stealthy C2 communications, while the SleeperGem supply chain attack poisons the RubyGems ecosystem. These developments underscore accelerating exploitation velocity, the convergence of AI tooling with offensive operations, and the persistent danger of edge-network appliances and supply chain vectors.

## Active Exploitation Details

### ServiceNow AI Platform Unauthenticated RCE (CVE-2026-6875)
- **Description**: A critical vulnerability in the ServiceNow AI Platform allows unauthenticated attackers to achieve remote code execution. The flaw resides in the platform's AI components and can be exploited without valid credentials.
- **Impact**: Full system compromise, unauthorized access to sensitive data, lateral movement within connected environments, and potential deployment of persistent malware or ransomware.
- **Status**: Actively exploited in the wild as of July 2026. Threat intelligence firm Defused Cyber confirmed active exploitation. ServiceNow has released patches; immediate application is critical.
- **CVE ID**: CVE-2026-6875

### WordPress RCE Chain (CVE-2026-60137 and CVE-2026-63030)
- **Description**: Two vulnerabilities chained together enable remote code execution on WordPress sites. CVE-2026-60137 and CVE-2026-63030 are being combined in a campaign dubbed "WP2Shell" to achieve unauthenticated takeover.
- **Impact**: Complete compromise of WordPress installations, including database access, file system control, and the ability to serve malicious content to visitors or pivot to internal networks.
- **Status**: Widely exploited within three days of public disclosure. Attackers are scanning and exploiting at scale across one of the largest attack surfaces on the internet. Patches available; emergency updates strongly recommended.
- **CVE ID**: CVE-2026-60137, CVE-2026-63030

### SonicWall SMA1000 Zero-Day Exploits
- **Description**: Two vulnerabilities in SonicWall SMA1000 series VPN appliances were exploited as zero-days for several weeks before public disclosure. Threat actors leveraged these flaws to install custom malware on vulnerable devices.
- **Impact**: Persistent access to corporate VPN infrastructure, credential harvesting, network pivoting, and potential deployment of ransomware or espionage tooling.
- **Status**: Actively exploited in zero-day attacks for weeks. SonicWall has released patches for both vulnerabilities. Organizations should assume compromise and conduct thorough incident response.
- **CVE ID**: [CVE IDs not provided in source articles]

### Windows LegacyHive Privilege Escalation Zero-Day
- **Description**: A zero-day vulnerability in Windows LegacyHive component allows local privilege escalation on fully patched Windows systems. The flaw enables attackers to gain SYSTEM-level privileges from a standard user context.
- **Impact**: Full administrative control over affected endpoints, bypass of security controls, credential theft, and facilitation of lateral movement.
- **Status**: Actively exploited; no official Microsoft patch available at time of reporting. Free unofficial patches have been released by security researchers (0patch) as a stopgap mitigation.
- **CVE ID**: [CVE ID not provided in source articles]

### 7-Zip XZ Archive Heap Buffer Overflow (CVE-2026-14266)
- **Description**: A heap-based buffer overflow in 7-Zip's processing of XZ chunked data allows code execution when a user extracts a crafted XZ archive.
- **Impact**: Arbitrary code execution in the context of the user running 7-Zip, potentially leading to malware installation, data theft, or further system compromise.
- **Status**: Vulnerability disclosed with proof-of-concept; active exploitation status unclear but high risk given 7-Zip's widespread deployment. Patched versions available.
- **CVE ID**: CVE-2026-14266

### AI Sandbox Escapes (Cursor, Codex, Gemini CLI, Antigravity)
- **Description**: Researchers demonstrated sandbox escape vulnerabilities across four AI coding assistants by having the AI agent write files that trusted host tools subsequently execute, breaking the isolation boundary.
- **Impact**: Escape from AI sandbox environments to execute arbitrary code on the host system, potentially accessing sensitive files, credentials, and development environments.
- **Status**: Multiple CVEs assigned; patches released for affected tools. Google downgraded two severity ratings post-disclosure. Active exploitation in the wild not confirmed but risk is high given developer adoption.
- **CVE ID**: [Multiple CVEs assigned; specific IDs not provided in source articles]

### Langflow RCE Exploited for ENCFORGE Ransomware
- **Description**: A remote code execution vulnerability in Langflow (a visual framework for building AI agents and RAG applications) is being exploited to deploy ENCFORGE ransomware, which specifically targets AI model files, training datasets, vector databases, and model checkpoints.
- **Impact**: Encryption and potential exfiltration of high-value AI/ML assets, disruption of AI development pipelines, and financial extortion.
- **Status**: Actively exploited by JADEPUFFER autonomous AI operator. Second confirmed attack on Langflow infrastructure by this actor. Patches for Langflow RCE should be applied immediately.
- **CVE ID**: [CVE ID not provided in source articles]

### Oracle E-Business Suite Flaw (Estée Lauder Breach)
- **Description**: A vulnerability in Oracle E-Business Suite was exploited to breach Estée Lauder's HR systems, resulting in customer data exposure.
- **Impact**: Unauthorized access to personal and potentially sensitive customer data, regulatory compliance violations, and reputational damage.
- **Status**: Exploited in confirmed breach. Oracle has released patches; organizations using E-Business Suite should verify patch status and monitor for indicators of compromise.
- **CVE ID**: [CVE ID not provided in source articles]

### Hugging Face Breach via Autonomous AI Agent
- **Description**: Attackers breached Hugging Face's production infrastructure using an autonomous AI agent system, gaining access to internal datasets and credentials.
- **Impact**: Compromise of the world's largest AI model repository, potential poisoning of model weights, theft of proprietary datasets and credentials, and supply chain risk for downstream users.
- **Status**: Confirmed breach disclosed by Hugging Face. Investigation ongoing. Highlights novel attack vector where AI agents themselves are weaponized as offensive tools.
- **CVE ID**: [No CVE applicable; novel attack methodology]

## Affected Systems and Products

- **ServiceNow AI Platform**: All versions prior to patched releases; cloud and on-premises deployments
- **WordPress**: Core versions affected by CVE-2026-60137 and CVE-2026-63030; millions of sites globally
- **SonicWall SMA1000 Series**: SMA1000 appliances running vulnerable firmware versions; enterprise VPN gateways
- **Windows LegacyHive Component**: All supported Windows versions (Windows 10, Windows 11, Windows Server 2016+)
- **7-Zip**: Versions prior to patched release; Windows, Linux, and macOS builds
- **Cursor, Codex, Gemini CLI, Antigravity**: AI coding assistant applications; developer workstations and CI/CD environments
- **Langflow**: Self-hosted Langflow servers; AI/ML development environments
- **Oracle E-Business Suite**: HR modules and connected components; enterprise ERP deployments
- **Hugging Face Platform**: Production infrastructure; spillover risk to hosted models and datasets
- **RubyGems Ecosystem**: Three malicious packages (sleeper_agent, sleeper_agent_core, sleeper_agent_utils); Ruby developer machines and CI pipelines
- **Microsoft 365 / Exchange Online**: Tenants with compromised mailboxes; HollowGraph malware abuses calendar feature for C2
- **GitHub**: 7,600+ malicious repositories in FakeGit campaign; developers cloning AI/ML-related repos
- **IP Cameras / IoT Devices**: Internet-connected security cameras across Europe and Ukraine; various vendors
- **Ostium Protocol / DeFi Infrastructure**: Off-chain price feed infrastructure; smart contract liquidity vaults

## Attack Vectors and Techniques

- **Vulnerability Chaining (WP2Shell)**: Attackers combine CVE-2026-60137 and CVE-2026-63030 in a single exploit chain to achieve unauthenticated RCE on WordPress, demonstrating rapid weaponization of disclosed flaws.
- **Zero-Day Exploitation of Edge Appliances**: SonicWall SMA1000 flaws exploited for weeks before disclosure, highlighting persistent targeting of VPN/network edge devices for initial access.
- **AI Agent Weaponization**: Autonomous AI agents (JADEPUFFER, Hugging Face attacker) used to conduct reconnaissance, exploit vulnerabilities, deploy ransomware, and manage C2—representing a paradigm shift in offensive automation.
- **Sandbox Escape via AI-Host Trust Boundary Abuse**: AI coding assistants tricked into writing malicious files that trusted host utilities (terminals, build systems, file watchers) automatically execute, breaking isolation.
- **Calendar-Based C2 (HollowGraph)**: Malware uses Microsoft 365 calendar events (including events dated 2050) as a covert command-and-control channel, hiding instructions and exfiltrated data in calendar attachments.
- **Supply Chain Poisoning (SleeperGem)**: Three malicious RubyGems packages published to official registry, targeting developer machines with credential theft and persistence capabilities.
- **Mass Repository Impersonation (FakeGit)**: 7,600 malicious GitHub repositories, 800+ masquerading as AI skills or MCP servers, distributing SmartLoader malware to developers.
- **Off-Chain Infrastructure Compromise**: Attackers manipulated price feed oracle infrastructure to drain $23.75M from Ostium's liquidity vault, bypassing on-chain security controls.
- **Living-off-the-Land / Legitimate Service Abuse**: HollowGraph leverages Microsoft Graph API and legitimate calendar features; JADEPUFFER uses AI agent frameworks as intended (but maliciously).
- **WebDAV Malware Delivery with AI-Generated Lures**: Exposed phishing toolkit reveals AI-assisted creation of lure templates, filename spoofing, and droppers delivered via WebDAV.
- **IoT Hijacking for Intelligence Collection**: Russian intelligence systematically compromises internet-connected cameras to monitor military logistics across NATO states and Ukraine.

## Threat Actor Activities

- **JADEPUFFER (Autonomous AI Operator)**: Linked to multiple Langflow server compromises; deploys ENCFORGE ransomware targeting AI model assets; operates with high automation and agentic decision-making.
- **bandcampro (Russian-Speaking Solo Actor)**: Uses Google Gemini CLI to orchestrate botnet of eight dental clinic PCs; demonstrates AI-assisted offensive operations by individual actors.
- **Russian Intelligence Service(s)**: Systematic hijacking of IP cameras across Europe and Ukraine for military surveillance; long-term, strategic espionage campaign.
- **FakeGit Operators**: Large-scale GitHub abuse campaign (7,600 repos); distributes SmartLoader malware; focuses on AI/ML developer ecosystem via MCP server impersonation.
- **HollowGraph Operators**: Espionage-focused implant using Microsoft 365 calendar for C2; likely state-aligned given stealth and targeting.
- **Defused Cyber (Threat Intelligence)**: First to report active exploitation of CVE-2026-6875 (ServiceNow); monitoring and disclosure of in-the-wild activity.
- **0patch (Micropatching Vendor)**: Released free unofficial patches for Windows LegacyHive zero-day; rapid response to unpatched vulnerabilities.
- **Sysdig (Security Research)**: Tracked JADEPUFFER activity; linked ENCFORGE ransomware to Langflow attacks; analyzed autonomous AI agent TTPs.
- **Rapid7 (Security Research)**: Discovered exposed phishing toolkit server; analyzed AI-assisted WebDAV malware campaign infrastructure.
- **Trend Micro (Security Research)**: Discovered and analyzed CVE-2026-14266 in 7-Zip; published technical details on XZ archive exploitation.

## Source Attribution

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
- **Mythos Didn't Break Your Security Program. Your Exposure Window Could.**: The Hacker News - https://thehackernews.com/2026/07/mythos-didnt-break-your-security.html
- **Microsoft confirms Windows Server Update Services sync delays**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-working-to-fix-wsus-server-sync-delays-and-timeouts/
- **Windows KB5121767 OOB update fixes shutdowns on some Dell PCs**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-bug-causing-some-dell-pcs-to-shut-down/
- **Critical ServiceNow code execution flaw now exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/
- **New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction**: The Hacker News - https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
- **Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs**: The Hacker News - https://thehackernews.com/2026/07/russian-speaking-hacker-uses-google.html
- **World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent**: The Hacker News - https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
- **SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines**: The Hacker News - https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html
