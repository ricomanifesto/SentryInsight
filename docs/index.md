# Exploitation Report

## Executive Summary

Organized crime syndicates have achieved unprecedented fraud scale through AI-enabled tooling, including real-time voice cloning, deepfake video overlays, LLM-driven persona management, and automated translation. These capabilities allow convincing social engineering at industrial volume, rendering traditional blocklist defenses obsolete as attackers generate disposable phishing infrastructure faster than reputation systems can track. Simultaneously, a Cambodian scam network dubbed Poipet leveraged ChatGPT across investment, romance, gambling, and law-enforcement impersonation schemes before OpenAI disrupted the operation.

Critical enterprise software is under active exploitation. CISA has added three vulnerabilities—affecting Langflow, N-central, and Apache Tomcat—to its Known Exploited Vulnerabilities catalog with evidence of in-the-wild abuse, giving federal agencies three days to mitigate. TP-Link has patched 15 zero-touch provisioning flaws in Omada devices that can be chained for remote code execution, while a long-standing supply chain compromise of the QuickFox VPN tool delivered the FDMTP backdoor via trojanized Windows installers. The Ransom Cartel ransomware operator was sentenced to 16 years for attacks against at least 18 companies, and a Canadian threat actor pleaded guilty to stealing data from 165 organizations via compromised Snowflake credentials.

Novel attack vectors are proliferating across the software supply chain and AI ecosystem. Researchers demonstrated zero-click "PleaseFix" agent hijacking in AI browsers, persistent prompt injection flaws with no perfect fix, agent-to-agent trust boundary exploits in Google's APK for Python, and command execution via malicious agent imports in Paperclip AI. A memory corruption flaw in the Linux kernel's Open vSwitch datapath (OVSwrap) provides local privilege escalation with a public exploit. Threat actors are weaponizing CSS for webmail data exfiltration, blockchain-based C2 channels (EtherHiding/NullReceiver) in trojanized npm packages, Microsoft device-code authentication flows via the Kali365 phishing kit, and browser fingerprinting across 250+ ClickFix domains targeting macOS. Meanwhile, 77 malicious "evil twin" extensions were removed from Open VSX, 321 n8n instances were found with exposed API tokens, and a phishing campaign exploits COLDCARD vulnerability fears to deploy ScreenConnect remote access tools.

## Active Exploitation Details

### PleaseFix Zero-Click Agent Hijacking
- **Description**: Attackers can take control of AI browser agents through malicious instructions hidden in content supplied to the browser, requiring zero user interaction beyond visiting a compromised page or processing malicious content.
- **Impact**: Full agent takeover allowing arbitrary actions within the AI browser's permission context, including data access, automation triggers, and potential lateral movement.
- **Status**: Actively exploitable with no simple fix; architectural challenge in separating trusted and untrusted instruction streams.

### Langflow Remote Code Execution
- **Description**: A vulnerability in Langflow (a visual framework for building AI agents and RAG applications) allowing unauthenticated remote code execution.
- **Impact**: Full server compromise, access to connected data sources and AI model credentials, potential supply chain impact on downstream AI applications.
- **Status**: Actively exploited in the wild; added to CISA KEV catalog on August 5, 2026.

### N-central Vulnerabilities
- **Description**: Flaws in N-able N-central remote monitoring and management platform.
- **Impact**: Compromise of managed service provider infrastructure, potential access to all downstream client environments.
- **Status**: Actively exploited in the wild; added to CISA KEV catalog on August 5, 2026.

### Apache Tomcat Vulnerabilities
- **Description**: Vulnerabilities in Apache Tomcat servlet container.
- **Impact**: Remote code execution, information disclosure, or denial of service on affected Tomcat deployments.
- **Status**: Actively exploited in the wild; added to CISA KEV catalog on August 5, 2026.

### TP-Link Omada Zero-Touch Provisioning Flaws
- **Description**: Fifteen vulnerabilities in the zero-touch provisioning (ZTP) mechanism of TP-Link Omada network devices, chainable with previously disclosed flaws.
- **Impact**: Remote code execution on network infrastructure devices, full network compromise, persistence at the network layer.
- **Status**: Patched by TP-Link; exploitation requires chaining multiple vulnerabilities.

### COLDCARD Wallet Vulnerability (Exploited via Phishing)
- **Description**: A vulnerability in COLDCARD hardware wallets (details tied to suspected $88.6M Bitcoin theft) being leveraged as a phishing lure.
- **Impact**: Credential theft and remote access tool (ScreenConnect) installation on victim systems via fear-based social engineering.
- **Status**: Phishing campaign actively exploiting vulnerability disclosure publicity; patch status of underlying wallet flaw unclear from reporting.

