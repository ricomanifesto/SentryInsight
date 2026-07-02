# Exploitation Report

## Executive Summary

A significant escalation in credential theft and initial access operations dominates the current threat landscape, with the FortiBleed campaign demonstrating how mass credential harvesting directly fuels ransomware operations. The stolen Fortinet VPN credentials have been linked to both INC and Lynx ransomware groups, indicating a mature supply chain where access brokers monetize compromised infrastructure through established ransomware affiliates. Simultaneously, a massive password-spraying campaign targeting Microsoft 365 and Azure CLI environments generated over 81 million login attempts, compromising at least 78 accounts and highlighting the persistent effectiveness of low-sophistication, high-volume credential attacks against cloud identities.

The malware delivery ecosystem continues to evolve toward social engineering dominance, with ClickFix establishing itself as the primary malware delivery mechanism through API-driven command distribution. Attackers are increasingly weaponizing legitimate platforms—including GitHub for trojanized proof-of-concept exploits targeting researchers, Blogger pages for multi-stage malware chains, and SEO-poisoned software download sites abusing ScreenConnect to deploy AsyncRAT. These campaigns demonstrate a shift toward living-off-trusted-sites techniques that bypass traditional reputation-based defenses. Meanwhile, the Scattered Spider group faces legal disruption with the extradition of a key operator, though the broader ecosystem of SIM-swapping and SaaS-targeted intrusions remains active.

Critical infrastructure and enterprise software remain under active exploitation pressure. Over 900 Oracle E-Business Suite instances are exposed to ongoing attacks leveraging a critical flaw, while the Progress Kemp LoadMaster pre-authentication RCE vulnerability faces active exploitation attempts in the wild. An unpatched Argo CD repo-server flaw threatens Kubernetes cluster takeover, and Adobe has released emergency patches for seven maximum-severity (CVSS 10.0) vulnerabilities in ColdFusion and Campaign Classic. Emerging attack vectors include AI-hallucinated domain registration (Phantom Squatting), prompt injection escapes in AI coding assistants, and browser-based ransomware abusing Chromium APIs—signaling a new frontier of AI-enabled supply chain and client-side exploitation.

## Active Exploitation Details

### FortiBleed Credential Theft Campaign
- **Description**: A massive credential harvesting operation targeting Fortinet VPN appliances, resulting in large-scale theft of valid corporate credentials. The campaign systematically collects authentication data from exposed or vulnerable FortiGate devices.
- **Impact**: Stolen credentials provide initial access for network intrusion, lateral movement, and ransomware deployment. Valid credentials bypass perimeter defenses and enable persistent access to corporate networks.
- **Status**: Actively exploited; credentials being monetized through ransomware affiliate networks. Fortinet has issued guidance on securing VPN appliances and rotating compromised credentials.

### Microsoft 365 / Azure CLI Password Spray Campaign
- **Description**: An aggressive, automated password-spraying campaign targeting Microsoft 365 environments and Azure command-line interface endpoints. The operation generated over 81 million login attempts across a two-week period.
- **Impact**: At least 78 Microsoft accounts compromised, providing attackers with footholds in cloud environments for data exfiltration, business email compromise, and further lateral movement into Azure resources.
- **Status**: Ongoing, large-scale operation. Microsoft recommends enforcing MFA, conditional access policies, and monitoring for anomalous authentication patterns.

### Progress Kemp LoadMaster Pre-Auth RCE Exploitation
- **Description**: A critical pre-authentication remote code execution vulnerability in Progress Kemp LoadMaster load balancers. The flaw allows unauthenticated attackers to execute arbitrary code on the appliance.
- **Impact**: Full compromise of load balancer appliances, enabling traffic interception, credential harvesting, network pivoting, and persistence in critical infrastructure paths.
- **Status**: Active exploitation attempts observed in the wild by eSentire's Threat Response Unit. Patches available; Patch available; immediate application strongly advised.

