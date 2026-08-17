---
schema_version: 2
report_date: 2026-08-16
generated_at: 2026-08-16T21:26:31Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-16/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse platforms, with threat actors rapidly weaponizing recently disclosed flaws. A global campaign targeting CVE-2026-59310 in VMware vCenter began earlier this month, while attackers are exploiting CVE-2026-55040 in Microsoft SharePoint following public proof-of-concept release. The North Korean Lazarus Group leveraged a Windows zero-day to deploy a novel backdoor against defense and aerospace targets in four countries as part of Operation Dream Job. Simultaneously, a maximum-severity SAP Commerce Cloud RCE is being attacked within days of patch availability, and macOS Screen Sharing authentication bypass exploitation has prompted a national cyber security center warning.

Financially motivated actors continue to exploit service provider vulnerabilities for large-scale fraud, evidenced by a €30 million bank heist leveraging a flaw at a third-party provider affecting Commerzbank customers. The Akira ransomware group demonstrated advanced defense evasion by abusing Safe Mode to disable EDR solutions. Espionage-focused operations persist, with the Jewelbug APT conducting parallel government targeting and cryptocurrency theft from a shared web panel. Belgium's eID authentication framework was fully compromised through severe browser extension vulnerabilities, exposing citizen accounts to remote code execution.

## Active Exploitation Details

### VMware vCenter Critical Flaw (CVE-2026-59310)
- **Description**: A critical vulnerability in VMware vCenter Server that allows remote code execution. Exploitation against this flaw began earlier this month as part of a global threat campaign.
- **Impact**: Attackers can achieve remote code execution on vulnerable vCenter servers, potentially leading to full compromise of virtualized infrastructure.
- **Status**: Actively exploited in a global campaign; patching may not be sufficient to fully mitigate the threat.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw)

### Microsoft SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: A critical security feature bypass vulnerability (CVSS 9.1) stemming from weak authentication in Microsoft SharePoint. The flaw was patched in July 2026 Patch Tuesday updates, but threat actors began exploitation following public proof-of-concept code release.
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access to SharePoint environments, potentially accessing sensitive documents and data.
- **Status**: Actively exploited in the wild after PoC publication; patch available since July 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### SAP Commerce Cloud Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in SAP Commerce Cloud that was patched three days before active targeting was observed by threat intelligence firm Defused.
- **Impact**: Successful exploitation allows remote code execution on SAP Commerce Cloud instances, potentially leading to full application and data compromise.
- **Status**: Actively targeted in attacks within days of patch release.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### macOS Screen Sharing Authentication Bypass
- **Description**: An authentication bypass vulnerability in macOS Screen Sharing functionality. Public exploit code has emerged, and the Netherlands' National Cyber Security Centre (NCSC) has issued a warning about active exploitation.
- **Impact**: Attackers can bypass authentication to gain unauthorized remote access to macOS systems, currently being used to deploy Monero cryptocurrency miners.
- **Status**: Actively exploited in the wild with public exploit code available; NCSC warning issued.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### Windows Zero-Day Exploited by Lazarus Group
- **Description**: A newly patched security flaw in Microsoft Windows exploited as a zero-day by the North Korean Lazarus Group. The vulnerability allows elevation to SYSTEM privileges and was used to deploy a never-before-seen backdoor.
- **Impact**: Attackers gain SYSTEM-level access on compromised Windows hosts and deploy persistent backdoors for espionage targeting defense and aerospace sectors.
- **Status**: Zero-day exploitation confirmed; patch now available; attributed to Operation Dream Job campaign.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### Belgium eID Authentication Browser Extension Vulnerabilities
- **Description**: Severe vulnerabilities in a key browser extension underlying Belgium's electronic ID trust framework, fully compromising the authentication system and enabling remote code execution on citizen accounts.
- **Impact**: Complete compromise of the eID trust framework, allowing remote code execution on citizen accounts and exposing broader systemic issues with browser extension security.
- **Status**: Vulnerabilities identified and framework fully compromised; highlights systemic extension security problems.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Service Provider Vulnerability in Bank Fraud
- **Description**: A vulnerability at a service provider exploited by cybercriminals to withdraw funds from Commerzbank customer accounts, resulting in €30 million in fraud across Brazil and Europe.
- **Impact**: Unauthorized financial transactions and fund withdrawal from victim bank accounts via compromised service provider infrastructure.
- **Status**: Actively exploited for financial fraud; four arrests in Brazil, three charged in Europe.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

## Affected Systems and Products

