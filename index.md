---
schema_version: 2
report_date: 2026-08-16
generated_at: 2026-08-16T03:29:24Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-16/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple platforms this period, with two confirmed zero-day vulnerabilities patched in Microsoft's July 2026 Patch Tuesday immediately pressed into service by nation-state actors. The Lazarus Group leveraged a Windows zero-day to deploy a novel backdoor against defense and aerospace targets across four countries, while the LegacyHive vulnerability saw exploitation prior to patch availability. Simultaneously, a global campaign is actively exploiting a critical VMware vCenter flaw (CVE-2026-59310) where patching alone may not suffice, and attackers are weaponizing a SharePoint authentication bypass (CVE-2026-55040) within days of public proof-of-concept release.

Financial and infrastructure targeting remains aggressive. A service provider vulnerability enabled a €30 million bank fraud against Commerzbank customers, resulting in arrests across Brazil and Europe. The Akira ransomware group demonstrated an effective EDR evasion technique using Safe Mode with Networking, while the Evooo1Bot Mirai variant compromises gateway devices into SOCKS5 relay nodes. The Clop ransomware gang claims 89GB of data from Shell, and the ShinyHunters extortion group breached 1.6 million RingCentral accounts. A long-running "City-Forum" campaign has silently exfiltrated data from Salesforce and ServiceNow environments since March 2025 using custom tooling.

Nation-state and criminal operations increasingly blur. The Jewelbug APT conducts simultaneous government espionage and cryptocurrency fraud from shared infrastructure. North Korea's Lazarus Group continues Operation Dream Job with zero-day capabilities. Over 737 malicious Chrome VPN extensions with 75,000+ installs intercept browser traffic, primarily targeting Russian-speaking users. Belgium's eID trust framework was fully compromised through browser extension vulnerabilities, exposing citizen accounts to remote code execution. Ransomware struck Colombia's Justice Ministry amid presidential transition, reflecting escalating Latin American critical infrastructure targeting.

## Active Exploitation Details

### VMware vCenter Critical Flaw (CVE-2026-59310)
- **Description**: A critical vulnerability in VMware vCenter Server that enables remote code execution. A global threat campaign began exploiting this flaw earlier this month, and researchers warn that applying the patch may not be sufficient to fully mitigate the threat due to potential persistent access.
- **Impact**: Remote code execution on vCenter servers, potential persistent compromise even after patching, lateral movement within virtualized infrastructure.
- **Status**: Actively exploited in global campaign since early this month. Patches available but may not fully remediate existing compromises.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw)

### SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: A critical security feature bypass vulnerability (CVSS 9.1) in Microsoft SharePoint stemming from weak authentication mechanisms. The flaw was patched in Microsoft's July 2026 Patch Tuesday, but threat actors began exploitation following public proof-of-concept code release.
- **Impact**: Authentication bypass allowing unauthorized access to SharePoint environments, potential data exfiltration and lateral movement.
- **Status**: Patched in July 2026 Patch Tuesday. Active exploitation observed after public PoC availability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### Evooo1Bot Linux Botnet Targeting Gateway Devices
- **Description**: A new Mirai-based modular Linux botnet malware called Evooo1Bot targeting internet-facing gateway devices (routers, modems). The botnet enrolls compromised devices into a SOCKS5 proxy network for traffic relaying.
- **Impact**: Compromised devices become traffic relay nodes for malicious actors, enabling anonymized proxy networks, credential theft, and further lateral attacks.
- **Status**: Actively targeting internet-facing gateway devices. No specific vendor patches referenced; mitigation relies on device hardening and network monitoring.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/)

### Service Provider Vulnerability Enabling €30M Bank Fraud
- **Description**: A vulnerability at an unnamed service provider was exploited to withdraw funds from Commerzbank customer accounts, resulting in €30 million in fraud. Four suspects arrested in Brazil, three charged in Europe.
- **Impact**: Direct financial theft from banking customers, compromise of service provider infrastructure enabling unauthorized transaction processing.
- **Status**: Exploitation confirmed via law enforcement action. Vulnerability details not publicly disclosed; service provider presumably patched post-incident.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

