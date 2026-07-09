# Exploitation Report

## Executive Summary

Active exploitation campaigns are intensifying across multiple vectors, with threat actors leveraging both newly disclosed vulnerabilities and mature attack techniques enhanced by artificial intelligence. China-linked threat cluster UAT-7810 is actively exploiting vulnerable Roundcube webmail servers at academic institutions across the United States and Canada while simultaneously expanding its Operational Relay Box (ORB) network through the novel LONGLEASH malware targeting unpatched networking devices. CISA has issued emergency directives for federal agencies to patch actively exploited flaws in Langflow, Adobe ColdFusion, and other platforms, underscoring the immediacy of the threat landscape.

Financially motivated operations are diversifying their delivery mechanisms, combining malvertising campaigns distributing Vidar Infostealer with sophisticated social engineering such as Entra passkey enrollment vishing and ClickFix lures deployed by the SCMBANKER banking malware targeting Mexican financial institutions. Supply chain attacks via typosquatted packages on npm and PyPI continue to harvest credentials from developers using payment platforms, while a new "ghost phishing" technique employed by the EvilTokens campaign evades traditional email security controls. The emergence of AI-assisted intrusion—exemplified by a lone attacker breaching an AWS environment in 72 hours using chained cloud weaknesses and AI workflows—signals a shift in adversary capability and speed.

## Active Exploitation Details

### Roundcube Webmail Vulnerability Exploitation
- **Description**: A China-linked threat cluster is exploiting vulnerable Roundcube webmail servers deployed at universities in the United States and Canada to steal credentials and deploy backdoor malware for persistent access.
- **Impact**: Credential theft, persistent backdoor deployment, and espionage targeting academic researchers.
- **Status**: Actively exploited in the wild; patches available but unpatched instances remain targets.

### Langflow Authentication Bypass Flaw
- **Description**: An authentication bypass vulnerability in the Langflow visual framework for building AI agents that allows unauthorized access to the application.
- **Impact**: Full compromise of Langflow instances, potential access to AI agent workflows and data.
- **Status**: Actively exploited; CISA ordered federal agencies to patch immediately via emergency directive.

### Adobe ColdFusion Maximum-Severity Flaw
- **Description**: A critical vulnerability in Adobe ColdFusion commercial web application development platform.
- **Impact**: Remote code execution and complete server compromise.
- **Status**: Actively exploited; CISA mandated federal patching by Friday deadline.

### Ubiquiti UniFi OS Command Injection Vulnerability
- **Description**: A maximum-severity command injection flaw in UniFi OS affecting UniFi Connect, Talk, Access, Protect, and OS platforms.
- **Impact**: Unauthenticated remote code execution leading to full device compromise and privilege escalation.
- **Status**: Actively exploited; Ubiquiti released security updates for seven critical vulnerabilities including this flaw.

### GhostLock Linux Kernel Flaw (CVE-2026-43499)
- **Description**: A 15-year-old Linux kernel vulnerability (CVE-2026-43499) that allows any logged-in user to achieve full root control and escape containers on unpatched systems.
- **Impact**: Local privilege escalation to root, container escape, complete host compromise on most Linux distributions.
- **Status**: Publicly disclosed with proof-of-concept; patches available for affected kernel versions.
- **CVE ID**: CVE-2026-43499

### CISA KEV Additions: Four Actively Exploited Flaws
- **Description**: CISA added four security flaws affecting Adobe, Joomla, and Langflow products to the Known Exploited Vulnerabilities catalog based on evidence of active exploitation.
- **Impact**: Varies by vulnerability; includes remote code execution, authentication bypass, and data exposure.
- **Status**: Actively exploited; federal agencies required to remediate per Binding Operational Directive 22-01.

## Affected Systems and Products

- **Roundcube Webmail**: Self-hosted webmail deployments at academic institutions in the U.S. and Canada; versions prior to security patches addressing the exploited flaw.
- **Langflow**: Visual framework for building AI agents; all unpatched instances exposed to the authentication bypass vulnerability.
- **Adobe ColdFusion**: Commercial web application development platform; versions affected by the maximum-severity actively exploited flaw.
- **Ubiquiti UniFi Ecosystem**: UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS; devices running firmware prior to the July 2026 security updates.
- **Linux Kernel**: Most Linux distributions running kernel versions vulnerable to GhostLock (CVE-2026-43499); affects containerized environments and multi-tenant systems.
- **Joomla CMS**: Installations affected by the actively exploited flaw added to CISA KEV catalog.
- **npm and PyPI Package Repositories**: Developers and users of Paysafe, Skrill, and Neteller payment applications who installed typosquatted malicious SDK packages.
- **Microsoft 365 / Entra ID**: Organizations across multiple sectors targeted by passkey enrollment vishing campaigns.
- **Networking Devices**: Internet-facing routers, firewalls, and edge devices—particularly unpatched Ruijie and other vendor equipment—targeted for ORB network recruitment.

## Attack Vectors and Techniques

