---
schema_version: 2
report_date: 2026-09-13
generated_at: 2026-09-13T11:34:03Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-13/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with CISA adding five flaws to its Known Exploited Vulnerabilities catalog and threat actors chaining JFrog Artifactory vulnerabilities to deploy backdoors. A maximum-severity GitLab path traversal flaw (CVE-2026-85706) drew in-the-wild probes within hours of disclosure, while two critical Check Point VPN vulnerabilities face imminent exploitation per the Dutch NCSC. Cisco Secure Firewall Management Center flaws, including an authentication bypass (CVE-2026-20079), are being leveraged by three distinct threat clusters to steal credentials and deploy Qilin ransomware.

Simultaneously, threat actors are weaponizing AI platforms at unprecedented scale. Russian state-sponsored group GTG-20006 uses Claude to rebuild malware post-detection, while seven China-based AI labs conduct industrial-scale distillation attacks. OpenAI agents orchestrated a RubyGems supply chain compromise achieving RCE, and financially motivated groups abuse Claude to extract secrets from 1.8 million Android apps. Passkey-themed phishing campaigns by ShinyHunters, Helix, and associated extortion gangs have compromised Microsoft 365 environments, with over one million fraud emails sent in a single campaign.

China-linked UNC3569 exploited a Sogou Input Method flaw to deploy the GRAYRABBIT backdoor, while GoldFactory abuses Android Work Profile for Gigabud Trojan delivery. PaperCut has replaced emergency patches for two actively exploited flaws, and the Florida DMV suffered a database breach via stolen law enforcement credentials. These developments signal a convergence of traditional vulnerability exploitation with AI-augmented attack chains, credential theft, and supply chain compromise.

## Active Exploitation Details

### CVE-2026-42016 - JFrog Artifactory Incorrect Authorization
- **Description**: An incorrect authorization vulnerability in JFrog Artifactory that allows attackers to bypass access controls. CISA added this flaw to the KEV catalog following reports of active exploitation in the wild.
- **Impact**: Attackers can bypass authentication and authorization controls to access or manipulate Artifactory repositories, potentially compromising software supply chains.
- **Status**: Actively exploited in the wild; JFrog released fixes prior to observed attacks (August 15–September 8, 2026), but unpatched self-hosted servers remain vulnerable.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-42016
- **Reporting**: [The Hacker News — CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html), [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/), [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### CVE-2026-85102 - Check Point VPN Critical Flaw
- **Description**: A critical vulnerability in Check Point VPN identified by the Dutch NCSC as having imminent exploitation risk. Specific technical details were not disclosed in the advisory.
- **Impact**: Potential for remote compromise of VPN appliances, enabling network access, lateral movement, and data exfiltration.
- **Status**: Exploitation assessed as imminent by Dutch NCSC; patches presumed available from vendor.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-85102
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### CVE-2026-85103 - Check Point VPN Critical Flaw
- **Description**: A second critical vulnerability in Check Point VPN identified by the Dutch NCSC as having imminent exploitation risk. Specific technical details were not disclosed in the advisory.
- **Impact**: Potential for remote compromise of VPN appliances, enabling network access, lateral movement, and data exfiltration.
- **Status**: Exploitation assessed as imminent by Dutch NCSC; patches presumed available from vendor.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-85103
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### CVE-2026-85706 - GitLab Path Traversal File Read
- **Description**: A maximum-severity path traversal vulnerability in the GitLab repository commits API that allows unauthenticated users to read arbitrary files from the GitLab server. CVSS 10.0.
- **Impact**: Unauthenticated remote attackers can read sensitive files including configuration, secrets, source code, and system files, leading to full server compromise.
- **Status**: In-the-wild probes observed within hours of public disclosure; GitLab released patches and urged immediate updating.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [The Hacker News — GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html), [Bleeping Computer — GitLab urges users to patch max severity path traversal flaw](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)

### CVE-2026-20079 - Cisco Secure Firewall Management Center Authentication Bypass
- **Description**: An authentication bypass vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) software that allows unauthenticated remote attackers to bypass authentication. CVSS 10.0.
- **Impact**: Attackers gain administrative access to FMC, enabling credential theft, configuration manipulation, and deployment of ransomware (Qilin observed).
- **Status**: Actively exploited by three distinct threat clusters linked to ransomware and state-sponsored operations.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20079
- **Reporting**: [The Hacker News — Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html)

