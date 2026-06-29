# Exploitation Report

## Executive Summary

A significant surge in active exploitation activity has been observed across multiple vectors, with two critical vulnerabilities now possessing public proof-of-concept exploits. The Linux kernel privilege escalation flaw CVE-2026-46331 ("pedit COW") and the libssh2 client-side memory corruption vulnerability CVE-2026-55200 both have working exploit code publicly available, dramatically lowering the barrier for attackers. Simultaneously, CISA has added a critical PTC Windchill RCE flaw to its Known Exploited Vulnerabilities catalog while mandating urgent patching of an actively exploited Cisco Unified Communications Manager vulnerability.

Supply chain attacks continue to escalate in sophistication and impact. A malicious operation spanning 119 Microsoft Edge extensions hid payloads in image and font files to steal credentials, while hijacked npm and Go packages now leverage VS Code Tasks to deploy cross-platform Python infostealers. The Miasma malware family—linked to the Mini Shai-Hulud and Hades campaigns—has compromised additional npm packages and GitHub Actions. A third-party vendor breach at Polymarket resulted in $3 million in customer losses through malicious script injection.

Nation-state activity remains intense, with Russian intelligence services (tracked as APT29/Cozy Bear) evolving their phishing campaigns to target Signal Backup Recovery Keys after initial credential theft. Ukrainian and U.S. intelligence jointly exposed a long-running operation using fake support texts to compromise messaging accounts. A Chinese-speaking APT has deployed the novel TinyRCT backdoor against government entities and critical infrastructure across Southeast Asia. Meanwhile, the StrikeShark campaign utilizes the new SharkLoader malware to deliver Cobalt Strike Beacons, and a photo-themed phishing campaign with Node.js implants targets hospitality organizations across Europe and Asia.

## Active Exploitation Details

### Linux Kernel pedit COW Privilege Escalation (CVE-2026-46331)
- **Description**: An out-of-bounds write vulnerability in the Linux kernel's traffic-control subsystem packet classifier (cls_api.c) that allows manipulation of the packet editing (pedit) action through copy-on-write mechanisms. The flaw enables a local unprivileged user to corrupt kernel memory by poisoning cached binaries.
- **Impact**: Local privilege escalation to root on affected Linux systems. A working exploit has been publicly demonstrated, making this immediately weaponizable by any local user.
- **Status**: Public exploit available as of June 25, 2026. Actively exploitable on vulnerable kernel versions.
- **CVE ID**: CVE-2026-46331

### libssh2 Client-Side SSH Memory Corruption (CVE-2026-55200)
- **Description**: A critical flaw in the libssh2 library that allows a malicious or compromised SSH server to trigger memory corruption on a connecting client during the key exchange process. The vulnerability stems from improper validation of server-supplied data.
- **Impact**: Remote code execution on the client machine when connecting to a malicious SSH server. Affects all applications using libssh2 for SSH client functionality.
- **Status**: Public proof-of-concept exploit released. No patch information provided in source articles.
- **CVE ID**: CVE-2026-55200

### PTC Windchill Remote Code Execution
- **Description**: A critical remote code execution vulnerability affecting PTC Windchill PDMlink and PTC FlexPLM enterprise Product Data Management solutions. The flaw allows unauthenticated attackers to execute arbitrary code on the server.
- **Impact**: Full system compromise of Windchill servers, enabling data theft, persistence, and lateral movement within enterprise networks. Web shell deployment observed in active attacks.
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog. Active web shell attacks continuing. Patches available from vendor.
- **CVE ID**: [Not provided in source article]

### Cisco Unified Communications Manager Server Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager Server that is being actively exploited in the wild. Specific technical details not disclosed in source article.
- **Impact**: Potential unauthorized access, command execution, or service disruption on affected Cisco UC Manager deployments.
- **Status**: Actively exploited. CISA has issued an urgent directive (BOD 22-01) requiring federal agencies to patch by Sunday (June 29, 2026 deadline).
- **CVE ID**: [Not provided in source article]

### DirtyClone Linux Kernel Privilege Escalation
- **Description**: A new Linux kernel privilege escalation vulnerability in the DirtyFrag family that allows local users to gain root access through cloned packet manipulation. JFrog Security Research published a working exploit walkthrough.
- **Impact**: Local privilege escalation to root on affected Linux systems.
- **Status**: Public exploit walkthrough published June 25, 2026. Actively exploitable.
- **CVE ID**: [Not provided in source article]

### Amazon Q Developer MCP Configuration Flaw
- **Description**: A high-severity flaw in Amazon Q Developer that allows a malicious repository to execute commands and steal developer cloud credentials through Model Context Protocol (MCP) configurations when a developer opens and trusts the workspace.
- **Impact**: Arbitrary command execution and cloud credential theft in developer environments using malicious repository contexts.
- **Status**: Active vulnerability. No patch information provided in source article.
- **CVE ID**: [Not provided in source article]

