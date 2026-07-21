# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple high-value attack surfaces, with threat actors rapidly weaponizing newly disclosed vulnerabilities in widely deployed platforms. The WordPress ecosystem faces immediate risk as attackers chain CVE-2026-60137 and CVE-2026-63030—collectively dubbed "wp2shell"—to achieve remote code execution across millions of sites, with public exploits now circulating barely days after disclosure. Simultaneously, a critical ServiceNow AI Platform flaw (CVE-2026-6875) is under active exploitation, while SonicWall SMA 1000 series VPN appliances were compromised as zero-days prior to public disclosure, granting attackers root access to network edge devices.

AI-driven attack vectors are emerging as a dominant theme. Autonomous AI agents have successfully breached Hugging Face's production infrastructure to access internal datasets and credentials, while the JadePuffer agent now deploys custom ransomware (EncForge) targeting AI model assets including training datasets and vector databases. Supply chain attacks continue to scale: the FakeGit campaign leverages 7,600 malicious GitHub repositories—over 800 masquerading as AI skills or MCP servers—to distribute SmartLoader malware, and the SleeperGem operation planted three malicious packages on RubyGems targeting developers. Russian state-sponsored actors (UAC-0145) are employing ClickFix social engineering against Ukrainian targets, while a separate Russian intelligence service systematically hijacks IP cameras across NATO states and Ukraine for military logistics surveillance.

## Active Exploitation Details

### WordPress Core "wp2shell" RCE Vulnerabilities
- **Description**: Two critical vulnerabilities in WordPress Core (CVE-2026-60137 and CVE-2026-63030) that can be chained together to achieve unauthenticated remote code execution. The flaw allows attackers to execute arbitrary code through a single request.
- **Impact**: Full remote takeover of WordPress sites, affecting millions of installations across the internet. Attackers can achieve complete control over the underlying server.
- **Status**: Actively exploited in the wild. Public exploits have been released. Patches are available but adoption remains critical. Attacks began "barely three days after disclosure."
- **CVE ID**: CVE-2026-60137, CVE-2026-63030

### ServiceNow AI Platform Code Execution Flaw
- **Description**: A critical vulnerability in the ServiceNow AI Platform that allows remote code execution.
- **Impact**: Attackers can execute arbitrary code on ServiceNow instances, potentially compromising enterprise IT service management platforms and accessing sensitive organizational data.
- **Status**: Actively exploited in attacks according to threat intelligence company Defused. Patches should be applied immediately.
- **CVE ID**: CVE-2026-6875

### SonicWall SMA 1000 Series Zero-Day Exploitation
- **Description**: Previously undocumented vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances that were exploited as zero-days before public disclosure.
- **Impact**: Attackers gained root access to VPN appliances, providing persistent network edge access and potential lateral movement into internal networks.
- **Status**: Exploited in the wild prior to disclosure. A previously undocumented threat actor has been attributed to this activity. Patches have since been released.
- **CVE ID**: Not explicitly provided in source articles

### 7-Zip XZ Archive Heap Buffer Overflow
- **Description**: A heap-based buffer overflow in how 7-Zip processes XZ chunked data. Opening a crafted XZ archive triggers the vulnerability.
- **Impact**: Remote code execution on the victim's machine when they extract a malicious archive. Affects users who handle untrusted compressed files.
- **Status**: Proof-of-concept/exploit potential demonstrated. Fixed in 7-Zip version 26.02 released June 25, 2026.
- **CVE ID**: CVE-2026-14266

### NGINX Heap Buffer Overflow
- **Description**: A critical flaw in nginx that allows a remote, unauthenticated attacker to trigger a heap buffer overflow in the worker process through crafted HTTP requests.
- **Impact**: Worker process crashes (denial of service) and potential remote code execution on affected web servers.
- **Status**: F5 has shipped fixes. Active exploitation status not explicitly confirmed but rated critical.
- **CVE ID**: CVE-2026-42533

