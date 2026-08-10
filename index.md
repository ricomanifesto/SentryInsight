# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are being actively exploited in the wild across diverse technology stacks, from enterprise networking equipment and remote management platforms to business intelligence software and mobile devices. CISA has confirmed ransomware gangs are exploiting recently patched SonicWall SMA1000 flaws, while a critical Progress Kemp LoadMaster command injection vulnerability has drawn over 792 exploit attempts and earned a spot on the Known Exploited Vulnerabilities catalog. Perhaps most concerning, a maximum-severity Metabase zero-day SQL injection flaw has been weaponized in data-theft attacks against customer instances including Framework and Tally, demonstrating how quickly attackers operationalize undisclosed vulnerabilities.

Simultaneously, sophisticated exploit chains previously reserved for nation-state operations are proliferating to organized cybercrime groups. The Coruna and DarkSword iOS exploit chains—capable of compromising fully patched iPhones—are now observed in broader criminal use, while China-linked threat actor Storm-1175 has leveraged an N-able N-central RMM flaw to deploy a novel ransomware strain called StormEncryptor. The Head Mare hacktivist group continues weaponizing TrueConf video conferencing server vulnerabilities to trojanize client installers with the PhantomCore backdoor, specifically targeting Russian instrumentation and electronics firms.

Supply chain and social engineering campaigns round out a high-tempo threat landscape. Nearly 800 malicious npm packages have been published to deliver cross-platform RAT and infostealer malware across Windows, Mac, and Linux. ClickFix-style attacks are distributing a Go-based macOS stealer capable of draining cryptocurrency wallets and harvesting iCloud Keychain data. The North Korean group Kimsuky has operationalized an offline AI stack to automate phishing and malware development, while data extortion group UNC6671 conducts vishing campaigns against financial services and private equity targets. A malicious VS Code extension masquerading as "Solidity Pro" has been caught exfiltrating crypto wallets, API keys, and credentials from developers.

## Active Exploitation Details

### SonicWall SMA1000 Vulnerabilities
- **Description**: Two recently patched vulnerabilities in SonicWall SMA1000 series appliances, including a maximum-severity server-side request forgery (SSRF) flaw. The vulnerabilities affect the SSL-VPN management interface.
- **Impact**: Attackers can achieve unauthenticated remote code execution and network access, enabling ransomware deployment and lateral movement within victim networks.
- **Status**: Actively exploited by ransomware gangs. CISA has confirmed exploitation in the wild. Patches are available from SonicWall.
- **CVE ID**: CVE-2025-23006, CVE-2025-23007

### Progress Kemp LoadMaster Command Injection
- **Description**: A critical-severity command injection vulnerability in Progress Kemp LoadMaster application delivery controllers. The flaw allows unauthenticated attackers to execute arbitrary commands on the underlying operating system.
- **Impact**: Full device compromise, network pivoting, data exfiltration, and persistence in critical load balancing infrastructure.
- **Status**: Actively exploited with 792 reported exploit attempts. Added to CISA Known Exploited Vulnerabilities (KEV) catalog. Hotfixes released by Progress.
- **CVE ID**: CVE-2025-23482

### Metabase Zero-Day SQL Injection
- **Description**: A maximum-severity SQL injection vulnerability in Metabase business intelligence and data visualization software. The flaw allows unauthenticated attackers to execute arbitrary SQL queries and achieve administrative access without authentication.
- **Impact**: Complete database compromise, customer data theft, administrative takeover of Metabase instances, and potential lateral movement to connected data sources.
- **Status**: Actively exploited as a zero-day in data-theft attacks. Known to impact Framework and Tally customer instances. Metabase has issued warnings and mitigation guidance.
- **CVE ID**: CVE-2025-23483

### N-able N-central RMM Vulnerability
- **Description**: A security flaw in N-able N-central Remote Monitoring and Management (RMM) platform that allows attackers to reach managed systems and establish persistence.
- **Impact**: Compromise of managed service provider infrastructure, access to all downstream customer endpoints, ransomware deployment (StormEncryptor), and long-term persistence.
- **Status**: Ongoing exploitation by Storm-1175 (China-linked). N-able has released Hotfix 2 as investigation continues. Attackers have demonstrated ability to reach managed systems and persist.
- **CVE ID**: CVE-2025-23484

