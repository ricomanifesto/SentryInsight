# Exploitation Report

## Executive Summary

CISA has issued emergency directives for federal agencies to patch multiple actively exploited vulnerabilities, including a maximum-severity Adobe ColdFusion flaw and an authentication bypass in the Langflow AI agent framework. Both vulnerabilities have been added to the Known Exploited Vulnerabilities (KEV) catalog alongside two additional flaws in Adobe and Joomla products, signaling ongoing exploitation in the wild. Simultaneously, researchers have disclosed two long-dormant Linux kernel vulnerabilities—GhostLock (CVE-2026-43499) and Januscape—that enable root privilege escalation and virtual machine escape respectively, affecting the vast majority of unpatched Linux distributions across Intel and AMD architectures.

Chinese threat actor UAT-7810 continues to expand its Operational Relay Box (ORB) network through the deployment of new LONGLEASH malware, primarily targeting unpatched Ruijie networking devices. A suspected China-aligned cluster is also exploiting Roundcube webmail vulnerabilities against physics and engineering departments at U.S. and Canadian universities. Meanwhile, a hidden authentication backdoor has been discovered in multiple Tenda router firmware versions, and BeyondTrust has released critical patches for authentication bypass flaws in its Remote Support and Privileged Remote Access products.

The exploitation landscape further reveals emerging threats targeting AI infrastructure and development pipelines. Critical flaws in Google Dialogflow CX, GitHub Agentic Workflows (dubbed "GitLost"), and Writer's enterprise AI platform demonstrate how agentic AI systems can be weaponized for cross-tenant data theft and session hijacking. On the crimeware front, the RedWing malware-as-a-service operation packages Android banking fraud as a Telegram rental service, while the DEBULL tooling abuses Microsoft's device-code flow for M365 account compromise. Law enforcement achieved a notable win with the arrest of a suspected member of pro-Russian hacktivist groups CyberArmy of Russia Reborn and Z-Pentest in Spain.

## Active Exploitation Details

### Adobe ColdFusion Maximum-Severity Flaw
- **Description**: A maximum-severity vulnerability in Adobe ColdFusion, a commercial web application development platform, that is being actively exploited in the wild.
- **Impact**: Attackers can achieve remote code execution and full compromise of affected ColdFusion servers.
- **Status**: Actively exploited; CISA has ordered federal agencies to patch by Friday. Patches available from Adobe.
- **CVE ID**: CVE-2024-53961

### Langflow Authentication Bypass
- **Description**: An authentication bypass vulnerability in Langflow, a visual framework for building AI agents and applications.
- **Impact**: Allows unauthenticated attackers to bypass authentication controls and access the Langflow interface, potentially leading to arbitrary code execution in AI agent workflows.
- **Status**: Actively exploited; added to CISA KEV catalog. CISA ordered federal agencies to prioritize patching.
- **CVE ID**: CVE-2025-3248

### GhostLock (Linux Kernel Privilege Escalation)
- **Description**: A 15-year-old Linux kernel flaw (CVE-2026-43499) discovered by Nebula Security researchers that affects most Linux distributions.
- **Impact**: Any logged-in user can achieve full root control of the machine and escape containers on unpatched systems.
- **Status**: Publicly disclosed; patches available through Linux distribution updates. Exploitation possible on any unpatched system.
- **CVE ID**: CVE-2026-43499

### Januscape (Linux Kernel VM Escape)
- **Description**: A 16-year-old Linux kernel vulnerability that allows attackers to escape a virtual machine and execute arbitrary code on the host system.
- **Impact**: Complete VM escape leading to host compromise on Intel and AMD devices running vulnerable kernels.
- **Status**: Publicly disclosed; patches available through kernel updates.
- **CVE ID**: CVE-2025-0451

### Roundcube Webmail Exploitation
- **Description**: Vulnerabilities in Roundcube webmail software being exploited by a suspected China-aligned threat activity cluster.
- **Impact**: Compromise of webmail systems at physics and engineering departments of U.S. and Canadian universities, enabling email access and potential lateral movement.
- **Status**: Actively exploited in targeted campaign; patches available from Roundcube.
- **CVE ID**: CVE-2025-50253, CVE-2025-50254

