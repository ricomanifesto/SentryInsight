---
schema_version: 2
report_date: 2026-08-16
generated_at: 2026-08-16T15:30:56Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-16/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity is accelerating across multiple platforms, with threat actors rapidly weaponizing newly disclosed vulnerabilities. A global campaign is actively exploiting CVE-2026-59310 in VMware vCenter, while Microsoft SharePoint servers face active attacks against CVE-2026-55040 following public proof-of-concept release. Both vulnerabilities carry critical severity ratings and have confirmed patches available, though the VMware campaign may require additional mitigation beyond patching.

Simultaneously, multiple zero-day vulnerabilities are under active exploitation. North Korea's Lazarus Group is leveraging a recently patched Windows zero-day to deploy a novel backdoor against defense and aerospace targets across four countries as part of Operation Dream Job. Microsoft has also patched the LegacyHive Windows zero-day disclosed after July Patch Tuesday. On macOS, attackers are exploiting a Screen Sharing authentication bypass to deploy cryptocurrency miners following public exploit code release, while a maximum-severity SAP Commerce Cloud RCE flaw is being targeted just days after patch availability.

Threat actor activity shows increasing convergence of espionage and financial crime. The Jewelbug APT conducts government espionage and cryptocurrency fraud from the same infrastructure, while Akira ransomware affiliates demonstrate novel EDR evasion via Safe Mode reboot. The Clop ransomware gang claims 89GB theft from Shell, and ShinyHunters breached 1.6 million RingCentral accounts. A massive malvertising campaign comprising 737 malicious Chrome VPN extensions has compromised over 75,000 installations, primarily targeting Russian-speaking users.

## Active Exploitation Details

### CVE-2026-59310 — VMware vCenter Critical Flaw
- **Description**: A critical vulnerability in VMware vCenter that allows remote code execution. The flaw is being exploited by a global threat campaign that began earlier this month.
- **Impact**: Attackers can achieve remote code execution on vCenter servers, potentially compromising entire virtualized infrastructure and enabling lateral movement.
- **Status**: Active exploitation ongoing; patches available but may not fully mitigate the threat according to threat intelligence.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw)

### CVE-2026-55040 — Microsoft SharePoint Authentication Bypass
- **Description**: A critical security feature bypass vulnerability in Microsoft SharePoint stemming from weak authentication mechanisms (CVSS 9.1). Public proof-of-concept code has been released.
- **Impact**: Attackers can bypass authentication controls to gain unauthorized access to SharePoint environments, potentially accessing sensitive documents and data.
- **Status**: Active exploitation observed following public PoC release; patched in Microsoft July 2026 Patch Tuesday updates.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### macOS Screen Sharing Authentication Bypass
- **Description**: An authentication bypass vulnerability in macOS Screen Sharing functionality. Public exploit code has emerged, enabling attackers to bypass authentication controls.
- **Impact**: Attackers can gain unauthorized remote access to macOS systems and deploy payloads including Monero cryptocurrency miners.
- **Status**: Actively exploited in the wild; Netherlands NCSC has issued warning about ongoing attacks.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### SAP Commerce Cloud Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in SAP Commerce Cloud. The flaw was patched three days prior to active targeting being observed.
- **Impact**: Attackers can achieve remote code execution on SAP Commerce Cloud instances, potentially compromising e-commerce platforms and customer data.
- **Status**: Actively targeted in attacks within days of patch release; Defused threat intelligence reports active exploitation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### LegacyHive Windows Zero-Day
- **Description**: A Windows zero-day vulnerability known as "LegacyHive" that was disclosed after the July 2026 Patch Tuesday release. Microsoft has since released security patches.
- **Impact**: As a zero-day, this vulnerability allowed attackers to exploit unpatched Windows systems before disclosure and patching.
- **Status**: Patched by Microsoft following disclosure; exploitation observed prior to patch availability.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — Microsoft patches LegacyHive Windows zero-day vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/)

### Belgium eID Browser Extension Vulnerabilities
- **Description**: Severe vulnerabilities in a key browser extension underlying Belgium's electronic ID (eID) authentication system, fully compromising the trust framework.
- **Impact**: Remote code execution possible against citizen accounts using the eID system; demonstrates systemic risks with browser extension trust models.
- **Status**: Vulnerabilities identified and framework compromised; unclear if actively exploited in wild versus proof-of-concept.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Service Provider Vulnerability (Commerzbank Fraud)
- **Description**: A vulnerability at an unnamed service provider that allowed attackers to withdraw funds from Commerzbank customer accounts, resulting in €30M fraud.
- **Impact**: Direct financial theft from bank customers; four arrests in Brazil and three charges in Europe.
- **Status**: Exploitation confirmed via law enforcement action; vulnerability presumably remediated following investigation.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

