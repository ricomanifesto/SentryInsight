---
schema_version: 2
report_date: 2026-09-08
generated_at: 2026-09-08T11:46:39Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-08/
---
# Exploitation Report

## Executive Summary

A critical zero-day vulnerability in Magento and Adobe Commerce, tracked as CVE-2026-75650 and codenamed StyleSmuggler, has been actively exploited since September 4, 2026. With a maximum CVSS score of 10.0, this unauthenticated remote code execution flaw allows attackers to deploy Rust-based backdoors and PHP web shells on e-commerce servers. Adobe has released emergency patches, but the exploitation window began before fixes were available, putting all unpatched Magento Open Source and Adobe Commerce instances at immediate risk.

Simultaneously, multiple infrastructure-level attacks are underway. Threat actors are chaining two recently disclosed MikroTik RouterOS vulnerabilities to hijack routers with internet-exposed SSH services, achieving full administrative control without authentication. The N-able N-central RMM platform faces its fourth hotfix in five weeks for an unauthenticated RCE flaw that the vendor's incident notice confirms has been exploited in the wild. Additionally, a critical VMware Workstation and Fusion flaw (CVE-2026-59346, CVSS 9.3) enables VM administrators to break out and execute arbitrary code on the host, with patches now available from Broadcom.

On the identity and access front, a sophisticated Microsoft 365 campaign combining vishing, adversary-in-the-middle token theft, and residential proxy sign-ins is targeting executives at scale. The BigBear 2.0 phishing-as-a-service framework has bypassed MFA at 258 organizations, stealing over 5,000 credentials. Meanwhile, the REVSTEALER malware family deploys persistent modules that disable Windows Update and Defender to run cryptocurrency miners, and the JSCeal malware bypasses Google authentication using stolen session cookies. A massive SEO poisoning campaign (BengalSEO) continues to deliver malware via manipulated Bing search results, while over 5,400 compromised websites serve ClickFix payloads stored on the BNB Smart Chain blockchain.

## Active Exploitation Details