### Oracle E-Business Suite Critical Flaw Exploitation
- **Description**: Ongoing attacks exploiting a critical security vulnerability in Oracle E-Business Suite (EBS) instances exposed to the internet. Over 900 instances have been identified as vulnerable and under active targeting.
- **Impact**: Potential full compromise of ERP systems containing financial, HR, and supply chain data. Attackers can achieve unauthorized data access, modification, and potential ransomware deployment.
- **Status**: Active exploitation ongoing. Oracle has released patches; exposed instances require immediate remediation and compromise assessment.

### Argo CD Repo-Server Unpatched Flaw
- **Description**: An unpatched vulnerability in the Argo CD repo-server component that allows unauthenticated attackers to execute code, provided they can reach the component. Argo CD is a widely used GitOps continuous delivery tool for Kubernetes.
- **Impact**: Complete takeover of Kubernetes clusters managed by Argo CD, including deployment manipulation, secret theft, supply chain poisoning, and cluster-wide persistence.
- **Status**: Unpatched as of reporting; active exploitation risk high for internet-exposed repo-server instances. Mitigation requires network segmentation and access restrictions until patch release.

### Adobe ColdFusion and Campaign Classic Maximum-Severity Flaws
- **Description**: Seven critical vulnerabilities (CVSS 10.0) affecting Adobe ColdFusion web application platform and Adobe Campaign Classic marketing automation platform. Flaws include deserialization, injection, and authentication bypass issues.
- **Impact**: Remote code execution, authentication bypass, and full server compromise without user interaction. ColdFusion and Campaign Classic are widely deployed in enterprise environments.
- **Status**: Patches released by Adobe; immediate deployment required. No confirmed exploitation in the wild at time of patch release, but high likelihood of rapid weaponization given severity.

### ChocoPoC Trojanized Proof-of-Concept Exploits
- **Description**: Multiple weaponized proof-of-concept exploits published on GitHub delivering a Python-based remote access trojan (ChocoPoC). The malware executes commands and steals sensitive data from researcher systems.
- **Impact**: Compromise of security researcher environments, theft of credentials, research data, and potential supply chain contamination if researchers integrate malicious code.
- **Status**: Active campaign targeting security community. Malicious repositories identified and reported; researchers advised to verify PoC sources and execute in isolated environments.

### VEIL#DROP Malware Chain via Blogger Platform
- **Description**: A multi-stage malware delivery chain leveraging Google's Blogger platform to host malicious content that delivers the PureLogs information stealer. The attack uses social engineering to lure victims to Blogger pages.
- **Impact**: Credential theft, browser data exfiltration, cryptocurrency wallet compromise, and system reconnaissance. Abuse of trusted Google infrastructure evades reputation-based blocking.
- **Status**: Active campaign; Blogger pages used as resilient, reputable hosting for payload delivery stages.

### SEO-Poisoned Software Sites Abusing ScreenConnect
- **Description**: Threat actors compromise software download rankings through SEO poisoning, directing victims to malicious sites that abuse the legitimate ScreenConnect remote access tool to deploy AsyncRAT.
- **Impact**: Full remote access to victim systems, persistent backdoor installation, credential theft, and lateral movement capabilities. Legitimate tool usage evades application allowlisting.
- **Status**: Active, "massive, multi-domain, multi-language" campaign per Kaspersky. ScreenConnect abuse represents living-off-the-land technique leveraging trusted remote administration software.

### Ousaban Banking Trojan Campaign
- **Description**: Brazilian banking trojan targeting Windows users of Spanish and Portuguese financial institutions. Delivery via phishing emails with fake PDF lures that execute malicious payloads.
- **Impact**: Financial credential theft, session hijacking, fraudulent transactions, and potential deployment of additional malware. Regionally focused but technically sophisticated.
- **Status**: Active campaign identified by FortiGuard Labs in May 2026; ongoing targeting of Iberian banking customers.

### AI-Generated Browser Ransomware
- **Description**: Novel ransomware artifact generated using DeepSeek AI that abuses Chromium browser APIs on Windows and Android to achieve file encryption and system compromise without traditional executable payloads.
- **Impact**: Cross-platform ransomware capability leveraging browser sandbox escapes and API abuse; demonstrates AI-accelerated malware development lowering barrier to entry.
- **Status**: Proof-of-concept / early deployment stage; represents emerging threat vector combining AI-generated code with browser capability abuse.

