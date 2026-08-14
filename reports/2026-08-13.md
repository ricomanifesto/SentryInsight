---
schema_version: 2
report_date: 2026-08-13
generated_at: 2026-08-13T21:54:18Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-13/
---
# Exploitation Report

## Executive Summary

A global exploitation campaign targeting **CVE-2026-59310** in VMware vCenter Server has emerged as the most critical active threat, with multiple threat intelligence sources confirming widespread exploitation for reverse SSH persistence and remote code execution since early August. The vulnerability carries a CVSS 9.8 rating and affects the vCenter Syslog Server component, with evidence indicating that patching alone may not fully mitigate risk due to potential pre-compromise persistence. Simultaneously, North Korean state-sponsored actor **Lazarus Group** is actively exploiting an unpatched Windows zero-day vulnerability to deploy a novel backdoor across defense and aerospace targets in France, Germany, Brazil, and India as part of the long-running Operation Dream Job campaign.

Microsoft's July 2026 Patch Tuesday addressed several actively exploited flaws, including the **LegacyHive** Windows zero-day and **CVE-2026-55040** (CVSS 9.1), a SharePoint authentication bypass now under active exploitation following public proof-of-concept release. Adobe Commerce platforms face exploitation attempts against **CVE-2026-71362** for customer account hijacking, while a long-running "City-Forum" data theft campaign continues harvesting exposed data from Salesforce Experience Cloud and ServiceNow portals using custom tooling. The threat landscape also shows increasing abuse of legitimate system features—including Windows Safe Mode for EDR evasion by Akira ransomware affiliates, Plug and Play for SYSTEM privilege escalation, and malicious Chrome extensions at massive scale (737 identified)—alongside supply chain compromises affecting Trezor customers via ShipMonk and over 2,100 organizations through trojanized LiteLLM packages on PyPI.

## Active Exploitation Details

### VMware vCenter Server Directory Traversal and RCE (CVE-2026-59310)
- **Description**: A critical directory-traversal vulnerability in VMware vCenter Server's Syslog Server component that allows unauthenticated attackers with network access to execute arbitrary code. Multiple independent sources confirm active exploitation campaigns deploying reverse SSH tunnels for persistent remote access.
- **Impact**: Full remote code execution on vCenter Server, enabling persistent administrative access, lateral movement across virtualized infrastructure, and potential compromise of all managed ESXi hosts and virtual machines.
- **Status**: Actively exploited in the wild since early August 2026. Patches are available from Broadcom/VMware, but security researchers warn patching may not remove established persistence mechanisms such as reverse SSH tunnels.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw), [Bleeping Computer — Critical VMware vCenter RCE flaw exploited for reverse SSH access](https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/), [The Hacker News — Attackers Exploit VMware vCenter Vulnerability to Gain Persistent Remote Access](https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html)

### Microsoft SharePoint Authentication Bypass (CVE-2026-55040)
- **Description**: A critical security feature bypass vulnerability stemming from weak authentication in Microsoft SharePoint. The flaw allows attackers to bypass authentication controls entirely. A public proof-of-concept exploit was released following the July 2026 Patch Tuesday, triggering immediate active exploitation.
- **Impact**: Unauthenticated attackers can bypass SharePoint authentication, potentially accessing sensitive documents, escalating privileges, and moving laterally within Microsoft 365 and on-premises SharePoint environments.
- **Status**: Patched in July 2026 Patch Tuesday. Active exploitation confirmed following public PoC release.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### Adobe Commerce / Magento Customer Account Hijacking (CVE-2026-71362)
- **Description**: A critical vulnerability in Adobe Commerce and Magento e-commerce platforms that enables attackers to hijack customer accounts. Exploitation attempts have been detected in the wild.
- **Impact**: Attackers can take over customer accounts on affected e-commerce sites, accessing personal data, order history, payment information, and potentially making fraudulent purchases.
- **Status**: Exploitation attempts actively detected. Adobe has released patches for affected versions.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-71362
- **Reporting**: [Bleeping Computer — Hackers exploit critical Adobe Commerce flaw to hijack customer accounts](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-adobe-commerce-flaw-to-hijack-customer-accounts/)

### Windows LegacyHive Zero-Day Vulnerability
- **Description**: A Windows zero-day vulnerability codenamed "LegacyHive" that was disclosed and patched during the July 2026 Patch Tuesday. The vulnerability was actively exploited prior to patch release.
- **Impact**: Specific technical details were not disclosed in the source article, but as a patched zero-day, it enabled privilege escalation or remote code execution on affected Windows versions.
- **Status**: Patched in July 2026 Patch Tuesday. Was actively exploited as a zero-day prior to patch availability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Microsoft patches LegacyHive Windows zero-day vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/)

