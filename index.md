---
schema_version: 2
report_date: 2026-08-17
generated_at: 2026-08-17T09:52:40Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-17/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, ranging from enterprise infrastructure to consumer devices. A global threat campaign is targeting a critical VMware vCenter flaw (CVE-2026-59310), while Microsoft addresses a Defender zero-day (CVE-2026-69414) and threat actors exploit a recently patched SharePoint authentication bypass (CVE-2026-55040) following public PoC release. North Korea's Lazarus Group has weaponized a Windows zero-day to deploy a novel backdoor against defense and aerospace targets in four countries as part of Operation Dream Job.

Simultaneously, financially motivated campaigns are escalating: a maximum-severity SAP Commerce Cloud RCE is being attacked within days of patch availability, the ShinyHunters extortion group breached 1.6 million RingCentral accounts, and Clop ransomware claims 89GB of data from Shell. The "City-Forum" campaign has conducted long-running data theft against Salesforce and ServiceNow since March 2025, while the Jewelbug APT blends state espionage with cryptocurrency theft. Mac users face active exploitation of a Screen Sharing authentication bypass to deploy Monero miners and a new ClickFix-delivered malware (AmnesiaStealer) with interactive browser control capabilities.

Infrastructure and supply chain attacks round out the threat landscape. A service provider vulnerability enabled €30M bank fraud against Commerzbank customers, leading to arrests in Brazil and Europe. A Mirai-based botnet (Evooo1Bot) is converting routers into SOCKS5 relay nodes, and 737 malicious Chrome VPN extensions with 75,000+ installs are intercepting browser traffic. Belgium's eID authentication framework was fully compromised via browser extension flaws, and Apple has issued mercenary spyware threat notifications to iPhone users.

## Active Exploitation Details

### ShieldBreak Zero-Day in Microsoft Defender
- **Description**: A zero-day vulnerability in Microsoft Defender disclosed by security researcher "Nightmare Eclipse" and tracked as CVE-2026-69414
- **Impact**: Full details not yet public; Microsoft is developing a security patch
- **Status**: Zero-day disclosed; patch in development by Microsoft
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: monitor
- **CVE IDs**: CVE-2026-69414
- **Reporting**: [Bleeping Computer — Microsoft working on Defender patch for ShieldBreak zero-day](https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/)

### Critical VMware vCenter Flaw (CVE-2026-59310)
- **Description**: Critical vulnerability in VMware vCenter being exploited by a global threat campaign
- **Impact**: Exploitation may allow attackers to compromise vCenter servers; patching alone may not fully mitigate the threat
- **Status**: Active global exploitation campaign underway since earlier this month
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw)

### SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: Critical authentication bypass vulnerability in Microsoft SharePoint (CVSS 9.1) stemming from weak authentication, patched in July 2026 Patch Tuesday
- **Impact**: Attackers can bypass security features and authentication controls
- **Status**: Actively exploited following public proof-of-concept code release
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### SAP Commerce Cloud Remote Code Execution
- **Description**: Maximum-severity remote code execution vulnerability in SAP Commerce Cloud patched three days prior to reporting
- **Impact**: Full remote code execution on affected SAP Commerce Cloud instances
- **Status**: Actively targeted in attacks per threat intelligence company Defused
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### Windows Zero-Day Exploited by Lazarus Group
- **Description**: Newly patched Windows zero-day vulnerability exploited by North Korean Lazarus Group to gain SYSTEM access and deploy a never-before-seen backdoor
- **Impact**: SYSTEM-level access and persistent backdoor deployment targeting defense and aerospace companies
- **Status**: Active exploitation as part of Operation Dream Job campaign
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### macOS Screen Sharing Authentication Bypass
- **Description**: Authentication bypass vulnerability in macOS Screen Sharing with public exploit code available
- **Impact**: Attackers deploying Monero cryptocurrency miners on compromised systems
- **Status**: Actively exploited; Netherlands NCSC has issued warning
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### Belgium eID Authentication Browser Extension Flaws
- **Description**: Severe vulnerabilities in a key browser extension underlying Belgium's electronic ID system, fully compromising the trust framework
- **Impact**: Remote code execution and citizen account compromise
- **Status**: Vulnerabilities demonstrated; framework fully compromised
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Service Provider Vulnerability in €30M Bank Fraud
- **Description**: Vulnerability at a service provider exploited to withdraw funds from Commerzbank customer accounts
- **Impact**: €30M fraud; four arrests in Brazil, three charged in Europe
- **Status**: Exploited in the wild; law enforcement action taken
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

## Affected Systems and Products

