---
schema_version: 2
report_date: 2026-08-14
generated_at: 2026-08-14T08:01:30Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-14/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with VMware vCenter, Microsoft SharePoint, and Adobe Commerce platforms facing immediate threats. A global campaign targeting CVE-2026-59310 in VMware vCenter has established persistent reverse SSH access on compromised systems, while threat actors rapidly weaponized a public proof-of-concept for CVE-2026-55040 in SharePoint following its July 2026 patch. Adobe Commerce sites are experiencing exploitation attempts against CVE-2026-71362 aimed at customer account takeover. Two separate Windows zero-day vulnerabilities—LegacyHive and an unnamed flaw exploited by the Lazarus Group—were patched in July 2026 after confirmed in-the-wild exploitation, with the latter deployed against defense and aerospace targets across four countries as part of Operation Dream Job.

Simultaneously, sophisticated threat actors are conducting espionage and financially motivated operations without relying on traditional vulnerability exploitation. Apple has issued new Threat Notifications warning of mercenary spyware targeting iPhone users, while the Jewelbug APT balances government webmail intrusions with cryptocurrency fraud. The long-running "City-Forum" campaign continues stealing data from misconfigured Salesforce and ServiceNow portals using custom tooling. Supply chain attacks have surfaced through 737 malicious Chrome VPN extensions proxying user traffic and two credential-stealing LiteLLM packages on PyPI. Akira ransomware affiliates have adopted a novel Safe Mode technique to disable EDR solutions, demonstrating evolving post-exploitation tradecraft.

## Active Exploitation Details

### CVE-2026-59310 - VMware vCenter Directory Traversal RCE
- **Description**: A critical directory-traversal vulnerability in VMware vCenter Server (CVSS 9.8) that allows a malicious actor with network access to execute arbitrary code. The flaw resides in the vCenter Syslog Server component and enables unauthenticated remote code execution.
- **Impact**: Attackers gain full control of vCenter servers, deploying reverse SSH tools for persistent remote access and lateral movement within virtualized infrastructure.
- **Status**: Actively exploited in a global campaign; patches released but may not fully mitigate threat if compromise already occurred.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw), [Bleeping Computer — Critical VMware vCenter RCE flaw exploited for reverse SSH access](https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/), [The Hacker News — Attackers Exploit VMware vCenter Vulnerability to Gain Persistent Remote Access](https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html)

### CVE-2026-55040 - Microsoft SharePoint Authentication Bypass
- **Description**: A critical security feature bypass (CVSS 9.1) stemming from weak authentication in Microsoft SharePoint. The vulnerability allows authentication bypass and was patched as part of the July 2026 Patch Tuesday updates.
- **Impact**: Attackers can bypass authentication controls to access SharePoint resources, potentially leading to data exfiltration, privilege escalation, and further network compromise.
- **Status**: Active exploitation observed following public PoC release; patch available since July 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### CVE-2026-71362 - Adobe Commerce/Magento Account Hijacking
- **Description**: A critical vulnerability in Adobe Commerce and Magento e-commerce platforms that allows attackers to hijack customer accounts.
- **Impact**: Successful exploitation enables account takeover, potentially leading to payment fraud, personal data theft, and unauthorized transactions on affected e-commerce sites.
- **Status**: Exploitation attempts actively detected in the wild; patch status not specified in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-71362
- **Reporting**: [Bleeping Computer — Hackers exploit critical Adobe Commerce flaw to hijack customer accounts](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-adobe-commerce-flaw-to-hijack-customer-accounts/)

### LegacyHive Windows Zero-Day Vulnerability
- **Description**: A Windows zero-day vulnerability codenamed "LegacyHive" that was actively exploited before being patched in the July 2026 Patch Tuesday release.
- **Impact**: As a zero-day, it provided attackers with an undisclosed capability (likely privilege escalation or remote code execution) against unpatched Windows systems.
- **Status**: Patched as of July 2026 Patch Tuesday; exploitation confirmed prior to patch.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Microsoft patches LegacyHive Windows zero-day vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/)

