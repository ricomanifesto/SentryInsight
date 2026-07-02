# Exploitation Report

## Executive Summary

A surge in active exploitation activity spans multiple vectors, from critical infrastructure flaws facing active attacks to large-scale credential campaigns and novel AI-driven delivery chains. The Progress Kemp LoadMaster pre-authentication RCE is under active exploitation attempts, while over 900 Oracle E-Business Suite instances remain exposed to ongoing attacks leveraging a critical flaw. Simultaneously, an unpatched Argo CD repo-server vulnerability threatens Kubernetes cluster takeover, and a massive Azure CLI password-spray operation has generated over 81 million login attempts, compromising at least 78 accounts. These infrastructure-targeted campaigns coincide with confirmed breaches at Kubota, where actors maintained month-long network access, and the Department of Homeland Security's HSIN information-sharing platform.

The malware delivery landscape continues to evolve rapidly. ClickFix has become the dominant social engineering technique for malware deployment, now backed by API-driven infrastructure managing thousands of live payloads. Threat actors are weaponizing trojanized proof-of-concept exploits on GitHub to target researchers with the ChocoPoC RAT, while SEO-poisoned software sites abuse ScreenConnect to deploy AsyncRAT in a massive, multi-language campaign. New delivery chains such as VEIL#DROP leverage the Blogger platform to drop the PureLogs stealer, and the Ousaban banking trojan targets Iberian users through fake PDF lures. Meanwhile, AI-generated threats are materializing: Phantom Squatting campaigns register LLM-hallucinated domains for phishing, and DeepSeek-generated browser ransomware abuses Chromium APIs on Windows and Android.

Threat actor accountability advanced with the extradition of a Scattered Spider suspect from Finland to face U.S. charges of conspiracy, computer intrusion, and fraud. Vendors are responding to critical flaw disclosures: Adobe patched seven CVSS 10.0 vulnerabilities in ColdFusion and Campaign Classic, Citrix addressed six NetScaler flaws enabling file read and denial-of-service, and Cursor's AI code editor faces two prompt-injection flaws that escape the sandbox. Across the board, exploitation is accelerating across identity, supply chain, and infrastructure layers, demanding immediate patching, phishing-resistant authentication, and supply chain verification.

## Active Exploitation Details

### Progress Kemp LoadMaster Pre-Auth RCE
- **Description**: A critical pre-authentication remote code execution flaw in Progress Kemp LoadMaster load balancers.
- **Impact**: Unauthenticated attackers can achieve remote code execution on affected appliances, potentially leading to full device compromise, traffic interception, and lateral movement.
- **Status**: Actively exploited in the wild; eSentire's Threat Response Unit has observed active exploitation attempts. Patch availability should be verified with Progress.

### Oracle E-Business Suite Critical Flaw Exploitation
- **Description**: A critical security flaw in Oracle E-Business Suite (EBS) being actively exploited against internet-exposed instances.
- **Impact**: Attackers can compromise over 900 identified exposed EBS instances, potentially accessing sensitive ERP data, financial records, and business processes.
- **Status**: Ongoing attacks against exposed instances; organizations running EBS should apply patches immediately and restrict network exposure.

### Argo CD Repo-Server Unpatched Flaw
- **Description**: An unpatched vulnerability in the Argo CD repo-server component that allows unauthenticated code execution when the component is reachable.
- **Impact**: Attackers who can reach the repo-server can run arbitrary code, leading to full Kubernetes cluster takeover, supply chain compromise, and deployment manipulation.
- **Status**: Unpatched as of reporting; mitigation requires network segmentation to restrict repo-server access until a fix is released.

### Azure CLI / Microsoft 365 Password Spray Campaign
- **Description**: A massive, automated password-spraying campaign targeting Microsoft Azure CLI and Microsoft 365 accounts.
- **Impact**: Over 81 million login attempts in a two-week period, with at least 78 accounts compromised, enabling access to cloud resources, email, and associated services.
- **Status**: Ongoing; enforcement of phishing-resistant MFA (FIDO2, certificate-based) and conditional access policies is critical.