### macOS Screen Sharing Authentication Bypass
- **Description**: An authentication bypass vulnerability in macOS Screen Sharing functionality. The Netherlands' National Cyber Security Centre (NCSC) issued a warning after public exploit code emerged, confirming active exploitation to deploy Monero cryptocurrency miners.
- **Impact**: Unauthorized remote access via Screen Sharing, deployment of cryptocurrency miners, potential persistence and lateral movement.
- **Status**: Actively exploited per NCSC advisory. Public exploit code available. Apple patch status not specified in reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### SAP Commerce Cloud Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in SAP Commerce Cloud. Patched three days prior to reporting, but threat intelligence firm Defused confirms active targeting in attacks.
- **Impact**: Full remote code execution on SAP Commerce Cloud instances, potential compromise of e-commerce platforms, payment data, and customer PII.
- **Status**: Patch available for three days. Active exploitation confirmed by threat intelligence.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### LegacyHive Windows Zero-Day
- **Description**: A Windows zero-day vulnerability designated "LegacyHive" that was actively exploited prior to disclosure. Microsoft addressed the flaw in the July 2026 Patch Tuesday release.
- **Impact**: Zero-day exploitation on Windows systems, specifics of impact vector not detailed in reporting.
- **Status**: Patched in July 2026 Patch Tuesday. Was actively exploited as a zero-day prior to patch availability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Microsoft patches LegacyHive Windows zero-day vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/)

### Windows Zero-Day Exploited by Lazarus Group (Operation Dream Job)
- **Description**: A newly patched Windows zero-day vulnerability exploited by the North Korean Lazarus Group to gain SYSTEM-level access and deploy a previously unseen backdoor. Targets defense and aerospace companies in France, Germany, Brazil, and India as part of the long-running Operation Dream Job campaign.
- **Impact**: SYSTEM-level compromise, custom backdoor deployment, persistent access to high-value defense/aerospace targets across four countries.
- **Status**: Zero-day exploited in the wild. Microsoft has released a patch. Active campaign attributed to nation-state actor.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### Belgium eID Browser Extension Vulnerabilities
- **Description**: Severe vulnerabilities in a key browser extension supporting Belgium's electronic ID (eID) authentication system. The trust framework underlying citizen authentication was fully compromised, enabling remote code execution against citizen accounts.
- **Impact**: Full compromise of Belgium's eID trust framework, RCE against citizen accounts, identity theft, authentication bypass for government services.
- **Status**: Vulnerabilities identified and trust framework confirmed "fully compromised." Remediation status of extension not specified.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Akira Ransomware Safe Mode EDR Evasion
- **Description**: An Akira ransomware affiliate disabled endpoint detection and response (EDR) protection by restarting the compromised system into Safe Mode with Networking, where the EDR solution does not load. The attackers exfiltrated data but failed to deploy the encryptor.
- **Impact**: EDR bypass enabling unimpeded enumeration and data exfiltration. Technique demonstrates reliable defense evasion on Windows systems.
- **Status**: Observed in active intrusion. Technique is procedural (no CVE); mitigation requires configuration changes.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Akira hackers disable EDR with Safe Mode, steal data but fail to encrypt](https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/)

### Malicious Chrome VPN Extensions Campaign
- **Description**: 737 malicious Chrome VPN and proxy extensions discovered in the Chrome Web Store, collectively amassing 75,486 installs. Extensions intercept browser traffic and route it through attacker-controlled proxy infrastructure. 274 extensions impersonate 66 legitimate VPN/proxy services. Primarily targets Russian-speaking users seeking access to blocked services.
- **Impact**: Full browser traffic interception, credential harvesting, session hijacking, traffic manipulation, potential corporate data exfiltration via BYOD.
- **Status**: Extensions identified and reported. Google removal status not confirmed in reporting. Large installed base remains active until user removal.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — 737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One](https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html)

