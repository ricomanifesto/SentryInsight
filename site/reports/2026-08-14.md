---
schema_version: 2
report_date: 2026-08-14
generated_at: 2026-08-14T20:40:49Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-14/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited in the wild across diverse technology stacks, including VMware vCenter, Microsoft SharePoint, Windows, SAP Commerce Cloud, and macOS. The VMware vCenter Syslog Server RCE (CVE-2026-59310) has triggered a global threat campaign with attackers deploying reverse SSH tunnels for persistence, while Microsoft SharePoint's authentication bypass (CVE-2026-55040) is being exploited following public PoC release.

A Windows zero-day known as LegacyHive was patched in July 2026 Patch Tuesday and immediately exploited by North Korea's Lazarus Group in Operation Dream Job targeting defense and aerospace organizations across four countries.

## Active Exploitation Details

### VMware vCenter Syslog Server RCE (CVE-2026-59310)
- **Description**: A critical remote code execution vulnerability in VMware vCenter Syslog Server that allows unauthenticated attackers to execute arbitrary code on affected systems.
- **Impact**: Attackers gain full control of the vCenter server, enabling deployment of reverse SSH tools for persistent remote access and lateral movement within virtualized infrastructure.
- **Status**: Actively exploited in a global threat campaign; patches available but may not fully mitigate threat if compromise already occurred.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw), [Bleeping Computer — Critical VMware vCenter RCE flaw exploited for reverse SSH access](https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/)