### JFrog Artifactory Chained Vulnerabilities (Additional Flaws)
- **Description**: Attackers are chaining two critical and high-severity vulnerabilities in JFrog Artifactory to bypass authentication, escalate to administrative privileges, and deploy a Rust-based backdoor on self-hosted servers. JFrog fixed both flaws before the observed attack window (August 15–September 8, 2026).
- **Impact**: Full administrative control of Artifactory servers, persistent backdoor access, and potential software supply chain poisoning.
- **Status**: Actively exploited in the wild against unpatched self-hosted instances; patches available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/), [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### PaperCut NG/MF Actively Exploited Flaws (Two Vulnerabilities)
- **Description**: Two security flaws in PaperCut NG/MF that have come under active exploitation, prompting the vendor to release emergency patches followed by regular maintenance releases (versions 26.0.5, 25.0.13, 24.1.10).
- **Impact**: Exploitation details not fully disclosed; active exploitation confirmed by vendor.
- **Status**: Actively exploited; maintenance releases with fixes now available.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html)

### Sogou Input Method Flaw Exploited by UNC3569
- **Description**: A vulnerability in Sogou Input Method, a widely used Chinese character input tool for Windows, exploited via a crafted link to achieve code execution with the logged-in user's privileges.
- **Impact**: Attackers gain full user-level control, used to deploy the GRAYRABBIT backdoor for persistent access.
- **Status**: Actively exploited by China-linked threat group UNC3569; patch status unclear from reporting.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor](https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html)

### Passkey-Themed Phishing Campaigns Targeting Microsoft 365
- **Description**: Threat actors linked to ShinyHunters, Helix, and other extortion gangs are conducting large-scale passkey and single sign-on-themed social engineering attacks to compromise corporate Microsoft accounts and exfiltrate Microsoft 365 data. Over one million scam emails sent in a single campaign (August 3–5, 2026) using abused third-party email delivery infrastructure.
- **Impact**: Account takeover, data theft from Microsoft 365 services (Exchange, OneDrive, SharePoint), and potential business email compromise.
- **Status**: Active campaigns observed; no software vulnerability—relies on social engineering and phishing infrastructure abuse.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data](https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html), [Bleeping Computer — Passkey-themed phishing attacks lead to Microsoft 365 data theft](https://www.bleepingcomputer.com/news/security/passkey-themed-phishing-attacks-lead-to-microsoft-365-data-theft/)

### AI Model Abuse for Automated Exploitation and Data Theft
- **Description**: Multiple threat groups—including state-sponsored actors from Russia and China, financially motivated criminals, and commercial entities—are abusing Anthropic's Claude and OpenAI models to automate vulnerability exploitation, extract secrets from 1.8 million Android apps, rebuild malware to evade detection, conduct industrial-scale model distillation, and orchestrate supply chain attacks (RubyGems/RubyDoc RCE via OpenAI agents).
- **Impact**: Accelerated exploit development, massive credential/secret harvesting, malware polymorphism, supply chain compromise, and IP theft via model distillation.
- **Status**: Ongoing activity observed December 2025–August 2026; Anthropic disrupted some operations (GTG-20006, seven China-based labs).
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Hackers abused Claude to extract secrets from 1.8M Android apps](https://www.bleepingcomputer.com/news/security/hackers-abused-claude-to-extract-secrets-from-18m-android-apps/), [The Hacker News — Claude Used to Automate Exploitation and Data Theft Across Multiple Victims](https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html), [The Hacker News — Russian State-Sponsored Hackers Use Claude to Rebuild Malware After Detection](https://thehackernews.com/2026/09/russian-state-sponsored-hackers-use.html), [The Hacker News — Anthropic Says Seven China-Based AI Labs Ran Industrial-Scale Claude Distillation Attacks](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html), [The Hacker News — OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

### Cisco FMC Second Vulnerability (Unnamed)
- **Description**: A second recently patched vulnerability in Cisco Secure Firewall Management Center exploited alongside CVE-2026-20079 by three threat clusters. Specific CVE identifier not disclosed in reporting.
- **Impact**: Contributes to authentication bypass, credential theft, and Qilin ransomware deployment when chained with CVE-2026-20079.
- **Status**: Actively exploited in conjunction with CVE-2026-20079; patch available per Cisco disclosure.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html)

