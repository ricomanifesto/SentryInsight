# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited across diverse platforms, ranging from enterprise software and cloud services to operating systems and browser extensions. The most severe activity involves zero-day exploitation by nation-state actors, particularly the North Korean Lazarus Group leveraging a Windows vulnerability (CVE-2026-68820) to target defense-sector organizations under Operation Dream Job. Simultaneously, a newly disclosed Microsoft SharePoint authentication bypass (CVE-2026-55040) is under active attack following public PoC release, while Adobe Commerce flaws (CVE-2026-71362) are being exploited to hijack customer accounts on e-commerce platforms.

A parallel wave of supply-chain and infrastructure compromise continues to expand. The "City-Forum" campaign has operated since March 2025, using custom tooling to harvest data from misconfigured Salesforce Experience Cloud and ServiceNow portals across multiple sectors. In the browser ecosystem, 737 malicious Chrome VPN extensions were discovered routing traffic through attacker-controlled SOCKS5 proxies, primarily targeting Russian-speaking users. Meanwhile, the Belgium eID trust framework was fully compromised via vulnerable browser extensions, demonstrating systemic risks in authentication infrastructure.

Threat actors are diversifying techniques and monetization models. The "Jewelbug" APT balances state-sponsored espionage with cryptocurrency theft from the same operational panel. Android malware campaigns now combine NFC relay attacks (WindRelay) with remote administration tools (SpyNote) to steal live payment card data and fraudulently obtain loans. The DeadLock ransomware operation employs blockchain-backed infrastructure to resist takedown, while a new Microsoft Defender zero-day dubbed "ShieldBreak" grants SYSTEM privileges and bypasses August 2026 patches. VMware vCenter, Cisco ASA/FTD, and SAP Commerce Cloud vulnerabilities round out a high-tempo exploitation landscape demanding immediate defensive action.

## Active Exploitation Details

### Microsoft SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: A critical authentication bypass vulnerability in Microsoft SharePoint that allows attackers to circumvent access controls. The flaw was publicly disclosed with proof-of-concept code released by Rapid7, triggering immediate exploitation activity.
- **Impact**: Attackers can gain unauthorized access to SharePoint environments, potentially accessing sensitive documents, internal communications, and proprietary data stored in organizational SharePoint instances.
- **Status**: Actively exploited in the wild following public PoC release. Microsoft has issued patches; immediate application is critical.
- **CVE ID**: CVE-2026-55040

### Adobe Commerce / Magento Critical Flaw (CVE-2026-71362)
- **Description**: A critical vulnerability in Adobe Commerce and Magento e-commerce platforms that enables customer account hijacking. Exploitation attempts have been detected in the wild.
- **Impact**: Attackers can take over customer accounts on affected e-commerce sites, leading to payment fraud, personal data theft, and unauthorized purchases.
- **Status**: Active exploitation detected. Adobe has released security updates for affected versions.
- **CVE ID**: CVE-2026-71362

### Windows Zero-Day Exploited by Lazarus Group (CVE-2026-68820)
- **Description**: A Windows zero-day vulnerability exploited by the North Korean Lazarus Group to gain SYSTEM-level access and deploy a previously unseen backdoor. The flaw was exploited before a patch was available.
- **Impact**: Full SYSTEM privileges on compromised Windows hosts, enabling persistent backdoor deployment, lateral movement, and data exfiltration from defense-sector targets.
- **Status**: Actively exploited as a zero-day; Microsoft has since released patches. Organizations in the defense industrial base are primary targets.
- **CVE ID**: CVE-2026-68820

### VMware vCenter Critical Vulnerability (CVE-2026-593...)
- **Description**: A recently patched critical security flaw in Broadcom VMware vCenter that allows attackers to gain persistent remote access to the virtualization management platform.
- **Impact**: Persistent administrative access to vCenter, enabling control over virtual infrastructure, VM manipulation, and potential escape to underlying hosts.
- **Status**: Actively exploited in the wild per QUIRSO findings. Patches available from Broadcom; immediate deployment recommended.
- **CVE ID**: CVE-2026-593...

