---
schema_version: 2
report_date: 2026-08-17
generated_at: 2026-08-17T01:42:15Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-17/
---
# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors rapidly weaponizing recently disclosed vulnerabilities and leveraging proven malware frameworks. Critical flaws in enterprise platforms—including VMware vCenter (CVE-2026-59310) and Microsoft SharePoint (CVE-2026-55040)—are under active global exploitation within days of patch availability, while a maximum-severity SAP Commerce Cloud RCE is already targeted in the wild.

Nation-state actors remain highly active: the Lazarus Group has exploited a Windows zero-day to deploy a novel backdoor against defense and aerospace targets in Europe, Brazil, and India as part of Operation Dream Job, and the Jewelbug APT conducts blended espionage and cryptocurrency theft operations from a shared web panel.

## Active Exploitation Details

### VMware vCenter Critical Flaw (CVE-2026-59310)
- **Description**: A critical vulnerability in VMware vCenter Server that enables remote code execution. Exploitation activity began earlier this month and has escalated into a global threat campaign.
- **Impact**: Attackers can achieve full compromise of vCenter infrastructure, potentially leading to hypervisor control, virtual machine manipulation, and lateral movement across virtualized environments.
- **Status**: Actively exploited in a global campaign; patches are available but may not be sufficient to fully mitigate the threat due to potential persistence or credential theft.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw)

### Microsoft SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: A critical security feature bypass (CVSS 9.1) stemming from weak authentication in Microsoft SharePoint. The vulnerability was patched in the July 2026 Patch Tuesday release, and public proof-of-concept code has since been released.
- **Impact**: Attackers can bypass authentication controls to access SharePoint resources, potentially leading to data exfiltration, privilege escalation, and lateral movement within Microsoft 365 environments.
- **Status**: Actively exploited following public PoC release; patch available since July 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### SAP Commerce Cloud Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in SAP Commerce Cloud that was patched three days prior to reported exploitation activity.
- **Impact**: Successful exploitation grants attackers full code execution on the commerce platform, enabling data theft, payment manipulation, and supply chain compromise.
- **Status**: Actively targeted in attacks within days of patch release; threat intelligence firm Defused has confirmed exploitation attempts.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### macOS Screen Sharing Authentication Bypass
- **Description**: An authentication bypass vulnerability in macOS Screen Sharing that allows unauthorized remote access. Public exploit code has emerged, enabling automated attacks.
- **Impact**: Attackers gain interactive control of the victim's desktop session, which has been used to deploy Monero cryptocurrency miners and could facilitate further payload delivery.
- **Status**: Actively exploited in the wild; Netherlands NCSC has issued warnings. No CVE identifier provided in source.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### Windows Zero-Day Exploited by Lazarus Group
- **Description**: A newly patched security flaw in Microsoft Windows exploited as a zero-day by the North Korean Lazarus Group. The vulnerability enables SYSTEM-level privilege escalation.
- **Impact**: Attackers gain SYSTEM access and deploy a never-before-seen backdoor, facilitating persistent espionage access to defense and aerospace organizations in France, Germany, Brazil, and India.
- **Status**: Zero-day exploitation confirmed by Check Point Research; patch now available. Part of Operation Dream Job campaign.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### Belgium eID Browser Extension RCE
- **Description**: Severe vulnerabilities in a key browser extension underpinning Belgium's electronic ID (eID) authentication system, fully compromising the trust framework.
- **Impact**: Remote code execution on citizen systems, enabling account takeover, identity theft, and potential compromise of government services relying on eID authentication.
- **Status**: Vulnerabilities demonstrated and framework compromised; no specific CVE provided in source.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Service Provider Vulnerability (Commerzbank Fraud)
- **Description**: A vulnerability at an unnamed service provider exploited by a cybercrime group to withdraw funds from Commerzbank customer accounts, resulting in €30M in fraud.
- **Impact**: Direct financial theft via unauthorized account access and fund withdrawal; four arrests in Brazil and three charges in Europe.
- **Status**: Vulnerability exploited for financial fraud; law enforcement action taken. No CVE provided.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

### SafePal Customer Data Breach
- **Description**: A flaw in SafePal's systems was exploited to steal order information for approximately 39,798 cryptocurrency hardware wallet customers. The stolen data is now being offered for sale by a threat actor.
- **Impact**: Exposure of customer PII and order details, enabling targeted phishing, physical theft risk, and cryptocurrency targeting.
- **Status**: Breach confirmed by SafePal; data actively marketed on underground forums. No CVE provided.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — SafePal data breach impacts 39,798 customers, stolen info for sale](https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/)

