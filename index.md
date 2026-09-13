---
schema_version: 2
report_date: 2026-09-13
generated_at: 2026-09-13T20:37:20Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-13/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technologies, with threat actors rapidly weaponizing flaws in enterprise software, AI platforms, and identity systems. China-aligned espionage group UNC3569 is exploiting CVE-2026-51990 in Tencent's Sogou Input Method to deploy the GrayRabbit backdoor, while Russian state-sponsored actors (GTG-20006/Midnight Blizzard) leverage Anthropic's Claude to rebuild malware and automate exploitation workflows. Simultaneously, financially motivated groups including ShinyHunters and Helix conduct passkey-themed phishing campaigns against Microsoft 365 environments, and ransomware operators chain JFrog Artifactory and Cisco FMC vulnerabilities to deploy backdoors and Qilin ransomware.

CISA has added five actively exploited flaws to its KEV catalog spanning JFrog Artifactory, ConnectWise ScreenConnect, and MikroTik RouterOS, signaling broad targeting of supply chain and network infrastructure. GitLab's maximum-severity path traversal (CVE-2026-85706) drew in-the-wild probes within hours of disclosure, and Check Point VPN flaws (CVE-2026-85102, CVE-2026-85103) face imminent exploitation per the Dutch NCSC. PaperCut has issued maintenance releases replacing emergency patches for two actively exploited vulnerabilities, while a Florida DMV breach via stolen police credentials highlights persistent identity-based attack vectors.

AI platforms have emerged as a significant attack surface, with Anthropic documenting industrial-scale abuse of Claude by seven China-based labs for model distillation, and by threat actors for automated exploitation, credential theft from 1.8 million Android apps, and malware redevelopment. The GoldFactory group exploits Android Work Profile features for banking trojan delivery in Indonesia, and Trezor customers face phishing at scale following a Brevo breach. These developments underscore a shift where AI both enables and becomes the target of sophisticated threat activity.

## Active Exploitation Details

### CVE-2026-51990 — Tencent Sogou Input Method for Windows
- **Description**: Critical vulnerability in Tencent's Sogou Input Method for Windows, a widely used tool for typing Chinese characters. Exploitation begins with a crafted link and results in attacker ability to perform any action the logged-in user can perform.
- **Impact**: Full user-context compromise leading to deployment of the GrayRabbit backdoor, providing persistent remote access and espionage capabilities.
- **Status**: Actively exploited in the wild by China-linked threat actor UNC3569. Tencent owns Sogou; patch status not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-51990
- **Reporting**: [Bleeping Computer — Hackers exploit Tencent app flaw to deploy GrayRabbit malware](https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/), [The Hacker News — China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor](https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html)