### Cisco ASA and FTD Remote DoS Flaw
- **Description**: A vulnerability in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software that can be triggered remotely to cause denial of service.
- **Impact**: Remote denial of service affecting network perimeter defenses, potentially disrupting connectivity and security monitoring capabilities.
- **Status**: Exploited in the wild. Cisco has issued advisories and patches; affected devices should be updated immediately.

### Microsoft Defender "ShieldBreak" Zero-Day
- **Description**: A zero-day exploit targeting Microsoft Defender, dubbed "ShieldBreak," that bypasses security controls and grants SYSTEM privileges. A proof-of-concept was released by researcher Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, Nightmare-Eclipse) after August 2026 Patch Tuesday.
- **Impact**: Local privilege escalation to SYSTEM, Defender tampering/bypass, and potential deployment of persistent malware on endpoint systems.
- **Status**: PoC publicly released; active exploitation risk is high. Microsoft has not yet patched this specific bypass as of the reporting period.
- **CVE ID**: Not yet assigned / CVE pending

### Belgium eID Browser Extension RCE
- **Description**: Severe vulnerabilities in a key browser extension underlying Belgium's electronic ID (eID) authentication trust framework, leading to full compromise of the citizen authentication system.
- **Impact**: Remote code execution in the context of the browser extension, potentially allowing account takeover, identity theft, and unauthorized access to government services tied to eID.
- **Status**: Trust framework fully compromised; patches for the extension deployed. Highlights systemic risks in browser extension supply chains.

### SAP Commerce Cloud Arbitrary Code Execution
- **Description**: A maximum-severity flaw in SAP Commerce Cloud (Data Hub Adapter) allowing unauthenticated attackers to execute arbitrary code.
- **Impact**: Pre-authentication remote code execution on SAP Commerce Cloud instances, leading to full platform compromise and data theft.
- **Status**: Patches released by SAP; exploitation risk is critical for unpatched instances.
- **CVE ID**: CVE ID assigned but not specified in source article

### Adobe ColdFusion, Commerce, and Campaign Classic Critical Flaws
- **Description**: Three CVSS 10.0 vulnerabilities across Adobe ColdFusion, Commerce, and Campaign Classic products that could result in arbitrary code execution.
- **Impact**: Complete compromise of affected Adobe platforms, enabling data theft, ransomware deployment, and lateral movement.
- **Status**: Patches shipped by Adobe; no confirmed wild exploitation reported at time of disclosure, but CVSS 10.0 warrants emergency patching.

## Affected Systems and Products

