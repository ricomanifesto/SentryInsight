# Exploitation Report

## Executive Summary

Multiple high-impact exploitation campaigns are actively targeting critical infrastructure, enterprise platforms, and end-users across diverse sectors. A pre-authentication remote code execution flaw in Progress Kemp LoadMaster is under active exploitation, while over 900 Oracle E-Business Suite instances face ongoing attacks leveraging a critical vulnerability. Simultaneously, a massive password-spraying campaign against Microsoft 365 and Azure CLI has generated more than 81 million login attempts, compromising at least 78 accounts. These infrastructure-level attacks are complemented by sophisticated social engineering operations abusing legitimate services including ScreenConnect, Blogger, and SEO-poisoned software download sites to deploy AsyncRAT, PureLogs stealer, and the Ousaban banking trojan.

Threat actors are rapidly adopting AI-driven techniques to expand their attack surface. The emergence of "Phantom Squatting" sees operators registering domains hallucinated by LLMs to host phishing and malware payloads, while novel prompt injection methods—including "BioShocking" and "Agentjacking"—demonstrate the ability to manipulate AI-powered browsers and coding agents into bypassing safety controls. A China-linked group has compromised at least ten organizations in Southeast Asia, including two state-owned entities, deploying a previously undocumented backdoor. Meanwhile, analysis of 3,000 live ClickFix payloads reveals an API-driven malware delivery backend scaling social engineering operations.

The convergence of infrastructure exploitation, credential attacks, AI-enabled supply chain abuse, and legitimate-service misuse signals a significant escalation in both volume and sophistication. Organizations must prioritize patching of exposed load balancers and ERP instances, enforce phishing-resistant authentication for cloud identities, and implement controls to detect and block AI-generated attack infrastructure.

## Active Exploitation Details

### Progress Kemp LoadMaster Pre-Auth RCE
- **Description**: A critical pre-authentication remote code execution vulnerability affecting Progress Kemp LoadMaster load balancing appliances. The flaw allows unauthenticated attackers to execute arbitrary code on vulnerable systems.
- **Impact**: Full system compromise of load balancers, LoadMaster appliances, potential lateral movement into internal networks, and disruption of critical application delivery infrastructure.
- **Status**: Active exploitation attempts observed by eSentire's Threat Response Unit (TRU). Advisory issued warning of ongoing attacks.
- **CVE ID**: Not specified in source article

### Oracle E-Business Suite Critical Vulnerability
- **Description**: A critical security flaw in Oracle E-Business Suite (EBS) enabling remote exploitation of exposed instances.
- **Impact**: Compromise of ERP systems containing financial, HR, and supply chain data. Over 900 instances found exposed online amid ongoing attacks.
- **Status**: Ongoing attacks against exposed instances. Organizations with internet-facing EBS deployments at immediate risk.
- **CVE ID**: Not specified in source article

### ScreenConnect Abuse for AsyncRAT Deployment
- **Description**: Unknown threat actors leveraging the legitimate ScreenConnect (ConnectWise) remote access tool through SEO-poisoned software download sites to deploy AsyncRAT payloads.
- **Impact**: Full remote access to victim systems, credential theft, lateral movement, and persistent foothold via legitimate RMM tool abuse.
- **Status**: Described as a "massive, multi-domain, multi-language" campaign by Kaspersky. Active across numerous compromised software distribution sites.
- **CVE ID**: Not specified in source article

### Microsoft 365 / Azure CLI Password Spray Campaign
- **Description**: Large-scale automated password spraying targeting Microsoft 365 environments and Azure command-line interface (CLI) authentication endpoints.
- **Impact**: At least 78 Microsoft accounts compromised from over 81 million login attempts over a two-week period. Credential theft, data access, and potential Business Email Compromise (BEC) enablement.
- **Status**: Massive, ongoing, automated campaign. Researchers warn of continued activity against cloud identities.
- **CVE ID**: Not specified in source article

### VEIL#DROP Malware Chain (PureLogs Stealer)
- **Description**: Multi-stage malware delivery chain using social engineering and compromised Blogger pages to deliver the PureLogs information stealer.
- **Impact**: Exfiltration of browser credentials, cryptocurrency wallets, system information, and sensitive files. Abuse of Google's Blogger platform for payload hosting evades reputation-based defenses.
- **Status**: Active campaign identified by researchers. Blogger platform abused as legitimate content delivery mechanism.
- **CVE ID**: Not specified in source article

### Ousaban Banking Trojan Campaign
- **Description**: Brazilian-origin banking trojan targeting Windows users of financial institutions in Spain and Portugal via phishing PDF lures.
- **Impact**: Financial fraud, credential theft for Iberian banking portals, webinject capabilities for transaction manipulation, and persistent system access.
- **Status**: Campaign identified by Fortinet FortiGuard Labs in May 2026. Active targeting of Spanish and Portuguese banking customers.
- **CVE ID**: Not specified in source article

