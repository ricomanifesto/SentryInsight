---
schema_version: 2
report_date: 2026-08-15
generated_at: 2026-08-15T01:33:41Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-15/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity continues to accelerate across enterprise software, operating systems, and identity infrastructure. Two maximum-severity vulnerabilities—CVE-2026-59310 in VMware vCenter Syslog Server and CVE-2026-55040 in Microsoft SharePoint—are under active global exploitation within days of patch availability, with threat actors weaponizing public proof-of-concept code to establish persistent reverse SSH access and bypass authentication.

Simultaneously, multiple zero-day vulnerabilities in Windows (LegacyHive and a separate Lazarus Group-exploited flaw), macOS Screen Sharing, and Belgium's eID browser extension are being actively exploited for cryptojacking, espionage, and remote code execution against high-value targets.

State-sponsored and financially motivated threat actors are diversifying their operations. The North Korean Lazarus Group continues Operation Dream Job, exploiting a Windows zero-day to deploy novel backdoors against defense and aerospace organizations across four countries. The Jewelbug APT simultaneously conducts government espionage and cryptocurrency fraud from shared infrastructure. Ransomware groups Akira and Clop demonstrate evolving tactics—Akira affiliates now disable EDR via Safe Mode with Networking, while Clop claims 89GB exfiltration from Shell. The ShinyHunters extortion group breached 1.6 million RingCentral accounts, and a long-running City-Forum campaign has targeted Salesforce and ServiceNow environments since March 2025 with custom tooling.

Supply chain and identity-focused attacks are expanding rapidly. A service provider vulnerability enabled €30M bank fraud against Commerzbank customers, resulting in international arrests. Belgium's entire eID trust framework was compromised through severe browser extension vulnerabilities affecting citizen authentication. Over 737 malicious Chrome VPN extensions with 75,000+ installations were caught routing traffic through attacker-controlled proxies. Apple issued new Threat Notifications for mercenary spyware targeting iPhones, while a widespread data breach at the Scottish prosecutor's office may extend to other agencies through a shared third-party provider.

## Active Exploitation Details

### CVE-2026-59310 - VMware vCenter Syslog Server Remote Code Execution
- **Description**: A critical remote code execution vulnerability in VMware vCenter Syslog Server that allows unauthenticated attackers to execute arbitrary code on affected systems. The flaw resides in the syslog processing component and can be triggered remotely without authentication.
- **Impact**: Attackers achieve full system compromise, deploying reverse SSH tools for persistent remote access and lateral movement within virtualized infrastructure. Exploitation grants complete control over vCenter management infrastructure.
- **Status**: Actively exploited in a global threat campaign since early this month. Patches are available but may not fully mitigate risk if exploitation already occurred.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-59310
- **Reporting**: [Dark Reading — Global Threat Campaign Hits Critical VMware vCenter Flaw](https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw), [Bleeping Computer — Critical VMware vCenter RCE flaw exploited for reverse SSH access](https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/)

### CVE-2026-55040 - Microsoft SharePoint Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in Microsoft SharePoint (CVSS 9.1) stemming from weak authentication mechanisms. The flaw allows attackers to bypass security features and gain unauthorized access to SharePoint environments.
- **Impact**: Attackers can access sensitive documents, internal sites, and connected systems within Microsoft 365 ecosystems. The vulnerability provides a pathway to Gmail, Drive, and other connected services through the broader Workspace attack chain.
- **Status**: Actively exploited in the wild following public PoC code release. Patched in Microsoft's July 2026 Patch Tuesday updates.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-55040
- **Reporting**: [The Hacker News — Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

### macOS Screen Sharing Authentication Bypass
- **Description**: An authentication bypass vulnerability in macOS Screen Sharing that allows remote attackers to bypass authentication controls. Public exploit code emerged prior to active exploitation, enabling rapid weaponization.
- **Impact**: Attackers deploy Monero cryptocurrency miners on compromised macOS systems, consuming system resources for financial gain. The Netherlands' NCSC has issued warnings about active exploitation.
- **Status**: Actively exploited following public exploit code release. Patch status not specified in reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Hackers exploit macOS Screen Sharing flaw to deploy Monero miner](https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)

