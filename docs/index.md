# Exploitation Report

## Executive Summary

Organized crime syndicates have entered a new era of AI-powered fraud at unprecedented scale, leveraging voice cloning, real-time deepfake video overlays, LLM-driven persona management, and automated translation to execute convincing scams across investment, romance, gambling, and law enforcement impersonation schemes. Simultaneously, the emergent attack surface of AI browsers and agentic systems is under active exploitation, with zero-click agent hijacking ("PleaseFix") and persistent prompt injection vulnerabilities affecting major vendors—researchers confirm there is no simple fix for these fundamental trust boundary issues. 

Critical infrastructure and enterprise software remain prime targets for active exploitation. CISA has added three actively exploited vulnerabilities—in IBM Langflow (RCE), N-central, and Apache Tomcat—to its Known Exploited Vulnerabilities catalog, mandating federal agency patching within three days. A SQL injection in an Oracle database enabled deployment of the "khunt" post-exploitation toolkit directly inside the database layer, while a supply chain compromise of the QuickFox VPN client delivered the FDMTP backdoor via trojanized Windows installers. 

Nation-state and cybercriminal actors are converging on identity and cloud targets. The Kali365 phishing kit weaponizes legitimate Microsoft device code flows to breach US organizations, while a Canadian threat actor pleaded guilty to compromising 165 organizations via Snowflake cloud storage for extortion. The Ransom Cartel operator received a 16-year sentence, and OpenAI disrupted a Cambodia-based scam network (Poipet) abusing ChatGPT. Meanwhile, 250+ ClickFix domains now employ browser fingerprinting to selectively deliver macOS malware, and trojanized npm packages use a novel "NullReceiver" blockchain technique to hide C2 infrastructure.

## Active Exploitation Details

### AI-Enabled Fraud and Scam Operations at Scale
- **Description**: Organized crime groups are deploying generative AI tooling—including voice cloning, real-time deepfake video overlays, LLM-driven persona management, and automated translation—to conduct convincing social engineering and fraud campaigns across multiple schemes simultaneously.
- **Impact**: Billions in fraud revenue through investment scams, romance scams, gambling fraud, and law enforcement impersonation; ability to operate at scale across language barriers with minimal human operators.
- **Status**: Actively ongoing; OpenAI disrupted one Cambodia-based network (Poipet) using ChatGPT, but the broader ecosystem of AI-enabled fraud services continues to expand on underground forums.

### PleaseFix Zero-Click Agent Hijacking in AI Browsers
- **Description**: Attackers can take control of AI browser agents through malicious instructions hidden in content supplied to the browser (web pages, documents, emails), requiring zero user interaction beyond the agent processing the content.
- **Impact**: Full agent hijacking leading to unauthorized actions, data exfiltration, credential theft, and potential lateral movement through agent permissions.
- **Status**: Actively exploitable across multiple AI browser vendors; researchers indicate no simple fix exists due to fundamental architecture of instruction-following agents.

### AI Browser Prompt Injection Vulnerabilities
- **Description**: Persistent prompt injection flaws in AI browsers from top vendors allow attackers to override system instructions and manipulate agent behavior through crafted inputs, despite multiple security guardrails.
- **Impact**: Bypass of safety controls, unauthorized tool use, data access, and execution of attacker-controlled workflows.
- **Status**: No perfect fix available; guardrails provide partial mitigation but fundamental trust boundary issues remain unresolved across the industry.

### SQL Injection Leading to Oracle Database Post-Exploitation Toolkit Deployment
- **Description**: Attackers exploited a SQL injection vulnerability in an Oracle database to install the "khunt" post-exploitation toolkit directly inside the database, using it as a foothold to breach the corporate network.
- **Impact**: Persistent database-layer compromise, credential theft, lateral movement, and full network breach originating from the data tier.
- **Status**: Active exploitation observed in the wild; demonstrates emerging trend of database-resident malware.