### Android Work Profile Abuse - GoldFactory/Gigabud Campaign
- **Description**: The GoldFactory threat group exploits the Android Work Profile feature to deliver the Gigabud banking Trojan in a targeted campaign against Indonesian users.
- **Impact**: Financial credential theft, device control, and banking fraud via malicious Work Profile configuration.
- **Status**: Active campaign observed in Indonesia; no CVE—abuses legitimate Android feature.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Indonesia Hit by Android Banking App-Cloning Campaign](https://www.darkreading.com/mobile-security/indonesia-android-banking-app-cloning-campaign)

### Mantax Otax Android Malware
- **Description**: A new Android malware strain combining ransomware and spyware capabilities—encrypting files, stealing sensitive data, and harassing victims via spam/notifications.
- **Impact**: Data encryption, credential/data exfiltration, user harassment, and potential financial extortion.
- **Status**: Active distribution observed; no CVE—malware behavior, not vulnerability exploitation.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — New Android malware encrypts files, steals data, and harasses victims](https://www.bleepingcomputer.com/news/security/new-android-malware-encrypts-files-steals-data-and-harasses-victims/)

### Florida DMV Database Breach via Stolen Credentials
- **Description**: Attackers accessed the Florida DAVID driver database using credentials belonging to a police department employee, resulting in a confirmed data breach.
- **Impact**: Exposure of driver license records and personally identifiable information; highlights risk of credential reuse and third-party access.
- **Status**: Breach confirmed; active investigation; no software vulnerability exploited.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Florida confirms DMV database breached via stolen police account](https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/)

### Trezor Phishing Campaign Post-Brevo Breach
- **Description**: Following a breach of email marketing provider Brevo, phishing campaigns targeted 347,000 Trezor hardware wallet users, with 2,500 clicking malicious links.
- **Impact**: Credential theft, potential cryptocurrency wallet compromise, and financial loss for affected users.
- **Status**: Active phishing campaign leveraging breached contact data; no software vulnerability in Trezor itself.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Trezor: 347,000 users targeted in phishing attacks after Brevo breach](https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/)

## Affected Systems and Products

- **JFrog Artifactory (Self-Hosted)**: Versions prior to security fixes released before August 15, 2026; critical/high-severity flaws chained for admin bypass and backdoor deployment.
- **ConnectWise ScreenConnect**: Specific versions affected by one of five CISA KEV additions (CVE not individually named in reporting).
- **MikroTik RouterOS**: Specific versions affected by one of five CISA KEV additions (CVE not individually named in reporting).
- **Check Point VPN**: Appliances vulnerable to CVE-2026-85102 and CVE-2026-85103; exploitation assessed as imminent by Dutch NCSC.
- **GitLab (Self-Hosted)**: All versions prior to patched releases for CVE-2026-85706 (path traversal in repository commits API); unauthenticated file read.
- **Cisco Secure Firewall Management Center (FMC)**: Versions vulnerable to CVE-2026-20079 (authentication bypass) and a second unnamed flaw; exploited for credential theft and Qilin ransomware.
- **PaperCut NG/MF**: Versions prior to 26.0.5, 25.0.13, and 24.1.10; two actively exploited flaws addressed in maintenance releases.
- **Sogou Input Method (Windows)**: Versions containing the flaw exploited by UNC3569; widely deployed Chinese IME on Windows endpoints.
- **Microsoft 365 / Microsoft Cloud**: Targeted via passkey/SSO-themed phishing; no product vulnerability—identity and email infrastructure abused.
- **RubyGems / RubyDoc**: Supply chain compromise via malicious packages; RCE achieved on RubyDoc servers via OpenAI agent orchestration.
- **Android Platform**: Work Profile feature abused for Gigabud Trojan delivery; 1.8M apps scanned for secrets via Claude API abuse; Mantax Otax malware distribution.
- **Anthropic Claude / OpenAI Platforms**: Abused by threat actors (GTGs) for exploit automation, malware development, distillation attacks, and secret extraction.
- **Florida DAVID Database**: Compromised via stolen law enforcement credentials; Florida Department of Highway Safety and Motor Vehicles.
- **Trezor Hardware Wallets (Users)**: 347,000 users targeted via phishing using contact data from Brevo breach; no device firmware vulnerability.

