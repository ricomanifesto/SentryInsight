# Exploitation Report

## Executive Summary

Multiple critical exploitation campaigns are actively underway across diverse technology stacks, from network infrastructure and virtualization layers to AI platforms and collaboration tools. Chinese state-aligned actors are leveraging the LONGLEASH malware to expand Operational Relay Box networks through unpatched routing devices, while a suspected China-aligned cluster exploits Roundcube webmail flaws against university physics and engineering departments. Iranian MOIS-affiliated operators have deployed the novel Cavern C2 framework against Israeli organizations, and the Armored Likho group has infiltrated critical infrastructure networks across Russia, Brazil, and Kazakhstan with the BusySnake infostealer.

Simultaneously, supply chain and platform vulnerabilities are enabling widespread credential theft and data exposure. A hidden authentication backdoor in Tenda router firmware grants administrative access across multiple versions, prompting CERT/CC warnings. The 16-year-old Januscape Linux KVM flaw (CVE-2025-) permits VM escape on Intel and AMD systems. GitHub's Agentic Workflows contain the GitLost flaw allowing unauthenticated private repository data extraction via crafted public issues. BeyondTrust has patched critical authentication bypass flaws in Remote Support and Privileged Remote Access products, while Google addressed the Rogue Agent vulnerability in Dialogflow CX and Writer patched a cross-tenant session token leak.

Phishing operations continue evolving in sophistication. The DEBULL campaign abuses Microsoft's device-code flow with collaboration-themed lures to compromise M365 accounts. A massive brand-impersonation campaign targeting marketing professionals uses nested redirects across 30+ brands including Adobe, Netflix, and OpenAI. Threat actors are weaponizing Microsoft Teams voice calls to deliver EtherRAT malware via fake IT support impersonation. The RedWing Android banking malware is now offered as a Telegram-hosted MaaS rental, lowering the barrier for financial fraud.

## Active Exploitation Details

### Tenda Router Firmware Hidden Authentication Backdoor
- **Description**: An undocumented authentication backdoor embedded in multiple Tenda router firmware versions that enables administrative access to the device's web management panel without legitimate credentials.
- **Impact**: Attackers gain full administrative control over affected routers, enabling network traffic interception, configuration modification, and potential lateral movement into connected networks.
- **Status**: Actively exploitable; CERT/CC has issued warnings. No patch information provided in sources.
- **CVE ID**: Not explicitly provided in articles

### Januscape Linux KVM Virtual Machine Escape
- **Description**: A 16-year-old use-after-free vulnerability in Linux's KVM hypervisor that can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel, enabling VM escape and arbitrary code execution on the host.
- **Impact**: Guest VMs can break isolation and execute code on the underlying host system, compromising all workloads on the hypervisor across Intel and AMD x86 platforms.
- **Status**: Vulnerability disclosed and tracked; patch status not specified in articles.
- **CVE ID**: CVE-2025- (tracked as CVE-2025- per The Hacker News)

### GitLost GitHub Agentic Workflows Data Leakage
- **Description**: A flaw in GitHub's Agentic Workflows that allows an unauthenticated attacker to craft a GitHub Issue in an organization's public repository and silently extract data from private repositories within the same organization.
- **Impact**: Unauthorized access to proprietary source code, secrets, and sensitive data stored in private repositories without authentication or direct repository access.
- **Status**: Disclosed by Noma Security researchers; GitHub remediation status not specified.
- **CVE ID**: Not explicitly provided in articles

### Rogue Agent Google Dialogflow CX Cross-Agent Compromise
- **Description**: A critical flaw in Google's Dialogflow CX platform where an attacker with edit rights on one Code Block-enabled agent can compromise other Code Block-enabled agents within the same Google Cloud project.
- **Impact**: Lateral movement across AI agents, potential data theft from connected agents, and manipulation of conversational AI workflows.
- **Status**: Reported by Varonis in late 2025; Google has addressed the vulnerability.
- **CVE ID**: Not explicitly provided in articles

