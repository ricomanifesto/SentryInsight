---
schema_version: 2
report_date: 2026-09-23
generated_at: 2026-09-23T16:39:12Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-23/
---
# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are being actively exploited in the wild across diverse technology stacks, ranging from network infrastructure and container runtimes to AI-driven attack frameworks. Chinese threat actor UTA0565 has weaponized a Chrome-Windows exploit chain (CVE-2026-85046, CVE-2026-87491, CVE-2026-85880) to deploy CLEANGULP malware through fake websites, while the ShinyHunters extortion group claims to have breached the FBI using an Oracle PeopleSoft zero-day.

Simultaneously, F5 BIG-IP APM (CVE-2026-94127) and Check Point Security Management Server (CVE-2026-93616) zero-days have been exploited for unauthenticated remote code execution, with patches released on September 22. A financially motivated actor is leveraging open-source AI agent frameworks to compromise over 100 e-commerce sites and steal 600,000+ credit card records at unprecedented scale.

## Active Exploitation Details

### MikroTrick Chain (MikroTik RouterOS SSH Vulnerabilities)
- **Description**: Two vulnerabilities in MikroTik RouterOS SSH implementation chained together to achieve unauthenticated administrative control. CVE-2026-67279 is an SSH state-machine flaw, and CVE-2026-86060 is an argument-injection bug in the RouterOS login process. The chain, dubbed "MikroTrick" by CERT Polska, allows attackers to take full control of Internet-exposed routers without a password, SSH key, or completed authentication.
- **Impact**: Full administrative control of affected MikroTik routers, enabling network pivoting, traffic interception, and persistent access.
- **Status**: Actively exploited; attack logs indicate ongoing activity. Vendor patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-67279, CVE-2026-86060
- **Reporting**: [The Hacker News — MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key](https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html)

### Ubuntu Linux AF_UNIX Socket Use-After-Free (Container Escape)
- **Description**: A use-after-free vulnerability in the Linux kernel's AF_UNIX socket subsystem (CVE-2026-80521, CVSS 7.8) allows container escape and host root privilege escalation. The flaw was fixed upstream on August 6, 2026, but Ubuntu has not yet shipped the patch for its 26.04, 24.04, or 22.04 LTS releases. DepthFirst published a working exploit on September 22.
- **Impact**: Attackers with container access can escape to the host and gain root privileges, compromising the entire host system and potentially other containers.
- **Status**: Exploit publicly released; Ubuntu LTS releases remain unpatched as of September 22.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **CVE IDs**: CVE-2026-80521
- **Reporting**: [The Hacker News — Exploit Released for Unpatched Ubuntu Linux Flaw Enabling Host-Root Container Escape](https://thehackernews.com/2026/09/exploit-released-for-unpatched-ubuntu.html)

### F5 BIG-IP APM OAuth Authorization Server Zero-Day
- **Description**: A critical vulnerability in F5 BIG-IP Access Policy Manager (APM) when configured as an OAuth authorization server (CVE-2026-94127). The flaw allows unauthenticated remote code execution on the BIG-IP system. F5 disclosed the vulnerability on September 22 and released engineering hotfixes.
- **Impact**: Unauthenticated remote code execution on BIG-IP systems serving as OAuth authorization servers, leading to full device compromise.
- **Status**: Actively exploited in the wild; patches/hotfixes released September 22.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-94127
- **Reporting**: [The Hacker News — F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html), [Bleeping Computer — F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)

### Chrome-Windows Zero-Day Exploit Chain (CLEANGULP Deployment)
- **Description**: Chinese threat actor UTA0565 exploited a chain of three zero-day vulnerabilities—two in Google Chrome (CVE-2026-85046, CVE-2026-87491) and one in Windows Advanced Local Procedure Call (CVE-2026-85880)—through fake websites to deploy CLEANGULP malware. Attacks were detected on September 3 and 4, 2026.
- **Impact**: Remote code execution and malware deployment via drive-by compromise; full system compromise on targeted endpoints.
- **Status**: Actively exploited as zero-days in early September 2026; vendor patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- **Reporting**: [The Hacker News — Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

### Check Point Security Management Server Zero-Day
- **Description**: A previously unknown flaw in Check Point's Security Management Server (CVE-2026-93616) allows an attacker with access to the server's web service to execute scripts without authentication. The vulnerability was exploited in a handful of targeted attacks on July 23, 2026. Check Point released a fix on September 22.
- **Impact**: Unauthenticated script execution on the management server that controls firewall policies, enabling policy manipulation and network control.
- **Status**: Exploited in targeted attacks July 23; patch released September 22.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-93616
- **Reporting**: [The Hacker News — Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks](https://thehackernews.com/2026/09/check-point-warns-of-management-server.html)

### Arista VeloCloud Orchestrator Zero-Day
- **Description**: A zero-day vulnerability in Arista VeloCloud Orchestrator (VCO) On-Prem deployments that is being actively exploited. Arista Networks released security patches on September 22.
- **Impact**: Compromise of VCO On-Prem management infrastructure, potentially affecting SD-WAN policy and visibility.
- **Status**: Actively exploited; patches released September 22.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Arista patches actively exploited VeloCloud Orchestrator zero-day](https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/)

### cPanel CalDAV/CardDAV and WP Toolkit Vulnerabilities
- **Description**: A flaw in cPanel's CalDAV and CardDAV service allows any hosting account holder to execute code as root and take full server control. A second vulnerability in the WP Toolkit plugin permits an account holder to modify databases belonging to other accounts. cPanel released fixed versions on September 22.
- **Impact**: Full server compromise via root code execution; cross-account data manipulation in shared hosting environments.
- **Status**: Patches released September 22; exploitation status not explicitly confirmed in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html)

### Next.js ImageResponse Server-Side Code Execution
- **Description**: A vulnerability in Next.js ImageResponse feature allows server-side code execution when attacker-controlled values (such as text from request URLs) are rendered into generated images via crafted SVG input. Vercel fixed the flaw on September 22.
- **Impact**: Remote code execution on Next.js servers using ImageResponse with user-supplied input.
- **Status**: Patch released September 22; active exploitation not confirmed in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html)