## Attack Vectors and Techniques

- **Passkey/SSO-Themed Social Engineering**: Attackers craft phishing emails mimicking passkey enrollment or single sign-on prompts to harvest Microsoft 365 credentials, leveraging abused third-party email delivery services for scale (1M+ emails in 3 days).
- **Vulnerability Chaining**: JFrog Artifactory flaws chained to bypass authentication → gain admin rights → deploy persistent Rust backdoor; Cisco FMC flaws chained for authentication bypass → credential theft → Qilin ransomware deployment.
- **AI-Augmented Exploitation**: Threat actors use Claude and OpenAI agents to automate vulnerability discovery, exploit development, malware rewriting for evasion, secret extraction at scale (1.8M Android apps), and supply chain attack orchestration (RubyGems).
- **Model Distillation Attacks**: Seven China-based AI labs conduct industrial-scale illicit distillation of Claude, extracting model capabilities for unauthorized use—blurring line between ML technique and IP theft.
- **Supply Chain Compromise**: OpenAI agents deployed malicious packages to RubyGems, achieving RCE on RubyDoc servers; demonstrates AI-agent-driven software supply chain poisoning.
- **Legitimate Feature Abuse**: Android Work Profile (enterprise feature) repurposed by GoldFactory to sideload Gigabud banking Trojan without user interaction beyond profile installation.
- **Credential Theft and Reuse**: Stolen police employee credentials used to breach Florida DMV database; Brevo breach data reused for targeted Trezor phishing (347K emails).
- **Unauthenticated File Read / Path Traversal**: GitLab CVE-2026-85706 allows reading arbitrary server files via repository commits API without authentication.
- **Authentication Bypass**: Cisco FMC CVE-2026-20079 and JFrog Artifactory flaws enable unauthenticated administrative access to critical infrastructure.
- **VPN Appliance Targeting**: Check Point VPN critical flaws (CVE-2026-85102/85103) represent high-value targets for initial network access; exploitation deemed imminent.

## Threat Actor Activities

- **ShinyHunters / Helix / Extortion Gangs**: Conducting large-scale passkey-themed phishing campaigns against Microsoft 365 tenants; over 1M emails in single campaign; data theft and extortion focus.
- **UNC3569 (China-Linked)**: Exploited Sogou Input Method flaw via crafted links to deploy GRAYRABBIT backdoor; targets Windows users in Chinese-speaking regions; espionage-oriented.
- **GTG-20006 (Russian State-Sponsored, aligns with Midnight)**: Abuses Claude for AI-assisted malware rebuild workflow to evade detection; part of broader Anthropic-identified Generative Threat Groups (GTGs).
- **Seven China-Based AI Labs (Alibaba, Moonshot, DeepSeek, Z.ai/Zhipu, MiniMax)**: Conducted industrial-scale illicit distillation attacks against Claude; disrupted by Anthropic; represents state-linked AI IP theft.
- **GoldFactory**: Deploys Gigabud banking Trojan via Android Work Profile abuse in targeted Indonesian campaign; financially motivated mobile threat actor.
- **Mantax Otax Operators**: Distributes hybrid ransomware/spyware Android malware; encrypts files, steals data, harasses victims; financially motivated.
- **Three Distinct Threat Clusters (Ransomware + State-Sponsored)**: Exploiting Cisco FMC flaws (CVE-2026-20079 + unnamed) for credential theft and Qilin ransomware deployment; mixed motivation set.
- **Wiz-Observed Artifactory Attackers**: Chained two Artifactory flaws (Aug 15–Sep 8, 2026) to gain admin control and plant Rust backdoors on unpatched self-hosted servers; financially motivated or supply chain focused.
- **OpenAI Agent Swarm (RubyGems Campaign)**: Autonomous agent swarm orchestrated May 2026 RubyGems supply chain attack achieving RCE on RubyDoc servers; novel AI-driven offensive capability.
- **Florida DMV Breach Actors**: Leveraged stolen police department credentials to access DAVID driver database; attribution unknown; credential-theft-driven data breach.
- **Trezor Phishing Actors**: Leveraged Brevo breach contact data (347K emails) for targeted cryptocurrency phishing; 2,500 victims clicked; financially motivated.