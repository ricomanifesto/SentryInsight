# Exploitation Report

## Executive Summary

This reporting period reveals a significant escalation in active exploitation across multiple critical vectors, with supply-chain attacks, zero-day vulnerabilities in widely deployed infrastructure, and record-breaking patch cycles dominating the threat landscape. Most critically, two SonicWall SMA 1000 zero-days (CVE-2026-15409 and CVE-2026-15410) are under active exploitation in the wild, enabling arbitrary command execution on internet-exposed Secure Mobile Access appliances. Simultaneously, CISA has issued an emergency directive for three actively exploited SharePoint Server vulnerabilities targeting on-premises deployments. Microsoft's July 2026 Patch Tuesday shipped fixes for a record 570–622 vulnerabilities, including three zero-days—two confirmed under active attack—marking the largest single-month remediation effort in the company's history.

Supply-chain compromise has emerged as a parallel crisis, with the AsyncAPI npm namespace infected across five package versions delivering multi-stage botnet malware to downstream consumers. Nearly 300 counterfeit GitHub repositories were discovered masquerading as legitimate software to distribute infostealers, while a novel Rust-based RAT (LabubaRAT) masquerades as NVIDIA software to evade detection. Developer tooling has become a high-value target: Cursor's automatic execution of `git.exe` in project roots enables zero-click code execution on Windows, and a two-click exploit chain grants attackers full access to source code and secrets in development environments.

AI-integrated attack surfaces are expanding rapidly. The "PromptFiction" vulnerability in Claude, though patched, demonstrated how chained exploits could enable end-to-end system compromise, while the Claude for Chrome extension flaw permits rogue extensions to exfiltrate Gmail, Google Docs, and Calendar data. Research into AI-automated vulnerability discovery has produced a functional "vulnerability vending machine" that converts LLM tokens into zero-day discoveries. Law enforcement actions disrupted a Russian bulletproof hosting operation responsible for $62 million in ransomware damages and a €140 million Spanish cyber fraud ring, signaling increased state-level response to cybercrime infrastructure.

## Active Exploitation Details

### SonicWall SMA 1000 Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting SonicWall Secure Mobile Access (SMA) 1000 series appliances. One vulnerability enables arbitrary command execution with administrative privileges, while the second provides a complementary attack path. Both are remotely exploitable on internet-exposed devices.
- **Impact**: Attackers can achieve full administrative control over SMA 1000 appliances, enabling network pivoting, credential theft, persistence establishment, and lateral movement into internal networks. These devices serve as critical VPN gateways for remote access.
- **Status**: Actively exploited in zero-day attacks. SonicWall has released emergency patches. CISA and vendor advisories urge immediate patching of all internet-exposed SMA 1000 appliances.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Microsoft July 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's largest-ever Patch Tuesday addressed 570–622 vulnerabilities across Windows and associated products. Three zero-days were resolved: two confirmed under active exploitation in the wild, and one publicly disclosed prior to patch availability. The exploited zero-days span core Windows components.
- **Impact**: Active exploitation of the two zero-days allows attackers to achieve privilege escalation, remote code execution, or security feature bypass on unpatched systems. The scale of 60+ critical vulnerabilities significantly expands the attack surface for organizations delayed in patch deployment.
- **Status**: Patches released July 2026. Active exploitation confirmed for two zero-days; one publicly disclosed. Emergency deployment recommended for all affected Windows versions (10, 11, Server).
- **CVE ID**: Specific CVE IDs for the three zero-days not provided in source articles; 570–622 total CVEs addressed.

### Actively Exploited SharePoint Server Vulnerabilities
- **Description**: Three vulnerabilities in on-premises Microsoft SharePoint Server are being actively exploited by threat actors targeting internet-exposed instances. The flaws enable remote code execution and authentication bypass chains.
- **Impact**: Compromise of SharePoint servers provides attackers with access to enterprise document repositories, internal collaboration data, and potential footholds for domain escalation via service accounts and application pools.
- **Status**: CISA has added these vulnerabilities to the Known Exploited Vulnerabilities (KEV) catalog and mandated federal civilian agency patching. Patches available from Microsoft; immediate application required for internet-facing deployments.
- **CVE ID**: Specific CVE IDs not provided in source articles.

