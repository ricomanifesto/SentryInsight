# Exploitation Report

## Executive Summary

Active exploitation activity has surged across multiple critical vectors in July 2026, with ransomware groups rapidly weaponizing freshly disclosed vulnerabilities. The most severe activity centers on the **wp2shell** vulnerability chain in WordPress Core (CVE-2026-60137 and CVE-2026-63030), which attackers began chaining for unauthenticated remote code execution within days of public disclosure, fueling mass scanning and webshell deployment across millions of sites. Simultaneously, the **Qilin (Agenda) ransomware gang** is actively exploiting a critical Palo Alto Networks PAN-OS GlobalProtect authentication bypass flaw for initial access, with Arctic Wolf confirming real-world intrusions. Microsoft's July Patch Tuesday brought a third SharePoint Server RCE (CVE-2026-50522) under active exploitation after a public proof-of-concept emerged, per watchTowr.

Beyond traditional infrastructure, a new class of **AI-agent-driven attacks** has emerged. The autonomous operator **JADEPUFFER** has been linked to Langflow RCE exploitation deploying the novel **ENCFORGE ransomware**, which specifically targets AI model files, training datasets, and vector databases. Researchers also demonstrated sandbox escapes across major AI coding assistants (Cursor, Codex, Gemini CLI, Antigravity), while a Russian-speaking actor "Trim" has integrated jailbroken frontier models into an offensive attack platform. SonicWall SMA1000 appliances were exploited as zero-days for weeks before disclosure, and ServiceNow's AI Platform is now seeing unauthenticated code execution attacks in the wild.

## Active Exploitation Details

### WordPress wp2shell Vulnerability Chain (CVE-2026-60137 and CVE-2026-63030)
- **Description**: A critical vulnerability suite dubbed "wp2shell" affecting WordPress Core, comprising two flaws that when chained together enable unauthenticated remote code execution and complete site compromise. CVE-2026-60137 and CVE-2026-63030 are being combined in exploit chains.
- **Impact**: Attackers achieve full remote code execution on vulnerable WordPress installations, allowing deployment of persistent webshells, installation of malicious plugins, and complete takeover of the hosting environment. Millions of WordPress sites are exposed.
- **Status**: Actively exploited in the wild. Public exploit code emerged shortly after disclosure, triggering mass scanning and exploitation attempts within three days. Patches are available but adoption varies across the massive WordPress install base.
- **CVE ID**: CVE-2026-60137, CVE-2026-63030

### Critical SharePoint Server RCE (CVE-2026-50522)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server, patched as part of the July 2026 Patch Tuesday release. This is the third SharePoint flaw addressed in this update cycle.
- **Impact**: Unauthenticated remote code execution on affected SharePoint servers, enabling full server compromise, lateral movement, and data exfiltration.
- **Status**: Under active exploitation following the release of a public proof-of-concept exploit. watchTowr has confirmed exploitation activity in the wild. Organizations must apply the July 2026 security updates immediately.
- **CVE ID**: CVE-2026-50522

### Palo Alto Networks PAN-OS GlobalProtect Authentication Bypass
- **Description**: A high-severity authentication bypass vulnerability in Palo Alto Networks PAN-OS GlobalProtect VPN portal. The flaw allows unauthenticated attackers to bypass authentication mechanisms.
- **Impact**: Provides initial network access for threat actors, enabling subsequent ransomware deployment, data theft, and lateral movement. Qilin ransomware operators are using this as their primary entry vector.
- **Status**: Actively exploited by Qilin (Agenda) ransomware gang. Arctic Wolf has confirmed real-world intrusions leveraging this vulnerability. Palo Alto Networks has released patches; immediate application is critical for all GlobalProtect deployments.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### SonicWall SMA1000 Zero-Day Exploitation
- **Description**: Two vulnerabilities in SonicWall SMA1000 series VPN appliances that were exploited as zero-days for several weeks before public disclosure.
- **Impact**: Attackers installed custom malware on vulnerable VPN appliances, establishing persistent access to victim networks, enabling credential harvesting, and facilitating further compromise.
- **Status**: Zero-day exploitation occurred for weeks prior to disclosure. SonicWall has since released patches. Organizations should investigate logs for signs of compromise during the pre-patch window.
- **CVE ID**: [CVE IDs not explicitly provided in source articles]

