---
schema_version: 2
report_date: 2026-09-09
generated_at: 2026-09-09T04:04:58Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-09/
---
# Exploitation Report

## Executive Summary

Microsoft's September 2026 Patch Tuesday set a historic record with 966 to 974 vulnerabilities addressed, including two actively exploited zero-days. While specific CVE identifiers for the Microsoft zero-days were not disclosed in the reporting, Microsoft confirmed active exploitation of two flaws and identified an additional 58 vulnerabilities as more likely to be exploited. This unprecedented patch volume, accelerated by AI-assisted vulnerability discovery, creates significant operational challenges for organizations testing and deploying fixes.

Adobe issued an emergency patch for CVE-2026-75650 (StyleSmuggler), a maximum-severity (CVSS 10.0) zero-day in Magento and Adobe Commerce that has been under active exploitation since September 4, 2026. Attackers are deploying Rust-based backdoors and PHP web shells to compromise e-commerce servers. Simultaneously, multiple threat actors are leveraging AI-driven frameworks—including autonomous multi-agent systems—to conduct large-scale credential harvesting, phishing via Google service redirects, and social engineering campaigns such as ClickFix that abuse legitimate services for persistent access.

Notable targeted intrusions include the Slim Spider group stealing crypto custody secrets from Brazilian financial institutions, ShinyHunters claiming a breach of Florida's DAVID DMV database with over 200,000 driver records, and a Linux rootkit campaign compromising F5 BIG-IP APM devices with fileless web shells. A zero-click WeChat worm exploiting incoming call handling on iOS and Android, a FreeIPA flaw chain enabling anonymous administrator credential creation, and SAP's maximum-severity OVERPASS kernel vulnerability further expand the active threat landscape.

## Active Exploitation Details