### Magento StyleSmuggler Zero-Day (CVE-2026-75650)
- **Description**: An unauthenticated remote code execution vulnerability in Adobe Commerce and Magento Open Source, codenamed StyleSmuggler by Sansec. The flaw allows attackers to execute arbitrary code on the server without authentication by exploiting improper input validation in style/layout processing components.
- **Impact**: Full server compromise enabling deployment of persistent backdoors (Rust-based Linux backdoor), PHP web shells, credit card skimmers, and complete control over e-commerce operations including customer data and payment processing.
- **Status**: Actively exploited in the wild since September 4, 2026. Adobe released security patches on September 8, 2026. All versions of Magento Open Source and Adobe Commerce are affected prior to patching.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-75650
- **Reporting**: [The Hacker News — Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html), [Bleeping Computer — Magento StyleSmuggler zero-day exploited to deploy Linux backdoor](https://www.bleepingcomputer.com/news/security/magento-stylesmuggler-zero-day-exploited-to-deploy-linux-backdoor/), [The Hacker News — Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores](https://thehackernews.com/2026/09/unpatched-magento-and-adobe-commerce.html)

### MikroTik RouterOS SSH Authentication Bypass Chain
- **Description**: A chain of two recently disclosed vulnerabilities in MikroTik RouterOS that allows unauthenticated attackers to gain full administrative control over devices with SSH services exposed to the internet. CERT Polska issued an attack warning on September 5, 2026, confirming successful attacks dating to at least September 2.
- **Impact**: Complete router compromise including traffic interception, network pivoting, DNS manipulation, VPN credential theft, and use as proxy infrastructure for further attacks.
- **Status**: Actively exploited in the wild. MikroTik has released patches for the underlying vulnerabilities. Devices with internet-accessible SSH remain at immediate risk until patched.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit new MikroTik RouterOS flaws to hijack routers](https://www.bleepingcomputer.com/news/security/hackers-exploit-new-mikrotik-routeros-flaws-to-hijack-routers/), [The Hacker News — Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html)

### N-able N-central Unauthenticated RCE
- **Description**: A maximum-severity unauthenticated remote code execution flaw in the N-central remote monitoring and management (RMM) platform. This is the fourth hotfix issued in five weeks (Hotfix 4 for build 2026.3.1.14), indicating persistent exploitation pressure and potential incomplete prior fixes.
- **Impact**: Full compromise of the RMM server and all managed endpoints, enabling supply-chain-style attacks against downstream customers, credential theft, and persistent network access.
- **Status**: N-able's incident notice states the flaw has been exploited in the wild, though release notes describe this as unconfirmed. Emergency Hotfix 4 released September 2026. All on-premises builds below 2026.3.1.14 are vulnerable.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw](https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html), [Bleeping Computer — N-able patches max severity N-central flaw amid ongoing attacks](https://www.bleepingcomputer.com/news/security/n-able-patches-max-severity-n-central-flaw-amid-ongoing-attacks/)

### VMware Workstation and Fusion VM Escape (CVE-2026-59346)
- **Description**: An integer-overflow vulnerability in VMware Workstation and Fusion that allows a local attacker with elevated privileges inside a virtual machine to execute arbitrary code on the host system. The flaw resides in the virtual hardware emulation layer.
- **Impact**: VM escape leading to host compromise, affecting all VMs on the host, potential access to host credentials, and lateral movement across virtualized environments.
- **Status**: Security updates released by Broadcom. No confirmed exploitation in the wild reported, but the critical severity and VM escape nature make it a high-value target.
- **Severity**: critical
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-59346
- **Reporting**: [The Hacker News — Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code](https://thehackernews.com/2026/09/critical-vmware-workstation-and-fusion.html)

### TeamCity Critical Vulnerability Exploitation at JetBrains
- **Description**: Attackers exploited a recently disclosed critical vulnerability in JetBrains TeamCity to breach the JetBrains Cadence environment and extract AWS credentials. JetBrains confirmed the incident and urged all Cadence users to immediately revoke and rotate credentials.
- **Impact**: Compromise of CI/CD infrastructure, theft of cloud credentials (AWS), potential supply chain contamination of build artifacts, and access to proprietary source code.
- **Status**: Confirmed exploitation against JetBrains' own environment. Patch status for the underlying TeamCity vulnerability not specified in reporting; credential rotation is the immediate required action.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials](https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html)

### Telerik UI Padding Oracle to RCE Chain
- **Description**: A padding oracle vulnerability in Telerik UI for ASP.NET AJAX (AES-CBC implementation) that can be chained to achieve unauthenticated remote code execution, but only against applications in a specific non-default configuration. Progress patched the vulnerability chain in July 2026. TantoSec released a public proof-of-concept exploit.
- **Impact**: Unauthenticated RCE on vulnerable web applications, potentially leading to server compromise and data theft.
- **Status**: Patched in July 2026. Public exploit available. No confirmed reports of exploitation in the wild per reporting.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — Telerik UI Padding-Oracle Bug Chained to Unauthenticated RCE — Public Exploit Released](https://thehackernews.com/2026/09/telerik-ui-padding-oracle-bug-chained.html)

### ConnectWise ScreenConnect Vulnerability (Unpatched)
- **Description**: A new vulnerability in ConnectWise ScreenConnect Remote Access software. ConnectWise has shared temporary mitigation measures and plans to release a patch. The flaw is being exploited in worm-like activity distributing malicious VBScript payloads.
- **Impact**: Remote access compromise, lateral movement via worm-like propagation to newly connected hosts, payload delivery (VBScript-based).
- **Status**: Unpatched as of reporting. Temporary mitigations available. Active exploitation confirmed via rogue ScreenConnect clients spreading four-stage VBScript chains.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Rogue ScreenConnect Clients Spread Four-Stage VBScript Chain to Newly Connected Hosts](https://thehackernews.com/2026/09/rogue-screenconnect-clients-spread-four.html), [Bleeping Computer — ConnectWise warns of new ScreenConnect flaw without patch](https://www.bleepingcomputer.com/news/security/connectwise-warns-of-new-screenconnect-flaw-without-patch/)

### BigBear 2.0 Microsoft 365 Phishing-as-a-Service
- **Description**: A phishing-as-a-service framework (BigBear 2.0) that bypasses multi-factor authentication using adversary-in-the-middle (AitM) techniques, residential proxy infrastructure, and token theft. Used against 258 organizations to steal over 5,000 Microsoft 365 credentials.
- **Impact**: Full account takeover despite MFA, access to email, SharePoint, Teams, and connected SaaS applications, business email compromise enablement, and data exfiltration.
- **Status**: Active campaign. No software patch applicable; requires identity and access defenses (phishing-resistant MFA, conditional access, token protection).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — BigBear Microsoft 365 phishing service bypassed MFA at 258 organizations](https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/)

### Executive Vishing and AitM Campaign (Microsoft 365/SaaS)
- **Description**: A widespread data theft and extortion operation targeting directors, vice presidents, and executive staff through IT help desk vishing (voice phishing), adversary-in-the-middle token theft, and residential-proxy sign-ins to bypass location-based controls.
- **Impact**: Executive account compromise, sensitive data theft, extortion, persistent SaaS access, and potential business email compromise propagation.
- **Status**: Active threat cluster. No patch applicable; requires executive protection programs, phishing-resistant authentication, and help desk verification procedures.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks](https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html)

