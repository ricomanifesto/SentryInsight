# Exploitation Report

## Executive Summary

Multiple critical exploitation activities are underway across diverse attack surfaces, from supply chain compromises and kernel privilege escalations to targeted phishing campaigns by nation-state actors. A public proof-of-concept for CVE-2026-55200 in libssh2 enables malicious SSH servers to achieve remote code execution on connecting clients, while two separate Linux kernel vulnerabilities—CVE-2026-46331 ("pedit COW") and the newly disclosed "DirtyClone" flaw—provide reliable local privilege escalation to root with working exploits publicly available. CISA has added an actively exploited PTC Windchill RCE to its Known Exploited Vulnerabilities catalog and set an urgent patching deadline for a Cisco Unified Communications Manager flaw under active attack.

Simultaneously, supply chain attacks have intensified across package ecosystems and development tools. Threat actors have compromised 119 Microsoft Edge extensions using steganography to hide payloads in images and fonts, hijacked npm and Go packages to deliver Python infostealers via VS Code Tasks, and injected malicious scripts into Polymarket's frontend through a third-party vendor breach resulting in $3 million in losses. The Miasma malware family continues evolving its supply chain campaign targeting npm packages and GitHub Actions. These incidents demonstrate persistent risks in software supply chains and developer tooling.

Nation-state activity remains prominent, with Russian intelligence services conducting multi-faceted campaigns including fake support texts to steal messaging credentials in Ukraine, an evolving phishing operation targeting Signal users that now seeks Backup Recovery Keys for full account takeover, and a photo-themed ZIP phishing campaign deploying Node.js implants targeting hospitality organizations across Europe and Asia. A Chinese-speaking APT deploys the novel TinyRCT backdoor against Southeast Asian government and critical infrastructure targets, while the StrikeShark campaign utilizes the new SharkLoader to deploy Cobalt Strike Beacons. These operations highlight continued espionage and credential theft objectives by sophisticated adversaries.

## Active Exploitation Details

### libssh2 Client-Side SSH Flaw (CVE-2026-55200)
- **Description**: A critical memory corruption vulnerability in libssh2 that allows a malicious or compromised SSH server to trigger memory corruption on a connecting client. The flaw resides in the client-side implementation and can be triggered during the SSH handshake or session establishment.
- **Impact**: Attackers controlling or compromising an SSH server can achieve remote code execution on any vulnerable client that connects to it, completely reversing the typical trust model where clients trust servers.
- **Status**: Public proof-of-concept exploit has been released. The vulnerability affects libssh2 versions prior to the patched release. Organizations using libssh2-based SSH clients should update immediately.
- **CVE ID**: CVE-2026-55200

### Linux Kernel pedit COW Privilege Escalation (CVE-2026-46331)
- **Description**: An out-of-bounds write vulnerability in the Linux kernel's traffic-control subsystem, specifically in the packet editing (pedit) code. The flaw leverages copy-on-write (COW) mechanisms to corrupt kernel memory.
- **Impact**: A local unprivileged user can escalate privileges to root on affected systems. The exploit works by poisoning cached binaries through the traffic control packet editing interface.
- **Status**: Working exploit publicly available. Nicknamed "pedit COW," this vulnerability affects Linux kernel versions with the vulnerable traffic-control subsystem code. Patches are available in upstream kernels and downstream distributions.
- **CVE ID**: CVE-2026-46331

### Linux Kernel DirtyClone Privilege Escalation
- **Description**: A new privilege escalation vulnerability in the Linux kernel belonging to the "DirtyFrag" family. The flaw involves improper handling of cloned packets in the networking stack, allowing local users to manipulate kernel memory.
- **Impact**: Local unprivileged users can gain root access on vulnerable systems. JFrog Security Research published a complete exploit walkthrough on June 25, 2026, representing the first public demonstration of this technique.
- **Status**: Working exploit publicly demonstrated. The vulnerability affects Linux kernel versions containing the flawed packet cloning logic. Distribution patches are expected rapidly given the public exploit availability.

### PTC Windchill Remote Code Execution
- **Description**: A critical remote code execution vulnerability affecting PTC Windchill PDMlink and PTC FlexPLM enterprise Product Data Management (PDM) and Product Lifecycle Management (PLM) solutions. The flaw allows unauthenticated attackers to execute arbitrary code on the server.
- **Impact**: Attackers can achieve full system compromise, deploy web shells for persistent access, and potentially pivot to connected engineering and manufacturing systems. Active web shell deployment campaigns are ongoing.
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog, confirming active exploitation in the wild. PTC has released security updates. Organizations using Windchill PDMlink or FlexPLM must prioritize patching immediately.

