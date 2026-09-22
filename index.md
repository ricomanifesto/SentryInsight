---
schema_version: 2
report_date: 2026-09-22
generated_at: 2026-09-22T16:48:50Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-22/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, from network infrastructure to cloud management platforms and endpoint security. Check Point Security Management Server, VeloCloud Orchestrator, Zyxel switches, and several Linux kernel flaws have all been confirmed as actively exploited in the wild, with CISA adding multiple entries to its Known Exploited Vulnerabilities catalog.

A maximum-severity zero-day in legacy D-Link routers has public exploit code with no patch forthcoming, while a Windows Defender zero-day actively blocks antivirus updates. Simultaneously, threat actors are conducting large-scale credential theft via Phishing-as-a-Service platforms, supply chain compromises targeting e-commerce merchants, and North Korean campaigns stealing millions in cryptocurrency through social engineering.

## Active Exploitation Details

### Check Point Security Management Server Zero-Day
- **Description**: A critical zero-day vulnerability in Check Point Security Management Server that allows attackers to execute arbitrary scripts on the management server, potentially compromising the entire security policy infrastructure.
- **Impact**: Full compromise of the security management plane, enabling attackers to manipulate firewall policies, access sensitive network configurations, and pivot to managed gateways.
- **Status**: Emergency hotfixes released by Check Point; actively exploited in attacks prior to patch availability.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Check Point warns of Management Server zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/)

### VeloCloud Orchestrator Certificate Authentication Flaw
- **Description**: A CVSS 10.0 vulnerability in on-premises VeloCloud Orchestrator (VCO) that allows unauthenticated remote attackers to privilege internal functions and affect the VCO host. Only orchestrators configured to authenticate Edge devices with certificates are vulnerable.
- **Impact**: Complete takeover of the SD-WAN management platform, enabling network-wide traffic manipulation, device reprogramming, and lateral movement across branch offices.
- **Status**: Actively exploited in the wild; Arista has released patches for affected VCO versions.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93952
- **Reporting**: [The Hacker News — New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups](https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html)

### Zyxel GS1900 Series Switch Buffer Overflow
- **Description**: A stack-based buffer overflow vulnerability (CVSS 8.8) in Zyxel GS1900 series switches that allows unauthenticated attackers to achieve arbitrary operating system command execution with elevated privileges.
- **Impact**: Full device compromise, network traffic interception, configuration tampering, and use as a pivot point for deeper network intrusion. Exploited for data theft according to CISA.
- **Status**: Patches available; added to CISA Known Exploited Vulnerabilities catalog with active exploitation confirmed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-7273
- **Reporting**: [Bleeping Computer — CISA orders feds to patch Zyxel flaw exploited for data theft](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-zyxel-flaw-by-thursday/), [The Hacker News — Zyxel and Veeam Flaws Under Active Exploitation With Command and SYSTEM Access](https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html)

### Veeam Vulnerability Under Active Exploitation
- **Description**: A security flaw in Veeam backup software that is currently under active exploitation, granting attackers SYSTEM-level access. Specific technical details were not disclosed in the source article.
- **Impact**: Potential compromise of backup infrastructure, data exfiltration, ransomware deployment, and destruction of recovery capabilities.
- **Status**: Actively exploited per CISA; patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Zyxel and Veeam Flaws Under Active Exploitation With Command and SYSTEM Access](https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html)

### Linux Kernel Vulnerabilities (Three Flaws)
- **Description**: Three distinct Linux kernel vulnerabilities actively exploited in the wild, one rated critical severity. CISA has issued an alert and added them to the KEV catalog. Specific CVE identifiers were not provided in the source article.
- **Impact**: Kernel-level code execution, privilege escalation, container escape, and potential host compromise across Linux servers and embedded devices.
- **Status**: Actively exploited per CISA; patches available in upstream kernel and distribution updates.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — CISA alerts of active exploitation of three Linux kernel flaws](https://www.bleepingcomputer.com/news/security/cisa-alerts-of-active-exploitation-of-three-linux-kernel-flaws/)

### Windows Defender Zero-Day Blocking AV Updates
- **Description**: A zero-day exploit in Microsoft Defender released by researcher Abdelhamid Naceri (Nightmare Eclipse) that prevents antivirus definition updates from installing, leaving systems unprotected against new threats.
- **Impact**: Persistent degradation of endpoint protection, enabling follow-on malware installation without detection. Exploit code is publicly available.
- **Status**: Zero-day exploit publicly released; Microsoft patch status not confirmed in source.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — New Windows Defender zero-day blocks Microsoft antivirus updates](https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/)