### CVE-2026-75650 (StyleSmuggler) — Adobe Magento/Adobe Commerce Zero-Day
- **Description**: A maximum-severity zero-day vulnerability in Adobe Commerce and Magento Open Source, codenamed StyleSmuggler by Sansec researchers. The flaw allows unauthenticated attackers to achieve remote code execution on affected e-commerce servers.
- **Impact**: Attackers can fully compromise Magento/Adobe Commerce servers, deploy persistent backdoors (including Rust-based implants and PHP web shells), exfiltrate customer and payment data, and establish long-term access for further lateral movement.
- **Status**: Actively exploited in the wild since September 4, 2026. Adobe released emergency security patches on September 8, 2026 addressing the vulnerability across multiple product versions.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-75650
- **Reporting**: [Bleeping Computer — Adobe fixes critical Magento zero-day exploited to backdoor servers](https://www.bleepingcomputer.com/news/security/adobe-fixes-critical-magento-zero-day-exploited-to-backdoor-servers/), [The Hacker News — Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html)

### Microsoft September 2026 Patch Tuesday — Two Actively Exploited Zero-Days
- **Description**: Microsoft's record-breaking September 2026 Patch Tuesday addressed 966–974 vulnerabilities across Windows and other products. Microsoft confirmed that two of these vulnerabilities are actively exploited zero-days, with an additional 58 vulnerabilities assessed as more likely to be exploited.
- **Impact**: Successful exploitation of the two zero-days could allow attackers to achieve remote code execution, elevation of privilege, or security feature bypass on affected Windows systems. The specific impact varies by vulnerability class.
- **Status**: Patches released as part of September 2026 Patch Tuesday (KB5122878 for Windows 10, KB5124008/KB5122880 for Windows 11). Active exploitation confirmed by Microsoft; specific CVE identifiers not disclosed in public reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Krebs on Security — Microsoft Plugs Nearly 1,000 Security Holes](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/), [Dark Reading — Patch Tuesday Sets Another Record With 974 CVEs](https://www.darkreading.com/vulnerabilities-threats/patch-tuesday-another-record-974-cves), [Bleeping Computer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/), [Bleeping Computer — Microsoft releases Windows 10 KB5122878 extended security update](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-10-kb5122878-extended-security-update/), [Bleeping Computer — Windows 11 cumulative updates KB5124008 & KB5122880 released](https://www.bleepingcomputer.com/news/microsoft/windows-11-cumulative-updates-kb5124008-and-kb5122880-released/)

### SAP OVERPASS Kernel Vulnerability
- **Description**: A maximum-severity memory corruption flaw in the SAP Kernel code, tracked under the name OVERPASS. SAP addressed this vulnerability along with 19 others in its September 2026 security updates.
- **Impact**: Memory corruption in the SAP Kernel could allow unauthenticated attackers to execute arbitrary code with kernel-level privileges, potentially leading to complete compromise of SAP application servers and underlying business data.
- **Status**: Patches released in SAP September 2026 security updates. No public evidence of active exploitation reported, but maximum severity rating indicates high risk.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [Bleeping Computer — SAP warns of maximum severity 'OVERPASS' kernel vulnerability](https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/)

### F5 BIG-IP APM Linux Rootkit Campaign
- **Description**: Threat actors are actively breaching F5 BIG-IP Access Policy Manager (APM) devices to deploy a sophisticated Linux rootkit. The rootkit intercepts PHP file loading and injects a fileless web shell directly into memory, avoiding disk writes to evade detection.
- **Impact**: Attackers gain persistent, stealthy access to F5 BIG-IP APM appliances, enabling traffic interception, credential harvesting, lateral movement into internal networks, and long-term foothold maintenance without leaving traditional forensic artifacts.
- **Status**: Active exploitation confirmed. F5 has not been reported to have released a specific patch in the provided articles; organizations should consult F5 security advisories.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers breach F5 BIG-IP APM devices to deploy Linux rootkit](https://www.bleepingcomputer.com/news/security/hackers-breach-f5-big-ip-apm-devices-to-deploy-linux-rootkit/)

### FreeIPA Flaw Chain — Anonymous Administrator Credential Creation
- **Description**: A vulnerability chain in FreeIPA (Red Hat's identity management system) allows an unauthenticated, never-logged-in client to create a Kerberos identity of its choosing in the directory and escalate to the administrators group. The attack requires a second flaw in the underlying 389 Directory Server (LDAP database).
- **Impact**: Complete compromise of the FreeIPA identity domain. Attackers can create arbitrary administrator accounts, access all domain resources, modify policies, and persist indefinitely with legitimate credentials.
- **Status**: Vulnerability disclosed by Red Hat. No CVE identifiers provided in reporting. Patch status not specified in articles.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — FreeIPA Flaw Chain Lets Anonymous Clients Create Reusable Administrator Credentials](https://thehackernews.com/2026/09/freeipa-flaw-chain-lets-anonymous.html)

### WeChat Zero-Click Worm (iOS/Android)
- **Description**: A zero-click worm demonstrated by researchers at Calif that takes over WeChat accounts via an incoming call on both iPhone and Android. The victim does not need to answer or interact with the call; the caller must be a WeChat contact. The worm spreads automatically among contacts.
- **Impact**: Full account takeover of WeChat users, potential access to messages, contacts, payment features, and social graph. Wormable propagation enables rapid, large-scale compromise.
- **Status**: Researchers reported the flaw to Tencent in July 2026; Tencent has since addressed it. No CVE identifier provided in reporting.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)

### ChatGPT Prompt Injection — Gmail Data Exfiltration
- **Description**: A flaw in ChatGPT's handling of connected Gmail accounts allows a single planted instruction in a conversation to cause ChatGPT to silently read data from the user's Gmail and exfiltrate it to an attacker-controlled ChatGPT account via a hidden channel, while appearing to answer the user's question normally.
- **Impact**: Unauthorized access to victim's Gmail data including emails, contacts, and potentially sensitive documents. The attack is stealthy and does not require user interaction beyond engaging with a compromised conversation.
- **Status**: Proof-of-concept demonstrated by Check Point Research. OpenAI response not detailed in reporting. No CVE identifier provided.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account](https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html)

## Affected Systems and Products

- **Adobe Commerce / Magento Open Source**: Multiple versions affected by CVE-2026-75650 (StyleSmuggler); emergency patches released September 8, 2026
- **Microsoft Windows 10**: All supported versions; KB5122878 extended security update includes September 2026 Patch Tuesday fixes
- **Microsoft Windows 11**: Versions 25H2/24H2 and 23H2; KB5124008 and KB5122880 cumulative updates
- **Microsoft Windows Server 2016**: August 2026 updates may trigger 0xc0000409 errors when Compatibility Appraiser diagnostic service is enabled
- **F5 BIG-IP Access Policy Manager (APM)**: Devices targeted by Linux rootkit campaign deploying fileless web shells
- **SAP Kernel**: Multiple SAP products affected by OVERPASS memory corruption flaw and 19 other vulnerabilities; September 2026 security updates released
- **FreeIPA / 389 Directory Server**: Red Hat identity management system and underlying LDAP database; flaw chain enables anonymous admin credential creation
- **WeChat (iOS and Android)**: Zero-click worm via incoming call handling; Tencent addressed after July 2026 disclosure
- **ChatGPT with Gmail Integration**: Connected Gmail accounts vulnerable to prompt injection data exfiltration
- **Google Services (Multi-hop Redirects)**: Multiple Google services abused for phishing credential harvesting and ScreenConnect remote access deployment

