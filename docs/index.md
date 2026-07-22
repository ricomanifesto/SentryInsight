# Exploitation Report

## Executive Summary

Active exploitation activity has surged across multiple critical platforms in July 2026, with threat actors rapidly weaponizing freshly disclosed vulnerabilities before organizations can patch. Microsoft SharePoint Server faces ongoing attacks leveraging CVE-2026-50522, a remote code execution flaw that allows attackers to steal machine keys and maintain persistent access even after patching. Simultaneously, the WordPress ecosystem is under mass exploitation from the chained "wp2shell" vulnerabilities (CVE-2026-60137 and CVE-2026-63030), which enable unauthenticated remote code execution and complete site compromise within days of public disclosure.

Ransomware operations continue to evolve in sophistication and targeting. The Qilin (Agenda) ransomware gang has adopted a now-patched Palo Alto Networks PAN-OS GlobalProtect authentication bypass as their primary initial access vector, demonstrating the speed with which affiliates operationalize N-day vulnerabilities. Meanwhile, the novel JADEPUFFER operator—an AI-agent-driven threat actor—has deployed custom ENCFORGE ransomware targeting AI model files, training datasets, and vector databases through Langflow RCE exploitation. Anubis ransomware has claimed a high-profile breach of Coca-Cola's Fairlife subsidiary, and SonicWall SMA1000 appliances were exploited as zero-days for weeks to deploy custom malware on VPN endpoints.

Emerging attack surfaces around AI-assisted development tools and agentic systems are being actively probed. AWS Kiro's agentic IDE was shown to execute attacker-controlled code via hidden web page text, while sandbox escapes across Cursor, Codex, Gemini CLI, and Antigravity allow AI agents to break out of isolation through file-write tricks. The Estée Lauder breach via Oracle E-Business Suite and the $23.7 million Ostium crypto theft via off-chain infrastructure compromise further illustrate the breadth of active campaigns.

## Active Exploitation Details

### Microsoft SharePoint Server RCE (CVE-2026-50522)
- **Description**: A critical remote code execution vulnerability in Microsoft SharePoint Server that was patched during July 2026 Patch Tuesday. The flaw allows unauthenticated attackers to execute arbitrary code on vulnerable servers.
- **Impact**: Attackers are actively exploiting this vulnerability to steal machine keys, which enables them to maintain persistent access to compromised SharePoint environments even after the servers are patched. The theft of machine keys effectively bypasses remediation efforts by allowing attackers to forge authentication tokens and sign malicious content.
- **Status**: Under active exploitation following public proof-of-concept release. Microsoft has released patches, but machine key compromise requires additional remediation (key rotation) beyond patching.
- **CVE ID**: CVE-2026-50522

### WordPress wp2shell Vulnerability Chain (CVE-2026-60137, CVE-2026-63030)
- **Description**: A pair of critical vulnerabilities in WordPress Core that, when chained together, enable unauthenticated remote code execution. CVE-2026-60137 and CVE-2026-63030 form the "wp2shell" exploit suite affecting millions of WordPress sites.
- **Impact**: Attackers can deploy persistent webshells, install malicious plugins, and achieve complete compromise of vulnerable WordPress installations without authentication. The exploit chain provides full remote control over affected websites.
- **Status**: Mass exploitation underway within days of disclosure. Public exploit availability has fueled widespread scanning and automated attacks against the WordPress attack surface. Patches are available but deployment lags across the vast WordPress ecosystem.
- **CVE ID**: CVE-2026-60137, CVE-2026-63030

### Palo Alto Networks PAN-OS GlobalProtect Authentication Bypass
- **Description**: A high-severity authentication bypass vulnerability in Palo Alto Networks PAN-OS GlobalProtect VPN portal. The flaw allows unauthenticated attackers to bypass authentication mechanisms and gain initial access to internal networks.
- **Impact**: Provides direct initial access for ransomware deployment. The Qilin ransomware gang is actively using this vulnerability as an entry point to breach victim environments and deploy encryptors.
- **Status**: Now-patched vulnerability being actively exploited by Qilin ransomware affiliates. Arctic Wolf has confirmed Qilin's use of this vector in recent intrusions.
- **CVE ID**: Not explicitly provided in source articles

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A zero-day vulnerability in the Windows LegacyHive component that allows attackers to escalate privileges on fully patched Windows systems. The flaw was recently disclosed with no official vendor patch availability.
- **Impact**: Local privilege escalation to SYSTEM, enabling attackers to bypass security controls, disable defenses, and achieve full control over compromised endpoints.
- **Status**: Actively exploited in the wild as a zero-day. Free unofficial patches have been released by third-party researchers (0patch) to mitigate the issue while Microsoft develops an official fix.
- **CVE ID**: Not explicitly provided in source articles