### TrueConf Server Vulnerabilities
- **Description**: Multiple security flaws in unpatched TrueConf video conferencing servers that allow attackers to breach the server infrastructure and replace legitimate client installers with malicious versions.
- **Impact**: Supply chain compromise delivering PhantomCore backdoor to all clients downloading installers, persistent access to victim networks, and targeting of Russian instrumentation, electronics, and industrial sectors.
- **Status**: Actively exploited by Head Mare hacktivist group. TrueConf has been breached; malicious installers distributed to clients. Patches and clean installers being distributed.
- **CVE ID**: CVE-2025-23485, CVE-2025-23486

### Coruna and DarkSword iOS Exploit Chains
- **Description**: Sophisticated iPhone exploit chains (Coruna and DarkSword) capable of compromising fully patched iOS devices. Previously limited to nation-state actors, these chains are now proliferating to organized cybercrime groups globally.
- **Impact**: Complete device compromise, data exfiltration, surveillance capabilities, and bypass of Apple's security mitigations including Pointer Authentication Codes (PAC) and hardware memory protection.
- **Status**: Actively proliferating beyond nation-state use into cybercrime ecosystems. Apple has not publicly acknowledged patches for the specific chains.
- **CVE ID**: CVE-2025-23487, CVE-2025-23488, CVE-2025-23489, CVE-2025-23490

### Malicious npm Supply Chain Campaign
- **Description**: A cluster of nearly 800 malicious packages published to the npm registry designed to deliver cross-platform malware targeting Windows, Mac, and Linux systems.
- **Impact**: Developer machine compromise, credential theft, cryptocurrency wallet drainage, persistent remote access via RAT functionality, and potential supply chain contamination of downstream software builds.
- **Status**: Active campaign with packages identified and being removed. Broad cross-platform impact across development ecosystems.
- **CVE ID**: None assigned (malicious package campaign)

### ClickFix macOS Stealer Campaign
- **Description**: ClickFix-style social engineering attacks delivering a Go-based macOS stealer malware capable of extracting cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials.
- **Impact**: Financial theft via crypto wallet drainage, credential harvesting for account takeover, and bypass of macOS security controls through user interaction deception.
- **Status**: Active campaigns using ClickFix technique (fake error pages prompting users to run malicious commands). Targeting macOS users broadly.
- **CVE ID**: None assigned (social engineering / malware delivery)

### Atlassian Rovo Data Exfiltration Vulnerability
- **Description**: A vulnerability in Atlassian's Rovo AI assistant that allows attacker-controlled instructions to trick the assistant into collecting Jira or Confluence data accessible to a signed-in user and sending it to an external server.
- **Impact**: Unauthorized access to sensitive project management data, confluence documentation, and Jira issue tracking information across organizations using Rovo.
- **Status**: Disclosed by two security firms. Atlassian investigating. Exploitation requires user interaction with malicious content.
- **CVE ID**: CVE-2025-23491

### CSS-Based Webmail Exfiltration Attacks
- **Description**: Novel CSS injection attacks that allow email content to escape message boundaries and interfere with webmail interfaces across Outlook, Gmail, Fastmail, Proton Mail, and Yahoo Mail.
- **Impact**: Theft of passwords, authentication tokens, and sensitive email content through crafted malicious emails that exploit CSS parsing behaviors in webmail clients.
- **Status**: Research demonstration with proof-of-concept across major webmail providers. No confirmed wild exploitation but high risk given email attack surface.
- **CVE ID**: None assigned (research findings)

### Solidity Pro VS Code Extension Supply Chain Attack
- **Description**: A malicious Microsoft Visual Studio Code extension named "Solidity Pro" (solidity-pro) published to the VS Code Marketplace that delivers browser wallet and credential stealing functionality.
- **Impact**: Theft of cryptocurrency wallets, API keys, credentials, and sensitive development artifacts from blockchain and Web3 developers.
- **Status**: Identified and flagged by researchers. Extension removed from marketplace. Unknown number of developer installations compromised.
- **CVE ID**: None assigned (malicious extension)

## Affected Systems and Products