## Attack Vectors and Techniques

- **AI-Driven Autonomous Multi-Agent Attack Frameworks**: Financially motivated threat actors (observed by Google Threat Intelligence Group) deploying autonomous, multi-agent AI systems that automate every stage of credential harvesting campaigns, compromising thousands of credentials in under six hours.
- **Multi-Hop Google Service Redirects for Phishing**: Threat actors chaining multiple legitimate Google services (e.g., Google Sites, Google Docs, Google AMP) to evade URL filtering and reputation checks, ultimately harvesting credentials or deploying ScreenConnect remote access agents.
- **ClickFix Social Engineering**: Attackers abusing legitimate services and familiar UI patterns (fake CAPTCHAs, browser verification prompts) to trick users into executing malicious PowerShell commands, establishing persistent access.
- **Prompt Injection via Planted Instructions**: Malicious instructions embedded in ChatGPT conversations (shared links, imported contexts) that hijack the model's connected-tool behavior to exfiltrate data from integrated services (Gmail) via covert channels.
- **Fileless Linux Rootkit with In-Memory PHP Web Shell Injection**: Rootkit targeting F5 BIG-IP APM intercepts PHP file loading at runtime to inject web shell code directly into process memory, avoiding disk artifacts and traditional file-based detection.
- **Zero-Click Worm Propagation via Incoming Call Handling**: WeChat vulnerability triggered by receiving a call (no answer required) enabling automatic account takeover and wormable spread to the victim's contact list.
- **Kerberos/LDAP Identity Spoofing via Anonymous Binding**: FreeIPA flaw chain allowing unauthenticated clients to create arbitrary Kerberos principals in the directory and leverage a 389 Directory Server flaw to escalate to domain administrators.
- **Mass-Scale Fake E-Commerce Infrastructure (DoppelCart)**: 119,000+ domains operating as interconnected fake online shops to harvest payment card credentials at industrial scale.
- **Rust-Based Backdoor and PHP Web Shell Deployment**: Post-exploitation tooling deployed via CVE-2026-75650 (StyleSmuggler) on Magento servers, combining modern Rust implants for persistence with PHP web shells for web-accessible command execution.

## Threat Actor Activities

- **Slim Spider (CrowdStrike-tracked)**: Previously undocumented financially motivated threat actor targeting Brazilian financial institutions since at least March 2026. Demonstrates deep operational knowledge of Brazilian financial infrastructure, including the instant payment system (PIX), and focuses on stealing crypto custody secrets.
- **ShinyHunters**: Extortion gang claiming breach of Florida Department of Motor Vehicles "DAVID" database platform, alleging theft of over 200,000 driver records. Known for data theft and extortion campaigns against high-profile targets.
- **DoppelCart Operators**: Organized fraud network operating 119,000+ fake e-commerce domains to systematically harvest payment card data. Represents industrial-scale carding infrastructure.
- **F5 BIG-IP APM Rootkit Operators**: Unidentified threat actors deploying sophisticated Linux rootkits with fileless web shell injection on compromised F5 BIG-IP APM appliances. High technical capability suggesting advanced persistent threat or skilled cybercrime group.
- **Google GTIG-Observed AI Framework Operators**: Diverse threat actors (financially motivated and otherwise) leveraging multi-agent AI frameworks to automate credential harvesting, vulnerability research, and attack execution at scale.
- **ClickFix Campaign Operators**: Multiple threat actor groups adopting the ClickFix social engineering technique, abusing legitimate cloud services (GitHub, Cloudflare, etc.) for payload hosting and command-and-control to achieve persistent access.
- **Liquid Network Hackers**: Unidentified actors who exploited an "Elements Bug" in the Liquid Bitcoin sidechain to steal nearly 4,000 BTC on September 6, 2026; returned 3,400 BTC the following day but still hold approximately 598.5 BTC (~$47M). Liquid Network remains paused.