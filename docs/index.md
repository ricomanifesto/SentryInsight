# Exploitation Report

## Executive Summary

Critical exploitation activity this period centers on actively exploited zero-day vulnerabilities in widely deployed Joomla extensions, with CISA confirming remote code execution flaws in iCagenda and Balbooa Forms are being weaponized in the wild. Simultaneously, supply chain attacks have surged across the npm ecosystem, where 148 malicious packages disguised as student proxies ensnared browsers into a DDoS botnet and a backdoored Jscrambler package delivered infostealer malware to nearly 1,500 downstream consumers. These campaigns demonstrate the growing potency of software supply chain compromise as an initial access vector.

Threat actor infrastructure continues to evolve with the emergence of Forg365, a new phishing-as-a-service platform combining device code phishing, adversary-in-the-middle session theft, and AI-assisted evasion to target Microsoft 365 environments. The ShinyHunters data extortion group has maintained a year-long campaign against Salesforce instances, leveraging configuration weaknesses rather than platform vulnerabilities. On the destructive front, the modular GigaWiper malware provides operators flexible wiper and backdoor capabilities, while CrashStealer macOS malware abuses a notarized dropper to bypass Gatekeeper and harvest credentials, keychain data, and cryptocurrency wallets.

Nation-state activity remains prominent, with Russian GRU actors and associated infrastructure targeting critical infrastructure across the U.S. and allied nations through vulnerable router exploitation. The U.S., UK, and EU have responded with coordinated sanctions against Russian military hackers, VPN providers, and malware cryptor services enabling ransomware operations. Notably, a misconfigured attacker server exposed three active Evilginx phishing operations targeting Microsoft 365, and suspected AI-generated PowerShell scripts are now being used for Active Directory reconnaissance, signaling adversarial adoption of generative AI for offensive operations.

## Active Exploitation Details

### iCagenda and Balbooa Forms Joomla Extensions RCE
- **Description**: Two maximum-severity remote code execution vulnerabilities affecting the iCagenda and Balbooa Forms extensions for the Joomla content management system. The flaws allow unauthenticated attackers to execute arbitrary code on vulnerable Joomla installations.
- **Impact**: Full compromise of affected Joomla servers, enabling attackers to deploy webshells, exfiltrate data, pivot to internal networks, and establish persistent access.
- **Status**: Actively exploited in the wild as zero-days. CISA has added both vulnerabilities to its Known Exploited Vulnerabilities catalog, mandating federal agencies to remediate immediately. Patches are available from the extension vendors.
- **CVE ID**: Not specified in source articles

### 148 Malicious npm Packages (Student Proxy Campaign)
- **Description**: A coordinated supply chain campaign publishing 148 npm packages masquerading as student web proxy utilities. When installed or executed, the packages instrumented visitors' browsers to participate in a distributed denial-of-service botnet.
- **Impact**: Compromised browsers were commandeered for DDoS attacks against targets selected by the operators. The campaign operated for approximately two weeks in May before detection.
- **Status**: Packages have been identified and reported by JFrog research. npm has removed the malicious packages. Organizations should audit dependencies and monitor for suspicious outbound traffic from development and CI/CD environments.

### Jscrambler npm Package Supply Chain Attack
- **Description**: Threat actors published a malicious version (v8.3.0) of the legitimate Jscrambler client-side security npm package containing infostealer malware. The backdoored package was downloaded nearly 1,500 times before detection.
- **Impact**: Compromised development environments and build systems, with the infostealer capable of harvesting credentials, tokens, and sensitive project data from affected machines.
- **Status**: Jscrambler disclosed the incident and published a clean version. The malicious package has been removed from npm. Affected organizations should rotate all credentials exposed in compromised environments.