### D-Link DIR-822A Router Maximum-Severity Zero-Day
- **Description**: A maximum-severity vulnerability in legacy D-Link DIR-822A dual-band Wi-Fi routers with public proof-of-concept exploit code. D-Link has stated no patch will be released for these end-of-life devices.
- **Impact**: Complete router compromise, traffic interception, DNS hijacking, botnet recruitment, and internal network access.
- **Status**: Public PoC available; no patch forthcoming (legacy/EOL product). Active exploitation not explicitly confirmed but imminent risk.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **CVE IDs**: CVE-2026-86296
- **Reporting**: [Bleeping Computer — D-Link warns of max severity zero-day bug in DIR-822A routers](https://www.bleepingcomputer.com/news/security/d-link-warns-of-max-severity-zero-day-bug-in-dir-822a-routers/)

### WordPress Click2Shell CSRF Vulnerability
- **Description**: A cross-site request forgery (CSRF) vulnerability in WordPress Core dubbed "Click2Shell" that allows attackers to execute arbitrary PHP code on the server when an authenticated administrator visits a malicious page.
- **Impact**: Remote code execution on the web server via administrator interaction, leading to full site compromise, data theft, and malware distribution.
- **Status**: Technical details and proof-of-concept exploit published; patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [Bleeping Computer — WordPress Click2Shell flaw lets hackers execute PHP on the server](https://www.bleepingcomputer.com/news/security/wordpress-click2shell-flaw-lets-hackers-execute-php-on-the-server/)

### WordPress Comment2Shell Vulnerability
- **Description**: A vulnerability (CVE-2026-93485) allowing anonymous visitors to inject malicious scripts via comments that execute when an administrator views the comment moderation queue, achieving authenticated RCE.
- **Impact**: Remote code execution on the WordPress server through social engineering of administrative users.
- **Status**: Patched in WordPress 7.1.1 (released September 17); no active exploitation reported.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-93485
- **Reporting**: [The Hacker News — WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session](https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html)

### SharePoint Server Authenticated RCE
- **Description**: A vulnerability (CVE-2026-65660) initially misclassified by Microsoft as spoofing (CVSS 6.5) but actually enabling authenticated remote code execution in SharePoint Server 2016, 2019, and Subscription Edition.
- **Impact**: Authenticated attackers can execute arbitrary code on SharePoint servers, accessing enterprise document repositories and internal data.
- **Status**: Patches released by Microsoft; no active exploitation reported in source.
- **Severity**: high
- **Exploitation Status**: not_observed
- **Action**: patch
- **CVE IDs**: CVE-2026-65660
- **Reporting**: [The Hacker News — SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE](https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html)

### Linux Kernel KVM ARM64 Guest Escape
- **Description**: A flaw (CVE-2026-89775) in the Linux kernel's KVM virtualization code for ARM64 processors that exposes freed host memory to guest VMs when nested virtualization is enabled, allowing guest-to-host escape.
- **Impact**: Virtual machine escape with read-write access to host kernel memory, enabling host compromise from a guest VM.
- **Status**: Proof-of-concept demonstrated by researcher; requires nested virtualization; no active exploitation reported.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-89775
- **Reporting**: [The Hacker News — New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory](https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html)

### EvilTokens Phishing-as-a-Service Campaign
- **Description**: A large-scale Phishing-as-a-Service platform (EvilTokens) that compromised over 12,000 Microsoft accounts across more than 10,000 organizations before being disrupted by Microsoft's Digital Crimes Unit.
- **Impact**: Mass credential theft, business email compromise, data exfiltration, and potential ransomware deployment across compromised Microsoft 365 tenants.
- **Status**: Platform disrupted and taken down by Microsoft DCU; compromised credentials require remediation.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — EvilTokens PhaaS disrupted after compromising 12,000 Microsoft accounts](https://www.bleepingcomputer.com/news/security/eviltokens-phaas-disrupted-after-compromising-12-000-microsoft-accounts/)

### Contagious Interview Campaign (North Korean)
- **Description**: A sustained North Korean campaign targeting web designers, engineers, and cryptocurrency specialists through fake interview lures, compromising at least 30,000 devices in 100+ countries and stealing $10.71M from 7,000+ cryptocurrency wallets.
- **Impact**: Large-scale device compromise, cryptocurrency theft, credential harvesting, and potential supply chain access through compromised developers.
- **Status**: Active campaign documented in joint cybersecurity advisory; ongoing threat.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Contagious Interview Campaign Compromises 30,000 Devices, Steals $10.71M in Crypto](https://thehackernews.com/2026/09/contagious-interview-campaign.html)

### SideCopy Spear-Phishing Campaign
- **Description**: Threat actor SideCopy expanding targeting to academic institutions in India using spear-phishing emails that abuse mshta.exe to execute malicious scripts and deploy ReverseRAT malware.
- **Impact**: Persistent access to academic networks, data theft, espionage, and potential lateral movement to connected research or government networks.
- **Status**: Active campaign observed by Trellix researchers; ongoing targeting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — SideCopy Broadens India Targeting to Academia With ReverseRAT Spear-Phishing](https://thehackernews.com/2026/09/sidecopy-broadens-india-targeting-to.html)

### BigCommerce Supply Chain Compromise via Ribon Apps
- **Description**: Attackers compromised credentials for third-party Ribon applications and used them to inject malicious scripts into BigCommerce merchant stores, leading to data breaches.
- **Impact**: Customer data theft, payment card skimming, reputation damage, and regulatory exposure for affected merchants.
- **Status**: Active breach reported; BigCommerce alerting affected merchants; Ribon credentials compromised.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — BigCommerce alerts merchants of data breach linked to Ribon apps](https://www.bleepingcomputer.com/news/security/bigcommerce-alerts-merchants-of-data-breach-linked-to-ribon-apps/)

### Fake LastPass Installer with Microsoft-Signed Driver
- **Description**: A trojanized LastPass Authenticator installer distributed on GitHub that installs a Microsoft-signed kernel driver to disable antivirus and EDR before deploying a password stealer.
- **Impact**: Complete security software bypass, credential theft from password managers and browsers, persistent system access.
- **Status**: Active distribution on GitHub; driver signed by Microsoft Hardware Compatibility Program; zero VirusTotal detections at time of research.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to Kill Antivirus and EDR](https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html)

### Malicious npm Package indexed-btree
- **Description**: A malicious npm package mimicking the legitimate "sorted-btree" package that hides its payload in application runtime code rather than lifecycle scripts, evading traditional supply chain scanners.
- **Impact**: Arbitrary code execution in applications that install the package, potential supply chain compromise of downstream software.
- **Status**: Package removed from npm registry after detection; demonstrates evolving evasion techniques.
- **Severity**: medium
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — Malicious npm Package indexed-btree Hid Its Loader in Runtime Code Before Removal](https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html)