### Kubota Network Intrusion
- **Description**: Hackers maintained unauthorized access to Kubota North America Corporation network systems for more than a month.
- **Impact**: Potential exposure of corporate data, intellectual property, and operational systems during the extended dwell time.
- **Status**: Incident disclosed; investigation and remediation underway.

### DHS HSIN Platform Breach
- **Description**: Cyberattack compromising the Homeland Security Information Network (HSIN), a sensitive information-sharing platform used by federal, state, and local partners.
- **Impact**: Potential exposure of law enforcement and homeland security information shared across government entities.
- **Status**: DHS investigating; platform access and integrity under review.

### ClickFix Social Engineering Dominance
- **Description**: ClickFix has become the dominant malware delivery technique, tricking users into executing malicious commands via fake "verify you're human" pages.
- **Impact**: High compromise rates across diverse malware families; researcher analysis of 3,000 live payloads reveals API-driven command-and-control infrastructure.
- **Status**: Actively used in widespread campaigns; user education and application control (e.g., PowerShell constraints) are key mitigations.

### ChocoPoC Trojanized PoC Exploits
- **Description**: Weaponized proof-of-concept exploits on GitHub delivering a Python-based remote access trojan (ChocoPoC) targeting security researchers.
- **Impact**: Researchers executing PoC code gain a persistent RAT capable of command execution and sensitive data theft.
- **Status**: Active supply chain attack on GitHub; verification of PoC authenticity and execution in isolated environments is essential.

### SEO-Poisoned ScreenConnect / AsyncRAT Campaign
- **Description**: Unknown threat actors leverage SEO-poisoned software download sites to deliver ScreenConnect installers that deploy AsyncRAT.
- **Impact**: Large-scale, multi-domain, multi-language campaign delivering a capable remote access trojan with keylogging, credential theft, and remote control.
- **Status**: Active; block unauthorized remote monitoring tools and monitor for ScreenConnect installations.

### VEIL#DROP Blogger / PureLogs Chain
- **Description**: Multi-stage malware delivery chain using Blogger pages for payload staging, ultimately dropping the PureLogs information stealer.
- **Impact**: Credential harvesting, browser data exfiltration, cryptocurrency wallet theft, and system profiling via a stealthy, platform-abusing chain.
- **Status**: Active; web filtering and behavioral endpoint detection can interrupt the delivery stages.

### Ousaban Banking Trojan Campaign
- **Description**: Brazilian banking trojan targeting Windows users of Spanish and Portuguese banks via phishing emails with fake PDF lures.
- **Impact**: Financial credential theft, transaction manipulation, and potential ransomware deployment in Iberian banking sector.
- **Status**: Active since at least May 2026; email filtering and user awareness for PDF-based lures recommended.

### AI-Generated Browser Ransomware (Chromium API Abuse)
- **Description**: Malware generated using DeepSeek that combines novel browser-malware concepts with real Chromium capabilities to encrypt files on Windows and Android.
- **Impact**: Cross-platform ransomware leveraging legitimate browser APIs for file system access, evading traditional binary-based detection.
- **Status**: Emerging; monitor for abnormal Chromium/Electron app behavior and enforce least-privilege browser policies.

### Phantom Squatting (AI-Hallucinated Domains)
- **Description**: Attackers register domains hallucinated by LLMs for legitimate brands, then host phishing pages or malware to capture mistyped or AI-referred traffic.
- **Impact**: Difficult-to-detect supply chain and phishing vector exploiting trust in AI-generated references and brand familiarity.
- **Status**: Emerging; domain monitoring for brand variants and secure DNS filtering advised.

### Cursor AI Editor Prompt Injection Flaws
- **Description**: Two flaws in the Cursor AI code editor allow prompt injection to escape the safety sandbox and execute arbitrary commands on the developer's machine.
- **Impact**: Full command execution in the developer environment without user interaction beyond viewing a malicious prompt, leading to source code theft, supply chain poisoning, or system compromise.
- **Status**: Unpatched as of reporting; avoid processing untrusted code snippets or prompts in Cursor until fixes are released.

