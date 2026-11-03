---
schema_version: 2
report_date: 2026-09-12
generated_at: 2026-09-12T20:27:13Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-12/
---
# Exploitation Report

## Executive Summary

CISA has added five actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog, spanning JFrog Artifactory, ConnectWise ScreenConnect, and MikroTik RouterOS. The most critical of these is CVE-2026-42016 (CVSS 8.1), an authorization bypass in JFrog Artifactory that threat actors are chaining with a second flaw to gain administrative control and deploy Rust-based backdoors on unpatched self-hosted servers. Simultaneously, the Dutch NCSC has warned that exploitation of two critical Check Point VPN flaws (CVE-2026-85102 and CVE-2026-85103) is imminent, urging immediate mitigation.

GitLab's maximum-severity path traversal vulnerability (CVE-2026-85706, CVSS 10.0) has drawn in-the-wild probes within hours of public disclosure, prompting urgent patching advisories. Cisco has confirmed that three distinct threat clusters—including ransomware operators and state-sponsored actors—are actively exploiting CVE-2026-20079 (CVSS 10.0), an authentication bypass in Secure Firewall Management Center, to steal credentials and deploy Qilin ransomware. PaperCut has also released maintenance updates replacing emergency patches for two actively exploited flaws in PaperCut NG/MF.

A significant trend across multiple reports is the weaponization of generative AI platforms by both financially motivated and state-sponsored threat actors. Anthropic has identified and disrupted industrial-scale abuse of Claude by seven China-based AI labs conducting distillation attacks, as well as a Russian state-sponsored group (GTG-20006, aligned with Midnight Blizzard/APT29) using Claude to rebuild malware after detection. Threat actors are also leveraging AI to automate exploitation, generate personalized phishing at scale, and extract secrets from millions of Android applications. China-linked UNC3569 exploited a Sogou Input Method flaw to deploy the GRAYRABBIT backdoor, while Android banking trojans (Gigabud, Mantax Otax) and passkey-themed phishing campaigns targeting Microsoft 365 demonstrate expanding mobile and identity-focused attack surfaces.

## Active Exploitation Details

### CVE-2026-42016 — JFrog Artifactory Incorrect Authorization
- **Description**: An incorrect authorization vulnerability in JFrog Artifactory that allows attackers to bypass authentication controls. This flaw is being chained with a second Artifactory vulnerability to escalate privileges.
- **Impact**: Attackers can bypass authentication, gain administrative privileges on self-hosted Artifactory servers, and deploy persistent backdoor malware (Rust-based) to maintain long-term access to software supply chain infrastructure.
- **Status**: Actively exploited in the wild; patches available from JFrog. CISA added to KEV catalog on September 2026. Only unpatched self-hosted servers are vulnerable.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-42016
- **Reporting**: [The Hacker News — CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html), [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/), [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### CVE-2026-85102 — Check Point VPN Critical Flaw
- **Description**: A critical vulnerability in Check Point VPN identified by the Dutch NCSC as having imminent exploitation risk. Specific technical details not disclosed in the advisory.
- **Impact**: Potential for unauthorized access to corporate VPN infrastructure, leading to network infiltration, data theft, and lateral movement.
- **Status**: Exploitation assessed as imminent by Dutch NCSC; mitigation guidance issued. Patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **CVE IDs**: CVE-2026-85102
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### CVE-2026-85103 — Check Point VPN Critical Flaw
- **Description**: A second critical vulnerability in Check Point VPN identified by the Dutch NCSC as having imminent exploitation risk. Specific technical details not disclosed in the advisory.
- **Impact**: Potential for unauthorized access to corporate VPN infrastructure, leading to network infiltration, data theft, and lateral movement.
- **Status**: Exploitation assessed as imminent by Dutch NCSC; mitigation guidance issued. Patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **CVE IDs**: CVE-2026-85103
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### CVE-2026-85706 — GitLab Path Traversal in Repository Commits API
- **Description**: A maximum-severity path traversal vulnerability in GitLab's repository commits API that allows unauthenticated users to read arbitrary files from the GitLab server.
- **Impact**: Unauthenticated remote attackers can read sensitive files including configuration, source code, secrets, and potentially source code signing keys from vulnerable GitLab instances.
- **Status**: Actively probed in the wild within hours of public disclosure; patches released by GitLab. Urgent patching advised.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [The Hacker News — GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html), [Bleeping Computer — GitLab urges users to patch max severity path traversal flaw](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)

### CVE-2026-20079 — Cisco Secure Firewall Management Center Authentication Bypass
- **Description**: An authentication bypass vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) software that allows unauthenticated, remote attackers to bypass authentication.
- **Impact**: Attackers can steal administrative credentials and deploy Qilin ransomware. Exploited by three distinct threat clusters including ransomware operators and state-sponsored groups.
- **Status**: Actively exploited in the wild; patches available from Cisco.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20079
- **Reporting**: [The Hacker News — Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html)

