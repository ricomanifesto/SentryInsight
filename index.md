---
schema_version: 1
report_date: 2026-08-13
generated_at: 2026-08-13T16:03:32Z
---
# Exploitation Report

## Executive Summary

Active exploitation campaigns have intensified across multiple vectors in August 2026, with threat actors rapidly weaponizing newly disclosed vulnerabilities and proof-of-concept code. North Korean state-sponsored group Lazarus is leveraging a Windows zero-day (CVE-2026-68820) against defense-sector targets under Operation Dream Job, while simultaneously a separate Microsoft Defender zero-day dubbed "ShieldBreak" grants SYSTEM privileges and has public PoC code circulating. Microsoft SharePoint authentication bypass (CVE-2026-55040) and VMware vCenter are both under active exploitation following PoC releases, and a critical Adobe Commerce flaw (CVE-2026-71362) is being used to hijack customer accounts on e-commerce platforms.

Supply chain and identity-focused attacks continue to expand in scope. The "City-Forum" campaign has operated since March 2025, using custom tooling to extract data from misconfigured Salesforce Experience Cloud and ServiceNow portals across multiple sectors. A massive browser extension campaign comprising 737 malicious Chrome VPN extensions routes victim traffic through attacker-controlled SOCKS5 proxies, primarily targeting Russian-speaking users. Meanwhile, the Belgium eID browser extension compromise demonstrates systemic risks in trust frameworks, enabling remote code execution against citizen authentication systems.

Financially motivated and espionage operations increasingly blur. The Jewelbug APT operates as a hackers-for-hire service conducting both state espionage and cryptocurrency theft from the same infrastructure. Android malware combinations—WindRelay NFC relay malware paired with SpyNote RAT—steal live payment card data and initiate fraudulent loans in real time. Cisco ASA/FTD vulnerabilities are exploited in the wild for denial-of-service, while a malicious PyPI supply chain attack via trojanized LiteLLM packages exposed over 2,100 organizations to credential theft.

## Active Exploitation Details

### Microsoft SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: A critical authentication bypass vulnerability in Microsoft SharePoint that allows unauthenticated attackers to circumvent access controls. The flaw was disclosed with a proof-of-concept exploit published by Rapid7.
- **Impact**: Attackers can gain unauthorized access to SharePoint sites, potentially exposing sensitive documents, internal communications, and organizational data. Successful exploitation enables further lateral movement within Microsoft 365 environments.
- **Status**: Actively exploited in the wild following public PoC release. Microsoft has released patches; organizations should prioritize immediate deployment.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040

### Windows Zero-Day Exploited by Lazarus Group (CVE-2026-68820)
- **Description**: A zero-day vulnerability in Microsoft Windows exploited by the North Korean Lazarus Group to achieve SYSTEM-level code execution. The exploit delivers a previously undocumented backdoor.
- **Impact**: Full SYSTEM privileges on compromised hosts, enabling persistent access, credential theft, lateral movement, and deployment of additional payloads. Used specifically against defense-sector companies.
- **Status**: Actively exploited as a zero-day prior to patching. Microsoft has since released fixes in August 2026 Patch Tuesday updates.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-68820

### Microsoft Defender "ShieldBreak" Zero-Day
- **Description**: A zero-day exploit targeting Microsoft Defender that bypasses security controls and grants SYSTEM-level privileges. The exploit, named "ShieldBreak," was released by researcher Nightmare Eclipse (also known as Chaotic Eclipse, INFINITE NIGHTMARE, MSNightmare) following August 2026 Patch Tuesday.
- **Impact**: Complete bypass of Microsoft Defender protections with SYSTEM access, effectively disabling endpoint defense and allowing unrestricted code execution.
- **Status**: Public PoC code available. Actively exploitable on patched systems as of disclosure. Microsoft has not yet issued a specific fix for this bypass technique.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: investigate