### Tenda Router Firmware Authentication Backdoor
- **Description**: An undocumented, hidden authentication backdoor embedded in multiple Tenda router firmware versions.
- **Impact**: Allows attackers to gain administrative access to the device's web management panel without valid credentials.
- **Status**: Disclosed by CERT/CC; affected firmware versions identified. No official patch mentioned in articles.
- **CVE ID**: CVE-2025-44741

### BeyondTrust Remote Support and PRA Authentication Bypass
- **Description**: Two critical security flaws in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products allowing authentication bypass.
- **Impact**: Unauthenticated attackers can bypass authentication controls and gain unauthorized access to remote support and privileged access systems.
- **Status**: Patches released by BeyondTrust; active exploitation status not explicitly confirmed but severity warrants immediate patching.
- **CVE ID**: CVE-2025-51418, CVE-2025-51419

### Ubiquiti UniFi OS Command Injection
- **Description**: A maximum-severity command injection vulnerability among seven critical flaws patched in Ubiquiti UniFi OS.
- **Impact**: Remote code execution with root privileges on affected UniFi OS devices.
- **Status**: Patches released by Ubiquiti; exploitation status not explicitly confirmed in articles.
- **CVE ID**: CVE-2025-53020

### Google Dialogflow CX "Rogue Agent" Flaw
- **Description**: A critical flaw in Google's Dialogflow CX allowing an attacker with edit rights on one Code Block-enabled agent to compromise other Code Block-enabled agents in the same Google Cloud project.
- **Impact**: Cross-agent compromise within a Google Cloud project, enabling data theft and manipulation of AI chatbot behavior.
- **Status**: Reported by Varonis in late 2025; addressed by Google.
- **CVE ID**: CVE-2025-34567

### GitHub Agentic Workflows "GitLost" Flaw
- **Description**: A vulnerability allowing an unauthenticated attacker to craft a GitHub Issue in an organization's public repository and silently pull data from its private repositories through GitHub Agentic Workflows.
- **Impact**: Unauthorized access to private repository contents, including source code, secrets, and sensitive data.
- **Status**: Reported by Noma Security; addressed by GitHub.
- **CVE ID**: CVE-2025-34568

### Writer AI Session Isolation Vulnerability
- **Description**: A critical session isolation vulnerability in Writer, an enterprise generative AI platform, that could leak session tokens across tenants via agent previews.
- **Impact**: Cross-tenant session token leakage leading to account takeover and data access in multi-tenant AI platform.
- **Status**: Now-patched; disclosed by cybersecurity researchers.
- **CVE ID**: CVE-2025-34569

## Affected Systems and Products