### Adobe ColdFusion and Campaign Classic Critical Flaws
- **Description**: Adobe released patches for seven maximum-severity (CVSS 10.0) vulnerabilities across ColdFusion and Campaign Classic platforms.
- **Impact**: Remote code execution, authentication bypass, and data exfiltration in widely deployed web application and marketing automation systems.
- **Status**: Patches available; immediate application is critical given maximum severity.

### Citrix NetScaler ADC/Gateway Flaws
- **Description**: Citrix patched six vulnerabilities in NetScaler ADC and NetScaler Gateway enabling file read and denial-of-service attacks.
- **Impact**: Unauthenticated attackers can read arbitrary files (potentially sensitive configuration, certificates, keys) or cause service disruption.
- **Status**: Patches released; apply updates to all exposed NetScaler appliances.

## Affected Systems and Products

- **Progress Kemp LoadMaster**: Load balancer appliances (pre-auth RCE); all versions prior to patched release
- **Oracle E-Business Suite (EBS)**: ERP platform; internet-exposed instances across versions with unpatched critical flaw
- **Argo CD**: Kubernetes GitOps continuous delivery tool; repo-server component in all current versions (unpatched)
- **Microsoft Azure CLI / Microsoft 365**: Cloud identity and productivity suite; tenants with legacy authentication enabled
- **Kubota North America Corporate Network**: Internal network infrastructure; unspecified systems accessed for month-long period
- **DHS Homeland Security Information Network (HSIN)**: Federal information-sharing platform; sensitive government user base
- **ScreenConnect (ConnectWise Control)**: Remote monitoring and management tool; abused as delivery vector for AsyncRAT
- **Blogger (Google)**: Blog publishing platform; abused for payload staging in VEIL#DROP chain
- **Windows 10/11**: Target platform for Ousaban banking trojan, AI-generated browser ransomware, and ChocoPoC RAT
- **Android**: Target platform for AI-generated browser ransomware abusing Chromium APIs
- **Adobe ColdFusion**: Web application development platform (2021, 2023 releases); seven CVSS 10.0 flaws patched
- **Adobe Campaign Classic**: Marketing automation platform (v7, v8); seven CVSS 10.0 flaws patched
- **Cursor AI Code Editor**: AI-assisted IDE (all current versions); two prompt-injection sandbox escape flaws
- **Citrix NetScaler ADC / NetScaler Gateway**: Application delivery controller and VPN gateway; six flaws patched (file read, DoS)
- **GitHub**: Code hosting platform; abused to host trojanized PoC exploits delivering ChocoPoC
- **Chromium-based Browsers (Chrome, Edge, Electron apps)**: Platform for AI-generated ransomware API abuse on Windows and Android

## Attack Vectors and Techniques

