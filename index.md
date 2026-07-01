# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple vectors this period, with actively exploited vulnerabilities in enterprise infrastructure, large-scale credential attacks against cloud identities, and emerging AI-driven attack techniques. The Progress Kemp LoadMaster pre-authentication RCE flaw is under active exploitation attempts per eSentire's Threat Response Unit, while over 900 Oracle E-Business Suite instances remain exposed to ongoing attacks leveraging a critical security flaw. Simultaneously, a massive Azure CLI password spray campaign has compromised at least 78 Microsoft accounts across more than 81 million attempts, demonstrating the continued effectiveness of credential-based attacks against cloud infrastructure.

Threat actors are rapidly adopting AI-enabled techniques across the kill chain. The Ousaban banking trojan campaigns target Spanish and Portuguese financial institutions using sophisticated PDF lures, while a China-linked group has compromised at least ten Southeast Asian organizations—including two state-owned entities—deploying a novel backdoor. Supply chain attacks persist through malicious PyPI packages trojanizing Pyrogram forks to steal arbitrary files from Telegram bot developers, a campaign active since November 2025. The ClickFix social engineering framework has evolved an API-driven backend managing over 3,000 live payloads, and "Phantom Squatting" leverages LLM-hallucinated domains for near-undetectable phishing infrastructure.

New AI-specific attack surfaces are being weaponized at speed. Critical flaws in the Cursor AI code editor allow prompt injection to escape sandboxes and execute arbitrary commands. The "BioShocking" prompt injection technique manipulates AI browsers into treating dangerous actions as fictional scenarios, bypassing safety controls. "Agentjacking" via fake bug reports hijacks AI coding agents at scale, while poisoned MCP tool descriptions silently exfiltrate data from AI agents. Attackers are also seizing exposed, unauthenticated AI endpoints to power offensive operations, and DeepSeek-generated browser ransomware abuses Chromium APIs across Windows and Android.

## Active Exploitation Details

### Progress Kemp LoadMaster Pre-Auth RCE
- **Description**: A critical pre-authentication remote code execution vulnerability affecting Progress Kemp LoadMaster load balancing appliances. The flaw allows unauthenticated attackers to execute arbitrary code on affected devices.
- **Impact**: Full compromise of load balancer appliances, potential lateral movement into internal networks, traffic interception, and persistence in critical network infrastructure.
- **Status**: Actively exploited in the wild. eSentire's Threat Response Unit has observed active exploitation attempts. Progress has released security advisories and patches.

### Oracle E-Business Suite Critical Flaw Exploitation
- **Description**: A critical security flaw in Oracle E-Business Suite (EBS) being actively exploited against internet-exposed instances.
- **Impact**: Over 900 EBS instances found exposed online with ongoing attacks. Successful exploitation could lead to unauthorized access to enterprise ERP data, financial systems, and sensitive business operations.
- **Status**: Ongoing attacks against exposed instances. Organizations urged to apply patches and restrict network access immediately.

### Azure CLI Password Spray Campaign
- **Description**: Massive, ongoing automated password spray attack targeting Microsoft's Azure Command-Line Interface (CLI) authentication endpoints.
- **Impact**: At least 78 Microsoft accounts compromised across more than 81 million authentication attempts. Provides attackers initial access to Azure tenants and associated cloud resources.
- **Status**: Active, ongoing campaign. Microsoft and security researchers tracking the activity.

### Ousaban Banking Trojan Campaign
- **Description**: Brazilian-origin banking trojan targeting Windows users of financial institutions in Spain and Portugal. Delivered via phishing emails containing malicious PDF lures that execute the payload.
- **Impact**: Credential theft, session hijacking, financial fraud against Iberian banking customers. Persistent access to compromised systems for follow-on operations.
- **Status**: Active campaign identified by Fortinet FortiGuard Labs in May 2026. Ongoing targeting of Spanish and Portuguese banking sectors.