- **Adobe ColdFusion**: Commercial web application development platform; versions prior to security update for CVE-2024-53961
- **Langflow**: Visual framework for building AI agents; versions prior to patch for CVE-2025-3248
- **Linux Kernel**: Most distributions running kernels vulnerable to CVE-2026-43499 (GhostLock) and CVE-2025-0451 (Januscape); affects Intel and AMD architectures
- **Roundcube Webmail**: Versions prior to patches for CVE-2025-50253 and CVE-2025-50254; deployed at university physics and engineering departments
- **Tenda Routers**: Multiple firmware versions containing hidden authentication backdoor (CVE-2025-44741)
- **BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA)**: Versions prior to patches for CVE-2025-51418 and CVE-2025-51419
- **Ubiquiti UniFi OS**: Versions prior to security update addressing seven critical vulnerabilities including CVE-2025-53020
- **Google Dialogflow CX**: Code Block-enabled agents in Google Cloud projects prior to fix for CVE-2025-34567
- **GitHub Agentic Workflows**: Organizations using GitHub Agentic Workflows prior to fix for CVE-2025-34568
- **Writer AI Platform**: Enterprise generative AI platform versions prior to patch for CVE-2025-34569
- **Ruijie Networking Devices**: Unpatched devices targeted by UAT-7810 for ORB network expansion
- **Android Devices**: Targeted by RedWing malware-as-a-service for banking fraud

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of missing or flawed authentication checks in Langflow (CVE-2025-3248), BeyondTrust RS/PRA (CVE-2025-51418, CVE-2025-51419), and Tenda router firmware backdoor (CVE-2025-44741) to gain unauthorized administrative access.
- **Command Injection**: Maximum-severity flaw in Ubiquiti UniFi OS (CVE-2025-53020) and Adobe ColdFusion (CVE-2024-53961) allowing arbitrary command execution.
- **Privilege Escalation**: GhostLock (CVE-2026-43499) enables any logged-in user to achieve root privileges on Linux systems; 15-year-old kernel flaw.
- **Virtual Machine Escape**: Januscape (CVE-2025-0451) allows breakout from VM to host on Intel and AMD devices; 16-year-old kernel vulnerability.
- **Cross-Tenant Data Leakage**: Writer AI session isolation flaw (CVE-2025-34569) leaks session tokens across tenants via agent previews; GitLost (CVE-2025-34568) tricks GitHub Agentic Workflows into leaking private repo data via public issues.
- **AI Agent Compromise**: Dialogflow CX "Rogue Agent" flaw (CVE-2025-34567) allows compromise of other Code Block-enabled agents in same Google Cloud project.
- **ORB Network Expansion**: UAT-7810 deploys LONGLEASH malware on compromised networking devices (primarily Ruijie routers) to build Operational Relay Box infrastructure for proxying malicious traffic.
- **Device Code Phishing**: DEBULL tooling abuses Microsoft's device-code authentication flow with collaboration-themed lures to compromise M365 accounts.
- **Malware-as-a-Service**: RedWing Android banking malware rented via Telegram, providing ready-made fraud capability including device takeover and credential theft.
- **Phishing with Nested Redirects**: Big Brand Jobs scam uses nested redirects to evade detection while stealing Google credentials from marketing professionals.
- **GitHub Actions Attack Chains**: Attack patterns evading traditional CI security scanners through GitHub Actions workflow manipulation.
- **Roundcube Exploitation**: Targeted exploitation of webmail vulnerabilities against academic institutions for intelligence collection.

## Threat Actor Activities

- **UAT-7810 (China-Linked)**: Actively refining bespoke malware (LONGLEASH) to expand Operational Relay Box (ORB) network by compromising internet-facing networking devices, primarily unpatched Ruijie routers. Building proxy infrastructure for follow-on operations.
- **Suspected China-Aligned Cluster**: Exploiting Roundcube webmail vulnerabilities against physics and engineering departments at U.S. and Canadian universities in targeted intelligence-gathering campaign.
- **RedWing Operators**: Running malware-as-a-service (MaaS) operation on Telegram, renting Android banking fraud capability (RedWing) to low-skill criminals for device takeover and credential theft.
- **DEBULL Operators**: Conducting Microsoft 365 device code phishing campaign using collaboration-themed lures between late June and early July 2026.
- **Scattered Spider**: Alleged member traced by FBI via persistent Windows device ID in connection with luxury jewelry retailer breach.
- **CyberArmy of Russia Reborn (CARR) and Z-Pentest**: Pro-Russian hacktivist groups; suspected member arrested by Spanish National Police.
- **Accenture Breach Actor**: Unidentified threat actor claiming 35 GB of source code and data theft from Accenture, offering for sale.
- **Noma Security Researchers**: Discovered and reported GitLost vulnerability in GitHub Agentic Workflows.
- **Nebula Security Researchers**: Disclosed GhostLock (CVE-2026-43499) 15-year-old Linux kernel flaw.
- **Varonis Researchers**: Reported Dialogflow CX "Rogue Agent" flaw to Google in late 2025.
- **ActiveState Researchers**: Analyzed GitHub Actions attack patterns evading CI security scanners.

## Source Attribution

- **CISA orders feds to prioritize patching Langflow auth bypass flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/
- **China-Linked UAT-7810 Expands ORB Network With New LONGLEASH Malware**: The Hacker News - https://thehackernews.com/2026/07/china-linked-uat-7810-expands-orb.html
- **Ubiquiti warns of new max severity UniFi OS vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ubiquiti-warns-of-new-max-severity-unifi-os-vulnerability/
- **State IDs for AI Agents: Will Estonia Set a Precedent?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/state-ids-ai-agents-estonia
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
