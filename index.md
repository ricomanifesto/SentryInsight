# Exploitation Report

## Executive Summary

Microsoft's July 2026 Patch Tuesday addressed a record-breaking 570 vulnerabilities, including two actively exploited zero-days and one publicly disclosed zero-day. Simultaneously, Progress Software confirmed a high-severity zero-day in ShareFile Storage Zone Controllers that forced an emergency shutdown before patches were released. These events underscore a continued pattern of attackers leveraging zero-day vulnerabilities in widely deployed enterprise software before defenders can respond.

Supply chain attacks have surged across multiple ecosystems. Nearly 300 malicious GitHub repositories impersonate legitimate software to distribute infostealers, while 148 npm packages disguised as student proxies covertly turned visitors' browsers into a DDoS botnet for two weeks. The Jscrambler npm package was backdoored with infostealer malware and downloaded approximately 1,500 times. Additionally, the Cursor IDE retains an unpatched vulnerability—reported in December—that allows auto-execution of malicious code from poisoned repositories, representing an ongoing risk to developers.

Credential theft and identity-focused attacks are evolving rapidly. Two new phishing kits, Jalisco and OmegaLord, target Microsoft 365 accounts with MFA-evading techniques. At least two distinct threat actors are weaponizing OAuth client ID spoofing to validate stolen Microsoft Entra credentials in cloud campaigns while evading telemetry. The ShinyHunters data-extortion group has spent a year exploiting misconfigured Salesforce environments across three attack paths without exploiting a single platform vulnerability, demonstrating that identity and configuration weaknesses remain more exploitable than code flaws.

## Active Exploitation Details

### Microsoft July 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's monthly security update addressed 570 vulnerabilities across Windows and associated products. Two of these vulnerabilities were zero-days actively exploited in attacks at the time of patching, and a third zero-day had been publicly disclosed prior to the update.
- **Impact**: Attackers leveraging the exploited zero-days could achieve remote code execution, privilege escalation, or security feature bypass on unpatched Windows systems. The scale of 570 flaws indicates broad attack surface exposure across the Windows ecosystem.
- **Status**: Patches released as part of July 2026 Patch Tuesday. Organizations should prioritize immediate deployment given confirmed exploitation of two vulnerabilities.
- **CVE ID**: CVE IDs not specified in source articles.

### Progress ShareFile Storage Zone Controller Zero-Day
- **Description**: A high-severity zero-day vulnerability in Progress Software's ShareFile Storage Zone Controllers triggered an emergency shutdown of the service. Progress confirmed the flaw was actively exploited and released security updates to remediate it.
- **Impact**: Successful exploitation likely allows unauthorized access to sensitive file storage, data exfiltration, or further lateral movement within connected environments.
- **Status**: Security updates released by Progress Software following emergency shutdown. Customers must apply patches immediately.
- **CVE ID**: CVE ID not specified in source articles.

### Cursor IDE Poisoned Repository Code Execution
- **Description**: A vulnerability in the Cursor AI coding platform allows automatic execution of malicious code when a developer interacts with a poisoned repository. Researchers reported the flaw to Cursor in December 2025, but it remains unpatched as of the reporting period.
- **Impact**: Attackers can compromise developer machines and potentially inject malicious code into software projects by luring developers to interact with compromised repositories.
- **Status**: Unpatched despite responsible disclosure. Active exploitation vector in poisoned repository attacks.
- **CVE ID**: CVE ID not specified in source articles.

### RabbitMQ Access Control Flaws
- **Description**: Two access control vulnerabilities in the RabbitMQ message broker service could allow attackers to leak OAuth client secrets and expose cross-tenant queue metadata. Researchers disclosed the flaws publicly.
- **Impact**: Compromise of OAuth secrets enables credential theft and unauthorized API access. Cross-tenant metadata exposure violates isolation guarantees in multi-tenant deployments.
- **Status**: Details disclosed by researchers; patch status not specified in source article.
- **CVE ID**: CVE IDs not specified in source articles.