### AI Coding Assistant Sandbox Escapes
- **Description**: Researchers demonstrated sandbox escapes in Cursor, Codex, Gemini CLI, and Antigravity by having the AI agent write files that trusted host tools later execute.
- **Impact**: Escape from the AI assistant's sandbox environment to execute arbitrary code on the host system, potentially compromising developer machines and build environments.
- **Status**: Multiple CVEs assigned. Patches released. Google downgraded severity ratings for two of the vulnerabilities.
- **CVE ID**: Multiple CVEs assigned (specific IDs not provided in source)

### Hugging Face Autonomous AI Agent Breach
- **Description**: An autonomous AI agent system breached Hugging Face's production infrastructure, gaining access to internal datasets and credentials.
- **Impact**: Compromise of the world's largest AI model repository, exposing proprietary datasets, model weights, and authentication credentials.
- **Status**: Breach detected and disclosed by Hugging Face. Investigation ongoing.
- **CVE ID**: Not explicitly provided in source articles

### JadePuffer Agentic Ransomware Attacks
- **Description**: The JadePuffer autonomous AI agent has been upgraded with custom malware called EncForge that specifically targets AI assets for encryption.
- **Impact**: Encryption and ransomware targeting training datasets, vector databases, and model checkpoints—core intellectual property for AI-driven organizations.
- **Status**: Active campaign observed. Represents evolution of AI agents into offensive autonomous weapons.
- **CVE ID**: Not applicable (malware campaign)

## Affected Systems and Products

- **WordPress Core**: All versions prior to patched releases; millions of sites globally affected; CVE-2026-60137 and CVE-2026-63030
- **ServiceNow AI Platform**: Enterprise IT service management instances; CVE-2026-6875
- **SonicWall SMA 1000 Series**: Secure Mobile Access VPN appliances (1000 series); zero-day exploitation pre-disclosure
- **7-Zip**: Versions prior to 26.02; Windows/Linux/macOS; CVE-2026-14266
- **NGINX / F5 NGINX Plus**: Worker processes handling HTTP requests; versions prior to patched releases; CVE-2026-42533
- **Cursor, Codex, Gemini CLI, Antigravity**: AI coding assistants with sandbox environments; developer workstations and CI/CD pipelines
- **Hugging Face Platform**: Production infrastructure hosting AI models and datasets; internal credential stores
- **GitHub Repositories**: 7,600 malicious repositories in FakeGit campaign; 800+ posing as AI skills/MCP servers
- **RubyGems**: Three malicious packages in SleeperGem campaign; Ruby developer ecosystems
- **Microsoft 365 / Exchange Online**: Calendar functionality abused for C2 by HollowGraph malware; enterprise tenants
- **IP Cameras / IoT Devices**: Internet-connected security cameras across Europe and Ukraine; various vendors
- **ViPNet Software**: Private networking product suite; Russian government agencies targeted via update mechanism
- **Windows / Enterprise Endpoints**: ACR Stealer targeting browser credentials, auth tokens, documents; Microsoft enterprise customers

## Attack Vectors and Techniques

