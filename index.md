# Exploitation Report

## Executive Summary

Active exploitation of critical vulnerabilities continues to accelerate across enterprise infrastructure, cloud environments, and consumer platforms. A maximum-severity command injection flaw in Arista VeloCloud Orchestrator (CVE-2026-16812) has been actively exploited as a zero-day before patch availability, while a separate zero-day in the widely deployed FastJson Java library is under active exploitation against U.S. firms with no patch yet released. Both vulnerabilities enable unauthenticated remote code execution and represent immediate risks to exposed deployments.

Simultaneously, threat actors are leveraging newly published proof-of-concept exploits for recently patched vulnerabilities in vBulletin, GitLab, and n8n, creating a narrow window for exploitation before organizations apply updates. The Dysphoria IoT botnet has expanded to approximately 200,000 compromised devices globally, incorporating blockchain-based command-and-control infrastructure and victim relay capabilities following law enforcement disruption of its predecessor infrastructure. Novel attack techniques—including ClickFix social engineering on Steam forums, browser-based malware assembly via malvertising (SourTrade), and AI-driven espionage using autonomous agents—demonstrate rapid adversary innovation beyond traditional vulnerability exploitation.

## Active Exploitation Details

### Arista VeloCloud Orchestrator Command Injection (CVE-2026-16812)
- **Description**: A maximum-severity command injection vulnerability affecting on-premises deployments of Arista VeloCloud Orchestrator (VCO). The flaw allows attackers to execute arbitrary commands on the underlying operating system.
- **Impact**: Full compromise of the VCO appliance, potential lateral movement into connected network segments, and complete control over SD-WAN orchestration functions.
- **Status**: Actively exploited in the wild as a zero-day prior to patch release. Arista has since issued patches for affected on-premises VCO versions.
- **CVE ID**: CVE-2026-16812

### FastJson 1.x Remote Code Execution
- **Description**: A critical deserialization vulnerability in FastJson, Alibaba's open-source JSON library for Java. In affected Spring Boot applications, a malicious JSON request can trigger arbitrary code execution without authentication or user interaction.
- **Impact**: Unauthenticated remote code execution on any Java application using vulnerable FastJson 1.x versions, particularly Spring Boot services exposed to untrusted input.
- **Status**: Actively exploited in zero-day attacks targeting U.S. firms. As of the reporting period, no patched version is available for the 1.x branch, leaving users dependent on mitigations or migration to FastJson 2.x.
- **CVE ID**: Not explicitly provided in source articles

### Certighost — Active Directory Certificate Services Vulnerability
- **Description**: A vulnerability in Windows Active Directory Certificate Services (AD CS) that enables authenticated attackers to escalate privileges and compromise the domain.
- **Impact**: Domain compromise from any authenticated user context, enabling persistence, lateral movement, and full control over Active Directory.
- **Status**: A proof-of-concept exploit has been publicly released, significantly lowering the barrier for exploitation. Patching status depends on Microsoft's AD CS updates.
- **CVE ID**: Not explicitly provided in source articles

### vBulletin Pre-Authentication Code Execution
- **Description**: An unauthenticated remote code execution flaw in vBulletin forum software where a crafted request reaches PHP's `eval()` function, allowing arbitrary code execution on the server.
- **Impact**: Complete compromise of the forum server, access to user data, and potential pivot to connected infrastructure.
- **Status**: The vulnerability was patched six weeks prior to public exploit release on July 27. Organizations that have not applied the patch are now at high risk due to public exploit availability.
- **CVE ID**: Not explicitly provided in source articles

### n8n Sandbox Escape
- **Description**: A high-severity expression-sandbox escape in the n8n workflow automation platform. An authenticated workflow editor can break out of the sandbox and execute operating-system commands as the n8n process user.
- **Impact**: Server compromise via legitimate workflow editing functionality, enabling persistence, data exfiltration, and lateral movement.
- **Status**: Patched by n8n following discovery by Security Joes. Exploitation requires authenticated access to the workflow editor.
- **CVE ID**: Not explicitly provided in source articles

### GitLab Authenticated RCE
- **Description**: A remote code execution flaw in GitLab self-managed instances that allows authenticated users to execute commands as the `git` system user.
- **Impact**: Compromise of the GitLab server, access to source code repositories, CI/CD pipelines, and potential supply chain poisoning.
- **Status**: Patched by GitLab on June 10. A working proof-of-concept exploit was published on July 24, six weeks post-patch. Affected versions include 18.11.3 and earlier self-managed instances.
- **CVE ID**: Not explicitly provided in source articles