### Oracle Database SQL Injection to khunt Toolkit Deployment
- **Description**: SQL injection vulnerability in an Oracle database exploited to install the khunt post-exploitation toolkit directly inside the database.
- **Impact**: Persistent database-level foothold, credential harvesting, lateral movement to corporate network breach.
- **Status**: Actively exploited; demonstrates novel database-resident post-exploitation technique.

### QuickFox Supply Chain Attack (FDMTP Backdoor)
- **Description**: Long-standing supply chain compromise of QuickFox VPN/network acceleration tool delivering FDMTP backdoor via trojanized Windows installer.
- **Impact**: Persistent remote access to overseas users' systems, potential network traffic interception and credential theft.
- **Status**: Disclosed by researchers; scope and duration of compromise described as "long-standing."

### Gitea Unauthenticated File Read
- **Description**: Critical flaw in Gitea (self-hosted Git platform) versions 1.22.1 through 1.27.0 allowing unauthenticated attackers to read any file accessible to the service account via Org-Mode markup processing.
- **Impact**: Source code exposure, configuration secret theft, SSH key compromise, internal infrastructure reconnaissance.
- **Status**: Public exploit available; affects wide version range.

### Paperclip AI Malicious Agent Import Flaws
- **Description**: Two security flaws in Paperclip (open-source AI agent control plane) allowing command execution on network servers or developer machines via malicious agent imports.
- **Impact**: Supply chain compromise of AI agent workflows, host compromise, lateral movement in development environments.
- **Status**: Vulnerabilities disclosed; patch status not specified in reporting.

### Google APK for Python Agent-to-Agent Attack
- **Description**: Trust boundary exploitation between two AI agents with different privilege levels in Google's Agent Development Kit (APK) for Python.
- **Impact**: Privilege escalation within agent workflows, potential supply chain automation compromise, unauthorized actions via lower-privileged agent manipulation.
- **Status**: Fixed by Google; demonstrates emerging class of multi-agent system vulnerabilities.

### OVSwrap Linux Kernel Local Privilege Escalation
- **Description**: Memory corruption flaw in the Linux kernel's Open vSwitch datapath (OVSwrap) giving ordinary local users a path to root on default-configured distributions.
- **Impact**: Full system compromise from any local user account; broad distribution impact due to default Open vSwitch inclusion.
- **Status**: Public exploit ships with pre-built binaries; patch status varies by distribution.

### ClickFix macOS Malware Campaign
- **Description**: Operation spanning 250+ front-end domains using browser fingerprinting to selectively deliver malware lures to macOS users.
- **Impact**: Targeted malware delivery evading automated analysis, macOS-specific payload deployment, infrastructure resilience through domain rotation.
- **Status**: Actively tracked by Microsoft Threat Intelligence; ongoing campaign.

### Kali365 Microsoft Device Code Phishing
- **Description**: Phishing kit weaponizing legitimate Microsoft device code authentication flow, targeting US organizations with attacker-controlled device codes.
- **Impact**: Account takeover bypassing MFA, persistent access via approved device registrations, enterprise data access.
- **Status**: Active campaign targeting US companies; leverages legitimate Microsoft infrastructure.

### Trojanized npm Packages with Blockchain C2 (NullReceiver/EtherHiding)
- **Description**: Evolution of EtherHiding technique concealing C2 server IP addresses inside made-up destination addresses on blockchain, deployed via trojanized npm packages.
- **Impact**: Resilient command-and-control infrastructure resistant to takedown, software supply chain compromise, developer environment infiltration.
- **Status**: Active technique observed in wild; packages identified by researchers.

### AI Browser Prompt Injection (Multi-Vendor)
- **Description**: Persistent prompt injection vulnerabilities across AI browsers from top vendors, bypassing multiple security guardrails.
- **Impact**: Data exfiltration, unauthorized actions, cross-origin attacks, plugin/extension abuse.
- **Status**: No perfect fix exists; guardrails provide partial mitigation only.

### Snowflake Credential-Based Data Theft
- **Description**: Compromise of Snowflake cloud storage accounts using stolen credentials to access and extort data from 165 organizations.
- **Impact**: Massive data breach across multiple victims, extortion demands in millions, cloud storage credential reuse risk.
- **Status**: Canadian perpetrator pleaded guilty; highlights cloud credential hygiene failures.

### Ransom Cartel Ransomware Operations
- **Description**: Ransomware-as-a-service operation conducting attacks against at least 18 companies worldwide.
- **Impact**: Data encryption, exfiltration, extortion, operational disruption across multiple sectors.
- **Status**: Creator/administrator Maksim Silnikau sentenced to 16 years; operation disrupted.

### Poison Claude Illicit AI Access Services
- **Description**: Underground services selling discounted access to Claude AI models while operators harvest all customer prompts.
- **Impact**: Intellectual property theft, prompt data harvesting, unauthorized AI usage, potential corporate secret exposure.
- **Status**: Multiple services advertised on cybercrime forums; ongoing illicit marketplace activity.

