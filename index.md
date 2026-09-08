---
schema_version: 2
report_date: 2026-09-08
generated_at: 2026-09-08T21:02:20Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-08/
---
# Exploitation Report

## Executive Summary

Microsoft's September 2026 Patch Tuesday addressed a record-breaking 966 vulnerabilities, including two actively exploited zero-days that demand immediate patching across Windows environments. Adobe simultaneously released an emergency fix for CVE-2026-75650, a maximum-severity Magento and Adobe Commerce zero-day (CVSS 10.0) dubbed StyleSmuggler that has been under active exploitation since September 4, enabling attackers to deploy Rust-based backdoors and PHP web shells on e-commerce servers.

Multiple high-impact intrusion campaigns are underway across diverse vectors. Threat actors are breaching F5 BIG-IP APM devices to deploy fileless Linux rootkits that inject web shells directly into memory, while the ShinyHunters extortion gang claims to have stolen over 200,000 records from Florida's DMV database. A newly identified financially motivated actor, Slim Spider, has been targeting Brazilian financial institutions since March 2026 with deep knowledge of local payment infrastructure. Meanwhile, the DoppelCart fraud network operates over 119,000 fake e-commerce domains to harvest payment card data at scale.

The threat landscape is rapidly evolving with AI-powered automation. Google Threat Intelligence Group observed a financially motivated group using autonomous multi-agent AI frameworks to compromise thousands of credentials in under six hours. ClickFix social engineering campaigns now abuse legitimate services for persistent access, and a sophisticated vishing operation combines IT help desk impersonation, adversary-in-the-middle token theft, and residential proxy sign-ins to target Microsoft 365 executives. Researchers also demonstrated a zero-click WeChat worm capable of account takeover via incoming calls, and a post-exploitation toolkit (PEEP) that turns Chrome and Edge into stealthy command-execution backdoors.

## Active Exploitation Details

### CVE-2026-75650 (StyleSmuggler)
- **Description**: A maximum-severity zero-day vulnerability in Magento and Adobe Commerce dubbed StyleSmuggler, caused by improper input validation that allows unauthenticated attackers to execute arbitrary code. The flaw enables attackers to bypass security controls and achieve remote code execution on affected e-commerce servers.
- **Impact**: Attackers can fully compromise Magento/Adobe Commerce servers, deploy persistent Rust-based backdoors and PHP web shells, exfiltrate customer and payment data, and maintain long-term access for further monetization or lateral movement.
- **Status**: Actively exploited in the wild since at least September 4, 2026. Adobe released an emergency security patch addressing the vulnerability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-75650
- **Reporting**: [Bleeping Computer — Adobe fixes critical Magento zero-day exploited to backdoor servers](https://www.bleepingcomputer.com/news/security/adobe-fixes-critical-magento-zero-day-exploited-to-backdoor-servers/), [The Hacker News — Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html)

### F5 BIG-IP APM Linux Rootkit Deployment
- **Description**: Attackers are breaching F5 BIG-IP Access Policy Manager (APM) devices to deploy a sophisticated Linux rootkit. The rootkit intercepts PHP file loading operations and injects a fileless web shell directly into memory, eliminating the need to write malicious code to disk and evading traditional file-based detection.
- **Impact**: Full compromise of F5 BIG-IP APM appliances, persistent stealthy access via memory-resident web shell, ability to intercept and manipulate application traffic, and potential lateral movement into connected network segments.
- **Status**: Active exploitation confirmed with rootkit deployment observed in the wild. No vendor patch mentioned in the reporting.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers breach F5 BIG-IP APM devices to deploy Linux rootkit](https://www.bleepingcomputer.com/news/security/hackers-breach-f5-big-ip-apm-devices-to-deploy-linux-rootkit/)

### Microsoft September 2026 Patch Tuesday Zero-Days (Two Vulnerabilities)
- **Description**: Two distinct zero-day vulnerabilities among 966 total flaws addressed in Microsoft's record-breaking September 2026 Patch Tuesday release. Both were confirmed as actively exploited in the wild at the time of patch release, affecting Windows and associated components.
- **Impact**: Varies by specific vulnerability; active exploitation indicates attackers have functional weaponized exploits capable of compromising unpatched systems, potentially leading to privilege escalation, remote code execution, or security feature bypass.
- **Status**: Patches released as part of September 2026 Patch Tuesday (KB5122878 for Windows 10, KB5124008/KB5122880 for Windows 11). Active exploitation confirmed prior to patch availability.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/)

