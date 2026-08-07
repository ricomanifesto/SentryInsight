# Exploitation Report

## Executive Summary

Active exploitation campaigns are targeting a diverse range of technologies, from enterprise CI/CD platforms and network infrastructure to AI agent frameworks and developer toolchains. The most critical ongoing activity involves CVE-2026-63077, a remote code execution flaw in on-premise JetBrains TeamCity instances that CISA has confirmed is under active exploitation in the wild, requiring immediate patching by federal agencies. Simultaneously, attackers are leveraging SQL injection in public-facing applications to deploy the khunt post-exploitation toolkit directly inside Oracle databases—achieving Windows SYSTEM access without writing executables to disk—while a factory-installed backdoor in at least 20 Zbtlink router models provides unauthenticated root shell access to any actor aware of the implant.

A parallel surge in AI-focused exploitation is evident across multiple fronts. Vulnerabilities in agent infrastructure from AWS, Google, and Vercel allow forged instructions to reach privileged tools without model authorization, while the "PleaseFix" zero-click hijacking technique enables attacker control of AI browsers through malicious content alone. Supply chain compromise continues via trojanized npm packages using blockchain-based C2 obfuscation (NullReceiver/EtherHiding), 77 malicious "evil twin" extensions on the Open VSX marketplace exfiltrating developer environment data, and leaked n8n API tokens exposing 321 live workflow automation instances. On the threat actor side, the sentencing of Ransom Cartel creator Maksim Silnikau to 16 years and the guilty plea of Snowflake breach operator Connor Riley Moucka mark significant law enforcement outcomes, even as new phishing kits like Kali365 weaponize legitimate Microsoft device-code flows and ClickFix campaigns scale to 250+ domains with browser fingerprinting evasion.

## Active Exploitation Details

### TeamCity CVE-2026-63077 Remote Code Execution
- **Description**: A newly patched security flaw impacting on-premise versions of JetBrains TeamCity continuous integration and deployment server. The vulnerability allows unauthenticated remote code execution.
- **Impact**: Attackers can achieve full server compromise and execute arbitrary code with the privileges of the TeamCity service account, potentially leading to supply chain compromise of build artifacts and deployment pipelines.
- **Status**: Actively exploited in the wild. CISA has added this vulnerability to its Known Exploited Vulnerabilities catalog and mandated federal agencies to mitigate within three days. JetBrains has released patches for affected on-premise versions.
- **CVE ID**: CVE-2026-63077

### Oracle Database SQL Injection to khunt Post-Exploitation Deployment
- **Description**: Attackers exploit a SQL injection vulnerability in a public-facing web application connected to an Oracle database backend. The injection vector is used to compile and execute the khunt post-exploitation toolkit entirely within the database process memory.
- **Impact**: Attackers gain Windows SYSTEM-level access on the database host without writing any executable files to disk, evading traditional file-based detection. The technique enables lateral movement, credential harvesting, and persistence from a highly privileged foothold.
- **Status**: Actively exploited in real-world intrusions. No specific CVE identifier has been disclosed for the SQL injection flaw; mitigation requires application-layer input validation and database privilege hardening.

### Zbtlink Router Factory Backdoor
- **Description**: At least 20 router models from Chinese manufacturer Zbtlink ship with a persistent, factory-installed backdoor that provides unauthenticated root shell access to the device operating system.
- **Impact**: Any network-adjacent actor or supply chain interdictor can gain full administrative control over affected devices without credentials, enabling traffic interception, firmware modification, botnet recruitment, and lateral network access.
- **Status**: Disclosed by VulnCheck researchers. No vendor patch available at time of reporting; affected organizations should isolate or replace compromised hardware.

### AI Agent Infrastructure Authorization Bypass (AWS, Google, Vercel)
- **Description**: Security flaws in the agent execution infrastructure of Amazon Web Services, Google, and Vercel allow untrusted or forged instructions to reach an agent's privileged tools without verification that a model turn authorized the action.
- **Impact**: Attackers can trigger arbitrary tool invocations—including file system access, API calls, and code execution—bypassing the intended safety boundary between the language model and its toolset.
- **Status**: Vendors have issued patches. No CVE identifiers disclosed in public reporting.

