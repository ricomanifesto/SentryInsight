# Exploitation Report

## Executive Summary

CISA has added two critical actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog this week, mandating emergency patching for federal agencies. A newly patched Microsoft SharePoint Server remote code execution zero-day (CVE-2026-58644) and two Fortinet FortiSandbox flaws are under active exploitation, while a critical Oracle E-Business Suite vulnerability also requires immediate remediation by Saturday. Separately, Zoom has released patches for a critical Windows account takeover flaw (CVE-2026-53412) affecting Zoom Workplace.

Multiple new malware families and attack frameworks are actively targeting organizations and individuals. The ClickLock macOS stealer employs a novel persistence technique that terminates user applications every 210 milliseconds until victims surrender their login credentials. The OkoBot framework delivers over 20 payloads targeting cryptocurrency wallets and credentials, while TELEPUZ malware spreads via ClickFix social engineering lures. A new Spirals ransomware operator achieved full network encryption in under 24 hours, and the Fairlife dairy subsidiary of Coca-Cola confirmed a ransomware attack halting U.S. production. Russian threat actor UAT-11795 is distributing the Starland RAT through trojanized WebEx and Zoom installers, and the China-linked Daxin malware has resurfaced in Taiwan alongside the previously undocumented Stupig pre-login SYSTEM backdoor.

Threat actor accountability advanced with the sentencing of two Scattered Spider members to 5.5 years each for the 2024 Transport for London hack causing £29 million in damage. Law enforcement also disrupted a €140 million cyber fraud ring in Spain and a Dutch investment fraud scheme exceeding €100 million. Meanwhile, the PhantomEnigma campaign compromised over 20 Brazilian government websites to serve as malware delivery channels. Emerging attack techniques include AI-focused threats: hidden text salting bypassing AI security filters in over one million phishing emails, agent data injection attacks manipulating AI agents into malicious actions, and a Claude Chrome extension flaw allowing malicious extensions to trigger unauthorized AI actions.

## Active Exploitation Details

### Microsoft SharePoint Server RCE Zero-Day (CVE-2026-58644)
- **Description**: A remote code execution vulnerability in Microsoft SharePoint Server that was exploited as a zero-day before being patched. CISA added this vulnerability to its Known Exploited Vulnerabilities (KEV) catalog on Thursday, confirming active exploitation in the wild.
- **Impact**: Attackers can achieve remote code execution on affected SharePoint Server instances, potentially leading to full server compromise, data exfiltration, and lateral movement within organizational networks.
- **Status**: Actively exploited; patched by Microsoft; CISA KEV catalog addition mandates federal agency remediation.
- **CVE ID**: CVE-2026-58644

### Fortinet FortiSandbox Actively Exploited Vulnerabilities
- **Description**: Two vulnerabilities in the Fortinet FortiSandbox threat detection platform that CISA has confirmed are under active exploitation. CISA ordered federal civilian executive branch agencies to prioritize patching.
- **Impact**: Exploitation of these flaws could allow attackers to compromise the threat detection platform itself, potentially bypassing security controls, accessing sandboxed malware samples, or using the appliance as a pivot point for further network intrusion.
- **Status**: Actively exploited; patches available; CISA emergency directive issued for federal agencies.

### Oracle E-Business Suite Critical Vulnerability
- **Description**: A critical vulnerability in Oracle E-Business Suite financial application that CISA has confirmed is being actively exploited in ongoing attacks. CISA ordered federal agencies to secure their systems by Saturday.
- **Impact**: Successful exploitation could compromise financial systems, leading to unauthorized access to sensitive financial data, fraudulent transactions, or disruption of critical financial operations.
- **Status**: Actively exploited; emergency patching mandated for federal agencies by Saturday deadline.

### Zoom Workplace for Windows Account Takeover (CVE-2026-53412)
- **Description**: A critical security flaw in Zoom Workplace for Windows that could facilitate account takeover. Zoom has released security updates addressing this vulnerability.
- **Impact**: Attackers could potentially take over user accounts, gaining access to meetings, recordings, chat history, and potentially using compromised accounts for further social engineering or lateral movement.
- **Status**: Patched by Zoom; CVE assigned with critical CVSS score.
- **CVE ID**: CVE-2026-53412

### n8n Token Exchange Flaw
- **Description**: A vulnerability in the n8n workflow automation platform's enterprise instances configured to trust multiple external token issuers. The flaw causes improper JWT matching, allowing an incoming token from one issuer to be matched to a local user account associated with a different issuer.
- **Impact**: Attackers could authenticate as users from another trusted identity provider, achieving unauthorized access to n8n workflows, credentials, and automation logic.
- **Status**: Vulnerability disclosed; affects enterprise instances with multi-issuer configurations.

### Claude Chrome Extension Flaw
- **Description**: A flaw in Anthropic's Claude for Chrome browser extension that allows a malicious extension to trigger predefined AI actions by simulating user clicks.
- **Impact**: Malicious extensions could abuse Claude's access to perform unauthorized AI actions, potentially accessing sensitive data, executing commands, or manipulating browser content through the AI assistant's capabilities.
- **Status**: Vulnerability disclosed; affects Claude Chrome extension users.