### SonicWall SMA1000 Zero-Day Exploitation
- **Description**: Two vulnerabilities in SonicWall SMA1000 series VPN appliances that were exploited as zero-days for weeks before disclosure. The flaws allow unauthenticated attackers to install custom malware on the appliances.
- **Impact**: Persistent compromise of VPN infrastructure, enabling network access, traffic interception, and lateral movement. Custom malware implants survive reboots and provide long-term access.
- **Status**: Zero-day exploitation confirmed for weeks prior to public disclosure. SonicWall has since released patches for the exploited vulnerabilities.
- **CVE ID**: Not explicitly provided in source articles

### ServiceNow AI Platform Unauthenticated Code Execution
- **Description**: A critical security flaw in the ServiceNow AI Platform that allows unauthenticated remote code execution. The vulnerability was recently disclosed and is already being exploited in the wild.
- **Impact**: Full unauthenticated code execution on ServiceNow AI Platform instances, potentially exposing enterprise workflow data, ITSM records, and integrated systems.
- **Status**: Active exploitation confirmed by Defused Cyber. Threat actors are targeting exposed instances immediately following disclosure.
- **CVE ID**: Not explicitly provided in source articles

### Langflow RCE Exploitation by JADEPUFFER
- **Description**: A remote code execution vulnerability in Langflow (an AI agent workflow framework) being exploited by the JADEPUFFER operator—an autonomous AI-agent-driven threat actor.
- **Impact**: Deployment of ENCFORGE ransomware specifically targeting AI assets including training datasets, vector databases, and model checkpoints. The operator has conducted multiple attacks on the same infrastructure.
- **Status**: Active targeting of Langflow servers. JADEPUFFER has upgraded tooling to include custom ransomware (ENCFORGE) focused on AI/ML model data destruction and encryption.
- **CVE ID**: Not explicitly provided in source articles

### Oracle E-Business Suite Flaw (Estée Lauder Breach)
- **Description**: A vulnerability in Oracle E-Business Suite exploited to breach Estée Lauder's HR operations infrastructure. The flaw allowed unauthorized access to employee data.
- **Impact**: Data breach affecting Estée Lauder employees. Attackers accessed HR systems through the Oracle E-Business Suite vulnerability, leading to notification obligations.
- **Status**: Exploitation confirmed resulting in confirmed data breach. Estée Lauder is notifying affected employees.
- **CVE ID**: Not explicitly provided in source articles

### AWS Kiro Agentic IDE Code Execution
- **Description**: A vulnerability in AWS Kiro (agentic coding IDE) where hidden text on a web page can cause the IDE to rewrite its own configuration file and execute attacker-controlled code on the developer's machine.
- **Impact**: Arbitrary code execution on developer workstations through poisoned web content. No approval step can prevent the execution, bypassing human-in-the-loop safeguards.
- **Status**: Demonstrated as exploitable. AWS has been notified; patch status not specified in source.
- **CVE ID**: Not explicitly provided in source articles

### AI Coding Tool Sandbox Escapes (Cursor, Codex, Gemini CLI, Antigravity)
- **Description**: Researchers demonstrated sandbox escapes across four major AI-assisted coding tools (Cursor, Codex, Gemini CLI, Antigravity) by having the AI agent write files that trusted host tools later execute.
- **Impact**: Escape from AI agent sandboxes to achieve code execution on the host system. Multiple CVEs assigned and patches released; Google downgraded two severity ratings post-disclosure.
- **Status**: Vulnerabilities disclosed with patches available. Represents a systemic class of vulnerabilities in AI agent architectures.
- **CVE ID**: Multiple CVEs assigned (specific IDs not provided in source articles)

## Affected Systems and Products

