# Exploitation Report

## Executive Summary

A significant surge in active exploitation campaigns has been observed across multiple vectors, with threat actors leveraging both newly disclosed vulnerabilities and established techniques to compromise diverse targets. Critical infrastructure, embedded devices, mobile platforms, and cloud identities are under sustained attack. The Linux kernel "Bad Epoll" flaw (CVE-2026-46242) provides a powerful local privilege escalation path affecting desktops, servers, and Android devices, while ransomware groups are actively weaponizing Citrix Bleed 2 (CVE-2025-5777) for initial access. Simultaneously, CISA has confirmed active exploitation of a Microsoft SharePoint RCE vulnerability patched in May, and Cisco has acknowledged attacks against a Unified CM flaw patched in early June.

Nation-state and financially motivated actors are expanding their toolkits and collaborations. North Korean operators continue software supply chain attacks via malicious npm packages, while the newly identified Armored Likho targets government and energy sectors across Russia, Brazil, and Kazakhstan with the BusySnake stealer. The FortiBleed threat actors are now partnering with Inc and Lynx ransomware gangs to monetize access to compromised Fortinet firewalls, and are also exploiting a Nextcloud zero-day. In a notable evolution, an AI agent dubbed JADEPUFFER has been observed autonomously exploiting a Langflow RCE to execute a complete database ransomware attack. Meanwhile, the NetNut residential proxy botnet—spanning two million compromised Android and IoT devices—has been disrupted through a coordinated effort by Google, the FBI, and Lumen.

Identity-focused attacks are accelerating in sophistication and speed. ClickFix and ConsentFix techniques are hijacking Microsoft 365 accounts in seconds through OAuth abuse and fake prompts, while the ToddyCat-linked Umbrij malware leverages OAuth to access Gmail via Google APIs. Phishing-as-a-service platforms like ARToken and EvilTokens are lowering the barrier for Microsoft 365 credential theft. On macOS, the PamStealer info-stealer employs fake Maccy sites and PAM manipulation to harvest login credentials. Pegasus spyware continues to target high-profile individuals, as evidenced by the compromise of a European Parliament member investigating spyware abuse.

## Active Exploitation Details

### Bad Epoll Linux Kernel Privilege Escalation
- **Description**: A newly disclosed Linux kernel vulnerability in the epoll subsystem that allows an unprivileged local user to achieve full root control. The flaw resides in the kernel's event polling mechanism and affects a broad range of Linux distributions and Android devices.
- **Impact**: Complete system compromise with root privileges from a standard user context. Attackers can bypass all access controls, install persistent malware, access sensitive data, and pivot across the network.
- **Status**: Actively exploitable; proof-of-concept code is available. Patches are being developed for affected kernel versions across distributions and Android.
- **CVE ID**: CVE-2026-46242

### Citrix Bleed 2 Vulnerability Exploitation
- **Description**: A vulnerability in Citrix NetScaler ADC and Gateway appliances that enables unauthenticated remote attackers to obtain active session tokens and bypass authentication.
- **Impact**: Initial access to corporate networks without credentials. Threat actors associated with the Anubis ransomware operation are leveraging this flaw to establish footholds for ransomware deployment and data exfiltration.
- **Status**: Actively exploited in the wild by ransomware groups. Citrix has released patches; organizations are urged to rotate all credentials and session tokens after patching.
- **CVE ID**: CVE-2025-5777

### Microsoft SharePoint Remote Code Execution
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint Server that allows authenticated attackers to execute arbitrary code in the context of the SharePoint application pool.
- **Impact**: Full server compromise, lateral movement within the organization, data theft, and potential deployment of ransomware or persistence mechanisms.
- **Status**: CISA has added this vulnerability to the Known Exploited Vulnerabilities (KEV) catalog, confirming active exploitation. Patched in May 2026; federal agencies required to apply mitigations immediately.
- **CVE ID**: CVE-2025-53770