### Cursor AI Editor Prompt Injection Flaws
- **Description**: Two vulnerabilities in the Cursor AI code editor allowing prompt injection to escape the safety sandbox and execute arbitrary commands on the developer's machine. Triggered by ordinary-looking prompts.
- **Impact**: Full command execution on developer workstations, source code theft, supply chain compromise via malicious commits, and lateral movement into development environments.
- **Status**: Vulnerabilities disclosed; patch status unclear. High-risk for developers using AI-assisted coding tools with elevated permissions.

### Phantom Squatting AI-Hallucinated Domain Attacks
- **Description**: Attackers register domain names hallucinated by large language models when generating code or content references. These domains receive traffic from AI-generated code that references non-existent libraries or resources.
- **Impact**: Supply chain compromise via typosquatting of AI-invented names, phishing credential harvest, malware delivery to developers and automated systems trusting LLM outputs.
- **Status**: Emerging threat vector; domains actively registered and weaponized. Difficult to detect as domains appear legitimate in AI-generated contexts.

## Affected Systems and Products

- **Fortinet FortiGate VPN Appliances**: Credential theft targeting VPN authentication systems; all versions with exposed management interfaces or vulnerable configurations.
- **Microsoft 365 / Azure CLI / Entra ID**: Cloud identity platforms targeted by large-scale password spray campaigns; tenants with legacy authentication or without MFA enforcement.
- **Progress Kemp LoadMaster**: Load balancer appliances (physical, virtual, cloud) running vulnerable firmware versions; critical infrastructure component in many enterprise networks.
- **Oracle E-Business Suite**: ERP platform instances exposed to internet; versions lacking critical security patches for the actively exploited flaw.
- **Argo CD**: Kubernetes GitOps deployments with repo-server component accessible to untrusted networks; all versions prior to patched release.
- **Adobe ColdFusion**: Web application server versions 2021, 2023, and earlier; enterprise deployments hosting custom applications.
- **Adobe Campaign Classic**: Marketing automation platform on-premise and hybrid deployments; versions prior to July 2026 security update.
- **GitHub / Public Code Repositories**: Platform hosting trojanized proof-of-concept exploits; researchers and automated systems consuming unverified code.
- **Google Blogger Platform**: Legitimate blogging service abused for multi-stage malware hosting; content delivery infrastructure with high reputation scores.
- **ScreenConnect / ConnectWise Control**: Legitimate remote access software abused as payload delivery mechanism; endpoints running ScreenConnect client.
- **Windows / Android (Chromium-based Browsers)**: Operating systems and browsers vulnerable to API abuse by AI-generated ransomware; Chrome, Edge, Brave, and other Chromium derivatives.
- **Cursor AI Code Editor**: AI-assisted development environment; versions with sandbox escape vulnerabilities affecting developers with local execution permissions.
- **Spanish/Portuguese Banking Infrastructure**: Financial institution customers targeted by Ousaban trojan; Windows endpoints with outdated protections.

## Attack Vectors and Techniques

