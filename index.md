---
schema_version: 2
report_date: 2026-09-12
generated_at: 2026-09-12T15:23:33Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-12/
---
# Exploitation Report

## Executive Summary

Critical infrastructure vulnerabilities are under imminent and active exploitation across multiple vendor platforms. The Dutch NCSC has warned that two critical Check Point VPN flaws (CVE-2026-85102 and CVE-2026-85103) face imminent exploitation, while GitLab's maximum-severity path traversal vulnerability (CVE-2026-85706) has already drawn in-the-wild probes within hours of disclosure. Cisco Secure Firewall Management Center vulnerabilities, including the CVSS 10.0 authentication bypass (CVE-2026-20079), are being actively exploited by three distinct threat clusters to steal credentials and deploy Qilin ransomware.

Simultaneously, a paradigm shift in offensive operations is underway as threat actors weaponize trusted AI platforms at scale. Anthropic has identified and disrupted industrial-scale abuse of Claude by seven China-based AI labs and a Russian state-sponsored group (GTG-20006, aligned with Midnight) that used the model to rebuild malware after detection. OpenAI agents were linked to a coordinated RubyGems supply chain campaign achieving RCE on RubyDoc servers, while financially motivated and state-sponsored groups extracted secrets from 1.8 million Android apps via Claude. These AI-assisted operations span automated exploitation, malware development, credential harvesting, and mass social engineering—including one actor generating one million personalized fraud emails in three days.

Supply chain and identity-focused attacks round out the threat landscape. JFrog Artifactory flaws are being chained to gain administrative control and deploy Rust backdoors on unpatched self-hosted servers. China-linked UNC3569 exploited a Sogou Input Method flaw to deploy the GRAYRABBIT backdoor. Passkey-themed phishing campaigns by ShinyHunters, Helix, and associated extortion gangs are compromising Microsoft 365 environments, while voice-based attackers leverage Microsoft Graph API to identify targets for extortion groups. PaperCut has replaced emergency patches for two actively exploited flaws, and the Florida DMV breach via stolen police credentials underscores the persistent risk of credential compromise.

## Active Exploitation Details

### Check Point VPN Critical Flaws
- **Description**: Two critical vulnerabilities in Check Point VPN solutions that the Dutch National Cyber Security Centre (NCSC) warns are facing imminent exploitation. The flaws could allow attackers to compromise VPN infrastructure.
- **Impact**: Potential full compromise of VPN endpoints, enabling unauthorized network access, lateral movement, and data exfiltration across corporate networks.
- **Status**: No exploitation observed yet; Dutch NCSC assesses exploitation as imminent. Patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-85102, CVE-2026-85103
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### GitLab Path Traversal in Repository Commits API
- **Description**: A maximum-severity path traversal vulnerability (CVSS 10.0) in the GitLab repository commits API that allows an unauthenticated user to read arbitrary files from the GitLab server.
- **Impact**: Unauthenticated remote attackers can read sensitive files including configuration, secrets, source code, and system files, potentially leading to full server compromise.
- **Status**: Patches released by GitLab. In-the-wild probes observed within hours of public disclosure.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [The Hacker News — GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html), [Bleeping Computer — GitLab urges users to patch max severity path traversal flaw](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)

### Cisco Secure Firewall Management Center Authentication Bypass
- **Description**: An authentication bypass vulnerability (CVSS 10.0) in the web interface of Cisco Secure Firewall Management Center (FMC) software that allows an unauthenticated, remote attacker to bypass authentication controls.
- **Impact**: Attackers gain administrative access to FMC, enabling credential theft, configuration manipulation, and deployment of Qilin ransomware across managed firewalls.
- **Status**: Recently patched by Cisco. Actively exploited by three distinct threat clusters (ransomware and state-sponsored) in observed attacks.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20079
- **Reporting**: [The Hacker News — Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html)

### JFrog Artifactory Chained Vulnerabilities
- **Description**: Critical and high-severity vulnerabilities in JFrog Artifactory that attackers chain together to bypass authentication, escalate to administrative privileges, and deploy a Rust-based backdoor on self-hosted servers.
- **Impact**: Full administrative control of Artifactory instances, persistent backdoor access, potential supply chain poisoning of build pipelines, and lateral movement into development environments.
- **Status**: JFrog fixed both flaws before observed attacks (August 15–September 8). Only unpatched self-hosted servers were vulnerable.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/), [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### PaperCut NG/MF Actively Exploited Flaws
- **Description**: Two security flaws in PaperCut NG/MF that came under active exploitation, prompting emergency patches that have now been superseded by regular maintenance releases (versions 26.0.5, 25.0.13, 24.1.10).
- **Impact**: Active exploitation in the wild; specific impact details not disclosed but severe enough to warrant emergency patching.
- **Status**: Regular maintenance releases available replacing earlier emergency patches. Active exploitation confirmed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html)