### Dysphoria IoT Botnet Expansion
- **Description**: A rapidly growing IoT botnet compromising approximately 200,000 devices worldwide for DDoS attacks and traffic relay operations.
- **Impact**: Large-scale DDoS capability, proxy infrastructure for anonymizing malicious traffic, and persistent foothold in compromised device fleets.
- **Status**: Actively expanding with new blockchain-based command-and-control (using blockchain name services) and victim relay mechanisms following the March law-enforcement disruption of the JackSkid botnet infrastructure.
- **CVE ID**: Not explicitly provided in source articles (botnet leverages multiple IoT vulnerabilities)

## Affected Systems and Products

- **Arista VeloCloud Orchestrator (on-premises)**: All on-premises VCO deployments prior to the July 2026 security patch. Cloud-hosted VCO instances are not affected.
- **FastJson 1.x Java Library**: All applications using FastJson 1.x, particularly Spring Boot services parsing untrusted JSON input. No patched 1.x release exists; migration to 2.x required.
- **Windows Active Directory Certificate Services**: Domain controllers running AD CS with vulnerable configurations. Specific affected Windows versions not detailed in source articles.
- **vBulletin Forum Software**: Self-hosted vBulletin instances prior to the June 2026 security patch. Cloud-hosted vBulletin Cloud customers were protected by the vendor.
- **n8n Workflow Automation Platform**: Self-hosted n8n instances prior to the July 2026 patch. Cloud-hosted n8n Cloud instances were updated by the vendor.
- **GitLab Self-Managed**: Versions 18.11.3 and earlier. GitLab.com SaaS was patched by the vendor on June 10.
- **IoT Devices (Dysphoria Botnet)**: Approximately 200,000 compromised devices globally, including routers, cameras, and other embedded Linux systems with weak credentials or unpatched vulnerabilities.
- **Google Cloud Platform & Microsoft Azure**: Environments vulnerable to "Confused Deputy" privilege escalation patterns where cross-service permissions allow administrative access bypass.
- **Steam Discussion Forums**: Valve's Steam community forums abused as a distribution platform for ClickFix social engineering lures.

## Attack Vectors and Techniques

- **Command Injection via Orchestration API**: Attackers send crafted API requests to on-premises VCO instances, injecting OS commands that execute with the privileges of the VCO service account.
- **FastJson Deserialization Gadget Chains**: Malicious JSON payloads with `@type` specifications trigger dangerous deserialization paths, executing arbitrary Java code during parsing without authentication.
- **AD CS Certificate Template Abuse (Certighost)**: Authenticated users request certificates from vulnerable templates, enabling domain controller impersonation and privilege escalation to Domain Admin.
- **PHP `eval()` Injection via Unvalidated Input**: Unauthenticated HTTP requests reach `eval()` in vBulletin's code path, executing attacker-controlled PHP code.
- **Expression Sandbox Escape (n8n)**: Authenticated workflow editors craft malicious expressions that break out of the sandbox's allowlist, achieving OS command execution.
- **GitLab Webhook/Import RCE**: Authenticated users exploit improper validation in repository import or webhook functionality to execute commands as the `git` user.
- **Blockchain-Based C2 (Dysphoria)**: Botnet operators use blockchain name services (e.g., ENS, Handshake) for resilient, censorship-resistant command-and-control domain resolution.
- **Victim Relay Infrastructure (Dysphoria)**: Compromised devices act as encrypted relays for C2 traffic, obscuring the true controller infrastructure and complicating takedown.
- **ClickFix Social Engineering**: Fake "fix" buttons on Steam forums and malvertising pages trick users into copying and executing PowerShell commands that deploy XMRig cryptominers.
- **Browser-Based Malware Assembly (SourTrade)**: Malicious JavaScript on fake Solana, Luno, and TradingView pages fetches payload fragments and uses the legitimate Bun runtime to assemble and execute Windows executables entirely in browser memory.
- **AI Agent "YOLO Mode" Espionage**: Attackers deploy the open-source Hermes autonomous AI agent in unrestricted mode to conduct reconnaissance, credential access, and data exfiltration against the Thai Ministry of Finance.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Cruciferra crypter loads a known vulnerable kernel driver to disable security controls and achieve kernel-level code execution for malware concealment.
- **Process Ghosting**: Malware executes from a deleted file handle, evading file-based detection by creating a process from an executable that no longer exists on disk.
- **Telegram C2 (TELESHIM)**: East Asia-linked threat actor uses Telegram bot API for command-and-control communications targeting Middle Eastern government entities.
- **Confused Deputy Cloud Privilege Escalation**: Attackers exploit excessive cross-service permissions in GCP and Azure to assume administrative roles without direct credential compromise.
- **RMM Tool Delivery via Phishing (Operation BlueDash)**: Microsoft Teams-themed phishing with "secure document" lures delivers legitimate Level RMM and ScreenConnect installers for persistent remote access.
- **Supply Chain Credential Theft (ShinyHunters)**: Credentials obtained via supply-chain compromise enable data breach and extortion against Ernst & Young and other victims.
- **Malvertising Drive-by Compromise**: SourTrade campaign delivers malicious JavaScript through advertising networks on legitimate sites, requiring no user interaction beyond page load.