### China-Linked Southeast Asia Critical Infrastructure Campaign
- **Description**: China-nexus threat group conducting targeted intrusions against critical systems in Southeast Asia, compromising at least 10 regional organizations including two state-owned entities.
- **Impact**: Deployment of a previously undocumented backdoor providing persistent access to strategic organizations. Potential espionage, intellectual property theft, and pre-positioning for disruptive operations.
- **Status**: Active campaign reported by Dark Reading. Attribution to China-linked actors based on TTPs and infrastructure.

### Malicious PyPI Supply Chain Attack (Trojanized Pyrogram)
- **Description**: Campaign distributing trojanized forks of the Pyrogram Telegram bot library via PyPI. Active since November 2025, targeting Python developers building Telegram bots.
- **Impact**: Arbitrary file read on compromised developer servers and build systems. Potential supply chain contamination of downstream applications. Access to Telegram bot tokens and communications.
- **Status**: Active campaign ongoing since November 2025. Multiple malicious packages identified and reported.

### ClickFix API-Driven Malware Delivery
- **Description**: Evolution of the ClickFix social engineering technique (fake "prove you're human" pages) now backed by an API-driven command-and-control infrastructure managing payload delivery.
- **Impact**: Automated, scalable malware delivery to victims who manually execute commands. Researchers analyzed 3,000 live payloads revealing diverse malware families and dynamic payload selection.
- **Status**: Active infrastructure with 3,000+ live payloads analyzed. Ongoing campaigns targeting diverse sectors.

### Phantom Squatting (AI-Hallucinated Domain Attacks)
- **Description**: Attackers register domains hallucinated by LLMs when referencing legitimate brands. These domains receive traffic from users and AI systems that inadvertently reference the fabricated URLs.
- **Impact**: Difficult-to-detect phishing and malware distribution. Exploits trust in AI-generated content and brand recognition. Bypasses traditional typo-squatting detection.
- **Status**: Emerging active threat vector. Multiple security vendors reporting increasing registration and weaponization of hallucinated domains.

### AI-Generated Browser Ransomware (Chromium API Abuse)
- **Description**: Novel ransomware artifact generated using DeepSeek AI that abuses Chromium browser APIs on Windows and Android to encrypt files and extort victims.
- **Impact**: Cross-platform browser-based ransomware leveraging legitimate browser capabilities. Demonstrates AI-accelerated malware development with novel attack paths.
- **Status**: Proof-of-concept/early-stage artifact identified by researchers. Represents new class of AI-generated browser malware.

### Cursor AI Editor Sandbox Escape
- **Description**: Two vulnerabilities in the Cursor AI code editor allowing prompt injection to break out of the editor's safety sandbox and execute arbitrary commands on the developer's machine.
- **Impact**: Remote code execution on developer workstations via malicious prompts in code context. Supply chain risk through compromised development environments.
- **Status**: Vulnerabilities disclosed. No patch status confirmed in source articles.

### BioShocking Prompt Injection Attack
- **Description**: Novel prompt injection technique that manipulates AI-powered browsers into treating real-world risky actions as fictional scenarios, bypassing safety guardrails to enable data theft.
- **Impact**: Data exfiltration from AI browser sessions. Bypass of safety controls designed to prevent dangerous actions. Exploits the blurring of fiction/reality in LLM reasoning.
- **Status**: Newly disclosed attack technique. Active research into mitigations.

### Agentjacking (Fake Bug Report AI Agent Hijacking)
- **Description**: Attack technique exploiting AI coding agents' inability to distinguish between content and instructions. Malicious bug reports or issues contain injected prompts that hijack the agent's behavior.
- **Impact**: Large-scale hijacking of AI coding assistants. Potential code injection, data exfiltration, and supply chain compromise through automated development workflows.
- **Status**: Demonstrated at scale. Emerging threat to AI-assisted development pipelines.

### Poisoned MCP Tool Description Attacks
- **Description**: Attack vector where malicious tool descriptions in Model Context Protocol (MCP) configurations cause AI agents to silently exfiltrate data to attacker-controlled destinations.
- **Impact**: Covert data leakage from AI agents acting on user behalf. Exploits trust in tool definitions. No user interaction required beyond agent invocation.
- **Status**: Microsoft research disclosure. Active threat to MCP-enabled AI agent deployments.