- **Microsoft Defender**: ShieldBreak zero-day (CVE-2026-69414) affecting Defender; patch in development
- **VMware vCenter**: Critical flaw CVE-2026-59310 under global exploitation campaign
- **Microsoft SharePoint**: Authentication bypass CVE-2026-55040 (CVSS 9.1) patched July 2026
- **SAP Commerce Cloud**: Maximum-severity RCE vulnerability patched three days before active targeting observed
- **Microsoft Windows**: Zero-day exploited by Lazarus Group; newly patched
- **macOS Screen Sharing**: Authentication bypass with public exploit code; Monero miner deployment
- **Belgium eID Authentication**: Browser extension vulnerabilities compromising citizen identity framework
- **SafePal Cryptocurrency Wallet**: Order information system flaw exploited; 39,798 customers affected
- **RingCentral**: Platform breached by ShinyHunters; 1.6 million accounts exposed (July 2026)
- **Shell**: Investigating potential incident after Clop claims 89GB data theft
- **Commerzbank/Service Provider**: Service provider flaw enabling €30M fraud against customer accounts
- **Threema Secure Messaging**: Targeted by large-scale DDoS attacks causing severe disruption
- **Internet-facing Gateway Devices/Routers**: Targeted by Evooo1Bot Mirai-based botnet for SOCKS5 relay nodes
- **Chrome Browser Extensions**: 737 malicious VPN/proxy extensions (75,486 installs) intercepting traffic
- **Salesforce and ServiceNow**: Targeted by long-running "City-Forum" campaign since March 2025
- **Apple iPhone**: Targets of mercenary spyware attacks triggering Apple Threat Notifications

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-days actively exploited (ShieldBreak, Windows zero-day by Lazarus, macOS Screen Sharing) before or shortly after disclosure
- **Public PoC Weaponization**: SharePoint CVE-2026-55040 exploited rapidly after proof-of-concept code release
- **N-Day Exploitation**: SAP Commerce Cloud RCE attacked within three days of patch availability
- **ClickFix Social Engineering**: AmnesiaStealer macOS malware delivered via ClickFix attacks tricking users into executing malicious commands
- **Browser Session Hijacking**: AmnesiaStealer includes streaming module for interactive remote control of victim's web browser
- **Mirai-Based Botnet Recruitment**: Evooo1Bot targets internet-facing gateway devices, converting them into SOCKS5 traffic relay nodes
- **Malicious Browser Extensions**: 737 Chrome VPN/proxy extensions (274 impersonating 66 brands) intercept and route browser traffic through proxy infrastructure
- **OAuth Token Theft**: Google Workspace attacks leveraging stolen OAuth tokens for access to Gmail, Drive, and connected systems
- **Service Provider/Supply Chain Compromise**: Vulnerability at service provider exploited for €30M bank fraud against Commerzbank customers
- **Third-Party Data Breach**: Scottish government breach via third-party service provider potentially affecting multiple agencies
- **Ransomware/Extortion**: Clop ransomware claiming 89GB from Shell; ShinyHunters extortion over RingCentral data; Colombian Justice Ministry ransomware
- **DDoS Attacks**: Large-scale distributed denial-of-service attacks disrupting Threema secure messaging
- **Authentication Bypass**: Multiple authentication bypass flaws (SharePoint, macOS Screen Sharing, Belgium eID)
- **Remote Code Execution**: SAP Commerce Cloud, Belgium eID, VMware vCenter, and Windows zero-day all enabling RCE
- **Mercenary Spyware Deployment**: Targeted iPhone attacks triggering Apple Threat Notifications

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Exploiting Windows zero-day for SYSTEM access and novel backdoor deployment against defense/aerospace targets in France, Germany, Brazil, and India as part of Operation Dream Job
- **ShinyHunters Extortion Group**: Breached RingCentral in July 2026, stealing 1.6 million account records for extortion
- **Clop Ransomware Gang**: Claims 89GB data theft from Shell; investigating potential incident
- **Jewelbug APT**: Hackers-for-hire conducting both state-sponsored espionage and financially motivated cryptocurrency theft from same web panel
- **City-Forum Campaign**: Long-running data theft operation active since March 2025 targeting Salesforce and ServiceNow across multiple sectors with custom tooling
- **Nightmare Eclipse**: Security researcher who disclosed ShieldBreak zero-day (CVE-2026-69414) in Microsoft Defender
- **Evooo1Bot Operators**: Deploying Mirai-based modular Linux botnet targeting routers/gateways for SOCKS5 proxy infrastructure
- **AmnesiaStealer Operators**: Distributing macOS info-stealer via ClickFix with interactive browser control capability
- **Chrome Extension Threat Actors**: Operating 40+ developer accounts publishing 737 malicious VPN/proxy extensions targeting Russian-speaking users (75,486 installs)
- **Brazilian/European Cybercriminals**: Four arrested in Brazil, three charged in Europe for €30M Commerzbank fraud via service provider vulnerability
- **Mercenary Spyware Operators**: Conducting targeted iPhone attacks triggering Apple Threat Notifications
- **Unknown Threat Actors**: Exploiting VMware vCenter CVE-2026-59310 in global campaign; exploiting SharePoint CVE-2026-55040 post-PoC; targeting SAP Commerce Cloud RCE; conducting DDoS against Threema; exploiting Belgium eID flaws