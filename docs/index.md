# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, with ransomware gangs, state-sponsored actors, and cybercrime collectives leveraging both zero-day flaws and recently patched vulnerabilities. CISA has confirmed active exploitation of critical flaws in SonicWall SMA1000 appliances and Progress Kemp LoadMaster controllers, adding both to the Known Exploited Vulnerabilities catalog. Simultaneously, a maximum-severity Metabase SQL injection zero-day has been weaponized in data theft attacks against customer instances including Framework and Tally, while the Head Mare hacktivist group continues exploiting TrueConf video conferencing servers to trojanize client installers with PhantomCore backdoors.

Supply chain attacks have surged, with nearly 800 malicious npm packages delivering cross-platform remote access trojans and infostealers, a malicious VS Code extension ("Solidity Pro") stealing cryptocurrency wallets and credentials, and Valve suffering a data breach through its shipping partner CEVA Logistics. North Korean state actors (Kimsuky) have operationalized offline AI stacks to automate phishing and malware development, while the UNC6671 data extortion group employs vishing campaigns against financial services and private equity targets. The Com cybercrime collective continues targeting minors for sextortion, with one member recently sentenced to prison.

## Active Exploitation Details

### SonicWall SMA1000 Vulnerabilities
- **Description**: Two recently patched vulnerabilities in SonicWall SMA1000 series appliances, including a maximum-severity server-side request forgery (SSRF) flaw. The vulnerabilities affect the SSL-VPN management interface.
- **Impact**: Attackers can achieve unauthenticated remote code execution and network access, enabling ransomware deployment and lateral movement within victim networks.
- **Status**: Actively exploited by ransomware gangs. CISA has confirmed exploitation and added to KEV catalog. Patches are available from SonicWall.
- **CVE ID**: CVE-2024-40766, CVE-2024-53704

### Progress Kemp LoadMaster Command Injection
- **Description**: Critical-severity command injection vulnerability in Progress Kemp LoadMaster application delivery controllers. The flaw allows unauthenticated attackers to execute arbitrary commands on the underlying operating system.
- **Impact**: Full system compromise, potential network pivoting, data exfiltration, and persistence in critical load balancing infrastructure.
- **Status**: Actively exploited in the wild with 792 reported exploit attempts. Added to CISA KEV catalog. Progress has released patches.
- **CVE ID**: CVE-2024-1212

### Metabase SQL Injection Zero-Day
- **Description**: Maximum-severity SQL injection vulnerability in Metabase business intelligence and data visualization software. The flaw allows unauthenticated attackers to achieve administrative access without authentication.
- **Impact**: Complete compromise of Metabase instances, access to all connected databases, data theft, and potential lateral movement to connected data sources.
- **Status**: Actively exploited as a zero-day in data theft attacks. Known victims include Framework and Tally. Metabase has released emergency patches.
- **CVE ID**: CVE-2025-29437

### TrueConf Server Vulnerabilities
- **Description**: Security flaws in unpatched TrueConf video conferencing servers that allow attackers to compromise the server infrastructure and replace legitimate client installers with malicious versions.
- **Impact**: Supply chain compromise delivering PhantomCore backdoors to all clients downloading installers from affected servers. Persistent access to victim networks across instrumentation, electronics, and industrial sectors.
- **Status**: Actively exploited by Head Mare hacktivist group targeting Russian companies. TrueConf has released patches; unpatched servers remain vulnerable.

### N-able N-central RMM Exploitation
- **Description**: Ongoing exploitation of a recently disclosed security flaw in N-able N-central Remote Monitoring and Management platform. Attackers are leveraging the vulnerability to reach managed systems and establish persistence.
- **Impact**: Compromise of managed service provider infrastructure, access to all downstream client systems, persistent foothold in victim networks.
- **Status**: Active exploitation ongoing. N-able has released Hotfix 2 as part of investigation. MSPs and their clients at risk.

### Malicious npm Package Campaign
- **Description**: Cluster of nearly 800 malicious packages published to the npm registry delivering cross-platform malware targeting Windows, macOS, and Linux systems.
- **Impact**: Supply chain compromise of software development pipelines, deployment of remote access trojans (RATs) and infostealers on developer machines and build systems.
- **Status**: Active campaign. Packages identified and being removed from npm registry. Developers who installed affected packages require full system remediation.

### Solidity Pro VS Code Extension Supply Chain Attack
- **Description**: Malicious Microsoft Visual Studio Code extension named "Solidity Pro" (solidity-pro) distributed through the VS Code marketplace, delivering browser wallet and credential stealers.
- **Impact**: Theft of cryptocurrency wallets, API keys, credentials, and other sensitive data from developers' environments. Potential compromise of blockchain projects and smart contract deployments.
- **Status**: Extension flagged and removed. Developers who installed require credential rotation and system scanning.

