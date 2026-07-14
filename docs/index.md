# Exploitation Report

## Executive Summary

Progress Software confirmed a high-severity zero-day vulnerability in ShareFile Storage Zone Controllers that forced an emergency shutdown of the service last week. The flaw is actively exploited in the wild, and Progress has released security updates to address the issue. This incident highlights the ongoing risk to file transfer and collaboration platforms, which remain prime targets for threat actors seeking initial access to corporate networks.

Multiple active exploitation campaigns are leveraging novel techniques to bypass modern defenses. At least two distinct threat actors are weaponizing OAuth client ID spoofing to validate stolen Microsoft Entra credentials in cloud environments, evading telemetry while enumerating valid accounts. Simultaneously, CISA has warned of active exploitation of remote code execution flaws in Joomla extensions (iCagenda and Balbooa Forms), and a supply chain compromise of the Jscrambler npm package delivered infostealer malware to nearly 1,500 downstream consumers. New phishing kits—Jalisco and OmegaLord—are defeating multi-factor authentication protections on Microsoft 365 accounts at scale.

The threat landscape continues to evolve with modular, multi-capability malware and abuse of trusted platforms. CrashStealer macOS malware uses a notarized dropper to bypass Gatekeeper while harvesting credentials, keychain data, and cryptocurrency wallets. The GigaWiper implant combines backdoor and wiper functionality in a modular framework. A campaign of 148 malicious npm packages disguised as student proxies turned visitors' browsers into a DDoS botnet for two weeks. Meanwhile, the ShinyHunters data-extortion group has spent a year accessing corporate Salesforce environments through misconfigurations and credential abuse rather than platform vulnerabilities, and U.S. sanctions have targeted VPN providers and malware cryptor services enabling ransomware operations.

## Active Exploitation Details

### Progress ShareFile Storage Zone Controller Zero-Day
- **Description**: A high-severity zero-day vulnerability in Progress Software's ShareFile Storage Zone Controllers that prompted an emergency shutdown of the service. The flaw allows attackers to compromise the storage zone infrastructure.
- **Impact**: Full compromise of ShareFile Storage Zone Controllers, potentially exposing sensitive file transfer data and providing a foothold into organizational networks.
- **Status**: Actively exploited in the wild. Progress Software has released security updates to patch the vulnerability. Organizations running Storage Zone Controllers must apply updates immediately.
- **CVE ID**: Not specified in source article

### Joomla iCagenda and Balbooa Forms RCE Vulnerabilities
- **Description**: Remote code execution vulnerabilities in the iCagenda and Balbooa Forms extensions for Joomla content management system.
- **Impact**: Attackers can achieve remote code execution on affected Joomla installations, leading to full server compromise.
- **Status**: Actively exploited in the wild. CISA has issued a warning urging immediate patching.
- **CVE ID**: Not specified in source article

### Jscrambler npm Package Supply Chain Compromise
- **Description**: Threat actors published a malicious version of the Jscrambler client-side web security npm package containing infostealer malware.
- **Impact**: Nearly 1,500 downloads of the backdoored package, potentially compromising development environments and build pipelines of organizations using Jscrambler.
- **Status**: Actively exploited via supply chain. Malicious package has been identified and reported.
- **CVE ID**: Not specified in source article

### OAuth Client ID Spoofing Campaign
- **Description**: A novel evasion technique where attackers spoof OAuth client IDs to validate stolen Microsoft Entra credentials while evading telemetry and detection.
- **Impact**: Enables threat actors to enumerate valid credentials in cloud environments, facilitating unauthorized access to Microsoft Entra ID (formerly Azure AD) tenants.
- **Status**: Actively weaponized by at least two distinct threat actors in ongoing cloud campaigns.
- **CVE ID**: Not specified in source article