### Adobe Commerce / Magento Critical Flaw (CVE-2026-71362)
- **Description**: A critical vulnerability in Adobe Commerce and Magento e-commerce platforms that allows attackers to hijack customer accounts without authentication.
- **Impact**: Full account takeover of customer accounts on affected e-commerce sites, enabling payment fraud, PII theft, order manipulation, and potential lateral access to administrative interfaces.
- **Status**: Active exploitation attempts detected in the wild. Adobe has released security patches; merchants should apply immediately.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-71362

### VMware vCenter Critical Vulnerability
- **Description**: A critical security flaw in Broadcom VMware vCenter that enables persistent remote access. Actively exploited by threat actors according to QUIRSO findings.
- **Impact**: Unauthenticated remote code execution with persistent access to the virtualization management layer, compromising all managed ESXi hosts and virtual machines.
- **Status**: Active exploitation confirmed. Broadcom has released patches; emergency deployment recommended for internet-exposed vCenter instances.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch

### Cisco ASA and FTD Remote DoS Vulnerability
- **Description**: A vulnerability in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software that can be triggered remotely to cause denial-of-service conditions.
- **Impact**: Complete service disruption of firewall capabilities, leaving networks unprotected during outage. Exploited in the wild per Cisco advisory.
- **Status**: Actively exploited in the wild. Cisco has released software updates and workarounds.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch

### Belgium eID Browser Extension RCE
- **Description**: Severe vulnerabilities in the browser extension underpinning Belgium's electronic ID (eID) authentication system, fully compromising the trust framework used for citizen authentication.
- **Impact**: Remote code execution in the context of citizen authentication sessions, enabling account takeover, identity theft, and unauthorized access to government services.
- **Status**: Vulnerabilities disclosed; patches for the browser extension deployed. Highlights systemic risks in browser extension trust models.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: patch

### SAP Commerce Cloud Arbitrary Code Execution
- **Description**: A maximum-severity security flaw in SAP Commerce Cloud (Data Hub Adapter) allowing unauthenticated attackers to execute arbitrary code.
- **Impact**: Full server compromise, access to commerce data, potential pivot to connected ERP systems, and supply chain disruption.
- **Status**: SAP has released patches. Exploitation status in wild not explicitly confirmed but severity warrants immediate patching.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch

### Malicious LiteLLM PyPI Supply Chain Attack
- **Description**: Two trojanized LiteLLM packages uploaded to PyPI in March 2026 containing credential-stealing code. The packages remained available for approximately 40 minutes but were downloaded by automated build systems.
- **Impact**: Harvesting of cloud API keys, SSH keys, Kubernetes tokens, database passwords, and other secrets from over 2,100 potentially affected organizations.
- **Status**: Packages removed from PyPI. Incident linked to Trivy security scanner compromise. Affected organizations must rotate all potentially exposed credentials.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate

## Affected Systems and Products

- **Microsoft SharePoint**: All versions affected by CVE-2026-55040; authentication bypass enables unauthenticated access to SharePoint Online and on-premises deployments
- **Microsoft Windows**: Versions vulnerable to CVE-2026-68820 (Lazarus zero-day) and ShieldBreak Defender bypass; impacts enterprise and consumer editions
- **Microsoft Defender**: Endpoint protection bypass via ShieldBreak zero-day; affects current definitions as of August 2026 Patch Tuesday
- **Adobe Commerce / Magento**: E-commerce platforms vulnerable to CVE-2026-71362 account takeover; affects both cloud and on-premises deployments
- **VMware vCenter**: Versions affected by a critical remote-access flaw; critical for virtualization infrastructure management
- **Cisco ASA and FTD**: Secure Firewall Adaptive Security Appliance and Threat Defense software versions vulnerable to remote DoS
- **Belgium eID Browser Extension**: The middleware extension used for citizen authentication across Belgian government services
- **SAP Commerce Cloud**: Data Hub Adapter component vulnerable to unauthenticated RCE; affects cloud-hosted commerce implementations
- **Salesforce Experience Cloud**: Misconfigured sites exposing data to anonymous access, targeted by City-Forum campaign
- **ServiceNow**: Customer portal instances with excessive anonymous access permissions, targeted by City-Forum campaign
- **Google Chrome**: Browser hosting 737 malicious VPN/proxy extensions on Chrome Web Store; primarily affecting Russian-speaking users
- **Android Devices**: Targeted by WindRelay NFC relay malware and SpyNote RAT combination for payment card theft and loan fraud
- **PyPI / Python Supply Chain**: Organizations using LiteLLM library; 2,100+ potentially exposed via trojanized packages versions 1.72.1 and 1.72.2
- **Adobe ColdFusion, Campaign Classic**: Multiple CVSS 10.0 vulnerabilities patched in August 2026; exploitation status not confirmed in wild