### Microsoft-Signed Linux UEFI Shim Secure Boot Bypass
- **Description**: Eleven old Microsoft-signed UEFI applications (shims) can be abused to bypass Secure Boot on most systems using the modern UEFI Secure Boot standard. These legacy shims remain trusted by the Microsoft UEFI certificate authority.
- **Impact**: Attackers with physical access or administrative privileges can load unsigned bootloaders or rootkits, defeating a foundational platform security control.
- **Status**: No mitigation specified in source article; requires UEFI revocation updates or configuration changes.
- **CVE ID**: CVE IDs not specified in source articles.

### OAuth Client ID Spoofing in Microsoft Entra ID
- **Description**: A novel evasion technique allows attackers to spoof OAuth client IDs, enabling validation of stolen Microsoft Entra (formerly Azure AD) credentials while slipping past telemetry and detection systems. At least two distinct threat actors are actively weaponizing this in cloud campaigns.
- **Impact**: Attackers can silently verify compromised credentials, enumerate valid accounts, and conduct credential stuffing or password spray attacks without triggering standard alerts.
- **Status**: Active exploitation by multiple threat actors. No patch available as this abuses legitimate OAuth protocol behavior; detection requires behavioral analytics.
- **CVE ID**: CVE ID not specified in source articles.

## Affected Systems and Products

- **Windows 10 and Windows 11**: All supported versions affected by July 2026 Patch Tuesday vulnerabilities (570 flaws). Windows 10 KB5099539 extended security update and Windows 11 KB5101650/KB5099414 cumulative updates address these.
- **Progress ShareFile Storage Zone Controllers**: On-premises storage controllers affected by zero-day vulnerability requiring emergency patching.
- **Cursor IDE**: AI-powered code editor (all versions as of reporting) vulnerable to auto-execution from poisoned repositories.
- **RabbitMQ**: Message broker deployments using affected versions; multi-tenant environments at heightened risk for cross-tenant data exposure.
- **Linux Systems with UEFI Secure Boot**: Most distributions using Microsoft-signed shims vulnerable to Secure Boot bypass via 11 legacy UEFI applications.
- **Microsoft Entra ID / Azure AD**: Tenants targeted by OAuth client ID spoofing campaigns validating stolen credentials.
- **Microsoft 365**: Accounts targeted by Jalisco and OmegaLord phishing kits with MFA evasion capabilities.
- **GitHub**: Platform hosting nearly 300 malicious repositories impersonating legitimate software projects.
- **npm Registry**: 148 malicious packages (student proxy disguises) and Jscrambler backdoored package distributed via the registry.
- **SAP NetWeaver, Commerce Cloud, and AppRouter**: Three critical vulnerabilities among 16 total flaws addressed in July 2026 security updates.
- **Salesforce**: Environments targeted by ShinyHunters via misconfiguration abuse across three attack paths (no platform vulnerabilities exploited).
- **NVIDIA Software**: Brand impersonated by LabubaRAT malware for Windows host compromise.
- **Apple Crash Reporter**: Impersonated by CrashStealer macOS malware for credential, keychain, and crypto wallet theft.
- **LastPass and Bitwarden**: Users targeted by phishing campaigns using fake security alerts.
- **Jscrambler**: Client-side security company's npm package supply chain compromised.

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in Windows (2 exploited zero-days) and ShareFile before or at patch release.
- **Supply Chain Compromise**: Malicious packages published to npm (148 DDoS botnet packages, Jscrambler backdoor) and fake GitHub repositories (nearly 300) impersonating legitimate software.
- **Poisoned Repository Attacks**: Developers lured to interact with compromised repositories triggering auto-execution in vulnerable IDEs (Cursor).
- **OAuth Client ID Spoofing**: Novel technique abusing OAuth protocol to validate stolen Entra credentials while evading telemetry; used by at least two threat actor groups.
- **MFA-Evading Phishing**: Jalisco and OmegaLord phishing kits defeat multi-factor authentication for Microsoft 365 accounts.
- **Brand Impersonation Malware Delivery**: LabubaRAT masquerades as NVIDIA software; CrashStealer poses as Apple crash reporter; fake GitHub repos impersonate legitimate projects.
- **Browser-Based DDoS Botnet**: Malicious npm packages execute JavaScript in visitors' browsers to create distributed denial-of-service capacity.
- **Salesforce Misconfiguration Abuse**: ShinyHunters exploits three attack paths involving excessive permissions, exposed APIs, and weak access controls—no code vulnerabilities required.
- **UEFI Secure Boot Bypass**: Legacy Microsoft-signed shims used to load unsigned code at boot time, defeating hardware-rooted trust.
- **Credential Validation via OAuth**: Stolen credentials silently verified against Entra ID using spoofed client IDs, enabling efficient credential stuffing.