### City-Forum Campaign Targeting Salesforce and ServiceNow
- **Description**: A long-running data theft campaign active since at least March 2025, targeting organizations across multiple sectors using custom tooling against Salesforce and ServiceNow platforms. Campaign dubbed "City-Forum" by researchers.
- **Impact**: Persistent unauthorized access to CRM and ITSM platforms, exfiltration of customer records, case data, internal communications, and configuration data.
- **Status**: Active for 15+ months. Custom tooling indicates dedicated development. Attribution not specified.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Long-running Data Theft Campaign Targeting Salesforce, ServiceNow](https://www.darkreading.com/cyberattacks-data-breaches/long-running-data-theft-campaign-salesforce-servicenow)

## Affected Systems and Products

- **VMware vCenter Server**: All versions vulnerable to CVE-2026-59310; patching may not fully remediate existing compromises
- **Microsoft SharePoint**: Versions prior to July 2026 Patch Tuesday vulnerable to CVE-2026-55040 (CVSS 9.1)
- **Internet-facing Gateway Devices (Routers/Modems)**: Linux-based devices targeted by Evooo1Bot Mirai variant for SOCKS5 proxy enrollment
- **Service Provider Infrastructure (Unnamed)**: Vulnerability enabling €30M Commerzbank fraud; specific product not disclosed
- **macOS Screen Sharing**: Versions with authentication bypass flaw; public exploit code circulating
- **SAP Commerce Cloud**: All unpatched instances; emergency patch released three days before active targeting confirmed
- **Microsoft Windows**: LegacyHive zero-day (patched July 2026); separate zero-day exploited by Lazarus (patched July 2026)
- **Belgium eID Browser Extension**: Key extension component of national electronic ID trust framework; fully compromised
- **Google Chrome Browser**: 737 malicious VPN/proxy extensions with 75,486 total installs; 274 impersonating 66 legitimate extensions
- **Salesforce & ServiceNow Platforms**: Targeted by City-Forum campaign since March 2025 using custom tooling
- **RingCentral Systems**: Breached by ShinyHunters; 1.6 million accounts compromised in July 2026
- **Shell Infrastructure**: Clop ransomware claims 89GB data exfiltration; investigation ongoing
- **Colombian Justice Ministry Systems**: Ransomware attack days before presidential transition
- **Scottish Government/Prosecutor's Office**: Third-party service provider breach with potential multi-agency impact

## Attack Vectors and Techniques

- **Mirai-based Botnet Recruitment**: Evooo1Bot scans for internet-facing gateway devices, exploits default/weak credentials or unpatched flaws, installs modular Linux payload converting devices to SOCKS5 relay nodes
- **Service Provider Supply Chain Exploitation**: Vulnerability in third-party service provider infrastructure leveraged to process fraudulent Commerzbank transactions (€30M)
- **Authentication Bypass via Public PoC**: CVE-2026-55040 (SharePoint) and macOS Screen Sharing flaw both exploited after proof-of-concept code publication
- **Zero-Day Exploitation by Nation-State**: Lazarus Group leveraged unpatched Windows flaw for SYSTEM access and custom backdoor deployment (Operation Dream Job)
- **Safe Mode EDR Evasion**: Akira ransomware affiliate restarts compromised host into Safe Mode with Networking where EDR drivers do not load, enabling unimpeded data theft
- **Browser Extension Supply Chain Compromise**: 737 malicious Chrome VPN extensions published across 40+ developer accounts, impersonating legitimate tools to intercept all browser traffic
- **National Trust Framework Subversion**: Belgium eID browser extension vulnerabilities fully compromise citizen authentication framework, enabling RCE and identity theft
- **Custom Platform-Specific Tooling**: City-Forum campaign uses bespoke tooling for Salesforce and ServiceNow, indicating target-specific development and long-term access
- **Ransomware with Failed Encryption**: Akira affiliate achieves data exfiltration but fails encryptor deployment, suggesting dual-extortion model with operational errors
- **OAuth Token Theft for Workspace Access**: Google Workspace attacks leveraging stolen OAuth tokens bypassing phishing requirements for Gmail/Drive access

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Active exploitation of Windows zero-day for SYSTEM access and novel backdoor deployment against defense/aerospace sector in France, Germany, Brazil, India. Part of multi-year Operation Dream Job espionage campaign. Attribution per Check Point Research.
- **Jewelbug / Jewelbug APT**: Hackers-for-hire group conducting simultaneous government/military espionage and cryptocurrency fraud from shared web panel infrastructure. Targets governments globally while running parallel financial crime operations.
- **Akira Ransomware Affiliates**: Demonstrated Safe Mode with Networking technique to disable EDR solutions. Achieved data exfiltration but failed encryption deployment. Indicates mature ransomware-as-a-service affiliate operations.
- **Clop Ransomware Gang**: Claims 89GB data theft from Shell. Shell investigating potential incident. Consistent with Clop's pattern of high-value corporate targeting and data extortion.
- **ShinyHunters Extortion Group**: Breached RingCentral in July 2026, exfiltrating 1.6 million account records. Data surfaced via Have I Been Pwned notification service.
- **Evooo1Bot Operators**: Deploying Mirai-derived modular botnet targeting gateway devices for SOCKS5 proxy network. Infrastructure suggests organized proxy-for-hire or traffic monetization operation.
- **City-Forum Campaign Operators**: Long-running (15+ months) data theft operation with custom Salesforce/ServiceNow tooling. Multi-sector targeting suggests espionage or competitive intelligence motivation. Attribution unknown.
- **Brazilian/European Cybercrime Network**: Four arrested in Brazil, three charged in Europe for €30M Commerzbank fraud via service provider vulnerability. Indicates transnational financial crime coordination.
- **Chrome VPN Extension Developers**: 40+ Chrome Web Store developer accounts publishing 737 malicious extensions (75K+ installs). Targeting Russian-speaking users for traffic interception. Supply chain abuse at scale.
- **Colombian Justice Ministry Ransomware Actors**: Ransomware deployment against critical government infrastructure days before presidential transition. Part of escalating Latin American government targeting trend.