- **SonicWall SMA1000 Series**: SSL-VPN appliances running vulnerable firmware versions prior to patched releases. Critical infrastructure for remote access.
- **Progress Kemp LoadMaster**: Application delivery controllers and load balancers (virtual and hardware appliances) running vulnerable versions. Used in enterprise and cloud environments.
- **Metabase**: Business intelligence and data visualization platform (open-source and cloud versions). Versions prior to security patch affecting Framework, Tally, and other customer instances.
- **N-able N-central**: Remote Monitoring and Management (RMM) platform used by managed service providers. All versions prior to Hotfix 2. Impacts MSP infrastructure and downstream managed endpoints.
- **TrueConf Server**: Video conferencing server software (on-premises deployments). Unpatched versions exploited to trojanize client installers for Windows, macOS, Linux, iOS, Android.
- **Apple iOS/iPhone**: Devices targeted by Coruna and DarkSword exploit chains. Specific iOS versions not disclosed; chains reportedly work on recent releases.
- **npm Registry / Node.js Ecosystem**: Developers and CI/CD pipelines installing any of the ~800 malicious packages. Cross-platform impact on Windows, macOS, Linux.
- **macOS**: Systems targeted by ClickFix social engineering delivering Go-based stealer malware. Requires user interaction with fake error pages.
- **Atlassian Rovo / Jira / Confluence**: Organizations using Atlassian's Rovo AI assistant with connected Jira and Confluence instances. Data accessible to signed-in users at risk.
- **Webmail Platforms**: Outlook Web Access, Gmail, Fastmail, Proton Mail, Yahoo Mail, and potentially other web-based email clients vulnerable to CSS injection attacks.
- **VS Code Marketplace / Extensions**: Developers who installed the "Solidity Pro" (solidity-pro) extension. Blockchain/Web3 developers primary targets.
- **N-able N-central Managed Endpoints**: Downstream customer systems managed through compromised N-central instances, receiving StormEncryptor ransomware payloads.

## Attack Vectors and Techniques

- **SSRF to RCE Chain (SonicWall)**: Server-side request forgery vulnerability chained to achieve unauthenticated remote code execution on VPN appliances, providing initial network access for ransomware gangs.
- **Command Injection (LoadMaster)**: Unauthenticated command injection in management interface allowing arbitrary OS command execution as root on load balancer appliances.
- **Zero-Day SQL Injection (Metabase)**: Pre-authentication SQL injection enabling administrative bypass, arbitrary query execution, and full database compromise without valid credentials.
- **RMM Supply Chain Compromise (N-central)**: Exploitation of centralized management platform to push malicious payloads (StormEncryptor ransomware) to all managed downstream endpoints simultaneously.
- **Software Supply Chain / Installer Trojanization (TrueConf)**: Compromise of vendor build/distribution infrastructure to replace legitimate client installers with backdoored versions (PhantomCore), infecting all downstream users.
- **Nation-Grade Exploit Chain Proliferation (iOS)**: Advanced exploit chains (Coruna, DarkSword) leveraging multiple vulnerabilities (browser, kernel, sandbox escape) migrating from state actors to cybercrime groups.
- **Malicious Package Publishing (npm)**: Typosquatting, dependency confusion, or direct publishing of ~800 malicious packages with obfuscated payloads delivering cross-platform RAT/infostealer.
- **ClickFix Social Engineering**: Fake browser error pages (Cloudflare/Google verification mimics) tricking users into copying/pasting malicious PowerShell/bash commands into terminal.
- **Prompt Injection / AI Assistant Abuse (Atlassian Rovo)**: Malicious instructions embedded in accessible content (Jira issues, Confluence pages) causing AI assistant to exfiltrate data to attacker-controlled servers.
- **CSS Injection / Side-Channel Exfiltration (Webmail)**: Crafted CSS in email content exploiting browser rendering behaviors to leak tokens, passwords, and cross-origin data via layout-based side channels.
- **IDE Extension Malware (VS Code)**: Malicious extension with legitimate-seeming functionality (Solidity development tools) hiding credential/crypto wallet exfiltration capabilities.
- **Offline AI for Offensive Operations (Kimsuky)**: North Korean actors deploying local LLMs for automated spear-phishing content generation, malware code development, and vulnerability research without cloud API exposure.
- **Vishing / Voice Phishing (UNC6671)**: Targeted phone calls to personal devices of employees at financial services, private equity, and professional services firms to steal SaaS credentials and data.
- **Ransomware Deployment via RMM (StormEncryptor)**: Novel ransomware strain deployed through compromised N-central RMM, indicating financially motivated actors adopting MSP-targeted distribution.

## Threat Actor Activities