### AI-Generated Browser Ransomware
- **Description**: Novel ransomware artifact generated using DeepSeek AI that abuses Chromium APIs on Windows and Android to achieve browser-based encryption and data theft.
- **Impact**: File encryption, data exfiltration, and system compromise via browser sandbox escape. Cross-platform capability across desktop and mobile Chromium-based browsers.
- **Status**: Proof-of-concept or early-stage malware demonstrating AI-assisted novel attack path construction.
- **CVE ID**: Not specified in source article

### China-Linked Group Southeast Asia Campaign
- **Description**: State-nexus threat group compromising critical infrastructure organizations across Southeast Asia, deploying a previously unknown backdoor.
- **Impact**: At least 10 organizations compromised including two state-owned entities. Persistent access to critical systems, espionage positioning, and potential disruptive capability.
- **Status**: Active campaign with confirmed intrusions. New backdoor indicates continued tooling development.
- **CVE ID**: Not specified in source article

### ClickFix API-Driven Malware Delivery
- **Description**: Social engineering technique ("ClickFix") tricking users into executing malicious commands manually, now backed by API-driven command-and-control infrastructure delivering payloads at scale.
- **Impact**: Bypasses traditional email and web filters by using legitimate user interaction. Analysis of 3,000 live payloads reveals automated backend operations.
- **Status**: Active and growing campaign with industrialized delivery infrastructure.
- **CVE ID**: Not specified in source article

### Phantom Squatting (AI-Hallucinated Domain Abuse)
- **Description**: Attackers registering domain names hallucinated by large language models when referencing legitimate brands, then hosting phishing pages and malware on these typosquatted domains.
- **Impact**: Difficult-to-detect supply chain attack vector exploiting developer and user trust in AI-generated code and references. Credential harvesting and malware delivery.
- **Status**: Emerging threat vector with active domain registrations and malicious hosting observed.
- **CVE ID**: Not specified in source article

## Affected Systems and Products

- **Progress Kemp LoadMaster**: Load balancing appliances (all versions prior to patched release) — **Platform**: On-premises and virtual appliance deployments exposed to management interfaces
- **Oracle E-Business Suite**: ERP platform instances (specific vulnerable modules not detailed) — **Platform**: Internet-facing EBS deployments across enterprise environments
- **ScreenConnect (ConnectWise)**: Remote monitoring and management software — **Platform**: Windows, Linux, macOS endpoints where agent is installed via malicious download
- **Microsoft 365 / Azure CLI**: Cloud identity and management platforms — **Platform**: Entra ID (Azure AD) tenants with accounts lacking phishing-resistant MFA
- **Blogger (Google)**: Content hosting platform abused for payload delivery — **Platform**: Web-based, accessible globally; PureLogs stealer targets Windows endpoints
- **Windows**: Primary target for AsyncRAT, PureLogs, Ousaban, and browser ransomware — **Platform**: Windows 10/11 endpoints in enterprise and consumer environments
- **Android**: Target for AI-generated browser ransomware via Chromium API abuse — **Platform**: Android devices running Chromium-based browsers
- **Chromium-Based Browsers**: Chrome, Edge, Brave, and derivatives — **Platform**: Windows, Android, and potentially Linux/macOS via API abuse vectors
- **Cursor AI Code Editor**: Versions vulnerable to prompt injection sandbox escape — **Platform**: Windows, macOS, Linux developer workstations
- **NetScaler ADC / NetScaler Gateway**: Patched for file read and DoS flaws — **Platform**: On-premises and cloud ADC appliances (exploitation not reported active)
- **Adobe ColdFusion / Campaign Classic**: Patched for CVSS 10.0 flaws — **Platform**: Web application servers and marketing automation platforms (exploitation not reported active)
- **Homeland Security Information Network (HSIN)**: Federal information-sharing platform — **Platform**: DHS-operated sensitive but unclassified collaboration environment

## Attack Vectors and Techniques