### Firefox Critical Vulnerability with Published Exploit Code
- **Description**: Mozilla Firefox contains a critical invalid pointer dereference vulnerability (CVE-2026-15718) for which exploit code has been publicly published. A second critical flaw was also addressed in the same release cycle.
- **Impact**: Successful exploitation can lead to arbitrary code execution in the browser context, enabling drive-by compromise, sandbox escape chaining, and sensitive data theft from browser memory.
- **Status**: Exploit code publicly available. Mozilla has released emergency updates. Users and enterprises should update to the latest Firefox version immediately.
- **CVE ID**: CVE-2026-15718

### Windows User Profile Service Zero-Day (LegacyHive)
- **Description**: Security researcher Chaotic Eclipse (Nightmare-Eclipse) released a proof-of-concept exploit named "LegacyHive" targeting the Windows User Profile Service. The vulnerability enables arbitrary hive loading, allowing registry manipulation and privilege escalation.
- **Impact**: Local privilege escalation to SYSTEM, persistence via registry manipulation, and potential bypass of security controls. PoC released hours after Patch Tuesday, indicating either a variant not covered by patches or a disclosure timing tactic.
- **Status**: PoC publicly available. Patch status unclear from sources; may represent a zero-day or a bypass of July 2026 fixes. Requires immediate validation against deployed patches.
- **CVE ID**: Not provided in source articles.

### SAP NetWeaver ABAP Critical Flaw
- **Description**: A critical vulnerability in SAP NetWeaver Application Server ABAP with a CVSS 9.9 score, the highest severity rating. The flaw allows unauthenticated attackers to expose or modify sensitive business data.
- **Impact**: Full compromise of SAP ERP data integrity and confidentiality, including financial records, supply chain data, HR information, and customer records. Potential for fraudulent transaction injection and business process disruption.
- **Status**: SAP has released security updates as part of July 2026 Security Patch Day. Emergency patching recommended for all exposed NetWeaver ABAP instances.
- **CVE ID**: Not provided in source articles.

### AsyncAPI npm Supply-Chain Compromise
- **Description**: Five malicious versions across four @asyncapi namespace packages (@asyncapi/generator, @asyncapi/parser, @asyncapi/validator, @asyncapi/markdown-template, @asyncapi/react-component) were published to npm, delivering a multi-stage botnet loader with credential-stealing and remote access capabilities.
- **Impact**: Any project installing compromised versions (2.6.0, 2.5.4, 2.5.3, 2.5.2, 2.5.1) executes malicious code during install or build, leading to full developer machine compromise, source code exfiltration, CI/CD credential theft, and downstream software supply-chain poisoning.
- **Status**: Malicious packages identified and reported by OX Security, SafeDep, Socket, and StepSecurity. npm has quarantined affected versions. Organizations must audit dependency trees, rotate all credentials, and rebuild artifacts.
- **CVE ID**: Not applicable (malicious package publication, not a vulnerability in legitimate code).

### Cursor IDE Zero-Click Code Execution
- **Description**: Cursor (AI-powered code editor) on Windows automatically executes any file named `git.exe` present in a project's root directory when the repository is opened. No user interaction, approval dialog, or warning is presented.
- **Impact**: Attackers distributing malicious repositories (via GitHub, git cloning, or zip extraction) achieve immediate arbitrary code execution on developer machines with the developer's privileges, enabling source code theft, supply-chain injection, and lateral movement.
- **Status**: No patch mentioned in sources. Mitigation requires disabling automatic repository opening, verifying repository contents before opening in Cursor, and monitoring for `git.exe` in project roots.
- **CVE ID**: Not provided in source articles.

### Two-Click Cursor Dev Environment Takeover
- **Description**: A chain of "simple age-old bugs" in Cursor enables attackers to take over development environments with just two clicks, accessing secrets, source code, and CI/CD tokens.
- **Impact**: Full compromise of developer workstations and connected cloud environments. Access to API keys, database credentials, signing keys, and proprietary source code.
- **Status**: Active exploitation potential high given simplicity. No patch status provided in sources.
- **CVE ID**: Not provided in source articles.

### Claude AI Prompt Injection Chain (PromptFiction)
- **Description**: The "PromptFiction" vulnerability in Anthropic's Claude, when combined with a second exploit, enables an end-to-end attack chain against targeted systems. The flaw has been patched but demonstrates the risk of chained prompt injection.
- **Impact**: Potential for full system compromise via AI agent manipulation, including data exfiltration, unauthorized actions, and privilege escalation through connected tools and APIs.
- **Status**: Patched by Anthropic. Serves as a proof-of-concept for AI agent attack chains.
- **CVE ID**: Not provided in source articles.