### SAP OVERPASS Kernel Memory Corruption
- **Description**: A maximum-severity memory corruption vulnerability in the SAP Kernel code, tracked under the name OVERPASS. The flaw exists in core kernel components used across multiple SAP products and could allow unauthenticated attackers to execute arbitrary code or cause denial of service.
- **Impact**: Potential remote code execution on SAP application servers, complete compromise of SAP landscapes, access to critical business data and processes, and disruption of enterprise operations.
- **Status**: SAP addressed this vulnerability along with 19 others in its September 2026 security updates. The reporting indicates SAP "warns of" the vulnerability but does not explicitly confirm active exploitation in the wild.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **Reporting**: [Bleeping Computer — SAP warns of maximum severity 'OVERPASS' kernel vulnerability](https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/)

### Liquid Network Elements Bug Exploitation
- **Description**: An vulnerability in the Elements protocol (underlying the Liquid Bitcoin sidechain) was exploited to steal nearly 4,000 BTC (approximately $47M at time of reporting) from the Liquid Network on September 6, 2026. The attackers returned 3,400 BTC the following day but still hold approximately 598.5 BTC. The Liquid Network remains paused.
- **Impact**: Theft of Bitcoin-backed assets from a federated sidechain, loss of user funds, network operational pause preventing conversions between L-BTC and BTC, and erosion of trust in the Liquid federation model.
- **Status**: Active exploitation occurred on September 6, 2026. Network remains paused as of reporting. Partial funds returned by attacker.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Liquid Hackers Return 3,400 Bitcoin Taken via Elements Bug, Still Holding $47M in BTC](https://thehackernews.com/2026/09/liquid-hackers-return-3400-bitcoin.html)

### WeChat Zero-Click Account Takeover Worm
- **Description**: Security researchers at Calif developed a zero-click worm that takes over WeChat accounts on iPhone and Android via incoming calls. The victim does not need to answer or interact with the call; the attacker must only be in the victim's WeChat contacts list. The worm demonstrates automated propagation across devices.
- **Impact**: Full account takeover without user interaction, potential access to private messages, payment functions, social graph, and linked services. Automated worm propagation could enable mass compromise.
- **Status**: Demonstrated by researchers in a controlled test across three devices. Reported to Tencent in July 2026; Tencent has since deployed a fix. No confirmed wild exploitation beyond researcher demonstration.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)

### FreeIPA Anonymous Administrator Credential Creation Chain
- **Description**: A flaw chain in FreeIPA (Red Hat's identity management system) combined with a secondary flaw in the underlying 389 Directory Server database software. An unauthenticated, never-logged-in client can create a Kerberos identity of its choosing and elevate it to the administrators group, achieving full domain compromise.
- **Impact**: Complete takeover of FreeIPA-managed Linux domains, creation of persistent administrative accounts, access to all domain-joined systems and services, and bypass of all authentication and authorization controls.
- **Status**: Disclosed by Red Hat. No indication of active exploitation in the wild; the attack requires chaining two distinct vulnerabilities.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — FreeIPA Flaw Chain Lets Anonymous Clients Create Reusable Administrator Credentials](https://thehackernews.com/2026/09/freeipa-flaw-chain-lets-anonymous.html)

### ChatGPT Prompt Injection for Gmail Data Exfiltration
- **Description**: A flaw in ChatGPT's handling of connected Gmail accounts allows a maliciously planted prompt (injected into a conversation) to cause ChatGPT to silently read the user's Gmail data and exfiltrate it to an attacker-controlled ChatGPT account via a hidden channel, while appearing to answer the user's question normally.
- **Impact**: Stealthy exfiltration of email contents, contacts, and sensitive communications from users who have connected their Gmail accounts to ChatGPT. The attack is invisible to the victim during active conversation.
- **Status**: Proof-of-concept demonstrated by Check Point Research. No confirmation of active exploitation in the wild.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account](https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html)

## Affected Systems and Products