### CrashStealer macOS Information Stealer
- **Description**: A new macOS malware family masquerading as Apple's crash reporting tool (crashreporterd). The malware uses a notarized dropper to pass Gatekeeper checks, then deploys a payload that harvests credentials, keychain data, browser cookies, and cryptocurrency wallet information.
- **Impact**: Full compromise of user sensitive data on macOS systems, including authentication tokens for cloud services, financial credentials, and crypto assets.
- **Status**: Actively distributed. The notarized dropper indicates the attackers either compromised a valid Apple Developer ID or abused the notarization process. No patch available; detection relies on endpoint security and behavioral analysis.

### GigaWiper Modular Destructive Malware
- **Description**: A modular implant combining backdoor functionality with configurable wiper capabilities. The malware borrows code from multiple known families and allows operators to select destruction parameters at deployment time.
- **Impact**: Flexible data destruction and system sabotage tailored to target environments, with persistent backdoor access maintained until wiper execution.
- **Status**: Active threat. The modular design suggests a malware-as-a-service or shared developer infrastructure. No specific attribution in source articles.

### Forg365 Phishing-as-a-Service (PhaaS)
- **Description**: A new PhaaS platform targeting Microsoft 365 that combines device code phishing (abusing the OAuth device authorization flow), adversary-in-the-middle (AitM) session token theft, antibot evasion techniques, and AI-assisted content generation.
- **Impact**: Bypasses multi-factor authentication by stealing valid session tokens, enabling full account takeover of Microsoft 365 tenants including Exchange, SharePoint, and Teams data.
- **Status**: Actively operated and advertised in underground markets. No patch; mitigation requires conditional access policies, phishing-resistant MFA (FIDO2/WebAuthn), and user education.

### Evilginx Phishing Operations Targeting Microsoft 365
- **Description**: Three distinct phoking campaigns using the Evilginx AitM framework were exposed via a misconfigured Python HTTP server with directory listing enabled. The campaigns targeted Microsoft 365 credentials and session tokens.
- **Impact**: Credential harvesting and session hijacking for Microsoft 365 accounts, with potential for business email compromise and data exfiltration.
- **Status**: Infrastructure exposed and likely burned. Operators will likely rotate infrastructure. Demonstrates operational security failures in active threat actor infrastructure.

### ShinyHunters Salesforce Data Extortion Campaign
- **Description**: A year-long campaign by the ShinyHunters data extortion group targeting corporate Salesforce environments. Attackers gained access without exploiting Salesforce platform vulnerabilities, instead leveraging misconfigurations, weak authentication, and exposed credentials.
- **Impact**: Large-scale data theft from Salesforce instances including customer PII, sales records, and proprietary business data, followed by extortion demands.
- **Status**: Ongoing. Microsoft Threat Intelligence has mapped three distinct attack paths. Mitigation requires Salesforce security posture management, MFA enforcement, and credential hygiene.

## Affected Systems and Products

- **Joomla CMS with iCagenda Extension**: All versions prior to patched release; Joomla 3.x, 4.x, 5.x sites using the iCagenda event management component
- **Joomla CMS with Balbooa Forms Extension**: All versions prior to patched release; Joomla sites using Balbooa Forms builder component for Joomla Forms for form creation
- **npm Ecosystem / Node.js Projects**: Any project that installed the 148 malicious proxy packages or Jscrambler v8.3.0; affects development workstations, CI/CD pipelines, and production builds
- **macOS Systems**: macOS versions supporting notarized applications; Gatekeeper bypass via valid notarization affects all current supported macOS releases
- **Microsoft 365 Tenants**: All tenants with device code flow enabled and without phishing-resistant MFA; specifically targeted by Forg365 PhaaS and Evilginx campaigns
- **Salesforce Environments**: Organizations with misconfigured sharing settings, dormant admin accounts, weak password policies, or exposed API tokens
- **Network Infrastructure / Routers**: Vulnerable and poorly configured routers targeted by Russian state actors for critical infrastructure infiltration; specific models not disclosed in source articles
- **Windows Active Directory Environments**: Domains where AI-generated PowerShell enumeration scripts have been deployed for reconnaissance