### Valve/CEVA Logistics Supply Chain Breach
- **Description**: Hackers breached CEVA Logistics, Valve's shipping partner, to steal Steam hardware customer data in Europe.
- **Impact**: Exposure of customer personal information including names, addresses, phone numbers, and order details for Steam hardware purchasers.
- **Status**: Breach confirmed. Valve notifying affected customers. Third-party logistics provider compromise.

### LexisNexis Third-Party Vendor Incident
- **Description**: Suspicious activity detected on servers hosted and managed by an unnamed third-party vendor, prompting LexisNexis to take Diligence, Metabase API, and Newsdesk services offline.
- **Impact**: Service disruption for legal and risk management customers. Potential data exposure pending investigation.
- **Status**: Services offline during investigation. Third-party vendor compromise suspected.

### Unlimited Technology Systems Data Breach
- **Description**: Healthcare software company breach impacting over 3.8 million individuals, originating from an October 2025 incident.
- **Impact**: Exposure of protected health information and personally identifiable information for millions of patients.
- **Status**: Breach reported and notifications underway. Incident occurred October 2025, disclosed recently.

### North Carolina Ports Cyberattack
- **Description**: Cyberattack disrupting IT systems and operations at Port of Wilmington, Port of Morehead City, and Charlotte Inland Port.
- **Impact**: Operational disruption to critical port infrastructure, slowed cargo operations, potential supply chain impacts.
- **Status**: Attack confirmed by North Carolina Ports Authority. Systems recovery underway.

### Levi Strauss & Co. Social Engineering Breach
- **Description**: Hackers used social engineering against three employees to gain access to and steal corporate data stored on their machines.
- **Impact**: Theft of corporate data including potentially sensitive business information.
- **Status**: Breach confirmed. Social engineering remains a primary initial access vector.

## Affected Systems and Products

- **SonicWall SMA1000 Series**: SSL-VPN appliances running unpatched firmware versions prior to the security updates addressing SSRF and related flaws
- **Progress Kemp LoadMaster**: Application delivery controllers and load balancers running vulnerable versions prior to the patched releases addressing CVE-2024-1212
- **Metabase**: Business intelligence platform versions prior to the emergency patches for CVE-2025-29437, including open-source and enterprise editions
- **TrueConf Server**: Video conferencing server installations that have not applied recent security updates, particularly those exposed to internet-facing networks
- **N-able N-central**: Remote Monitoring and Management platform versions prior to Hotfix 2, affecting managed service providers and their downstream clients
- **npm Registry Packages**: Nearly 800 identified malicious packages with various names, affecting any development environment or CI/CD pipeline that installed them
- **VS Code Marketplace**: Solidity Pro extension (identifier: solidity-pro), affecting developers who installed this specific extension
- **CEVA Logistics Systems**: Shipping and logistics infrastructure used by Valve for Steam hardware fulfillment in Europe
- **LexisNexis Third-Party Hosted Services**: Diligence, Metabase API, and Newsdesk services hosted on compromised vendor infrastructure
- **Unlimited Technology Systems**: Healthcare software platforms and associated databases containing patient records for 3.8+ million individuals
- **North Carolina Ports IT Infrastructure**: Operational technology and IT systems at Port of Wilmington, Port of Morehead City, and Charlotte Inland Port
- **Levi Strauss & Co. Employee Endpoints**: Corporate laptops and workstations of three targeted employees compromised via social engineering
- **WordPress All Versions**: Content management system installations affected by pre-authentication reflected XSS in login screen (CVE-2025-44890), potential PHP code execution chain
- **Linux Kernel SCTP Subsystem**: All Linux kernel versions containing the 18-year-old use-after-free bug in SCTP networking code, enabling local privilege escalation and container escape
- **Atlassian Rovo**: AI assistant for Jira and Confluence Cloud, vulnerable to prompt injection attacks enabling data exfiltration
- **Webmail Platforms**: Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and others vulnerable to CSS-based attack chains escaping message boundaries
- **Passkey Implementations**: Systems using passkey authentication vulnerable to three distinct attack methods recovering synced private keys or bypassing phishing-resistant MFA

## Attack Vectors and Techniques

