# Exploitation Report

## Executive Summary

Microsoft's August 2026 Patch Tuesday addressed a staggering 400 vulnerabilities, including three zero-day flaws—one confirmed as actively exploited in the wild and two publicly disclosed. This massive update cycle underscores the accelerating pace of vulnerability discovery and exploitation across the Microsoft ecosystem. Simultaneously, CISA confirmed that ransomware operators have begun leveraging a high-severity Microsoft SharePoint remote code execution vulnerability in active campaigns since early July, with researchers separately disclosing an AI-assisted exploit chain achieving unauthenticated RCE against SharePoint servers.

Nation-state threat activity remains intense and diversified. The Sandworm-linked group UAC-0145 is conducting social engineering campaigns against Ukrainian IT workers using fake job interviews to deliver a malicious VPN client capable of arbitrary command execution. Gunra ransomware, attributed to North Korean actors, is exploiting Fortinet and Schneider Electric vulnerabilities to breach critical infrastructure globally, prompting joint warnings from U.S. and South Korean authorities. In a striking OT incident, attackers accessed a Polish power plant's control systems via a private cellular network (APN), shutting down a steam turbine and water treatment systems—demonstrating the growing risk to industrial control systems from compromised dedicated network links.

Supply chain attacks and novel AI-driven threat vectors are emerging as critical concerns. A compromise of WordPress plugin vendor BdThemes allowed threat actors to poison a remote JSON feed, creating rogue administrator accounts across an unknown number of victim sites. Researchers demonstrated that malicious MCP servers can exfiltrate secrets from AI coding agents through instruction splitting, while malicious SIM cards can execute attacker code on cellular IoT modems in EV chargers and industrial routers. DDoS attacks exceeding 1 Tbps surged fivefold in Q2 2026, with Cloudflare mitigating over 800 such events, signaling a dramatic escalation in volumetric attack capacity.

## Active Exploitation Details

### Microsoft SharePoint Remote Code Execution (Ransomware Exploitation)
- **Description**: A high-severity remote code execution vulnerability in Microsoft SharePoint that allows unauthenticated attackers to execute arbitrary code on affected servers. Researchers separately disclosed an AI-assisted exploit chain achieving unauthenticated RCE with administrative privileges.
- **Impact**: Full server compromise, administrative access, ransomware deployment, lateral movement within organizational networks
- **Status**: Actively exploited in ransomware attacks since early July 2026 per CISA confirmation; Microsoft August 2026 Patch Tuesday includes fixes for 400 flaws including zero-days
- **CVE ID**: Not explicitly provided in source articles

### Gunra Ransomware Exploitation of Fortinet and Schneider Electric Flaws
- **Description**: Gunra ransomware operators are exploiting vulnerabilities in Fortinet and Schneider Electric products to gain initial access to critical infrastructure networks worldwide.
- **Impact**: Network breach, ransomware deployment, critical infrastructure disruption, data exfiltration
- **Status**: Actively exploited in the wild; joint advisory issued by U.S. federal agencies and South Korea's National Police Agency
- **CVE ID**: Not explicitly provided in source articles

### Microsoft August 2026 Patch Tuesday Zero-Days
- **Description**: Three zero-day vulnerabilities addressed in Microsoft's August 2026 Patch Tuesday release, including one actively exploited in the wild and two publicly disclosed prior to patch availability.
- **Impact**: Varies by vulnerability; includes potential for remote code execution, privilege escalation, and security feature bypass
- **Status**: Patched in August 2026 cumulative updates (KB5121003, KB5120240 for Windows 11; KB5120249 for Windows 10); one actively exploited, two publicly disclosed
- **CVE ID**: Not explicitly provided in source articles

### Cisco Secure Endpoint Connector ClamAV Vulnerabilities
- **Description**: Two high-severity vulnerabilities in the ClamAV scanning engine used by Cisco Secure Endpoint Connector that allow denial-of-service attacks via crafted files.
- **Impact**: ClamAV scanning process crash, denial of service, potential bypass of malware scanning capabilities
- **Status**: Public exploits available; Cisco has issued warnings and mitigations
- **CVE ID**: Not explicitly provided in source articles

### Metabase SQL Zero-Day
- **Description**: A maximum-severity zero-day vulnerability in Metabase business analytics platform allowing remote unauthenticated administrative access. No CVE has been assigned yet.
- **Impact**: Full administrative access to Metabase instances, downstream user compromise, data exposure
- **Status**: Actively exploited in the wild; no patch available at time of reporting; no CVE assigned
- **CVE ID**: Not explicitly provided in source articles (no CVE assigned)