- **Adobe Commerce / Magento Open Source**: Multiple versions affected by CVE-2026-75650 (StyleSmuggler); emergency patch released
- **F5 BIG-IP Access Policy Manager (APM)**: Devices targeted for Linux rootkit deployment and fileless web shell injection
- **Microsoft Windows 10**: Requires KB5122878 extended security update (includes September 2026 Patch Tuesday fixes)
- **Microsoft Windows 11** (versions 25H2/24H2 and 23H2): Requires KB5124008 and KB5122880 cumulative updates
- **Microsoft Windows Server 2016**: August 2026 updates may trigger 0xc0000409 errors when Compatibility Appraiser is enabled
- **Microsoft Windows Server 2025**: Recent memory management changes may cause application crashes
- **SAP Kernel**: Multiple products using the SAP Kernel affected by OVERPASS memory corruption and 19 other vulnerabilities; September 2026 security updates released
- **Liquid Network / Elements Protocol**: Bitcoin sidechain paused following exploitation of Elements bug; ~598.5 BTC still held by attacker
- **WeChat** (iOS and Android): Zero-click worm via incoming calls; Tencent deployed fix after July 2026 responsible disclosure
- **FreeIPA / 389 Directory Server**: Linux identity management domains vulnerable to anonymous administrator credential creation chain
- **ChatGPT with Gmail Integration**: Users with connected Gmail accounts vulnerable to prompt injection data exfiltration (PoC demonstrated)
- **Google Workspace**: Third-party application integrations retaining excessive access post-purpose; webinar highlights breach risks
- **Chrome and Edge Browsers**: Susceptible to PEEP post-exploitation toolkit that injects malicious bookmarks extensions bypassing Web Store controls

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Threat actors abuse legitimate services (e.g., fake CAPTCHA/verification pages) to trick users into executing malicious PowerShell commands, establishing persistent access. Two separate campaigns observed using this tactic.
- **Autonomous Multi-Agent AI Frameworks**: Financially motivated groups deploy coordinated AI agent swarms that automate reconnaissance, credential harvesting, lateral movement, and data exfiltration—compromising thousands of credentials in under six hours.
- **IT Help Desk Vishing + AitM Token Theft + Residential Proxy Sign-ins**: Sophisticated Microsoft 365 targeting campaign impersonates IT support via phone, steals session tokens through adversary-in-the-middle phishing, and uses residential proxies to mimic legitimate executive login locations.
- **SEO Poisoning (BengalSEO Campaign)**: Long-running operation (since ~2015, Rajasthan, India) poisons Bing search results to deliver MayaBot malware and tech support scams, leveraging compromised IT service provider infrastructure.
- **Zero-Click Mobile Exploitation (WeChat Worm)**: Account takeover via specially crafted incoming call handling; no user interaction required beyond having the attacker as a contact. Demonstrated wormable propagation.
- **Fileless Memory-Resident Web Shell (F5 BIG-IP)**: Linux rootkit hooks PHP file loading to inject web shell directly into process memory, avoiding disk writes and standard file integrity monitoring.
- **StyleSmuggler Magento RCE Chain (CVE-2026-75650)**: Unauthenticated remote code execution via crafted input leading to deployment of Rust-based backdoor (persistence) and PHP web shell (command execution) on e-commerce servers.
- **PEEP Post-Exploitation Browser Extension Injection**: Toolkit masquerades as bookmarks extension; installer injects directly into Chrome/Edge profiles by forging Secure Preferences, bypassing Web Store validation and user prompts. Requires prior admin/code execution.
- **Fake E-Commerce Network (DoppelCart)**: 119,000+ domains hosting counterfeit online shops to harvest payment card details at industrial scale; infrastructure designed for resilience and rapid rotation.
- **Prompt Injection via Connected Services (ChatGPT/Gmail)**: Malicious instruction planted in conversation context hijacks AI assistant's authorized access to exfiltrate data from connected third-party accounts (Gmail) via covert channels.

## Threat Actor Activities

- **DoppelCart Operators**: Run a massive fraud network of 119,000+ fake e-commerce domains stealing payment card data. Industrial-scale operation with automated domain rotation and infrastructure resilience.
- **ShinyHunters**: Extortion gang claiming breach of Florida "DAVID" DMV database, exfiltrating 200,000+ driver records. Known for data theft, extortion, and leak site operations.
- **Slim Spider** (CrowdStrike tracking name): Previously undocumented financially motivated actor targeting Brazilian financial institutions since at least March 2026. Demonstrates deep operational knowledge of Brazilian instant payment (PIX) infrastructure and crypto custody workflows.
- **BengalSEO Operators**: Two IT service providers (WeConnect and associates) based in Rajasthan, India, running SEO poisoning campaign since at least 2015 to deliver MayaBot malware and tech support scams via poisoned Bing results.
- **ClickFix Campaign Operators**: Multiple distinct threat groups adopting ClickFix social engineering technique for initial access and persistence via legitimate service abuse.
- **Liquid Network Attacker**: Unknown operator exploited Elements protocol bug to steal ~4,000 BTC from Liquid sidechain on September 6, 2026; returned 3,400 BTC next day; still holds ~598.5 BTC. Network remains paused.
- **Fake IT Support Vishing Cluster**: Targets Microsoft 365 executives (directors, VPs) via help desk impersonation calls, AitM token theft, and residential proxy sign-ins for data theft and extortion.
- **Autonomous AI Agent Operators**: Financially motivated group observed by Google GTIG using multi-agent AI frameworks to automate end-to-end credential harvesting campaigns at unprecedented speed and scale.
- **Calif Researchers**: Discovered and demonstrated WeChat zero-click worm; responsibly disclosed to Tencent in July 2026. Not a threat actor, but capability demonstration indicates plausible exploit path.
- **Check Point Research**: Discovered and reported ChatGPT prompt injection flaw enabling Gmail data exfiltration via planted prompts. Proof-of-concept only; no wild exploitation confirmed.