## Affected Systems and Products

- **Linux Kernel**: Versions with traffic-control subsystem (cls_api.c) packet classifier pedit action vulnerable to CVE-2026-46331; additional versions affected by DirtyClone privilege escalation
- **libssh2 Library**: All versions prior to patched release; affects any application using libssh2 for SSH client connections (including Git, curl, and numerous DevOps tools)
- **PTC Windchill PDMlink and FlexPLM**: Enterprise Product Data Management solutions; specific vulnerable versions not detailed in source
- **Cisco Unified Communications Manager Server**: Affected versions not specified in source; federal agencies mandated to patch urgently
- **Microsoft Edge Extensions Platform**: 119 malicious extensions removed from Edge Add-ons store; users who installed affected extensions
- **npm and Go Package Ecosystems**: Hijacked packages distributing Python infostealers across Windows, Linux, and macOS
- **GitHub Actions and npm Registry**: Targeted by Miasma/Mini Shai-Hulud/Hades malware family supply chain attacks
- **Amazon Q Developer**: AWS AI coding assistant; vulnerable to MCP configuration exploitation
- **Signal Messenger**: Backup Recovery Keys targeted in phishing campaigns; all platforms
- **Polymarket Platform**: Frontend compromised via third-party vendor breach; cryptocurrency prediction market users affected

## Attack Vectors and Techniques

- **Steganographic Payload Delivery**: Malicious Edge extensions hiding executable payloads inside ordinary image and font files, with delayed activation days after installation to evade detection
- **Supply Chain Compromise via Package Managers**: Hijacked npm and Go packages leveraging VS Code Tasks functionality to automatically execute Python-based infostealers upon project opening
- **AI Agent Subversion**: Clean-appearing GitHub repositories crafted to exploit agentic coding tools, causing AI agents to execute malicious payloads invisible to scanners and human review
- **Phishing with Signal Backup Recovery Key Theft**: Evolution of credential phishing to specifically request Signal Backup Recovery Keys, enabling full message history access on new devices
- **Fake Support Social Engineering**: Russian intelligence using spoofed support text messages to trick targets into surrendering messaging application credentials
- **Web Shell Deployment**: Persistent post-exploitation access on compromised PTC Windchill servers through web shell implants
- **Node.js Implant Delivery**: Photo-themed ZIP files containing malicious Node.js implants targeting hospitality sector via phishing emails
- **Third-Party Vendor Breach for Script Injection**: Compromise of a vendor to inject malicious JavaScript into Polymarket's frontend, draining customer funds
- **Fraudulent SaaS Organization Invites**: Creation of impersonated OpenAI organization tenants to social engineer employees into joining and exposing sensitive data
- **Local Kernel Exploitation via Traffic Control**: Manipulation of Linux kernel packet classifier (cls_api) through crafted network traffic rules to achieve root via CVE-2026-46331 and DirtyClone
- **Malicious SSH Server Client Exploitation**: Compromised or attacker-controlled SSH servers exploiting libssh2 clients during connection establishment (CVE-2026-55200)
- **IDE/Editor Feature Abuse**: Exploitation of VS Code Tasks and Amazon Q Developer MCP configurations to achieve code execution in development environments
- **Cobalt Strike Beacon Deployment via Custom Loaders**: SharkLoader malware family used to deploy Cobalt Strike Beacons in StrikeShark campaign operations

## Threat Actor Activities

- **Russian Intelligence Services (APT29/Cozy Bear)**: Conducting evolved phishing campaigns targeting Signal users, now specifically harvesting Backup Recovery Keys to access full message histories. Joint FBI/CISA advisory issued. Previously exposed by Ukraine SSU and FBI for long-running fake support text campaign stealing messaging credentials. Used Cellebrite UFED forensic tools on activist iPhone in 2021.
- **Chinese-Speaking APT**: Deploying novel TinyRCT custom backdoor in campaigns targeting government entities and critical infrastructure across Southeast Asia. Attribution to Chinese-speaking operators based on tooling and infrastructure.
- **StrikeShark Campaign Operators**: Utilizing previously undocumented SharkLoader malware family to deliver Cobalt Strike Beacons. Active cyber attack campaign with custom loader development.
- **Miasma/Mini Shai-Hulud/Hades Supply Chain Actors**: Evolving supply chain attack campaign compromising npm packages and GitHub Actions. Continuous malware family development targeting software supply chain.
- **Edge Extension Malware Operators**: Long-running operation distributing 119 malicious extensions via Microsoft Edge Add-ons store, using steganography in images/fonts for credential theft.
- **Polymarket Attackers**: Unknown threat actors who breached a third-party vendor to inject malicious scripts into Polymarket frontend, stealing approximately $3 million in customer funds.
- **Fraudulent OpenAI Invitation Actors**: Unknown operators creating impersonated OpenAI organization tenants targeting cybersecurity firms for sensitive information harvesting.
- **Hotel/ Hospitality Phishing Campaign**: Active since April 2026, targeting organizations across Europe and Asia with photo-themed ZIP lures delivering Node.js implants. Attribution not specified in source.