## Attack Vectors and Techniques

- **Public PoC Weaponization**: Rapid exploitation of CVE-2026-55040 (SharePoint) and a vCenter flaw within days of PoC publication by Rapid7 and other researchers
- **Zero-Day Exploitation**: Lazarus Group leveraging CVE-2026-68820 before patch availability; ShieldBreak Defender bypass released immediately after Patch Tuesday
- **Browser Extension Compromise**: Malicious Chrome Web Store extensions (737 VPN/proxy tools) routing traffic through attacker SOCKS5 proxies; Belgium eID extension RCE via trust framework flaws
- **Supply Chain Injection**: Trojanized PyPI packages (LiteLLM) with credential harvester; automated build systems amplified impact to 2,100+ organizations
- **NFC Relay Attack**: WindRelay malware relaying live payment card data via NFC from victim Android devices to attacker-controlled terminals in real time
- **RAT-Enabled Financial Fraud**: SpyNote RAT providing remote control for loan application fraud and transaction authorization bypass on compromised Android devices
- **Anonymous Portal Enumeration**: City-Forum custom tooling scanning for misconfigured Salesforce Experience Cloud and ServiceNow portals with excessive anonymous permissions
- **Plug and Play Abuse**: "Plug and Pwn" technique forcing Windows to install vulnerable vendor drivers via malicious USB device descriptors for SYSTEM escalation
- **Authentication Bypass**: SharePoint flaw allowing unauthenticated access; Adobe Commerce flaw enabling customer account takeover without credentials
- **AI Reasoning Extraction**: API flaw across OpenAI, Anthropic, and Google allowing weaker models to decode stronger models' hidden reasoning and extract API keys from session logs

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Exploiting Windows zero-day CVE-2026-68820 against defense-sector companies under Operation Dream Job; deploying novel backdoor with SYSTEM access; attributed to Microsoft Defender ShieldBreak research release
- **Jewelbug APT**: Hackers-for-hire operation conducting simultaneous state-sponsored espionage and cryptocurrency theft; operating from shared Web panel infrastructure; blurring line between APT and cybercrime
- **City-Forum Campaign Operators**: Long-running data theft operation active since at least March 2025; custom tooling targeting Salesforce and ServiceNow across multiple industry sectors; unknown attribution
- **Nightmare Eclipse / Chaotic Eclipse**: Security researcher releasing ShieldBreak Microsoft Defender zero-day PoC; multiple aliases (INFINITE NIGHTMARE, MSNightmare); published bypass immediately after August 2026 Patch Tuesday
- **Malicious PyPI Publishers**: Actors uploading trojanized LiteLLM packages tied to Trivy scanner compromise; credential theft targeting cloud infrastructure secrets; 40-minute window but high-impact downstream
- **Chrome Extension Operators**: Single provider operating 737 malicious VPN/proxy extensions on Chrome Web Store; targeting Russian-speaking users seeking censorship circumvention; traffic interception via SOCKS5 proxies
- **Android Malware Operators**: Deploying WindRelay + SpyNote combination for real-time payment card relay and loan fraud; financially motivated with sophisticated NFC exploitation
- **Cisco ASA/FTD Exploiters**: Unknown actors exploiting firewall DoS vulnerability in the wild; likely reconnaissance or diversion tactic
- **FBI-Warned Account Compromise Actors**: Cybercriminals targeting social media and online accounts of adults and children for explicit content theft; sextortion and blackmail follow-on
- **Colombian Justice Ministry Ransomware Actors**: Ransomware group targeting government critical infrastructure during presidential transition; part of increased Latin American activity trend