- **Password Spraying / Credential Stuffing**: Automated high-volume login attempts against Azure CLI and Microsoft 365 using common passwords; bypasses account lockouts via distributed IP rotation.
- **User-Agent Fingerprinting for OS-Specific Phishing**: Phishing campaigns analyze HTTP User-Agent headers to deliver tailored payloads (Windows, macOS, Linux, mobile) increasing compromise rates.
- **Trojanized Proof-of-Concept Exploits**: Malicious actors publish weaponized PoC code on GitHub targeting researchers; execution drops ChocoPoC Python RAT with command execution and data theft capabilities.
- **ClickFix Social Engineering**: Fake verification pages (CAPTCHA, "I'm not a robot", browser error) trick users into copying and executing PowerShell/Command Prompt commands that download and run malware.
- **API-Driven Malware Delivery Infrastructure**: ClickFix payloads backed by dynamic API endpoints serving obfuscated commands, enabling rapid campaign updates and evasion.
- **SEO Poisoning for Software Impersonation**: Malicious sites rank for legitimate software searches, delivering trojanized installers (ScreenConnect) that deploy AsyncRAT.
- **Legitimate Remote Access Tool Abuse**: ScreenConnect used as a living-off-the-land binary for persistent remote access and AsyncRAT deployment.
- **Platform Abuse for Payload Hosting**: Blogger (Google) pages used to host staged payloads in VEIL#DROP chain, leveraging trusted domain reputation.
- **Fake PDF Lures for Banking Trojans**: Phishing emails with PDF attachments masquerading as banking documents deliver Ousaban trojan on Windows.
- **AI-Hallucinated Domain Registration (Phantom Squatting)**: Attackers query LLMs for brand domains, register non-existent but plausible variants, and host phishing/malware sites.
- **Prompt Injection Sandbox Escape**: Malicious prompts injected into Cursor AI editor break out of safety sandbox to execute arbitrary shell commands on host.
- **Chromium API Abuse for Ransomware**: AI-generated malware uses `fileSystemAccess` and related Chromium APIs to enumerate and encrypt user files cross-platform.
- **Unpatched Pre-Auth RCE Exploitation**: Direct exploitation of Kemp LoadMaster management interface without authentication for remote code execution.
- **Exposed ERP Instance Targeting**: Automated scanning and exploitation of internet-facing Oracle EBS instances with known critical vulnerability.
- **Unauthenticated Kubernetes Component Access**: Network reachability to Argo CD repo-server enables unauthenticated code execution and cluster takeover.

## Threat Actor Activities

- **Scattered Spider (UNC3944 / 0ktapus)**: 19-year-old suspect extradited from Finland to U.S. to face charges of conspiracy, computer intrusion, and fraud; group known for SIM-swapping, MFA bypass, and cloud extortion campaigns against telecom, BPO, and technology firms.
- **Unknown Operators (ClickFix Campaigns)**: Multiple threat groups adopting ClickFix as primary delivery mechanism; infrastructure analysis reveals shared API backends across campaigns delivering Lumma, Danabot, NetSupport RAT, and others.
- **Unknown Operators (ChocoPoC Supply Chain)**: Actors publishing trojanized PoC exploits on GitHub under convincing repositories; targeting security researchers and practitioners evaluating vulnerabilities.
- **Unknown Operators (SEO-Poisoned ScreenConnect/AsyncRAT)**: "Massive, multi-domain, multi-language" campaign per Kaspersky; likely financially motivated cybercrime group leveraging malvertising/SEO for broad AsyncRAT distribution.
- **Unknown Operators (VEIL#DROP / PureLogs)**: Multi-stage delivery chain using Blogger for staging; PureLogs stealer indicates credential harvesting and financial fraud objectives.
- **Ousaban Operators (Brazilian Banking Trojan Group)**: Portuguese/Spanish-speaking actors deploying Ousaban against Iberian banks; sophisticated webinjects and transaction manipulation capabilities.
- **Unknown Operators (AI-Generated Browser Ransomware)**: Early adoption of LLM-generated malware (DeepSeek) for cross-platform ransomware; indicates lowering barrier for novel capability development.
- **Unknown Operators (Phantom Squatting)**: Opportunistic actors monitoring LLM outputs for hallucinated brand domains; rapid registration and weaponization for phishing.
- **Unknown Operators (Kemp LoadMaster Exploitation)**: Active exploitation attempts observed by eSentire TRU; likely initial access brokers or ransomware affiliates targeting exposed load balancers.
- **Unknown Operators (Oracle EBS Exploitation)**: Ongoing attacks against 900+ exposed instances; consistent with financially motivated groups targeting ERP for data theft or ransomware deployment.
- **Unknown Operators (Kubota Intrusion)**: Month-long dwell time suggests espionage or persistent access objectives; attribution not publicly disclosed.
- **Unknown Operators (DHS HSIN Breach)**: Compromise of federal information-sharing platform; potential espionage motivation given sensitive user base; attribution not publicly disclosed.

## Source Attribution

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
- **Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service**: The Hacker News - https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html