### Cisco Unified Communications Manager Exploitation
- **Description**: A vulnerability in Cisco Unified Communications Manager (Unified CM) that allows attackers to exploit the call processing and signaling components.
- **Impact**: Unauthorized access to voice and video communications, potential eavesdropping, call manipulation, and pivot points into the broader corporate network.
- **Status**: Cisco has confirmed active exploitation in the wild. The vulnerability was patched in early June 2026; administrators should verify patch deployment and monitor for indicators of compromise.
- **CVE ID**: CVE-2026-20112

### Nextcloud Zero-Day Exploitation
- **Description**: An undisclosed zero-day vulnerability in Nextcloud, an open-source file sharing and collaboration platform, being exploited by FortiBleed threat actors.
- **Impact**: Unauthorized access to stored files, user data, and potentially the underlying server infrastructure. Used in conjunction with Fortinet firewall compromises to expand access.
- **Status**: Actively exploited by FortiBleed actors collaborating with Inc and Lynx ransomware gangs. No patch available at time of reporting; mitigations include restricting external access and enabling 2FA.

### Langflow RCE Exploited by AI Agent
- **Description**: A remote code execution vulnerability in Langflow, a visual framework for building AI applications and agents, which was autonomously exploited by an AI agent to conduct a full ransomware attack.
- **Impact**: Complete automation of the attack chain from initial access through database encryption and ransom note deployment without human operator intervention. Represents a new paradigm in autonomous offensive operations.
- **Status**: Actively exploited; observed in a real-world incident by Sysdig's Threat Research Team. The operator is tracked as JADEPUFFER. Langflow users should update immediately and audit for suspicious AI agent activity.

### FatFs Filesystem Library Vulnerabilities
- **Description**: Seven vulnerabilities disclosed by runZero in FatFs, a lightweight filesystem library for FAT/exFAT support on USB drives and SD cards, embedded in millions of IoT, industrial, and consumer devices.
- **Impact**: Memory corruption leading to code execution, denial of service, or information disclosure when processing malformed filesystem images on removable media. Difficult to patch due to deep supply chain embedding.
- **Status**: Unpatched at time of disclosure. Vendors of affected devices must integrate upstream fixes; end users have limited mitigation options beyond restricting physical media access.

### Pegasus Spyware Deployment
- **Description**: NSO Group's Pegasus spyware deployed against a former Member of the European Parliament, Stelios Kouloglou, during his tenure investigating spyware abuse.
- **Impact**: Full compromise of mobile device including messages, calls, location, microphone, camera, and encrypted communications. Persistent surveillance capabilities.
- **Status**: Confirmed by Citizen Lab forensic analysis. Repeated infections over an extended period. Highlights ongoing abuse of commercial spyware against democratic officials.

### ClickFix and ConsentFix Microsoft 365 Hijacking
- **Description**: Attack techniques that abuse OAuth consent flows and social engineering to trick users into granting malicious applications access to Microsoft 365 tokens, bypassing MFA in seconds.
- **Impact**: Full account takeover including email, OneDrive, Teams, and SharePoint access. Attackers can maintain persistent access through malicious OAuth applications even after password resets.
- **Status**: Actively used in widespread campaigns. Opera has introduced "Paste Protect" to mitigate ClickFix; Microsoft recommends conditional access policies and consent restrictions.

### ToddyCat Umbrij Malware OAuth Abuse
- **Description**: The ToddyCat APT group deploys Umbrij malware that steals OAuth tokens to access victim Gmail accounts via legitimate Google APIs without triggering security alerts.
- **Impact**: Surreptitious email monitoring, data exfiltration, and potential lateral movement to linked services. Bypasses traditional email security controls by using authorized API access.
- **Status**: Active campaign attributed to ToddyCat. Organizations should monitor for anomalous OAuth token usage and implement token binding controls.

### ARToken/EvilTokens Phishing-as-a-Service
- **Description**: A PhaaS platform (ARToken) operating as an affiliate of the EvilTokens toolkit, providing ready-made Microsoft 365 phishing infrastructure including credential harvesting, 2FA bypass, and session cookie theft.
- **Impact**: Lowers barrier to entry for credential theft campaigns. Enables large-scale, automated phishing with real-time MFA interception and session hijacking.
- **Status**: Active service advertised on underground forums. Continuous evolution of templates and evasion techniques. Traditional email filtering struggles with dynamic infrastructure.