### Exposed AI Endpoint Hijacking
- **Description**: Attackers locate and seize unauthenticated AI model endpoints exposed to the internet, using them to power offensive operations without authorization.
- **Impact**: Free compute for threat actors. Attribution obfuscation. Potential data poisoning of models. Unauthorized use of organizational AI infrastructure.
- **Status**: Active technique. Dark Reading reports threat actors actively scanning for and exploiting exposed endpoints.

### EU/Asia Hospitality Sector Phishing Campaigns
- **Description**: Separate but similar campaigns by Microsoft and Trend Micro tracking phishing targeting hospitality organizations in Europe and Asia using malicious zip files, social engineering, obfuscation, and blockchain abuse for persistence.
- **Impact**: Persistent access to hospitality networks. Credential theft, payment data exposure, potential lateral movement to corporate systems.
- **Status**: Active campaigns. Multiple threat actors or shared TTPs across campaigns.

### Adobe ColdFusion and Campaign Classic Maximum Severity Flaws
- **Description**: Adobe released patches for seven CVSS 10.0 (maximum severity) vulnerabilities across ColdFusion (web application platform) and Campaign Classic (marketing automation).
- **Impact**: Potential remote code execution, authentication bypass, and full system compromise of affected servers. Critical internet-facing infrastructure at risk.
- **Status**: Patches released. Exploitation status in wild not explicitly confirmed in source articles.

### Citrix NetScaler File Read and DoS Vulnerabilities
- **Description**: Six vulnerabilities in NetScaler ADC and NetScaler Gateway allowing unauthorized file read and denial-of-service conditions.
- **Impact**: Information disclosure of sensitive files on ADC appliances. Service disruption through DoS. Potential chaining with other vulnerabilities.
- **Status**: Patches released by Citrix. Exploitation status not explicitly confirmed in source articles.

## Affected Systems and Products

- **Progress Kemp LoadMaster**: Load balancing appliances; pre-auth RCE vulnerability; network infrastructure layer
- **Oracle E-Business Suite (EBS)**: ERP platform; 900+ internet-exposed instances under active attack; enterprise business applications
- **Microsoft Azure CLI**: Cloud management interface; password spray targeting authentication endpoints; Azure tenant identities
- **Windows (Spain/Portugal banking users)**: Ousaban banking trojan targeting via malicious PDF lures; financial sector endpoints
- **Southeast Asian Critical Infrastructure**: State-owned and critical private entities; novel backdoor deployment; strategic organizational networks
- **Python/PyPI Ecosystem**: Pyrogram Telegram library forks; developer build systems and servers; software supply chain
- **ClickFix Victims**: Users tricked by fake verification pages; diverse sectors; endpoint execution via social engineering
- **LLM-Hallucinated Domains**: Any brand referenced by LLMs; users and AI systems following fabricated links; web infrastructure
- **Chromium-Based Browsers (Windows/Android)**: AI-generated ransomware abusing browser APIs; cross-platform browser capabilities
- **Cursor AI Code Editor**: Developer workstations; sandbox escape via prompt injection; development environments
- **AI-Powered Browsers**: BioShocking prompt injection targets; data theft via safety bypass; AI browser sessions
- **AI Coding Agents (GitHub Copilot, etc.)**: Agentjacking via fake bug reports; automated development pipelines; source code repositories
- **MCP-Enabled AI Agents**: Agents using Model Context Protocol; enterprise AI assistants; data accessible to agents
- **Exposed AI Model Endpoints**: Unauthenticated inference APIs; organizational AI infrastructure; cloud and on-prem deployments
- **Hospitality Sector Systems (EU/Asia)**: Property management, booking, payment systems; persistent phishing access; service industry networks
- **Adobe ColdFusion**: Web application development platform; CVSS 10.0 flaws; internet-facing application servers
- **Adobe Campaign Classic**: Marketing automation platform; CVSS 10.0 flaws; customer engagement infrastructure
- **Citrix NetScaler ADC/Gateway**: Application delivery controllers and gateways; file read and DoS flaws; network edge infrastructure

