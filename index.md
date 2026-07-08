# Exploitation Report

## Executive Summary

Active exploitation activity this period centers on a convergence of AI-enabled social engineering, infrastructure compromise for proxy networks, and actively exploited vulnerabilities in widely deployed enterprise and developer platforms. CISA has issued emergency directives for federal agencies to patch multiple actively exploited flaws—including a maximum-severity Adobe ColdFusion vulnerability, a Langflow authentication bypass, and additional Adobe, Joomla, and Langflow flaws added to the Known Exploited Vulnerabilities catalog—signaling immediate, real-world threat activity. Simultaneously, a 15-year-old Linux kernel privilege escalation flaw (CVE-2026-43499, "GhostLock") has been disclosed, enabling root access and container escape across most unpatched distributions.

Threat actors are rapidly operationalizing new techniques: China-linked UAT-7810 is expanding its Operational Relay Box (ORB) network via the LONGLEASH malware targeting unpatched networking devices, while financially motivated groups deploy ClickFix lures (SCMBANKER), device-code phishing (DEBULL), and Android malware-as-a-service (RedWing) against banking targets. AI-powered service desk impersonation, "ghost phishing" that evades email security through encrypted payloads, and GitHub Actions supply chain attacks demonstrate the maturation of identity and developer infrastructure as primary attack surfaces. High-profile breaches at KDDI (12M+ records) and Accenture (35 GB source code) underscore the impact of these campaigns.

## Active Exploitation Details

### GhostLock Linux Kernel Privilege Escalation (CVE-2026-43499)
- **Description**: A 15-year-old flaw in the Linux kernel (CVE-2026-43499) discovered by Nebula Security that allows any logged-in user to obtain full root control of an unpatched machine. The vulnerability also facilitates container escape, enabling breakout from containerized environments to the host system.
- **Impact**: Attackers with low-privileged local access can achieve complete system compromise, including root persistence and lateral movement across containerized workloads. Affects most Linux distributions that have not applied the patch.
- **Status**: Publicly disclosed with proof-of-concept; patching is urgent across all affected Linux distributions. No indication of prior widespread exploitation in the articles, but the age and breadth of impact make it a high-risk candidate for rapid weaponization.
- **CVE ID**: CVE-2026-43499

### Langflow Authentication Bypass
- **Description**: An actively exploited authentication bypass vulnerability in Langflow, a visual framework for building AI agents and LLM applications.
- **Impact**: Allows unauthenticated attackers to bypass authentication controls and potentially take control of AI agent workflows, access sensitive data, or manipulate AI-driven processes.
- **Status**: Actively exploited in the wild. CISA has ordered federal civilian agencies to prioritize patching by an emergency deadline, and the flaw was added to the KEV catalog.

### Adobe ColdFusion Maximum-Severity Flaw
- **Description**: A critical vulnerability in Adobe ColdFusion, a commercial web application development platform.
- **Impact**: Maximum-severity flaw enabling remote code execution or authentication bypass, leading to full server compromise.
- **Status**: Actively exploited. CISA issued an emergency directive ordering federal agencies to patch by Friday, and the vulnerability was added to the KEV catalog.

### Adobe, Joomla, and Additional Langflow Flaws (KEV Additions)
- **Description**: CISA added four actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog, affecting Adobe products, Joomla CMS, and additional Langflow components.
- **Impact**: Varies by component; includes remote code execution, authentication bypass, and data exposure in widely deployed enterprise and web platforms.
- **Status**: All four are confirmed actively exploited and now cataloged in KEV, mandating urgent remediation for federal agencies and strongly recommended for all organizations.

### Ubiquiti UniFi OS Command Injection (Maximum Severity)
- **Description**: Ubiquiti released patches for seven critical vulnerabilities in UniFi OS, including a maximum-severity command injection flaw.
- **Impact**: Unauthenticated or authenticated attackers can execute arbitrary commands on the underlying operating system of UniFi network management consoles, leading to full device compromise and network pivoting.
- **Status**: Patches released; active exploitation risk is high given the severity and internet-exposed nature of UniFi controllers.

### Dialogflow CX "Rogue Agent" Flaw
- **Description**: A critical flaw in Google Dialogflow CX that allowed an attacker with edit rights on one Code Block-enabled agent to compromise other Code Block-enabled agents within the same Google Cloud project.
- **Impact**: Cross-agent data theft and hijacking of AI chatbot logic, potentially exposing sensitive conversation data and enabling manipulation of automated customer interactions.
- **Status**: Reported to Google in late 2025 and addressed; organizations should verify patch deployment across Dialogflow CX projects.