### Microsoft SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: A critical security feature bypass vulnerability (CVSS 9.1) stemming from weak authentication in Microsoft SharePoint, patched as part of July 2026 Patch Tuesday.
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access to SharePoint environments, potentially accessing sensitive documents, sites, and connected systems.
- **Status**: Actively exploited following public proof-of-concept code release; patch available since July 2026 Patch Tuesday.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### Windows LegacyHive Zero-Day
- **Description**: A Windows zero-day vulnerability dubbed "LegacyHive" that was actively exploited before being patched in Microsoft's July 2026 Patch Tuesday release.
- **Impact**: Provides attackers with SYSTEM-level access on compromised Windows systems, enabling deployment of backdoors and full system compromise.
- **Status**: Patched in July 2026 Patch Tuesday; confirmed exploited by Lazarus Group in Operation Dream Job campaign.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Microsoft patches LegacyHive Windows zero-day vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/), [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### SAP Commerce Cloud Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in SAP Commerce Cloud that was patched only three days before active exploitation was observed.
- **Impact**: Unauthenticated remote code execution allowing full compromise of SAP Commerce Cloud instances and potential access to connected business systems and customer data.
- **Status**: Patch available; active targeting confirmed by threat intelligence within days of patch release.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### macOS Screen Sharing Authentication Bypass
- **Description**: An authentication bypass vulnerability in macOS Screen Sharing that allows unauthorized remote access; public exploit code has emerged.
- **Impact**: Attackers can bypass authentication to gain remote desktop access, currently being used to deploy Monero cryptocurrency miners on compromised systems.
- **Status**: Actively exploited in the wild per NCSC-NL warning; public exploit code available.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### Belgium eID Authentication Browser Extension RCE
- **Description**: Severe vulnerabilities in a key browser extension underlying Belgium's electronic ID (eID) authentication system that fully compromise the trust framework.
- **Impact**: Remote code execution enabling takeover of citizen accounts authenticated through the eID system, exposing identity theft and unauthorized access to government services.
- **Status**: Vulnerabilities disclosed; trust framework fully compromised.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Service Provider Flaw in Banking Sector
- **Description**: A vulnerability at a third-party service provider exploited to withdraw funds from Commerzbank customer accounts, resulting in €30M fraud.
- **Impact**: Unauthorized financial transactions and account takeover at scale across bank customers; four arrests in Brazil and charges in Europe.
- **Status**: Law enforcement action taken; vulnerability exploited for financial fraud.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

## Affected Systems and Products

- **VMware vCenter Syslog Server**: All versions prior to patched release; critical virtualization management infrastructure
- **Microsoft SharePoint**: On-premises and cloud deployments affected by CVE-2026-55040; patched in July 2026 Patch Tuesday
- **Microsoft Windows**: All supported versions vulnerable to LegacyHive zero-day; patched in July 2026 Patch Tuesday
- **SAP Commerce Cloud**: Cloud-hosted e-commerce platform instances; emergency patch released three days before exploitation observed
- **macOS Screen Sharing**: macOS systems with Screen Sharing enabled; authentication bypass allows remote access
- **Belgium eID Browser Extension**: Citizen authentication infrastructure for Belgian government services; browser extension component fully compromised
- **Third-party Banking Service Provider**: Undisclosed service provider platform used by Commerzbank; flaw enabled €30M fraud

## Attack Vectors and Techniques

- **Reverse SSH Tunneling for Persistence**: Attackers exploiting CVE-2026-59310 deploy reverse SSH tools to maintain persistent remote access to compromised vCenter servers, enabling lateral movement across virtualized environments.
- **Public PoC-Driven Exploitation**: Following the release of proof-of-concept code for CVE-2026-55040, threat actors rapidly weaponized the SharePoint authentication bypass for real-world attacks.
- **Zero-Day Exploitation in Targeted Espionage**: Lazarus Group leveraged the LegacyHive Windows zero-day to gain SYSTEM access and deploy a novel backdoor in Operation Dream Job, targeting defense and aerospace sectors in France, Germany, Brazil, and India.
- **Safe Mode EDR Evasion**: Akira ransomware affiliates disable endpoint detection and response by restarting compromised systems into Safe Mode with Networking, where EDR solutions typically do not load.
- **OAuth Token Theft for Workspace Access**: Attackers bypass phishing by stealing OAuth tokens to gain persistent access to Google Workspace environments including Gmail and Drive.
- **Cryptocurrency Miner Deployment**: Exploitation of macOS Screen Sharing flaw used to deploy Monero miners, indicating financially motivated opportunistic attacks.
- **Supply Chain Compromise**: Multiple incidents (Trezor via ShipMonk, Scottish government via third party, Commerzbank via service provider) demonstrate attackers targeting logistics and service providers to reach primary victims.

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Conducting Operation Dream Job since at least 2026, exploiting Windows zero-day (LegacyHive) to deploy never-before-seen backdoor targeting defense and aerospace companies in France, Germany, Brazil, and India; attributed by Check Point Research.
- **Akira Ransomware Affiliates**: Using Safe Mode with Networking to disable EDR solutions, exfiltrating data but failing to encrypt in observed intrusion; demonstrates evolving ransomware tactics focused on data theft over encryption.
- **Clop Ransomware Gang**: Claimed theft of 89GB of data from Shell; investigating potential incident; known for mass-exploitation campaigns and data extortion.
- **Jewelbug Hacker Group**: Balancing state-sponsored espionage targeting governments and militaries with parallel cryptocurrency fraud operations; operating from same web panel for both mission sets per Dark Reading research.
- **ShinyHunters Extortion Group**: Breached RingCentral in July 2026, stealing personal information from 1.6 million accounts; data surfaced on Have I Been Pwned.
- **City-Forum Campaign**: Long-running data theft operation active since at least March 2025 targeting Salesforce and ServiceNow instances across multiple sectors using custom tooling.
- **Unknown Operators - VMware Campaign**: Global threat campaign exploiting CVE-2026-59310 for reverse SSH access; patching alone may not mitigate if persistence already established.
- **Unknown Operators - SAP Exploitation**: Rapid weaponization of max-severity SAP Commerce Cloud flaw within days of patch release; attributed to threat intelligence from Defused.
- **Unknown Operators - macOS Exploitation**: Opportunistic exploitation of Screen Sharing flaw for cryptocurrency mining after public exploit emergence; warned by NCSC-NL.