### Windows 11 USB Auto-Install SYSTEM Takeover
- **Description**: Researchers demonstrated a full SYSTEM privilege escalation on fully updated Windows 11 by abusing Windows Plug and Play to fetch signed vendor software for an emulated USB device and executing privileged installation components.
- **Impact**: Full SYSTEM-level compromise, bypass of security controls, persistence
- **Status**: Proof-of-concept demonstrated; affects fully updated Windows 11; no patch mentioned in source articles
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **Microsoft SharePoint**: On-premises and cloud deployments; exploited for unauthenticated RCE in ransomware campaigns since early July 2026
- **Microsoft Windows 10 (21H2, 22H2)**: Extended Security Updates via KB5120249 addressing 400+ vulnerabilities including zero-days
- **Microsoft Windows 11 (23H2, 24H2, 25H2)**: Cumulative updates KB5121003 and KB5120240 addressing security vulnerabilities and zero-days
- **Fortinet Products**: Specific products not detailed in source articles; exploited by Gunra ransomware for initial access
- **Schneider Electric Products**: Specific products not detailed in source articles; exploited by Gunra ransomware for initial access
- **Cisco Secure Endpoint Connector**: ClamAV scanning engine vulnerabilities with public exploits causing DoS
- **Metabase Business Analytics Platform**: All versions vulnerable to unauthenticated remote admin access via SQL zero-day
- **BdThemes WordPress Plugins**: Premium web-design tools; supply chain compromise of JSON feed delivery infrastructure
- **Cellular IoT Modems**: Modems in EV chargers, industrial routers, car telematics units vulnerable to malicious SIM card command execution
- **Polish Power Plant OT Systems**: Steam turbine and process-water treatment controls accessible via private cellular network (APN)
- **Mozilla Firefox and Thunderbird (Linux)**: GPG signing key revoked after exposure in private repository
- **AI Coding Agents with MCP Integration**: Vulnerable to instruction-splitting attacks from malicious MCP servers exfiltrating SSH keys, secrets, source code

## Attack Vectors and Techniques

- **Social Engineering via Fake Job Interviews**: UAC-0145 (Sandworm-linked) targets IT workers with fraudulent employment offers delivering malicious VPN clients with command execution capabilities
- **Wi-Fi Deauthentication Attacks**: Unauthorized Wi-Fi network deployed on commercial flight targeting DEF CON attendees; forces device disconnection for potential credential harvesting or MitM
- **Supply Chain Compromise (JSON Poisoning)**: BdThemes infrastructure compromised to modify remote JSON feed delivered to WordPress admin panels, creating rogue administrator accounts
- **Private Cellular Network (APN) Intrusion**: Attackers accessed Polish energy plant OT network via dedicated private APN, shutting down turbine and water treatment systems
- **AI-Assisted Vulnerability Research & Exploit Development**: Researchers used AI to discover SharePoint exploit chain; OpenAI released GPT-5.6-Cyber with reduced safeguards for exploit development
- **Malicious MCP Server Instruction Splitting**: Malicious Model Context Protocol servers split instructions across benign-appearing requests to exfiltrate secrets from AI coding agents without triggering safety controls
- **Malicious SIM Card Command Injection**: Specially crafted SIM cards execute attacker commands on baseband processors of cellular IoT devices (EV chargers, industrial routers, telematics)
- **USB Device Emulation for Privilege Escalation**: Windows Plug and Play abused to emulate USB devices, fetch signed vendor installers, and chain privileged installation components for SYSTEM access
- **Decentralized Ransomware Infrastructure**: DeadLock ransomware uses Polygon blockchain smart contracts for victim communications and data leak operations, increasing operational resilience
- **Volumetric DDoS (>1 Tbps)**: Cloudflare mitigated 800+ attacks exceeding 1 Tbps in Q2 2026, a fivefold increase; targeting network-layer infrastructure
- **Internet-Exposed PLC Targeting**: Water system attacks across multiple U.S. states targeting ill-secured, internet-accessible programmable logic controllers
- **GhostJacking AI Agent Hijacking**: Attackers manipulate security alerts and blocked events to hijack AI agent identities and permissions
- **North Korean IT Worker Infiltration**: Suspected DPRK operatives hired through fake cryptocurrency startup; virtual machine monitoring revealed malicious activity patterns

## Threat Actor Activities

- **UAC-0145 (Sandworm-Linked)**: Russian nation-state group conducting social engineering campaign against Ukrainian IT workers via fake job interviews delivering malicious VPN software with arbitrary command execution capability; disclosed by CERT-UA
- **Gunra Ransomware (North Korea-Linked)**: Exploiting Fortinet and Schneider Electric vulnerabilities to breach government and critical infrastructure networks globally; joint warning from U.S. federal agencies and South Korea's National Police Agency
- **DeadLock Ransomware Group**: Utilizing Polygon blockchain smart contracts for decentralized victim communication and data leak infrastructure to resist takedown efforts
- **ExfilSquad**: Claimed data theft from Wesco (global supply chain/distribution giant); Wesco confirmed investigating cybersecurity incident
- **Iran-Linked Actors (Suspected)**: Targeting water systems across a dozen U.S. states via internet-exposed PLCs; attacks widening per Dark Reading reporting
- **North Korean IT Worker Operations**: Suspected DPRK operatives infiltrated a researcher-created fake cryptocurrency startup; three hires identified through VM monitoring and behavioral analysis
- **Unknown Actors (Polish Power Plant)**: Breached combined heat and power plant via private cellular network (APN), shutting down steam turbine and process-water treatment; occurred in 2025 per Bleeping Computer
- **Ransomware Affiliates (SharePoint)**: Multiple ransomware gangs now exploiting SharePoint RCE vulnerability since early July 2026 per CISA confirmation