- **Vulnerability Chaining**: Attackers combine CVE-2026-60137 and CVE-2026-63030 in WordPress for reliable RCE; single request achieves full compromise
- **Zero-Day Exploitation**: SonicWall SMA vulnerabilities exploited before public disclosure; root access achieved on network edge devices
- **AI Agent Weaponization**: Autonomous AI agents used to breach production infrastructure (Hugging Face) and execute ransomware campaigns (JadePuffer/EncForge)
- **Sandbox Escape via Tool Trust**: AI coding assistants tricked into writing files that trusted host tools execute; escapes isolation boundaries in Cursor, Codex, Gemini CLI, Antigravity
- **Software Supply Chain - Typosquatting/Impersonation**: FakeGit campaign uses 7,600 GitHub repos, 800+ masquerading as legitimate AI skills/MCP servers to deliver SmartLoader
- **Software Supply Chain - Package Poisoning**: SleeperGem publishes three malicious RubyGems packages targeting developer machines
- **Living-off-the-Land / Trusted Service Abuse**: HollowGraph malware uses Microsoft Graph API and compromised M365 calendar events (dated 2050) for stealthy C2 and data exfiltration
- **AI-Assisted Phishing Toolkit**: WebDAV-based malware delivery with 1,048-component toolkit including lure templates, filename spoofing, droppers, and builders
- **ClickFix Social Engineering**: UAC-0145 uses fake CAPTCHA verification to trick Ukrainian targets into self-infecting via PowerShell commands
- **Update Mechanism Compromise**: Advanced threat actor abuses ViPNet software update mechanism to target Russian government agencies
- **Infrastructure Hijacking for Surveillance**: Russian intelligence service systematically compromises IP cameras across NATO/Ukraine to monitor military logistics routes
- **Credential Theft via Infostealer**: ACR Stealer surge targeting browser-stored passwords, authentication tokens, and sensitive documents on enterprise endpoints
- **Fileless Loader Techniques**: "The TFF Trap" BEC campaign uses fileless loaders with low detection rates to deploy Agent Tesla, Remcos, XWorm, Best Private Logger
- **Archive-Based Code Execution**: Crafted XZ archives exploit 7-Zip heap overflow during extraction (CVE-2026-14266)
- **HTTP Request Smuggling/Overflow**: Crafted HTTP requests trigger nginx heap buffer overflow in worker process (CVE-2026-42533)
- **AI CLI as C2 Framework**: Russian-speaking actor "bandcampro" uses Google Gemini CLI to control botnet of dental clinic PCs

## Threat Actor Activities

- **UAC-0145 (Russian State-Sponsored)**: Leveraging ClickFix CAPTCHA social engineering to infect Ukrainian targets with data-stealing malware; ongoing campaign
- **Russian Intelligence Service (Unnamed)**: Systematic hijacking of internet-connected security cameras across Europe and Ukraine for military logistics surveillance; strategic espionage operation
- **"bandcampro" (Russian-Speaking Solo Actor)**: Uses Google Gemini CLI to command and control a botnet of eight compromised dental clinic PCs; novel AI-assisted C2
- **JadePuffer Operators**: Deploying autonomous AI agent with EncForge ransomware targeting AI model assets (datasets, vector DBs, checkpoints); evolving agentic threat
- **FakeGit Campaign Operators**: Managing 7,600 malicious GitHub repositories distributing SmartLoader malware; 800+ repos impersonating AI skills/MCP servers; large-scale supply chain operation
- **SleeperGem Operators**: Published three malicious RubyGems packages targeting Ruby developers; software supply chain attack on package registry
- **HollowGraph Operators**: Espionage implant using compromised M365 calendars for C2 and data exfiltration; calendar events dated 2050 for stealth; advanced persistent threat
- **ViPNet Update Abuse Actor**: Advanced threat actor compromising ViPNet update mechanism to target Russian government agencies; supply chain / trusted channel abuse
- **ACR Stealer Operators**: Surge in campaigns against Microsoft enterprise customers stealing browser credentials, tokens, documents; financially motivated
- **TFF Trap / BEC Actors**: Fileless loader campaigns deploying Agent Tesla, Remcos, XWorm, Best Private Logger; business email compromise focus
- **SonicWall Zero-Day Actor**: Previously undocumented threat actor exploiting SMA 1000 series as zero-days for root access; sophisticated capability
- **Hugging Face Breach Actor**: Autonomous AI agent system that compromised production infrastructure; novel agentic intrusion method

## Source Attribution

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
- **Update now: 7-Zip fixes RCE flaw exploitable with malicious archives**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/update-now-7-zip-fixes-rce-flaw-exploitable-with-malicious-archives/
- **WordPress Core "wp2shell" RCE flaws get public exploits, patch now**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/
- **Microsoft warns of surge in ACR Stealer attacks on customers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-acr-stealer-attacks-on-customers/