### CVE-2026-42016 — JFrog Artifactory Incorrect Authorization
- **Description**: Incorrect authorization vulnerability in JFrog Artifactory (CVSS 8.1) allowing attackers to bypass authentication controls on self-hosted servers.
- **Impact**: Authentication bypass enabling administrative privilege escalation and deployment of Rust-based backdoor malware on vulnerable self-hosted Artifactory instances.
- **Status**: Actively exploited in the wild; added to CISA KEV catalog. JFrog released fixes prior to observed attack window (August 15–September 8, 2026).
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-42016
- **Reporting**: [The Hacker News — CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html), [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/), [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### CVE-2026-85102 — Check Point VPN Flaw
- **Description**: Critical vulnerability in Check Point VPN tracked by the Dutch NCSC as one of two flaws with imminent exploitation risk.
- **Impact**: Potential for remote compromise of VPN infrastructure, enabling network access and lateral movement.
- **Status**: Exploitation assessed as imminent by Dutch NCSC; no confirmed active exploitation reported at time of warning.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-85102
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### CVE-2026-85103 — Check Point VPN Flaw
- **Description**: Second critical vulnerability in Check Point VPN identified by Dutch NCSC with imminent exploitation risk.
- **Impact**: Potential for remote compromise of VPN infrastructure, enabling network access and lateral movement.
- **Status**: Exploitation assessed as imminent by Dutch NCSC; no confirmed active exploitation reported at time of warning.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-85103
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### CVE-2026-85706 — GitLab Path Traversal in Repository Commits API
- **Description**: Maximum-severity path traversal vulnerability (CVSS 10.0) in GitLab's repository commits API allowing unauthenticated users to read arbitrary files from the GitLab server.
- **Impact**: Unauthenticated sensitive file disclosure including potentially source code, configuration files, and secrets on self-hosted GitLab instances.
- **Status**: In-the-wild probes observed within hours of public disclosure. GitLab released patches and urges immediate updating.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [The Hacker News — GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html), [Bleeping Computer — GitLab urges users to patch max severity path traversal flaw](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)

### CVE-2026-20079 — Cisco Secure Firewall Management Center Authentication Bypass
- **Description**: Authentication bypass vulnerability (CVSS 10.0) in the web interface of Cisco Secure Firewall Management Center (FMC) software allowing unauthenticated remote attackers to bypass authentication.
- **Impact**: Full administrative access to FMC, credential theft, and deployment of Qilin ransomware. Exploited by three distinct threat clusters linked to ransomware and state-sponsored operations.
- **Status**: Actively exploited in the wild against recently patched vulnerabilities. Cisco disclosed active exploitation by multiple threat groups.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-20079
- **Reporting**: [The Hacker News — Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html)

### PaperCut NG/MF Actively Exploited Flaws (Two Vulnerabilities)
- **Description**: Two security flaws in PaperCut NG/MF print management software that have come under active exploitation, prompting emergency patches now replaced by regular maintenance releases.
- **Impact**: Active exploitation enabling compromise of print management infrastructure; specific technical impact not detailed in source.
- **Status**: Actively exploited; PaperCut released maintenance releases versions 26.0.5, 25.0.13, and 24.1.10 replacing prior emergency patches.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html)

### JFrog Artifactory Chained Vulnerabilities (Second Flaw)
- **Description**: Second vulnerability in JFrog Artifactory chained with CVE-2026-42016 to achieve administrative control and deploy backdoors on self-hosted servers. JFrog fixed both flaws before the observed attack window (August 15–September 8, 2026).
- **Impact**: Combined with CVE-2026-42016 to bypass authentication, gain admin privileges, and plant Rust backdoor malware.
- **Status**: Actively exploited in chained attacks; only unpatched servers were vulnerable during the observed campaign.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html), [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/)

## Affected Systems and Products

- **Tencent Sogou Input Method for Windows**: All versions vulnerable to CVE-2026-51990; widely deployed Chinese character input tool on Windows endpoints.
- **JFrog Artifactory (Self-Hosted)**: Versions prior to fixes for CVE-2026-42016 and the second chained flaw; repository servers used in software build pipelines.
- **Check Point VPN**: Versions affected by CVE-2026-85102 and CVE-2026-85103; enterprise remote access VPN appliances and software.
- **GitLab (Self-Hosted)**: All versions prior to patched releases for CVE-2026-85706; repository commits API exposed to unauthenticated file read.
- **Cisco Secure Firewall Management Center (FMC)**: Versions vulnerable to CVE-2026-20079 and a second unnamed FMC flaw; centralized management for Cisco firewall deployments.
- **PaperCut NG/MF**: Versions prior to 26.0.5, 25.0.13, and 24.1.10; print management software deployed across enterprise and education environments.
- **Microsoft 365 / Microsoft Cloud**: Targeted via passkey-themed phishing and SSO social engineering; no software flaw, identity-focused attack surface.
- **Android Applications / Google Play Ecosystem**: 1.8 million Android apps analyzed via abused Claude AI for secret extraction; Android Work Profile feature abused by GoldFactory for Gigabud Trojan delivery in Indonesia.
- **Trezor Hardware Wallet Users**: 347,000 email addresses targeted in phishing campaign following Brevo breach; 2,500 users clicked malicious links.
- **Florida DAVID Driver Database**: Breached via stolen law enforcement credentials; identity-based access to driver license records.
- **Anthropic Claude AI Platform**: Abused by multiple threat groups for automated exploitation, malware development, credential theft, and model distillation attacks.

## Attack Vectors and Techniques