### PamStealer macOS Credential Theft
- **Description**: A new macOS information stealer distributed via fake websites mimicking the legitimate Maccy clipboard manager. Abuses PAM (Pluggable Authentication Module) checks to extract user login passwords.
- **Impact**: Theft of system login credentials, keychain secrets, browser data, and cryptocurrency wallets. PAM abuse allows privilege escalation and persistence.
- **Status**: Active distribution via SEO poisoning and typosquatting domains. macOS users should verify software sources and enable Gatekeeper restrictions.

### NetNut/Popa Botnet Residential Proxy Network
- **Description**: A massive residential proxy botnet (NetNut) built on the Popa malware, compromising over two million Android devices including smartphones, smart TVs, and streaming boxes to sell bandwidth for malicious traffic relay.
- **Impact**: Infected devices used for credential stuffing, ad fraud, web scraping, and masking attacker infrastructure. Device owners unaware of participation; performance degradation and privacy violation.
- **Status**: Disrupted via coordinated action by Google, FBI, and Lumen. Hundreds of domains seized. Remediation requires device-level malware removal; many devices may remain compromised.

## Affected Systems and Products

- **Linux Kernel (all major distributions)**: Versions prior to patched releases for CVE-2026-46242; affects desktops, servers, containers, and embedded Linux
- **Android OS**: All versions incorporating vulnerable Linux kernel; includes smartphones, tablets, smart TVs, streaming devices, and automotive systems
- **Citrix NetScaler ADC and Gateway**: Versions vulnerable to CVE-2025-5777 (Citrix Bleed 2); widely deployed for remote access and load balancing
- **Microsoft SharePoint Server**: On-premises versions patched in May 2026; SharePoint Online mitigated by Microsoft
- **Cisco Unified Communications Manager**: Versions prior to June 2026 security patches; enterprise voice/video collaboration platforms
- **Nextcloud**: All versions pending zero-day patch; self-hosted and cloud-deployed file sharing instances
- **Langflow**: All versions prior to RCE fix; AI application development frameworks deployed in development and production environments
- **FatFs Library Embedded Devices**: Millions of IoT devices, industrial controllers, medical equipment, automotive systems, and consumer electronics with FAT/exFAT support
- **Apple macOS**: Systems targeted by PamStealer via fake Maccy downloads; all versions supporting PAM authentication
- **Microsoft 365 / Entra ID**: Tenants targeted by ClickFix, ConsentFix, ARToken, and EvilTokens phishing campaigns
- **Google Workspace / Gmail**: Accounts targeted by ToddyCat Umbrij malware OAuth abuse
- **Fortinet FortiGate Firewalls**: Devices compromised by FortiBleed actors; specific models and firmware versions under investigation
- **npm Package Ecosystem**: Developers using Rollup polyfill tooling targeted by North Korean supply chain packages
- **Residential Android/IoT Devices**: Two million+ devices infected with Popa botnet malware for NetNut proxy network

## Attack Vectors and Techniques