### Windows Zero-Day Exploited by Lazarus Group
- **Description**: A newly patched Windows zero-day vulnerability exploited by North Korea's Lazarus Group to gain SYSTEM-level access and deploy a previously unseen backdoor.
- **Impact**: Full system compromise with highest privileges; targeting defense and aerospace companies in France, Germany, Brazil, and India as part of Operation Dream Job.
- **Status**: Active exploitation attributed to nation-state actor; vulnerability recently patched by Microsoft.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

## Affected Systems and Products

- **VMware vCenter**: All versions vulnerable to CVE-2026-59310; global exploitation campaign active
- **Microsoft SharePoint**: Versions prior to July 2026 Patch Tuesday updates vulnerable to CVE-2026-55040
- **macOS**: Systems with Screen Sharing enabled vulnerable to authentication bypass exploit
- **SAP Commerce Cloud**: Unpatched instances targeted within days of patch release
- **Microsoft Windows**: Multiple versions affected by LegacyHive zero-day and separate Lazarus-exploited zero-day; patched in July 2026 updates
- **Belgium eID Browser Extension**: Citizen authentication system compromised via extension vulnerabilities
- **Service Provider Infrastructure**: Unnamed provider platform exploited for banking fraud against Commerzbank
- **Google Chrome**: 737 malicious VPN/proxy extensions (75,486 total installs) across 40+ developer accounts
- **RingCentral**: 1.6 million customer accounts breached via ShinyHunters intrusion
- **Shell**: Potential 89GB data theft claimed by Clop ransomware gang

## Attack Vectors and Techniques

- **Public PoC Weaponization**: Attackers rapidly exploit CVE-2026-55040 (SharePoint) within days of proof-of-concept code release
- **Zero-Day Exploitation**: Lazarus Group and LegacyHive actors leverage undisclosed Windows vulnerabilities for initial access
- **Authentication Bypass**: macOS Screen Sharing flaw and SharePoint CVE-2026-55040 both exploit weak authentication mechanisms
- **Remote Code Execution**: SAP Commerce Cloud, VMware vCenter, and Belgium eID flaws enable direct code execution
- **EDR Evasion via Safe Mode**: Akira ransomware affiliates reboot systems into Safe Mode with Networking to disable endpoint detection
- **Malicious Browser Extensions**: 737 Chrome VPN/proxy extensions intercept and proxy browser traffic (274 impersonating 66 legitimate extensions)
- **ClickFix Social Engineering**: AmnesiaStealer macOS malware delivered via ClickFix attacks with interactive browser streaming capability
- **Mirai-Based Botnet Modularity**: Evooo1Bot Linux botnet targets gateway devices for SOCKS5 traffic relay infrastructure
- **OAuth Token Theft**: Google Workspace attacks leveraging stolen OAuth tokens for persistent access to Gmail, Drive, and connected systems
- **Insider Threat Data Exfiltration**: Data analyst contractor stole and extorted employer for $2.5M

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Active exploitation of Windows zero-day for Operation Dream Job targeting defense/aerospace sectors in France, Germany, Brazil, India; deploys novel backdoor with SYSTEM access
- **Jewelbug APT**: Hackers-for-hire conducting simultaneous state-sponsored espionage against governments/militaries and financially motivated cryptocurrency fraud from shared web panel infrastructure
- **Akira Ransomware Affiliates**: Novel EDR evasion technique using Safe Mode with Networking reboot; data theft without encryption in observed incident
- **Clop Ransomware Gang**: Claims 89GB data theft from Shell; potential incident under investigation
- **ShinyHunters Extortion Group**: Breached RingCentral in July 2026, exfiltrated 1.6 million customer records
- **City-Forum Campaign**: Long-running data theft operation active since March 2025 targeting Salesforce and ServiceNow across multiple sectors with custom tooling
- **Evooo1Bot Operators**: Mirai-based modular botnet targeting internet-facing gateway devices for SOCKS5 proxy infrastructure
- **AmnesiaStealer Operators**: ClickFix-delivered macOS info-stealer with interactive browser session hijacking capability
- **Ukrainian Call Center Fraud Networks**: 94 fraudulent call centers shut down by authorities; investment scams and bank account takeover operations
- **Brazilian/European Banking Fraud Ring**: Four arrested in Brazil, three charged in Europe for €30M Commerzbank fraud via service provider vulnerability exploitation