- **Microsoft SharePoint Server**: All versions vulnerable to CVE-2026-50522 prior to July 2026 Patch Tuesday updates. Machine key compromise persists post-patching without key rotation.
- **WordPress Core**: Millions of sites running versions affected by CVE-2026-60137 and CVE-2026-63030. Entire WordPress ecosystem exposed due to widespread deployment and slow patch adoption.
- **Palo Alto Networks PAN-OS GlobalProtect**: VPN portal/appliance versions prior to the authentication bypass fix. Used as initial access for Qilin ransomware deployment.
- **Windows (LegacyHive component)**: Up-to-date Windows systems vulnerable to zero-day privilege escalation until official patch release. Unofficial 0patch mitigations available.
- **SonicWall SMA1000 Series**: VPN appliances exploited as zero-days for weeks. Custom malware implants persist on compromised devices.
- **ServiceNow AI Platform**: Instances exposed to unauthenticated code execution. Enterprise ITSM and workflow automation platforms at risk.
- **Langflow**: AI agent workflow framework servers targeted by JADEPUFFER operator for ENCFORGE ransomware deployment against AI model assets.
- **Oracle E-Business Suite**: HR module deployments vulnerable to exploitation leading to employee data breach (Estée Lauder incident).
- **AWS Kiro**: Agentic coding IDE installations vulnerable to configuration manipulation and code execution via poisoned web content.
- **AI Coding Assistants**: Cursor, Codex, Gemini CLI, Antigravity—all affected by sandbox escape vulnerabilities allowing host code execution.

## Attack Vectors and Techniques

- **Machine Key Theft for Persistent Access**: Exploitation of CVE-2026-50522 to extract SharePoint machine keys, enabling attackers to forge authentication tokens and maintain access after patching. This technique defeats standard remediation by compromising the cryptographic trust anchor.
- **Vulnerability Chaining for Unauthenticated RCE**: wp2shell exploitation chains CVE-2026-60137 and CVE-2026-63030 to achieve unauthenticated remote code execution on WordPress Core, bypassing authentication entirely and enabling mass compromise.
- **VPN Authentication Bypass for Initial Access**: Qilin ransomware affiliates exploit PAN-OS GlobalProtect authentication bypass to gain initial foothold in target networks without credentials, demonstrating rapid operationalization of N-day vulnerabilities.
- **Zero-Day Privilege Escalation**: Windows LegacyHive zero-day provides local privilege escalation to SYSTEM on fully patched systems, used to bypass endpoint defenses and deploy follow-on payloads.
- **Custom Malware on VPN Appliances**: SonicWall SMA1000 zero-day exploitation deploys persistent custom malware on VPN hardware, providing network-level persistence that survives reboots and firmware updates.
- **AI Asset-Targeted Ransomware**: ENCFORGE ransomware specifically encrypts AI/ML assets—training datasets, vector databases, model checkpoints—representing a novel targeting paradigm for intellectual property destruction.
- **Off-Chain Infrastructure Compromise**: $23.7M crypto theft from Ostium via compromise of off-chain price feed infrastructure, demonstrating supply chain attacks on DeFi oracle systems.
- **Hidden Text Injection for AI Agent Hijacking**: AWS Kiro exploited via invisible/hidden text on web pages that instructs the agentic IDE to rewrite configuration and execute code, bypassing approval mechanisms.
- **Sandbox Escape via Trusted Tool Chain**: AI coding agents escape sandboxes by writing files that are subsequently executed by trusted host tools (linters, formatters, build systems), turning the agent's legitimate capabilities into an exploit primitive.
- **AI-Agent-Driven Autonomous Operations**: JADEPUFFER operator uses autonomous AI agents to conduct reconnaissance, exploitation, and ransomware deployment with minimal human intervention, including repeat targeting of the same infrastructure.

## Threat Actor Activities

- **Qilin (Agenda) Ransomware Gang**: Actively exploiting PAN-OS GlobalProtect authentication bypass for initial access in ransomware campaigns. Confirmed by Arctic Wolf. Rapid adoption of N-day vulnerabilities for affiliate operations. High-volume targeting of enterprise VPN infrastructure.
- **Anubis Ransomware Gang**: Claimed responsibility for cyberattack on Coca-Cola's Fairlife dairy subsidiary. Threatening to publish allegedly stolen corporate data. Operating as a traditional double-extortion ransomware group with leak site operations.
- **JADEPUFFER (AI-Agent-Driven Operator)**: Autonomous AI-agent-driven threat actor documented by Sysdig. Conducted multiple attacks on Langflow servers. Deployed custom ENCFORGE ransomware targeting AI model files, training data, and vector databases. Demonstrates evolution toward AI-driven offensive operations.
- **ENCFORGE Ransomware Operation**: Custom ransomware deployed by JADEPUFFER, specifically designed to encrypt AI/ML assets. Represents specialized tooling for high-value intellectual property targets in AI development environments.
- **"Trim" (Russian-Speaking Actor)**: Dismantled publicly available frontier AI models and integrated them with offensive security tools to create an offensive attack platform. Demonstrates individual actors weaponizing AI jailbreaks for capability development.
- **Arctic Wolf (Threat Intelligence)**: Security firm tracking and reporting on Qilin ransomware's exploitation of PAN-OS vulnerability. Provides visibility into affiliate tactics and initial access trends.
- **Defused Cyber (Threat Intelligence)**: Reported active exploitation of ServiceNow AI Platform flaw for unauthenticated code execution. Shared intelligence via public disclosure on X.
- **Sysdig (Security Research)**: Documented JADEPUFFER operator activity and ENCFORGE ransomware deployment. Linked multiple attacks on same Langflow infrastructure to the same AI-agent-driven operator.
- **watchTowr (Security Research)**: Reported active exploitation of CVE-2026-50522 (SharePoint RCE) following public PoC release. Provided early warning on post-patch exploitation activity.

