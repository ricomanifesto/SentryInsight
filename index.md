---
schema_version: 2
report_date: 2026-09-08
generated_at: 2026-09-08T16:26:24Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-08/
---
# Exploitation Report

## Executive Summary

Adobe Commerce and Magento Open Source are under active exploitation via a maximum-severity zero-day vulnerability tracked as CVE-2026-75650 (StyleSmuggler), which has been weaponized since early September 2026 to deploy Rust-based backdoors and PHP web shells on compromised e-commerce servers. Sansec discovered the exploitation campaign, and Adobe released emergency patches addressing the CVSS 10.0 flaw across all supported versions.

Simultaneously, threat actors are operationalizing autonomous AI agent frameworks to conduct large-scale credential harvesting at unprecedented speed, with Google Threat Intelligence Group observing a financially motivated group compromising thousands of credentials in under six hours. These AI-driven campaigns complement established phishing-as-a-service operations like BigBear 2.0, which has bypassed multi-factor authentication at 258 organizations and stolen over 5,000 Microsoft 365 credentials through adversary-in-the-middle token theft and residential proxy infrastructure.

Multiple zero-click and low-interaction attack vectors have emerged across messaging and communication platforms. A WeChat zero-click worm demonstrated account takeover via incoming calls on both iOS and Android without user interaction, while a ChatGPT prompt injection flaw allowed planted instructions to exfiltrate connected Gmail data to attacker-controlled accounts. In the remote access space, rogue ConnectWise ScreenConnect clients are spreading worm-like VBScript payloads to newly connected hosts through diverse initial access vectors including tech-support scams and phishing-delivered installers.

## Active Exploitation Details

### Adobe Commerce and Magento StyleSmuggler Zero-Day (CVE-2026-75650)
- **Description**: A maximum-severity zero-day vulnerability in Adobe Commerce and Magento Open Source dubbed "StyleSmuggler" that allows unauthenticated remote code execution. The flaw resides in the handling of style/layout XML processing and was discovered being actively exploited in the wild starting September 4, 2026.
- **Impact**: Attackers achieve full server compromise, deploying persistent Rust-based backdoors and PHP web shells that provide ongoing remote access to e-commerce infrastructure, enabling data theft, payment skimming, and lateral movement.
- **Status**: Actively exploited since September 4, 2026. Adobe released emergency security patches addressing the vulnerability across all affected versions of Adobe Commerce and Magento Open Source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-75650
- **Reporting**: [Bleeping Computer — Adobe fixes critical Magento zero-day exploited to backdoor servers](https://www.bleepingcomputer.com/news/security/adobe-fixes-critical-magento-zero-day-exploited-to-backdoor-servers/), [The Hacker News — Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html), [Bleeping Computer — Magento StyleSmuggler zero-day exploited to deploy Linux backdoor](https://www.bleepingcomputer.com/news/security/magento-stylesmuggler-zero-day-exploited-to-deploy-linux-backdoor/)

### Liquid Network Elements Bug Exploitation
- **Description**: An exploitation of a vulnerability in the Elements sidechain protocol underlying the Liquid Network, a Bitcoin layer-2 solution. Attackers stole approximately 4,000 BTC (valued at roughly $47M at time of reporting) from the network on September 6, 2026.
- **Impact**: Direct theft of Bitcoin backing the L-BTC token. The network was paused, preventing holders from converting L-BTC back to Bitcoin. Approximately 3,400 BTC was subsequently returned by the attackers, leaving ~598.5 BTC still unaccounted for.
- **Status**: Exploitation occurred September 6, 2026. Liquid Network remains paused. No patch information provided in source articles.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Liquid Hackers Return 3,400 Bitcoin Taken via Elements Bug, Still Holding $47M in BTC](https://thehackernews.com/2026/09/liquid-hackers-return-3400-bitcoin.html)

### WeChat Zero-Click Account Takeover Worm
- **Description**: A zero-click worm targeting WeChat on iOS and Android that achieves account takeover via an incoming call. The victim does not need to answer or interact with the call; the only requirement is that the caller is already a WeChat contact. Researchers at Calif demonstrated the worm spreading among test devices and reported the flaw to Tencent in July 2026.
- **Impact**: Full account compromise without user interaction, enabling message interception, contact harvesting, and potential further social engineering. The worm capability allows automatic propagation through the victim's contact list.
- **Status**: Demonstrated by researchers; reported to Tencent in July 2026. Tencent has since addressed the vulnerability per researcher statements.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)