## Attack Vectors and Techniques

- **Software Supply Chain Compromise**: Malicious code injection into legitimate npm packages (Jscrambler, 148 proxy packages) to achieve downstream execution in development and build environments
- **Remote Code Execution via Web Application Flaws**: Unauthenticated RCE in Joomla extensions (iCagenda, Balbooa Forms) enabling direct server compromise
- **Adversary-in-the-Middle (AitM) Phishing**: Evilginx and Forg365 frameworks proxying authentication flows to capture credentials and session tokens, bypassing traditional MFA
- **Device Code Phishing**: Abuse of OAuth 2.0 device authorization grant flow to trick users into authorizing attacker-controlled sessions on Microsoft 365
- **Notarized Malware Delivery**: Abuse of Apple's notarization process to distribute signed, Gatekeeper-bypassing droppers for macOS malware (CrashStealer)
- **Browser-Based DDoS Botnet**: Malicious npm packages instrumenting client browsers to participate in distributed denial-of-service attacks without traditional malware installation
- **AI-Generated Offensive Scripting**: Suspected LLM-generated PowerShell scripts used for Active Directory enumeration and domain reconnaissance
- **AI-Powered Phishing Content Generation**: Forg365 PhaaS using artificial intelligence to craft convincing phishing lures and evade detection
- **Memory/State Poisoning in AI Agents (MemGhost)**: Single malicious email planting persistent false memories in AI assistants with inbox access, causing long-term behavioral manipulation
- **Modular Wiper/Backdoor Deployment**: GigaWiper's selectable destruction modes combined with persistent access for timed or conditional sabotage
- **Critical Infrastructure Router Exploitation**: Russian state actors targeting vulnerable, misconfigured, or end-of-life routers for initial access to OT/IT networks
- **Caller ID Spoofing Platform Abuse**: Russian Coms platform enabling 1.8+ million scam calls for social engineering and fraud

## Threat Actor Activities

- **ShinyHunters (Data Extortion Group)**: Year-long campaign against Salesforce environments across multiple sectors; three distinct attack paths identified by Microsoft; focuses on data theft and extortion rather than encryption/ransomware
- **Russian GRU / Military Intelligence (APT28/Fancy Bear et al.)**: Coordinated targeting of critical infrastructure in U.S. and allied nations via vulnerable router exploitation; subject of first-ever joint UK-EU cyber sanctions package
- **Forg365 Operators (PhaaS Providers)**: Running a commercial phishing-as-a-service operation with device code, AitM, AI-assisted evasion, and antibot capabilities; advertising in underground markets
- **Evilginx Campaign Operators (Unknown/Unattributed)**: At least three distinct phishing operations targeting Microsoft 365 exposed via OPSEC failure; likely criminal credential harvesting groups
- **Jscrambler Supply Chain Attacker (Unknown/Unattributed)**: Compromised or typosquatted the Jscrambler npm publishing pipeline to inject infostealer into v8.3.0; ~1,500 downloads before detection
- **Student Proxy Campaign Operator (Unknown/Unattributed)**: Published 148 coordinated npm packages over two-week period in May; built browser-based DDoS botnet; infrastructure and attribution not disclosed
- **CrashStealer Developers (Unknown/Unattributed)**: Created macOS info-stealer with notarized dropper; capability suggests access to valid Apple Developer ID or notarization abuse
- **GigaWiper Operators (Unknown/Unattributed)**: Modular destructive malware with code overlap across multiple families; likely shared developer or MaaS model
- **Russian Coms Platform Operators (Charged by UK NCA)**: Five individuals charged for operating caller ID spoofing service used for 1.8M+ scam calls; platform enabled financial fraud and social engineering
- **VPN/Malware Cryptor Sanctioned Entities**: Two individuals and one VPN service designated by OFAC for enabling ransomware actors; specific names in OFAC designations
- **CISA Contractor (Insider/Accidental)**: Published internal CISA credentials including AWS GovCloud keys to public GitHub repository; not malicious but significant exposure