### n8n API Token Exposure
- **Description**: 321 live n8n workflow automation instances with API tokens exposed in public GitHub commits.
- **Impact**: Credential theft, downstream system access, workflow manipulation, sensitive data exposure across connected services.
- **Status**: Disclosed by GitGuardian; four exploitation paths demonstrated.

### Open VSX Malicious Evil Twin Extensions
- **Description**: Cluster of 77 extensions on Open VSX marketplace impersonating legitimate developer tools while exfiltrating system and development environment information.
- **Impact**: Developer machine reconnaissance, credential harvesting, source code theft, supply chain poisoning.
- **Status**: Removed from marketplace; installation count and impact assessment ongoing.

### CSS Webmail Data Exfiltration
- **Description**: CSS-based attacks capable of exfiltrating data from webmail interfaces through advanced selectors and layout manipulation techniques.
- **Impact**: Email content theft, contact harvesting, calendar data exposure, bypass of traditional script-based protections.
- **Status**: Researchers warn some vendors unprepared; client-side mitigation challenging.

### Veeam, Terraform MCP, and Django Critical Vulnerabilities
- **Description**: Eleven vulnerabilities patched across Veeam Service Provider Console, Terraform MCP Server, and Django, led by a CVSS 10.0 cross-tenant bug.
- **Impact**: Cross-tenant data access in multi-tenant environments, infrastructure-as-code compromise, web application takeover.
- **Status**: Patches released by all three vendors; CVSS 10.0 flaw represents highest severity.

### Unitel (Angola Telco) Breach
- **Description**: Cyberattack against Angola's largest mobile operator causing outages on the day of its government-owned IPO.
- **Impact**: Service disruption, reputational damage, potential financial market manipulation, critical infrastructure impact.
- **Status**: Recovery ongoing; timing suggests targeted operation.

## Affected Systems and Products

- **AI Browsers (Multiple Vendors)**: Vulnerable to PleaseFix zero-click hijacking and persistent prompt injection; no complete mitigation available
- **Langflow**: All versions prior to patched release; visual AI agent/RAG framework
- **N-able N-central**: Affected versions per CISA advisory; RMM platform used by MSPs
- **Apache Tomcat**: Affected versions per CISA advisory; widely deployed servlet container
- **TP-Link Omada Network Devices**: Devices with ZTP functionality; 15 vulnerabilities patched in firmware updates
- **COLD CARD Hardware Wallets**: Models affected by disclosed vulnerability; exploited via phishing lure
- **Oracle Database**: Versions with exploitable SQL injection vector; used as khunt toolkit deployment target
- **QuickFox VPN/Network Accelerator**: Trojanized Windows installer versions; supply chain compromise
- **Gitea**: Versions 1.22.1 through 1.27.0; self-hosted Git platform
- **Paperclip AI Control Plane**: Versions with agent import flaws; open-source AI agent orchestration
- **Google Agent Development Kit (APK) for Python**: Versions prior to fix; multi-agent development framework
- **Linux Kernel (Open vSwitch Datapath)**: Default-configured distributions shipping Open vSwitch; OVSwrap memory corruption
- **macOS Systems**: Targeted by ClickFix campaign across 250+ domains; browser fingerprinting evasion
- **Microsoft Entra ID / Azure AD**: Device code authentication flow abused by Kali365 phishing kit
- **npm Ecosystem**: Trojanized packages employing NullReceiver blockchain C2 technique
- **Snowflake Cloud Data Platform**: Customer instances compromised via credential theft (not platform vulnerability)
- **n8n Workflow Automation**: 321 instances with exposed API tokens in public GitHub repositories
- **Open VSX Marketplace**: 77 malicious extensions removed; VS Code / Open VSX compatible editors
- **Webmail Providers**: Various vendors vulnerable to CSS-based data exfiltration techniques
- **Veeam Service Provider Console**: Versions prior to patch; multi-tenant backup management
- **Terraform MCP Server**: Versions prior to patch; infrastructure-as-code management
- **Django Web Framework**: Versions prior to patch; Python web application framework
- **Unitel Telecommunications Infrastructure**: Angola's dominant mobile operator; critical national infrastructure

## Attack Vectors and Techniques