### Cisco Unified Communications Manager Server Vulnerability
- **Description**: A vulnerability in Cisco Unified Communications Manager Server that is being actively exploited in attacks. Specific technical details were not disclosed in the advisory.
- **Impact**: Successful exploitation could allow attackers to compromise the communications infrastructure, potentially enabling call interception, voicemail access, and lateral movement within corporate networks.
- **Status**: CISA has issued an urgent directive giving federal agencies until Sunday to apply patches. The active exploitation status indicates weaponized exploits are in circulation. Cisco has released security updates.

### Amazon Q Developer MCP Configuration Flaw
- **Description**: A high-severity vulnerability in Amazon Q Developer that allows a malicious repository to execute commands and steal developer cloud credentials through Model Context Protocol (MCP) configurations. The attack triggers when a developer opens the repository, trusts the workspace, and the malicious MCP config is processed.
- **Impact**: Attackers can achieve arbitrary command execution in the developer's environment and exfiltrate cloud credentials, potentially leading to broader cloud infrastructure compromise.
- **Status**: Vulnerability disclosed with technical details. Amazon has likely issued or is preparing a fix. Developers using Amazon Q Developer should exercise caution with untrusted repositories and review MCP configurations.

## Affected Systems and Products

- **Microsoft Edge Browser Extensions**: 119 malicious extensions removed from the Edge Add-ons store. Affected versions include any Edge browser with these extensions installed. Extensions hid malware payloads in image and font files using steganography, activating days after installation to steal credentials.
- **libssh2 Library**: All versions prior to the patched release containing the fix for CVE-2026-55200. Affected platforms include any SSH client application linked against vulnerable libssh2 versions across Linux, Windows, macOS, and embedded systems.
- **Linux Kernel**: Versions containing the vulnerable traffic-control subsystem (pedit COW, CVE-2026-46331) and packet cloning logic (DirtyClone). Affected platforms include all Linux distributions, containers, Android devices, and embedded Linux systems running unpatched kernels.
- **Cisco Unified Communications Manager Server**: Specific vulnerable versions identified in Cisco's security advisory. Platform includes on-premises and virtualized deployments of Cisco's call control and collaboration suite.
- **PTC Windchill PDMlink and FlexPLM**: Enterprise PDM/PLM versions prior to the security update. Affected platforms include on-premises and cloud-hosted deployments used in manufacturing, aerospace, defense, and high-tech industries.
- **npm and Go Package Ecosystems**: Multiple hijacked packages identified in both ecosystems. Affected platforms include any development environment or CI/CD pipeline that installed compromised packages. The Python infostealer payload targets Windows, Linux, and macOS.
- **Visual Studio Code**: VS Code Tasks feature abused by malicious packages to achieve code execution. Affected versions include VS Code installations where users opened projects containing malicious task configurations.
- **Amazon Q Developer**: Versions prior to the security fix. Affected platforms include AWS Cloud9, VS Code with Amazon Q extension, JetBrains IDEs with Amazon Q plugin, and command-line interfaces.
- **Signal Messenger**: All platforms (iOS, Android, Desktop) where users can be phished for Backup Recovery Keys. The vulnerability is in the account recovery design, not the Signal protocol itself.
- **Polymarket Platform**: Frontend compromised via third-party vendor breach. Affected users include anyone who interacted with the platform during the injection window.
- **KDDI Corporation Email Systems**: Email infrastructure used by KDDI and five other Japanese ISPs. Approximately 14.2 million email login credentials exposed.
- **Hotel and Hospitality Systems**: Property management, booking, and guest services systems in Europe and Asia targeted by photo-themed ZIP phishing delivering Node.js implants.

## Attack Vectors and Techniques