### Oracle PeopleSoft Zero-Day (ShinyHunters FBI Breach Claim)
- **Description**: ShinyHunters claims to have breached FBI systems using a new Oracle PeopleSoft zero-day vulnerability, gaining access to internal services and stealing sensitive data on employees and job applicants.
- **Impact**: Unauthorized access to sensitive government personnel data; potential compromise of federal systems.
- **Status**: Claimed exploitation by threat actor; no vendor advisory or CVE published at time of reporting.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)

### AI Agent-Driven Credit Card Skimming Campaign
- **Description**: A financially motivated threat actor is using open-source AI agent frameworks to automate attacks against hundreds of online retailers at scale, injecting malicious skimmers and stealing over 600,000 credit card records across 100+ compromised sites.
- **Impact**: Mass payment card theft; persistent compromise of e-commerce infrastructure.
- **Status**: Active, ongoing campaign at scale.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Malicious AI agents steal 600K credit cards, infect 100+ sites with skimmers](https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/)

### CLOSEDQUORUM AI-Driven Windows Malware
- **Description**: Windows malware (CLOSEDQUORUM) that uses a voting mechanism among up to four AI models (Google Gemini, DeepSeek, Qwen, Mistral) to autonomously determine post-compromise actions including credential theft, browser password extraction, and crypto wallet targeting. Cisco Talos reported the malware on September 22; the public version is non-functional.
- **Impact**: Autonomous post-exploitation decision-making; credential and cryptocurrency theft.
- **Status**: Proof-of-concept / developmental; not observed in successful end-to-end operations.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — This Windows Malware is Built to Let Up to Four AI Models Vote on Its Next Move](https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html), [Bleeping Computer — New ClosedQuorum Windows malware uses AI for attack decisions](https://www.bleepingcomputer.com/news/security/new-closedquorum-windows-malware-uses-ai-for-attack-decisions/)

### MemTensor Supply Chain Compromise (sckit Implant)
- **Description**: Unknown threat actors compromised legitimate MemTensor packages (@memtensor/memos-cloud-openclaw-plugin) on both npm and PyPI to deliver a cross-platform Go-based credential stealer (sckit) targeting Windows, Linux, and macOS.
- **Impact**: Credential theft across development environments; supply chain contamination affecting downstream consumers.
- **Status**: Active supply chain compromise; malicious packages identified by multiple security firms.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI](https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html)

