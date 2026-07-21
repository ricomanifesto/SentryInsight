# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse attack surfaces, ranging from enterprise VPN appliances and collaboration platforms to AI development tools and supply chain repositories. SonicWall SMA 1000 series VPN appliances were targeted as zero-days for weeks before disclosure, enabling root-level compromise and custom malware deployment. Simultaneously, a critical ServiceNow AI Platform flaw (CVE-2026-6875) is being actively exploited in the wild, while WordPress sites face mass exploitation through a chained RCE involving CVE-2026-60137 and CVE-2026-63030. These campaigns demonstrate rapid weaponization of disclosed vulnerabilities and persistent zero-day operations by both documented and previously unknown threat actors.

Supply chain and AI-focused attacks have surged, with the FakeGit campaign leveraging 7,600 malicious GitHub repositories—over 800 masquerading as AI skills or MCP servers—to distribute SmartLoader malware. Autonomous AI agents have emerged as both attack vectors and threat actors, evidenced by the Hugging Face breach via an autonomous AI system and the JadePuffer agent deploying EncForge ransomware specifically targeting AI model assets. Russian intelligence services continue systematic compromise of IP cameras across NATO states and Ukraine for military logistics surveillance, while the UAC-0145 group employs ClickFix social engineering against Ukrainian targets.

Novel post-exploitation techniques are proliferating, including HollowGraph malware's innovative use of Microsoft 365 calendar events as a covert C2 channel, and an exposed AI-assisted phishing toolkit revealing 1,048 files for WebDAV-based malware delivery. Critical flaws in widely deployed infrastructure—including nginx (CVE-2026-42533), 7-Zip (CVE-2026-14266), and the ViPNet update mechanism—expand the exploitation landscape. Sandbox escapes across Cursor, Codex, Gemini CLI, and Antigravity demonstrate a new class of AI toolchain vulnerabilities, while the SleeperGem supply chain attack poisons the RubyGems ecosystem with three malicious packages targeting developers.

## Active Exploitation Details

### SonicWall SMA 1000 Series Zero-Day Exploitation
- **Description**: Two vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances were exploited as zero-days for weeks prior to public disclosure. Attackers leveraged these flaws to gain root access on vulnerable appliances and install custom malware.
- **Impact**: Full administrative control over VPN appliances, enabling network persistence, traffic interception, lateral movement, and deployment of custom malware payloads. Compromised appliances provide a foothold into internal corporate networks.
- **Status**: Actively exploited in the wild before disclosure; patches now available from SonicWall. A previously undocumented threat actor has been attributed to this campaign.
- **CVE ID**: Not explicitly provided in source articles

### ServiceNow AI Platform Code Execution (CVE-2026-6875)
- **Description**: A critical vulnerability in the ServiceNow AI Platform allows remote code execution. Threat intelligence company Defused has confirmed active exploitation in the wild.
- **Impact**: Unauthenticated remote code execution on ServiceNow instances, potentially leading to full platform compromise, data theft, and lateral movement within enterprise environments using ServiceNow for IT service management and workflow automation.
- **Status**: Actively exploited; patches available from ServiceNow. Defused has observed exploitation activity.
- **CVE ID**: CVE-2026-6875

### WordPress WP2Shell Chained RCE (CVE-2026-60137 and CVE-2026-63030)
- **Description**: Attackers are widely chaining CVE-2026-60137 and CVE-2026-63030 to achieve remote code execution on WordPress sites. Exploitation began barely three days after disclosure, targeting one of the largest attack surfaces on the internet.
- **Impact**: Remote code execution on vulnerable WordPress installations, enabling complete site takeover, malware injection, data exfiltration, and use of compromised sites for further attacks (watering hole, SEO spam, redirect chains).
- **Status**: Actively exploited in mass campaigns; patches available for both vulnerabilities. Rapid weaponization indicates high attacker interest.
- **CVE ID**: CVE-2026-60137, CVE-2026-63030