### Lazarus Group Windows Zero-Day Exploitation (Operation Dream Job)
- **Description**: The North Korean Lazarus Group is exploiting a newly patched Windows zero-day vulnerability to gain SYSTEM-level access and deploy a previously unseen backdoor. This activity is part of Operation Dream Job, a long-running cyber espionage campaign targeting defense and aerospace sectors.
- **Impact**: SYSTEM-level compromise of target systems, deployment of custom backdoor for persistent espionage access, targeting defense and aerospace companies in France, Germany, Brazil, and India.
- **Status**: Active exploitation by a sophisticated nation-state actor. Microsoft has released a patch for the underlying vulnerability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### Adobe ColdFusion OS Command Injection (CVE-2026-48362)
- **Description**: An operating system command injection vulnerability in Adobe ColdFusion rated CVSS 10.0, the maximum severity score. This was among three critical flaws patched by Adobe across ColdFusion, Commerce, and Campaign Classic.
- **Impact**: Unauthenticated remote code execution with the privileges of the ColdFusion service, potentially leading to full server compromise.
- **Status**: Patched by Adobe in August 2026 updates. Exploitation status in the wild not explicitly confirmed in source articles.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: patch
- **CVE IDs**: CVE-2026-48362
- **Reporting**: [The Hacker News — Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws](https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html)

### Belgium eID Browser Extension RCE Vulnerabilities
- **Description**: Severe vulnerabilities in a key browser extension used for Belgium's electronic ID (eID) authentication system, fully compromising the trust framework underlying citizen authentication. The flaws enable remote code execution.
- **Impact**: Complete compromise of citizen authentication for Belgian eID system, enabling identity theft, unauthorized access to government services, and potential RCE on user systems.
- **Status**: Vulnerabilities disclosed. Remediation status of the browser extension not specified in source.
- **Severity**: critical
- **Exploitation Status**: unknown
- **Action**: investigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Akira Ransomware EDR Evasion via Safe Mode
- **Description**: Akira ransomware affiliates are disabling Endpoint Detection and Response (EDR) solutions by restarting compromised systems into Safe Mode with Networking, where EDR drivers and services typically do not load.
- **Impact**: Bypass of advanced endpoint protection, enabling unimpeded ransomware execution, data theft, and encryption attempts. In the observed case, data was stolen but encryption failed.
- **Status**: Active technique in use by Akira affiliates. No patch available—this is a defense evasion technique abusing a legitimate Windows feature.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Akira hackers disable EDR with Safe Mode, steal data but fail to encrypt](https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/)