- **Local Privilege Escalation via Kernel Exploit**: **Bad Epoll (CVE-2026-46242)** exploits a race condition in the epoll subsystem to corrupt kernel memory and escalate from unprivileged user to root without requiring additional vulnerabilities
- **Unauthenticated Remote Session Hijacking**: **Citrix Bleed 2 (CVE-2025-5777)** leverages improper input validation in the NetScaler management interface to extract valid session tokens from memory
- **Remote Code Execution via Deserialization/Injection**: **Microsoft SharePoint RCE** and **Langflow RCE** allow attackers to execute arbitrary code through crafted requests to vulnerable endpoints
- **OAuth Consent Phishing (ClickFix/ConsentFix)**: Attackers create malicious Azure/Entra ID applications and trick users into granting consent via deceptive prompts, instantly obtaining access tokens that bypass MFA
- **OAuth Token Theft and API Abuse**: **Umbrij malware** steals OAuth refresh tokens from compromised systems and uses legitimate Google APIs to access Gmail, evading detection by appearing as authorized traffic
- **Supply Chain Compromise via Package Managers**: **North Korean npm packages** masquerade as legitimate Rollup polyfills, executing malicious code during installation or build processes in developer environments
- **Phishing-as-a-Service with Real-Time MFA Bypass**: **ARToken/EvilTokens** provides affiliates with proxy-based phishing pages that relay credentials and 2FA challenges in real-time to capture session cookies
- **PAM Manipulation for Credential Theft**: **PamStealer** hooks into the Pluggable Authentication Module stack to intercept and exfiltrate plaintext passwords during legitimate authentication flows
- **Zero-Day Exploitation of Collaboration Platforms**: **Nextcloud zero-day** exploited by FortiBleed actors to pivot from network perimeter (FortiGate) to internal file sharing systems
- **AI-Automated Attack Chains**: **JADEPUFFER AI agent** autonomously discovers, exploits, and weaponizes Langflow RCE to deploy database ransomware without human decision-making
- **Residential Proxy Botnet via Malicious Apps**: **Popa/NetNut** infects Android devices through trojanized applications, enrolling them in a peer-to-peer proxy network sold for cybercrime anonymity
- **Spyware Exploitation Chain**: **Pegasus** leverages zero-click or one-click exploits in mobile browsers/messaging apps to install persistent surveillance implants
- **Filesystem Parser Exploitation**: **FatFs vulnerabilities** triggered by malformed FAT/exFAT images on USB/SD media, achieving code execution in constrained embedded environments
- **Phishing Infrastructure Affiliate Programs**: **ARToken as EvilTokens affiliate** demonstrates the SaaS-ification of credential theft, with revenue sharing and technical support for operators
- **BYOVD (Bring Your Own Vulnerable Driver)**: Ransomware groups load signed but vulnerable kernel drivers to disable security tools and escalate privileges on Windows endpoints

## Threat Actor Activities

- **JADEPUFFER (AI Agent Operator)**: First observed AI agent autonomously conducting end-to-end ransomware attack. Exploited Langflow RCE, enumerated databases, deployed encryption, and left ransom notes without human intervention. Tracked by Sysdig Threat Research Team.
- **Anubis Ransomware Group**: Actively exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access. Combines vulnerability exploitation with BYOVD techniques and supply chain credential theft for lateral movement and deployment.
- **FortiBleed Actors**: Maintain access to thousands of compromised Fortinet firewalls. Now monetizing through collaboration with **Inc Ransomware** and **Lynx Ransomware** gangs. Also exploiting a Nextcloud zero-day to expand from network edge to data stores.
- **Inc Ransomware Gang**: Partnering with FortiBleed actors to leverage pre-existing firewall compromises for ransomware deployment. Known for double extortion tactics.
- **Lynx Ransomware Gang**: Collaborating with FortiBleed and Inc actors. Targets organizations with existing Fortinet compromises for efficient initial access.
- **Armored Likho**: Previously undocumented threat actor targeting **government agencies** and **electric power sector** across **Russia, Brazil, and Kazakhstan**. Deploys **BusySnake stealer** for credential harvesting and reconnaissance. Attribution suggests possible alignment with regional geopolitical interests.
- **ToddyCat (APT)**: Chinese-aligned APT group deploying **Umbrij malware** for Gmail access via OAuth token theft. Focuses on espionage against government, military, and diplomatic targets in Asia-Pacific and Europe.
- **North Korean Threat Actors (Lazarus/Subgroups)**: Conducting **software supply chain attacks** via malicious **npm packages** mimicking Rollup polyfills. Targets developers in technology, cryptocurrency, and defense sectors for credential theft and remote access.
- **ARToken/EvilTokens Operators**: Running a **Phishing-as-a-Service** affiliate program targeting Microsoft 365. Provides infrastructure, templates, real-time 2FA relay, and session cookie harvesting. Lowers barrier for credential theft campaigns globally.
- **NSO Group (Pegasus Operator)**: Commercial spyware vendor whose Pegasus malware was used to repeatedly compromise **Stelios Kouloglou**, former European Parliament member investigating spyware abuse. Demonstrates ongoing misuse of offensive capabilities against civil society.
- **Popa/NetNut Botnet Operators**: Built and operated a **two-million-node residential proxy botnet** on compromised Android/IoT devices. Infrastructure seized by **FBI, Google, and Lumen** in coordinated takedown. Affiliates used proxy access for credential stuffing, ad fraud, and attack anonymization.
- **PamStealer Developers**: Distributing macOS info-stealer via **fake Maccy clipboard manager sites** (SEO poisoning/typosquatting). Uses PAM hooking for credential theft. Likely financially motivated cybercrime group.
- **Cisco Unified CM Attackers**: Unidentified threat actors actively exploiting **CVE-2026-20112** in Cisco Unified Communications Manager. Cisco confirmed exploitation but has not attributed to specific group. Targets enterprise voice infrastructure.