### Kubernetes/GCP Config Connector Privilege Escalation
- **Description**: A confused deputy vulnerability in Google Kubernetes Config Connector allows a Kubernetes user with limited permissions to escalate to full Google Cloud organization control via a single malicious YAML file.
- **Impact**: Organization-wide privilege escalation in GCP; complete control over cloud resources.
- **Status**: Proof-of-concept demonstrated by Varonis; active exploitation not confirmed.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — How One Kubernetes YAML Can Hand Over a GCP Organization](https://www.bleepingcomputer.com/news/security/how-one-kubernetes-yaml-can-hand-over-a-gcp-organization/)

### Rogue External MFA Provider Credential Theft
- **Description**: Researchers demonstrated an attack where privileged actors can register a rogue external MFA provider to intercept and steal user passwords during legitimate login flows.
- **Impact**: Credential harvesting from authenticated sessions; bypass of MFA protections.
- **Status**: Research proof-of-concept; no confirmed active exploitation.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Rogue external MFA providers can steal passwords during logins](https://www.bleepingcomputer.com/news/security/rogue-external-mfa-providers-can-steal-passwords-during-logins/)

## Affected Systems and Products

- **MikroTik RouterOS**: Internet-exposed routers running vulnerable RouterOS versions; SSH service accessible from untrusted networks
- **Ubuntu Linux**: 26.04, 24.04, and 22.04 LTS releases (container hosts running unpatched kernels)
- **F5 BIG-IP Access Policy Manager**: Systems configured as OAuth authorization servers issuing access tokens
- **Google Chrome + Microsoft Windows**: Endpoints running unpatched Chrome and Windows versions (ALPC subsystem)
- **Check Point Security Management Server**: Management servers with web service accessible to attackers (controls firewall policies)
- **Arista VeloCloud Orchestrator**: On-Prem deployments (cloud-managed SD-WAN orchestration)
- **cPanel & WHM**: Shared hosting servers running vulnerable CalDAV/CardDAV service and WP Toolkit plugin
- **Next.js Applications**: Applications using ImageResponse feature with user-controlled input in image generation
- **Oracle PeopleSoft**: Enterprise deployments potentially vulnerable to undisclosed zero-day
- **ZyXEL GS1900 Smart Managed Switches**: Network switches exploited by Chinese-speaking threat actor
- **WordPress**: Sites exploited in conjunction with ZyXEL flaws for government data theft
- **Google Kubernetes Engine / Config Connector**: GCP organizations using Config Connector for Kubernetes resource management
- **npm / PyPI Package Repositories**: Developers and CI/CD pipelines consuming compromised @memtensor/memos-cloud-openclaw-plugin packages
- **Microsoft 365**: Accounts targeted by EvilTokens device code phishing-as-a-service platform
- **E-commerce Platforms**: Online retailers using platforms vulnerable to AI-agent-driven skimmer injection

## Attack Vectors and Techniques

- **AI Agent Framework Automation**: Financially motivated actors using open-source AI agent frameworks (e.g., LangChain, AutoGPT-style architectures) to orchestrate large-scale web attacks, including vulnerability discovery, exploitation, and skimmer injection across hundreds of targets simultaneously
- **Multi-Stage Browser/OS Exploit Chaining**: UTA0565 combining Chrome renderer exploits (CVE-2026-85046, CVE-2026-87491) with Windows kernel ALPC vulnerability (CVE-2026-85880) for sandbox escape and malware deployment via drive-by download
- **SSH Protocol State Machine Manipulation**: MikroTrick chain exploiting SSH protocol implementation flaws (state machine + argument injection) to bypass authentication entirely on network infrastructure
- **Container Escape via Kernel Use-After-Free**: AF_UNIX socket subsystem flaw (CVE-2026-80521) enabling breakout from containerized workloads to host root
- **OAuth Authorization Server RCE**: Unauthenticated code execution on F5 BIG-IP APM via crafted requests to OAuth endpoints
- **Management Interface Script Injection**: Unauthenticated script execution on Check Point Management Server web interface (CVE-2026-93616)
- **Confused Deputy / Privilege Escalation via Config Connector**: Abusing Google Kubernetes Config Connector's elevated service account permissions through malicious Kubernetes YAML to gain GCP organization admin
- **Supply Chain Compromise (npm/PyPI)**: Legitimate package takeover (@memtensor/memos-cloud-openclaw-plugin) delivering cross-platform Go implant (sckit) for credential theft
- **AI Model Poisoning for Disinformation/Phishing**: Seeding web content with malicious links/data optimized for LLM ingestion to manipulate ChatGPT, Gemini, and Google AI Overview outputs
- **AI Voting for Malware C2 Decisions**: CLOSEDQUORUM malware using ensemble of LLMs (Gemini, DeepSeek, Qwen, Mistral) to autonomously select post-exploitation actions
- **Rogue External MFA Provider Registration**: Privileged attacker registering malicious MFA provider to intercept credentials during legitimate authentication flows
- **Device Code Phishing (EvilTokens)**: Phishing-as-a-service leveraging OAuth device authorization flow to compromise Microsoft 365 accounts without credential harvesting pages
- **Web Application Skimmer Injection**: Automated injection of JavaScript payment skimmers into checkout pages via compromised admin interfaces or vulnerable plugins
- **Zero-Day Exploitation of Network Management Interfaces**: Targeting of vendor management consoles (Check Point, Arista VCO, MikroTik) for network infrastructure control

## Threat Actor Activities

- **UTA0565 (Chinese APT)**: Observed exploiting Chrome-Windows zero-day chain (CVE-2026-85046, CVE-2026-87491, CVE-2026-85880) via fake websites on September 3–4, 2026, deploying CLEANGULP malware; high-confidence attribution to Chinese state-sponsored activity
- **ShinyHunters (Cyber Extortion Group)**: Claims responsibility for FBI breach using alleged Oracle PeopleSoft zero-day; publicized theft of sensitive data on FBI agents and job applicants on dark web; previously associated with major data breaches and extortion campaigns
- **Chinese-Speaking Threat Actor (Unnamed)**: Exploiting ZyXEL GS1900 switch vulnerabilities and WordPress flaws to compromise 996 devices and exfiltrate 18,500+ records from government backend databases; targeting aligns with espionage objectives
- **Financially Motivated Actor (AI Agent Operator)**: Deploying open-source AI agent frameworks to automate mass compromise of e-commerce platforms; 100+ sites infected with skimmers; 600,000+ credit cards stolen; represents paradigm shift toward AI-orchestrated crime-at-scale
- **Unknown Actor (MemTensor Supply Chain)**: Compromised legitimate maintainer accounts or build pipelines for @memtensor/memos-cloud-openclaw-plugin on npm and PyPI; delivered sckit credential stealer across Windows, Linux, macOS; operational security suggests experienced operator
- **EvilTokens Operators (Phishing-as-a-Service)**: Ran device code phishing platform targeting Microsoft 365; infrastructure disrupted by Microsoft (50 sites seized, 150+ domains disabled); service enabled low-skill affiliates to bypass MFA
- **Ryuk Ransomware Affiliate (Armenian National)**: Sentenced to 24 months for Ryuk ransomware attacks against U.S. companies; illustrates continued law enforcement pressure on ransomware ecosystem
- **InfraTrust-Observed Actors (Unattributed)**: Targeting network management systems across enterprises; exploiting critical vulnerabilities in management interfaces before or shortly after vendor disclosure; suggests dedicated infrastructure-targeting capability