## Attack Vectors and Techniques

- **Pre-Authentication RCE**: Unauthenticated remote code execution on network infrastructure (Kemp LoadMaster); network-level access without credentials
- **Credential Spraying at Scale**: Automated password spray against Azure CLI (81M+ attempts); cloud identity compromise; low-and-slow evasion
- **Phishing with Malicious Documents**: PDF lures delivering banking trojans (Ousaban); social engineering targeting financial sector; Windows malware execution
- **Novel Backdoor Deployment**: Custom malware for persistent access (China-linked group); strategic targeting; critical infrastructure focus
- **Supply Chain Compromise via Package Repositories**: Trojanized PyPI packages (Pyrogram forks); developer machine compromise; arbitrary file read
- **Social Engineering with Fake Verification**: ClickFix "prove you're human" pages; manual command execution by victims; API-driven payload delivery
- **AI-Hallucinated Domain Registration**: Phantom Squatting registering LLM-fabricated URLs; phishing/malware hosting; detection evasion via legitimacy appearance
- **AI-Generated Malware Development**: DeepSeek-created browser ransomware; Chromium API abuse; cross-platform (Windows/Android) capability
- **Prompt Injection Sandbox Escape**: Malicious prompts breaking AI editor isolation (Cursor); arbitrary command execution on developer machines
- **Fictional Scenario Manipulation**: BioShocking attack framing dangerous actions as fiction; AI browser safety bypass; data exfiltration
- **Content/Instruction Confusion in AI Agents**: Agentjacking via fake bug reports; hijacking automated coding assistants; scale exploitation
- **Poisoned Tool Definitions**: Malicious MCP tool descriptions causing data leakage; covert exfiltration via trusted agent workflows
- **Unauthenticated AI Endpoint Abuse**: Scanning for and seizing open AI inference APIs; free compute for offensive ops; attribution hiding
- **Multi-Stage Phishing with Persistence**: Malicious zip files, obfuscation, blockchain abuse (hospitality campaigns); long-term access maintenance
- **Maximum Severity Web App Exploitation**: CVSS 10.0 flaws in ColdFusion/Campaign Classic; potential RCE and auth bypass; internet-facing servers
- **File Read and DoS on Network Edge**: NetScaler ADC/Gateway vulnerabilities; information disclosure and service disruption; network perimeter

## Threat Actor Activities

- **Ousaban Operators (Brazilian Nexus)**: Banking trojan campaigns targeting Spanish and Portuguese financial institutions; active since at least May 2026; PDF-based delivery; financial fraud focus
- **China-Linked APT Group**: Southeast Asia critical infrastructure targeting; 10+ organizations compromised including 2 state-owned entities; novel backdoor deployment; espionage/pre-positioning objectives
- **PyPI Supply Chain Actors**: Active since November 2025; trojanized Pyrogram packages targeting Telegram bot developers; arbitrary file read on dev servers; Python ecosystem focus
- **ClickFix Infrastructure Operators**: API-driven malware delivery backend managing 3,000+ live payloads; automated payload selection; diverse malware distribution; social engineering at scale
- **Phantom Squatters**: Registering LLM-hallucinated brand domains; phishing and malware hosting; exploiting AI hallucination phenomenon; difficult attribution
- **Azure CLI Password Spray Actors**: Massive automated campaign (81M+ attempts, 78+ compromises); cloud identity targeting; likely credential reuse/credential stuffing operations
- **AI Malware Developers**: Using DeepSeek for browser ransomware generation; novel Chromium API abuse; cross-platform malware innovation
- **Hospitality Sector Phishing Groups**: Microsoft and Trend Micro tracking separate campaigns; EU and Asia targeting; malicious zip delivery; blockchain abuse for persistence; potential shared TTPs or actors
- **Exposed AI Endpoint Hijackers**: Opportunistic scanning for unauthenticated AI APIs; offensive compute theft; attribution obfuscation; infrastructure abuse

## Source Attribution