### Claude for Chrome Extension Cross-Extension Exploitation
- **Description**: The Claude for Chrome extension permits any other browser extension capable of running scripts on claude.ai to trigger Claude actions targeting the user's Gmail, Google Docs, comments, and Calendar.
- **Impact**: Data exfiltration from Google Workspace (emails, documents, calendar events) by malicious or compromised extensions. Bypasses extension isolation boundaries.
- **Status**: No patch status provided in sources. Users should review installed extensions and consider disabling Claude for Chrome until mitigated.
- **CVE ID**: Not provided in source articles.

### 6 GHz Wi-Fi Automated Frequency Coordination Flaws
- **Description**: Automated Frequency Coordination (AFC) systems for 6 GHz Wi-Fi inherently trust client-side data, enabling location spoofing and interference attacks that can disrupt critical wireless systems.
- **Impact**: Disruption of critical infrastructure relying on 6 GHz bands (industrial IoT, medical devices, public safety, transportation). Location spoofing enables regulatory bypass and interference injection.
- **Status**: Architectural flaw in AFC trust model. No patches available; requires protocol-level fixes and client-side validation deployment.
- **CVE ID**: Not provided in source articles.

### LabubaRAT NVIDIA-Masquerading Malware
- **Description**: A previously undocumented Rust-based remote access trojan (LabubaRAT) masquerades as legitimate NVIDIA software (filenames, metadata, behavior) to blend into target environments and evade detection.
- **Impact**: Full remote control of infected Windows hosts, including command execution, file exfiltration, keylogging, screen capture, and lateral movement. NVIDIA disguise reduces suspicion in gaming, AI/ML, and engineering environments.
- **Status**: Active in the wild. Detection signatures being deployed by endpoint vendors. No specific vulnerability exploited; relies on social engineering and supply-chain delivery.
- **CVE ID**: Not applicable (malware campaign).

### GitHub Repository Impersonation Campaign
- **Description**: Nearly 300 fake GitHub repositories impersonating legitimate software and security projects distribute infostealer malware to developers and users seeking tools.
- **Impact**: Credential theft (browser passwords, crypto wallets, API keys, session cookies), system reconnaissance, and potential supply-chain compromise if developers integrate malicious code.
- **Status**: Active campaign. GitHub takedowns in progress but new repositories likely appear continuously. Requires developer vigilance and verified source verification.
- **CVE ID**: Not applicable (social engineering / typosquatting campaign).

## Affected Systems and Products

- **SonicWall SMA 1000 Series Appliances**: All firmware versions prior to the emergency July 2026 patches. Internet-exposed VPN gateways at highest risk.
- **Microsoft Windows (10, 11, Server 2016/2019/2022)**: All supported versions affected by July 2026 Patch Tuesday vulnerabilities (570–622 CVEs). Extended Security Updates (ESU) customers on Windows 10 receive KB5099539.
- **Microsoft SharePoint Server (On-Premises)**: Internet-exposed on-premises SharePoint Server farms. Specific versions not detailed in sources; all unpatched instances at risk.
- **Mozilla Firefox**: All versions prior to the July 2026 security release containing fixes for CVE-2026-15718 and a second critical flaw.
- **SAP NetWeaver Application Server ABAP**: All versions affected by the CVSS 9.9 critical flaw. Emergency patches released in July 2026 Security Patch Day.
- **AsyncAPI npm Packages**: @asyncapi/generator, @asyncapi/parser, @asyncapi/validator, @asyncapi/markdown-template, @asyncapi/react-component versions 2.6.0, 2.5.4, 2.5.3, 2.5.2, 2.5.1. All projects with these versions in dependency trees (direct or transitive).
- **Cursor IDE (Windows)**: All Windows versions of Cursor that automatically execute `git.exe` from project roots. Electron-based architecture on Windows.
- **Anthropic Claude / Claude for Chrome Extension**: Claude web interface and Chrome extension users. Patched version for PromptFiction; Chrome extension flaw status unclear.
- **6 GHz Wi-Fi AFC Systems**: All deployments using Automated Frequency Coordination with client-trusted data models. Enterprise, industrial, and critical infrastructure wireless networks.
- **Dell Devices (Specific Models)**: Certain Dell PCs running Windows 11 experiencing shutdowns and performance issues after July 2026 updates. Microsoft has blocked updates on affected hardware.
- **Developer Workstations (General)**: Any system cloning GitHub repositories, installing npm packages, or using Cursor IDE. High-value targets due to credential and source code access.