### Malware Distribution via Film Torrents
- **Description**: Cybercriminals distributing new malware through torrent files for popular films, with identified victims in Africa including Kenya and Uganda.
- **Impact**: Malware installation on victim systems via social engineering, potential botnet recruitment, data theft, and financial fraud.
- **Status**: Active distribution campaign; geographic targeting observed.
- **Severity**: medium
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — Cybercriminals Are Hiding New Malware in Torrents for Popular Films](https://www.darkreading.com/cyberattacks-data-breaches/cybercriminals-hiding-new-malware-torrents-popular-films)

### ShinyHunters Compromise of Clop Ransomware Infrastructure
- **Description**: Threat actor ShinyHunters breached Clop ransomware group's dark web site, defaced it, and claims to have stolen victim data, potentially exposing organizations that paid ransoms to renewed extortion.
- **Impact**: Double extortion risk for previous Clop victims; exposure of sensitive stolen data; disruption of ransomware operations.
- **Status**: Active incident; data exposure ongoing; implications for prior victims.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Dark Reading — ShinyHunters Hacked Clop. Now What About Clop's Victims?](https://www.darkreading.com/cyberattacks-data-breaches/shinyhunters-hacked-clop-what-about-clops-victims)

### Meta Muse AI Assistant Backdoor via Hidden Setting
- **Description**: A proof-of-concept demonstrating that malware already present on a Mac can modify a hidden Meta Muse setting to redirect voice dictation to an attacker instead of Meta, turning the AI assistant into a surveillance backdoor.
- **Impact**: Audio surveillance, command injection via voice interface, privacy violation for Mac users with Muse installed.
- **Status**: Proof-of-concept only; requires pre-existing malware infection; no active exploitation reported.
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — One Hidden Meta Muse Setting Could Let Attackers Turn the AI Assistant Into a Backdoor](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html)