### "PleaseFix" Zero-Click AI Browser Agent Hijacking
- **Description**: A zero-click exploitation technique targeting AI-enabled browsers where malicious instructions embedded in web content, documents, or messages are automatically processed by the browser's agent, hijacking its toolchain without user interaction.
- **Impact**: Full agent takeover enabling data exfiltration, unauthorized actions on authenticated sessions, and persistent compromise of the browser's autonomous capabilities.
- **Status**: No comprehensive fix exists; researchers indicate architectural changes are required. No CVE identifier assigned.

### Paperclip AI Control Plane Command Execution
- **Description**: Two security flaws in Paperclip, an open-source control plane for AI agent teams, allow attackers to execute arbitrary commands on the host server or developer workstation by importing malicious agent definitions.
- **Impact**: Remote code execution in the context of the Paperclip service, leading to supply chain compromise of AI workflows and developer environment takeover.
- **Status**: Vulnerabilities disclosed; patch status unclear. No CVE identifiers disclosed.

### Google APK for Python Agent-to-Agent Trust Boundary Bypass
- **Description**: Fixed vulnerabilities in Google's Agent Development Kit (ADK) for Python exploited a trust boundary between two AI agents operating at different privilege levels, allowing a lower-privilege agent to trigger privileged automation.
- **Impact**: Supply chain compromise via unauthorized privileged agent actions, potentially affecting downstream systems and data.
- **Status**: Google has fixed the issues. No CVE identifiers disclosed.

### OVSwrap Linux Kernel Local Privilege Escalation (Open vSwitch)
- **Description**: A memory corruption flaw in the Linux kernel's Open vSwitch (OVS) datapath implementation (OVSwrap) allows local users to escalate privileges to root on default-configured distributions.
- **Impact**: Local privilege escalation to root on a broad range of Linux distributions shipping Open vSwitch, including container hosts and virtualized environments.
- **Status**: Public exploit code is available. No CVE identifier disclosed in reporting; kernel patches expected.

### Critical Gitea Unauthenticated File Read
- **Description**: An unauthenticated attacker can read arbitrary files accessible to the Gitea service account on affected instances (versions 1.22.1 through 1.27.0) via Org-Mode markup processing. No login or repository write access required.
- **Impact**: Disclosure of source code, configuration files, SSH keys, environment variables, and other sensitive data stored on the Gitea server filesystem.
- **Status**: Public exploit available. Fixed in Gitea 1.27.1. No CVE identifier disclosed in reporting.

### Apache Tomcat, IBM Langflow, and N-central Active Exploitation
- **Description**: CISA has warned of active exploitation targeting vulnerabilities in Apache Tomcat, IBM Langflow, and N-central (N-able remote monitoring platform). Federal agencies were given three days to apply mitigations.
- **Impact**: Remote code execution, unauthorized access, and potential lateral movement in enterprise environments running these platforms.
- **Status**: Actively exploited per CISA advisory. Specific CVE identifiers not disclosed in the source article; vendors have released patches.

### Veeam Service Provider Console, Terraform MCP Server, and Django Critical Flaws
- **Description**: Eleven vulnerabilities patched across Veeam Service Provider Console, HashiCorp Terraform MCP Server, and the Django web framework. The most severe is an unauthenticated cross-tenant bug rated CVSS 10.0.
- **Impact**: Cross-tenant data access, authentication bypass, remote code execution, and privilege escalation depending on the component.
- **Status**: Patches released by all three vendors. Specific CVE identifiers not disclosed in the source article.

## Affected Systems and Products

