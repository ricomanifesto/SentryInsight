# Exploitation Report

## Executive Summary

Critical exploitation activity spans multiple vectors this reporting period, from kernel-level vulnerabilities enabling full system compromise to targeted campaigns against enterprise infrastructure and AI platforms. A 15-year-old Linux kernel flaw dubbed GhostLock (CVE-2026-43499) grants any logged-in user root access and container escape capabilities across most unpatched distributions, while a separate 16-year-old vulnerability named Januscape enables virtual machine escape on Intel and AMD hardware. CISA has mandated emergency patching for an actively exploited maximum-severity Adobe ColdFusion flaw and added four actively exploited vulnerabilities in Adobe, Joomla, and Langflow to its Known Exploited Vulnerabilities catalog.

Simultaneously, threat actors are leveraging infrastructure compromises and novel phishing techniques at scale. Chinese-aligned operators tracked as UAT-7810 are expanding their Operational Relay Box network through the LONGLEASH malware, targeting unpatched networking devices, while a separate China-aligned cluster exploits Roundcube webmail servers at U.S. and Canadian universities. The DEBULL campaign abuses Microsoft's device-code flow to compromise M365 accounts via collaboration-themed lures, and a large-scale phishing operation impersonates over 30 major brands in fake job interviews to steal Google credentials from marketing professionals. Critical authentication bypass flaws in BeyondTrust remote access software, a hidden backdoor in Tenda router firmware, and session isolation failures in Google Dialogflow CX and Writer AI platforms further expand the attack surface.

## Active Exploitation Details

### GhostLock (CVE-2026-43499)
- **Description**: A 15-year-old Linux kernel vulnerability that allows any logged-in user to escalate privileges to root and escape container isolation on most unpatched Linux distributions.
- **Impact**: Full root control of the host system and container escape, enabling compromise of all workloads on affected machines.
- **Status**: Actively exploitable on unpatched systems; patches available from distribution maintainers.
- **CVE ID**: CVE-2026-43499

### Januscape Linux Kernel Flaw
- **Description**: A 16-year-old Linux kernel vulnerability that enables virtual machine escape, allowing attackers to execute arbitrary code on the host from within a guest VM.
- **Impact**: Complete VM escape and host code execution on Intel and AMD platforms, breaking fundamental virtualization isolation.
- **Status**: Proof-of-concept exploitation demonstrated; patches under development by kernel maintainers.

### Adobe ColdFusion Maximum-Severity Flaw
- **Description**: An actively exploited critical vulnerability in Adobe ColdFusion web application development platform.
- **Impact**: Remote code execution and full server compromise; CISA has ordered all federal civilian agencies to patch by emergency directive.
- **Status**: Actively exploited in the wild; emergency patching mandated for U.S. federal systems.

### CISA KEV Additions: Adobe, Joomla, and Langflow Flaws
- **Description**: Four security flaws added to CISA's Known Exploited Vulnerabilities catalog with evidence of active exploitation.
- **Impact**: Varies by component; includes remote code execution and authentication bypass in widely deployed web platforms.
- **Status**: Actively exploited; immediate patching required per CISA binding operational directive.

### BeyondTrust Remote Support and PRA Authentication Bypass
- **Description**: Two critical security flaws in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) software allowing unauthenticated attackers to bypass authentication controls.
- **Impact**: Full administrative access to remote management consoles, enabling lateral movement and privileged access across managed environments.
- **Status**: Patches released; active exploitation reported prior to remediation.

### Tenda Router Firmware Hidden Backdoor
- **Description**: An undocumented authentication backdoor embedded in multiple Tenda router firmware versions granting administrative access to the web management panel.
- **Impact**: Complete device takeover, traffic interception, and network pivoting capabilities for any attacker aware of the backdoor.
- **Status**: No vendor patch reported; CERT/CC has issued warning; mitigation requires firmware replacement or device isolation.

### Dialogflow CX "Rogue Agent" Flaw
- **Description**: A critical vulnerability in Google's Dialogflow CX platform allowing an attacker with edit rights on one Code Block-enabled agent to compromise other Code Block-enabled agents within the same Google Cloud project.
- **Impact**: Cross-agent data theft and manipulation within multi-tenant AI chatbot deployments.
- **Status**: Reported to Google in late 2025; addressed in platform updates.

### Writer AI Session Isolation Vulnerability
- **Description**: A critical session isolation flaw in Writer's enterprise generative AI platform that could leak session tokens across tenant boundaries via agent preview functionality.
- **Impact**: Unauthorized access to other tenants' AI sessions and potential data exposure in multi-tenant deployments.
- **Status**: Now patched; disclosed by cybersecurity researchers.

### GitHub Agentic Workflows "GitLost" Flaw
- **Description**: A vulnerability allowing unauthenticated attackers to craft a GitHub Issue in a public repository and exfiltrate data from private repositories within the same organization via GitHub Agentic Workflows.
- **Impact**: Private source code, secrets, and proprietary data leakage from organizations using GitHub's agentic automation features.
- **Status**: Demonstrated by Noma Security researchers; mitigation guidance available.

