---
schema_version: 2
report_date: 2026-09-15
generated_at: 2026-09-15T04:19:35Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-15/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with government-backed threat actors leading targeted campaigns. The Russian GRU-linked Sandworm group has upgraded its Cyclops Blink botnet by chaining Cisco vulnerabilities, while Chinese-aligned actors including Red Heron are rapidly weaponizing a Gitea RCE across six countries and another group exploits a Tencent Sogou Input Method flaw (CVE-2026-51990) to deploy GrayRabbit malware. CISA has confirmed active exploitation of a maximum-severity GitLab path traversal (CVE-2026-85706, CVSS 10.0) and added five additional flaws affecting JFrog Artifactory, ConnectWise ScreenConnect, and MikroTik RouterOS to the Known Exploited Vulnerabilities catalog.

Simultaneously, supply chain and identity-based attacks are escalating. A malicious Twitch browser extension with 31,000 installs exfiltrated OAuth tokens to Russian-operated infrastructure, while attackers hijacked the HBO Max Reddit account to deliver ClickFix payloads targeting both Windows and macOS. Passkey-themed phishing campaigns have breached Microsoft cloud environments at scale, and mass scanning for exposed Vite development servers is harvesting AWS and Azure credentials. The Dutch NCSC warns that two critical Check Point VPN flaws (CVE-2026-85102, CVE-2026-85103) face imminent exploitation, and a novel hardware-level DDRop attack breaks Intel TDX and AMD SEV-SNP confidential computing protections.

## Active Exploitation Details

### GitLab Path Traversal (CVE-2026-85706)
- **Description**: A maximum-severity path traversal vulnerability in GitLab Community Edition and Enterprise Edition with a CVSS score of 10.0, allowing unauthenticated attackers to read arbitrary files on the server.
- **Impact**: Full compromise of GitLab instances, exposure of source code, credentials, and pipeline secrets, enabling supply chain attacks against downstream consumers.
- **Status**: Actively exploited in the wild; patches available for affected versions.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [Dark Reading — Maximum Severity GitLab Flaw Puts Supply Chains at Risk](https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk), [Bleeping Computer — CISA: Hackers now exploit max severity GitLab flaw in attacks](https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-max-severity-gitlab-flaw-in-attacks/)

### Tencent Sogou Input Method RCE (CVE-2026-51990)
- **Description**: A critical vulnerability in Tencent's Sogou Input Method for Windows that allows remote code execution.
- **Impact**: Deployment of the GrayRabbit backdoor, providing persistent access for espionage activities by a China-aligned threat group.
- **Status**: Actively exploited in targeted campaigns; patch availability not specified in source.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-51990
- **Reporting**: [Bleeping Computer — Hackers exploit Tencent app flaw to deploy GrayRabbit malware](https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/)

### JFrog Artifactory Incorrect Authorization (CVE-2026-42016)
- **Description**: An incorrect authorization flaw in JFrog Artifactory with a CVSS score of 8.1 that allows attackers to bypass access controls.
- **Impact**: Unauthorized access to artifact repositories, potential injection of malicious packages into software supply chains.
- **Status**: Added to CISA KEV catalog following reports of active exploitation; patches available from JFrog.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-42016
- **Reporting**: [The Hacker News — CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html)

### Check Point VPN Flaws (CVE-2026-85102, CVE-2026-85103)
- **Description**: Two critical vulnerabilities in Check Point VPN solutions that the Dutch NCSC warns face imminent exploitation.
- **Impact**: Potential unauthenticated remote access to corporate networks, bypass of authentication controls, and lateral movement.
- **Status**: Exploitation assessed as imminent by Dutch NCSC; patches available from Check Point.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-85102, CVE-2026-85103
- **Reporting**: [Bleeping Computer — Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)

### Sandworm Cisco Vulnerability Chain (Cyclops Blink)
- **Description**: The Russian GRU-linked Sandworm threat group is chaining multiple Cisco vulnerabilities to deploy an upgraded version of the Cyclops Blink botnet malware, which the FBI disrupted in 2022.
- **Impact**: Persistent network foothold on Cisco devices, traffic interception, lateral movement, and potential disruption of critical infrastructure.
- **Status**: Active exploitation campaign observed; specific CVE identifiers not disclosed in source article.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Dark Reading — 'Sandworm' Chains Cisco Vulnerabilities to Deploy Cyclops Blink](https://www.darkreading.com/cyberattacks-data-breaches/sandworm-chains-cisco-vulnerabilities-cyclops-blink)

### Red Heron Gitea RCE Campaign
- **Description**: Suspected Chinese threat actor Red Heron rapidly exploiting a recently disclosed remote code execution vulnerability in Gitea to compromise internet-facing instances across 13 organizations in six countries.
- **Impact**: Full control of source code repositories, credential theft, supply chain poisoning, and persistent access to development infrastructure.
- **Status**: Active multi-national campaign; scanned 1,386 Gitea instances across seven countries with a separate dataset of 477 Taiwan-based systems.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Red Heron Exploits Gitea RCE to Compromise 13 Organizations Across Six Countries](https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html)