### Oracle E-Business Suite Flaw (Estée Lauder Breach)
- **Description**: Hackers exploited a flaw in Oracle E-Business Suite used by Estée Lauder for human resources operations, leading to a data breach affecting customer information.
- **Impact**: Unauthorized access to HR systems and customer data. The breach triggered customer notification requirements.
- **Status**: Exploited in a confirmed breach; Estée Lauder has disclosed the incident. Oracle patch status not specified in source.
- **CVE ID**: Not explicitly provided in source articles

### 7-Zip XZ Archive Heap Buffer Overflow (CVE-2026-14266)
- **Description**: A heap-based buffer overflow in 7-Zip's processing of XZ chunked data allows code execution when a user opens a crafted XZ archive. Discovered by Trend Micro.
- **Impact**: Arbitrary code execution in the context of the user opening the archive. High impact due to 7-Zip's widespread deployment as a default archive utility.
- **Status**: Vulnerability disclosed; patch availability from 7-Zip. Exploitation requires user interaction (opening malicious archive).
- **CVE ID**: CVE-2026-14266

### NGINX Heap Buffer Overflow (CVE-2026-42533)
- **Description**: A critical flaw in nginx allows a remote, unauthenticated attacker to trigger a heap buffer overflow in the worker process via crafted HTTP requests. Patched by F5.
- **Impact**: Worker process crash (DoS) and potential remote code execution. Affects all nginx deployments handling untrusted HTTP traffic.
- **Status**: Patches shipped by F5. Exploitation status in the wild not confirmed in source articles but rated critical.
- **CVE ID**: CVE-2026-42533

### AI Tool Sandbox Escapes (Cursor, Codex, Gemini CLI, Antigravity)
- **Description**: Researchers demonstrated sandbox escapes in Cursor, Codex, Gemini CLI, and Antigravity by having AI agents write files that trusted host tools later execute. Multiple CVEs assigned; patches released; Google downgraded two severity ratings.
- **Impact**: Escape from AI agent sandboxes to execute arbitrary code on the host system, compromising developer machines and potentially CI/CD pipelines.
- **Status**: Vulnerabilities disclosed and patched across affected tools. Active exploitation in the wild not confirmed but proof-of-concepts exist.
- **CVE ID**: Multiple CVEs assigned (specific IDs not provided in source excerpts)

### ViPNet Software Update Mechanism Abuse
- **Description**: An advanced threat actor is abusing the update mechanism for the ViPNet private networking product suite to target Russian organizations, including government agencies.
- **Impact**: Supply chain compromise via trusted update channel, enabling malware deployment with high privileges on sensitive government networks.
- **Status**: Active campaign observed; mitigation requires ViPNet vendor response and network monitoring.
- **CVE ID**: Not explicitly provided in source articles