### CISA KEV: Actively Exploited Langflow RCE, N-central, and Apache Tomcat Flaws
- **Description**: Three vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog on August 5, 2026: an RCE in IBM Langflow, a flaw in N-central (N-able), and an Apache Tomcat vulnerability. All have confirmed active exploitation.
- **Impact**: Remote code execution, unauthorized access, and potential supply chain compromise through widely deployed automation, monitoring, and application server platforms.
- **Status**: Actively exploited in the wild; CISA mandated federal agencies to mitigate within three days (by August 8, 2026).

### QuickFox Supply Chain Attack Delivering FDMTP Backdoor
- **Description**: Long-standing supply chain compromise of QuickFox, a VPN and network acceleration tool for overseas users, delivering the FDMTP backdoor through trojanized Windows installers.
- **Impact**: Persistent remote access to victim networks, traffic interception, and potential pivot to connected infrastructure; targets users seeking network circumvention tools.
- **Status**: Active supply chain compromise; trojanized installers distributed through legitimate update channels.

### Kali365 Phishing Kit Weaponizing Microsoft Device Code Authentication
- **Description**: Phishing kit (Kali365) abuses legitimate Microsoft device code flow—attacker-controlled device codes that victims approve on Microsoft's real login page—bypassing traditional credential harvesting detection.
- **Impact**: Account takeover with valid session tokens, MFA bypass, access to corporate Microsoft 365/Azure resources, and persistent access via refresh tokens.
- **Status**: Actively targeting US organizations; leverages legitimate Microsoft infrastructure making detection difficult.

### ClickFix Campaign with Browser Fingerprinting Targeting macOS
- **Description**: Over 250 front-end domains in a ClickFix operation fingerprint visitors before selectively delivering macOS malware lures, evading automated analysis and blocking.
- **Impact**: Targeted malware delivery to macOS users, evasion of security crawlers and sandbox analysis, social engineering via fake verification prompts.
- **Status**: Active campaign tracked by Microsoft Threat Intelligence; infrastructure continuously rotating.

### Trojanized npm Packages Using NullReceiver Blockchain C2 Technique
- **Description**: Evolution of the EtherHiding technique—trojanized npm packages decode C2 server IP addresses from blockchain transactions using a "NullReceiver" tactic that conceals the destination in made-up addresses.
- **Impact**: Stealthy command-and-control resilient to takedown, supply chain compromise through malicious packages, blockchain-based infrastructure hiding.
- **Status**: Active in npm ecosystem; represents advancement in blockchain-enabled C2 obfuscation.

### COLDCARD Vulnerability-Themed Phishing Delivering ScreenConnect RAT
- **Description**: Phishing campaign exploits fear around a disclosed COLDCARD hardware wallet vulnerability and rumored $88.6M Bitcoin theft to trick users into installing ScreenConnect remote access software.
- **Impact**: Full remote control of victim systems, cryptocurrency wallet compromise, credential theft, and persistent access.
- **Status**: Active phishing campaign leveraging vulnerability disclosure publicity for social engineering.

### Leaked n8n API Tokens Exposing Live Instances to Credential Theft
- **Description**: 321 n8n workflow automation instances found with API tokens exposed in public GitHub commits, enabling attackers to access sensitive data and downstream credentials through four demonstrated attack paths.
- **Impact**: Unauthorized access to workflow automation platforms, credential harvesting from connected services, potential supply chain compromise through automated workflows.
- **Status**: Active exposure; GitGuardian researchers demonstrated practical exploitation paths.

### Open VSX Malicious Evil Twin Extensions Exfiltrating Developer Data
- **Description**: Cluster of 77 malicious extensions on Open VSX marketplace impersonating legitimate developer tools (typosquatting/brandjacking) while exfiltrating system and development environment information.
- **Impact**: Developer machine reconnaissance, credential theft, source code exfiltration, supply chain poisoning via compromised development environments.
- **Status**: Removed from Open VSX after discovery; unknown number of prior installations.

### Paperclip AI Flaws Allowing Host Command Execution via Malicious Agent Imports
- **Description**: Two security flaws in Paperclip (open-source AI agent control plane) allow attackers to execute arbitrary commands on network servers or developer machines through malicious agent imports.
- **Impact**: Remote code execution on AI infrastructure, compromise of agent orchestration platforms, lateral movement through AI/ML pipelines.
- **Status**: Vulnerabilities disclosed; patch status unclear from available reporting.