### SAP Commerce Cloud Remote Code Execution
- **Description**: A maximum-severity remote code execution vulnerability in SAP Commerce Cloud that was patched only three days before active targeting began. The flaw allows unauthenticated remote code execution on affected Commerce Cloud instances.
- **Impact**: Attackers can achieve full compromise of e-commerce platforms, accessing customer data, payment information, and backend systems. Threat intelligence firm Defused confirmed active targeting immediately post-patch.
- **Status**: Actively targeted in attacks within days of patch release. Patches are available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

### Microsoft LegacyHive Windows Zero-Day
- **Description**: A Windows zero-day vulnerability dubbed "LegacyHive" that was actively exploited before Microsoft released patches following the July 2026 Patch Tuesday. Details of the underlying flaw remain limited in public reporting.
- **Impact**: As a zero-day exploit, attackers achieved SYSTEM-level access on compromised Windows systems prior to patch availability, enabling full system compromise and persistence.
- **Status**: Patched by Microsoft after active exploitation as a zero-day. Patches released in July 2026 Patch Tuesday.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Microsoft patches LegacyHive Windows zero-day vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/)

### Lazarus Group Windows Zero-Day (Operation Dream Job)
- **Description**: A separate Windows zero-day vulnerability exploited by the North Korean Lazarus Group as part of Operation Dream Job, a long-running cyber espionage campaign. The flaw enables SYSTEM-level access and deployment of a never-before-seen backdoor.
- **Impact**: Targets defense and aerospace companies in France, Germany, Brazil, and India. Provides persistent SYSTEM access and custom backdoor deployment for long-term espionage.
- **Status**: Actively exploited in targeted attacks. Patch status not specified in reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

### Belgium eID Browser Extension Remote Code Execution
- **Description**: Severe vulnerabilities in a key browser extension underlying Belgium's electronic ID (eID) authentication system. The trust framework for citizen authentication was fully compromised, exposing fundamental weaknesses in browser extension security architecture.
- **Impact**: Remote code execution on citizen systems, complete compromise of the eID trust framework, potential access to government services, banking, and identity verification for all Belgian citizens using the system.
- **Status**: Vulnerabilities identified and framework compromised. Remediation status not specified.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Dark Reading — Belgium's eID Authentication Opens Citizen Accounts to RCE](https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce)

### Service Provider Vulnerability (Commerzbank Fraud)
- **Description**: An unspecified vulnerability at a service provider that allowed cybercriminals to withdraw funds from Commerzbank customers' accounts, resulting in €30M fraud. Four perpetrators arrested in Brazil, three charged in Europe.
- **Impact**: Direct financial theft from bank customers, compromise of banking authentication/authorization flows through third-party service provider.
- **Status**: Law enforcement action completed with arrests. Vulnerability presumably remediated.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers arrested over €30M bank fraud exploiting service provider flaw](https://www.bleepingcomputer.com/news/security/hackers-arrested-over-30m-bank-fraud-exploiting-service-provider-flaw/)

### Malicious Chrome VPN Extensions Traffic Interception
- **Description**: 737 malicious Chrome VPN and proxy extensions (across 40+ developer accounts) with 75,486 total installations were found intercepting browser traffic and routing it through attacker-controlled proxy infrastructure. 274 extensions impersonated 66 legitimate brands.
- **Impact**: Full visibility into victims' browsing traffic, credential harvesting, session hijacking, and potential injection of malicious content. Primarily targeted Russian-speaking users seeking blocked services.
- **Status**: Extensions identified and presumably removed from Chrome Web Store. 75,000+ installations already occurred.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — 737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One](https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html)