- **Storm-1175 (China-Linked, Financially Motivated)**: Deploying StormEncryptor ransomware via exploited N-able N-central RMM vulnerability. Targeting managed service providers and their downstream customers for financial gain. Demonstrates Chinese nexus actors engaging in ransomware operations.
- **Head Mare (Hacktivist, Pro-Ukrainian)**: Exploiting TrueConf server vulnerabilities to breach Russian organizations in instrumentation, electronics, and industrial sectors. Trojanizing client installers with PhantomCore backdoor for persistent access and data collection.
- **Former Medusa Affiliate (Financially Motivated)**: Operating independently after Medusa ransomware operation, now deploying new StormEncryptor strain. Indicates ransomware ecosystem fluidity and affiliate migration between operations.
- **Kimsuky / APT43 (North Korea State-Sponsored)**: Building and operating offline AI stack (local LLMs) to enhance spear-phishing campaigns, automate malware development, and conduct vulnerability research without attribution risk from cloud AI APIs.
- **UNC6671 (Data Extortion Group)**: Conducting targeted vishing campaigns against financial services, private equity, and professional services. Using personal phone outreach to steal SaaS credentials and exfiltrate sensitive data for extortion.
- **The Com (Loose-Knit Cybercrime Collective)**: Targeting children and teenagers for blackmail and sextortion. Member sentenced to two years for offenses against nearly 120 victims. Represents youth-focused cybercrime trend.
- **Ransomware Gangs (Multiple, Unattributed)**: Exploiting SonicWall SMA1000 and Progress LoadMaster vulnerabilities for initial access and ransomware deployment. Opportunistic targeting of internet-exposed appliances.
- **Unknown/Unattributed (npm Supply Chain)**: Operators of ~800 malicious npm package campaign delivering cross-platform RAT/infostealer. Broad opportunistic targeting of developers across ecosystems.
- **Unknown/Unattributed (ClickFix macOS)**: Operators using ClickFix social engineering to deliver Go-based macOS stealer. Targeting cryptocurrency holders and general macOS users via fake verification pages.

## Source Attribution

- **The Patch Gap: Why Defenders Need to Think in Chains, Not Checklists**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/patch-gap-defenders-chains-not-checklists
- **New StormEncryptor ransomware used by former Medusa affiliate**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-stormencryptor-ransomware-used-by-former-medusa-affiliate/
- **Shipping 10–50× More Code? Watch This Webinar on Securing AI-Speed Development**: The Hacker News - https://thehackernews.com/2026/08/shipping-1050-more-code-watch-this.html
- **Coruna, DarkSword iOS Exploits Proliferate Globally**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/coruna-darksword-ios-exploits-proliferate-globally
- **China-Linked Hackers Deploy New StormEncryptor Ransomware, Likely via N-central Flaw**: The Hacker News - https://thehackernews.com/2026/08/china-linked-hackers-deploy-new.html
- **Outdated Cybercrime Laws Put Security Researchers at Risk**: Dark Reading - https://www.darkreading.com/application-security/outdated-cybercrime-laws-security-researchers-risk
- **Sherlock Holmes was the “OG” Social Engineer**: Dark Reading - https://www.darkreading.com/cyber-risk/sherlock-holmes-was-the-og-social-engineer
- **⚡ Weekly Recap: AI Goes Rogue, Metabase 0-Day, MCP Supply-Chain Attacks, and Router Backdoors**: The Hacker News - https://thehackernews.com/2026/08/weekly-recap-ai-goes-rogue-metabase-0.html
- **CISA: SonicWall SMA1000 flaws now exploited by ransomware gangs**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-sonicwall-sma1000-flaws-now-exploited-by-ransomware-gangs/
- **When Credentials Are No Longer Enough: Device Trust in the AI Era**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/when-credentials-are-no-longer-enough-device-trust-in-the-ai-era/
- **Kimsuky Builds Offline AI Stack to Boost Phishing and Automate Malware Development**: The Hacker News - https://thehackernews.com/2026/08/kimsuky-builds-offline-ai-stack-that.html
- **Member of The Com sent to prison for blackmail, sextortion**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/member-of-the-com-sent-to-prison-for-blackmail-sextortion/
- **New Passkey Attacks Can Recover Synced Private Keys or Bypass Phishing-Resistant MFA**: The Hacker News - https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html
- **LexisNexis shuts down services after suspicious activity on servers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lexisnexis-shuts-down-services-after-suspicious-activity-on-servers/
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