### Lazarus Group Windows Zero-Day Exploitation
- **Description**: An undisclosed Windows zero-day vulnerability exploited by the North Korean Lazarus Group to gain SYSTEM access and deploy a never-before-seen backdoor. The flaw was patched in a recent Microsoft update.
- **Impact**: Full SYSTEM-level compromise enabling persistent backdoor access, targeting defense and aerospace organizations in France, Germany, Brazil, and India as part of Operation Dream Job.
- **Status**: Actively exploited in targeted espionage campaign; patch released.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### Apple Mercenary Spyware Attacks
- **Description**: Apple has issued new Threat Notifications to users detecting "mercenary spyware attacks" targeting iPhones, indicating active exploitation of likely zero-day vulnerabilities in iOS by commercial spyware vendors.
- **Impact**: Full device compromise enabling surveillance, data exfiltration, and persistent monitoring of high-value targets.
- **Status**: Active targeting confirmed via Apple Threat Notifications; no public patch information available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Apple sends new ‘Threat Notification’ alerts over mercenary spyware attacks](https://www.bleepingcomputer.com/news/apple/apple-sends-new-threat-notification-alerts-over-mercenary-spyware-attacks/)

### Akira Ransomware Safe Mode EDR Bypass
- **Description**: Akira ransomware affiliates are disabling Endpoint Detection and Response (EDR) solutions by restarting compromised systems into Safe Mode with Networking, where EDR agents typically do not run.
- **Impact**: Attackers evade detection during critical post-exploitation phases, enabling data theft and encryption attempts without interference from security tools.
- **Status**: Actively used in intrusions; no patch applicable (technique abuse).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Akira hackers disable EDR with Safe Mode, steal data but fail to encrypt](https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/)