### Writer AI Session Isolation Vulnerability
- **Description**: A critical session isolation flaw in Writer, an enterprise generative AI platform, that could leak session tokens across tenant boundaries in agent preview functionality.
- **Impact**: Cross-tenant session hijacking, enabling unauthorized access to other customers' AI agent sessions and proprietary data.
- **Status**: Now patched; enterprises using Writer should confirm update deployment.

### GitHub Agentic Workflows "GitLost" Data Leakage
- **Description**: A flaw in GitHub's Agentic Workflows (also referred to as "GitLost") where an unauthenticated attacker can craft a GitHub Issue in an organization's public repository and silently exfiltrate data from private repositories within the same organization.
- **Impact**: Unauthorized access to proprietary source code, secrets, and internal documentation across private repos triggered by a single public issue.
- **Status**: Disclosed by Noma Security; GitHub has been notified. Organizations using GitHub Agentic Workflows should review workflow permissions and monitor for anomalous issue activity.

### GitHub "Verified" Commit Hash Rewriting
- **Description**: Research demonstrating that a signed Git commit's hash can be rewritten into a new hash without breaking the cryptographic signature, undermining the assumption that a commit hash is a unique, immutable identifier.
- **Impact**: Supply chain integrity violations; attackers can present malicious code as a "verified" commit from a trusted developer, bypassing signature-based trust policies in CI/CD pipelines.
- **Status**: No patch available as this is a fundamental property of Git's design; mitigations require policy changes (e.g., requiring signed tags, commit verification beyond hash matching).

### GitHub Actions Attack Chains Evading CI Scanners
- **Description**: Attack patterns in GitHub Actions workflows that chain multiple steps to evade traditional CI security scanners, allowing malicious code execution during pipeline runs without detection.
- **Impact**: Persistent compromise of build pipelines, injection of malicious artifacts, and credential theft from runner environments.
- **Status**: Active research by ActiveState; no single CVE—defenders must implement behavioral pipeline monitoring and least-privilege runner configurations.

### Tenda Router Firmware Hidden Backdoor
- **Description**: A hidden authentication backdoor discovered in multiple Tenda router firmware versions that grants administrative access to the device's web management panel without valid credentials.
- **Impact**: Full administrative control over affected routers, enabling traffic interception, DNS hijacking, and network pivoting.
- **Status**: No patch information provided in the article; owners of Tenda routers should check vendor advisories and consider replacement if end-of-life.

## Affected Systems and Products

- **Langflow**: Visual framework for building AI agents/LLM applications — authentication bypass actively exploited; emergency patching mandated by CISA.
- **Adobe ColdFusion**: Commercial web application development platform — maximum-severity flaw actively exploited; CISA emergency directive issued.
- **Adobe Products (unspecified)**: Multiple Adobe vulnerabilities added to KEV catalog with confirmed active exploitation.
- **Joomla CMS**: Content management system — actively exploited flaw added to KEV catalog.
- **Linux Kernel (most distributions)**: 15-year-old GhostLock flaw (CVE-2026-43499) enabling root privilege escalation and container escape on unpatched systems.
- **Ubiquiti UniFi OS**: Network management operating system — seven critical vulnerabilities patched, including maximum-severity command injection.
- **Google Dialogflow CX**: Conversational AI platform — "Rogue Agent" flaw patched; affected Code Block-enabled agents in shared Google Cloud projects.
- **Writer AI Platform**: Enterprise generative AI platform — session isolation flaw in agent previews patched.
- **GitHub (Agentic Workflows, Actions, Verified Commits)**: Multiple attack surfaces — Agentic Workflow data leakage (GitLost), Actions attack chains evading scanners, commit hash rewriting undermining signature trust.
- **GitHub Copilot**: AI coding assistant — bypasses chat refusals by executing harmful requests via code editor context.
- **Microsoft M365 (Device Code Flow)**: Authentication flow abused by DEBULL tooling for phishing campaigns targeting collaboration-themed lures.
- **Tenda Routers (multiple firmware versions)**: Hidden authentication backdoor granting admin panel access.
- **Ruijie Routers**: Primary target of UAT-7810 for ORB network expansion via LONGLEASH malware (unpatched devices).
- **Android Devices**: Targeted by RedWing malware-as-a-service for banking credential theft and device takeover.
- **Mexican Financial Sector**: Banks, fintech platforms, payment processors, and cryptocurrency exchanges targeted by SCMBANKER via ClickFix lures.
- **KDDI Email Platform**: Breach affecting five Japanese ISPs and 12+ million users' email addresses and passwords.
- **Accenture Internal Systems**: 35 GB of source code and data stolen; threat actor offering data for sale.

## Attack Vectors and Techniques