- **Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures**: The Hacker News - https://thehackernews.com/2026/07/ousaban-banking-trojan-targets-iberian.html
- **Adobe Patches 7 CVSS 10.0 Flaws in ColdFusion and Campaign Classic**: The Hacker News - https://thehackernews.com/2026/07/adobe-patches-7-cvss-100-flaws-in.html
- **'Phantom Squatting': An Emerging AI-Driven Supply Chain Threat**: Dark Reading - https://www.darkreading.com/endpoint-security/phantom-squatting-ai-driven-supply-chain-threat
- **Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands**: The Hacker News - https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
- **Turning Indicators into Intelligence in OpenCTI with Criminal IP**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/turning-indicators-into-intelligence-in-opencti-with-criminal-ip/
- **Progress Kemp LoadMaster Pre-Auth RCE Flaw Faces Active Exploitation Attempts**: The Hacker News - https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html
- **Safe Events Start With Threat Intel and Digital Security**: Dark Reading - https://www.darkreading.com/threat-intelligence/safe-events-threat-intel-digital-security
- **AI-Generated Browser Ransomware Abuses Chromium API on Windows and Android**: The Hacker News - https://thehackernews.com/2026/07/ai-generated-browser-ransomware-abuses.html
- **Over 900 Oracle E-Business instances exposed to ongoing attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/over-900-oracle-e-business-instances-exposed-to-ongoing-attacks/
- **2026 Cybersecurity Assessment: The Gap Between Awareness and Resilience**: The Hacker News - https://thehackernews.com/2026/07/2026-cybersecurity-assessment-gap.html
- **Microsoft fixes GIF functionality in the Windows Emoji Panel**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-gif-functionality-in-the-windows-emoji-panel/
- **Microsoft Accelerates Post-Quantum Cryptography Shift to 2029**: The Hacker News - https://thehackernews.com/2026/07/microsoft-accelerates-post-quantum.html
- **Amazon fined $2.25M for withholding evidence from fraud victims**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/amazon-fined-225m-for-withholding-evidence-from-fraud-victims/
- **Adobe patches seven max severity ColdFusion, Campaign flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/adobe-patches-seven-max-severity-coldfusion-campaign-flaws/
- **Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware**: The Hacker News - https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html
- **Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls**: The Hacker News - https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html
- **Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts**: The Hacker News - https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
- **Researcher Analyzes 3,000 Live ClickFix Payloads, Exposing API-Driven Malware Delivery**: The Hacker News - https://thehackernews.com/2026/07/researcher-analyzes-3000-live-clickfix.html
- **Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service**: The Hacker News - https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html
- **China-Linked Group Targets Southeast Asia Critical Systems**: Dark Reading - https://www.darkreading.com/threat-intelligence/china-linked-group-targets-southeast-asia-critical-systems
- **Anthropic to restore Claude Fable access on Wednesday**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-to-restore-claude-fable-access-on-wednesday/
- **Anthropic rolls out Sonnet 5 with near-Opus 4.8 performance at a lower price**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-rolls-out-sonnet-5-with-near-opus-48-performance-at-a-lower-price/
- **New BioShocking attack manipulates AI browser into data theft**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/
- **Fake Bug Report Hijacks AI Coding Agents at Scale**: Dark Reading - https://www.darkreading.com/cyber-risk/fake-bug-report-hijacks-ai-coding-agents
- **Microsoft accelerates quantum-safe roadmap as risks grow**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-accelerates-quantum-safe-roadmap-as-risks-grow/
- **Malicious PyPI packages give hackers control of Telegram bot servers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/malicious-pypi-packages-give-hackers-control-of-telegram-bot-servers/
- **Attackers Seize Exposed AI Endpoints to Power Offensive Ops**: Dark Reading - https://www.darkreading.com/cloud-security/attackers-hijack-exposed-ai-endpoints-power-offensive-ops
- **Why Identity Security Is Your Cyber Career Entry Point**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/identity-security-cyber-career-entry-point
- **Phishers Gain Persistence at EU, Asia Hospitality Orgs**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/phishers-persistence-eu-asia-hospitality-orgs
- **Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data**: The Hacker News - https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html