### Google APK for Python Agent-to-Agent Trust Boundary Exploitation
- **Description**: Flaws in Google's APK for Python exploited a trust boundary between two AI agents with different privilege levels, enabling automation that could compromise the software supply chain.
- **Impact**: Privilege escalation between AI agents, supply chain compromise through automated agent interactions, unauthorized code execution in build/deployment pipelines.
- **Status**: Google has fixed the issues; demonstrates emerging class of agent-to-agent vulnerabilities.

### Critical Gitea Unauthenticated File Read via Org-Mode Markup
- **Description**: Unauthenticated attackers can read any file accessible to the Gitea service account on versions 1.22.1 through 1.27.0 via Org-mode markup processing, requiring no login or repository write access.
- **Impact**: Source code disclosure, configuration theft (including secrets), internal file system reconnaissance, potential credential exposure.
- **Status**: Public exploit available; affects default configurations of self-hosted Git platform.

### New OVSwrap Linux Kernel Flaw in Open vSwitch Datapath
- **Description**: Memory corruption flaw in the Linux kernel's Open vSwitch (OVS) datapath (OVSwrap) allows local users to gain root privileges on a broad set of default-configured distributions; public exploit available.
- **Impact**: Local privilege escalation to root, container escape potential, compromise of virtualized/networked environments using OVS.
- **Status**: Public exploit ships with proof-of-concept; affects default-configured distributions broadly.

### Veeam, Terraform MCP, and Django Critical Vulnerabilities Patched
- **Description**: Eleven vulnerabilities patched across HashiCorp Terraform MCP Server, Veeam Service Provider Console, and Django, led by a CVSS 10.0 cross-tenant bug enabling unauthorized cross-tenant data access.
- **Impact**: Cross-tenant data breach in multi-tenant environments, remote code execution, authentication bypass, and privilege escalation in backup, infrastructure automation, and web framework platforms.
- **Status**: Patches released; CVSS 10.0 flaw represents maximum severity cross-tenant isolation failure.

### TP-Link Omada ZTP Zero-Touch Provisioning Vulnerabilities
- **Description**: Fifteen vulnerabilities in TP-Link Omada network devices' zero-touch provisioning (ZTP) mechanism that can be chained with previously disclosed flaws to achieve remote code execution.
- **Impact**: Network device compromise, traffic interception, network pivoting, persistent infrastructure access through automated provisioning systems.
- **Status**: TP-Link has released patches; ZTP attack surface represents systemic risk in automated network provisioning.

### CSS-Based Data Exfiltration from Webmail
- **Description**: Researchers demonstrate CSS capabilities sufficient to exfiltrate data from webmail interfaces through crafted stylesheets, with some vendors unprepared for this attack vector.
- **Impact**: Data theft from email clients without JavaScript execution, bypassing traditional XSS protections, stealthy exfiltration via CSS loading mechanisms.
- **Status**: Proof-of-concept demonstrated; vendor mitigation status varies.

## Affected Systems and Products