### Jewelbug APT Espionage and Fraud Operations
- **Description**: The Jewelbug hacker group conducts simultaneous cyber espionage against governments and militaries while operating cryptocurrency fraud schemes, accessed through compromised government webmail systems.
- **Impact**: Sensitive government communications exposed alongside financial theft via crypto fraud, indicating dual-mission operational posture.
- **Status**: Ongoing campaigns observed; initial access vector not specified in reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers breach govt webmail while running parallel crypto fraud](https://www.bleepingcomputer.com/news/security/hackers-breach-govt-webmail-while-running-parallel-crypto-fraud/), [Dark Reading — 'Jewelbug' APT Balances State Espionage & Cryptocurrency Theft](https://www.darkreading.com/threat-intelligence/jewelbug-apt-state-espionage-cryptocurrency-theft)

### City-Forum Data Theft Campaign
- **Description**: A long-running campaign (active since at least March 2025) using custom tools to steal data exposed through anonymous access misconfigurations in Salesforce Experience Cloud and ServiceNow customer portals across multiple sectors.
- **Impact**: Large-scale data theft from enterprise CRM and ITSM platforms without requiring vulnerability exploitation—leveraging excessive anonymous permissions.
- **Status**: Active ongoing campaign with custom tooling; mitigation requires configuration review.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — "City-Forum" data-theft attacks target Salesforce, ServiceNow portals](https://www.bleepingcomputer.com/news/security/city-forum-data-theft-attacks-target-salesforce-servicenow-portals/), [Dark Reading — Long-running Data Theft Campaign Targeting Salesforce, ServiceNow](https://www.darkreading.com/cyberattacks-data-breaches/long-running-data-theft-campaign-salesforce-servicenow)

### Malicious Chrome VPN Extensions Campaign
- **Description**: Over 737 malicious browser extensions published on the Chrome Web Store impersonate legitimate VPN/proxy services while routing user traffic through attacker-controlled SOCKS5 proxies, amassing 75,486 installs across 40+ developer accounts.
- **Impact**: Interception and proxying of all browser traffic, enabling credential harvesting, session hijacking, and surveillance of affected users (primarily Russian-speaking).
- **Status**: Active on Chrome Web Store at time of reporting; 274 extensions impersonate 66 known brands.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hundreds of fake Chrome VPN extensions route traffic through a proxy](https://www.bleepingcomputer.com/news/security/hundreds-of-fake-chrome-vpn-extensions-route-traffic-through-a-proxy/), [The Hacker News — 737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One](https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html)

### Malicious LiteLLM Supply Chain Attack
- **Description**: Two malicious LiteLLM packages uploaded to PyPI in March 2026 contained credential-stealing code harvesting cloud keys, SSH keys, Kubernetes tokens, and database passwords. Packages remained available for approximately 40 minutes, potentially exposing 2,100+ organizations.
- **Impact**: Compromise of developer and CI/CD environments with access to cloud infrastructure, containers, and databases via stolen secrets.
- **Status**: Packages removed; exposure window closed but compromise assessment required for affected organizations.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Malicious LiteLLM Releases Tied to Trivy Hack May Have Exposed 2,100+ Organizations](https://thehackernews.com/2026/08/malicious-litellm-releases-tied-to.html)

### Belgium eID Authentication RCE Vulnerabilities
- **Description**: Severe vulnerabilities in a key browser extension underlying Belgium's electronic ID (eID) system fully compromise the trust framework, enabling remote code execution against citizen accounts.
- **Impact**: Complete compromise of eID authentication for Belgian citizens, enabling identity theft, unauthorized access to government services, and digital signature forgery.
- **Status**: Vulnerabilities identified in browser extension component; patch status not specified.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Colombian Justice Ministry Ransomware Attack
- **Description**: Ransomware operators successfully compromised the Colombian Justice Ministry days before a presidential transition, continuing a pattern of targeting critical government infrastructure in Latin America.
- **Impact**: Disruption of judicial operations, potential data exfiltration, and operational paralysis during a sensitive political transition period.
- **Status**: Active incident; initial access vector not specified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — Ransomware Hits Colombian Justice Ministry Days Before Presidential Transition](https://www.darkreading.com/cyberattacks-data-breaches/ransomware-hits-colombian-justice-ministry-presidential-transition)

## Affected Systems and Products

- **VMware vCenter Server / vCenter Syslog Server**: Versions vulnerable to CVE-2026-59310; directory traversal leads to unauthenticated RCE
- **Microsoft SharePoint**: Versions prior to July 2026 Patch Tuesday affected by CVE-2026-55040 authentication bypass
- **Adobe Commerce / Magento**: E-commerce platforms vulnerable to CVE-2026-71362 customer account hijacking
- **Microsoft Windows**: Systems unpatched against LegacyHive zero-day and Lazarus-exploited zero-day (both addressed in July 2026 Patch Tuesday)
- **Apple iOS / iPhone**: Devices targeted by mercenary spyware campaigns triggering Apple Threat Notifications
- **Salesforce Experience Cloud**: Customer portals with misconfigured anonymous access permissions exploited by City-Forum campaign
- **ServiceNow**: Customer portals with excessive anonymous data exposure targeted by City-Forum campaign
- **Google Chrome Browser**: Users who installed any of 737 malicious VPN/proxy extensions from Chrome Web Store
- **Python/PyPI Ecosystem**: Organizations that installed malicious LiteLLM packages (versions published March 2026)
- **Belgium eID Browser Extension**: Component underlying national electronic ID system with RCE vulnerabilities
- **Adobe ColdFusion**: Versions affected by CVE-2026-48362 (CVSS 10.0 OS command injection) and other patched flaws
- **Android Devices**: Targets of WindRelay NFC relay malware and SpyNote RAT combination for financial fraud

## Attack Vectors and Techniques

- **Directory Traversal to RCE**: Exploitation of CVE-2026-59310 in VMware vCenter via crafted requests to Syslog Server component, enabling arbitrary code execution and reverse SSH deployment for persistence
- **Authentication Bypass via Weak Controls**: CVE-2026-55040 in SharePoint exploited after public PoC release, allowing unauthorized access through flawed authentication logic
- **Customer Account Takeover**: CVE-2026-71362 in Adobe Commerce exploited to hijack user sessions and credentials on e-commerce platforms
- **Zero-Day Exploitation**: Two distinct Windows zero-days (LegacyHive and Lazarus-attributed) exploited pre-patch for SYSTEM-level access and backdoor deployment
- **Mercenary Spyware Delivery**: Commercial surveillance tools (likely Pegasus-class) targeting iPhones via zero-click or one-click exploits, detected by Apple's Threat Notification system
- **Safe Mode EDR Evasion**: Akira affiliates reboot compromised hosts into Safe Mode with Networking to disable EDR agents that don't load in minimal boot environment
- **Anonymous Data Exposure Exploitation**: City-Forum campaign uses custom tooling to enumerate and extract data from Salesforce/ServiceNow portals with misconfigured public access
- **Malicious Browser Extension Distribution**: 737 Chrome extensions published under 40+ developer accounts impersonate legitimate VPNs to route traffic through attacker SOCKS5 proxies
- **Supply Chain Package Compromise**: Typosquat or dependency confusion via malicious LiteLLM packages on PyPI delivering credential-stealing payloads to developer environments
- **Browser Extension RCE**: Vulnerabilities in Belgium's eID browser extension enable remote code execution against citizen authentication flows
- **Dual-Purpose Espionage/Fraud Infrastructure**: Jewelbug APT uses same web panel for government webmail intrusion and cryptocurrency fraud operations
- **NFC Relay + RAT Combination**: WindRelay malware relays live credit card data via NFC while SpyNote RAT provides device control for loan fraud on Android

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Active exploitation of Windows zero-day to deploy novel backdoor against defense/aerospace targets in France, Germany, Brazil, and India under Operation Dream Job; attributed by Check Point Research
- **Jewelbug APT**: Hackers-for-hire conducting simultaneous state-sponsored espionage (government/military webmail breach) and financially motivated cryptocurrency fraud from shared infrastructure
- **Akira Ransomware Affiliates**: Operating with novel Safe Mode EDR bypass technique to disable defenses during data theft and encryption attempts
- **City-Forum Campaign Operators**: Long-running (since March 2025) data theft operation targeting Salesforce Experience Cloud and ServiceNow portals across multiple sectors using custom-built enumeration and exfiltration tools
- **Mercenary Spyware Vendors**: Commercial surveillance actors targeting high-value iPhone users, triggering Apple's Threat Notification system; likely NSO Group or similar operators
- **Chrome Extension Threat Actors**: Coordinated campaign publishing 737 malicious VPN/proxy extensions across 40+ Chrome Web Store developer accounts, primarily targeting Russian-speaking users seeking censorship circumvention
- **LiteLLM Supply Chain Attackers**: Unknown operators who published credential-stealing PyPI packages tied to the Trivy security scanner compromise, harvesting cloud/SSH/Kubernetes secrets
- **Colombian Justice Ministry Ransomware Operators**: Unidentified ransomware group targeting critical government infrastructure during presidential transition period, consistent with increased Latin American activity
- **VMware vCenter Campaign Actors**: Unattributed threat actors conducting global exploitation of CVE-2026-59310 for persistent reverse SSH access; potentially multiple groups given widespread activity
- **SharePoint PoC Weaponizers**: Opportunistic attackers rapidly exploiting CVE-2026-55040 following public proof-of-concept release post-July 2026 patch
- **Adobe Commerce Exploiters**: Actors scanning for and exploiting CVE-2026-71362 to hijack customer accounts on Magento/Commerce platforms