- **VMware vCenter Server**: All versions vulnerable to CVE-2026-59310; global exploitation campaign ongoing
- **Microsoft SharePoint**: Versions prior to July 2026 Patch Tuesday updates vulnerable to CVE-2026-55040 authentication bypass
- **SAP Commerce Cloud**: Unpatched instances targeted within days of patch release for maximum-severity RCE
- **macOS Screen Sharing**: macOS systems with Screen Sharing enabled; public exploit code circulating
- **Microsoft Windows**: Versions prior to the zero-day patch; exploited by Lazarus Group for SYSTEM access
- **Belgium eID Browser Extension**: The key browser extension component of Belgium's electronic ID trust framework
- **Third-party Banking Service Provider**: Undisclosed service provider infrastructure used by Commerzbank and potentially other financial institutions
- **Internet-facing Gateway Devices/Routers**: Targeted by Evooo1Bot Mirai-based botnet for SOCKS5 traffic relay recruitment
- **Salesforce and ServiceNow Instances**: Targeted by long-running City-Forum data theft campaign since March 2025
- **Google Workspace Environments**: Targeted via stolen OAuth tokens and modern attack chains beyond traditional phishing
- **Chrome Browser with VPN/Proxy Extensions**: 737 malicious extensions routing traffic through proxy infrastructure (75,486 installs)

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploited in Microsoft SharePoint (CVE-2026-55040), macOS Screen Sharing, and Belgium eID framework to gain unauthorized access without credentials
- **Remote Code Execution**: Leveraged in VMware vCenter (CVE-2026-59310), SAP Commerce Cloud, and Belgium eID extension for full system compromise
- **Zero-Day Exploitation**: Lazarus Group exploited unpatched Windows vulnerability before patch availability for Operation Dream Job espionage
- **Proof-of-Concept Weaponization**: Rapid exploitation of SharePoint flaw following public PoC release demonstrates immediate attacker adaptation
- **Safe Mode EDR Evasion**: Akira ransomware affiliate restarts compromised systems into Safe Mode with Networking to disable endpoint detection and response solutions
- **ClickFix Social Engineering**: AmnesiaStealer macOS malware delivery via ClickFix attacks tricking users into executing malicious commands
- **Mirai-based Botnet Recruitment**: Evooo1Bot targets internet-facing gateway devices to build SOCKS5 traffic relay infrastructure
- **OAuth Token Theft**: Google Workspace compromise via stolen OAuth tokens bypassing traditional phishing defenses
- **Browser Extension Compromise**: Malicious Chrome VPN/proxy extensions (737 identified) intercept and route browser traffic through attacker infrastructure
- **Service Provider Supply Chain Attack**: Exploitation of third-party service provider vulnerability to access banking customer accounts (€30M fraud)
- **Mercenary Spyware Deployment**: Apple Threat Notifications indicate targeted mercenary spyware attacks against iPhone users
- **Custom Tooling for Cloud Platforms**: City-Forum campaign uses bespoke tools targeting Salesforce and ServiceNow for long-term data theft

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Zero-day exploitation of Windows vulnerability for Operation Dream Job campaign targeting defense and aerospace companies in France, Germany, Brazil, and India; deploys novel backdoor for persistent espionage access
- **Akira Ransomware Affiliates**: Advanced defense evasion using Safe Mode restart to disable EDR; data exfiltration without encryption in observed intrusion
- **Jewelbug APT**: Dual-motivation operations combining state-sponsored espionage against governments/militaries with financially motivated cryptocurrency fraud from shared web panel infrastructure
- **ShinyHunters Extortion Group**: Breached RingCentral, exfiltrated personal data from 1.6 million accounts; data surfaced via Have I Been Pwned notification service
- **Clop Ransomware Gang**: Claimed 89GB data theft from Shell; oil giant investigating potential incident
- **Evooo1Bot Operators**: Mirai-based botnet campaign recruiting routers/gateways as SOCKS5 relay nodes for traffic proxying infrastructure
- **City-Forum Campaign Operators**: Long-running (since March 2025) data theft operation targeting Salesforce and ServiceNow across multiple sectors with custom tooling
- **Brazilian/European Cybercrime Group**: Four arrested in Brazil, three charged in Europe for €30M bank fraud exploiting service provider vulnerability affecting Commerzbank customers
- **Ukrainian Call Center Fraud Networks**: 94 fraudulent call centers shut down by authorities conducting investment scams and bank account takeover attempts
- **AmnesiaStealer Developers**: New macOS information stealer with interactive browser control streaming module delivered via ClickFix social engineering
- **Mercenary Spyware Operators**: Targeted iPhone users triggering Apple Threat Notifications; attribution to commercial surveillance vendors suspected