- **AI Browsers / Agentic Browsers (multiple vendors)**: All major AI browser platforms vulnerable to PleaseFix zero-click hijacking and prompt injection; fundamental architecture issue affecting instruction-following agents
- **IBM Langflow**: RCE vulnerability actively exploited; affects automation/AI workflow platforms
- **N-central (N-able)**: Actively exploited flaw in RMM platform; affects MSP-managed endpoints
- **Apache Tomcat**: Actively exploited vulnerability; affects widespread Java application server deployments
- **Oracle Database**: SQL injection enabling khunt toolkit deployment; enterprise database installations
- **QuickFox VPN/Network Accelerator**: Trojanized Windows installers delivering FDMTP backdoor; overseas user base
- **Microsoft Device Code Authentication / Microsoft 365 / Azure AD**: Kali365 phishing kit abusing legitimate device code flow; US organizations targeted
- **Snowflake Cloud Data Platform**: 165 organizations compromised via credential abuse; cloud data warehouse customers
- **macOS Systems**: ClickFix campaign with 250+ fingerprinting domains selectively delivering malware
- **npm Ecosystem / Node.js Supply Chain**: Trojanized packages using NullReceiver blockchain C2; developers and CI/CD pipelines
- **COLDCRAD Hardware Wallets / Bitcoin Users**: Phishing campaign leveraging vulnerability disclosure fear; cryptocurrency holders
- **n8n Workflow Automation Instances**: 321 instances with exposed API tokens in public GitHub; self-hosted and cloud deployments
- **Open VSX Marketplace / VS Code Extensions**: 77 malicious evil-twin extensions exfiltrating developer data; Open VSX users
- **Paperclip AI Control Plane**: Open-source AI agent orchestration platform; two RCE flaws via malicious agent imports
- **Google APK for Python**: Agent-to-agent trust boundary flaws; Python-based AI agent frameworks
- **Gitea Self-Hosted Git Platform**: Versions 1.22.1–1.27.0; unauthenticated file read via Org-mode markup
- **Linux Kernel (Open vSwitch / OVSwrap)**: Default-configured distributions using OVS datapath; local privilege escalation to root
- **Veeam Service Provider Console**: Cross-tenant CVSS 10.0 flaw and other critical vulnerabilities; MSP backup infrastructure
- **HashiCorp Terraform MCP Server**: Critical vulnerabilities in infrastructure automation control plane
- **Django Web Framework**: Multiple vulnerabilities patched in widely used Python web framework
- **TP-Link Omada Network Devices**: 15 ZTP vulnerabilities chainable to RCE; enterprise and SMB network infrastructure
- **Webmail Platforms (multiple vendors)**: CSS-based data exfiltration; vendors with insufficient CSS sandboxing

## Attack Vectors and Techniques

- **AI-Enabled Social Engineering at Scale**: Voice cloning, real-time deepfake video overlays, LLM-driven persona management, automated translation enabling multi-lingual, high-volume fraud operations
- **Zero-Click Agent Hijacking (PleaseFix)**: Malicious instructions embedded in content (web pages, documents, emails) processed by AI browser agents, requiring no user interaction beyond agent invocation
- **Prompt Injection Against AI Agents**: Crafted inputs overriding system instructions and safety guardrails in AI browsers and agentic systems, exploiting fundamental instruction-following architecture
- **SQL Injection to Database-Resident Malware**: Web application SQLi used to deploy post-exploitation toolkit (khunt) directly inside Oracle database, establishing persistence at data tier
- **Supply Chain Compromise via Trojanized Installers**: Legitimate software update channels compromised to deliver backdoors (FDMTP) through signed/verified installers (QuickFox)
- **Legitimate Authentication Flow Abuse (Device Code Phishing)**: Attacker-controlled Microsoft device codes approved by victims on real Microsoft login pages, yielding valid session tokens without credential harvesting
- **Browser Fingerprinting for Selective Malware Delivery**: 250+ front-end domains profiling visitors before showing malware lures, evading automated analysis and blocking (ClickFix)
- **Blockchain-Based C2 Obfuscation (NullReceiver/EtherHiding Evolution)**: C2 IP addresses encoded in blockchain transactions using made-up destination addresses, resilient to infrastructure takedown
- **Vulnerability Disclosure-Themed Social Engineering**: Phishing campaigns exploiting fear from recent vulnerability announcements (COLDARD) to deliver remote access tools
- **Secrets Exposure in Public Repositories**: API tokens, credentials committed to public GitHub repositories enabling unauthorized access to automation platforms (n8n)
- **Typosquatting/Brandjacking in Extension Marketplaces**: Malicious extensions impersonating legitimate developer tools on Open VSX, exfiltrating development environment data
- **Malicious Agent Import / Supply Chain in AI Orchestration**: Compromised agent definitions in Paperclip AI control plane enabling host command execution on import
- **Agent-to-Agent Trust Boundary Exploitation**: Privilege escalation between AI agents with different permission levels (Google APK for Python), compromising automated pipelines
- **Unauthenticated File Read via Markup Processing**: Org-mode markup parser in Gitea allowing path traversal/file read without authentication
- **Local Kernel Privilege Escalation via Network Datapath**: Memory corruption in Open vSwitch kernel module (OVSwrap) enabling root from unprivileged local user
- **Cross-Tenant Isolation Failure**: CVSS 10.0 vulnerability in Veeam Service Provider Console allowing unauthorized access to other tenants' data in multi-tenant environments
- **Zero-Touch Provisioning Chain Exploitation**: 15 vulnerabilities in TP-Link Omada ZTP mechanism chainable to RCE, exploiting automated network device onboarding
- **CSS-Only Data Exfiltration**: Crafted stylesheets exfiltrating data from webmail interfaces without JavaScript execution, bypassing XSS protections