## Source Attribution

- **Ransomware Is Accelerating, But It's Not Because of AI**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/ransomware-is-accelerating-not-ai
- **Using LLMs to Find and Prioritize Vulnerabilities Is No Easy Task**: Dark Reading - https://www.darkreading.com/application-security/finding-and-prioritizing-vulnerabilities-no-easy-task
- **Critical SharePoint RCE flaw exploited to steal machine keys**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/critical-sharepoint-rce-flaw-exploited-to-steal-machine-keys/
- **Anubis ransomware claims Coca-Cola Fairlife attack, threatens data leak**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/anubis-ransomware-claims-coca-cola-fairlife-attack-threatens-data-leak/
- **Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs**: The Hacker News - https://thehackernews.com/2026/07/apple-fixes-hide-my-email-bug-that.html
- **Hacker Turns AI Jailbreaks Into Offensive Attack Platform**: Dark Reading - https://www.darkreading.com/cyber-risk/hacker-ai-jailbreaks-offensive-attack-platform
- **Critical wp2shell WordPress flaws exploited to install webshells**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/critical-wp2shell-wordpress-flaws-exploited-to-install-webshells/
- **AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code**: The Hacker News - https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html
- **Google Launches Gemini 3.5 Flash Cyber AI to Find and Fix Software Vulnerabilities**: The Hacker News - https://thehackernews.com/2026/07/google-launches-gemini-35-flash-cyber.html
- **Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC**: The Hacker News - https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
- **Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access**: The Hacker News - https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
- **Closing the Identity Gaps in Critical Infrastructure Security**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/closing-the-identity-gaps-in-critical-infrastructure-security/
- **Zimbra Patches Critical SNMP Command Injection and Four XSS Vulnerabilities**: The Hacker News - https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html
- **Choose Wisely: AI-Generated Coding Risk Varies, a Lot**: Dark Reading - https://www.darkreading.com/application-security/choose-wisely-ai-generated-coding-risk-varies
- **Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs**: The Hacker News - https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html
- **N-day is Becoming N-Hour. Patching Faster Won't Save You.**: The Hacker News - https://thehackernews.com/2026/07/n-day-is-becoming-n-hour-patching.html
- **New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit**: The Hacker News - https://thehackernews.com/2026/07/new-bit2watt-attack-could-let-cloud.html
- **US seizes over 1,000 websites in FIFA World Cup piracy crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-seizes-over-1-000-fifa-world-cup-illegal-streaming-domains/
- **Critical Palo Alto VPN bug now exploited by Qilin ransomware gang**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/critical-globalprotect-vpn-bug-now-exploited-in-ransomware-attacks/
- **Microsoft shares manual fix for WSUS sync delays and timeouts**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-manual-fix-for-wsus-sync-delays-and-timeouts/
- **WordPress wp2shell Exploitation Grows as Public Exploit Fuels Mass Scanning**: The Hacker News - https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
- **Windows LegacyHive zero-day flaw gets free, unofficial patches**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/windows-legacyhive-zero-day-flaw-gets-free-unofficial-patches/
- **New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack**: The Hacker News - https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html
- **Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution**: The Hacker News - https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
- **Estée Lauder discloses data breach via Oracle E-Business flaw**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/est-e-lauder-discloses-data-breach-via-oracle-e-business-flaw/
- **SonicWall SMA1000 flaws exploited as zero-days to push custom malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sonicwall-sma1000-flaws-exploited-as-zero-days-to-push-custom-malware/
- **Hackers steal $23.7 million in crypto from Ostium in off-chain attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-steal-237-million-in-crypto-from-ostium-in-off-chain-attack/
- **'WP2Shell' Opens Millions of WordPress Sites to Remote Takeover**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/wp2shell-millions-wordpress-sites-remote-takeover
- **Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/
- **JadePuffer agentic attacks now target AI model data with ransomware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-attacks-now-target-ai-model-data-with-ransomware/