### Writer AI Cross-Tenant Session Token Leakage
- **Description**: A critical session isolation vulnerability in Writer's enterprise generative AI platform that allowed agent previews to leak session tokens across tenant boundaries.
- **Impact**: Unauthorized access to other tenants' sessions, potential data exposure, and privilege escalation within the AI platform.
- **Status**: Now-patched; researchers disclosed details after fix deployment.
- **CVE ID**: Not explicitly provided in articles

### BeyondTrust Remote Support and Privileged Remote Access Authentication Bypass
- **Description**: Two critical security flaws in BeyondTrust's Remote Support (RS) and Privileged Remote Access (PRA) software that allow unauthenticated attackers to bypass authentication mechanisms.
- **Impact**: Complete authentication bypass enabling unauthorized administrative access to remote support and privileged access infrastructure.
- **Status**: BeyondTrust has released updates addressing both flaws; active exploitation risk for unpatched instances.
- **CVE ID**: Not explicitly provided in articles

### Roundcube Webmail Exploitation Campaign
- **Description**: Active exploitation of vulnerabilities in Roundcube webmail software targeting physics and engineering departments at U.S. and Canadian universities.
- **Impact**: Compromise of academic email systems, potential access to research data, credential harvesting, and foothold establishment in university networks.
- **Status**: Actively exploited by suspected China-aligned threat actors; patch status of targeted instances unclear.
- **CVE ID**: Not explicitly provided in articles

### Citrix NetScaler Memory Disclosure Under Attack
- **Description**: Attackers rapidly targeting a memory disclosure flaw in Citrix NetScaler products following public proof-of-concept exploit publication, reminiscent of the CitrixBleed vulnerability pattern.
- **Impact**: Memory leakage potentially exposing session tokens, credentials, and sensitive application data from NetScaler appliances.
- **Status**: Active exploitation observed shortly after PoC release; patch availability referenced but not detailed.
- **CVE ID**: Not explicitly provided in articles

## Affected Systems and Products

- **Tenda Routers**: Multiple firmware versions across various router models containing undocumented administrative backdoor
- **Linux Kernel KVM Hypervisor**: Versions spanning approximately 16 years affecting Intel and AMD x86 virtualization hosts
- **GitHub Agentic Workflows**: GitHub's AI-powered workflow automation system used by organizations with public and private repositories
- **Google Dialogflow CX**: Enterprise conversational AI platform with Code Block-enabled agents in Google Cloud projects
- **Writer Enterprise AI Platform**: Generative AI platform used by enterprises for content generation with multi-tenant architecture
- **BeyondTrust Remote Support (RS)**: Remote support software used for IT assistance and system administration
- **BeyondTrust Privileged Remote Access (PRA)**: Privileged access management solution for secure remote administration
- **Roundcube Webmail**: Open-source webmail software deployed by university physics and engineering departments
- **Citrix NetScaler (ADC)**: Application delivery controller and load balancing appliances exposed to internet
- **Microsoft 365 / Entra ID**: Cloud identity and productivity platform targeted via device code authentication flow
- **Android Devices**: Mobile devices targeted by RedWing banking malware distributed via Telegram MaaS
- **Microsoft Teams**: Collaboration platform abused for voice call-based social engineering delivering EtherRAT
- **Google Accounts**: Consumer and enterprise Google accounts targeted via brand-impersonation phishing

## Attack Vectors and Techniques

