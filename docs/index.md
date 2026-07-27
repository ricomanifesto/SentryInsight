# Exploitation Report

## Executive Summary

This reporting period reveals a significant escalation in the exploitation of automation and AI-driven workflows, with critical vulnerabilities in widely deployed platforms such as n8n, GitLab, and Fastjson enabling remote code execution. Simultaneously, threat actors are weaponizing legitimate remote monitoring and management (RMM) tools through sophisticated social engineering campaigns—exemplified by Operation BlueDash and BlueNoroff's phishing kits—while the Cl0p ransomware affiliate network continues to mass-scan for unpatched PTC Windchill and FlexPLM instances. The convergence of AI-generated supply chain attacks (slopsquatting), browser-based malware assembly via malvertising (SourTrade), and the abuse of Telegram for command-and-control (TELESHIM) illustrates a threat landscape where traditional file-based detection is increasingly evaded.

Active Directory environments face a newly published privilege escalation path (Certighost) that allows low-privileged users to impersonate domain controllers, and the Fastjson 1.x deserialization flaw remains unpatched while under active exploitation. Credential stuffing and data-leak-fueled extortion (ShinyHunters, Chick-fil-A) persist at scale, while the DevMan RaaS platform demonstrates the continued industrialization of ransomware operations. Notably, AI agents themselves are becoming attack vectors: the Hermes agent was used to automate post-exploitation in a Thai government breach, and shadow AI proliferation introduces ungoverned execution surfaces across enterprises.

## Active Exploitation Details

### n8n Sandbox Escape (Expression-Sandbox Escape)
- **Description**: A high-severity sandbox escape in the n8n workflow automation platform allows an authenticated workflow editor to break out of the expression sandbox and execute arbitrary operating-system commands on the underlying server.
- **Impact**: Attackers with workflow-editor permissions—often a broad group in collaborative environments—gain full command execution as the n8n process user, enabling lateral movement, credential theft, and persistence on the automation server.
- **Status**: Patched by n8n; organizations must upgrade immediately. Exploitation requires authentication but no elevated privileges.

### Fastjson 1.x Remote Code Execution
- **Description**: A critical deserialization vulnerability in Alibaba's Fastjson 1.x Java library, exploited via malicious JSON requests in affected Spring Boot applications. Security firms ThreatBook and Imperva confirm active targeting in the wild.
- **Impact**: Unauthenticated remote code execution on any application using vulnerable Fastjson versions with default parser configurations, leading to full server compromise.
- **Status**: No official patch available for the 1.x branch at the time of reporting. Mitigation requires upgrading to Fastjson 2.x or applying parser-configuration workarounds.

### GitLab RCE (Authenticated User Command Execution)
- **Description**: A vulnerability in GitLab's self-managed instances (versions up to 18.11.3) allows authenticated users to execute arbitrary commands as the `git` system user. A proof-of-concept exploit was published on July 24, six weeks after GitLab's June 10 patch.
- **Impact**: Any authenticated user—including low-privilege project members—can achieve code execution on the GitLab server, potentially accessing source code, secrets, and CI/CD pipelines.
- **Status**: Patched in GitLab 18.11.4 and later. PoC availability increases risk for unpatched instances.

### PTC Windchill and FlexPLM Unauthenticated RCE (Cl0p Exploitation)
- **Description**: Cl0p ransomware affiliates are actively exploiting unauthenticated remote code execution flaws in internet-exposed PTC Windchill and FlexPLM deployments. The vulnerabilities enable pre-authentication command execution.
- **Impact**: Direct server compromise without credentials, facilitating ransomware deployment, data exfiltration, and lateral movement into connected OT/IT environments.
- **Status**: Actively exploited; PTC has released security advisories and patches. Immediate patching or network segmentation is critical.

### Certighost Exploit (Active Directory Privilege Escalation)
- **Description**: A working exploit (published July 24 by researchers H0j3n and Aniq Fakhrul) allows a low-privileged Active Directory user to request a certificate for a Domain Controller machine account and authenticate as that DC, effectively achieving domain admin equivalence.
- **Impact**: Full domain compromise from any standard user account in environments with vulnerable AD CS configurations (specifically, misconfigured certificate templates allowing machine-account enrollment).
- **Status**: Exploit code publicly available. Mitigation requires AD CS hardening, template reconfiguration, and monitoring for anomalous certificate requests.

### ClickFix Social Engineering Campaigns (Steam Forums & Broad)
- **Description**: Attackers abuse Steam discussion forums and other trusted platforms to post fake "fixes" that instruct victims to paste PowerShell or Run-dialog commands, deploying XMRig cryptominers and other payloads. The technique—dubbed ClickFix—relies on user-assisted execution rather than software vulnerabilities.
- **Impact**: Mass-scale malware delivery to gamers and general users; bypasses email/web gateways because the malicious instruction is hosted on legitimate, high-reputation domains.
- **Status**: Ongoing. No software patch; defense requires user awareness, script-blocking policies, and EDR behavioral detection.