### RingCentral Data Breach (ShinyHunters)
- **Description**: The ShinyHunters extortion group compromised RingCentral in July 2025, exfiltrating personal information from 1.6 million accounts. Data surfaced via Have I Been Pwned notification service.
- **Impact**: Large-scale exposure of customer PII for extortion and follow-on attacks; breach confirmed via third-party notification.
- **Status**: Historical breach (July 2025) with data now circulating; law enforcement and victim notification ongoing. No CVE provided.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — RingCentral data breach exposed info of 1.6 million accounts](https://www.bleepingcomputer.com/news/security/ringcentral-data-breach-exposed-info-of-16-million-accounts/)

### City-Forum Campaign (Salesforce, ServiceNow)
- **Description**: A long-running data theft campaign active since at least March 2025 targeting Salesforce and ServiceNow instances across multiple sectors using custom tooling.
- **Impact**: Persistent unauthorized access to CRM and IT service management platforms, enabling intellectual property theft, credential harvesting, and supply chain reconnaissance.
- **Status**: Ongoing campaign with custom malware; no specific vulnerability CVE identified in reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Long-running Data Theft Campaign Targeting Salesforce, ServiceNow](https://www.darkreading.com/cyberattacks-data-breaches/long-running-data-theft-campaign-salesforce-servicenow)

### AmnesiaStealer macOS Malware (ClickFix)
- **Description**: A new macOS information stealer delivered via ClickFix social engineering attacks, featuring a browser streaming module for interactive remote control of victim web sessions.
- **Impact**: Credential theft, session hijacking, cryptocurrency wallet compromise, and real-time browser manipulation for fraud and further exploitation.
- **Status**: Actively distributed via ClickFix lures; novel interactive capability observed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — New AmnesiaStealer macOS malware hijacks browser sessions via remote control](https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/)

### Evooo1Bot Linux Botnet (Mirai-based)
- **Description**: A modular Mirai-derivative Linux botnet targeting internet-facing gateway devices (routers, IoT) to enroll them as SOCKS5 traffic relay nodes.
- **Impact**: Compromised devices become anonymization infrastructure for follow-on attacks, credential stuffing, and C2 obfuscation; potential bandwidth abuse.
- **Status**: Active scanning and infection of exposed gateway devices; modular design enables rapid capability updates.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/)

### Clop Ransomware Data Theft (Shell)
- **Description**: The Clop ransomware gang claims to have stolen 89GB of data from Shell, prompting an investigation by the oil giant.
- **Impact**: Potential exposure of sensitive corporate data, operational disruption, and extortion pressure; claim may precede leak site publication.
- **Status**: Claim posted by Clop; Shell investigating potential incident. No specific vulnerability CVE identified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Shell investigates 'potential incident' after Clop data theft claims](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)

### Mercenary Spyware Attacks (Apple Threat Notifications)
- **Description**: Apple has issued new Threat Notifications to iPhone users warning of mercenary spyware attacks targeting their devices.
- **Impact**: Sophisticated, targeted surveillance of high-value individuals; likely zero-click or one-click exploits against iOS.
- **Status**: Active targeting confirmed by Apple notifications; specific exploit chain not disclosed.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Apple sends new ‘Threat Notification’ alerts over mercenary spyware attacks](https://www.bleepingcomputer.com/news/apple/apple-sends-new-threat-notification-alerts-over-mercenary-spyware-attacks/)

### Colombian Justice Ministry Ransomware
- **Description**: Ransomware attack on the Colombian Ministry of Justice days before a presidential transition, continuing a pattern of critical infrastructure targeting in Latin America.
- **Impact**: Operational disruption to judicial systems, potential data exfiltration, and political destabilization risk during leadership transition.
- **Status**: Active incident; ransomware variant and initial access vector not publicly identified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — Ransomware Hits Colombian Justice Ministry Days Before Presidential Transition](https://www.darkreading.com/cyberattacks-data-breaches/ransomware-hits-colombian-justice-ministry-presidential-transition)

### Threema DDoS Attacks
- **Description**: Multiple large-scale distributed denial-of-service attacks targeting the Threema secure messaging service, causing severe communication disruptions.
- **Impact**: Service degradation and outage for Threema users; no data breach reported but availability impact significant.
- **Status**: Active DDoS campaign; mitigation efforts ongoing. No vulnerability exploitation—volumetric attack.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Large-scale DDoS attacks disrupted Threema secure messaging service](https://www.bleepingcomputer.com/news/security/large-scale-ddos-attacks-disrupted-threema-secure-messaging-service/)

### Malicious Chrome VPN Extensions (737 Extensions)
- **Description**: 737 malicious Chrome Web Store VPN and proxy extensions (75,486 total installs) intercepting browser traffic and routing it through attacker-controlled proxy infrastructure, with 274 extensions impersonating 66 legitimate brands.
- **Impact**: Traffic interception, credential harvesting, session hijacking, and privacy violation for predominantly Russian-speaking users seeking censorship circumvention.
- **Status**: Extensions identified and reported; removal from Chrome Web Store likely in progress. Supply chain compromise via developer accounts.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — 737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One](https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html)

## Affected Systems and Products

