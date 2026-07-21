# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks this week, with ransomware groups and advanced threat actors rapidly weaponizing recently disclosed flaws. The Qilin ransomware gang has begun leveraging a critical PAN-OS GlobalProtect authentication bypass to breach corporate networks, while attackers are chaining two WordPress vulnerabilities (CVE-2026-60137 and CVE-2026-63030) for unauthenticated remote code execution across millions of sites just days after public disclosure. Simultaneously, a critical ServiceNow AI Platform flaw (CVE-2026-6875) is being exploited for unauthenticated code execution, and two SonicWall SMA1000 zero-day vulnerabilities were exploited for weeks before disclosure to deploy custom malware on VPN appliances.

AI-focused attacks are escalating rapidly, with the JADEPUFFER autonomous AI agent—now equipped with custom ENCFORGE ransomware—targeting AI model files, training datasets, and vector databases in Langflow RCE attacks. Hugging Face disclosed a breach of internal datasets and credentials via an autonomous AI agent, while researchers demonstrated sandbox escapes across Cursor, Codex, Gemini CLI, and Antigravity. Russian intelligence services are systematically hijacking internet-connected IP cameras across NATO states and Ukraine for military logistics surveillance, and a new espionage implant dubbed HollowGraph uses compromised Microsoft 365 calendars as a covert command-and-control channel.

## Active Exploitation Details

### PAN-OS GlobalProtect Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in Palo Alto Networks PAN-OS GlobalProtect VPN portal that allows unauthenticated attackers to access protected resources
- **Impact**: Full network breach capability, enabling ransomware deployment and lateral movement within victim environments
- **Status**: Actively exploited by Qilin ransomware gang; Arctic Wolf observed exploitation in the wild
- **CVE ID**: Not explicitly provided in source articles

### WordPress WP2Shell Chained RCE (CVE-2026-60137 and CVE-2026-63030)
- **Description**: Two critical WordPress vulnerabilities that when chained together enable unauthenticated remote code execution and complete compromise of vulnerable websites
- **Impact**: Unauthenticated remote code execution leading to full website takeover, malware injection, and potential server compromise
- **Status**: Mass scanning and exploitation underway within three days of public disclosure; public exploit code fueling widespread attacks
- **CVE ID**: CVE-2026-60137 and CVE-2026-63030

### ServiceNow AI Platform Unauthenticated Code Execution
- **Description**: Critical security flaw in ServiceNow AI Platform allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication, enabling data theft, persistence, and lateral movement
- **Status**: Actively exploited in attacks; Defused Cyber observed exploitation and reported via threat intelligence
- **CVE ID**: CVE-2026-6875

### SonicWall SMA1000 Zero-Day Vulnerabilities
- **Description**: Two vulnerabilities in SonicWall SMA1000 series VPN appliances exploited as zero-days for several weeks prior to disclosure
- **Impact**: Installation of custom malware on VPN appliances, persistent access to corporate networks, traffic interception
- **Status**: Were exploited as zero-days for weeks; patches now available but exploitation occurred pre-disclosure
- **CVE ID**: Not explicitly provided in source articles

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: Zero-day flaw in Windows LegacyHive component allowing local privilege escalation on fully patched Windows systems
- **Impact**: SYSTEM-level privilege escalation from standard user context, enabling full host compromise
- **Status**: Publicly disclosed with exploitation details; unofficial micropatches available from 0patch; official Microsoft patch pending
- **CVE ID**: Not explicitly provided in source articles

### Langflow RCE Exploited by JADEPUFFER/ENCFORGE
- **Description**: Remote code execution vulnerability in Langflow (AI application framework) exploited by autonomous AI agent JADEPUFFER
- **Impact**: Deployment of ENCFORGE ransomware targeting AI assets including training datasets, vector databases, and model checkpoints
- **Status**: Active exploitation campaign; same operator linked to multiple Langflow server compromises
- **CVE ID**: Not explicitly provided in source articles

### 7-Zip XZ Archive Heap Buffer Overflow
- **Description**: Heap-based buffer overflow in 7-Zip's processing of XZ chunked data that triggers during archive extraction
- **Impact**: Arbitrary code execution when user opens crafted XZ archive
- **Status**: Vulnerability disclosed (CVE-2026-14266); exploitation potential high but active exploitation not confirmed in articles
- **CVE ID**: CVE-2026-14266

### AI Coding Tool Sandbox Escapes
- **Description**: Sandbox escape vulnerabilities in Cursor, Codex, Gemini CLI, and Antigravity AI coding assistants allowing AI agents to write files that trusted host tools later execute
- **Impact**: Escape from AI sandbox to host system, enabling arbitrary code execution on developer machines
- **Status**: Multiple CVEs assigned; patches released; Google downgraded two severity ratings post-analysis
- **CVE ID**: Multiple CVEs assigned (specific IDs not provided in source articles)