### Unpatched Shark Robot Vacuum Flaw
- **Description**: An unpatched vulnerability in Shark RV2320EDUS robot vacuums where extracting the certificate from the device flash allows attackers to run root commands on other Shark vacuums across the same AWS region.
- **Impact**: Attackers can remotely control other users' vacuums, access camera feeds, drive the robots, and read device data across an entire AWS region.
- **Status**: Unpatched; no vendor fix available at time of reporting.

## Affected Systems and Products

- **Microsoft SharePoint Server**: Versions affected by CVE-2026-58644; on-premises SharePoint Server deployments
- **Fortinet FortiSandbox**: Threat detection platform appliances; specific versions affected by the two actively exploited flaws
- **Oracle E-Business Suite**: Financial application modules; versions containing the critically exploited vulnerability
- **Zoom Workplace for Windows**: Versions prior to the security update addressing CVE-2026-53412
- **n8n Workflow Automation Platform**: Enterprise instances configured with multiple external token issuers (OIDC/SAML)
- **Anthropic Claude Chrome Extension**: Browser extension installations; all versions prior to fix
- **Shark RV2320EDUS Robot Vacuum**: IoT device; all firmware versions (unpatched)
- **macOS Systems**: Targeted by ClickLock info-stealer malware; all versions supporting the Terminal-based attack vector
- **Windows Systems**: Targeted by Spirals ransomware, OkoBot framework, TELEPUZ malware, and Starland RAT
- **Brazilian Government Websites**: Over 20 hijacked sites used as malware delivery channels in PhantomEnigma campaign
- **Transport for London (TfL) Infrastructure**: Compromised in 2024 Scattered Spider attack
- **Fairlife (Coca-Cola) Dairy Production Systems**: Ransomware-affected operational technology and IT systems
- **23andMe Genetic Data Platform**: Breached customer genetic data leading to $18 million settlement

## Attack Vectors and Techniques

- **ClickLock Credential Coercion**: Malware terminates all visible user processes every 210 milliseconds in an infinite loop, forcing victims to enter their system login password to regain control. Delivered via command pasted into Terminal.
- **ClickFix Social Engineering**: TELEPUZ malware spreads via websites infected with ClickFix lures that trick users into executing malicious PowerShell commands under the guise of fixing a system issue.
- **Trojanized Legitimate Software**: Russian threat actor UAT-11795 distributes Starland RAT through modified WebEx and Zoom installers, stealing credentials and cryptocurrency.
- **Hidden Text Salting (Text Injection)**: Over one million phishing emails use invisible Unicode characters and CSS manipulation to poison AI/ML security filter analysis while displaying clean text to human recipients.
- **Agent Data Injection**: Attackers plant malicious instructions in data sources (product reviews, GitHub threads, documentation) that AI agents consume, causing the agents to execute attacker-controlled actions like clicking "Buy Now" or applying malicious code changes.
- **Multi-Payload Framework Deployment**: OkoBot delivers 20+ distinct payloads in a single infection chain, targeting cryptocurrency wallet seed phrases, browser credentials, system information, and persistent access mechanisms.
- **Rapid Ransomware Encryption**: Spirals ransomware achieves initial access through data exfiltration and full network encryption in under 24 hours, minimizing defender response windows.
- **Government Website Compromise for Malware Delivery**: PhantomEnigma campaign hijacked 20+ Brazilian government websites to serve as trusted distribution points for malware payloads.
- **Pre-Login SYSTEM Backdoor**: Stupig backdoor achieves SYSTEM-level persistence before user login, surviving reboots and providing early-boot access to compromised Taiwan manufacturing firm systems.
- **JWT Issuer Confusion**: n8n token exchange flaw allows cross-issuer authentication bypass in multi-tenant enterprise configurations.
- **AI Extension Click Simulation**: Malicious Chrome extensions simulate user clicks on Claude extension UI to trigger unauthorized AI actions without user consent.
- **Investment Fraud Money Laundering**: Large-scale cyber-enabled investment fraud ("pig butchering") schemes laundering tens of millions through complex financial networks across multiple jurisdictions.

## Threat Actor Activities