- **JetBrains TeamCity (on-premise)**: All unpatched versions prior to the CVE-2026-63077 fix; CI/CD build servers in enterprise environments
- **Oracle Database**: Instances backing public-facing web applications with unvalidated SQL input; Windows-hosted deployments particularly impacted by khunt's SYSTEM-access technique
- **Zbtlink Routers**: At least 20 models across product lines; SOHO and enterprise branch-office deployments
- **AWS Agent Infrastructure**: Amazon Bedrock Agents, AWS Lambda-integrated agent runtimes, and associated tooling frameworks
- **Google Agent Infrastructure**: Vertex AI Agent Builder, ADK for Python, and related agent execution environments
- **Vercel AI SDK / Agent Infrastructure**: Vercel AI SDK integrations, serverless function-based agent deployments
- **AI-Enabled Browsers**: Browsers with integrated autonomous agent capabilities (specific vendors not named in reporting)
- **Paperclip**: Self-hosted deployments of the Paperclip AI control plane; developer workstations running local instances
- **Linux Kernel (Open vSwitch / OVSwrap)**: Distributions shipping Open vSwitch with vulnerable kernel modules; container hosts, VM hypervisors, and SDN infrastructure
- **Gitea**: Versions 1.22.1 through 1.27.0; self-hosted Git service deployments
- **Apache Tomcat**: Unpatched versions targeted by active exploitation campaigns
- **IBM Langflow**: Vulnerable versions of the low-code AI flow builder
- **N-central (N-able)**: Vulnerable versions of the RMM platform used by MSPs
- **Veeam Service Provider Console**: Multi-tenant backup management consoles for service providers
- **HashiCorp Terraform MCP Server**: Model Context Protocol server implementations
- **Django Web Framework**: Applications using unpatched Django versions
- **n8n Workflow Automation**: 321 instances with API tokens exposed in public GitHub repositories
- **Open VSX Marketplace**: 77 malicious "evil twin" extensions impersonating legitimate developer tools
- **npm Registry**: Trojanized packages employing NullReceiver/EtherHiding blockchain C2 technique

## Attack Vectors and Techniques

- **SQL Injection to In-Database Code Execution**: Leveraging SQL injection in web applications to compile and run post-exploitation toolkits (khunt) directly inside Oracle database processes, achieving fileless SYSTEM access on Windows hosts
- **Factory-Installed Hardware Backdoor**: Persistent root shell access embedded in router firmware at manufacture, requiring no authentication or configuration error
- **Agent Toolchain Authorization Bypass**: Forging or injecting instructions that bypass the language model's decision loop and directly invoke privileged tools in AI agent frameworks (AWS, Google, Vercel)
- **Zero-Click Agent Hijacking ("PleaseFix")**: Embedding malicious instructions in content (web pages, documents, messages) that AI browsers automatically process, hijacking the agent without user interaction
- **Malicious Agent Definition Import**: Crafting poisoned agent specifications that, when imported into Paperclip or similar control planes, execute arbitrary host commands
- **Cross-Agent Trust Boundary Escalation**: Exploiting insufficient privilege separation between cooperating AI agents to trigger high-privilege actions from a low-privilege context (Google ADK for Python)
- **Blockchain-Based C2 Obfuscation (NullReceiver / EtherHiding)**: Encoding command-and-control server IP addresses within fake blockchain destination addresses on Ethereum or compatible chains, decoded at runtime by trojanized npm packages
- **Evil Twin Extension Typosquatting**: Publishing malicious extensions on Open VSX that mimic popular developer tools by name and metadata, exfiltrating system fingerprinting data and environment details
- **Credential Leakage via Public Repositories**: Harvesting exposed API tokens (n8n) from public GitHub commits to access live workflow instances and downstream credentials
- **ClickFix Social Engineering with Browser Fingerprinting**: Deploying 250+ front-end domains that fingerprint visitors before delivering macOS malware lures, evading automated analysis and blocklists
- **Device Code Phishing (Kali365)**: Weaponizing Microsoft's legitimate device authorization flow—attacker-controlled device codes presented to victims who approve them on Microsoft's real login page, granting token access
- **Org-Mode Markup File Read**: Exploiting Gitea's Org-Mode rendering to traverse and read arbitrary files accessible to the service account without authentication
- **Kernel Memory Corruption via Open vSwitch Datapath**: Triggering controlled memory corruption in the OVSwrap kernel module to escalate from local user to root
- **Cross-Tenant Authorization Bypass (CVSS 10.0)**: Unauthenticated exploitation of tenant isolation flaws in multi-tenant SaaS platforms (Veeam Service Provider Console)