### Cursor IDE Poisoned Repository Code Execution
- **Description**: Vulnerability in Cursor IDE that allows automatic execution of malicious code when developers interact with poisoned repositories. Reported to Cursor in December but remains unpatched.
- **Impact**: Arbitrary code execution in developer environments when opening or interacting with compromised repositories, potentially leading to supply chain attacks or credential theft.
- **Status**: Unpatched as of reporting. Actively exploitable in poisoned repository attacks.
- **CVE ID**: Not specified in source article

### Microsoft 365 Phishing Kits (Jalisco and OmegaLord)
- **Description**: Two new phishing kits specifically designed to target Microsoft 365 accounts with techniques that defeat multi-factor authentication protections.
- **Impact**: Credential theft and account takeover of Microsoft 365 users despite MFA enforcement, enabling business email compromise and data exfiltration.
- **Status**: Actively deployed in phishing campaigns targeting Microsoft 365 tenants.
- **CVE ID**: Not specified in source article

### ClickFix Attack Ecosystem
- **Description**: The ClickFix attack vector has matured into a rental ecosystem available at scale, employing techniques that evade traditional AV and EDR solutions.
- **Impact**: Social engineering attacks that trick users into executing malicious commands, leading to malware installation and system compromise.
- **Status**: Actively available for rent and deployed in campaigns. YARA analysis identified as best detection option.
- **CVE ID**: Not specified in source article

### RabbitMQ Access Control Flaws
- **Description**: Two access control-related vulnerabilities in RabbitMQ message broker that could leak OAuth client secrets and expose cross-tenant queue metadata.
- **Impact**: Unauthorized access to sensitive OAuth client secret leakage enabling impersonation attacks, and cross-tenant data exposure in multi-tenant RabbitMQ deployments.
- **Status**: Disclosed by researchers. Exploitation status not confirmed as active in the wild.
- **CVE ID**: Not specified in source article

### 11 Legacy Microsoft-Signed UEFI Shim Secure Boot Bypass
- **Description**: Eleven old Microsoft-signed UEFI applications that can be abused to bypass Secure Boot protections on modern systems.
- **Impact**: Secure Boot bypass enabling bootkit and rootkit installation, persistence at firmware level, and evasion of UEFI security controls.
- **Status**: Vulnerable shims identified. Active exploitation not confirmed in source article.
- **CVE ID**: Not specified in source article

### SAP NetWeaver and Commerce Cloud Critical Flaws
- **Description**: Three critical vulnerabilities among 16 total flaws addressed in SAP's July 2026 security updates, affecting NetWeaver, Commerce Cloud, and AppRouter.
- **Impact**: Potential for critical business system compromise, data theft, and disruption of ERP and commerce operations.
- **Status**: Patches released in July 2026 security updates. Exploitation status not confirmed as active in the wild.
- **CVE ID**: Not specified in source article

## Affected Systems and Products

- **Progress ShareFile Storage Zone Controllers**: All versions prior to the emergency security update. On-premises storage zone components for ShareFile file sharing platform.
- **Joomla CMS with iCagenda Extension**: Joomla installations using the iCagenda event management extension. Specific affected versions not detailed in source.
- **Joomla CMS with Balbooa Forms Extension**: Joomla installations using the Balbooa Forms extension. Specific affected versions not detailed in source.
- **Jscrambler npm Package**: Version(s) containing the backdoored infostealer malware. Downloaded approximately 1,500 times before detection.
- **Cursor IDE**: All current versions as of reporting. AI-powered code editor vulnerable to poisoned repository attacks.
- **Microsoft Entra ID / Azure AD**: Tenants targeted by OAuth client ID spoofing campaigns for credential validation and enumeration.
- **Microsoft 365 / Office 365**: Accounts targeted by Jalisco and OmegaLord phishing kits with MFA bypass capabilities.
- **RabbitMQ Message Broker**: Deployments with affected access control configurations, particularly multi-tenant environments.
- **Systems with Legacy Microsoft-Signed UEFI Shims**: Most modern systems using UEFI Secure Boot with any of the 11 identified legacy shim binaries.
- **SAP NetWeaver**: Enterprise application platform installations requiring July 2026 security patches.
- **SAP Commerce Cloud**: Cloud commerce platform deployments requiring July 2026 security patches.
- **SAP AppRouter**: Application router component requiring July 2026 security patches.
- **macOS Systems**: Targeted by CrashStealer malware posing as Apple's crash reporting tool.
- **npm Ecosystem**: 148 malicious packages disguised as student web proxies, affecting browsers visiting compromised sites.
- **Salesforce Environments**: Corporate instances targeted by ShinyHunters through misconfiguration and credential abuse.
- **Google Chrome and Microsoft Edge**: Browsers with ModHeader extension (1.6 million installs) containing hidden browsing history collector.
- **Linux UEFI Boot Systems**: Systems relying on Microsoft-signed shims for Secure Boot compatibility.