- **VMware vCenter Server**: All versions vulnerable to CVE-2026-59310; critical RCE exploited in global campaign
- **Microsoft SharePoint / Microsoft 365**: On-premises and cloud instances affected by CVE-2026-55040 authentication bypass; patched July 2026
- **SAP Commerce Cloud**: All unpatched instances vulnerable to maximum-severity RCE; active exploitation within days of patch
- **macOS (Screen Sharing)**: Versions with vulnerable Screen Sharing authentication mechanism; public exploit code available
- **Microsoft Windows**: Versions affected by zero-day privilege escalation exploited by Lazarus Group; patched in recent update cycle
- **Belgium eID Browser Extension**: Key extension component of national electronic ID system; RCE via compromised trust framework
- **SafePal Hardware Wallet Backend**: Customer order management systems; flaw exposed 39,798 customer records
- **RingCentral Platform**: Internal systems breached in July 2025; 1.6 million customer accounts compromised
- **Salesforce & ServiceNow Instances**: Targeted by City-Forum campaign since March 2025 using custom tooling
- **Internet-Facing Gateway Devices (Routers, IoT)**: Linux-based devices targeted by Evooo1Bot Mirai-variant for SOCKS5 proxy enrollment
- **iOS / iPhone**: Targeted by mercenary spyware campaigns triggering Apple Threat Notifications
- **Chrome Browser / Chrome Web Store**: 737 malicious VPN/proxy extensions with 75,486 installs; traffic interception via proxy infrastructure
- **Threema Messaging Infrastructure**: Targeted by volumetric DDoS attacks causing service disruption
- **Shell Corporate Systems**: Investigating Clop ransomware claim of 89GB data theft
- **Colombian Ministry of Justice IT Systems**: Ransomware attack during presidential transition period
- **Unnamed Financial Service Provider**: Vulnerability exploited for €30M Commerzbank fraud; arrests in Brazil and Europe

## Attack Vectors and Techniques

- **Public PoC Weaponization**: Rapid exploitation of CVE-2026-55040 (SharePoint) and CVE-2026-59310 (vCenter) following proof-of-concept release and patch availability
- **Zero-Day Privilege Escalation**: Lazarus Group leveraging Windows kernel flaw for SYSTEM access before patch deployment
- **ClickFix Social Engineering**: AmnesiaStealer delivery via fake verification prompts tricking users into executing malicious commands
- **Authentication Bypass**: Weak authentication in SharePoint (CVE-2026-55040) and macOS Screen Sharing enabling unauthorized access
- **Browser Extension Compromise**: Belgium eID extension vulnerabilities undermining national trust framework; malicious Chrome VPN extensions intercepting traffic
- **Mirai-Variant Botnet Propagation**: Evooo1Bot scanning and infecting exposed gateway devices via default/weak credentials and known exploits
- **Custom Tooling for SaaS Platforms**: City-Forum campaign using bespoke malware for Salesforce and ServiceNow data exfiltration
- **Interactive Browser Streaming**: AmnesiaStealer's novel module allowing real-time attacker control of victim browser sessions
- **Supply Chain / Service Provider Exploitation**: Unnamed provider flaw enabling €30M bank fraud against Commerzbank customers
- **Ransomware + Data Extortion**: Clop (Shell), ShinyHunters (RingCentral), and unidentified actors (Colombian Justice Ministry) combining encryption with data theft
- **Mercenary Spyware Delivery**: Likely zero-click iOS exploits targeting high-value individuals; detected via Apple Threat Notifications
- **Volumetric DDoS**: Multi-vector flooding attacks against Threema messaging infrastructure
- **Extortion Data Monetization**: Stolen SafePal and RingCentral customer data actively marketed on underground forums

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Zero-day exploitation of Windows vulnerability for SYSTEM access; deployment of novel backdoor targeting defense/aerospace sectors in France, Germany, Brazil, India under Operation Dream Job; attributed by Check Point Research
- **Jewelbug APT**: Hackers-for-hire group conducting blended state-sponsored espionage and financially motivated cryptocurrency theft from shared web panel infrastructure
- **Clop Ransomware Gang**: Claims 89GB data theft from Shell; established extortion operation with leak site publication model
- **ShinyHunters Extortion Group**: Breached RingCentral in July 2025; exfiltrated 1.6M customer records; data surfaced via Have I Been Pwned
- **City-Forum Campaign Operators**: Long-running (since March 2025) data theft operation targeting Salesforce and ServiceNow across multiple verticals with custom malware
- **AmnesiaStealer Developers/Operators**: New macOS malware family using ClickFix delivery and interactive browser streaming capability
- **Evooo1Bot Operators**: Mirai-variant botnet herders building SOCKS5 proxy infrastructure from compromised gateway devices
- **Unnamed Cybercrime Group (Commerzbank Fraud)**: Exploited service provider vulnerability for €30M theft; four arrested in Brazil, three charged in Europe
- **Mercenary Spyware Vendors/Operators**: Conducting targeted iPhone surveillance campaigns triggering Apple Threat Notifications; likely commercial surveillance tools
- **Colombian Justice Ministry Ransomware Actors**: Unidentified group targeting government infrastructure during political transition; part of Latin America targeting surge
- **Threema DDoS Operators**: Coordinated volumetric attack campaign against secure messaging service; motivation unclear (hacktivism, extortion, disruption)
- **Chrome VPN Extension Developers**: 40+ developer accounts publishing 737 malicious extensions (274 brand impersonators) targeting Russian-speaking users for traffic interception