- **Steganographic Payload Delivery in Browser Extensions**: Malicious Edge extensions concealed executable payloads within benign-appearing image and font files. The malware remained dormant for days post-installation to evade initial scanning, then extracted and executed the hidden payload to steal browser credentials, cookies, and session tokens.
- **Supply Chain Compromise via Package Managers**: Attackers gained control of legitimate npm and Go packages (likely through credential theft or maintainer account compromise) and published malicious versions containing Python-based information stealers. The packages abused VS Code Tasks configurations to achieve automatic code execution when developers opened the project.
- **AI Coding Agent Manipulation**: Seemingly clean GitHub repositories crafted to exploit agentic coding tools (e.g., GitHub Copilot, Cursor, Devin). The repositories contain malicious payloads invisible to static analysis, security scanners, and human code review, but executed when AI agents clone and set up the project.
- **SSH Client-Side Exploitation via Malicious Server**: CVE-2026-55200 reverses the typical SSH trust model—a compromised or attacker-controlled SSH server exploits a memory corruption flaw in the connecting libssh2-based client during protocol negotiation, achieving RCE on the client machine.
- **Linux Kernel Privilege Escalation via Networking Subsystem Flaws**: Two distinct techniques: (1) pedit COW exploits an out-of-bounds write in the traffic-control packet editor using copy-on-write semantics to corrupt kernel memory; (2) DirtyClone manipulates packet cloning logic in the network stack to achieve similar kernel memory corruption. Both provide reliable local-to-root escalation.
- **Web Shell Deployment on Enterprise Applications**: Attackers exploiting the PTC Windchill RCE deploy web shells for persistent remote access, enabling data exfiltration, lateral movement, and long-term foothold in engineering and manufacturing environments.
- **Phishing with Fake Support Communications**: Russian intelligence services send SMS/text messages impersonating legitimate support channels (e.g., Microsoft, Google, Telegram support) to trick targets into providing messaging application credentials. The campaign uses social engineering rather than technical exploits.
- **Signal Backup Recovery Key Phishing**: Evolution of Signal phishing where attackers, after obtaining the primary registration code via phishing, now coax victims into providing their Signal Backup Recovery Key. This allows full message history restoration on attacker-controlled devices, bypassing Signal's forward secrecy for historical messages.
- **Themed ZIP Archive Phishing with Node.js Implants**: Photo-themed ZIP attachments targeting hospitality sector employees. Archives contain malicious Node.js applications disguised as image viewers or documents. Upon execution, the implant establishes persistence, harvests credentials, and conducts network reconnaissance.
- **Third-Party Vendor Compromise for Supply Chain Injection**: Attackers breached a third-party vendor to inject malicious JavaScript into Polymarket's frontend, enabling cryptocurrency wallet draining. The script executed in users' browsers during legitimate platform interaction.
- **MCP Configuration Abuse in AI Development Tools**: Malicious Model Context Protocol configurations in repositories exploit Amazon Q Developer's trust model. When a developer opens the repository and trusts the workspace, the MCP config instructs the AI assistant to execute arbitrary commands and exfiltrate credentials.
- **Forensic Tool Exploitation of Mobile Devices**: Russian authorities used Cellebrite UFED forensic software to extract data from a locked iPhone belonging to an opposition activist, demonstrating continued effectiveness of commercial forensic tools against mobile device encryption even after vendor sales restrictions.

## Threat Actor Activities

- **Russian Intelligence Services (GRU/FSB-linked)**: Conducting multiple parallel campaigns: (1) Long-running fake support text campaign uncovered by Ukraine's SSU and FBI targeting messaging credentials in Ukraine; (2) Evolving Signal phishing operation now targeting Backup Recovery Keys for full account takeover, warned by FBI and CISA; (3) Photo ZIP phishing campaign since April 2026 targeting European and Asian hospitality organizations with Node.js implants, attributed by Microsoft. These operations demonstrate coordinated credential theft and espionage objectives across messaging platforms and sector-specific targets.
- **Chinese-Speaking APT Actor**: Deploying the novel TinyRCT backdoor in a campaign targeting government entities and critical infrastructure in Southeast Asia. TinyRCT represents a new custom implant family, indicating dedicated malware development resources. The targeting profile aligns with regional strategic intelligence collection.
- **StrikeShark Campaign Operators**: Utilizing the previously undocumented SharkLoader malware family as a dedicated loader for Cobalt Strike Beacon deployment. The campaign represents a new intrusion set with custom tooling, suggesting either a new threat group or existing actor adopting fresh infrastructure and payloads.
- **Miasma/Mini Shai-Hulud/Hades Supply Chain Operators**: Continuing evolution of a persistent npm supply chain campaign. The operators compromise package maintainer accounts or publish typo-squatted packages, now extending to GitHub Actions workflow compromise. The malware family shows modular design with infostealer and persistence capabilities across Windows, Linux, and macOS.
- **Polymarket Supply Chain Attackers**: Unknown threat actors who compromised a third-party vendor to inject malicious frontend code into the Polymarket prediction market platform, draining approximately $3 million in user funds before detection. The attack demonstrates financial motivation and sophisticated supply chain access.
- **OpenAI Impersonation Actors**: Threat actors creating fraudulent OpenAI organization tenants that mimic legitimate cybersecurity companies, then inviting employees to join. The objective appears to be harvesting sensitive corporate information, API keys, or credentials through social engineering rather than technical exploitation.
- **Unknown Operators - Edge Extension Campaign**: Operators behind the 119 malicious Edge extensions using steganography. The campaign's longevity and scale (119 extensions) suggest organized operation with dedicated infrastructure for extension publishing, payload hosting, and credential exfiltration.
- **Unknown Operators - Hijacked npm/Go Packages**: Actors responsible for compromising legitimate package maintainer accounts or publishing supply chain attacks in both ecosystems simultaneously. The use of VS Code Tasks for payload delivery indicates familiarity with developer workflows and IDE attack surfaces.

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