- **AI-Assisted Cloud Intrusion**: Attacker chained AI workflows, cloud misconfigurations, and stolen credentials to breach an AWS environment and extort a large Amazon customer within 72 hours.
- **Malvertising with Vidar Infostealer**: Financially motivated actors use lures for cracked/pirated software to deliver Vidar infostealer combined with cryptominers via malicious advertisements.
- **Supply Chain Typosquatting**: Malicious packages mimicking legitimate Paysafe, Skrill, and Neteller SDKs published to npm and PyPI deliver credential-stealing malware to developers.
- **Entra Passkey Enrollment Vishing**: Voice-based social engineering impersonating security requests tricks Microsoft 365 users into enrolling attacker-controlled passkeys, bypassing MFA.
- **ClickFix Social Engineering**: SCMBANKER operators use fake verification prompts (ClickFix lures) to execute malicious PowerShell commands targeting Mexican banking, fintech, and cryptocurrency users.
- **Ghost Phishing / EvilTokens Campaign**: Malicious pages remain hidden until decryption at runtime, evading static email security analysis and targeting businesses in the US and Europe.
- **HalluSquatting**: AI coding assistants hallucinate non-existent package names; attackers register these names to deliver botnet malware when the assistant recommends them.
- **ORB Network Expansion via LONGLEASH**: Custom malware (LONGLEASH) compromises internet-facing networking devices to expand Operational Relay Box infrastructure for traffic obfuscation.
- **GitHub Commit Signature Bypass**: Researchers demonstrated that signed Git commit hashes can be rewritten into new hashes without breaking signatures, undermining supply chain trust.
- **GitHub Copilot Safety Bypass**: Harmful requests refused in chat interface are executed when decomposed into small steps within the code editor context.

## Threat Actor Activities

- **UAT-7810 (China-Linked)**: Actively exploiting Roundcube servers at U.S. and Canadian universities for credential theft and backdoor deployment; developing and deploying LONGLEASH malware to compromise networking devices and expand ORB network infrastructure for operational obfuscation.
- **SCMBANKER Operators**: Conducting banking fraud campaigns targeting customers of Mexican banks, fintechs, payment processors, and cryptocurrency exchanges using ClickFix social engineering lures; tracked by Elastic Security.
- **EvilTokens Campaign**: Executing "ghost phishing" attacks against businesses in the US and Europe using novel evasion techniques that decrypt malicious content at runtime to bypass email security gateways.
- **Vidar Infostealer Operators**: Running malvertising campaigns delivering Vidar infostealer and cryptominers via pirated software lures, heavily impacting SMBs.
- **Lone AWS Attacker**: Single operator leveraged AI tooling, cloud misconfigurations, and credential theft to breach and extort a major Amazon Web Services customer in 72 hours.
- **Accenture Breach Actor**: Unnamed threat actor claimed theft of 35 GB of source code and data from Accenture; offered for sale on underground forums.
- **KDDI Breach Actors**: Unidentified attackers breached an email platform used by five Japanese ISPs, exposing email addresses and passwords of over 12 million individuals.
- **Mount Royal University Attackers**: Hackers breached the university network, exfiltrated and deleted data from file storage systems; claimed responsibility publicly.

## Source Attribution

- **Mexico's New Cyber Plan Faces Its First Real Test**: Dark Reading - https://www.darkreading.com/cyber-risk/mexicos-cyber-plan-first-real-test
- **Mount Royal University confirms breach as hackers claim attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/mount-royal-university-confirms-breach-as-hackers-claim-attack/
- **Lone Attacker Uses AI to Breach AWS Cloud Environment in 72 Hours**: Dark Reading - https://www.darkreading.com/cloud-security/lone-attacker-ai-breach-aws-cloud-environment
- **Fake Paysafe, Skrill SDKs on NPM and PyPi steal credentials**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fake-paysafe-skrill-sdks-on-npm-and-pypi-steal-credentials/
- **Hackers exploit Roundcube flaw to spy on academic researchers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-exploit-roundcube-flaw-to-spy-on-academic-researchers/
- **AI Coding Agents Found Triggering Endpoint Security Rules Built to Catch Attackers**: The Hacker News - https://thehackernews.com/2026/07/ai-coding-agents-found-triggering.html
- **Entra passkey enrollment vishing targets Microsoft 365 users**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/entra-passkey-enrollment-vishing-targets-microsoft-365-users/
- **Vidar Infostealer Hammers SMBs via Malvertising Campaign**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/vidar-infostealer-smb-malvertising-campaign
- **New HalluSquatting Attack Could Trick AI Coding Assistants Into Installing Botnet Malware**: The Hacker News - https://thehackernews.com/2026/07/new-hallusquatting-attack-could-trick.html
- **Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS**: The Hacker News - https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html
- **3 Ways AI Powers Service Desk Attacks and How to Prevent Them**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/3-ways-ai-powers-service-desk-attacks-and-how-to-prevent-them/
- **New Ghost Phishing Wave Is Breaking Traditional Email Security**: The Hacker News - https://thehackernews.com/2026/07/new-ghost-phishing-wave-is-breaking.html
- **SCMBANKER Malware Uses ClickFix Lures to Target Mexican Banking Users**: The Hacker News - https://thehackernews.com/2026/07/scmbanker-malware-uses-clickfix-lures.html
- **Felons, Fraudsters Flog Offensive Cybersecurity Startup**: Krebs on Security - https://krebsonsecurity.com/2026/07/felons-fraudsters-flog-offensive-cybersecurity-startup/
- **DuckDuckGo browser now blocks YouTube video ads**: Bleeping Computer - https://www.bleepingcomputer.com/news/software/duckduckgo-browser-now-blocks-youtube-video-ads/
- **GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures**: The Hacker News - https://thehackernews.com/2026/07/github-verified-commits-can-be.html
- **The Verification Step Is the New ATO Battleground in 2026**: The Hacker News - https://thehackernews.com/2026/07/the-verification-step-is-new-ato.html
- **Telco giant KDDI says data breach affects over 12 million people**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/japanese-telecom-giant-kddi-says-data-breach-affects-12-million-people/
- **GitHub Copilot Refuses Harmful Requests in Chat, Then Writes Them in Code**: The Hacker News - https://thehackernews.com/2026/07/github-copilot-refuses-harmful-requests.html
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