## Attack Vectors and Techniques

- **Zero-Day Exploitation of File Transfer Infrastructure**: Targeting Progress ShareFile Storage Zone Controllers for initial access and data theft.
- **Remote Code Execution via CMS Extensions**: Exploiting vulnerable Joomla extensions (iCagenda, Balbooa Forms) for server compromise.
- **Software Supply Chain Compromise**: Injecting infostealer malware into legitimate npm packages (Jscrambler) to compromise downstream consumers.
- **OAuth Client ID Spoofing**: Novel technique to validate stolen Microsoft Entra credentials while evading telemetry and detection systems.
- **Poisoned Repository Attacks**: Malicious code in repositories that auto-executes in vulnerable AI-powered IDEs (Cursor) when developers interact with them.
- **MFA-Bypassing Phishing Kits**: Jalisco and OmegaLord kits using advanced techniques to defeat multi-factor authentication on Microsoft 365.
- **ClickFix Social Engineering**: Tricking users into executing malicious commands via fake verification pages, evading AV/EDR through living-off-the-land techniques.
- **OAuth Secret Leakage via Message Broker Misconfiguration**: Exploiting RabbitMQ access control flaws to harvest OAuth client secrets and cross-tenant metadata.
- **Secure Boot Bypass via Legacy UEFI Shims**: Abusing 11 old Microsoft-signed UEFI applications to disable Secure Boot protections.
- **Notarized Dropper Abuse**: CrashStealer malware using Apple-notarized dropper to pass Gatekeeper checks on macOS.
- **Browser-Based DDoS Botnet**: 148 malicious npm packages disguised as student proxies converting visitors' browsers into distributed denial-of-service nodes.
- **Salesforce Misconfiguration and Credential Abuse**: ShinyHunters accessing corporate Salesforce environments without exploiting platform vulnerabilities.
- **Malicious Browser Extension Data Collection**: ModHeader extension with hidden browsing history collector affecting 1.6 million users across Chrome and Edge.
- **Modular Wiper/Backdoor Implant**: GigaWiper combining destructive wiper capabilities with persistent backdoor access in a configurable framework.
- **Fake Security Alert Phishing**: Campaigns impersonating LastPass and Bitwarden security notices to steal password manager credentials.
- **VPN and Malware Infrastructure for Ransomware**: Sanctioned entities providing VPN services and malware cryptors to enable ransomware operations.

## Threat Actor Activities