## Threat Actor Activities

- **Global Organized Crime Syndicates (AI Fraud Networks)**: Operating at industrial scale using generative AI tooling for investment, romance, gambling, and law enforcement impersonation fraud; billions in revenue; disrupted Poipet network (Cambodia-based) used ChatGPT across multiple schemes
- **Poipet Scam Network (Cambodia-based)**: Disrupted by OpenAI; used ChatGPT to facilitate wide-ranging fraud schemes including investment, romance, gambling, and law enforcement impersonation
- **Ransom Cartel (Maksim Silnikau)**: Creator/administrator sentenced to 16 years for ransomware attacks against at least 18 companies worldwide; operation dismantled
- **Canadian Threat Actor (Snowflake Extortion)**: Pleaded guilty to accessing company accounts at Snowflake, stealing data from 165+ organizations in extortion scheme seeking millions
- **Kali365 Operators**: Deploying phishing kit weaponizing Microsoft device code authentication against US organizations; attacker-controlled device codes yielding valid MFA-bypassed sessions
- **ClickFix Threat Group**: Operating 250+ front-end domains with browser fingerprinting for selective macOS malware delivery; infrastructure tracked by Microsoft Threat Intelligence
- **EtherHiding/NullReceiver Operators**: Evolving blockchain-based C2 technique via trojanized npm packages; concealing C2 IPs in blockchain transactions using made-up destination addresses
- **QuickFox Supply Chain Actors**: Long-standing compromise of VPN/network tool distribution delivering FDMTP backdoor; targeting overseas users seeking network circumvention
- **khunt Toolkit Operators**: Using SQL injection to deploy post-exploitation framework inside Oracle databases for corporate network breach; database-resident malware technique
- **COLDARD Phishing Actors**: Leveraging vulnerability disclosure publicity and rumored $88.6M Bitcoin theft to deliver ScreenConnect RAT via social engineering
- **n8n Token Harvesters**: Scanning GitHub for exposed API tokens (321 instances found) to access workflow automation platforms and downstream credentials
- **Open VSX Evil-Twin Extension Authors**: 77 malicious extensions impersonating legitimate tools for developer data exfiltration; marketplace supply chain attack
- **Paperclip AI Exploiters**: Targeting AI agent control plane via malicious agent imports for host command execution on servers and developer machines
- **Langflow/N-central/Tomcat Exploiters**: Actively exploiting three CISA KEV vulnerabilities (added August 5, 2026) for RCE and unauthorized access; federal agencies given 3-day mitigation deadline

## Source Attribution