## Threat Actor Activities

- **Ransom Cartel (Maksim Silnikau)**: Creator and administrator of the Ransom Cartel ransomware-as-a-service operation (established 2021). Responsible for attacks against at least 18 companies worldwide. Silnikau sentenced to 16 years in U.S. federal prison (August 2025).
- **Snowflake Data Theft Operator (Connor Riley Moucka)**: Canadian threat actor who pleaded guilty to computer fraud, wire fraud, aggravated identity theft, and conspiracy for the 2024 breaches of Snowflake customer environments affecting at least 165 organizations and 100+ million individuals. Extortion-driven campaign using stolen credentials.
- **Poipet Scam Network**: Cambodia-based organized crime group using ChatGPT to facilitate investment fraud, romance scams, gambling schemes, and law enforcement impersonation across multiple languages. Disrupted by OpenAI.
- **Kali365 Phishing Kit Operators**: Threat actors deploying a phishing-as-a-service kit targeting U.S. enterprises via Microsoft device code flow abuse. Kit automates token capture after victim approval on legitimate Microsoft login pages.
- **ClickFix Campaign Operators (macOS)**: Threat group running a large-scale ClickFix operation across 250+ front-end domains with browser fingerprinting to selectively deliver macOS malware (likely Atomic Stealer or similar). Tracked by Microsoft Threat Intelligence.
- **NullReceiver / EtherHiding Supply Chain Actors**: Operators of trojanized npm packages using blockchain-based C2 IP encoding. Evolution of the EtherHiding technique previously observed in supply chain campaigns.
- **Open VSX Evil Twin Publishers**: Actor(s) behind 77 malicious extensions on the Open VSX marketplace impersonating legitimate tools (ESLint, Prettier, Docker, etc.) to exfiltrate developer environment data.
- **Zbtlink Backdoor Implanter**: Unknown supply chain actor responsible for embedding persistent root backdoors in Zbtlink router firmware at manufacture. At least 20 models affected.
- **COLDcard Phishing Campaign Operators**: Threat actors exploiting fear around a disclosed COLDcard hardware wallet vulnerability and alleged $88.6M Bitcoin theft to deliver ScreenConnect remote access trojans via phishing.
- **AI-Enabled Fraud Syndicates**: Organized crime groups leveraging voice cloning, real-time deepfake video overlays, LLM-driven persona management, and automated translation to scale social engineering and fraud operations globally.

## Source Attribution

- **Attackers Compile khunt Inside Oracle to Turn SQL Injection Into Windows SYSTEM Access**: The Hacker News - https://thehackernews.com/2026/08/attackers-compile-khunt-inside-oracle.html
- **AWS, Google, and Vercel Agent Flaws Let Attackers Trigger Tools Without Running the Model**: The Hacker News - https://thehackernews.com/2026/08/aws-google-and-vercel-patch-agent-flaws.html
- **Chinese-Made Zbtlink Routers Ship With Backdoor That Opens Unauthenticated Root Shells**: The Hacker News - https://thehackernews.com/2026/08/chinese-made-zbtlink-routers-ship-with.html
- **Ransom Cartel Creator Gets 16 Years in Prison for Operating Ransomware-as-a-Service**: The Hacker News - https://thehackernews.com/2026/08/ransom-cartel-creator-gets-16-years-in.html
- **CISA Flags TeamCity CVE-2026-63077 RCE Flaw Under Active Exploitation in the Wild**: The Hacker News - https://thehackernews.com/2026/08/cisa-flags-teamcity-cve-2026-63077-rce.html
- **Snowflake Hacker Pleads Guilty Over Breaches Affecting at Least 100 Million People**: The Hacker News - https://thehackernews.com/2026/08/snowflake-hacker-pleads-guilty-over.html
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