- **AI-Powered Service Desk Impersonation**: Attackers use generative AI to create highly convincing, personalized, and scalable voice/video/text interactions that impersonate IT support, bypassing traditional verification during onboarding and password resets.
- **Ghost Phishing (EvilTokens Campaign)**: Malicious pages remain hidden until client-side decryption, evading static email security scanners and URL reputation checks; targets businesses in the US and Europe.
- **ClickFix Lures**: Social engineering technique tricking users into executing malicious commands (often via "fix" buttons or clipboard injection) to deploy malware like SCMBANKER.
- **Device Code Phishing (DEBULL Tooling)**: Abuses Microsoft's device authorization flow (RFC 8628) with collaboration-themed lures to hijack M365 accounts without credential theft; observed late June to early July 2026.
- **ORB Network Expansion via Compromised Network Devices**: UAT-7810 breaches internet-facing routers (primarily unpatched Ruijie) to deploy LONGLEASH malware, converting them into operational relay boxes for anonymizing further intrusions.
- **LONGLEASH Malware Deployment**: Custom malware used by UAT-7810 to maintain persistence on compromised networking equipment and proxy attacker traffic.
- **SCMBANKER Banking Malware**: Targets Mexican financial sector customers via ClickFix; steals banking credentials and session tokens for fraudulent transactions.
- **RedWing Android Malware-as-a-Service**: Rented on Telegram; provides turnkey bank fraud capability including overlay attacks, SMS interception, and remote device control for low-skill operators.
- **Dialogflow CX Cross-Agent Compromise**: Attacker with edit rights on one Code Block agent pivots to other agents in the same GCP project via the "Rogue Agent" flaw.
- **GitHub Agentic Workflow Data Exfiltration (GitLost)**: Public issue in a public repo triggers workflow execution that accesses and exfiltrates private repository contents.
- **GitHub Actions Supply Chain Attacks**: Multi-step attack chains in CI/CD pipelines that evade static scanners by splitting malicious logic across steps, using trusted actions, or abusing runner permissions.
- **Git Commit Hash Rewriting**: Generating new commit hashes that preserve valid signatures, allowing malicious code to masquerade as verified commits from trusted developers.
- **Nested Redirect Phishing Evasion**: Multi-layered redirect chains (Big Brand Jobs Scam) to evade URL analysis and steal Google credentials from marketing professionals.
- **Hidden Firmware Backdoor Exploitation**: Authentication bypass in Tenda router web management interfaces via undocumented backdoor credentials or endpoints.
- **GitHub Copilot Contextual Bypass**: Harmful requests refused in chat are fulfilled when decomposed into ordinary-looking steps within the code editor context.

## Threat Actor Activities

- **UAT-7810 (China-Linked)**: Actively expanding ORB network infrastructure by compromising internet-facing networking devices (primarily unpatched Ruijie routers) and deploying LONGLEASH malware. Tracked by multiple vendors; operations align with Chinese state-sponsored espionage objectives requiring anonymized relay infrastructure.
- **EvilTokens Operators**: Conducting "ghost phishing" campaign targeting businesses across the US and Europe; technique specifically designed to defeat traditional email security gateways through encrypted payload delivery.
- **SCMBANKER Operators**: Financially motivated group targeting customers of Mexican banks, fintechs, payment processors, and cryptocurrency exchanges using ClickFix social engineering lures. Activity cluster tracked by Elastic Security.
- **DEBULL Tooling Operators**: Running Microsoft 365 device code phishing campaign with collaboration-themed lures (late June–early July 2026); infrastructure and tooling suggest organized credential harvesting operation.
- **RedWing MaaS Operators**: Operating Android banking fraud-as-a-service on Telegram; lowers barrier to entry for mobile financial crime by providing rental access to sophisticated overlay, SMS interception, and RAT capabilities.
- **Scattered Spider (ALPHV/BlackCat Affiliate)**: Alleged member linked via Windows device ID to luxury jewelry retailer breach; court filing reveals FBI used persistent device identifiers for attribution. Group known for social engineering, SIM swapping, and SaaS/identity provider targeting.
- **CyberArmy of Russia Reborn (CARR) & Z-Pentest**: Pro-Russian hacktivist groups; Spanish authorities arrested a suspected active member. Groups associated with DDoS, defacement, and data leak operations aligned with Russian geopolitical interests.
- **Accenture Breach Threat Actor (Unnamed)**: Claimed theft of 35 GB of source code and data; offering for sale on underground forums. Accenture confirmed breach; attribution not publicly disclosed.
- **Offensive Cybersecurity Startup (Felon-Run)**: Startup actively soliciting zero-day vulnerabilities in popular software; operated by convicted felons and far-right conspiracy theorists. Represents a novel supply-side threat to vulnerability markets.
- **GitLost / Noma Security Researchers**: Disclosed GitHub Agentic Workflow data leakage flaw; demonstrated unauthenticated exfiltration via crafted public issues.