### SleeperGem RubyGems Supply Chain Attack
- **Description**: Three malicious gems published to RubyGems under the SleeperGem campaign target developer machines with the end goal of stealing credentials and sensitive data.
- **Impact**: Compromise of developer environments, potential theft of source code, credentials, SSH keys, and access to production systems via developer access.
- **Status**: Malicious packages identified and flagged; RubyGems removal in progress. Active targeting of Ruby ecosystem developers.
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **SonicWall SMA 1000 Series VPN Appliances**: All firmware versions prior to patched releases; enterprise remote access VPN deployments
- **ServiceNow AI Platform**: Instances running vulnerable versions; enterprise IT service management and workflow automation platforms
- **WordPress Core**: Versions affected by CVE-2026-60137 and CVE-2026-63030; millions of sites globally including self-hosted and managed installations
- **Oracle E-Business Suite**: HR module deployments; specific version details not disclosed in Estée Lauder breach notification
- **7-Zip**: Versions vulnerable to CVE-2026-14266 when processing crafted XZ archives; widely deployed on Windows, Linux, and macOS
- **NGINX / F5 NGINX Plus**: All versions prior to patched releases; web servers, reverse proxies, load balancers, and API gateways
- **Cursor, Codex, Gemini CLI, Antigravity**: AI-assisted development tools with sandbox environments; developer workstations and CI/CD systems
- **ViPNet Private Networking Suite**: Russian government and enterprise deployments using the vendor update mechanism
- **RubyGems / Ruby Ecosystem**: Developer machines installing gems from the public RubyGems registry; three specific malicious packages identified
- **Microsoft 365 / Exchange Online**: Tenants compromised for HollowGraph C2 calendar abuse; requires initial access to mailbox
- **GitHub / Developer Workstations**: Users cloning from 7,600 malicious FakeGit repositories; 800+ repos impersonating AI skills/MCP servers
- **IP Cameras / IoT Devices**: Internet-connected security cameras across Europe and Ukraine; various vendors with default/weak credentials
- **Hugging Face Platform**: AI model repository infrastructure; internal datasets and credentials accessed via autonomous AI agent breach
- **Ostium Trading Platform**: Off-chain price feed infrastructure; liquidity provider vault smart contracts
- **WebDAV Servers / Phishing Infrastructure**: Servers hosting AI-assisted phishing toolkit with 1,048 component files

## Attack Vectors and Techniques

- **Zero-Day VPN Appliance Exploitation**: Pre-disclosure exploitation of SonicWall SMA 1000 flaws for root access and custom malware installation; attributed to previously undocumented threat actor
- **Chained WordPress RCE**: Combining CVE-2026-60137 and CVE-2026-63030 for unauthenticated remote code execution; mass scanning and exploitation within days of disclosure
- **AI Agent Sandbox Escape**: Manipulating AI coding agents to write malicious files that are subsequently executed by trusted host tools (build systems, terminals, interpreters); affects Cursor, Codex, Gemini CLI, Antigravity
- **Autonomous AI Agent Intrusion**: Self-directed AI systems breaching production infrastructure (Hugging Face) to access internal datasets and credentials
- **AI-Targeted Ransomware (EncForge)**: JadePuffer agent deploys custom ransomware specifically encrypting AI assets—training datasets, vector databases, model checkpoints
- **Microsoft 365 Calendar C2 (HollowGraph)**: Using compromised mailbox calendar events (dated 2050) as covert command-and-control channel; instructions and exfiltrated data stored as event attachments
- **AI-Assisted Phishing Toolkit (WebDAV)**: 1,048-file toolkit including lure templates, filename-spoofing tests, execution experiments, droppers, and builders delivered via WebDAV
- **GitHub Repository Impersonation (FakeGit)**: 7,600 malicious repositories, 800+ masquerading as AI skills/MCP servers, distributing SmartLoader malware to developers
- **Supply Chain Update Hijacking (ViPNet)**: Compromising vendor update mechanism to push malware to high-value government targets
- **ClickFix Social Engineering (UAC-0145)**: Tricking Ukrainian targets into executing malicious commands via fake CAPTCHA/verification prompts
- **IP Camera Hijacking**: Systematic compromise of internet-connected cameras for persistent surveillance of military logistics routes across NATO states and Ukraine
- **Off-Chain Infrastructure Compromise**: Targeting price feed oracles and off-chain components of DeFi protocols (Ostium) to manipulate liquidity vaults
- **Malicious Archive Code Execution (7-Zip)**: Crafted XZ archives triggering heap buffer overflow during extraction; requires user interaction
- **HTTP Request Smuggling/Overflow (NGINX)**: Crafted HTTP requests triggering heap buffer overflow in worker process; unauthenticated, remote
- **RubyGems Typosquatting/Malicious Publishing (SleeperGem)**: Three malicious packages published to official registry targeting developer credential theft
- **ServiceNow AI Platform RCE**: Exploitation of CVE-2026-6875 for unauthenticated code execution on enterprise workflow platforms

## Threat Actor Activities