### REVSTEALER Persistent Modules with Defense Evasion
- **Description**: Four previously undocumented programs associated with the REVSTEALER information stealer (ProManager, WinUpdate, SoftManager, and a fourth unnamed module) that persist after the stealer self-deletes. One module disables Windows Update and Microsoft Defender before executing a cryptocurrency miner.
- **Impact**: Persistent foothold, defense evasion (AV/Update disablement), resource hijacking (crypto mining), and potential re-infection vector.
- **Status**: Active malware family with novel persistence and defense evasion techniques documented by Elastic Security Labs.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Four REVSTEALER-Linked Modules Disable Windows Update and Defender to Run a Crypto Miner](https://thehackernews.com/2026/09/four-revstealer-linked-modules-disable.html)

### JSCeal Malware Google Authentication Bypass
- **Description**: A sophisticated compiled V8 JavaScript (JSC) malware with credential harvesting, surveillance, and traffic interception capabilities. It bypasses Google authentication using stolen session cookies, protected by javascript-obfuscator with RC4 strings, control-flow flattening, and proxy functions.
- **Impact**: Google account takeover via session hijacking, credential theft, browser surveillance, traffic interception, and persistent access without 2FA challenge.
- **Status**: Active malware with advanced obfuscation and authentication bypass capabilities documented by Check Point Research.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — JSCeal Malware Can Bypass Google Authentication Using Stolen Session Cookies](https://thehackernews.com/2026/09/jsceal-malware-can-bypass-google.html)

### PEEP Chromium Post-Exploitation Toolkit
- **Description**: A post-exploitation toolkit masquerading as a bookmarks extension for Chrome and Edge. Requires prior administrative or code execution access; its installer injects the extension directly into browser profiles by forging Chromium's Secure Preferences, bypassing Web Store checks and user prompts.
- **Impact**: Persistent browser compromise, host command execution, credential harvesting from browser stores, session hijacking, and stealthy command-and-control.
- **Status**: Toolkit disclosed by researchers. Requires initial access; not an initial access vulnerability. Detection and removal guidance needed.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — PEEP Turns Chrome and Edge Into Post-Compromise Backdoors for Host Command Execution](https://thehackernews.com/2026/09/peep-turns-chrome-and-edge-into-post.html)

### BengalSEO Poisoning Campaign
- **Description**: A long-running (since at least 2015) SEO poisoning campaign operating from Rajasthan, India, driven by two IT service providers. Manipulates Bing search results to deliver MayaBot malware and tech support scam pages.
- **Impact**: Malware delivery (MayaBot), tech support fraud, credential theft, and financial loss for victims redirected from legitimate search queries.
- **Status**: Active, sprawling campaign discovered by DFIR Report in March 2026. Infrastructure takedown and search engine cooperation needed.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — BengalSEO Poisons Bing Search Results to Deliver MayaBot and Tech Support Scams](https://thehackernews.com/2026/09/bengalseo-poisons-bing-search-results.html)

### ClickFix Blockchain-Hosted Payload Campaign
- **Description**: Over 5,400 compromised small-business websites serve ClickFix payloads stored in smart contracts on the BNB Smart Chain (BSC), leveraging blockchain infrastructure for resilient payload hosting.
- **Impact**: Malware delivery via social engineering (ClickFix), resilient C2/payload infrastructure resistant to traditional takedowns, widespread website compromise.
- **Status**: Active large-scale operation. Requires website remediation and blockchain monitoring.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Over 5,400 hacked sites serve ClickFix payloads stored on the blockchain](https://www.bleepingcomputer.com/news/security/over-5-400-hacked-sites-serve-clickfix-payloads-stored-on-the-blockchain/)

### ASCII Smuggling Phishing Technique
- **Description**: Threat actors using invisible Unicode characters (ASCII smuggling) to conceal phishing lures and evade email security filters. The technique embeds malicious content in visually benign messages.
- **Impact**: Email security bypass, increased phishing success rates, credential theft, and malware delivery.
- **Status**: Active technique adoption across phishing campaigns. No patch; requires email security rule updates and user awareness.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Attackers conceal phishing lures using invisible Unicode characters](https://www.bleepingcomputer.com/news/security/attackers-conceal-phishing-lures-using-invisible-unicode-characters/)

## Affected Systems and Products

- **Adobe Commerce / Magento Open Source**: All versions prior to September 2026 security patches (CVE-2026-75650)
- **MikroTik RouterOS**: Devices with SSH exposed to internet; patches available for the vulnerability chain
- **N-able N-central (on-premises)**: All builds below 2026.3.1.14 (requires Hotfix 4)
- **VMware Workstation and Fusion**: Versions prior to September 2026 security updates (CVE-2026-59346)
- **JetBrains TeamCity**: Versions affected by the recently disclosed critical vulnerability (specific versions not detailed in reporting)
- **Telerik UI for ASP.NET AJAX**: Applications using non-default configuration vulnerable to padding oracle chain; patched July 2026
- **ConnectWise ScreenConnect**: All versions pending patch; temporary mitigations published
- **Microsoft 365 / Entra ID**: Tenants targeted by BigBear 2.0 PhaaS and executive vishing/AitM campaigns
- **Google Workspace / Consumer Accounts**: Targets of JSCeal session cookie theft
- **Chrome and Edge Browsers**: Post-compromise targets for PEEP extension injection
- **Windows Endpoints**: Targets of REVSTEALER modules (Windows Update/Defender disablement, crypto mining)
- **Small Business Websites**: 5,400+ compromised sites serving ClickFix payloads via BNB Smart Chain
- **Bing Search Users**: Targets of BengalSEO poisoning delivering MayaBot and tech support scams
- **APIS (Advance Passenger Information System)**: Vietnam-linked database exposed via default credentials (220M records)
- **Mathspace Metabase Instance**: Breached internal reporting system (1M+ records exposed)
- **Trezor/ShipMonk**: Cryptocurrency hardware wallet customer data breach via logistics provider (81K customers)

## Attack Vectors and Techniques

- **Unauthenticated RCE via Input Validation Flaw**: StyleSmuggler exploits improper style/layout processing in Magento/Adobe Commerce for pre-auth code execution
- **SSH Authentication Bypass Chain**: Two MikroTik RouterOS flaws chained for full router takeover without credentials
- **RMM Supply Chain Exploitation**: Unauthenticated RCE in N-central RMM platform enabling downstream customer compromise
- **VM Escape via Integer Overflow**: Local VM admin leverages CVE-2026-59346 to execute host code from guest
- **CI/CD Credential Theft via TeamCity**: Exploited TeamCity vulnerability used to breach JetBrains Cadence and extract AWS credentials
- **Padding Oracle to RCE Chain**: Telerik UI AES-CBC padding oracle chained to unauthenticated RCE in specific configurations
- **Rogue RMM Client Propagation**: Malicious ScreenConnect clients worm-like spread VBScript payloads to new hosts
- **Adversary-in-the-Middle Phishing**: BigBear 2.0 and executive campaigns use AitM to bypass MFA and steal session tokens
- **Vishing (Voice Phishing)**: IT help desk impersonation targeting executives for credential and MFA bypass
- **Residential Proxy Sign-ins**: Attackers use residential IP infrastructure to bypass geo-location and risk-based conditional access
- **Session Cookie Theft for Auth Bypass**: JSCeal malware steals Google session cookies to bypass authentication including 2FA
- **Browser Extension Injection via Secure Preferences Forgery**: PEEP toolkit forges Chromium Secure Preferences to silently install malicious extensions
- **Defense Evasion via Service Disablement**: REVSTEALER modules disable Windows Update and Microsoft Defender before mining
- **SEO Poisoning for Malware Delivery**: BengalSEO manipulates Bing rankings to serve MayaBot and scam pages
- **Blockchain-Hosted Payloads**: ClickFix payloads stored in BNB Smart Chain smart contracts for resilient delivery
- **ASCII Smuggling / Invisible Unicode**: Phishing lures concealed using non-printing characters to evade email filters
- **Default Credential Exposure**: APIS database accessed via cloud path using default credentials (220M traveler records)
- **Internal Reporting System Breach**: Mathspace Metabase instance compromised for data exfiltration (1M+ records)
- **Supply Chain / Third-Party Breach**: Trezor customer data exposed via ShipMonk logistics provider breach

## Threat Actor Activities

- **Sansec (Researcher/Defender)**: Discovered and named StyleSmuggler zero-day; tracked exploitation from September 4, 2026; provided advisory and indicators
- **BengalSEO Operators**: Long-running (since ~2015) SEO poisoning group based in Rajasthan, India; operated by two IT service providers (WeConnect and unnamed); delivers MayaBot and tech support scams via Bing manipulation
- **BigBear PhaaS Operators**: Phishing-as-a-service framework (BigBear 2.0) used against 258 organizations; stole 5,000+ Microsoft 365 credentials via AitM and residential proxies
- **Executive Targeting Threat Cluster**: Unnamed group conducting vishing, AitM token theft, and residential proxy sign-ins against directors/VPs for data theft and extortion
- **REVSTEALER Developers/Operators**: Emerging Windows info-stealer family deploying four persistent post-exploitation modules (ProManager, WinUpdate, SoftManager) for defense evasion and crypto mining
- **JSCeal Malware Authors**: Sophisticated V8 JavaScript malware with heavy obfuscation (RC4, control-flow flattening); targets Google accounts via session cookie theft
- **ClickFix Campaign Operators**: Large-scale operation compromising 5,400+ small business websites; uses BNB Smart Chain smart contracts for payload hosting resilience
- **MikroTik Router Hijackers**: Unidentified actors exploiting RouterOS SSH chain; attacks observed from September 2, 2026 per CERT Polska
- **JetBrains Intruders**: Unidentified threat actors who exploited TeamCity to breach Cadence and extract AWS credentials
- **PEEP Toolkit Developers**: Created post-exploitation Chromium extension toolkit for stealthy browser persistence and host command execution
- **DFIR Report Researchers**: Discovered and documented BengalSEO campaign in March 2026
- **Elastic Security Labs**: Analyzed and documented four REVSTEALER-linked modules with defense evasion capabilities
- **Check Point Research**: Unpacked and analyzed JSCeal malware authentication bypass techniques
- **TantoSec**: Published proof-of-concept exploit chain for Telerik UI padding oracle to RCE
- **CERT Polska**: Issued attack warning for MikroTik router exploitation on September 5, 2026
- **Huntress**: Identified three unrelated incidents of rogue ScreenConnect client abuse with diverse initial access (Quick Assist scam, phishing MSI, fake...)