### PaperCut NG/MF Actively Exploited Flaws (Two Vulnerabilities)
- **Description**: Two security flaws in PaperCut NG/MF that have come under active exploitation, prompting emergency patches that have now been replaced with regular maintenance releases.
- **Impact**: Active exploitation allowing attackers to compromise print management servers; specific impact details not disclosed in source.
- **Status**: Actively exploited; fixed in PaperCut NG/MF versions 26.0.5, 25.0.13, and 24.1.10 released as Regular Maintenance Releases.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html)

### Sogou Input Method Flaw Exploited by UNC3569
- **Description**: A vulnerability in Sogou Input Method, a widely used Chinese character input tool for Windows, exploited via a crafted link to achieve code execution in the context of the logged-in user.
- **Impact**: Attackers gain full user-context control on victim machines, enabling deployment of the GRAYRABBIT backdoor for persistent access and espionage.
- **Status**: Actively exploited by China-linked threat group UNC3569; patch status not specified in source.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor](https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html)

## Affected Systems and Products

- **JFrog Artifactory (Self-Hosted)**: Versions prior to the patched releases; only self-hosted deployments affected. Used as software supply chain repository for build pipelines.
- **ConnectWise ScreenConnect**: Specific versions not detailed in source; added to CISA KEV for active exploitation.
- **MikroTik RouterOS**: Specific versions not detailed in source; added to CISA KEV for active exploitation.
- **Check Point VPN**: Enterprise VPN appliances and software; specific versions not detailed in Dutch NCSC advisory.
- **GitLab (Self-Managed and GitLab.com)**: All versions prior to the security release addressing CVE-2026-85706; affects both self-managed instances and SaaS platform.
- **Cisco Secure Firewall Management Center (FMC)**: Software versions vulnerable to CVE-2026-20079; specific version range not detailed in source.
- **PaperCut NG/MF**: Versions prior to 26.0.5, 25.0.13, and 24.1.10; print management software deployed on Windows, Linux, and macOS servers.
- **Sogou Input Method**: Windows versions of the input method editor; widely deployed in Chinese-language environments.
- **Android Devices**: Devices running malicious applications (Gigabud, Mantax Otax) delivered via app cloning and Work Profile abuse; Google Play Protect and sideloaded APKs.
- **Microsoft 365 / Entra ID**: Corporate tenants targeted via passkey-themed phishing and Graph API reconnaissance; BYOD personal devices used as initial access vector.

## Attack Vectors and Techniques