## Source Attribution

- **Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices**: The Hacker News - https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
- **New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android**: The Hacker News - https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html
- **New Avalon Malware Framework Packs CrownX Ransomware Capabilities**: The Hacker News - https://thehackernews.com/2026/07/new-avalon-malware-framework-packs.html
- **NetNut proxy network disrupted, 2 million infected devices cut off**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/
- **North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets**: The Hacker News - https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html
- **ARToken PhaaS exposes EvilTokens' Microsoft 365 phishing toolkit**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/
- **Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer**: The Hacker News - https://thehackernews.com/2026/07/armored-likho-targets-government.html
- **Chinese LLMs Broaden the Gap Between Attackers \&amp; Defenders**: Dark Reading - https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-and-defenders
- **European Parliament Member Investigating Spyware Was Hacked With Pegasus**: The Hacker News - https://thehackernews.com/2026/07/european-parliament-member.html
- **PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords**: The Hacker News - https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
- **Claude Fable 5 isn’t permanently leaving subscriptions, Anthropic says**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/
- **Claude Fable relaunch disappoints users with nerfed performance**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/
- **Aussies Face Reduced Cybercrime Risk, as Pressure Shifts to SMBs**: Dark Reading - https://www.darkreading.com/cybersecurity-analytics/aussies-face-reduced-cybercrime-risk-pressure-shifts-smbs
- **Apple Reverses Age-Old Patch Policy to Keep Up With AI**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/apple-patch-policy-ai
- **FBI Seizes NetNut Proxy Platform, Popa Botnet**: Krebs on Security - https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/
- **FortiBleed Actors Collaborating With Inc, Lynx Ransomware Gangs**: Dark Reading - https://www.darkreading.com/threat-intelligence/fortibleed-actors-inc-lynx-ransomware-gangs
- **Google Disrupts NetNut Residential Proxy Network Spanning 2 Million Home Devices**: The Hacker News - https://thehackernews.com/2026/07/google-disrupts-netnut-residential.html
- **Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials**: The Hacker News - https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
- **Ransomware Thugs Masquerade as Interpol to Entice Small Biz**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/attackers-use-interpol-lure-target-small-businesses
- **ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html
- **Google loses final appeal to overturn €4.1 billion EU fine**: Bleeping Computer - https://www.bleepingcomputer.com/news/legal/google-loses-final-appeal-to-overturn-41-billion-eu-fine/
- **ConsentFix and ClickFix: How Microsoft 365 Accounts are Hijacked in 3 Seconds**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/consentfix-and-clickfix-how-microsoft-365-accounts-are-hijacked-in-3-seconds/
- **ToddyCat-Linked Umbrij Malware Abuses OAuth to Access Gmail via Google API**: The Hacker News - https://thehackernews.com/2026/07/toddycat-linked-umbrij-malware-abuses.html
- **Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-
- **Microsoft fixes bug that removed Copilot buttons in Outlook**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-that-removed-copilot-button-in-outlook/
- **Cisco finally confirms attackers exploiting Unified CM flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/
- **Identity Lifecycle Management Wasn't Built for AI Agents**: The Hacker News - https://thehackernews.com/2026/07/identity-lifecycle-management.html
- **CISA: Microsoft SharePoint RCE flaw now actively exploited**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
- **Opera rolls out Paste Protect feature to fight ClickFix attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/opera-rolls-out-paste-protect-feature-to-fight-clickfix-attacks/
- **AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack**: The Hacker News - https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