## Affected Systems and Products

- **Check Point Security Management Server**: All versions prior to emergency hotfix; management plane for Check Point firewall infrastructure
- **VeloCloud Orchestrator (VCO)**: On-premises deployments with certificate-based Edge authentication; Arista SD-WAN management platform
- **Zyxel GS1900 Series Switches**: All firmware versions prior to patched release; web-managed Gigabit Ethernet switches
- **Veeam Backup & Replication**: Specific product/version not disclosed in source; enterprise backup infrastructure
- **Linux Kernel**: Multiple kernel versions across distributions; three distinct vulnerabilities affecting server, cloud, and embedded deployments
- **Windows Defender / Microsoft Defender**: Windows endpoints with Defender enabled; exploit blocks definition updates
- **D-Link DIR-822A Routers**: Legacy dual-band Wi-Fi routers (end-of-life); no patch will be released
- **WordPress Core**: Versions prior to 7.1.1 for Comment2Shell; Click2Shell affects Core component (version range not specified)
- **Microsoft SharePoint Server**: 2016, 2019, and Subscription Edition; on-premises deployments
- **Linux KVM on ARM64**: Hosts with nested virtualization enabled; affects cloud providers and enterprises using ARM64 virtualization
- **Microsoft 365 / Entra ID**: Accounts targeted via EvilTokens PhaaS; 12,000+ compromised across 10,000+ organizations
- **BigCommerce Merchant Stores**: Stores using compromised Ribon third-party applications; e-commerce platform merchants
- **npm Ecosystem**: Projects that installed malicious `indexed-btree` package; JavaScript/TypeScript supply chain
- **macOS with Meta Muse**: Mac systems running Meta's Muse AI assistant; requires pre-existing malware infection
- **GitHub / Software Distribution**: Fake LastPass Authenticator installer hosted on GitHub; Windows systems
- **Torrent Networks**: Users downloading pirated film content; malware-laced torrent files

## Attack Vectors and Techniques