- **Vulnerability Chaining (Artifactory)**: Attackers chain an authentication bypass (CVE-2026-42016) with a second Artifactory flaw to escalate from unauthenticated access to full administrative control, then deploy a Rust-based backdoor for persistence.
- **Path Traversal / Arbitrary File Read (GitLab)**: Unauthenticated exploitation of CVE-2026-85706 via the repository commits API to read arbitrary server files, including secrets and configuration.
- **Authentication Bypass (Cisco FMC)**: Unauthenticated remote attackers bypass the FMC web interface login (CVE-2026-20079) to steal credentials and deploy Qilin ransomware.
- **AI-Assisted Malware Development**: Russian state-sponsored actors (GTG-20006 / Midnight Blizzard) use Claude to rebuild and obfuscate malware after detection, accelerating the detection-evasion cycle.
- **AI-Automated Exploitation & Data Theft**: Generative Threat Groups (GTGs) use Claude to automate vulnerability scanning, exploitation, credential harvesting, and data exfiltration across multiple victims (Dec 2025–Aug 2026).
- **Industrial-Scale AI Model Distillation**: Seven China-based AI labs (Alibaba, Moonshot, DeepSeek, Z.ai, MiniMax) conduct large-scale distillation attacks against Claude to replicate model capabilities without authorization.
- **Passkey / SSO-Themed Social Engineering**: ShinyHunters, Helix, and extortion gangs use passkey and single sign-on-themed phishing to compromise Microsoft 365 accounts and steal data.
- **Voice Phishing (Vishing) + BYOD Abuse**: Threat actors use voice calls to trick BYOD users into approving MFA prompts, then leverage Microsoft Graph API for reconnaissance and pass access to extortion groups.
- **Android Work Profile Abuse**: GoldFactory threat group exploits Android's Work Profile feature to deliver the Gigabud banking trojan, bypassing user interaction requirements.
- **App Cloning & Trojanization**: Mantax Otax combines ransomware (file encryption), spyware (data theft), and harassment (spam/notifications) in a single Android malware strain.
- **Supply Chain Credential Theft (Brevo → Trezor)**: Breach of marketing provider Brevo exposes 347,000 Trezor customer emails; phishing campaign yields 2,500 compromised users.
- **Stolen Law Enforcement Credentials**: Attackers use compromised police department employee credentials to access Florida DMV's DAVID driver database.

## Threat Actor Activities

- **GTG-20006 (Russian State-Sponsored / Midnight Blizzard / APT29)**: Uses Claude for AI-assisted malware reconstruction after detection, maintaining operational tempo. Attributed by Anthropic. Active December 2025–August 2026.
- **Generative Threat Groups (GTGs) — Multiple Clusters**: Anthropic-tracked clusters spanning state-sponsored espionage, financially motivated cybercrime, and commercial surveillance operators. Use Claude for automated exploitation, weapons design, propaganda, and mass surveillance.
- **Seven China-Based AI Labs (Alibaba, Moonshot, DeepSeek, Z.ai/Zhipu, MiniMax)**: Conduct industrial-scale distillation attacks against Claude to extract model capabilities. Disrupted by Anthropic.
- **UNC3569 (China-Linked)**: Exploits Sogou Input Method flaw via crafted links to deploy GRAYRABBIT backdoor for persistent espionage access on Windows endpoints.
- **ShinyHunters & Helix (Extortion Gangs)**: Conduct passkey/SSO-themed phishing against Microsoft 365; leverage vishing and Graph API reconnaissance; partner with initial access brokers using BYOD abuse.
- **GoldFactory (Android Threat Group)**: Exploits Android Work Profile to deliver Gigabud banking trojan targeting financial institutions in Indonesia.
- **Mantax Otax Operators**: Deploy dual-purpose Android malware (ransomware + spyware + harassment) via app cloning campaigns.
- **Qilin Ransomware Affiliates (Three Threat Clusters)**: Exploit CVE-2026-20079 in Cisco FMC to steal credentials and deploy Qilin ransomware; includes both ransomware-focused and state-sponsored clusters per Cisco.
- **Conti Ransomware Gang (Historical)**: Ukrainian member sentenced to 4 years for 2021–2022 operations; demonstrates law enforcement follow-through on ransomware actors.