### Mercenary Spyware iPhone Attacks
- **Description**: Apple issued new Threat Notifications to users targeted by mercenary spyware attacks on iPhones. The specific vulnerabilities exploited were not disclosed, but such attacks typically leverage zero-day chains for silent installation.
- **Impact**: Full device compromise, access to communications, location data, credentials, and encryption keys. Targets are typically high-value individuals (journalists, activists, officials).
- **Status**: Active targeting confirmed by Apple's threat notifications. Apple mitigations deployed via notifications and likely silent patches.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Apple sends new ‘Threat Notification’ alerts over mercenary spyware attacks](https://www.bleepingcomputer.com/news/apple/apple-sends-new-threat-notification-alerts-over-mercenary-spyware-attacks/)

### Akira Ransomware Safe Mode EDR Bypass
- **Description**: An Akira ransomware affiliate demonstrated a novel technique to disable Endpoint Detection and Response (EDR) solutions by restarting compromised systems into Safe Mode with Networking, where EDR drivers typically do not load.
- **Impact**: EDR evasion enabling data exfiltration without encryption (in this observed case). Technique allows ransomware operators to operate unimpeded by behavioral monitoring.
- **Status**: Observed in active intrusion. No patch available—requires defensive configuration changes.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Akira hackers disable EDR with Safe Mode, steal data but fail to encrypt](https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/)

### Jewelbug Government Webmail Breach
- **Description**: The Jewelbug hacker group breached government webmail systems while simultaneously running cryptocurrency fraud operations. The group operates as hackers-for-hire performing both espionage and financially motivated heists from shared infrastructure.
- **Impact**: Government and military espionage, credential theft, cryptocurrency fraud. Dual-mission operations blur attribution lines between state-sponsored and criminal activity.
- **Status**: Active campaign observed. Initial access vector not specified in reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers breach govt webmail while running parallel crypto fraud](https://www.bleepingcomputer.com/news/security/hackers-breach-govt-webmail-while-running-parallel-crypto-fraud/), [Dark Reading — 'Jewelbug' APT Balances State Espionage & Cryptocurrency Theft](https://www.darkreading.com/threat-intelligence/jewelbug-apt-state-espionage-cryptocurrency-theft)

### City-Forum Salesforce/ServiceNow Data Theft Campaign
- **Description**: A long-running data theft campaign (active since at least March 2025) targeting Salesforce and ServiceNow environments across multiple sectors using custom tooling. The campaign demonstrates sophisticated understanding of SaaS platform internals.
- **Impact**: Theft of sensitive CRM and IT service management data, including customer records, internal communications, and operational data from enterprise SaaS platforms.
- **Status**: Ongoing campaign with custom tooling. Specific vulnerabilities exploited not publicly disclosed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Dark Reading — Long-running Data Theft Campaign Targeting Salesforce, ServiceNow](https://www.darkreading.com/cyberattacks-data-breaches/long-running-data-theft-campaign-salesforce-servicenow)

### Clop Ransomware Data Theft (Shell)
- **Description**: The Clop ransomware gang claimed theft of 89GB of data from Shell, prompting the oil giant to investigate a potential security incident. Clop continues to focus on data extortion over encryption.
- **Impact**: Large-scale data exfiltration from a major energy corporation, potential exposure of operational, financial, and proprietary data.
- **Status**: Claimed by threat actor, under investigation by victim. Initial access vector not specified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Shell investigates 'potential incident' after Clop data theft claims](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)