## Source Attribution

- **3 Ways AI Powers Service Desk Attacks and How to Prevent Them**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/3-ways-ai-powers-service-desk-attacks-and-how-to-prevent-them/
- **New Ghost Phishing Wave Is Breaking Traditional Email Security**: The Hacker News - https://thehackernews.com/2026/07/new-ghost-phishing-wave-is-breaking.html
- **SCMBANKER Malware Uses ClickFix Lures to Target Mexican Banking Users**: The Hacker News - https://thehackernews.com/2026/07/scmbanker-malware-uses-clickfix-lures.html
- **Felons, Fraudsters Flog Offensive Cybersecurity Startup**: Krebs on Security - https://krebsonsecurity.com/2026/07/felons-fraudsters-flog-offensive-cybersecurity-startup/
- **DuckDuckGo browser now blocks YouTube video ads**: Bleeping Computer - https://www.bleepingcomputer.com/news/software/duckduckgo-browser-now-blocks-youtube-video-ads/
- **GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures**: The Hacker News - https://thehackernews.com/2026/07/github-verified-commits-can-be.html
- **The Verification Step Is the New ATO Battleground in 2026**: The Hacker News - https://thehackernews.com/2026/07/the-verification-step-is-new-ato.html
- **Telco giant KDDI says data breach affects over 12 million people**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/japanese-telecom-giant-kddi-says-data-breach-affects-12-million-people/
- **GitHub Copilot Refuses Harmful Requests in Chat, Then Writes Them in Code**: The Hacker News - https://thehackernews.com/2026/07/github-copilot-refuses-harmful-requests.html
- **CISA orders feds to prioritize patching Langflow auth bypass flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/
- **China-Linked UAT-7810 Expands ORB Network With New LONGLEASH Malware**: The Hacker News - https://thehackernews.com/2026/07/china-linked-uat-7810-expands-orb.html
- **Ubiquiti warns of new max severity UniFi OS vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ubiquiti-warns-of-new-max-severity-unifi-os-vulnerability/
- **State IDs for AI Agents: Will Estonia Set a Precedent?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/state-ids-ai-agents-estonia
- **CISA orders feds to patch max severity ColdFusion flaw by Friday**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-coldfusion-flaw-by-friday/
- **15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros**: The Hacker News - https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html
- **CISA Adds 4 Actively Exploited Adobe, Joomla, and Langflow Flaws to KEV**: The Hacker News - https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html
- **Accenture confirms breach after hacker offers stolen data for sale**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/accenture-confirms-breach-after-hacker-offers-stolen-data-for-sale/
- **Big Brand Jobs Scam Targets Marketing Pros' Google Accounts**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/big-brand-jobs-scam-marketing-pros-google-accounts
- **Dialogflow CX 'Rogue Agent' Flaw Enabled AI Chatbot Data Theft**: Dark Reading - https://www.darkreading.com/application-security/dialogflow-cx-rogue-agent-flaw-enabled-ai-chatbot-data-theft
- **Chinese hackers develop LONGLEASH malware to expand ORB network**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/chinese-hackers-develop-longleash-malware-to-expand-orb-network/
- **Hidden backdoor in Tenda router firmware grants admin access**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hidden-backdoor-in-tenda-router-firmware-grants-admin-access/
- **RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service**: The Hacker News - https://thehackernews.com/2026/07/redwing-maas-packages-android-bank.html
- **Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots**: The Hacker News - https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html
- **'GitLost' Flaw Leaks Private Data From GitHub's Agentic Workflows**: Dark Reading - https://www.darkreading.com/cyber-risk/gitlost-leaks-private-data-github-agentic-workflows
- **Spain arrests suspected member of pro-Russian hacktivist groups**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/spain-arrests-suspected-member-of-pro-russian-hacktivist-groups/
- **DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts**: The Hacker News - https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html
- **Public GitHub Issue Could Trick GitHub Agentic Workflows Into Leaking Private Repo Data**: The Hacker News - https://thehackernews.com/2026/07/public-github-issue-could-trick-github.html
- **The GitHub Actions Attack Pattern Your CI Security Scanners Miss**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-github-actions-attack-pattern-your-ci-security-scanners-miss/
- **Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker**: The Hacker News - https://thehackernews.com/2026/07/court-filing-reveals-windows-device-id.html
- **Writer AI Flaw Could Let Agent Previews Leak Session Tokens Across Tenants**: The Hacker News - https://thehackernews.com/2026/07/writer-ai-flaw-could-let-agent-previews.html