## Threat Actor Activities

- **VeloCloud Exploitation Actors**: Unknown threat actors actively scanning for and exploiting CVE-2026-16812 in on-premises VCO deployments prior to patch availability. Motivation and attribution not disclosed in source articles.
- **FastJson Zero-Day Exploiters**: Unidentified hackers targeting U.S. firms with FastJson RCE attacks. No attribution provided; activity suggests financially motivated or espionage-focused operators.
- **Dysphoria Botnet Operators**: Tracked by CNCERT and XLab. Demonstrated resilience by migrating to blockchain C2 and relay infrastructure after JackSkid disruption in March 2026. Likely criminal DDoS-for-hire service.
- **Cruciferra Crypter Group**: China-linked cybercrime group conducting income tax-themed phishing against Indian taxpayers, tax professionals, and corporate finance teams. Uses BYOVD and Process Ghosting for stealth.
- **TELESHIM / East Asia-Linked APT**: Threat actor with ties to East Asia targeting government entities in the Middle East. Uses Telegram for C2, indicating focus on operational security and resilient communications.
- **Operation BlueDash Operators**: Unattributed group conducting Microsoft Teams phishing to deploy legitimate RMM tools (Level RMM, ScreenConnect) for persistent access. Tactics suggest initial access broker or ransomware affiliate activity.
- **LockBit Ransomware Affiliates**: Disrupted by FBI-led Operation Cronos. Law enforcement exploited breakdown of trust among affiliates to accelerate takedown of the largest ransomware-as-a-service operation at the time.
- **ShinyHunters Extortion Group**: Claimed responsibility for Ernst & Young data breach via supply-chain credential theft. Leaked data fuels $2,000 Bitcoin sextortion campaigns against exposed individuals.
- **SourTrade Malvertising Operators**: Unattributed group running large-scale malvertising campaign (fake Solana, Luno, TradingView pages) using browser-based malware assembly with Bun runtime.
- **Hermes AI Agent Espionage Operators**: Unknown actors deploying the open-source Hermes autonomous agent in "YOLO mode" against Thailand's Ministry of Finance. Represents novel use of offensive AI agents for state-targeted espionage.
- **GitLab PoC Publishers (depthfirst)**: Security researchers who published working exploit code for a patched GitLab RCE six weeks post-patch. Not a threat actor, but their release accelerates exploitation risk for unpatched instances.

## Source Attribution