## Attack Vectors and Techniques

- **Supply-Chain Compromise (npm)**: Malicious package publication to legitimate namespace (@asyncapi) with version numbers mimicking legitimate releases. Multi-stage payload: installer scripts → downloader → botnet loader → RAT + infostealer.
- **Supply-Chain Compromise (GitHub)**: Typosquatting and brand impersonation across ~300 repositories. Social engineering via search ranking, README quality, and star manipulation to trick developers into cloning/running malicious code.
- **Zero-Day Exploitation (Network Perimeter)**: Remote exploitation of SonicWall SMA 1000 (CVE-2026-15409, CVE-2026-15410) and SharePoint Server (3 KEV-listed CVEs) on internet-exposed devices. No authentication required for initial access.
- **Zero-Day Exploitation (Client-Side)**: Firefox CVE-2026-15718 with public exploit code enables drive-by compromise. Windows LegacyHive PoC enables local privilege escalation post-exploitation.
- **Developer Environment Targeting**: Cursor `git.exe` auto-execution (zero-click RCE) and two-click exploit chain. Malicious repositories crafted to exploit IDE behaviors. High-value credential and source code theft.
- **AI Agent Prompt Injection Chaining**: PromptFiction demonstrates multi-stage prompt injection combined with secondary exploit for end-to-end compromise. Claude for Chrome extension cross-origin messaging abuse enables data exfiltration via rogue extensions.
- **Masquerading / Living-off-the-Land**: LabubaRAT mimics NVIDIA software (filenames, certificates, process names) to evade EDR and analyst scrutiny. Rust implementation avoids common detection signatures.
- **Bulletproof Hosting Infrastructure**: Russian BPH service (charged by US DOJ) provided resilient hosting for ransomware affiliates (LockBit, BlackCat, etc.), enabling $62M+ in damages. Infrastructure resilience via abuse-compliant registrars, fast-flux DNS, and offshore hosting.
- **Business Email Compromise (BEC) + Investment Fraud**: Spanish fraud ring combined BEC (credential phishing, invoice manipulation) with pig-butchering investment scams for €140M total take. Money laundering via crypto exchanges and shell companies.
- **AFC Trust Model Abuse**: Client-side location data spoofing in 6 GHz Wi-Fi AFC systems. Attackers inject false coordinates to claim spectrum access, disrupting legitimate critical systems.

## Threat Actor Activities

- **Chaotic Eclipse / Nightmare-Eclipse**: Security researcher who publicly released the LegacyHive PoC for Windows User Profile Service hours after July 2026 Patch Tuesday. Motivation appears to be vulnerability disclosure pressure or demonstration of patch bypass. No attribution to APT or cybercrime group.
- **Russian Bulletproof Hosting Operators (Charged)**: Three Russian nationals (names in public indictment) alleged to have operated a bulletproof hosting service used by LockBit, BlackCat/ALPHV, and other ransomware groups. Infrastructure enabled $62M+ in victim damages. US DOJ unsealed charges July 2026.
- **Spanish Cyber Fraud Ring (Dismantled)**: Four individuals arrested by Spanish National Police. Operated combined BEC and investment fraud ("pig butchering") campaign netting €140M ($160M). Money laundering via crypto mixers, shell companies, and complicit financial intermediaries.
- **AsyncAPI Supply-Chain Actor (Unknown)**: Actor(s) who gained publish access to @asyncapi npm namespace (credential theft, compromised maintainer account, or social engineering). Delivered sophisticated multi-stage botnet. Attribution not established in sources.
- **GitHub Impersonation Campaign Actor (Unknown)**: Operator of ~300 fake repositories distributing infostealers. Likely a single group or service selling access. Infrastructure overlaps with prior typosquatting campaigns. Attribution not established.
- **SonicWall Zero-Day Exploiters (Unknown)**: Threat actors actively exploiting CVE-2026-15409 and CVE-2026-15410 in the wild. Targeting internet-exposed SMA 1000 appliances. No attribution provided; could be APT (espionage) or initial access brokers (ransomware).
- **SharePoint Exploiters (Unknown)**: Actors leveraging three KEV-listed SharePoint flaws against on-premises servers. CISA warning indicates broad exploitation. Consistent with initial access broker activity feeding ransomware affiliates.
- **Intruder (Researcher/Vendor)**: Developed AI-powered "vulnerability vending machine" combining code slicing with LLMs to automatically discover complex vulnerabilities. Demonstrated zero-day discovery capability. Commercial entity; tool not publicly released.