- **SEO Poisoning**: Malicious actors compromise or create software download sites optimized for search rankings, delivering trojanized installers that deploy ScreenConnect and AsyncRAT — **Vector**: Web search → malicious download → RMM agent installation → C2 establishment
- **Password Spraying**: Automated, low-volume credential guessing against Microsoft 365 and Azure CLI endpoints across thousands of tenants — **Vector**: Auth endpoints (login.microsoftonline.com, Azure CLI token requests) using common password lists
- **Legitimate Service Abuse (ScreenConnect)**: Valid RMM tool deployed via social engineering to gain persistent remote access — **Vector**: User executes installer → ScreenConnect service registers with attacker-controlled relay → interactive session
- **Legitimate Service Abuse (Blogger)**: Google's trusted Blogger platform used to host malware staging pages and payloads — **Vector**: Social engineering link → Blogger page → PureLogs download/execution
- **Phishing with PDF Lures**: Banking trojan delivered via deceptive PDF documents mimicking financial communications — **Vector**: Email/web → PDF open → embedded exploit or social engineering → Ousaban installation
- **Prompt Injection Sandbox Escape**: Malicious prompts crafted to bypass AI safety controls and execute arbitrary commands — **Vector**: Cursor editor chat interface, AI browser chat, coding agent issue trackers
- **AI-Hallucinated Domain Registration (Phantom Squatting)**: Domains invented by LLMs registered by attackers before legitimate entities claim them — **Vector**: Developer/user follows AI-suggested import/reference → resolves to attacker-controlled server → payload delivery
- **ClickFix Social Engineering**: Fake verification pages (CAPTCHA, "prove you're human") instruct victims to run PowerShell commands — **Vector**: Compromised/typosquatted site → fake verification → clipboard injection → user executes → API-driven payload fetch
- **API-Driven Malware Delivery Backend**: Automated infrastructure serving unique payloads per victim interaction — **Vector**: ClickFix execution → API call → tailored payload delivery → execution
- **Pre-Auth RCE Exploitation**: Unauthenticated code execution on exposed load balancer management interfaces — **Vector**: Internet-accessible management port → exploit payload → root-level code execution
- **ERP Vulnerability Exploitation**: Critical flaw in Oracle EBS exploited for unauthorized access — **Vector**: Internet-facing EBS portal → exploit → application/server compromise
- **Backdoor Deployment (China-Linked Group)**: Custom malware implanted for persistent access to critical infrastructure — **Vector**: Initial access (unspecified) → backdoor installation → C2 communications
- **Chromium API Abuse**: Malicious use of browser extension/API capabilities for ransomware encryption — **Vector**: Malicious extension or compromised site → browser API calls → file system encryption/data theft

## Threat Actor Activities

- **Unknown Operators (ScreenConnect/AsyncRAT Campaign)**: Conducting massive, multi-language SEO poisoning operation distributing AsyncRAT via trojanized ScreenConnect installers. Broad targeting across geographies and languages suggests opportunistic, high-volume approach.
- **Unknown Operators (HSIN Breach)**: Successfully infiltrated the Homeland Security Information Network, a sensitive federal information-sharing platform. Attribution not disclosed; investigation ongoing by DHS.
- **Unknown Operators (VEIL#DROP/PureLogs)**: Operating multi-stage delivery chain leveraging Blogger for hosting. PureLogs stealer indicates financially motivated data theft operation.
- **Unknown Operators (Microsoft 365/Azure Password Spray)**: Executing industrial-scale credential attack (81M+ attempts) with focus on Azure CLI authentication. Compromise of 78+ accounts suggests downstream BEC and data theft objectives.
- **Ousaban Banking Trojan Operators**: Brazilian threat group targeting Iberian Peninsula financial sector. Campaign active since at least May 2026 with localized lures for Spanish and Portuguese banks.
- **China-Linked APT Group**: Conducting espionage-focused intrusion campaign against Southeast Asian critical infrastructure. Minimum 10 organizations compromised including 2 state-owned entities. Deployment of novel backdoor indicates dedicated tooling development.
- **Unknown Operators (ClickFix Infrastructure)**: Running API-backed social engineering campaign at scale (3,000+ live payloads analyzed). Industrialized backend suggests organized criminal operation.
- **Unknown Operators (Phantom Squatting)**: Registering AI-hallucinated domains for phishing and malware hosting. Opportunistic exploitation of LLM supply chain trust.
- **Unknown Operators (Progress Kemp LoadMaster Exploitation)**: Actively scanning for and exploiting pre-auth RCE on exposed LoadMaster appliances. eSentire TRU tracking exploitation attempts.
- **Unknown Operators (Oracle EBS Attacks)**: Targeting 900+ exposed EBS instances with critical vulnerability exploit. Ongoing campaign against enterprise ERP systems.
- **AI-Assisted Malware Author (DeepSeek-Generated Ransomware)**: Demonstrated novel browser-based ransomware construction using AI coding assistance. Cross-platform Chromium API abuse technique.

## Source Attribution

- **SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT**: The Hacker News - https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html
- **DHS confirms hackers breached HSIN info-sharing platform**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/
- **VEIL#DROP Malware Chain Uses Blogger Platform to Deliver PureLogs Stealer**: The Hacker News - https://thehackernews.com/2026/07/veildrop-malware-chain-uses-blogger.html
- **Webinar: Why traditional email security is no longer enough**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/webinar-why-traditional-email-security-is-no-longer-enough/
- **Hackers target Microsoft 365 accounts with 81 million login attempts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-target-microsoft-365-accounts-with-81-million-login-attempts/
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