## Source Attribution

- **Microsoft starts testing cleaner Windows Search without ads**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-starts-testing-cleaner-windows-search-without-ads/
- **US sanctions VPN, malware providers for enabling ransomware attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-sanctions-vpn-malware-providers-linked-to-ransomware-gangs/
- **Grok Build Uploads Entire Git Repositories to xAI Storage, Not Just Files It Reads**: The Hacker News - https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html
- **U.S. Sanctions First VPN Service and Malware Cryptor Seller Over Ransomware Support**: The Hacker News - https://thehackernews.com/2026/07/us-sanctions-first-vpn-service-and.html
- **148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet**: The Hacker News - https://thehackernews.com/2026/07/148-npm-packages-disguised-as-student.html
- **Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity**: The Hacker News - https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
- **Weak Security Continues to Fuel Russian Cyberattacks**: Dark Reading - https://www.darkreading.com/endpoint-security/weak-security-fuel-russian-cyberattacks
- **Japan's largest taxi operator shuts systems after cyberattack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/japans-largest-taxi-operator-shuts-systems-after-cyberattack/
- **Hackers backdoor Jscrambler npm package with infostealer malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/
- **New CrashStealer malware poses as Apple crash reporting tool**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-crashstealer-malware-poses-as-apple-crash-reporting-tool/
- **'Yellow Teams' Are Defining the Future of AI Security**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/yellow-teams-defining-future-ai-security
- **CrashStealer macOS Malware Uses Notarized Dropper to Pass Gatekeeper Checks**: The Hacker News - https://thehackernews.com/2026/07/crashstealer-macos-malware-uses.html
- **Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found**: The Hacker News - https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html
- **GigaWiper Lets Threat Actors Choose Their Own Destructive Attack**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/gigawiper-threat-actors-choose-their-own-destructive-attack
- **CISA warns of actively exploited RCE flaws in Joomla extensions**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-rce-flaws-in-joomla-extensions/
- **⚡ Weekly Recap: ShareFile Threat, Citrix Bleed 2 Ransomware, AI Coding Attacks, and More**: The Hacker News - https://thehackernews.com/2026/07/weekly-recap-sharefile-threat-citrix.html
- **Lessons Learned from CISA’s Recent GitHub Leak**: Krebs on Security - https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/
- **Lidl discloses online shop breach after service provider hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lidl-discloses-online-shop-breach-after-service-provider-hack/
- **Breach at the Beach: Play the Ultimate Entra ID CTF**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/breach-at-the-beach-play-the-ultimate-entra-id-ctf/
- **New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email**: The Hacker News - https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html
- **UK charges suspects linked to Russian Coms call spoofing platform**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/uk-charges-suspects-linked-to-russian-coms-call-spoofing-platform/
- **Forg365 PhaaS Targets Microsoft 365 with Device Code and AitM Session Theft**: The Hacker News - https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
- **Turning the Tables on Email Scammers With 'ScamBuster'**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/turning-tables-email-scammers-scambuster
- **Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling**: The Hacker News - https://thehackernews.com/2026/07/meta-files-patent-for-ai-that-can.html
- **Thinking Fast and Slow in the SOC: The Case for Combining Autonomous AI with Analyst Copilots**: The Hacker News - https://thehackernews.com/2026/07/thinking-fast-and-slow-in-soc-case-for.html
- **EU sanctions Russian GRU military hackers over cyberattacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/eu-and-uk-hit-russia-with-first-joint-cyber-sanctions-package/
- **Attacker Uses Suspected AI-Generated PowerShell Script to Map Active Directory**: The Hacker News - https://thehackernews.com/2026/07/attacker-uses-suspected-ai-generated.html
- **US and allies warn of Russian critical infrastructure attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-and-allies-share-defense-tips-against-russian-hackers-targeting-critical-infrastructure/
- **Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365**: The Hacker News - https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
- **iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days**: The Hacker News - https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