- **Previously Undocumented Threat Actor (SonicWall Campaign)**: Attributed to zero-day exploitation of SonicWall SMA 1000 appliances prior to disclosure; deployed custom malware; maintained access for weeks; high sophistication level suggesting state-sponsored or advanced persistent threat
- **JadePuffer / EncForge Operators**: Autonomous AI agent upgraded with custom EncForge ransomware; specifically targets AI model assets (datasets, vector DBs, checkpoints); represents evolution of AI-driven offensive operations
- **UAC-0145 (Russian State-Sponsored)**: Leverages ClickFix social engineering technique to infect Ukrainian targets with data-stealing malware; ongoing campaign aligned with Russian strategic interests
- **Russian Intelligence Service (IP Camera Campaign)**: At least one Russian intelligence service systematically hijacking IP cameras across Europe and Ukraine for military logistics intelligence collection; persistent, large-scale operation
- **FakeGit / SmartLoader Operators**: Maintains 7,600 malicious GitHub repositories with 800+ impersonating AI skills/MCP servers; distributes SmartLoader malware; sophisticated supply chain deception campaign
- **HollowGraph Operators**: Espionage-focused implant using Microsoft 365 calendar as C2 channel; plants operator instructions and exfiltrates data via calendar event attachments; targets compromised enterprise tenants
- **bandcampro (Russian-Speaking Solo Actor)**: Uses Google Gemini CLI to control botnet of eight dental clinic PCs; demonstrates AI-assisted botnet management by individual threat actor
- **ViPNet Supply Chain Actor**: Advanced threat actor compromising ViPNet update mechanism to target Russian government agencies; high-value targeting suggests state-sponsored or highly resourced group
- **SleeperGem Operators**: Published three malicious RubyGems packages targeting developer machines for credential theft; active supply chain poisoning of Ruby ecosystem
- **Ostium Attacker**: Compromised off-chain price feed infrastructure to drain $23.75M from liquidity provider vault; sophisticated DeFi-focused financial crime
- **AI-Assisted Phishing Toolkit Operator**: Built 1,048-file toolkit with AI-generated lure templates, filename spoofing, and WebDAV delivery; server exposure revealed full operational infrastructure
- **ServiceNow Exploitation Actors**: Active exploitation of CVE-2026-6875 observed by Defused threat intelligence; specific attribution not disclosed
- **Autonomous AI Agent (Hugging Face Breach)**: Self-directed AI system breached Hugging Face production infrastructure to access internal datasets and credentials; novel threat actor category

## Source Attribution

- **Estée Lauder discloses data breach via Oracle E-Business flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/est-e-lauder-discloses-data-breach-via-oracle-e-business-flaw/
- **SonicWall SMA1000 flaws exploited as zero-days to push custom malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sonicwall-sma1000-flaws-exploited-as-zero-days-to-push-custom-malware/
- **Hackers steal $23.7 million in crypto from Ostium in off-chain attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-steal-237-million-in-crypto-from-ostium-in-off-chain-attack/
- **'WP2Shell' Opens Millions of WordPress Sites to Remote Takeover**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/wp2shell-millions-wordpress-sites-remote-takeover
- **Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/
- **JadePuffer agentic attacks now target AI model data with ransomware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-attacks-now-target-ai-model-data-with-ransomware/
- **Remediating Vulnerabilities With LLMs: Inside Ivanti's Automation Push**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/remediating-vulnerabilities-llms-ivanti-automation
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
- **Critical NGINX Vulnerability Can Crash Workers and May Allow Remote Code Execution**: The Hacker News - https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html
- **Hackers abuse ViPNet software to target Russian govt agencies**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-abuse-vipnet-software-to-target-russian-govt-agencies/
- **UAC-0145 Uses ClickFix CAPTCHAs to Infect Ukrainian Devices wih Malware**: The Hacker News - https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html
- **SonicWall SMA Zero-Days Exploited Before Disclosure to Gain Root Access**: The Hacker News - https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html