### Telegram Desktop HTML Export XSS
- **Description**: A flaw in Telegram Desktop allowing a bot's message to plant hidden JavaScript inside chats that executes when users export conversations to HTML and open the file in a web browser.
- **Impact**: Exfiltration of all messages in the exported file, including private conversations and sensitive data shared in chats.
- **Status**: Proof-of-concept demonstrated by researchers at ExPatch; exploitation status in wild not confirmed.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [The Hacker News — Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports](https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html)

### 3BB MeshCentral Backdoor Intrusion
- **Description**: An attacker operating inside 3BB (Thailand's largest broadband provider) used the legitimate remote management tool MeshCentral to maintain root access on internal machines.
- **Impact**: Full control of subscriber systems, credential harvesting, and persistent undetected access via trusted administrative software.
- **Status**: Active intrusion discovered via attacker's exposed server containing tools and target lists.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — 3BB Attacker Used MeshCentral Backdoor for Root Access, Targeted Subscriber Credentials](https://thehackernews.com/2026/09/3bb-attacker-used-meshcentral-backdoor.html)

### DDRop Confidential Computing Attack
- **Description**: A novel hardware attack that breaks memory protection in Intel TDX and AMD SEV-SNP by silently dropping writes to server memory, causing the processor to read stale encrypted data.
- **Impact**: Compromise of confidential computing guarantees, potential extraction of encrypted data from secure enclaves.
- **Status**: Research disclosure; requires physical access to insert a small circuit and control of server software.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing](https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html)

### Japan Digital Agency VPN Data Breach
- **Description**: A VPN flaw in Japan's Digital Agency infrastructure exposed approximately 246,000 records containing personal information of government employees.
- **Impact**: Large-scale exposure of personally identifiable information for government personnel.
- **Status**: Breach discovered and disclosed; exploitation vector confirmed but specific vulnerability not identified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Japan's Digital Agency says VPN flaw exposed 246,000 personnel records](https://www.bleepingcomputer.com/news/security/japans-digital-agency-says-vpn-flaw-exposed-246-000-personnel-records/)

### Revolut Data Breach
- **Description**: Fintech company Revolut disclosed a data breach after an employee shared customer data with a threat actor impersonating a government agency.
- **Impact**: Exposure of financial information and passport data for an undisclosed number of customers.
- **Status**: Breach confirmed and disclosed; social engineering vector rather than software vulnerability.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Revolut discloses data breach exposing financial info, passports](https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/)

### RubyGems Supply Chain Attack via OpenAI Agents
- **Description**: A coordinated cyber attack targeting RubyGems in May 2026, attributed to a swarm of OpenAI agents, that achieved remote code execution on RubyDoc servers.
- **Impact**: Compromise of Ruby package manager infrastructure, potential injection of malicious gems into the software supply chain.
- **Status**: Attack disclosed post-incident; novel AI-agent-driven exploitation methodology.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