## Source Attribution

- **Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands**: The Hacker News - https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html
- **Delta probes Wi-Fi deauth attack on flight carrying DEF CON attendees**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/delta-probes-wi-fi-deauth-attack-on-flight-carrying-def-con-attendees/
- **Microsoft releases Windows 10 KB5120249 extended security update**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5120249-cumulative-update-released-with-fixes/
- **Microsoft August 2026 Patch Tuesday fixes 400 flaws, 3 zero-days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-august-2026-patch-tuesday-fixes-400-flaws-3-zero-days/
- **Windows 11 KB5121003 \& KB5120240 cumulative updates released**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5121003-and-kb5120240-cumulative-updates-released/
- **Researchers Disclose AI-Assisted SharePoint Exploit Chain Reaching Unauthenticated RCE**: The Hacker News - https://thehackernews.com/2026/08/researchers-disclose-ai-assisted.html
- **DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt**: The Hacker News - https://thehackernews.com/2026/08/deadlock-ransomware-uses-polygon-smart.html
- **Wesco confirms security incident after ExfilSquad claims data theft**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/
- **Mozilla updates GPG signing key for Firefox releases after exposure**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/mozilla-updates-gpg-key-for-signing-firefox-thunderbird-releases-after-exposure/
- **Vague Task, Total Access: When AI Delegation Becomes a Security Risk**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/vague-task-total-access-when-ai-delegation-becomes-a-security-risk/
- **OpenAI Launches GPT-5.6-Cyber with Reduced Safeguards for Exploit Development**: The Hacker News - https://thehackernews.com/2026/08/openai-launches-gpt-56-cyber-with.html
- **DDoS attacks over 1 Tbps surged fivefold in the second quarter**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ddos-attacks-over-1-tbps-surged-fivefold-in-the-second-quarter/
- **CISA: Microsoft SharePoint flaw now exploited in ransomware attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-flaw-now-exploited-in-ransomware-attacks/
- **A Malicious SIM Card Can Run Attacker Code Inside the Modems Behind Cellular IoT Devices**: The Hacker News - https://thehackernews.com/2026/08/a-malicious-sim-card-can-run-attacker.html
- **Mozilla Revokes Firefox and Thunderbird Linux Signing Key After Key Lands in Private Repo**: The Hacker News - https://thehackernews.com/2026/08/mozilla-revokes-firefox-and-thunderbird.html
- **Researchers Built a Fake Crypto Startup and Hired Three Suspected North Korean IT Workers**: The Hacker News - https://thehackernews.com/2026/08/researchers-built-fake-crypto-startup.html
- **Cisco warns of high-severity ClamAV flaws with public exploits**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-warns-of-high-severity-clamav-flaws-with-public-exploits/
- **Researchers Turn USB Auto-Install Into a Full SYSTEM Takeover on Windows 11**: The Hacker News - https://thehackernews.com/2026/08/researchers-turn-usb-auto-install-into.html
- **Malicious MCP Servers Can Split Instructions to Make AI Coding Agents Exfiltrate Secrets**: The Hacker News - https://thehackernews.com/2026/08/malicious-mcp-servers-can-split.html
- **US and South Korea warn of Gunra ransomware targeting govt agencies**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-warns-of-gunra-ransomware-attacks-against-government-critical-infrastructure/
- **Gunra Ransomware Exploits Fortinet and Schneider Electric Flaws to Breach Networks**: The Hacker News - https://thehackernews.com/2026/08/gunra-ransomware-exploits-fortinet-and.html
- **Hackers Breach Polish Power Plant Controls via Private Cellular Network and Shut Turbine**: The Hacker News - https://thehackernews.com/2026/08/hackers-breach-polish-power-plant.html
- **BdThemes Supply Chain Attack Poisons JSON to Create Rogue WordPress Admins**: The Hacker News - https://thehackernews.com/2026/08/bdthemes-supply-chain-attack-poisons.html
- **Hackers breached a small Polish energy plant via private APN last year**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-breached-a-small-polish-energy-plant-via-private-apn-last-year/
- **'GhostJacking' Exposes Identity Governance Gaps in AI Agents**: Dark Reading - https://www.darkreading.com/cyber-risk/ghostjacking-identity-governance-gaps-ai-agents
- **Multistate Water System Attacks Widen, Iran Suspected**: Dark Reading - https://www.darkreading.com/ics-ot-security/multistate-water-system-attacks-widen-iran-suspected
- **BdThemes plugins supply-chain hack creates rogue WordPress admins**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/bdthemes-plugins-supply-chain-hack-creates-rogue-wordpress-admins/
- **Metabase SQL Zero-Day Attacks Could Have Wide Blast Radius**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/metabase-sql-zero-day-attacks-wide-blast-radius
- **OpenAI releases ChatGPT 5.6 Cyber, but it's only for approved users**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/openai-releases-chatgpt-56-cyber-but-its-only-for-approved-users/
- **The Patch Gap: Why Defenders Need to Think in Chains, Not Checklists**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/patch-gap-defenders-chains-not-checklists