### SourTrade Malvertising (Browser-Based Malware Assembly)
- **Description**: A malvertising operation (SourTrade) delivers fragmented malicious JavaScript via fake Solana, Luno, and TradingView pages. The victim's browser uses a legitimate Bun runtime to assemble and execute a Windows executable entirely in memory, never writing a complete malicious file to disk.
- **Impact**: Evades traditional AV and sandbox analysis; delivers loaders, stealers, and RATs to visitors of compromised ad networks.
- **Status**: Active campaign. Mitigation requires browser hardening, ad blockers, and runtime execution monitoring.

### BlueNoroff Zoom Phishing Kit (North Korean APT)
- **Description**: The North Korean threat group BlueNoroff operates a phishing kit impersonating Zoom and Microsoft Teams via typosquatted domains. The kit profiles victim cryptocurrency wallets before delivering tailored malware.
- **Impact**: Credential theft, wallet compromise, and targeted malware deployment against crypto-focused organizations and individuals.
- **Status**: Active infrastructure; domains continuously rotated. Attribution to DPRK-nexus actors.

### Operation BlueDash (Fake Teams Update → RMM Deployment)
- **Description**: A phishing campaign using "secure document" lures and fake Microsoft Teams update pages to trick victims into installing legitimate RMM tools (Level, ScreenConnect), granting attackers persistent remote access.
- **Impact**: Full interactive control over victim endpoints without exploiting vulnerabilities; bypasses application allowlists because the tools are digitally signed and commonly used by IT.
- **Status**: Active. Detection relies on monitoring for unauthorized RMM installations and anomalous admin-tool usage.

### Hermes AI Agent Automated Post-Exploitation
- **Description**: A threat actor used the open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation activity during an alleged breach of Thailand's Ministry of Finance.
- **Impact**: Demonstrates offensive use of autonomous AI agents for lateral movement, data discovery, and exfiltration at machine speed.
- **Status**: Single reported incident; signals emerging trend of AI-driven offensive automation.

### Hotel Wi-Fi DNS Hijacking (Microsoft 365 Phishing)
- **Description**: Attackers compromise hotel and conference-center Wi-Fi infrastructure to modify DNS responses, redirecting users to convincing fake Microsoft 365 login pages for credential harvesting.
- **Impact**: Targeted credential theft from traveling executives and government personnel; bypasses corporate network controls by attacking upstream infrastructure.
- **Status**: Ongoing campaigns reported across multiple regions.

### Cruciferra Crypter (BYOVD & Process Ghosting)
- **Description**: A China-linked cybercrime group employs the Cruciferra crypter, which combines Bring Your Own Vulnerable Driver (BYOVD) techniques with Process Ghosting to disable security agents and execute payloads stealthily on Windows.
- **Impact**: Kernel-level defense evasion and persistence; used in tax-themed phishing campaigns targeting Indian entities.
- **Status**: Active tooling observed in recent intrusions.

### TELESHIM (Telegram-Based C2 Targeting Middle East Governments)
- **Description**: An East Asia-linked threat actor uses TELESHIM malware that abuses the Telegram Bot API for command-and-control, targeting government entities in the Middle East.
- **Impact**: Covert, resilient C2 channel blending with legitimate traffic; enables long-term espionage access.
- **Status**: Active campaign; indicators of compromise published by researchers.

### DevMan Ransomware-as-a-Service Portal
- **Description**: The DevMan RaaS operation provides affiliates a web portal for payload building, victim management, and payout tracking, lowering the barrier to ransomware deployment.
- **Impact**: Accelerates ransomware proliferation; affiliates gain professional tooling without technical expertise.
- **Status**: Platform actively maintained; multiple affiliates observed.

### Slopsquatting / Phantom Domains / HalluSquatting (AI Supply Chain Attack)
- **Description**: AI coding agents hallucinate package, repository, or domain names; attackers register these "phantom" identifiers and publish malicious packages or typosquatted domains, which are then automatically pulled by downstream AI-generated code.
- **Impact**: Supply chain compromise at the point of AI-assisted development; affects npm, PyPI, GitHub, and domain registrars.
- **Status**: Emerging threat class; GitHub and PyPI have introduced time-based Dependabot cooldowns (3-day delay) as a partial mitigation.

### ShinyHunters Data Leak Sextortion Campaign
- **Description**: Threat actors leverage email addresses exposed in ShinyHunters-extorted breaches to send sextortion demands ($2,000 in Bitcoin), exploiting breach fatigue and credential reuse fears.
- **Impact**: Mass extortion leveraging verified breach data; psychological pressure increases payment rates.
- **Status**: Active spam campaigns; no technical vulnerability exploited.