- **Authentication Backdoor Exploitation**: Leveraging hardcoded/undocumented credentials in firmware to gain administrative device access
- **Virtual Machine Escape**: Triggering use-after-free in KVM hypervisor shadow page handling from guest VM to achieve host code execution
- **Supply Chain Workflow Poisoning**: Crafting malicious public GitHub Issues to manipulate Agentic Workflows into exfiltrating private repository data
- **AI Agent Cross-Contamination**: Exploiting insufficient isolation between Code Block-enabled agents in shared Google Cloud projects
- **Session Token Leakage Across Tenants**: Abusing preview functionality in multi-tenant AI platforms to harvest authenticated sessions
- **Authentication Bypass in Privileged Access Tools**: Exploiting logic flaws in remote support software to circumvent authentication entirely
- **Webmail Software Exploitation**: Targeting known vulnerabilities in Roundcube installations at high-value academic targets
- **Rapid PoC Weaponization**: Converting published NetScaler memory disclosure proof-of-concept into active exploitation campaigns within hours
- **Device Code Phishing (DEBULL)**: Abusing Microsoft's device authorization flow with collaboration-themed lures to capture M365 tokens
- **Multi-Brand Impersonation with Nested Redirects**: Phishing campaign rotating 30+ brand identities (Adobe, Netflix, Coca-Cola, OpenAI) using redirect chains to evade detection
- **Voice Call Social Engineering (Vishing)**: Impersonating IT support via Microsoft Teams voice calls to deliver EtherRAT malware
- **Malware-as-a-Service Distribution**: Renting Android banking trojan (RedWing) via Telegram channels with ready-to-use fraud infrastructure
- **Operational Relay Box Network Expansion**: Compromising unpatched internet-facing networking devices to build proxy infrastructure (LONGLEASH)
- **Modular C2 Framework Deployment**: Using novel Cavern C2 framework for flexible command-and-control against Israeli targets
- **Infostealer Deployment in Critical Infrastructure**: Placing BusySnake in government and electrical power networks for credential and data theft
- **Windows Device ID Forensics**: Law enforcement leveraging persistent Windows device identifiers to attribute Scattered Spider intrusions

## Threat Actor Activities

- **UAT-7810 (Chinese State-Aligned)**: Actively evolving LONGLEASH malware to expand Operational Relay Box network by compromising unpatched internet-facing networking devices, primarily routers
- **Suspected China-Aligned Cluster**: Exploiting Roundcube webmail vulnerabilities against physics and engineering departments at U.S. and Canadian universities for intelligence collection
- **MOIS-Affiliated Iranian Actors (Ministry of Intelligence and Security)**: Deploying novel Cavern modular C2 framework in targeted operations against Israeli organizations
- **Armored Likho**: Infiltrating government agencies and electrical power entities across Russia, Brazil, and Kazakhstan with BusySnake infostealer for credential harvesting and network mapping
- **Scattered Spider (ALPHV/BlackCat Affiliates)**: Conducting high-profile intrusions including luxury jewelry retailer breach; members identified via Windows device ID forensics
- **CyberArmy of Russia Reborn (CARR) & Z-Pentest**: Pro-Russian hacktivist groups with members subject to international law enforcement action (Spain arrest)
- **DEBULL Operators**: Running device code phishing campaign against M365 accounts using collaboration-themed lures during late June–early July 2026
- **RedWing MaaS Operators**: Operating Android banking fraud service on Telegram, providing turnkey phone takeover and credential theft capabilities to low-skill criminals
- **EtherRAT Operators**: Conducting vishing campaigns via Microsoft Teams impersonating corporate IT support to establish initial access footholds
- **Accenture Breach Actor**: Unidentified threat actor claiming 35 GB source code and data theft from Accenture, offering for sale on underground markets
- **GitLost/Noma Security Researchers**: Discovered and disclosed GitHub Agentic Workflows vulnerability enabling cross-repository data leakage

## Source Attribution

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
- **Fake IT support calls on Microsoft Teams push EtherRAT malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fake-it-support-calls-on-microsoft-teams-push-etherrat-malware/
- **Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations**: The Hacker News - https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html
- **Vietnam arrests suspects behind HiAnime anime piracy service**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/vietnam-arrests-suspects-behind-hianime-anime-piracy-service/
- **16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems**: The Hacker News - https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html