### Hugging Face Autonomous AI Agent Breach
- **Description**: Attackers used an autonomous AI agent to breach Hugging Face production infrastructure
- **Impact**: Access to internal datasets and credentials; potential supply chain impact for AI/ML community
- **Status**: Breach disclosed by Hugging Face; investigation ongoing
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **Palo Alto Networks PAN-OS GlobalProtect**: VPN portal appliances; specific versions not detailed in source articles
- **WordPress**: Core WordPress installations; millions of sites potentially affected by chained CVE-2026-60137 and CVE-2026-63030
- **ServiceNow AI Platform**: ServiceNow instances with AI Platform module enabled; cloud and on-premises deployments
- **SonicWall SMA1000 Series**: SMA1000 VPN appliances; firmware versions prior to patched releases
- **Microsoft Windows**: All supported Windows versions with LegacyHive component (registry hive handling); up-to-date systems affected
- **Langflow**: AI application framework servers exposed to internet; versions with RCE vulnerability
- **7-Zip**: Versions processing XZ archives; vulnerable to CVE-2026-14266 heap buffer overflow
- **Cursor, Codex, Gemini CLI, Antigravity**: AI coding assistant applications; sandbox escape vulnerabilities patched in recent updates
- **Hugging Face Platform**: Production infrastructure hosting AI models, datasets, and Spaces
- **Oracle E-Business Suite**: HR modules used by Estée Lauder; specific flaw not detailed in source articles
- **Microsoft 365 / Exchange Online**: Calendar functionality abused by HollowGraph malware for C2 communications
- **IP Cameras / IoT Devices**: Internet-connected security cameras across Europe and Ukraine; various vendors/models

## Attack Vectors and Techniques

- **Authentication Bypass**: Qilin ransomware gang exploiting PAN-OS GlobalProtect flaw to bypass VPN authentication and gain initial network access
- **Vulnerability Chaining**: Attackers combining CVE-2026-60137 and CVE-2026-63030 for unauthenticated RCE in WordPress—first vulnerability enables the second
- **Zero-Day Exploitation**: SonicWall SMA1000 flaws exploited for weeks before public disclosure; custom malware deployed during zero-day window
- **AI-Agent-Driven Attacks**: JADEPUFFER autonomous AI agent conducting reconnaissance, exploitation, and ransomware deployment without human operators
- **Ransomware Targeting AI Assets**: ENCFORGE specifically encrypts training datasets, vector databases, model checkpoints—high-value AI intellectual property
- **Sandbox Escape via Host Tool Trust**: AI agents write malicious files that trusted host utilities (git, npm, build tools) later execute, breaking isolation
- **Calendar-Based C2**: HollowGraph malware uses Microsoft 365 calendar events (dated 2050) as covert command channel and data exfiltration path
- **Supply Chain / Repository Poisoning**: FakeGit campaign uses 7,600 malicious GitHub repositories (800+ masquerading as AI skills/MCP servers) to deliver SmartLoader
- **Fileless BEC Phishing**: "TFF Trap" technique uses fileless loaders with low detection rates to deploy Agent Tesla, Remcos, XWorm, Best Private Logger
- **Off-Chain Infrastructure Compromise**: Attackers compromised price feed infrastructure for Ostium trading protocol, manipulating oracle data to drain $23.75M
- **IoT Device Hijacking**: Russian intelligence systematically compromising internet-connected IP cameras for persistent surveillance of military logistics
- **Autonomous AI Agent Intrusion**: Attackers deployed autonomous AI agent to breach Hugging Face infrastructure and access internal datasets/credentials

## Threat Actor Activities

- **Qilin Ransomware Gang**: Actively exploiting PAN-OS GlobalProtect authentication bypass for initial access in ransomware campaigns; observed by Arctic Wolf
- **JADEPUFFER (AI-Agent-Driven Operator)**: Autonomous AI agent conducting Langflow RCE attacks; upgraded with ENCFORGE ransomware targeting AI model assets; linked to multiple server compromises per Sysdig
- **Russian Intelligence Service(s)**: Systematic hijacking of IP cameras across NATO states and Ukraine for military logistics intelligence collection; persistent surveillance campaign
- **FakeGit Campaign Operators**: Managing 7,600 malicious GitHub repositories; 800+ pose as AI skills/MCP servers; distributing SmartLoader malware to developers
- **HollowGraph Operators**: Espionage actors using compromised Microsoft 365 mailboxes for C2; planting commands and exfiltrating data via calendar events dated 2050
- **BEC Phishing Actors**: Using "TFF Trap" fileless technique combo to deploy Agent Tesla, Remcos, XWorm, Best Private Logger; evasion-focused loader chain
- **Ostium Attacker**: Compromised off-chain price feed infrastructure to manipulate oracle data and drain $23.75M from liquidity provider vault
- **Estée Lauder Breach Actors**: Exploited Oracle E-Business Suite flaw to access HR data; customer notification underway

## Source Attribution

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
- **Mythos Didn't Break Your Security Program. Your Exposure Window Could.**: The Hacker News - https://thehackernews.com/2026/07/mythos-didnt-break-your-security.html
- **Microsoft confirms Windows Server Update Services sync delays**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-working-to-fix-wsus-server-sync-delays-and-timeouts/
- **Windows KB5121767 OOB update fixes shutdowns on some Dell PCs**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-bug-causing-some-dell-pcs-to-shut-down/
- **Critical ServiceNow code execution flaw now exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/
- **New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction**: The Hacker News - https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