### Chick-fil-A Credential Stuffing Breach
- **Description**: Credential stuffing attacks against Chick-fil-A's website and mobile app (June 17–19) compromised over 13,000 customer accounts using previously leaked credentials.
- **Impact**: Account takeover, loyalty-point theft, and potential payment-method abuse.
- **Status**: Incident contained; highlights ongoing risk of credential reuse.

### Vatican Prayer App API Exposure
- **Description**: An unauthenticated, porous API endpoint in the Vatican's official prayer app exposes names, email addresses, countries, and site status for 700,000+ global users.
- **Impact**: Mass PII leakage enabling phishing, OSINT, and targeted social engineering.
- **Status**: Disclosed; remediation status unclear at time of reporting.

### Insurance Phishing Evolution (Real-Time Account Hijacking)
- **Description**: CTM360 research documents a shift from static credential harvesting to real-time session hijacking: phishing proxies (AiTM) capture MFA tokens and session cookies, enabling immediate account takeover.
- **Impact**: Bypasses traditional MFA; attackers gain live access to financial and insurance portals.
- **Status**: Active technique adoption across financial-sector phishing kits.

## Affected Systems and Products

- **n8n Workflow Automation Platform**: All versions prior to the patched release; self-hosted and cloud deployments where workflow-editor roles are assigned.
- **Fastjson 1.x (Alibaba JSON Library for Java)**: Spring Boot applications using Fastjson 1.x with default parser settings; no patched 1.x release available.
- **GitLab Self-Managed**: Versions 18.11.3 and earlier; patched in 18.11.4+.
- **PTC Windchill & FlexPLM**: Internet-exposed instances without vendor patches applied; specific versions detailed in PTC security advisories.
- **Active Directory Certificate Services (AD CS)**: Environments with vulnerable certificate templates (e.g., `User` or `Machine` templates allowing low-privileged enrollment).
- **Steam Discussion Forums**: Platform abused for ClickFix lure hosting; no software vulnerability in Steam itself.
- **Bun JavaScript Runtime**: Legitimate runtime leveraged by SourTrade malvertising for in-browser executable assembly.
- **Level RMM & ScreenConnect**: Legitimate RMM tools weaponized via social engineering in Operation BlueDash.
- **Zoom / Microsoft Teams (Typosquatted Domains)**: Brand impersonation in BlueNoroff phishing kit; no vulnerability in legitimate applications.
- **Hotel/Conference Wi-Fi Infrastructure**: DNS configuration hijacked to serve phishing pages.
- **Hermes AI Agent (Open Source)**: Used in autonomous mode for offensive automation.
- **Cruciferra Crypter / BYOVD Drivers**: Vulnerable kernel drivers (e.g., known BYOVD-susceptible drivers) on Windows endpoints.
- **Telegram Bot API**: Abused as C2 channel by TELESHIM malware.
- **DevMan RaaS Portal**: Web-based affiliate platform for ransomware operations.
- **npm / PyPI / GitHub / Domain Registrars**: Platforms targeted by slopsquatting/phantom-package registration.
- **Chick-fil-A Web & Mobile App**: Credential stuffing target due to lack of rate limiting / bot detection at time of attack.
- **Vatican "Click To Pray" Official App**: API endpoint lacking authentication and rate controls.
- **Insurance/Financial Phishing Proxy Kits (AiTM)**: Real-time session-hijacking infrastructure.

## Attack Vectors and Techniques

- **Sandbox Escape / Expression Injection**: n8n workflow editor expressions abused to break isolation and execute OS commands.
- **Deserialization RCE (Java/Fastjson)**: Malicious JSON payloads trigger arbitrary code execution during parsing.
- **Authenticated RCE via Feature Abuse**: GitLab feature (CI/CD, import/export, or similar) allows command execution as `git` user.
- **Unauthenticated RCE (Pre-Auth)**: PTC Windchill/FlexPLM flaws exploitable without credentials.
- **AD CS Certificate Theft / Machine Account Impersonation**: Certighost exploits misconfigured templates to obtain DC certificates.
- **ClickFix / User-Assisted Execution**: Social engineering convinces victims to run attacker-supplied commands (PowerShell, `mshta`, Run dialog).
- **Malvertising / Browser-Based Malware Assembly**: Fragmented JS + legitimate runtime (Bun) builds executable in memory; no disk artifact.
- **RMM Tool Weaponization (Living Off The Land)**: Legitimate signed admin tools (Level, ScreenConnect) installed via phishing for persistent access.
- **AiTM Phishing / Real-Time Session Hijacking**: Reverse-proxy phishing kits capture MFA tokens and session cookies.
- **DNS Hijacking (Rogue AP / Compromised Infrastructure)**: Upstream DNS manipulation redirects to credential-harvesting pages.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Signed but vulnerable kernel drivers loaded to disable EDR/AV at kernel level.
- **Process Ghosting**: Executable image tampering during process creation to evade callback-based scanners.
- **Telegram Bot API C2**: Covert command channel using legitimate, encrypted messaging infrastructure.
- **AI Agent Autonomous Offensive Operations**: Open-source agents (Hermes) scripted for unattended post-exploitation.
- **Slopsquatting / Hallucination Squatting**: Registration of AI-hallucinated package/domain names for supply chain injection.
- **Credential Stuffing**: Automated login attempts using breach-compromised credential pairs.
- **Unauthenticated API Enumeration / PII Exposure**: Open endpoints leaking sensitive data without authentication.
- **Sextortion via Breach Data**: Extortion emails personalized with verified breach data to increase credibility.
- **RaaS Affiliate Portal Operations**: Centralized web platforms for payload generation, victim tracking, and cryptocurrency payout management.