### Citrix NetScaler Memory Disclosure Flaw
- **Description**: A memory disclosure vulnerability in Citrix NetScaler (formerly Citrix ADC) products) ADC and Gateway products actively targeted after proof-of-concept exploit publication.
- **Impact**: Sensitive memory contents exposure including session tokens and encryption keys; potential chaining for further compromise.
- **Status**: Actively exploited post-PoC; patches available from Citrix.

## Affected Systems and Products

- **Ubiquiti UniFi OS**: Seven critical vulnerabilities including maximum-severity command injection; all UniFi OS versions prior to security update.
- **Adobe ColdFusion**: Commercial web application development platform; all unpatched versions subject to CISA emergency directive.
- **Linux Kernel (GhostLock)**: Most Linux distributions with kernels dating back 15 years; affects container runtimes and host systems.
- **Linux Kernel (Januscape)**: Intel and AMD virtualization hosts running vulnerable kernel versions spanning 16 years.
- **BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA)**: All versions prior to July 2026 security updates.
- **Tenda Router Firmware**: Multiple firmware versions across various Tenda router models; specific versions identified in CERT/CC advisory.
- **Google Dialogflow CX**: Code Block-enabled agents in Google Cloud projects; addressed in late 2025 platform updates.
- **Writer AI Platform**: Enterprise generative AI platform deployments; patched in recent platform version.
- **GitHub Agentic Workflows**: Organizations using GitHub's agentic automation features with public and private repository mixes.
- **Citrix NetScaler ADC and Gateway**: Versions affected by latest memory disclosure flaw; actively exploited post-PoC.
- **Roundcube Webmail**: Deployments at U.S. and Canadian university physics and engineering departments; specific versions under active exploitation.
- **Microsoft 365 Device Code Flow**: All tenants using device authentication flow; targeted by DEBULL phishing campaign.

## Attack Vectors and Techniques

- **Kernel Privilege Escalation via Legacy Flaws**: Exploitation of long-dormant Linux kernel vulnerabilities (GhostLock, Januscape) that bypass modern mitigations due to their presence in core memory management and virtualization subsystems.
- **Authentication Bypass in Privileged Access Management**: Direct exploitation of logic flaws in BeyondTrust RS/PRA to circumvent authentication without credentials, granting immediate administrative console access.
- **Firmware-Level Persistent Backdoors**: Undocumented manufacturer backdoors in Tenda router firmware providing persistent administrative access surviving reboots and configuration changes.
- **AI Platform Cross-Tenant Isolation Failures**: Exploitation of insufficient boundary controls in Dialogflow CX and Writer AI platforms allowing lateral movement between tenant resources via shared agent/preview functionality.
- **Supply Chain Compromise via Agentic Workflows**: Manipulation of GitHub Actions and Agentic Workflows through crafted public issues to exfiltrate private repository data, bypassing traditional CI/CD security scanners.
- **Operational Relay Box (ORB) Network Expansion**: Compromise of internet-facing networking devices (primarily unpatched routers) to build layered proxy infrastructure obscuring true attacker origin.
- **Device Code Phishing (DEBULL)**: Abuse of Microsoft's legitimate device authorization flow (RFC 8628) using collaboration-themed lures to trick users into authorizing attacker-controlled device sessions.
- **Brand Impersonation Phishing at Scale**: Multi-brand (30+ organizations including Adobe, Netflix, Coca-Cola, OpenAI) fake job interview campaigns using nested redirects to evade detection and harvest Google credentials.
- **Webmail Exploitation for Intelligence Collection**: Targeted exploitation of Roundcube installations at academic institutions to access communications of physics and engineering researchers.
- **Memory Disclosure Chaining**: Rapid weaponization of Citrix NetScaler memory disclosure PoC to extract session material for follow-on authentication bypass and lateral movement.

## Threat Actor Activities

- **UAT-7810 (Chinese-aligned)**: Actively evolving LONGLEASH malware to expand Operational Relay Box network by compromising unpatched internet-facing networking devices; infrastructure-focused operations enabling further targeting.
- **China-Aligned Threat Activity Cluster (Roundcube)**: Exploiting Roundcube webmail vulnerabilities against physics and engineering departments at U.S. and Canadian universities; likely intelligence collection targeting academic research.
- **Armored Likho**: Deploying "BusySnake" infostealer against government agencies and electrical power entities in Russia, Brazil, and Kazakhstan; critical infrastructure targeting for credential theft and network reconnaissance.
- **DEBULL Campaign Operators**: Conducting Microsoft 365 device code phishing between late June and early July 2026 using collaboration-themed lures; focused on M365 account takeover for business email compromise and data access.
- **Big Brand Jobs Scam Operators**: Running large-scale phishing campaign impersonating 30+ major brands in fake job interviews targeting marketing professionals' Google accounts; financially motivated credential harvesting.
- **Scattered Spider (ALLEGED)**: Linked via Windows device ID forensics to luxury jewelry retailer breach; demonstrates persistent device identifiers as attribution evidence in federal prosecution.
- **CyberArmy of Russia Reborn (CARR) / Z-Pentest**: Pro-Russian hacktivist groups; Spanish authorities arrested suspected active member, indicating ongoing disruptive operations.
- **Accenture Breach Actor**: Unnamed threat actor claiming 35 GB source code and data theft from Accenture; attempting to monetize via data sale on underground markets.