- **Microsoft SharePoint**: On-premises and cloud instances vulnerable to CVE-2026-55040 authentication bypass; all unpatched versions affected
- **Adobe Commerce / Magento**: E-commerce platforms running unpatched versions vulnerable to CVE-2026-71362 account hijacking
- **Microsoft Windows**: Systems unpatched against CVE-2026-68820; defense-sector workstations and servers actively targeted
- **VMware vCenter**: All versions prior to patched releases vulnerable to CVE-2026-593... persistent remote access flaw
- **Cisco Secure Firewall ASA & FTD**: Appliances and virtual appliances running vulnerable software versions; network perimeter devices at risk
- **Microsoft Defender**: Endpoints running Defender on Windows; "ShieldBreak" zero-day bypasses August 2026 patches
- **Belgium eID Browser Extension**: Citizens and government systems relying on the compromised extension for authentication
- **SAP Commerce Cloud (Data Hub Adapter)**: Cloud deployments with unpatched Data Hub Adapter component
- **Adobe ColdFusion, Commerce, Campaign Classic**: All three product lines with CVSS 10.0 flaws; on-premises and managed cloud instances
- **Salesforce Experience Cloud**: Misconfigured sites exposing data to anonymous access; targeted by "City-Forum" campaign
- **ServiceNow Customer Portals**: Portal configurations allowing anonymous data access; targeted by "City-Forum" campaign
- **Chrome Browser Extensions**: 737 malicious VPN/proxy extensions on Chrome Web Store; Russian-speaking users primarily targeted
- **Android Devices**: Devices installing malicious apps (WindRelay, SpyNote) from unofficial sources or social engineering
- **LiteLLM / PyPI Ecosystem**: Organizations using compromised LiteLLM packages (versions 1.7.0 and 1.7.1) between March 2026

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of CVE-2026-55040 in SharePoint to circumvent access controls without credentials
- **Zero-Day Exploitation**: Lazarus Group leveraging CVE-2026-68820 before patch availability for initial access and SYSTEM escalation
- **Public PoC Weaponization**: Rapid operationalization of SharePoint and ShieldBreak PoC code for real-world attacks
- **Supply Chain Compromise**: Malicious LiteLLM packages on PyPI stealing cloud credentials, SSH keys, Kubernetes tokens, and database passwords
- **Browser Extension Hijacking**: 737 fake VPN extensions intercepting and routing all browser traffic through attacker SOCKS5 proxies
- **Plug and Play Abuse**: "Plug and Pwn" technique forcing Windows to install vulnerable vendor drivers via fake USB devices for SYSTEM access
- **NFC Relay Attack**: WindRelay malware relaying live payment card data via NFC to attacker-controlled devices in real time
- **Remote Administration Tool Deployment**: SpyNote RAT providing persistent control over compromised Android devices
- **Anonymous Data Harvesting**: Custom tooling scraping exposed Salesforce Experience Cloud and ServiceNow portal data without authentication
- **Blockchain-Resilient C2**: DeadLock ransomware using decentralized blockchain infrastructure for command-and-control and leak site hosting
- **Defender Tampering/Bypass**: ShieldBreak exploit disabling or circumventing Microsoft Defender protections post-patch
- **Pre-Auth RCE**: Unauthenticated arbitrary code execution via SAP Commerce Cloud Data Hub Adapter and Adobe CVSS 10.0 flaws
- **Social Engineering / Operation Dream Job**: Lazarus Group targeting defense-sector employees with fake job offers to deliver exploits
- **Account Takeover**: Adobe Commerce flaw (CVE-2026-71362) enabling customer session hijacking and fraudulent transactions

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Exploiting CVE-2026-68820 Windows zero-day against defense-sector companies under Operation Dream Job; deploying novel backdoors with SYSTEM persistence; combining social engineering with vulnerability exploitation
- **Jewelbug APT**: Operating as hackers-for-hire conducting both state-sponsored espionage and financially motivated cryptocurrency theft from a shared Web panel infrastructure; dual-mission operational model
- **City-Forum Campaign Operators**: Long-running data theft operation active since March 2025 targeting Salesforce Experience Cloud and ServiceNow portals across multiple sectors using custom scraping tooling; unknown attribution
- **Nightmare Eclipse / Chaotic Eclipse (INFINITE NIGHTMARE, MSNightmare, Nightmare-Eclipse)**: Security researcher / threat actor releasing ShieldBreak zero-day PoC for Microsoft Defender bypass; claiming patch bypass with SYSTEM access
- **DeadLock Ransomware Gang**: Operating decentralized, blockchain-backed infrastructure to resist takedown; maintaining resilient C2 and data-leak operations
- **Malicious Extension Operators**: Single provider operating 737 fake Chrome VPN/proxy extensions targeting Russian-speaking users; traffic interception and proxy monetization model
- **Android Malware Developers**: Distributing WindRelay (NFC relay) and SpyNote (RAT) combo for real-time credit card theft and loan fraud; financial motivation
- **Supply Chain Attackers (LiteLLM/Trivy)**: Compromised PyPI packages tied to Trivy hack; credential harvesting from 2,100+ potentially exposed organizations; cloud and infrastructure key theft
- **Cybercriminal Account Hijackers**: Targeting social media and online accounts per FBI warning to steal explicit images/videos; extortion and privacy violation motives