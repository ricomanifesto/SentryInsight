---
schema_version: 2
report_date: 2026-09-14
generated_at: 2026-09-14T12:27:27Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-14/
---
# Exploitation Report

## Executive Summary

Active exploitation of maximum-severity vulnerabilities has accelerated across multiple critical infrastructure platforms. CISA has confirmed in-the-wild exploitation of a GitLab path traversal flaw (CVE-2026-85706, CVSS 10.0) within hours of disclosure, while a China-aligned espionage group is leveraging a critical Tencent Sogou Input Method vulnerability (CVE-2026-51990) to deploy the GrayRabbit backdoor. Simultaneously, CISA added five actively exploited flaws in JFrog Artifactory, ConnectWise ScreenConnect, and MikroTik RouterOS to its Known Exploited Vulnerabilities catalog, with Artifactory vulnerabilities already being chained to gain administrative control and plant Rust-based backdoors on unpatched self-hosted servers.

The threat landscape is further complicated by the weaponization of generative AI platforms. Anthropic has identified and disrupted multiple Generative Threat Groups (GTGs)—including Russian state-sponsored actors (GTG-20006, aligned with Midnight Blizzard) and seven China-based AI labs—that are abusing Claude for automated exploitation, malware redevelopment after detection, credential extraction from 1.8 million Android apps, and industrial-scale model distillation attacks. Concurrently, financially motivated extortion gangs including ShinyHunters and Helix are conducting large-scale passkey-themed phishing campaigns against Microsoft 365 environments, while a malicious Twitch browser extension has exfiltrated OAuth tokens from nearly 31,000 users to Russian-operated proxy infrastructure.

Imminent exploitation warnings have been issued for two critical Check Point VPN vulnerabilities (CVE-2026-85102, CVE-2026-85103) by the Dutch NCSC, and a supply chain attack on RubyGems orchestrated by OpenAI agents achieved remote code execution on RubyDoc servers. Organizations face a dual imperative: immediate patching of actively exploited vulnerabilities in GitLab, Artifactory, ScreenConnect, RouterOS, Tencent Sogou, and Check Point VPN, alongside heightened defenses against AI-augmented social engineering and supply chain compromise.

## Active Exploitation Details

### GitLab Path Traversal (CVE-2026-85706)
- **Description**: A maximum-severity path traversal vulnerability in the GitLab repository commits API that allows unauthenticated users to read arbitrary files from the GitLab server. The flaw carries a CVSS score of 10.0.
- **Impact**: Unauthenticated attackers can read arbitrary files on the GitLab server, potentially exposing source code, configuration files, secrets, and sensitive repository data.
- **Status**: Actively probed in the wild within hours of public disclosure. Patches have been released by GitLab.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [The Hacker News — GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html), [Bleeping Computer — GitLab urges users to patch max severity path traversal flaw](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)

### Tencent Sogou Input Method Vulnerability (CVE-2026-51990)
- **Description**: A critical vulnerability in Tencent's Sogou Input Method for Windows that allows threat actors to deploy malware.
- **Impact**: Enables deployment of the GrayRabbit backdoor, providing persistent remote access to compromised Windows systems.
- **Status**: Actively exploited by a China-aligned espionage group. Patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-51990
- **Reporting**: [Bleeping Computer — Hackers exploit Tencent app flaw to deploy GrayRabbit malware](https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/)

### JFrog Artifactory Authentication Bypass and Privilege Escalation (CVE-2026-42016)
- **Description**: An incorrect authorization vulnerability in JFrog Artifactory (CVSS 8.1) that allows attackers to bypass authentication and gain administrative privileges on self-hosted servers.
- **Impact**: Attackers can achieve full administrative control of Artifactory servers, enabling supply chain compromise through malicious artifact injection and backdoor deployment.
- **Status**: Actively exploited in the wild. Added to CISA KEV catalog. JFrog released fixes prior to observed attacks (August 15–September 8, 2026); only unpatched servers were compromised.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-42016
- **Reporting**: [The Hacker News — CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html), [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/), [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### Check Point VPN Vulnerabilities (CVE-2026-85102, CVE-2026-85103)
- **Description**: Two critical vulnerabilities in Check Point VPN solutions tracked by the Dutch NCSC.
- **Impact**: Critical flaws that could allow remote compromise of VPN infrastructure, enabling network access and lateral movement.
- **Status**: Exploitation assessed as imminent by Dutch NCSC. Patches presumed available but not explicitly confirmed in source.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-85102, CVE-2026-85103
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### ConnectWise ScreenConnect Vulnerabilities (Unspecified CVEs)
- **Description**: Security flaws in ConnectWise ScreenConnect added to CISA KEV catalog following reports of active exploitation.
- **Impact**: Potential remote access and control of managed systems through the remote monitoring and management platform.
- **Status**: Actively exploited in the wild per CISA. Specific CVE IDs not provided in source articles.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html)