- **Phishing-as-a-Service (PhaaS)**: EvilTokens platform providing turnkey credential harvesting infrastructure targeting Microsoft 365 accounts at scale, using adversary-in-the-middle techniques to bypass MFA.
- **Supply Chain Credential Compromise**: Attackers steal third-party application credentials (Ribon apps) to inject malicious scripts into downstream customer environments (BigCommerce merchants).
- **Spear-Phishing with Living-off-the-Land**: SideCopy abuses `mshta.exe` (Microsoft HTML Application Host) to execute malicious scripts without dropping files, evading detection while deploying ReverseRAT.
- **Social Engineering via Fake Interviews**: North Korean Contagious Interview campaign uses fictitious job interviews to deliver malware to developers and cryptocurrency professionals across 100+ countries.
- **Trojanized Legitimate Software**: Fake LastPass Authenticator installer leverages a Microsoft-signed kernel driver to disable security agents (AV/EDR) before deploying password-stealing payload.
- **Malicious Package Runtime Evasion**: `indexed-btree` npm package hides malicious loader in application runtime code rather than install scripts, bypassing lifecycle-based supply chain scanners.
- **Zero-Day Exploitation of Management Planes**: Check Point Management Server and VeloCloud Orchestrator vulnerabilities target centralized network/security management infrastructure for maximum blast radius.
- **Network Device Exploitation**: Zyxel switch buffer overflow and D-Link router zero-day exploit network infrastructure devices often lacking timely patching.
- **Kernel-Level Virtualization Escape**: Linux KVM flaw (CVE-2026-89775) exploits nested virtualization memory management to break guest isolation on ARM64 hosts.
- **Authenticated Web Application RCE**: SharePoint and WordPress vulnerabilities chain low-privilege access (authenticated user, admin session) to achieve server-side code execution.
- **Malvertising / Trojanized Media**: Malware distributed through torrent files for popular films, targeting users seeking pirated content in specific geographic regions.
- **Ransomware Infrastructure Compromise**: ShinyHunters breaches Clop's dark web infrastructure, stealing victim data and enabling secondary extortion of organizations that already paid ransoms.
- **AI Assistant Subversion**: Local malware manipulates hidden settings in Meta Muse to redirect voice input, demonstrating post-exploitation abuse of AI integrations.
- **Certificate-Based Authentication Bypass**: VeloCloud Orchestrator flaw specifically affects certificate-authenticated Edge configurations, highlighting risks in PKI-dependent architectures.

## Threat Actor Activities

- **EvilTokens Operators**: Ran a large-scale Phishing-as-a-Service platform compromising 12,000+ Microsoft accounts across 10,000+ organizations before disruption by Microsoft Digital Crimes Unit. Platform offered adversary-in-the-middle capabilities to defeat MFA.
- **SideCopy (APT)**: Pakistan-aligned threat actor expanding targeting from Indian government entities to academic institutions. Uses spear-phishing with `mshta.exe` execution and ReverseRAT malware for persistent access and espionage.
- **North Korean Actors (Contagious Interview Campaign)**: State-sponsored group conducting global campaign targeting web designers, engineers, and crypto specialists via fake interview lures. Compromised 30,000+ devices in 100+ countries, stole $10.71M from 7,000+ cryptocurrency wallets. Documented in joint cybersecurity advisory.
- **ShinyHunters**: Opportunistic threat actor that breached Clop ransomware group's dark web infrastructure, defaced their leak site, and claims possession of victim data. Creates secondary extortion risk for organizations that previously paid Clop ransoms.
- **Clop Ransomware Group**: Victim of infrastructure compromise by ShinyHunters; their victim data now exposed, potentially leading to renewed extortion attempts against prior victims.
- **Unknown Actors (Zyxel/Linux Kernel/Check Point/Veeam Exploitation)**: CISA-confirmed active exploitation of Zyxel switches, three Linux kernel flaws, Check Point Management Server, and Veeam software. Attribution not provided in sources; likely multiple distinct threat groups given target diversity.
- **Unknown Actors (VeloCloud Exploitation)**: Active exploitation of CVE-2026-93952 in certificate-configured VCO instances; targeting SD-WAN management infrastructure suggests network-focused threat actor.
- **Abdelhamid Naceri (Nightmare Eclipse)**: Security researcher who publicly released Windows Defender zero-day exploit blocking AV updates; not a threat actor but increases exploitation risk through public disclosure.
- **Patrick Wardle**: Security researcher who published proof-of-concept for Meta Muse backdoor via hidden setting manipulation; demonstrates post-exploitation technique requiring initial malware foothold.
- **Cybercriminal Groups (Torrent Malware)**: Financially motivated actors distributing malware via trojanized film torrents, with observed victims in Kenya and Uganda. Geographic targeting suggests regional focus or opportunity.
- **Ribon Credential Thieves**: Actors who compromised credentials for Ribon third-party applications, enabling supply chain injection into BigCommerce merchant stores. Initial access vector not specified.