### ServiceNow AI Platform Unauthenticated Code Execution
- **Description**: A critical security flaw in the ServiceNow AI Platform that allows unauthenticated remote code execution.
- **Impact**: Full server compromise without authentication, potentially exposing sensitive IT service management data, workflows, and connected systems.
- **Status**: Actively exploited in the wild. Defused Cyber has observed and reported active exploitation attempts. ServiceNow has issued security advisories and patches.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### Langflow RCE Exploited by JADEPUFFER for ENCFORGE Ransomware
- **Description**: A remote code execution vulnerability in Langflow (an AI agent workflow framework) being exploited by the autonomous AI agent operator JADEPUFFER to deploy ENCFORGE ransomware.
- **Impact**: Encryption of high-value AI assets including training datasets, vector databases, model checkpoints, and other machine learning artifacts. Represents a novel targeting of AI/ML infrastructure.
- **Status**: Active exploitation confirmed by Sysdig researchers. JADEPUFFER has conducted multiple attacks on the same Langflow server infrastructure. Patches for the underlying Langflow RCE should be applied immediately.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### Oracle E-Business Suite Flaw (Estée Lauder Breach)
- **Description**: A vulnerability in Oracle E-Business Suite exploited to breach Estée Lauder's HR operations environment.
- **Impact**: Data breach affecting customer information. Attackers leveraged the flaw in the HR module to access sensitive personal data.
- **Status**: Exploitation confirmed; Estée Lauder has disclosed the breach and is notifying affected customers. Oracle has likely issued patches for the affected E-Business Suite components.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### Windows LegacyHive Zero-Day Privilege Escalation
- **Description**: A zero-day privilege escalation vulnerability in Windows LegacyHive component affecting up-to-date Windows systems.
- **Impact**: Local privilege escalation allowing attackers to gain SYSTEM-level access from standard user contexts.
- **Status**: Actively exploited as a zero-day. Unofficial micropatches are available from 0patch while Microsoft develops an official fix. No official patch released at time of reporting.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### AWS Kiro Agentic IDE Code Execution via Poisoned Web Content
- **Description**: A flaw in AWS Kiro (agentic coding IDE) where hidden text on a web page can cause the IDE to rewrite its own configuration file and execute attacker-controlled code on the developer's machine.
- **Impact**: Arbitrary code execution on developer workstations with no approval step required. Supply chain risk through compromised development environments.
- **Status**: Vulnerability disclosed; AWS is expected to release mitigations. Developers using Kiro should exercise caution with web content rendering.
- **CVE ID**: [CVE ID not explicitly provided in source articles]

### AI Coding Assistant Sandbox Escapes (Cursor, Codex, Gemini CLI, Antigravity)
- **Description**: Researchers demonstrated sandbox escape vulnerabilities across four major AI coding assistants where the AI agent can write files that trusted host tools later execute, breaking out of the intended isolation.
- **Impact**: Arbitrary code execution on host systems from within the AI assistant sandbox, compromising developer machines and potentially CI/CD pipelines.
- **Status**: Multiple CVEs assigned; patches released by vendors. Google has downgraded two Gemini CLI capabilities as mitigation. Developers should update all AI coding tools immediately.
- **CVE ID**: [Multiple CVEs assigned but not explicitly listed in source articles]

## Affected Systems and Products

- **WordPress Core**: All versions prior to patched releases addressing CVE-2026-60137 and CVE-2026-63030. Millions of sites globally affected.
- **Microsoft SharePoint Server**: Versions affected by CVE-2026-50522 (specific versions detailed in July 2026 Patch Tuesday advisory).
- **Palo Alto Networks PAN-OS**: GlobalProtect VPN portal versions prior to the authentication bypass fix. All PAN-OS versions with GlobalProtect enabled.
- **SonicWall SMA1000 Series**: SMA1000 appliances running firmware versions vulnerable to the two zero-day flaws exploited pre-disclosure.
- **ServiceNow AI Platform**: Instances running vulnerable versions of the AI Platform module prior to security patches.
- **Langflow**: Deployments running versions vulnerable to the RCE exploited by JADEPUFFER/ENCFORGE.
- **Oracle E-Business Suite**: HR module versions containing the exploited flaw used in the Estée Lauder breach.
- **Windows (All Supported Versions)**: LegacyHive component vulnerability affecting up-to-date Windows 10/11 and Server editions.
- **AWS Kiro**: Agentic coding IDE installations processing untrusted web content.
- **AI Coding Assistants**: Cursor, OpenAI Codex CLI, Google Gemini CLI, and Antigravity prior to sandbox escape patches.