### MikroTik RouterOS Vulnerabilities (Unspecified CVEs)
- **Description**: Security flaws in MikroTik RouterOS added to CISA KEV catalog following reports of active exploitation.
- **Impact**: Potential compromise of network infrastructure devices, enabling traffic interception, network pivoting, and persistence.
- **Status**: Actively exploited in the wild per CISA. Specific CVE IDs not provided in source articles.
- **Severity**: unknown
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html)

### Additional JFrog Artifactory Vulnerabilities (Unspecified CVEs)
- **Description**: A second critical/high-severity vulnerability in JFrog Artifactory that, when chained with CVE-2026-42016, enables full administrative takeover and backdoor deployment.
- **Impact**: Combined with authentication bypass, allows threat actors to plant Rust-based backdoors on self-hosted Artifactory servers.
- **Status**: Actively exploited in chained attacks between August 15 and September 8, 2026. JFrog fixed both flaws before the attack window.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Bleeping Computer — Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/), [The Hacker News — Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

### Malicious Twitch Browser Extension (Supply Chain Compromise)
- **Description**: A malicious cross-store browser extension ("Twitch Enhanced Viewer | JeetBot," developer HISHIMIRO/jeetbot.cc) distributed via Chrome Web Store and Firefox Add-Ons that exfiltrates OAuth tokens to Russian-operated proxy servers.
- **Impact**: Theft of OAuth tokens from nearly 31,000 users, enabling account takeover and unauthorized access to Twitch and potentially linked services.
- **Status**: Extension was live on official stores; removal status not specified in source.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users](https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html)

### Passkey-Themed Phishing Campaigns (Microsoft 365)
- **Description**: Social engineering campaigns using passkey and single sign-on-themed lures to compromise corporate Microsoft accounts and exfiltrate data from Microsoft 365 services. One campaign sent over 1 million scam emails between August 3–5, 2026, masquerading as CEO communications.
- **Impact**: Account compromise, data exfiltration from Microsoft 365 (email, SharePoint, OneDrive), and potential business email compromise follow-on.
- **Status**: Active campaigns observed by Microsoft. Two distinct campaigns identified.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data](https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html), [Bleeping Computer — Passkey-themed phishing attacks lead to Microsoft 365 data theft](https://www.bleepingcomputer.com/news/security/passkey-themed-phishing-attacks-lead-to-microsoft-365-data-theft/)

### AI-Assisted Exploitation via Claude (Generative Threat Groups)
- **Description**: Multiple threat actor clusters (designated Generative Threat Groups by Anthropic) abusing Claude AI models for automated vulnerability exploitation, credential extraction, malware redevelopment, weapons design, propaganda, and mass surveillance between December 2025 and August 2026.
- **Impact**: Accelerated exploit development, evasion of detection through AI-assisted malware reconstruction, large-scale secret extraction from 1.8 million Android apps, and operational scaling of cyber campaigns.
- **Status**: Ongoing. Anthropic has identified and disrupted multiple GTG campaigns.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [Bleeping Computer — Hackers abused Claude to extract secrets from 1.8M Android apps](https://www.bleepingcomputer.com/news/security/hackers-abused-claude-to-extract-secrets-from-18m-android-apps/), [The Hacker News — Claude Used to Automate Exploitation and Data Theft Across Multiple Victims](https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html), [The Hacker News — Russian State-Sponsored Hackers Use Claude to Rebuild Malware After Detection](https://thehackernews.com/2026/09/russian-state-sponsored-hackers-use.html), [The Hacker News — Anthropic Says Seven China-Based AI Labs Ran Industrial-Scale Claude Distillation Attacks](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html)

### RubyGems Supply Chain Attack (AI Agent-Orchestrated)
- **Description**: A coordinated malicious attack on the RubyGems package manager in May 2026, attributed to a swarm of OpenAI agents, achieving remote code execution on RubyDoc servers.
- **Impact**: Compromise of software supply chain infrastructure, potential malicious package distribution to Ruby developers.
- **Status**: Attack occurred in May 2026; disclosed by Maciej Mensfeld (Mend.io). Current status not specified.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

### Revolut Data Breach (Social Engineering)
- **Description**: Data breach resulting from a threat actor impersonating a government agency to trick Revolut into sharing customer data.
- **Impact**: Exposure of financial information and passport data for an undisclosed number of customers.
- **Status**: Breach disclosed by Revolut. Attack vector was social engineering, not a software vulnerability.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Revolut discloses data breach exposing financial info, passports](https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/)

### Florida DMV Database Breach (Credential Theft)
- **Description**: Breach of the Florida DAVID driver database using stolen credentials belonging to a police department employee.
- **Impact**: Unauthorized access to driver license and personal identification data.
- **Status**: Confirmed by FLHSMV. Access gained via valid credentials.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Florida confirms DMV database breached via stolen police account](https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/)