## Source Attribution

- **Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts**: The Hacker News - https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html
- **Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw**: The Hacker News - https://thehackernews.com/2026/06/public-poc-released-for-critical.html
- **Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer**: The Hacker News - https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html
- **Data breach exposes up to 14.2 million email logins at six ISPs**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/data-breach-exposes-up-to-142-million-email-logins-at-six-isps/
- **Ukraine Says Russian Intelligence Used Fake Support Texts to Steal Messaging Credentials**: The Hacker News - https://thehackernews.com/2026/06/ukraine-says-russian-intelligence-used.html
- **Clean GitHub repo tricks AI coding agents into running malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/clean-github-repo-tricks-ai-coding-agents-into-running-malware/
- **OpenAI Previews GPT-5.6 Sol With Restricted Access and Stronger Cyber Safeguards**: The Hacker News - https://thehackernews.com/2026/06/openai-limits-gpt-56-rollout-as-sol.html
- **Third-Party Breaches Teach Education Sector a Costly Lesson in Vendor Risk**: Dark Reading - https://www.darkreading.com/cyber-risk/third-party-breaches-teaches-education-lesson-vendor-risk
- **FBI: Russian hackers now target Signal backup recovery keys**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fbi-russian-hackers-now-target-signal-backup-recovery-keys/
- **CISA sets urgent deadline to fix Cisco flaw exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-sets-urgent-deadline-to-fix-cisco-flaw-exploited-in-attacks/
- **FBI Warns Russian Intelligence Hackers Target Signal Backup Recovery Keys**: The Hacker News - https://thehackernews.com/2026/06/fbi-warns-russian-intelligence-hackers.html
- **AI Decline? Confidence in Autonomous Penetration Testing Falls**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/ai-decline-confidence-autonomous-penetration-testing
- **New SharkLoader Malware Deploys Cobalt Strike in StrikeShark Cyberattacks**: The Hacker News - https://thehackernews.com/2026/06/new-sharkloader-malware-deploys-cobalt.html
- **Polymarket customers lose $3 million in supply-chain attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/polymarket-customers-lose-3-million-in-supply-chain-attack/
- **Cybersecurity firms targeted by fraudulent OpenAI organization invites**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cybersecurity-firms-targeted-by-fraudulent-openai-organization-invites/
- **Cisco Adds NHI to Security Stack With Astrix, WideField Acquisitions**: Dark Reading - https://www.darkreading.com/identity-access-management-security/cisco-adds-nhi-security-stack-with-astrix-widefield
- **New Initiative Tackles Security for End-of-Life Open Source Software**: Dark Reading - https://www.darkreading.com/application-security/initiative-tackles-security-end-of-life-open-source
- **Chinese-Speaking APT Deploys New TinyRCT Backdoor in Southeast Asia Campaign**: The Hacker News - https://thehackernews.com/2026/06/chinese-speaking-apt-deploys-new.html
- **AI Won't Wipe-Out Entry-Level Cybersecurity Jobs**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/ai-wont-wipe-out-entry-level-cybersecurity-jobs
- **Your First GRC Agent: A Red Teamer's Walkthrough**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/your-first-grc-agent-a-red-teamers-walkthrough/
- **New Linux pedit COW Exploit Enables Root Access by Poisoning Cached Binaries**: The Hacker News - https://thehackernews.com/2026/06/new-linux-pedit-cow-exploit-enables.html
- **Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs**: The Hacker News - https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html
- **Meeting Trump's 2030 Quantum Deadline Will be Expensive, Complex**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/meeting-2030-quantum-deadline-expensive-complex
- **Thanks for Crushing the Submissions Inbox. We're Trying to Keep Up**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/submissions-guidelines-reminder
- **CISA Adds Exploited PTC Windchill RCE Flaw to KEV as Web Shell Attacks Continue**: The Hacker News - https://thehackernews.com/2026/06/cisa-adds-exploited-ptc-windchill-rce.html
- **New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets**: The Hacker News - https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html
- **Guardian Agents: The Next Layer of Identity Governance**: The Hacker News - https://thehackernews.com/2026/06/guardian-agents-next-layer-of-identity.html
- **Miasma Malware Targets npm Packages and GitHub Actions in Supply Chain Attack**: The Hacker News - https://thehackernews.com/2026/06/miasma-malware-targets-npm-packages-and.html
- **Microsoft Warns of Photo ZIP Phishing Campaign Targeting Hotels with Node.js Implant**: The Hacker News - https://thehackernews.com/2026/06/microsoft-warns-of-photo-zip-phishing.html
- **Russia Used Cellebrite on Jailed Activist's iPhone Months After Sales Cutoff**: The Hacker News - https://thehackernews.com/2026/06/russia-used-cellebrite-on-jailed.html