## Source Attribution

- **Ubiquiti warns of new max severity UniFi OS vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ubiquiti-warns-of-new-max-severity-unifi-os-vulnerability/
- **CISA orders feds to patch max severity ColdFusion flaw by Friday**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-coldfusion-flaw-by-friday/
- **15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros**: The Hacker News - https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html
- **CISA Adds 4 Actively Exploited Adobe, Joomla, and Langflow Flaws to KEV**: The Hacker News - https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html
- **Accenture confirms breach after hacker offers stolen data for sale**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/accenture-confirms-breach-after-hacker-offers-stolen-data-for-sale/
- **Big Brand Jobs Scam Targets Marketing Pros' Google Accounts**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/big-brand-jobs-scam-marketing-pros-google-accounts
- **Dialogflow CX 'Rogue Agent' Flaw Enabled AI Chatbot Data Theft**: Dark Reading - https://www.darkreading.com/application-security/dialogflow-cx-rogue-agent-flaw-enabled-ai-chatbot-data-theft
- **Chinese hackers develop LONGLEASH malware to expand ORB network**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/chinese-hackers-develop-longleash-malware-to-expand-orb-network/
- **Hidden backdoor in Tenda router firmware grants admin access**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hidden-backdoor-in-tenda-router-firmware-grants-admin-access/
- **RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service**: The Hacker News - https://thehackernews.com/2026/07/redwing-maas-packages-android-bank.html
- **Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots**: The Hacker News - https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html
- **'GitLost' Flaw Leaks Private Data From GitHub's Agentic Workflows**: Dark Reading - https://www.darkreading.com/cyber-risk/gitlost-leaks-private-data-github-agentic-workflows
- **Spain arrests suspected member of pro-Russian hacktivist groups**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/spain-arrests-suspected-member-of-pro-russian-hacktivist-groups/
- **DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts**: The Hacker News - https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html
- **Public GitHub Issue Could Trick GitHub Agentic Workflows Into Leaking Private Repo Data**: The Hacker News - https://thehackernews.com/2026/07/public-github-issue-could-trick-github.html
- **The GitHub Actions Attack Pattern Your CI Security Scanners Miss**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-github-actions-attack-pattern-your-ci-security-scanners-miss/
- **Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker**: The Hacker News - https://thehackernews.com/2026/07/court-filing-reveals-windows-device-id.html
- **Writer AI Flaw Could Let Agent Previews Leak Session Tokens Across Tenants**: The Hacker News - https://thehackernews.com/2026/07/writer-ai-flaw-could-let-agent-previews.html
- **Webinar tomorrow: Why modern email attacks require a new approach to defense**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/webinar-tomorrow-why-modern-email-attacks-require-a-new-approach-to-defense/
- **New Januscape Linux flaw allows VM escape on Intel, AMD devices**: Bleeping Computer - https://www.bleepingcomputer.com/news/linux/new-januscape-linux-kernel-flaw-allows-vm-escape-on-intel-amd-devices/
- **What Changes When Your Software Supply Chain Includes AI Writing Your Code?**: The Hacker News - https://thehackernews.com/2026/07/what-changes-when-your-software-supply.html
- **Microsoft to enable Windows settings backup by default for orgs**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-to-enable-windows-backup-for-organizations-by-default/
- **Suspected China-Aligned Hackers Exploit Roundcube Flaws Against Universities**: The Hacker News - https://thehackernews.com/2026/07/suspected-china-aligned-hackers-exploit.html
- **BeyondTrust warns of critical flaws in remote access software**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/beyondtrust-warns-of-critical-flaws-in-remote-access-software/
- **Microsoft testing new Cloud Rebuild Windows 11 recovery feature**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-testing-new-cloud-rebuild-windows-11-recovery-feature/
- **CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware**: The Hacker News - https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html
- **BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA**: The Hacker News - https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html
- **'BusySnake' Infostealer Slithers Into Critical Infrastructure Networks**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/busysnake-infostealer-critical-infrastructure-networks
- **CitrixBleed-ing Again? NetScaler Vulnerability Under Attack**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/citrixbleed-ing-again-netscaler-vulnerability-under-attack
- **Phishing poses as big-brand job interview to steal Google accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/phishing-poses-as-big-brand-job-interview-to-steal-google-accounts/