- **Credential Theft & Password Spraying**: Large-scale automated authentication attempts against cloud identity providers (Microsoft 365, Azure CLI) using common password lists; low-and-slow techniques to evade lockout policies.
- **VPN Credential Harvesting**: Targeted exploitation of Fortinet VPN appliances to extract valid corporate credentials for resale to ransomware operators and initial access brokers.
- **Pre-Authentication Remote Code Execution**: Exploitation of unauthenticated RCE flaws in internet-facing appliances (Kemp LoadMaster) and applications (Argo CD repo-server) for immediate foothold.
- **ERP/Business Application Exploitation**: Targeting of critical business systems (Oracle E-Business) exposed to internet with unpatched critical vulnerabilities.
- **Trojanized Security Tooling**: Weaponization of proof-of-concept exploits on GitHub targeting security researchers; supply chain attack on vulnerability research workflow.
- **Living-Off-Trusted-Sites**: Abuse of legitimate platforms (Blogger, Google infrastructure, ScreenConnect) for payload hosting, command-and-control, and remote access—evading reputation and allowlist controls.
- **SEO Poisoning & Malvertising**: Manipulation of search rankings for software downloads to deliver malware via legitimate remote administration tools (ScreenConnect → AsyncRAT).
- **Social Engineering with OS Fingerprinting**: Phishing campaigns that auto-adapt payloads based on victim User-Agent strings; device-specific lure delivery increasing compromise rates.
- **ClickFix Social Engineering**: "Prove you're human" fake verification pages tricking users into executing malicious PowerShell commands; API-driven command distribution at scale.
- **AI-Hallucinated Domain Registration (Phantom Squatting)**: Registration of domains invented by LLMs in code/output; pre-positioned for supply chain and developer targeting.
- **Prompt Injection Sandbox Escape**: Malicious prompts crafted to break AI assistant safety boundaries and achieve code execution on host systems (Cursor editor).
- **Browser API Abuse**: Exploitation of Chromium extension and API capabilities for cross-platform ransomware execution without traditional binary payloads.
- **Banking Trojan Web Injects & Overlays**: Region-specific financial malware (Ousaban) using fake PDF lures, credential phishing, and session manipulation for fraud.

## Threat Actor Activities

- **Lynx Ransomware Group**: Consuming FortiBleed-harvested credentials for initial access in ransomware operations; affiliated with INC ransomware operation indicating shared access broker ecosystem.
- **INC Ransomware Operation**: Linked to FortiBleed credential theft campaign; utilizes stolen VPN credentials for network intrusion and extortion.
- **Scattered Spider (UNC3944/0ktapus)**: Financially motivated threat group specializing in SIM swapping, SaaS credential theft, and social engineering; 19-year-old operator extradited from Finland to face U.S. charges (conspiracy, computer intrusion, fraud).
- **ChocoPoC Operators**: Unknown threat actor(s) publishing weaponized PoC exploits on GitHub targeting security researchers; Python-based RAT development suggests technical capability.
- **VEIL#DROP Operators**: Unknown group leveraging Blogger platform for multi-stage PureLogs stealer delivery; sophisticated social engineering and trusted-infrastructure abuse.
- **SEO Poisoning / AsyncRAT Campaign Operators**: Unknown threat actors running "massive, multi-domain, multi-language" campaign (per Kaspersky) abusing ScreenConnect; likely initial access brokers or financially motivated group.
- **Ousaban Banking Trojan Operators**: Brazilian cybercrime group targeting Iberian (Spain/Portugal) financial institutions; regionally focused with Portuguese/Spanish language capabilities.
- **Phantom Squatting Registrants**: Opportunistic actors monitoring LLM outputs for hallucinated domains; registering and weaponizing for supply chain and phishing attacks.
- **AI-Generated Malware Authors**: Individuals or groups leveraging LLMs (DeepSeek) to generate novel attack code; lowering technical barrier for browser-based ransomware development.

## Source Attribution

- **FortiBleed credential-theft campaign linked to Lynx ransomware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fortibleed-credential-theft-campaign-linked-to-lynx-ransomware/
- **Kubota says hackers had month-long access to network systems**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/kubota-says-hackers-had-month-long-access-to-network-systems/
- **Crafty Phishing Campaigns Auto-Adapt to Victim's Device, OS**: Dark Reading - https://www.darkreading.com/application-security/phishing-campaigns-auto-adapt-victims-device-os
- **New ChocoPoC malware targets researchers via trojanized PoC exploits**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-chocopoc-malware-targets-researchers-via-trojanized-poc-exploits/
- **And the Winner in Dominant Malware Delivery? ClickFix**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/winner-dominant-malware-delivery-clickfix
- **Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters**: The Hacker News - https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html
- **19-Year-Old Scattered Spider Suspect Extradited to Face U.S. Hacking Charges**: The Hacker News - https://thehackernews.com/2026/07/19-year-old-scattered-spider-suspect.html
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