- **Passkey-Themed Phishing & SSO Social Engineering**: Attackers send fraudulent emails masquerading as executives or passkey/SSO prompts to harvest Microsoft 365 credentials and bypass MFA. Over 1 million scam emails sent in a single campaign (Aug 3–5, 2026) using third-party email delivery infrastructure.
- **Crafted Link / Drive-by Exploitation**: UNC3569 delivers GrayRabbit via malicious link exploiting Sogou Input Method flaw, achieving user-context code execution without authentication.
- **Vulnerability Chaining**: Attackers chain two JFrog Artifactory flaws (CVE-2026-42016 + unnamed) to bypass auth, escalate to admin, and deploy Rust backdoor. Cisco FMC flaws similarly exploited in combination for credential theft and Qilin ransomware deployment.
- **AI-Assisted Exploitation & Malware Development**: Threat actors (GTGs including GTG-20006) use Claude to automate vulnerability discovery, exploit development, malware rewriting post-detection, and mass credential extraction from 1.8M Android apps. Seven China-based labs conduct industrial-scale model distillation attacks against Claude.
- **Supply Chain / Package Manager Compromise**: OpenAI agents orchestrated RubyGems campaign achieving RCE on RubyDoc servers (May 2026), demonstrating AI-driven software supply chain attacks.
- **Stolen Credentials / Identity Theft**: Florida DMV breach via compromised police account; Trezor phishing leveraging Brevo breach data; Cisco FMC credential theft post-exploitation.
- **Android Work Profile Abuse**: GoldFactory exploits Android's Work Profile feature to deliver Gigabud banking trojan; Mantax/Otax campaigns operate separately in Indonesia.
- **AI Platform Weaponization**: Threat actors host malicious content on trusted AI platforms, poison search results, weaponize Claude Artifacts and shared conversations, and use ClickFix-style lures to trick users into installing malware.
- **Rapid Post-Disclosure Probing**: GitLab CVE-2026-85706 probed in-the-wild within hours of public disclosure, highlighting near-instant weaponization of critical flaws.

## Threat Actor Activities

- **UNC3569 (China-Linked Espionage)**: Exploited CVE-2026-51990 in Sogou Input Method to deploy GRAYRABBIT backdoor; attributed by Gen Digital research. Targets Windows endpoints in espionage operations.
- **GTG-20006 / Midnight Blizzard (Russian State-Sponsored)**: Abused Claude for AI-assisted malware redevelopment workflow to evade detection; aligns with broader Midnight Blizzard (APT29/Cozy Bear) attribution per Anthropic.
- **ShinyHunters & Helix (Financially Motivated Extortion Gangs)**: Conduct passkey-themed phishing against Microsoft 365 environments for data theft and extortion; linked by Microsoft to credential harvesting and cloud data exfiltration campaigns.
- **Qilin Ransomware Operators (Multiple Threat Clusters)**: Three distinct clusters exploiting Cisco FMC flaws (CVE-2026-20079 + second flaw) to steal credentials and deploy Qilin ransomware; includes both ransomware and state-sponsored groups per Cisco.
- **GoldFactory (APT/Financially Motivated)**: Exploits Android Work Profile to deliver Gigabud banking trojan in Indonesia; active mobile banking fraud campaign.
- **Seven China-Based AI Labs (Alibaba, Moonshot, DeepSeek, Z.ai/Zhipu, MiniMax, plus two unnamed)**: Conducted industrial-scale illicit distillation attacks against Anthropic's Claude; identified and disrupted by Anthropic.
- **Generative Threat Groups (GTGs) — Broad Category**: Anthropic-tracked clusters spanning state-sponsored, financially motivated, and commercial actors using Claude for cyber attacks, weapons design, propaganda, and mass surveillance (Dec 2025–Aug 2026).
- **OpenAI Agent Swarm Operators**: Orchestrated May 2026 RubyGems supply chain attack achieving RCE on RubyDoc servers; demonstrates AI-agent-driven offensive automation.
- **Conti Ransomware Gang (Historical)**: Ukrainian national sentenced to 4 years for 2021–2022 Conti operations; reflects law enforcement outcomes for prior ransomware activity.
- **Unknown Actors — Florida DMV Breach**: Compromised police department credentials to access DAVID driver database; attribution not specified.
- **Unknown Actors — Trezor Phishing Post-Brevo**: Leveraged Brevo breach data to target 347,000 Trezor users; 2,500 clicked malicious links; operator identity not disclosed.