## Threat Actor Activities

- **Cl0p / Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest**: Ransomware affiliate network actively exploiting PTC Windchill/FlexPLM RCE for initial access; mass-scanning internet-exposed instances.
- **BlueNoroff (North Korea / DPRK-nexus)**: Operates Zoom/Teams typosquatting phishing kit with crypto-wallet profiling; delivers tailored malware to financial/crypto targets.
- **Operation BlueDash Operators (Unattributed)**: Conducts Microsoft Teams-themed phishing to deploy Level RMM and ScreenConnect; infrastructure overlaps with other RMM-abuse campaigns.
- **Cruciferra Group (China-linked Cybercrime)**: Uses BYOVD + Process Ghosting crypter in tax-themed phishing against Indian taxpayers, tax pros, and corporate finance teams.
- **TELESHIM Actor (East Asia-linked)**: Deploys Telegram-based C2 malware against Middle East government entities; espionage-focused.
- **DevMan RaaS Operators**: Maintains affiliate portal for ransomware payload building, victim management, and payout automation; multiple active affiliates.
- **ShinyHunters (Extortion Group)**: Data breaches leaked by this group fuel downstream sextortion campaigns by other actors.
- **Hermes AI Attacker (Unattributed)**: Leveraged open-source Hermes agent in "YOLO" mode for automated post-exploitation in Thai Ministry of Finance breach.
- **Hotel Wi-Fi DNS Hijackers (Unattributed)**: Compromises hospitality Wi-Fi infrastructure for targeted Microsoft 365 credential phishing against travelers.
- **SourTrade Malvertising Operators (Unattributed)**: Runs browser-assembly malvertising campaign via fake crypto/trading sites; leverages Bun runtime.
- **Generic Credential Stuffing Actors**: Automated tooling targeting consumer-facing apps (Chick-fil-A, others) with breached credential lists.
- **Insurance/Financial Phishing Actors (Multiple)**: Adopting AiTM proxy kits for real-time session hijacking, bypassing MFA.

## Source Attribution

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
- **Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE**: The Hacker News - https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
- **DevMan RaaS Portal Centralizes Payload Builds, Victim Management, and Affiliate Payouts**: The Hacker News - https://thehackernews.com/2026/07/devman-raas-portal-centralizes-payload.html
- **OpenAI confirms ChatGPT is down worldwide**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-confirms-chatgpt-is-down-worldwide/
- **CISOs vs. Boards: Myth or Misunderstanding?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cisos-vs-boards-myth-or-misunderstanding-
- **OnTrac notifies customers of data breach after network hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/
- **Escape Artists: 'Incorrigible' AI Models Resist Rehabilitation**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/incorrigible-ai-models-resist-rehabilitation
- **Hermes AI agent used to automate attack on Thai Finance Ministry**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hermes-ai-agent-used-to-automate-attack-on-thai-finance-ministry/
- **Hackers hijack hotel Wi-Fi DNS to steal Microsoft 365 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-hijack-hotel-wi-fi-dns-to-steal-microsoft-365-accounts/
- **Microsoft blames massive Microsoft 365 outage on maintenance bug**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-blames-massive-microsoft-365-outage-on-maintenance-bug/
- **BlueNoroff Zoom Phishing Kit Profiles Crypto Wallets Before Malware Delivery**: The Hacker News - https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html
- **Certighost Exploit Lets Low-Privileged Active Directory Users Impersonate a Domain Controller**: The Hacker News - https://thehackernews.com/2026/07/certighost-exploit-lets-low-privileged.html
- **Chick-fil-A data breach affects more than 13,000 customers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/chick-fil-a-data-breach-affects-more-than-13-000-customers/
- **Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/
- **Vatican's Official Prayer App Leaks 700K+ Global Users' PII**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/vatican-official-prayer-app-leaks-700k-pii
- **Europol flags 4,340 URLs for removal in 'The Com' crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/europol-flags-4-340-urls-for-removal-in-the-com-crackdown/