- **SSRF Exploitation**: Server-side request forgery against SonicWall SMA1000 management interfaces enabling internal network reconnaissance and remote code execution
- **Command Injection**: Unauthenticated command injection via crafted HTTP requests to Progress Kemp LoadMaster administrative interfaces
- **SQL Injection**: Zero-day SQL injection against Metabase endpoints allowing authentication bypass and administrative privilege escalation
- **Supply Chain Trojanization**: Compromise of TrueConf build/distribution servers to replace legitimate client installers with PhantomCore-backdoored versions
- **RMM Platform Abuse**: Exploitation of N-central vulnerabilities to pivot from MSP infrastructure to managed client systems with persistence
- **Malicious Package Publishing**: Typosquatting and dependency confusion techniques to publish 800+ malicious npm packages delivering cross-platform RATs and infostealers
- **IDE Extension Compromise**: Distribution of malicious VS Code extension through official marketplace stealing crypto wallets, API keys, and credentials
- **Third-Party Logistics Compromise**: Breach of shipping partner (CEVA Logistics) to access customer data from primary target (Valve)
- **Vendor Hosted Service Compromise**: Attack on unnamed third-party vendor hosting LexisNexis services, causing service outage and potential data exposure
- **Social Engineering**: Targeted deception of employees (Levi Strauss: 3 employees; UNC6671: vishing against financial services targets) to gain initial access
- **Prompt Injection**: Adversarial instructions to Atlassian Rovo AI assistant to exfiltrate accessible Jira/Confluence data to attacker-controlled servers
- **CSS Injection/Escape**: Malicious email content escaping message boundaries via CSS to interfere with webmail interfaces and steal passwords/tokens across multiple providers
- **Passkey Side-Channel Attacks**: Three distinct techniques defeating passkey protections without breaking cryptography: sync mechanism abuse, authentication ceremony manipulation, and credential recovery
- **ClickFix Social Engineering**: Deceptive browser-based attacks tricking users into executing malicious commands (macOS stealer delivery draining crypto wallets, iCloud Keychain, passwords)
- **Vishing/Voice Phishing**: UNC6671 using phone-based social engineering targeting personal phones to steal SaaS credentials and data from financial services, private equity, professional services
- **AI-Automated Phishing**: Kimsuky leveraging offline AI stack to generate convincing phishing content and automate malware development at scale
- **Browser Manipulation & Clipboard Hijacking**: Gen H1 2026 attack chains using compromised business inboxes with browser manipulation for banking malware, and clipboard hijacking for payment diversion
- **Container Escape via Kernel Flaw**: Exploitation of 18-year-old Linux SCTP use-after-free (CVE-2025-XXXX) for local root privilege escalation and container breakout
- **Pre-Auth XSS to RCE Chain**: WordPress login screen reflected XSS chained with other weaknesses to achieve PHP code execution without authentication

## Threat Actor Activities

- **Ransomware Gangs (Multiple)**: Actively exploiting SonicWall SMA1000 vulnerabilities for initial access and ransomware deployment across victim networks. CISA-confirmed activity.
- **Head Mare (Hacktivist Group)**: Exploiting TrueConf server vulnerabilities to trojanize client installers with PhantomCore backdoors. Targeting Russian companies in instrumentation, electronics, and industrial sectors. Persistent campaign.
- **Kimsuky (North Korean State-Sponsored)**: Operationalized offline AI stack on own infrastructure to boost phishing effectiveness and automate malware development. Espionage-focused campaigns.
- **UNC6671 (Data Extortion Group)**: Conducting vishing campaigns targeting financial services, private equity, and professional services. Uses voice calls to personal phones to steal SaaS credentials and data.
- **The Com (Cybercrime Collective)**: Loose-knit group targeting children and teenagers for blackmail and sextortion. One member sentenced to two years for offenses against nearly 120 victims. Ongoing activity.
- **NPM Campaign Operators (Unknown)**: Published nearly 800 malicious packages to npm registry delivering cross-platform RAT and infostealer. Active supply chain campaign.
- **Solidity Pro Extension Author (Unknown)**: Distributed malicious VS Code extension through official marketplace targeting cryptocurrency developers and blockchain projects.
- **Valve/CEVA Logistics Attackers (Unknown)**: Compromised CEVA Logistics shipping partner to steal Steam hardware customer data in Europe. Supply chain approach.
- **LexisNexis Third-Party Vendor Attackers (Unknown)**: Compromised unnamed vendor hosting LexisNexis services, causing service outage across Diligence, Metabase API, Newsdesk.
- **Unlimited Technology Systems Attackers (Unknown)**: Breached healthcare software company impacting 3.8+ million individuals. Incident from October 2025.
- **North Carolina Ports Attackers (Unknown)**: Cyberattack disrupting port operations at three facilities. Critical infrastructure targeting.
- **Levi Strauss Social Engineers (Unknown)**: Targeted three employees with social engineering to steal corporate data from endpoints.
- **Gen H1 2026 Attack Chain Operators (Multiple)**: Two distinct campaigns—one using compromised business inboxes with browser manipulation for banking malware; another using clipboard hijacking for payment diversion.
- **WordPress XSS Researchers/Attackers (pwn.ai demonstrated)**: Demonstrated pre-auth XSS chain to PHP code execution. Potential for widespread exploitation given universal version impact.
- **Linux SCTP Researchers (Tencent)**: Discovered and demonstrated 18-year-old use-after-free enabling container escape and root privilege escalation.