### ShinyHunters RingCentral Data Breach
- **Description**: The ShinyHunters extortion group breached RingCentral in July, stealing personal information from 1.6 million accounts. Data surfaced via Have I Been Pwned breach notification service.
- **Impact**: Exposure of personal information for 1.6 million RingCentral customers, enabling identity theft, phishing, and account takeover attacks.
- **Status**: Breach occurred in July, data now circulating. Initial access method not specified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — RingCentral data breach exposed info of 1.6 million accounts](https://www.bleepingcomputer.com/news/security/ringcentral-data-breach-exposed-info-of-16-million-accounts/)

### Scottish Government Prosecutor's Office Data Breach
- **Description**: A data breach at the Scottish prosecutor's office caused by a third-party service provider that may have serviced other government agencies, potentially widening the impact across the Scottish government.
- **Impact**: Compromise of legal/prosecutorial data, potential cascade to other agencies sharing the same third-party provider. Supply chain risk realization.
- **Status**: Breach reported, scope potentially widening. Third-party relationship under investigation.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — Scottish Govt Suffers Potentially Widening Data Breach at Prosecutor's Office](https://www.darkreading.com/cyberattacks-data-breaches/scottish-govt-data-breach-prosecutors-office)

### Colombian Justice Ministry Ransomware
- **Description**: Ransomware attack on the Colombian Justice Ministry days before a presidential transition, part of increased targeting of critical infrastructure and government organizations across Latin America.
- **Impact**: Disruption of judicial operations during political transition, potential data theft, operational paralysis of critical government functions.
- **Status**: Attack executed during sensitive political period. Ransomware variant and initial access not specified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Dark Reading — Ransomware Hits Colombian Justice Ministry Days Before Presidential Transition](https://www.darkreading.com/cyberattacks-data-breaches/ransomware-hits-colombian-justice-ministry-presidential-transition)

### Google Workspace OAuth Token Theft
- **Description**: Attackers leverage stolen OAuth tokens as an alternative initial access vector into Google Workspace environments (Gmail, Drive, connected systems), bypassing traditional phishing defenses and MFA.
- **Impact**: Full access to email, documents, and integrated applications without credential compromise. Tokens provide persistent access until explicitly revoked.
- **Status**: Active attack vector highlighted by Material Security. Not a vulnerability but an abused legitimate feature.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — The Modern Attack Chain: Rethinking Google Workspace Security in the Age of AI](https://www.bleepingcomputer.com/news/security/the-modern-attack-chain-rethinking-google-workspace-security-in-the-age-of-ai/)

## Affected Systems and Products

- **VMware vCenter Syslog Server**: All versions prior to patched releases addressing CVE-2026-59310; virtualized infrastructure management platforms
- **Microsoft SharePoint**: On-premises and cloud versions prior to July 2026 Patch Tuesday updates addressing CVE-2026-55040
- **macOS Screen Sharing**: macOS versions with Screen Sharing enabled prior to security updates addressing the authentication bypass
- **SAP Commerce Cloud**: Cloud deployments prior to the emergency patch released three days before active exploitation began
- **Microsoft Windows**: All supported Windows versions affected by LegacyHive zero-day (patched July 2026) and the separate Lazarus Group zero-day
- **Belgium eID Browser Extension**: The specific browser extension component of Belgium's electronic identity system; all citizen authentication workflows
- **Chrome VPN/Proxy Extensions**: 737 identified malicious extensions across 40+ developer accounts; 75,486 total installations before removal
- **Apple iOS/iPhone**: Devices targeted by mercenary spyware; specific iOS versions not disclosed
- **RingCentral**: Cloud communications platform; 1.6 million customer accounts compromised in July breach
- **Salesforce & ServiceNow**: Enterprise SaaS platforms targeted by City-Forum campaign since March 2025 with custom tooling
- **Shell Enterprise Systems**: Oil & gas operational and IT infrastructure; 89GB data claimed exfiltrated by Clop
- **Scottish Government Agencies**: Prosecutor's office and potentially other agencies sharing the compromised third-party provider
- **Colombian Justice Ministry**: Government judicial systems disrupted by ransomware during presidential transition
- **Commerzbank & Service Provider**: Banking authentication/authorization flows through compromised third-party service provider
- **Google Workspace**: Gmail, Drive, and connected applications accessible via stolen OAuth tokens

## Attack Vectors and Techniques

- **Public PoC Weaponization**: Attackers rapidly exploit CVE-2026-55040 (SharePoint) and macOS Screen Sharing flaw after proof-of-concept code publication, reducing time-to-exploit to days
- **Reverse SSH Persistence**: CVE-2026-59310 exploitation deploys reverse SSH tools for persistent, firewall-evasive remote access to vCenter infrastructure
- **Safe Mode EDR Evasion**: Akira ransomware affiliates restart systems into Safe Mode with Networking to disable EDR drivers that don't load in minimal boot environment
- **OAuth Token Theft & Replay**: Attackers bypass phishing and MFA by stealing and replaying OAuth tokens for Google Workspace, gaining persistent access without credentials
- **Browser Extension Supply Chain Compromise**: Malicious Chrome VPN extensions (737 identified) intercept and proxy all browser traffic through attacker infrastructure
- **Zero-Day Exploitation**: Lazarus Group and LegacyHive attackers leverage undisclosed Windows vulnerabilities for SYSTEM access before patches exist
- **eID Trust Framework Subversion**: Belgium's citizen authentication system compromised via browser extension RCE, undermining national digital identity infrastructure
- **Service Provider Pivot**: €30M bank fraud achieved by exploiting vulnerability in third-party service provider connected to Commerzbank systems
- **Dual-Mission Infrastructure**: Jewelbug APT uses identical web panel for both government espionage and cryptocurrency fraud operations
- **Custom SaaS Tooling**: City-Forum campaign deploys purpose-built tools targeting Salesforce and ServiceNow APIs and data models
- **Data Extortion Over Encryption**: Clop and Akira (in observed case) prioritize data theft and extortion over ransomware encryption
- **Mercenary Spyware Chains**: Sophisticated zero-day chains deployed against high-value iPhone targets for silent surveillance
- **Third-Party Supply Chain Breach**: Scottish government breach originates from shared service provider, demonstrating cascade risk
- **Brand Impersonation at Scale**: 274 malicious Chrome extensions impersonate 66 legitimate brands to gain user trust and installations

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Conducts Operation Dream Job—exploiting Windows zero-day for SYSTEM access and novel backdoor deployment against defense/aerospace targets in France, Germany, Brazil, India; attributed by Check Point Research
- **Jewelbug APT**: Hackers-for-hire balancing state espionage (government/military webmail breaches) and cryptocurrency fraud from shared infrastructure; dual-mission operations complicate attribution
- **Akira Ransomware**: Affiliates innovate EDR evasion via Safe Mode with Networking restart technique; observed stealing data but failing to encrypt in reported intrusion
- **Clop Ransomware Gang**: Claims 89GB data theft from Shell; continues data extortion model targeting large enterprises; no encryption claimed in this incident
- **ShinyHunters Extortion Group**: Breached RingCentral in July 2026, exfiltrating 1.6 million customer records; data circulated via Have I Been Pwned
- **City-Forum Campaign**: Long-running (since March 2025) data theft operation targeting Salesforce and ServiceNow across sectors with custom tooling; sophisticated SaaS-specific tradecraft
- **Commerzbank Fraud Group**: International cybercrime ring (4 arrested in Brazil, 3 charged in Europe) exploiting service provider flaw for €30M bank fraud
- **Mercenary Spyware Operators**: Targeting high-value iPhone users with zero-day chains; Apple Threat Notifications confirm active campaigns against specific individuals
- **Malicious Extension Developers**: 40+ Chrome Web Store developer accounts distributing 737 VPN/proxy extensions (75K+ installs) for traffic interception; 274 impersonating 66 brands
- **Colombian Justice Ministry Attackers**: Ransomware operators timing attack for maximum disruption during presidential transition; part of Latin America targeting surge
- **Scottish Government Breach Actors**: Unknown operators leveraging third-party service provider compromise; potential access to multiple agencies
- **Belgium eID Researchers/Attackers**: Parties who discovered/exploited severe browser extension vulnerabilities compromising national digital identity trust framework