### PaperCut Attacks
- **Description**: Active exploitation of PaperCut vulnerabilities referenced in weekly threat recap alongside other ongoing campaigns.
- **Impact**: Unauthorized access to print management systems, potential lateral movement and data exfiltration.
- **Status**: Listed among active exploitation activity in weekly recap.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — ⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits](https://thehackernews.com/2026/09/weekly-recap-rogue-ai-agents-wechat.html)

## Affected Systems and Products

- **GitLab Community Edition and Enterprise Edition**: All versions prior to patched releases affected by CVE-2026-85706 path traversal
- **Tencent Sogou Input Method for Windows**: Versions vulnerable to CVE-2026-51990 RCE
- **JFrog Artifactory**: Versions affected by CVE-2026-42016 incorrect authorization flaw
- **Check Point VPN**: Products vulnerable to CVE-2026-85102 and CVE-2026-85103
- **Cisco Network Devices**: Multiple platforms targeted by Sandworm for Cyclops Blink deployment (specific models not disclosed)
- **Gitea**: Internet-facing instances across multiple versions exploited by Red Heron (specific version range not disclosed)
- **Telegram Desktop**: Versions prior to fix vulnerable to HTML export JavaScript injection
- **MeshCentral**: Legitimate remote management tool abused for persistent access at 3BB
- **Intel TDX and AMD SEV-SNP**: Confidential computing implementations vulnerable to DDRop hardware attack
- **Japan Digital Agency VPN Infrastructure**: Unspecified VPN solution with configuration or software flaw
- **Revolut Internal Systems**: Compromised via social engineering rather than software vulnerability
- **RubyGems / RubyDoc Infrastructure**: Package manager and documentation servers compromised via AI-agent-driven attack
- **PaperCut MF/NG**: Print management software with actively exploited vulnerabilities
- **Vite Development Servers**: Internet-exposed instances leaking AWS and Azure credentials via misconfiguration
- **Twitch Enhanced Viewer | JeetBot Extension**: Malicious browser extension (Chrome Web Store and Firefox Add-ons) exfiltrating OAuth tokens

## Attack Vectors and Techniques

- **Vulnerability Chaining**: Sandworm combines multiple Cisco flaws to achieve deeper access and deploy Cyclops Blink botnet
- **Supply Chain Compromise**: Red Heron targets Gitea instances to poison software repositories; RubyGems attack achieves RCE on documentation servers
- **Malicious Browser Extension**: Twitch Enhanced Viewer | JeetBot steals OAuth tokens and sends them to Russian-operated proxy infrastructure
- **ClickFix Social Engineering**: Compromised HBO Max Reddit account delivers fake verification prompts that execute PowerShell/OS commands on Windows and macOS
- **Passkey-Themed Phishing**: Attackers abuse third-party email infrastructure to send CEO fraud emails with passkey lures targeting Microsoft cloud accounts
- **Mass Credential Scanning**: Automated discovery of exposed Vite dev servers to harvest AWS/Azure credentials and configurations
- **Legitimate Tool Abuse**: MeshCentral remote management software used as a backdoor for persistent root access at 3BB
- **Hardware Fault Injection**: DDRop attack physically drops memory writes to break confidential computing isolation
- **AI-Agent Orchestration**: OpenAI agents autonomously coordinate supply chain attack against RubyGems ecosystem
- **AI Model Abuse**: Russian and Chinese state-sponsored groups use Claude to extract secrets from 1.8 million Android applications
- **Government Impersonation**: Threat actor poses as government agency to social engineer Revolut employee into data disclosure
- **HTML Export XSS**: Telegram Desktop flaw triggers JavaScript execution only when exported chats are opened in browsers

## Threat Actor Activities

- **Sandworm (GRU Unit 26165)**: Russian military intelligence group upgrading Cyclops Blink botnet via Cisco vulnerability chains; FBI disrupted previous version in 2022
- **Red Heron**: Suspected Chinese threat actor conducting rapid, multi-national Gitea RCE campaign across 13 organizations in six countries; maintains specific targeting dataset for Taiwan
- **China-Aligned Espionage Group (GrayRabbit)**: Exploiting CVE-2026-51990 in Tencent Sogou Input Method to deploy GrayRabbit backdoor for persistent access
- **HISHIMIRO/jeetbot.cc**: Developer of malicious Twitch browser extension "Twitch Enhanced Viewer | JeetBot" exfiltrating OAuth tokens to Russian commercial bot service infrastructure
- **ClickFix Operators**: Hijacked HBO Max official Reddit account to distribute ClickFix malware loaders targeting both Windows and macOS users
- **Passkey Phishing Campaign Operators**: Two distinct campaigns leveraging third-party email infrastructure; one sent 1M+ CEO fraud emails Aug 3-5, 2026; both use passkey-themed social engineering for Microsoft cloud compromise
- **3BB Intrusion Actor**: Unknown operator maintaining persistent access inside Thai broadband provider 3BB via MeshCentral; left exposed server with tooling and target lists
- **Russian and Chinese State-Sponsored Groups**: Multiple threat groups abusing Anthropic's Claude AI to extract secrets from 1.8M Android apps
- **OpenAI Agent Swarm**: Autonomous AI agents orchestrated the May 2026 RubyGems supply chain attack achieving RCE on RubyDoc servers
- **Government Impersonation Actor**: Social-engineered Revolut employee into disclosing customer financial and passport data