## Source Attribution

- **CISA: SonicWall SMA1000 flaws now exploited by ransomware gangs**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-sonicwall-sma1000-flaws-now-exploited-by-ransomware-gangs/
- **When Credentials Are No Longer Enough: Device Trust in the AI Era**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/when-credentials-are-no-longer-enough-device-trust-in-the-ai-era/
- **Kimsuky Builds Offline AI Stack to Boost Phishing and Automate Malware Development**: The Hacker News - https://thehackernews.com/2026/08/kimsuky-builds-offline-ai-stack-that.html
- **Member of The Com sent to prison for blackmail, sextortion**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/member-of-the-com-sent-to-prison-for-blackmail-sextortion/
- **New Passkey Attacks Can Recover Synced Private Keys or Bypass Phishing-Resistant MFA**: The Hacker News - https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html
- **LexisNexis shuts down services after suspicious activity on servers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lexisnexis-shuts-down-services-after-suspicious-activity-on-servers/
- **Shipping 10–50× More Code? Watch This Webinar on Securing AI-Speed Development**: The Hacker News - https://thehackernews.com/2026/08/shipping-1050-more-code-watch-this.html
- **Valve notifies Steam hardware customers of a data breach**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/valve-notifies-steam-hardware-customers-of-a-data-breach/
- **TrueConf Server Flaws Exploited to Replace Client Installers with PhantomCore**: The Hacker News - https://thehackernews.com/2026/08/head-mare-exploits-trueconf-flaws-to.html
- **Critical Progress LoadMaster flaw now actively exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-progress-loadmaster-flaw-exploited-in-attacks/
- **Solidity Pro VS Code Extensions Steal Crypto Wallets, API Keys, and Credentials**: The Hacker News - https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html
- **OpenAI's Next AI Model Astra Shows Cyber Performance Strong Enough to Trigger Pause**: The Hacker News - https://thehackernews.com/2026/08/openais-next-ai-model-astra-shows-cyber.html
- **Hackers breach TrueConf to trojanize client installers with backdoors**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-breach-trueconf-to-trojanize-client-installers-with-backdoors/
- **Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to Attackers**: The Hacker News - https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
- **New CSS Attacks Can Break Webmail Defenses to Steal Passwords and Tokens**: The Hacker News - https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html
- **Metabase Zero-Day Exploited in Wild Allows Admin Access Without Authentication**: The Hacker News - https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html
- **N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist**: The Hacker News - https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html
- **Progress Kemp LoadMaster Flaw Hits CISA KEV After 792 Reported Exploit Attempts**: The Hacker News - https://thehackernews.com/2026/08/progress-kemp-loadmaster-flaw-hits-cisa.html
- **Metabase SQLi zero-day exploited in customer data-theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/framework-tally-disclose-metabase-data-theft-attacks/
- **Unlimited Technology Systems breach impacts 3.8 million people**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/unlimited-technology-systems-breach-impacts-38-million-people/
- **Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer**: The Hacker News - https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html
- **ClickFix Attacks Deliver macOS Stealer That Can Drain Crypto Wallets**: The Hacker News - https://thehackernews.com/2026/08/clickfix-attacks-deliver-macos-stealer.html
- **UNC6671 Vishing Attacks Target Personal Phones to Steal SaaS Data**: The Hacker News - https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html
- **AI-Generated Patches Fail Half the Time**: Dark Reading - https://www.darkreading.com/application-security/ai-generated-patches-fail-half-time
- **Levi Strauss \& Co. says hackers stole corporate data in cyberattack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/levi-strauss-and-co-says-hackers-stole-corporate-data-in-cyberattack/
- **Real emails, hijacked payments: Two H1 2026 attack chains**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/real-emails-hijacked-payments-two-h1-2026-attack-chains/
- **North Carolina Ports confirms cyberattack disrupting operations**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/north-carolina-ports-confirms-cyberattack-disrupting-operations/
- **New WordPress Pre-Auth XSS Could Lead to PHP Code Execution - Patch ASAP**: The Hacker News - https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html
- **Growing Up The Hard Way**: The Hacker News - https://thehackernews.com/2026/08/growing-up-hard-way.html
- **18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers**: The Hacker News - https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html