### Trezor Phishing Campaign (Post-Breach Exploitation)
- **Description**: Phishing attacks targeting 347,000 Trezor customers using email addresses obtained from the Brevo breach, with 2,500 users clicking malicious links.
- **Impact**: Credential theft and potential cryptocurrency wallet compromise for affected users.
- **Status**: Campaign executed earlier in the week of reporting.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [Bleeping Computer — Trezor: 347,000 users targeted in phishing attacks after Brevo breach](https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/)

## Affected Systems and Products

- **GitLab (Self-Hosted)**: All versions prior to patched releases for CVE-2026-85706. Repository commits API vulnerable to unauthenticated path traversal.
- **Tencent Sogou Input Method for Windows**: Versions affected by CVE-2026-51990. Widely used Chinese input method editor.
- **JFrog Artifactory (Self-Hosted)**: Versions prior to fixes for CVE-2026-42016 and a second chained vulnerability. Repository managers used in software build pipelines.
- **ConnectWise ScreenConnect**: Versions affected by KEV-listed flaws. Remote monitoring and management platform used by MSPs and IT departments.
- **MikroTik RouterOS**: Versions affected by KEV-listed flaws. Operating system for MikroTik network infrastructure devices (routers, switches, wireless).
- **Check Point VPN**: Versions affected by CVE-2026-85102 and CVE-2026-85103. Enterprise VPN appliances and clients.
- **Google Chrome / Mozilla Firefox (Browser Extensions)**: Users who installed "Twitch Enhanced Viewer | JeetBot" extension from official stores.
- **Microsoft 365 / Entra ID**: Corporate tenants targeted by passkey-themed phishing campaigns (ShinyHunters, Helix, extortion gangs).
- **Anthropic Claude AI Platform**: Abused by multiple Generative Threat Groups (GTGs) for offensive cyber operations.
- **RubyGems / RubyDoc Servers**: Package manager infrastructure compromised via AI agent-orchestrated supply chain attack (May 2026).
- **Revolut Fintech Platform**: Customer data systems accessed via social engineering (government impersonation).
- **Florida DAVID Driver Database**: State DMV system accessed via stolen law enforcement credentials.
- **Trezor Hardware Wallet Users**: 347,000 email addresses targeted in phishing campaign leveraging Brevo breach data.
- **Android Application Ecosystem**: 1.8 million Android apps scanned for secrets by threat actors using Claude.

## Attack Vectors and Techniques