## Source Attribution

- **​ ​AsyncAPI npm packages infected with credential-stealing malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/-asyncapi-npm-packages-infected-with-credential-stealing-malware/
- **Claude Flaw Automatically Sends Malicious Prompts to AI Agents**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/claude-flaw-malicious-prompts-ai-agents
- **We built a vulnerability vending machine: AI tokens in, zero-days out**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/we-built-a-vulnerability-vending-machine-ai-tokens-in-zero-days-out/
- **Firefox, Chrome, Adobe, and VMware Updates Fix Multiple Critical Security Flaws**: The Hacker News - https://thehackernews.com/2026/07/firefox-chrome-adobe-and-vmware-updates.html
- **2-Click Cursor Exploit Enables Dev Environment Takeover**: Dark Reading - https://www.darkreading.com/application-security/2-click-cursor-exploit-dev-environment-takeover
- **SASE Has An AI Blind Spot. Inspecting Packets Is No Longer Enough.**: The Hacker News - https://thehackernews.com/2026/07/sase-has-ai-blind-spot-inspecting.html
- **Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday**: The Hacker News - https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html
- **New Webinar: Closing the Approval Gap in AI-Era Ad Tech**: The Hacker News - https://thehackernews.com/2026/07/new-webinar-closing-approval-gap-in-ai.html
- **Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution**: The Hacker News - https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html
- **CISA warns admins to patch actively exploited SharePoint flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-patch-actively-exploited-sharepoint-flaws/
- **Compromised AsyncAPI npm Packages Deliver Multi-Stage Botnet Malware**: The Hacker News - https://thehackernews.com/2026/07/compromised-asyncapi-npm-packages.html
- **Microsoft: Some Dell PCs shut down after recent Windows updates**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-some-dell-devices-shut-down-after-windows-update/
- **Nigeria Deepens Cybersecurity Efforts as Cybercriminals See More Profits**: Dark Reading - https://www.darkreading.com/cyber-risk/nigeria-cybersecurity-efforts-cybercriminals-profits
- **US charges alleged operators of Russian bulletproof hosting service**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-alleged-russian-bulletproof-hosting-service-operators/
- **Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands**: The Hacker News - https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html
- **Cribl Adds Agentic Detection Engineering \&amp; Boosts SecOps With CardinalOps Deal**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cribl-adds-agentic-detection-engineering-boosts-secops-with-cardinalops-deal
- **Records Are Made to Be Broken: Patch Tuesday Raises Triage Stakes**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/records-broken-patch-tuesday-raises-triage-stakes
- **SonicWall warns of SMA1000 flaws exploited in zero-day attacks, patch now**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-sma1000-flaws-exploited-in-zero-day-attacks-patch-now/
- **Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack**: The Hacker News - https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html
- **Spanish Police take down €140 million cyber fraud ring, arrest four**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/spanish-police-take-down-140-million-cyber-fraud-ring-arrest-four/
- **6 GHz Wi-Fi Flaws Could Disrupt Critical Systems**: Dark Reading - https://www.darkreading.com/perimeter/6-ghz-wi-fi-flaws-disrupt-critical-systems
- **Microsoft Patches a Record 570 Security Flaws**: Krebs on Security - https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/
- **Nearly 300 GitHub repos pose as legit software to push malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/nearly-300-github-repos-pose-as-legit-software-to-push-malware/
- **Microsoft releases Windows 10 KB5099539 extended security update**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-10-kb5099539-extended-security-update/
- **SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data**: The Hacker News - https://thehackernews.com/2026/07/sap-patches-cvss-99-netweaver-abap-flaw.html
- **Microsoft July 2026 Patch Tuesday fixes massive 570 flaws, 3 zero-days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2026-patch-tuesday-fixes-massive-570-flaws-3-zero-days/
- **Manage Vendor Risk in a Few Practical Steps**: Dark Reading - https://www.darkreading.com/cyber-risk/manage-vendor-risk-in-a-few-practical-steps
- **Windows 11 KB5101650 \& KB5099414 cumulative updates released**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5101650-and-kb5099414-cumulative-updates-released/
- **Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads**: The Hacker News - https://thehackernews.com/2026/07/claude-for-chrome-flaw-lets-other.html
- **LabubaRAT Masquerades as NVIDIA Software to Control Windows Hosts**: The Hacker News - https://thehackernews.com/2026/07/labubarat-masquerades-as-nvidia.html