- **Scattered Spider (UNC3944/0ktapus)**: Two members (Owen Flowers, 18, and Thalha Jubair, 20) sentenced to 5.5 years each for the 2024 Transport for London hack causing £29 million in damage and disrupting services for 148 stations. The group specializes in social engineering, SIM swapping, and cloud identity attacks.
- **UAT-11795 (Russian Financially Motivated Actor)**: Distributing Starland RAT via trojanized WebEx and Zoom application installers. Targets credentials and cryptocurrency wallets. Operates through software supply chain compromise of legitimate communication tools.
- **Daxin/China-Linked APT**: Advanced malware previously attributed to Chinese threat actors resurfaced after four years in a Taiwan manufacturing firm. Deployed alongside the novel Stupig pre-login SYSTEM backdoor, indicating sophisticated persistent access capabilities.
- **PhantomEnigma**: Active campaign compromising 20+ Brazilian government websites to convert them into malware delivery channels. Leverages trust in government domains for payload distribution. Identified by ANY.RUN interactive malware analysis.
- **Spirals Ransomware Group**: New ransomware actor demonstrating extreme operational speed—completing corporate intrusion from initial access through data theft to full encryption in under 24 hours.
- **OkoBot Operators**: Deploying modular framework with 20+ payloads focused on cryptocurrency theft, credential harvesting, and data exfiltration. Framework design suggests organized development and affiliate distribution model.
- **ClickLock Developers**: Created novel macOS info-stealer using aggressive process termination loop for credential coercion. Terminal-based delivery suggests targeted or social engineering-driven distribution.
- **TELEPUZ Operators**: Utilizing ClickFix technique for initial access since late April 2026. Modular malware with data theft and command execution capabilities.
- **Spanish Cyber Fraud Ring (Iberian Hackers)**: Disrupted by police after conducting varied cyberattacks and laundering €140 million through complex financial networks.
- **Dutch Investment Fraud Network**: International scheme with tens of thousands of victims and over €100 million stolen. Multiple arrests by Dutch Police.
- **U.S. Investment Fraud Launderers**: Two individuals charged in New York for laundering $43 million stolen in cyber investment fraud scams ("pig butchering" operations).

## Source Attribution

- **US charges two over laundering $43 million from investment fraud**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-two-over-laundering-43-million-from-investment-fraud/
- **CISA urges immediate action on actively exploited Fortinet flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV**: The Hacker News - https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **New ClickLock macOS malware traps users into revealing login password**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/
- **Coca-Cola says Fairlife ransomware attack halts US dairy production**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production/
- **Agentic AI Is Untamable: Ask the Right Security Questions**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/agentic-ai-untamable-ask-the-right-security-questions
- **1M+ Emails Use Hidden Text to Dupe AI Security Filters**: Dark Reading - https://www.darkreading.com/threat-intelligence/1m-emails-hidden-text-dupe-ai-security-filters
- **Claude Chrome extension flaw lets malicious extensions trigger AI actions**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/claude-chrome-extension-flaw-lets-malicious-extensions-trigger-ai-actions/
- **New OkoBot framework deploys 20 payloads to steal data, crypto**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-okobot-framework-deploys-20-payloads-to-steal-data-crypto/
- **Two Scattered Spider Hackers Get 5.5 Years Each for £29 Million TfL Hack**: The Hacker News - https://thehackernews.com/2026/07/two-scattered-spider-hackers-get-55.html
- **ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html
- **AI Agents Broke the Security Playbook. Here's What Replaces It.**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ai-agents-broke-the-security-playbook-heres-what-replaces-it/
- **23andMe to pay $18 million in new genetics data breach settlement**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/23andme-to-pay-18-million-in-new-genetics-data-breach-settlement/
- **n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer**: The Hacker News - https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html
- **New TELEPUZ Malware Spreads via ClickFix to Steal Data and Run Commands**: The Hacker News - https://thehackernews.com/2026/07/new-telepuz-malware-spreads-via.html
- **New ClickLock macOS Stealer Kills Apps Every 210ms Until Victims Type Their Password**: The Hacker News - https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html
- **Scattered Spider members behind TfL hack get five years in prison**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison/
- **Windows 11 24H2 Home and Pro reach end of support in 90 days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-11-24h2-home-and-pro-reach-end-of-support-in-90-days/
- **20+ Hijacked Government Websites Became an Attack Channel**: The Hacker News - https://thehackernews.com/2026/07/20-hijacked-government-websites.html
- **New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands**: The Hacker News - https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html
- **Daxin Resurfaces in Taiwan Alongside Stupig Pre-Login SYSTEM Backdoor**: The Hacker News - https://thehackernews.com/2026/07/daxin-resurfaces-in-taiwan-alongside.html
- **CISA orders feds to patch actively exploited Oracle flaw by Saturday**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-flaw-by-saturday/
- **Russian hackers trojanize WebEx, Zoom apps to push Starland malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/russian-hackers-trojanize-webex-zoom-apps-to-push-starland-malware/
- **AI Can Find Bugs, But Human Knowledge Still Proves Them**: The Hacker News - https://thehackernews.com/2026/07/ai-can-find-bugs-but-human-knowledge.html
- **New Spirals ransomware encrypts victim network in under 24 hours**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-spirals-ransomware-encrypts-victim-network-in-under-24-hours/
- **Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide**: The Hacker News - https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html
- **OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol**: The Hacker News - https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html
- **Zoom Patches Critical Windows Flaw That Could Enable Account Takeover**: The Hacker News - https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html
- **Police Disrupt a €140M Cyber Fraud Ring in Spain**: Dark Reading - https://www.darkreading.com/threat-intelligence/police-disrupt-140m-euro-cyber-fraud-ring-spain
- **Dutch police bust investment fraud ring stealing over €100 million**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/dutch-police-bust-investment-fraud-ring-stealing-over-100-million/