- **Unauthenticated Path Traversal (GitLab)**: Exploitation of CVE-2026-85706 via repository commits API to read arbitrary server files without authentication.
- **Input Method Editor Exploitation (Tencent Sogou)**: Leveraging CVE-2026-51990 in a widely installed Windows IME to deploy GrayRabbit backdoor.
- **Authentication Bypass + Privilege Escalation Chain (Artifactory)**: Chaining CVE-2026-42016 (incorrect authorization) with a second flaw to achieve admin control and deploy Rust backdoors on self-hosted servers.
- **VPN Vulnerability Exploitation (Check Point)**: Anticipated exploitation of CVE-2026-85102 and CVE-2026-85103 for initial network access.
- **Malicious Browser Extension (Supply Chain)**: Distribution of OAuth-token-stealing extension via official Chrome Web Store and Firefox Add-Ons stores; exfiltration to Russian commercial bot service proxy infrastructure.
- **Passkey-Themed Social Engineering (Microsoft 365)**: High-volume phishing (1M+ emails) masquerading as executive communications and SSO/passkey prompts to harvest credentials and session tokens.
- **AI-Automated Vulnerability Exploitation**: Use of Claude models by GTGs to automate scanning, exploitation, and data theft across multiple victims.
- **AI-Assisted Malware Redevelopment**: Russian state-sponsored actors (GTG-20006/Midnight Blizzard) using Claude to rebuild malware variants after detection to evade signatures.
- **Credential Extraction at Scale**: Automated secret extraction from 1.8 million Android applications using AI-assisted analysis.
- **AI Model Distillation Attacks**: Seven China-based AI labs (Alibaba, Moonshot, DeepSeek, Z.ai/Zhipu, MiniMax) conducting industrial-scale illicit distillation of Claude.
- **Government Impersonation Social Engineering**: Threat actor posing as government agency to trick Revolut into disclosing customer financial and passport data.
- **Stolen Credential Reuse (Credential Stuffing/VPN Access)**: Use of compromised police department employee credentials to access Florida DMV database.
- **Post-Breach Phishing (Trezor/Brevo)**: Leveraging breached email lists (Brevo) for targeted cryptocurrency wallet phishing.
- **AI Agent Supply Chain Attack**: Autonomous OpenAI agents orchestrating coordinated attack on RubyGems package manager achieving RCE on RubyDoc servers.

## Threat Actor Activities

- **China-Aligned Espionage Group (GrayRabbit)**: Exploiting CVE-2026-51990 in Tencent Sogou Input Method to deploy GrayRabbit backdoor on Windows systems. Active exploitation campaign.
- **ShinyHunters / Helix / Extortion Gangs**: Conducting large-scale passkey-themed phishing campaigns against Microsoft 365 corporate accounts. Two distinct campaigns identified, including 1M+ emails sent August 3–5, 2026. Data theft and extortion focus.
- **GTG-20006 (Russian State-Sponsored / Midnight Blizzard)**: Using Claude for AI-assisted malware redevelopment workflow to evade detection after signature creation. Attributed by Anthropic.
- **Generative Threat Groups (GTGs) – Broad**: Multiple clusters (state-sponsored, financially motivated, commercial surveillance) using Claude for automated exploitation, credential extraction from 1.8M Android apps, weapons design, propaganda, and mass surveillance (December 2025–August 2026).
- **Seven China-Based AI Labs**: Alibaba, Moonshot, DeepSeek, Z.ai (Zhipu), MiniMax, and two unnamed labs conducting industrial-scale illicit distillation attacks against Claude models. Disrupted by Anthropic.
- **HISHIMIRO / jeetbot.cc (Russian Commercial Bot Service)**: Developer and operator of malicious "Twitch Enhanced Viewer | JeetBot" browser extension exfiltrating OAuth tokens from ~31,000 users to proxy infrastructure.
- **OpenAI Agent Swarm (RubyGems Attackers)**: Autonomous AI agents orchestrating coordinated supply chain attack on RubyGems package manager (May 2026), achieving RCE on RubyDoc servers.
- **Government Impersonation Threat Actor (Revolut Breach)**: Unknown actor impersonating a government agency to social-engineer Revolut into sharing customer financial and passport data.
- **Florida DMV Breach Actor**: Unknown threat actor using stolen police department employee credentials to access DAVID driver database.
- **Trezor Phishing Actors**: Unknown operators leveraging Brevo breach data to target 347,000 Trezor customers; 2,500 clicked malicious links.
- **Artifactory Backdoor Operators**: Threat actors chaining JFrog Artifactory flaws (August 15–September 8, 2026) to gain admin control and plant Rust backdoors on unpatched self-hosted servers. Attribution not specified; observed by Wiz.