### Plug and Pwn: Windows Plug and Play Abuse for SYSTEM Access
- **Description**: A novel attack technique abusing the Windows Plug and Play feature to trigger automatic installation of vulnerable or insecure vendor-signed drivers/software, resulting in SYSTEM-level privilege escalation.
- **Impact**: Local privilege escalation to SYSTEM without exploiting a traditional vulnerability, leveraging legitimate Windows driver installation mechanisms and vulnerable vendor software.
- **Status**: Proof-of-concept/research disclosure. Active exploitation in the wild not explicitly confirmed.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Plug and Pwn attack uses fake USB devices for Windows SYSTEM access](https://www.bleepingcomputer.com/news/security/plug-and-pwn-attack-uses-fake-usb-devices-for-windows-system-access/)

### Android NFC Relay Malware (WindRelay + SpyNote)
- **Description**: A combination of WindRelay NFC relay malware and SpyNote remote administration tool (RAT) that steals live credit card data via NFC relay and exfiltrates it in real time, while also enabling full device control.
- **Impact**: Real-time theft of physical credit card data via NFC relay attacks, full device compromise via RAT capabilities, fraudulent loan applications initiated on victim devices.
- **Status**: Active malware campaign observed in the wild.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Android malware combo takes out loans and relays victims' credit cards](https://www.bleepingcomputer.com/news/security/android-malware-combo-takes-out-loans-and-relays-victims-credit-cards/)

### City-Forum Data Theft Campaign (Salesforce/ServiceNow)
- **Description**: A long-running campaign active since at least March 2025 using custom tooling to enumerate and extract data exposed to anonymous users through Salesforce Experience Cloud sites and ServiceNow customer portals.
- **Impact**: Large-scale data theft from misconfigured cloud portals, potentially exposing customer PII, support tickets, internal documents, and business data across multiple sectors.
- **Status**: Active ongoing campaign with custom tooling. Not a vulnerability in the platforms themselves but exploitation of misconfigurations.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — "City-Forum" data-theft attacks target Salesforce, ServiceNow portals](https://www.bleepingcomputer.com/news/security/city-forum-data-theft-attacks-target-salesforce-servicenow-portals/), [Dark Reading — Long-running Data Theft Campaign Targeting Salesforce, ServiceNow](https://www.darkreading.com/cyberattacks-data-breaches/long-running-data-theft-campaign-salesforce-servicenow)

### Malicious Chrome VPN Extensions (737 Extensions)
- **Description**: Over 737 malicious Chrome Web Store extensions impersonating legitimate VPN and proxy services, routing user traffic through attacker-controlled SOCKS5 proxy infrastructure. Published across 40+ developer accounts with 75,000+ combined installs, primarily targeting Russian-speaking users.
- **Impact**: Full interception of browser traffic, credential harvesting, session hijacking, and potential injection of malicious content. 274 extensions impersonated 66 legitimate VPN brands.
- **Status**: Active on Chrome Web Store until discovery. Google has been notified; removal status ongoing.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hundreds of fake Chrome VPN extensions route traffic through a proxy](https://www.bleepingcomputer.com/news/security/hundreds-of-fake-chrome-vpn-extensions-route-traffic-through-a-proxy/), [The Hacker News — 737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One](https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html)

### Supply Chain Compromise: Trojanized LiteLLM Packages on PyPI
- **Description**: Two malicious LiteLLM releases published on PyPI for approximately 40 minutes in March 2026, containing credential-stealing code that harvested cloud keys, SSH keys, Kubernetes tokens, database passwords, and other secrets. Linked to a compromise of the Trivy security scanner project.
- **Impact**: Potential exposure of 2,100+ organizations that may have installed the malicious packages. Attackers captured approximately 434,000 files containing secrets and credentials.
- **Status**: Packages removed from PyPI. Incident response ongoing for potentially affected organizations.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Malicious LiteLLM Releases Tied to Trivy Hack May Have Exposed 2,100+ Organizations](https://thehackernews.com/2026/08/malicious-litellm-releases-tied-to.html)

### Trezor Data Breach via ShipMonk Supply Chain
- **Description**: Hardware wallet manufacturer Trezor disclosed a breach affecting nearly 14,000 customers after its shipping and logistics provider ShipMonk was compromised.
- **Impact**: Exposure of customer shipping information (names, addresses, emails, phone numbers) for cryptocurrency hardware wallet users, enabling targeted physical and phishing attacks.
- **Status**: Breach disclosed. ShipMonk compromise confirmed.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Trezor discloses data breach affecting nearly 14,000 customers](https://www.bleepingcomputer.com/news/security/trezor-discloses-data-breach-affecting-nearly-14-000-customers/)

## Affected Systems and Products

- **VMware vCenter Server**: All versions with Syslog Server component enabled prior to patched releases. Critical infrastructure virtualization management platform.
- **Microsoft SharePoint**: On-premises SharePoint Server and Microsoft 365 SharePoint Online affected by CVE-2026-55040 authentication bypass.
- **Adobe Commerce / Magento**: E-commerce platform versions prior to August 2026 security patches (CVE-2026-71362).
- **Adobe ColdFusion**: Versions prior to August 2026 security updates (CVE-2026-48362 and related flaws).
- **Adobe Campaign Classic**: Affected by critical patches in Adobe's August 2026 release.
- **Microsoft Windows**: Multiple versions affected by LegacyHive zero-day and the Lazarus-exploited zero-day (both patched July 2026).
- **Belgium eID Browser Extension**: The middleware extension used for Belgian national electronic identity authentication in web browsers.
- **Salesforce Experience Cloud**: Sites with misconfigured anonymous/public access settings targeted by City-Forum campaign.
- **ServiceNow Customer Portals**: Instances with excessive anonymous access permissions targeted by City-Forum campaign.
- **Android Devices**: Devices running malicious WindRelay/SpyNote applications, typically installed via social engineering.
- **Google Chrome Browser**: Users who installed any of the 737 malicious VPN/proxy extensions from Chrome Web Store.
- **Python/PyPI Ecosystem**: Organizations that installed LiteLLM versions 1.72.0 or 1.72.1 during the ~40-minute compromise window in March 2026.
- **Trezor Hardware Wallet Customers**: Approximately 14,000 customers whose shipping data was exposed via ShipMonk breach.

## Attack Vectors and Techniques

- **Reverse SSH Persistence via vCenter Exploitation**: Attackers exploit CVE-2026-59310 to deploy reverse SSH tunnels, establishing persistent remote access that survives patching and reboot. This provides long-term foothold in virtualization management infrastructure.
- **Public PoC-Driven Exploitation (SharePoint)**: Rapid weaponization of CVE-2026-55040 following proof-of-concept release, demonstrating the shrinking window between disclosure and active exploitation for authentication bypass flaws.
- **Safe Mode EDR Evasion**: Akira ransomware affiliates reboot compromised endpoints into Safe Mode with Networking, where EDR kernel drivers and monitoring services are not loaded, allowing unimpeded execution of malicious tools.
- **Windows Plug and Play Abuse (Plug and Pwn)**: Attackers connect malicious USB devices or emulate them to trigger automatic installation of vulnerable vendor-signed drivers/software via Windows' legitimate PnP mechanism, achieving SYSTEM privileges without memory corruption exploits.
- **Anonymous Cloud Portal Enumeration (City-Forum)**: Custom tooling systematically scans Salesforce Experience Cloud and ServiceNow instances for data exposed to unauthenticated/anonymous users, extracting customer records, support tickets, and internal documents.
- **NFC Relay Attack (WindRelay)**: Malware relays live NFC communications from victim's physical credit card (via compromised Android device) to attacker's device in real time, enabling card-present fraud without physical card access.
- **Malicious Browser Extensions at Scale**: 737 extensions published across 40+ developer accounts on Chrome Web Store, using brand impersonation and legitimate-seeming functionality to achieve 75,000+ installs before detection.
- **Supply Chain Injection (PyPI/LiteLLM)**: Attackers compromised the Trivy project or its build pipeline to publish trojanized LiteLLM packages on PyPI, harvesting secrets from CI/CD pipelines and developer environments.
- **Logistics Provider Compromise**: Attackers breached ShipMonk (shipping/logistics provider) to access Trezor customer data, demonstrating risk from third-party vendors with access to sensitive customer information.
- **Operation Dream Job Social Engineering**: Lazarus Group uses fake job offers targeting defense/aerospace professionals to deliver payloads exploiting Windows zero-day, combining social engineering with zero-day exploitation.
- **API Reasoning Replay Attack**: Researchers demonstrated that encrypted reasoning objects from OpenAI, Anthropic, and Google APIs can be captured from one session and replayed into another to extract internal reasoning, API keys, and passwords.

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Active exploitation of Windows zero-day for SYSTEM access and novel backdoor deployment targeting defense/aerospace sectors in France, Germany, Brazil, and India under Operation Dream Job. High-confidence attribution by Check Point Research.
- **Akira Ransomware Affiliates**: Active use of Safe Mode reboot technique to disable EDR, conducting data theft and attempted encryption operations. Demonstrates adaptive defense evasion by ransomware operators.
- **Jewelbug APT (Hackers-for-Hire)**: Conducting dual-mission operations—government/military espionage via webmail breaches alongside cryptocurrency fraud for financial gain. Researchers identified shared infrastructure and web panel usage for both mission types.
- **City-Forum Campaign Operators**: Long-running (since March 2025) data theft campaign targeting Salesforce Experience Cloud and ServiceNow portals across multiple sectors using custom enumeration and extraction tooling. Attribution unknown.
- **Unknown Actors (VMware vCenter Campaign)**: Multiple exploitation campaigns leveraging CVE-2026-59310 for reverse SSH persistence and remote access. QUIRSO and other researchers observe active exploitation but have not attributed to specific groups.
- **Unknown Actors (SharePoint Exploitation)**: Rapid exploitation of CVE-2026-55040 following PoC release. No specific attribution in source articles.
- **Unknown Actors (Adobe Commerce Exploitation)**: Active exploitation attempts against CVE-2026-71362 for customer account hijacking. No attribution provided.
- **Chrome VPN Extension Operators**: Coordinated operation across 40+ Chrome Web Store developer accounts publishing 737 malicious extensions impersonating 66 legitimate VPN brands, targeting Russian-speaking users with 75,000+ total installs.
- **LiteLLM/Trivy Supply Chain Attackers**: Unknown actors who compromised the Trivy project or its publishing pipeline to inject credential-stealing code into LiteLLM packages on PyPI, potentially affecting 2,100+ organizations.
- **ShipMonk Breach Actors**: Unknown threat actors who compromised ShipMonk logistics platform to access Trezor customer shipping data (14,000 records).