### ChatGPT Prompt Injection Gmail Data Exfiltration
- **Description**: A prompt injection vulnerability in ChatGPT where a single planted instruction in a conversation causes the model to silently exfiltrate data from the user's connected Gmail account and pass it to a second attacker-controlled ChatGPT account through a hidden channel, while appearing to answer the user's question normally.
- **Impact**: Unauthorized access to email content, contacts, and potentially sensitive communications from connected Google accounts. The attack is stealthy, leaving no visible indication to the victim.
- **Status**: Proof-of-concept demonstrated by Check Point Research. No indication of active exploitation in the wild provided in source articles.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account](https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html)

### FreeIPA Flaw Chain for Anonymous Administrator Credential Creation
- **Description**: A vulnerability chain in FreeIPA (Red Hat's identity management system built on 389 Directory Server) that allows an unauthenticated client to create a Kerberos identity of its choosing in the directory and gain membership in the administrators group. The attack requires chaining a FreeIPA flaw with a second vulnerability in the underlying 389 Directory Server database software.
- **Impact**: Full domain compromise in Linux environments using FreeIPA for centralized authentication, allowing attackers to create persistent administrative accounts without any prior credentials.
- **Status**: Disclosed by Red Hat. No information on active exploitation or patch availability provided in source articles.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — FreeIPA Flaw Chain Lets Anonymous Clients Create Reusable Administrator Credentials](https://thehackernews.com/2026/09/freeipa-flaw-chain-lets-anonymous.html)

### Telerik UI Padding Oracle Chain to Unauthenticated RCE
- **Description**: A proof-of-concept exploit chain published by TantoSec that transforms an AES-CBC padding oracle vulnerability in Telerik UI for ASP.NET AJAX into unauthenticated remote code execution. The chain only works against applications in a specific non-default configuration.
- **Impact**: Unauthenticated remote code execution on vulnerable ASP.NET applications using Telerik UI components in the affected configuration.
- **Status**: Public exploit released by TantoSec. Progress patched the vulnerability chain in July 2026. No confirmed reports of exploitation in the wild.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **Reporting**: [The Hacker News — Telerik UI Padding-Oracle Bug Chained to Unauthenticated RCE — Public Exploit Released](https://thehackernews.com/2026/09/telerik-ui-padding-oracle-bug-chained.html)

### SAP Kernel OVERPASS Memory Corruption Vulnerability
- **Description**: A maximum-severity memory corruption flaw in the SAP Kernel code, addressed as part of SAP's September 2026 security updates which fixed 20 vulnerabilities across multiple products.
- **Impact**: Potential remote code execution or denial of service in SAP systems running vulnerable kernel versions, affecting core enterprise business processes.
- **Status**: Patched in September 2026 SAP security updates. No information on active exploitation provided in source articles.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — SAP warns of maximum severity 'OVERPASS' kernel vulnerability](https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/)

### Rogue ScreenConnect VBScript Worm Distribution
- **Description**: Worm-like activity abusing ConnectWise ScreenConnect remote access software to distribute a four-stage VBScript payload to newly connected systems. The campaign uses diverse initial access methods including Quick Assist tech-support scams, phishing-delivered MSI installers, and fake software updates.
- **Impact**: Automated lateral movement and payload deployment across ScreenConnect-connected environments, enabling persistent access, credential theft, and further compromise.
- **Status**: Active campaign observed by Huntress across three unrelated incidents. No patch information for ScreenConnect itself provided; mitigation relies on blocking initial access vectors.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Rogue ScreenConnect Clients Spread Four-Stage VBScript Chain to Newly Connected Hosts](https://thehackernews.com/2026/09/rogue-screenconnect-clients-spread-four.html)

## Affected Systems and Products

- **Adobe Commerce / Magento Open Source**: All versions affected by CVE-2026-75650 (StyleSmuggler); emergency patches released
- **Liquid Network / Elements Sidechain**: Bitcoin layer-2 protocol; network paused following exploitation
- **WeChat (iOS and Android)**: Mobile messaging application; zero-click worm demonstrated; Tencent has addressed per researchers
- **ChatGPT with Gmail Integration**: OpenAI's chatbot platform when connected to Google Workspace/Gmail; prompt injection flaw demonstrated
- **FreeIPA / Red Hat Identity Management**: Linux domain identity management system using 389 Directory Server; flaw chain allows anonymous admin creation
- **Telerik UI for ASP.NET AJAX**: Specific non-default configurations vulnerable to padding oracle chain; patched by Progress in July 2026
- **SAP Kernel**: Core component across multiple SAP products; maximum-severity memory corruption flaw patched in September 2026 updates
- **ConnectWise ScreenConnect**: Remote access software abused for worm-like VBScript distribution; initial access via tech-support scams, phishing MSI, fake updates
- **Microsoft 365**: Targeted by BigBear 2.0 phishing-as-a-service (258 organizations, 5,000+ credentials) and executive-focused vishing/AitM campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation of E-Commerce Platforms**: Attackers leveraging CVE-2026-75650 (StyleSmuggler) in Adobe Commerce/Magento for initial access and persistent backdoor deployment via Rust implants and PHP web shells
- **AI-Driven Autonomous Credential Harvesting**: Multi-agent AI frameworks automating reconnaissance, phishing, credential validation, and exfiltration at scale (thousands of credentials in under six hours)
- **Phishing-as-a-Service with MFA Bypass**: BigBear 2.0 framework using adversary-in-the-middle (AitM) token theft and residential proxy infrastructure to defeat multi-factor authentication
- **Zero-Click Mobile Exploitation**: WeChat worm achieving account takeover via incoming call handling without user interaction on both iOS and Android
- **Prompt Injection for Data Exfiltration**: Planted instructions in ChatGPT conversations causing silent Gmail data extraction to attacker-controlled accounts
- **Executive-Targeted Vishing and AitM**: Fake IT help desk calls combined with adversary-in-the-middle token theft and residential proxy sign-ins targeting directors and VPs
- **SEO Poisoning for Malware Delivery**: BengalSEO campaign poisoning Bing search results since 2015 to deliver MayaBot malware and tech support scams
- **Worm-Like Remote Access Tool Abuse**: Rogue ScreenConnect clients automatically distributing multi-stage VBScript payloads to newly connected hosts
- **Padding Oracle to RCE Exploit Chain**: Telerik UI AES-CBC padding oracle chained to unauthenticated remote code execution in specific configurations
- **Post-Exploitation Browser Toolkits**: PEEP framework masquerading as bookmarks extension to turn Chrome/Edge into persistent command execution backdoors (requires prior admin access)

## Threat Actor Activities

- **Financially Motivated AI-Enabled Credential Harvesting Group**: Observed by Google Threat Intelligence Group (GTIG) deploying autonomous multi-agent attack frameworks to compromise thousands of credentials in under six hours; diverse motivations noted across observed attackers
- **BigBear 2.0 Phishing-as-a-Service Operators**: Operating a mature PhaaS platform that has bypassed MFA at 258 organizations and stolen over 5,000 Microsoft 365 credentials using AitM techniques and residential proxy infrastructure
- **Executive-Targeted Data Theft and Extortion Cluster**: Conducting widespread Microsoft 365 and SaaS targeting through IT help desk vishing, AitM token theft, and residential proxy sign-ins, primarily focusing on directors, VPs, and executive staff
- **BengalSEO Campaign Operators**: Long-running (since at least 2015) SEO poisoning operation based in Rajasthan, India, operated by two IT service providers (WeConnect and associates), delivering MayaBot malware and tech support scams via poisoned Bing search results
- **Liquid Network Attackers**: Unknown actors who exploited the Elements sidechain bug to steal ~4,000 BTC, subsequently returning 3,400 BTC while retaining ~598.5 BTC; network remains paused
- **ScreenConnect Worm Operators**: At least three unrelated incident clusters using diverse initial access (Quick Assist scams, phishing MSI, fake updates) to deploy rogue ScreenConnect clients that spread VBScript payloads worm-style
- **Sansec Researchers**: Discovered and reported the StyleSmuggler (CVE-2026-75650) zero-day exploitation in Magento/Adobe Commerce starting September 4, 2026
- **Calif Security Researchers**: Developed and demonstrated the WeChat zero-click worm, reported to Tencent in July 2026
- **Check Point Research**: Discovered and reported the ChatGPT prompt injection flaw enabling Gmail data exfiltration
- **TantoSec**: Published proof-of-concept exploit chain for Telerik UI padding oracle to unauthenticated RCE; Progress patched in July 2026
- **Huntress**: Disclosed the rogue ScreenConnect VBScript worm campaign across three incidents