- **AI-Enabled Fraud Stack**: Voice cloning, real-time deepfake video overlays, LLM-driven persona management, automated translation enabling industrial-scale social engineering
- **Zero-Click Agent Hijacking (PleaseFix)**: Malicious instructions embedded in content processed by AI browsers, no user interaction required
- **Prompt Injection**: Persistent cross-vendor AI browser vulnerabilities bypassing guardrails via crafted inputs
- **SQL Injection**: Oracle database compromise enabling post-exploitation toolkit deployment
- **Supply Chain Compromise**: Trojanized legitimate software installers (QuickFox) and packages (npm) delivering persistent backdoors
- **Browser Fingerprinting Evasion**: ClickFix campaign using 250+ domains with fingerprinting to selectively target macOS users and evade analysis
- **Device Code Phishing (Kali365)**: Abuse of Microsoft's legitimate device authorization flow for MFA-bypassing account takeover
- **Blockchain-Based C2 (EtherHiding/NullReceiver)**: C2 IP addresses concealed in blockchain transactions via made-up destination addresses
- **CSS Data Exfiltration**: Advanced CSS selectors and layout manipulation extracting data from webmail without JavaScript execution
- **Agent-to-Agent Trust Boundary Exploitation**: Manipulation of lower-privileged AI agents to trigger privileged automation actions
- **Malicious Agent Import**: Command execution via compromised agent definitions in AI orchestration platforms
- **Local Kernel Privilege Escalation (OVSwrap)**: Memory corruption in Open vSwitch datapath granting root from unprivileged user
- **Unauthenticated File Read (Gitea)**: Org-Mode markup processing flaw exposing server filesystem
- **Credential Stuffing/Reuse**: Snowflake compromise via stolen credentials affecting 165 organizations
- **Ransomware-as-a-Service**: Ransom Cartel operation with affiliate model targeting 18+ companies
- **Illicit AI Access Marketplaces**: Poison Claude services harvesting prompts while providing unauthorized model access
- **API Token Harvesting**: GitHub scraping for exposed n8n tokens enabling downstream credential theft
- **Evil Twin Extension Typosquatting**: Malicious VS Code extensions impersonating legitimate tools for developer reconnaissance
- **Cross-Tenant Vulnerability Exploitation**: CVSS 10.0 flaw in multi-tenant backup/platform software
- **Phishing via Vulnerability Disclosure Fear**: COLDCARD vulnerability publicity used as lure for ScreenConnect deployment
- **Critical Infrastructure Timing**: Unitel breach coordinated with IPO for maximum impact

## Threat Actor Activities

- **Organized Crime Syndicates (Global)**: Industrial-scale AI fraud operations generating billions via voice cloning, deepfakes, LLM personas, and automated translation; rendered blocklists obsolete
- **Poipet Scam Network (Cambodia-based)**: Multi-scheme fraud operation (investment, romance, gambling, law enforcement impersonation) using ChatGPT; disrupted by OpenAI
- **Ransom Cartel (Maksim Silnikau)**: Ransomware-as-a-service creator/administrator sentenced to 16 years; attacks against 18+ companies worldwide
- **Kali365 Operators**: Phishing kit developers targeting US enterprises via Microsoft device code authentication; active campaign
- **ClickFix Threat Group**: Operators of 250+ domain infrastructure with browser fingerprinting for macOS malware delivery; tracked by Microsoft Threat Intelligence
- **QuickFox Supply Chain Attackers**: Long-standing compromise of VPN tool distribution; FDMTP backdoor deployment via trojanized installer
- **Snowflake Data Thief (Canadian Individual)**: Pleaded guilty to accessing 165 organizations' Snowflake accounts for data theft and extortion
- **khunt Toolkit Operators**: Actors deploying Oracle database-resident post-exploitation framework for corporate network breach
- **Poison Claude Operators**: Underground marketplace actors selling illicit AI access while harvesting customer prompts; multiple services advertised
- **EtherHiding/NullReceiver Developers**: Evolution of blockchain C2 technique deployed via trojanized npm packages targeting developers
- **OVSwrap Exploit Authors**: Published local privilege escalation exploit with pre-built binaries for Linux Open vSwitch flaw
- **Gitea Exploit Researchers/Actors**: Public exploit for unauthenticated file read in versions 1.22.1-1.27.0
- **Paperclip AI Vulnerability Researchers/Actors**: Disclosed command execution via malicious agent imports
- **Google APK Vulnerability Researchers**: Disclosed agent-to-agent trust boundary exploitation; fixed by Google
- **TP-Link ZTP Exploit Researchers/Actors**: 15 vulnerabilities disclosed and patched; chainable for RCE
- **Unitel Breach Actors (Unknown)**: Targeted attack on Angola's largest telco timed with IPO
- **COLD CARD Phishing Campaign Operators (Unknown)**: Leveraging vulnerability disclosure fear for ScreenConnect deployment
- **Open VSX Malicious Extension Publishers (Unknown)**: 77 evil twin extensions exfiltrating developer data
- **Veeam/Terraform/Django Vulnerability Researchers**: Disclosed 11 vulnerabilities including CVSS 10.0 cross-tenant bug
- **CSS Exfiltration Researchers**: Demonstrated webmail data theft via advanced CSS techniques
- **n8n Token Harvesters (Unknown)**: Actors scraping GitHub for exposed API tokens; 321 vulnerable instances identified

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