## Attack Vectors and Techniques

- **Chained WordPress RCE (wp2shell)**: Attackers chain CVE-2026-60137 and CVE-2026-63030 to achieve unauthenticated remote code execution, deploying webshells and malicious plugins for persistence.
- **Public PoC-Driven SharePoint Exploitation**: Rapid weaponization of CVE-2026-50522 proof-of-concept code for unauthenticated RCE against internet-facing SharePoint servers.
- **VPN Authentication Bypass for Initial Access**: Qilin ransomware operators exploit PAN-OS GlobalProtect authentication bypass to gain initial network foothold without credentials.
- **Zero-Day VPN Appliance Compromise**: SonicWall SMA1000 flaws exploited pre-disclosure to install custom malware on edge VPN devices, bypassing perimeter defenses.
- **AI Platform Unauthenticated RCE**: Direct exploitation of ServiceNow AI Platform flaw for code execution without authentication.
- **AI Workflow Framework Targeting**: JADEPUFFER exploits Langflow RCE to deploy ENCFORGE ransomware specifically encrypting AI/ML model artifacts.
- **Poisoned Web Content for IDE Compromise**: Hidden text/markup on web pages triggers AWS Kiro to rewrite config and execute attacker code on developer machines.
- **AI Agent Sandbox Escape via File Write**: Malicious prompts cause AI coding assistants to write files that are subsequently executed by trusted host tools, breaking sandbox isolation.
- **Fileless BEC Phishing (The TFF Trap)**: Attackers combine fileless techniques and low-detection loaders to deploy RATs/stealers (Agent Tesla, Remcos, XWorm, Best Private Logger).
- **Off-Chain Infrastructure Compromise**: Ostium attack via compromised price feed infrastructure rather than on-chain smart contract exploitation.

## Threat Actor Activities

- **Qilin (Agenda) Ransomware Gang**: Actively exploiting PAN-OS GlobalProtect authentication bypass for initial access in ransomware campaigns. Confirmed by Arctic Wolf. High-volume targeting of VPN-exposed organizations.
- **Anubis Ransomware Gang**: Claimed responsibility for Coca-Cola Fairlife subsidiary attack, threatening data leak. Operating as a Ransomware-as-a-Service (RaaS) affiliate model.
- **JADEPUFFER (AI-Agent-Driven Operator)**: Autonomous AI agent operator conducting novel attacks on AI/ML infrastructure. Linked to Langflow RCE exploitation and deployment of ENCFORGE ransomware targeting model files, datasets, and vector databases. Tracked by Sysdig.
- **Trim (Russian-Speaking Actor)**: Developed offensive attack platform by jailbreaking frontier AI models and integrating them with security tools. Demonstrates AI-enabled offensive capability development.
- **Defused Cyber**: Threat intelligence firm reporting active exploitation of ServiceNow AI Platform flaw via unauthenticated code execution.
- **watchTowr**: Security research firm confirming active exploitation of SharePoint CVE-2026-50522 following public PoC release.
- **Arctic Wolf**: Cybersecurity company attributing PAN-OS GlobalProtect exploitation to Qilin ransomware operations.
- **Sysdig**: Researchers tracking JADEPUFFER campaigns and ENCFORGE ransomware targeting AI assets.
- **Unknown Actors (BEC/Phishing)**: Operators behind "The TFF Trap" campaign deploying Agent Tesla, Remcos, XWorm, and Best Private Logger via fileless phishing techniques.
- **Unknown Actors (Ostium Attack)**: Compromised off-chain price feed infrastructure to steal $23.75M from liquidity provider vault.

## Source Attribution

- **Anubis ransomware claims Coca-Cola Fairlife attack, threatens data leak**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/anubis-ransomware-claims-coca-cola-fairlife-attack-threatens-data-leak/
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
- **Remediating Vulnerabilities With LLMs: Inside Ivanti's Automation Push**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/remediating-vulnerabilities-llms-ivanti-automation
- **25 Years After Code Red: What the Worm Era Can Teach Us About AI Security**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/25-years-after-code-red-what-the-worm-era-can-teach-us-about-ai-security-2
- **CISOs Feel the Heat Over AI Risk**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cisos-feel-heat-ai-risk
- **Attackers Combo Up Evasion Tactics for BEC Phishing**: Dark Reading - https://www.darkreading.com/endpoint-security/attackers-combo-evasion-tactics-bec-phishing