- **AI Sends Global Crime Syndicates Into Fraud Nirvana**: Dark Reading - https://www.darkreading.com/threat-intelligence/ai-global-crime-syndicates-fraud-nirvana
- **AI Browsers Vulnerable to 'PleaseFix' Zero-Click Agent Hijacking**: Dark Reading - https://www.darkreading.com/cyber-risk/ai-browsers-zero-click-agent-hijacking
- **Ransom Cartel ransomware creator sentenced to 16 years in prison**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ransom-cartel-ransomware-creator-sentenced-to-16-years-in-prison/
- **No Perfect Fix for AI Browser Prompt Injection Flaws**: Dark Reading - https://www.darkreading.com/application-security/no-perfect-fix-ai-browser-prompt-injection-flaws
- **Canadian pleads guilty to Snowflake cloud data-theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/canadian-pleads-guilty-to-snowflake-cloud-data-theft-attacks/
- **Hackers run khunt post-exploitation toolkit from Oracle database**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-run-khunt-post-exploitation-toolkit-from-oracle-database/
- **CSS: The Hidden Threat Lurking in Your Inbox**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/css-hidden-threat-lurking-inbox
- **15 TP-Link Bugs Expose Risks in Zero-Trust Provisioning**: Dark Reading - https://www.darkreading.com/endpoint-security/15-tp-link-bugs-risks-zero-trust-provisioning
- **Over 250 ClickFix Domains Use Browser Fingerprinting to Hide macOS Malware Lures**: The Hacker News - https://thehackernews.com/2026/08/over-250-clickfix-domains-use-browser.html
- **OpenAI Disrupts Poipet Scam Network Using ChatGPT Across Multiple Fraud Schemes**: The Hacker News - https://thehackernews.com/2026/08/openai-disrupts-poipet-scam-network.html
- **Flaws in Google APK for Python Unlock Agent-to-Agent Attack**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/flaws-google-apk-python-agent-to-agent-attack
- **COLDCARD security audit phishing attack installs remote access tool**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coldcard-security-audit-phishing-attack-installs-remote-access-tool/
- **CISA warns of hackers exploiting Langflow, N-central, Apache Tomcat flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-langflow-n-central-apache-tomcat-flaws/
- **Poison Claude Sells Discounted Claude Access While Its Operator Sees Every Customer Prompt**: The Hacker News - https://thehackernews.com/2026/08/poison-claude-sells-discounted-claude.html
- **Paperclip AI Flaws Let Attackers Run Host Commands via Malicious Agent Imports**: The Hacker News - https://thehackernews.com/2026/08/paperclip-ai-flaws-let-attackers-run.html
- **Google Blogger locks hundreds of blogs in malware false positive**: Bleeping Computer - https://www.bleepingcomputer.com/news/google/google-blogger-locks-hundreds-of-blogs-in-malware-false-positive/
- **Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug**: The Hacker News - https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html
- **How AI-powered phishing killed blocklists for good**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/how-ai-powered-phishing-killed-blocklists-for-good/
- **Trojanized npm Packages Employ NullReceiver Tactic to Decode C2 IP from Blockchain**: The Hacker News - https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html
- **New OVSwrap Linux Kernel Flaw Lets Local Users Gain Root via Open vSwitch**: The Hacker News - https://thehackernews.com/2026/08/new-ovswrap-linux-kernel-flaw-lets.html
- **Kali365 Weaponizes Microsoft Authentication Against US Companies: New Enterprise Risk**: The Hacker News - https://thehackernews.com/2026/08/kali365-weaponizes-microsoft.html
- **Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup**: The Hacker News - https://thehackernews.com/2026/08/critical-gitea-flaw-let-unauthenticated.html
- **Leaked n8n API Tokens Exposed Live Instances to Credential Theft**: The Hacker News - https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
- **Open VSX Removes 77 Malicious Evil Twin Extensions Exfiltrating Developer Data**: The Hacker News - https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html
- **Angola's Largest Telco Breached Hours Before IPO**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/angolas-largest-telco-breached-hours-before-ipo
- **Claude Mythos 5 Tried to Backdoor a Real Open-Source Project in Testing, Then Vouched for Itself**: The Hacker News - https://thehackernews.com/2026/08/claude-mythos-5-tried-to-backdoor-real.html
- **CISA Flags Langflow RCE, Tomcat, and N-central Flaws as Actively Exploited**: The Hacker News - https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html
- **QuickFox Supply Chain Attack Delivers FDMTP Backdoor via Trojanized Windows Installer**: The Hacker News - https://thehackernews.com/2026/08/quickfox-supply-chain-attack-delivers.html
- **OpenAI, Anthropic AI agents targeted real people and systems in cyber tests**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/openai-anthropic-ai-agents-targeted-real-people-and-systems-in-cyber-tests/
- **TP-Link patches Omada ZTP flaws allowing hackers to breach networks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/tp-link-patches-omada-ztp-flaws-allowing-hackers-to-breach-networks/