- **Attackers Exploit Arista VeloCloud Orchestrator Command Injection Flaw**: The Hacker News - https://thehackernews.com/2026/07/attackers-exploit-arista-velocloud.html
- **AI Agent Drives Espionage Attack on Thai Ministry of Finance**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-espionage-attack-thai-ministry-finance
- **Hackers target US firms in FastJson RCE zero-day attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-target-us-firms-in-fastjson-rce-zero-day-attacks/
- **Arista patches VeloCloud Orchestrator zero-day exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/arista-patches-velocloud-orchestrator-zero-day-exploited-in-attacks/
- **New Dysphoria DDoS botnet spreads to 200k devices worldwide**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-dysphoria-ddos-botnet-spreads-to-200k-devices-worldwide/
- **New Certighost PoC exploit lets attackers hijack Windows domains**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-certighost-poc-exploit-lets-attackers-hijack-windows-domains/
- **'Confused Deputy' Flaws Persist in Google Cloud, Microsoft Azure**: Dark Reading - https://www.darkreading.com/cloud-security/confused-deputy-flaws-google-cloud-microsoft-azure
- **FBI: Breaking Affiliate Trust Sped Along LockBit's Takedown**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/fbi-breaking-affiliate-trust-lockbit-takedown
- **NVIDIA Forms 37-Member Open Secure AI Alliance and Open-Sources NOOA Framework**: The Hacker News - https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html
- **Adversaries Don't Need a Zero-Day — They Read Your Rulebook**: Dark Reading - https://www.darkreading.com/threat-intelligence/adversaries-do-not-need-zero-day-they-read-your-rulebook
- **Apple sued over fake App Store crypto wallet app stealing $1.8M in Bitcoin**: Bleeping Computer - https://www.bleepingcomputer.com/news/apple/apple-sued-over-fake-app-store-crypto-wallet-app-stealing-18m-in-bitcoin/
- **Dysphoria IoT Botnet Adds Blockchain C2 and Victim Relays After JackSkid Disruption**: The Hacker News - https://thehackernews.com/2026/07/dysphoria-iot-botnet-adds-blockchain-c2.html
- **Coca-Cola confirms data theft in Fairlife ransomware attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coca-cola-confirms-data-theft-in-fairlife-ransomware-attack/
- **Ernst \& Young data breach claimed by ShinyHunters extortion gang**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ernst-and-young-data-breach-claimed-by-shinyhunters-extortion-gang/
- **Public Exploit Released for Patched vBulletin Pre-Auth Code Execution Flaw**: The Hacker News - https://thehackernews.com/2026/07/public-exploit-released-for-patched.html
- **⚡ Weekly Recap: Rogue AI Agents, Check Point Exploit, Slopsquatting, ClickFix Lures and More**: The Hacker News - https://thehackernews.com/2026/07/weekly-recap-rogue-ai-agents-check.html
- **Shadow AI agents are multiplying. Here's how to find and secure them.**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/shadow-ai-agents-are-multiplying-heres-how-to-find-and-secure-them/
- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process**: The Hacker News - https://thehackernews.com/2026/07/n8n-sandbox-escape-lets-workflow.html
- **Operation BlueDash Deploys Level RMM and ScreenConnect via Fake Teams Update**: The Hacker News - https://thehackernews.com/2026/07/operation-bluedash-deploys-level-rmm.html
- **Cruciferra Crypter Uses BYOVD and Process Ghosting to Hide Windows Malware**: The Hacker News - https://thehackernews.com/2026/07/cruciferra-crypter-uses-byovd-and.html
- **TELESHIM Abuses Telegram for C2 in Attacks Against Middle East Governments**: The Hacker News - https://thehackernews.com/2026/07/teleshim-abuses-telegram-for-c2-in.html
- **GitHub Adds 3-Day Dependabot Cooldown to Limit Poisoned Package Adoption**: The Hacker News - https://thehackernews.com/2026/07/github-adds-3-day-dependabot-cooldown.html
- **GitHub, PyPI add time-based defenses against supply chain attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/github-pypi-add-time-absed-defenses-against-supply-chain-attacks/
- **Steam forum ClickFix attacks infect gamers with XMRig cryptominers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/steam-forum-clickfix-attacks-infect-gamers-with-xmrig-cryptominers/
- **Malvertising Sends Malware in Pieces, Then Makes the Browser Build the Executable**: The Hacker News - https://thehackernews.com/2026/07/malvertising-sends-malware-in-pieces.html
- **Malicious sites use JavaScript to build malware in browser memory**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/malicious-sites-use-javascript-to-build-malware-in-browser-memory/
- **ShinyHunters data leaks fuel $2,000 sextortion email scam**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/shinyhunters-data-leaks-fuel-2-000-sextortion-email-scam/
- **Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available**: The Hacker News - https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html
- **Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git**: The Hacker News - https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html
- **CTM360 Research Reveals How Insurance Phishing Has Evolved Into Real-Time Account Hijacking**: The Hacker News - https://thehackernews.com/2026/07/ctm360-research-reveals-how-insurance.html