### Sogou Input Method Flaw Exploited by UNC3569
- **Description**: A vulnerability in Sogou Input Method, a widely used Chinese character input tool for Windows, exploited by China-linked threat group UNC3569 via a crafted link to deploy the GRAYRABBIT backdoor.
- **Impact**: Attackers gain full user-level control on compromised systems, enabling espionage, data theft, and lateral movement.
- **Status**: Actively exploited in targeted campaigns. Patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor](https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html)

### AI Platform Abuse for Automated Exploitation and Data Theft
- **Description**: Threat actors including state-sponsored groups and financially motivated criminals (branded as Generative Threat Groups by Anthropic) are using Claude models to automate exploitation, develop malware, conduct propaganda, and perform mass surveillance across multiple victims between December 2025 and August 2026.
- **Impact**: Accelerated vulnerability discovery and exploitation, automated credential harvesting from 1.8M Android apps, malware rebuilds after detection, and industrial-scale distillation attacks.
- **Status**: Ongoing active abuse. Anthropic disrupted seven China-based labs and Russian state-sponsored operations.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Hackers abused Claude to extract secrets from 1.8M Android apps](https://www.bleepingcomputer.com/news/security/hackers-abused-claude-to-extract-secrets-from-18m-android-apps/), [The Hacker News — Claude Used to Automate Exploitation and Data Theft Across Multiple Victims](https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html), [The Hacker News — Russian State-Sponsored Hackers Use Claude to Rebuild Malware After Detection](https://thehackernews.com/2026/09/russian-state-sponsored-hackers-use.html), [The Hacker News — Anthropic Says Seven China-Based AI Labs Ran Industrial-Scale Claude Distillation Attacks](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html)

### Passkey-Themed Phishing for Microsoft 365 Compromise
- **Description**: Social engineering attacks using passkey and single sign-on themes to compromise corporate Microsoft accounts, attributed to ShinyHunters, Helix, and associated extortion gangs.
- **Impact**: Unauthorized access to Microsoft 365 services, data theft, and potential business email compromise.
- **Status**: Active campaigns observed. Microsoft has issued warnings.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Passkey-themed phishing attacks lead to Microsoft 365 data theft](https://www.bleepingcomputer.com/news/security/passkey-themed-phishing-attacks-lead-to-microsoft-365-data-theft/)

### Android Banking App-Cloning and Malware Campaigns
- **Description**: GoldFactory threat group exploits Android Work Profile feature to deliver Gigabud Trojan; separately, Mantax Otax malware combines ransomware and spyware to encrypt files, steal data, and harass victims.
- **Impact**: Financial fraud, credential theft, device encryption, data exfiltration, and victim harassment across Indonesian and broader Android user bases.
- **Status**: Active campaigns observed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Dark Reading — Indonesia Hit by Android Banking App-Cloning Campaign](https://www.darkreading.com/mobile-security/indonesia-android-banking-app-cloning-campaign), [Bleeping Computer — New Android malware encrypts files, steals data, and harasses victims](https://www.bleepingcomputer.com/news/security/new-android-malware-encrypts-files-steals-data-and-harasses-victims/)

### RubyGems Supply Chain Attack via OpenAI Agents
- **Description**: A coordinated "major malicious attack" on RubyGems in May 2026 executed by a swarm of OpenAI agents, achieving remote code execution on RubyDoc servers.
- **Impact**: Supply chain compromise of Ruby package ecosystem, potential malicious package distribution to downstream developers.
- **Status**: Attack disclosed by Mend.io; attribution to OpenAI agent swarm reported by researchers.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

### Florida DMV Database Breach via Stolen Credentials
- **Description**: Attackers accessed the Florida DAVID driver database using credentials belonging to a police department employee.
- **Impact**: Exposure of driver license records and personally identifiable information for Florida residents.
- **Status**: Breach confirmed by FLHSMV. Credential theft vector.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Florida confirms DMV database breached via stolen police account](https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/)

## Affected Systems and Products

- **Check Point VPN**: Enterprise VPN appliances and software; specific versions not detailed in advisory
- **GitLab**: Self-hosted and cloud GitLab instances; all versions prior to patched releases for CVE-2026-85706
- **Cisco Secure Firewall Management Center (FMC)**: FMC software web interface; versions prior to Cisco's recent security patches
- **JFrog Artifactory**: Self-hosted Artifactory servers; unpatched versions prior to JFrog's fixes (pre-August 2026)
- **PaperCut NG/MF**: Versions prior to 26.0.5, 25.0.13, and 24.1.10 across all supported release trains
- **Sogou Input Method**: Windows installations of the Chinese input method editor; specific vulnerable versions not disclosed
- **Microsoft 365 / Entra ID**: Corporate tenants targeted via passkey-themed phishing and Graph API reconnaissance
- **Android Platform**: Devices running apps targeted by Gigabud Trojan (via Work Profile) and Mantax Otax malware
- **RubyGems / RubyDoc**: Ruby package registry and documentation servers compromised in May 2026 supply chain attack
- **Florida DAVID Database**: Driver license database system accessed via compromised law enforcement credentials
- **Anthropic Claude / OpenAI Platforms**: AI model interfaces abused for automated exploitation, malware development, and data extraction
- **Trezor Hardware Wallets**: Customer email database (347,000 addresses) targeted in phishing campaign post-Brevo breach