## Threat Actor Activities

- **ShinyHunters**: Data-extortion group active for at least one year targeting corporate Salesforce environments. Mapped to three distinct attack paths involving misconfigurations rather than vulnerabilities. Focus on data theft and extortion over ransomware deployment.
- **OAuth Client ID Spoofing Operators**: At least two distinct threat actor groups weaponizing OAuth client ID spoofing in cloud campaigns against Microsoft Entra ID. Demonstrates sophisticated understanding of identity protocols and telemetry evasion.
- **GitHub Repository Impersonation Actor**: Single threat actor or group publishing nearly 300 fake repositories to distribute infostealer malware. Broad targeting of developers and software users.
- **npm Supply Chain Attackers**: Operators behind 148 malicious packages (DDoS botnet campaign, May 2026, ~2 weeks duration) and the Jscrambler package backdoor (infostealer, ~1,500 downloads). JFrog researchers attributed the proxy campaign.
- **LabubaRAT Operators**: Deploying previously undocumented Rust-based RAT masquerading as NVIDIA software. Targeting Windows hosts for remote access and control.
- **CrashStealer Operators**: Distributing macOS infostealer posing as Apple crash reporter to harvest credentials, keychain data, and cryptocurrency wallets.
- **Phishing Kit Operators (Jalisco/OmegaLord)**: Deploying advanced MFA-evading phishing infrastructure targeting Microsoft 365 credentials at scale.
- **Russian Cyber Actors**: Sanctioned jointly by UK and EU for cyberattacks and disinformation campaigns. Specific groups not named in source articles.
- **Ransomware Enablers**: Two individuals and one VPN service provider sanctioned by OFAC for enabling ransomware attacks against U.S. organizations. Includes a malware cryptor seller.

## Source Attribution

- **Nearly 300 GitHub repos pose as legit software to push malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/nearly-300-github-repos-pose-as-legit-software-to-push-malware/
- **Microsoft releases Windows 10 KB5099539 extended security update**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-10-kb5099539-extended-security-update/
- **Microsoft July 2026 Patch Tuesday fixes massive 570 flaws, 3 zero-days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2026-patch-tuesday-fixes-massive-570-flaws-3-zero-days/
- **Manage Vendor Risk in a Few Practical Steps**: Dark Reading - https://www.darkreading.com/cyber-risk/manage-vendor-risk-in-a-few-practical-steps
- **Windows 11 KB5101650 \& KB5099414 cumulative updates released**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5101650-and-kb5099414-cumulative-updates-released/
- **LabubaRAT Masquerades as NVIDIA Software to Control Windows Hosts**: The Hacker News - https://thehackernews.com/2026/07/labubarat-masquerades-as-nvidia.html
- **Progress confirms ShareFile zero-day flaw behind Storage Zone shutdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/
- **Frontier AI: The Genie's Out of the Bottle, but Where's the Rulebook?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/frontier-ai-genie-out-of-bottle-where-rulebook
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