- **ShinyHunters (Data-Extortion Group)**: Conducted a year-long campaign accessing corporate Salesforce environments through three distinct attack paths involving misconfigurations, credential reuse, and excessive permissions—without exploiting any Salesforce platform vulnerabilities. Microsoft has mapped their activity across multiple victim organizations.
- **Two Distinct Threat Actors (OAuth Client ID Spoofing)**: At least two separate groups actively weaponizing OAuth client ID spoofing in cloud campaigns against Microsoft Entra ID tenants for credential validation and enumeration.
- **Jscrambler Supply Chain Attacker**: Unknown threat actor who compromised the Jscrambler npm package publishing pipeline to distribute infostealer malware to nearly 1,500 downstream consumers.
- **ClickFix Operators**: Threat actors operating the ClickFix attack ecosystem as a rental service, continuously evolving techniques to evade AV/EDR detection.
- **Phishing Kit Operators (Jalisco/OmegaLord)**: Groups deploying advanced phishing kits targeting Microsoft 365 with MFA bypass capabilities.
- **CISA-Tracked Joomla Exploiters**: Unknown actors actively exploiting iCagenda and Balbooa Forms RCE vulnerabilities in Joomla installations.
- **Russian Cyber Actors**: Individuals and entities sanctioned jointly by UK and EU for cyberattacks and disinformation campaigns in the region.
- **Nihon Kotsu Attackers**: Unknown threat actors who compromised Japan's largest taxi operator, forcing infrastructure shutdown.
- **CrashStealer Operators**: Developers and distributors of macOS information stealer using notarized dropper to bypass Gatekeeper, targeting credentials, keychain data, and cryptocurrency wallets.
- **npm DDoS Botnet Operators**: Campaign operators who published 148 malicious packages disguised as student proxies, operating a browser-based DDoS botnet for approximately two weeks in May.
- **Sanctioned Ransomware Enablers**: Two individuals and one VPN service provider designated by OFAC for providing infrastructure (VPN services, malware cryptors) to ransomware actors and cybercriminals.
- **LastPass/Bitwarden Phishing Campaign Operators**: Unknown actors running ongoing phishing campaigns using fake security alerts to target password manager users.
- **ModHeader Extension Developer**: Party responsible for embedding hidden browsing history collector in popular header-editing extension with 1.6 million installs.

## Source Attribution

- **Progress confirms ShareFile zero-day flaw behind Storage Zone shutdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/
- **Frontier AI: The Genie's Out of the Bottle, But Where's the Rulebook?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/frontier-ai-genie-out-of-bottle-where-rulebook
- **ClickFix's Mushrooming Ecosystem Demands New Defense Tactics**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/clickfixs-ecosystem-demands-new-defense
- **LastPass, Bitwarden users targeted with fake security alerts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lastpass-bitwarden-users-targeted-with-fake-security-alerts/
- **You Don't Have to Run an Exploit to Know If You're Vulnerable**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/you-dont-have-to-run-an-exploit-to-know-if-youre-vulnerable/
- **RabbitMQ Flaws Could Leak OAuth Secrets and Expose Cross-Tenant Queue Metadata**: The Hacker News - https://thehackernews.com/2026/07/rabbitmq-flaws-could-leak-oauth-secrets.html
- **Cursor IDE Auto-Executes Malicious Code in Poisoned Repos**: Dark Reading - https://www.darkreading.com/application-security/cursor-ide-malicious-code-poisoned-repos
- **Microsoft Entra ID gets passkeys default authentication starting September**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-entra-id-gets-passkeys-default-authentication-starting-september/
- **New phishing kits target Microsoft 365 accounts, evade MFA**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/
- **11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot**: The Hacker News - https://thehackernews.com/2026/07/11-old-microsoft-signed-linux-uefi.html
- **Study of 85 Crypto Wallet Extensions Finds Address Leaks and Cross-Site Tracking Risks**: The Hacker News - https://thehackernews.com/2026/07/study-of-85-crypto-wallet-extensions.html
- **SAP warns of critical flaws in NetWeaver and Commerce Cloud**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sap-warns-of-critical-flaws-in-netweaver-and-commerce-cloud/
- **How Pentera Turns AI Security Workflows into Validation Engines**: The Hacker News - https://thehackernews.com/2026/07/how-pentera-turns-ai-security-workflows.html
- **OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials**: The Hacker News - https://thehackernews.com/2026/07/oauth-client-id-spoofing-lets-attackers.html
- **Microsoft starts testing cleaner Windows Search without ads**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-starts-testing-cleaner-windows-search-without-ads/
- **US sanctions VPN, malware providers for enabling ransomware attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-sanctions-vpn-malware-providers-linked-to-ransomware-gangs/
- **Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read**: The Hacker News - https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html
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