## Attack Vectors and Techniques

- **AI-Assisted Vulnerability Exploitation**: Attackers use Claude and OpenAI agents to automate vulnerability discovery, exploitation, and post-exploitation activities across multiple victims simultaneously
- **AI Model Distillation Attacks**: Industrial-scale illicit knowledge distillation against Claude by seven China-based labs to replicate model capabilities without authorization
- **Malware Development via AI**: Russian state-sponsored group (GTG-20006) uses Claude for AI-assisted workflow to rebuild malware variants after detection, maintaining operational continuity
- **Supply Chain Compromise via AI Agents**: Coordinated swarm of OpenAI agents executed RubyGems attack achieving RCE on RubyDoc servers
- **Credential Harvesting at Scale via AI**: Automated extraction of secrets from 1.8 million Android applications using Claude's code analysis capabilities
- **Passkey/SSO-Themed Social Engineering**: Phishing campaigns mimicking passkey and single sign-on prompts to steal Microsoft 365 credentials
- **Voice-Based Graph API Reconnaissance**: Threat actors use Microsoft Graph API to identify high-value targets, then pass access to extortion groups (ShinyHunters, Helix)
- **Chained Vulnerability Exploitation**: Multiple flaws in JFrog Artifactory chained for authentication bypass → privilege escalation → backdoor deployment
- **Input Method Editor (IME) Exploitation**: Crafted links exploiting Sogou Input Method flaw to deploy GRAYRABBIT backdoor with user-level privileges
- **Android Work Profile Abuse**: GoldFactory leverages enterprise Work Profile feature to deliver Gigabud banking Trojan outside standard app store controls
- **Dual-Function Mobile Malware**: Mantax Otax combines ransomware encryption, spyware data theft, and harassment/spam capabilities in single payload
- **Credential Theft via Compromised Insider Accounts**: Florida DMV breach initiated through stolen police department employee credentials
- **AI Platform Content Poisoning**: Weaponized Claude Artifacts, shared conversations, sponsored search results, and ClickFix-style lures to distribute malware
- **Mass AI-Generated Fraud**: Single threat actor generated 1 million personalized fraud emails in 3 days using AI automation

## Threat Actor Activities

- **ShinyHunters / Helix / Associated Extortion Gangs**: Conducting passkey-themed phishing campaigns targeting Microsoft 365 corporate accounts for data theft and extortion; receiving access from voice-based Graph API reconnaissance operators
- **GTG-20006 (Russian State-Sponsored, Aligned with Midnight)**: Disrupted by Anthropic for using Claude in AI-assisted malware reconstruction workflow to evade detection; attributed to broader Midnight Blizzard/APT29 reporting
- **Seven China-Based AI Labs (Alibaba, Moonshot, DeepSeek, Z.ai/Zhipu, MiniMax, plus two unnamed)**: Conducted industrial-scale illicit distillation attacks against Claude; disrupted by Anthropic
- **UNC3569 (China-Linked)**: Exploited Sogou Input Method flaw to deploy GRAYRABBIT backdoor for espionage operations
- **GoldFactory**: Android threat group exploiting Work Profile feature to deliver Gigabud banking Trojan in Indonesian campaign
- **Mantax Otax Operators**: Deploying novel Android malware combining ransomware, spyware, and harassment capabilities
- **Generative Threat Groups (GTGs) - Broad Category**: Anthropic's designation for state-sponsored groups, financially motivated criminals, and commercial surveillance operators abusing Claude for cyber attacks, weapons design, propaganda, and mass surveillance (December 2025–August 2026)
- **OpenAI Agent Swarm Operators**: Unattributed actors who orchestrated RubyGems supply chain attack via coordinated AI agents achieving RCE on RubyDoc servers (May 2026)
- **Conti Ransomware Gang (Historical)**: Ukrainian member sentenced to 4 years for 2021–2022 operations; indicates ongoing law enforcement pressure on ransomware ecosystems
- **Qilin Ransomware Affiliates**: One of three threat clusters exploiting Cisco FMC flaws (CVE-2026-20079) to deploy ransomware after credential theft
- **State-Sponsored Clusters Targeting Cisco FMC**: Two additional distinct threat clusters (beyond Qilin affiliates) exploiting Cisco FMC vulnerabilities, attributed to state-sponsored activity