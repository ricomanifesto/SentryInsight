# Exploitation Report

## Executive Summary

Microsoft's July 2026 Patch Tuesday has set a new record with 570 to 622 vulnerabilities addressed across its product ecosystem, including three zero-day flaws—two confirmed under active exploitation and one publicly disclosed. This massive release, complemented by critical patches from SonicWall, Progress Software, and SAP, signals an escalation in both the volume and severity of vulnerabilities requiring immediate triage. Organizations face a compressed patching window as threat actors move quickly to weaponize disclosed flaws.

Active exploitation campaigns are diversifying beyond traditional vulnerability exploitation. At least two distinct threat actors are leveraging a novel OAuth client ID spoofing technique to validate stolen Microsoft Entra ID credentials while evading telemetry. Meanwhile, the ClickFix attack framework has matured into a rental ecosystem that bypasses AV and EDR solutions, and two new phishing kits (Jalisco and OmegaLord) are defeating MFA protections on Microsoft 365 accounts. A large-scale GitHub supply chain campaign has deployed nearly 300 malicious repositories impersonating legitimate software to distribute infostealers, and the previously undocumented LabubaRAT masquerades as NVIDIA software to maintain persistence on compromised Windows hosts.

Law enforcement and regulatory actions are also accelerating. Spanish authorities dismantled a €140 million cyber fraud ring combining investment scams and business email compromise, arresting four operators. The U.S. Treasury Department sanctioned two individuals and one entity for providing VPN and malware infrastructure that enabled ransomware attacks against American organizations. These developments underscore the convergence of state-level response with the operational tempo of financially motivated threat groups.

## Active Exploitation Details

### Microsoft July 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's largest Patch Tuesday on record addressed 570–622 CVEs across Windows, Office, Exchange, and related products. Three zero-day vulnerabilities were patched: two actively exploited in the wild and one publicly disclosed prior to patch release. More than 60 vulnerabilities received Critical severity ratings.
- **Impact**: Attackers exploiting the two active zero-days can achieve remote code execution, privilege escalation, or security feature bypass depending on the specific component. The sheer volume of critical flaws significantly expands the attack surface for organizations delaying patch deployment.
- **Status**: Patches released July 2026. Active exploitation confirmed for two zero-days; one publicly disclosed. Organizations should prioritize deployment based on asset criticality and exposure.
- **CVE ID**: Specific CVE IDs for the zero-days were not disclosed in the source articles.

### SonicWall SMA1000 Zero-Day Vulnerabilities
- **Description**: Two vulnerabilities in SonicWall SMA1000 series appliances are being exploited in zero-day attacks. The flaws affect the SSL-VPN management interface and could allow unauthenticated attackers to execute arbitrary commands.
- **Impact**: Successful exploitation grants attackers administrative access to the appliance, enabling network pivoting, credential harvesting, and persistent foothold in victim environments.
- **Status**: Actively exploited in the wild. SonicWall has released emergency firmware updates and urges immediate installation.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Progress ShareFile Storage Zone Controller Zero-Day
- **Description**: A high-severity zero-day vulnerability in Progress ShareFile Storage Zone Controllers triggered an emergency shutdown of the service last week. The flaw allows unauthenticated attackers to compromise the storage controller.
- **Impact**: Attackers can access, modify, or exfiltrate sensitive files stored in ShareFile zones, potentially exposing confidential enterprise data shared with partners and customers.
- **Status**: Actively exploited (triggered emergency shutdown). Progress Software has released security updates to patch the vulnerability.
- **CVE ID**: Specific CVE ID not disclosed in the source article.

### SAP NetWeaver ABAP Critical Flaw
- **Description**: A CVSS 9.9 critical vulnerability in SAP NetWeaver Application Server ABAP, patched as part of SAP's July 2026 security updates addressing 16 total vulnerabilities across NetWeaver, Commerce Cloud, and AppRouter.
- **Impact**: The flaw could allow attackers to expose or modify sensitive business data processed by the ABAP stack, including financial, HR, and supply chain records.
- **Status**: Patched in July 2026 release. Three critical vulnerabilities addressed across the SAP portfolio.
- **CVE ID**: Specific CVE ID not disclosed in the source articles.

### Cursor IDE Poisoned Repository Code Execution
- **Description**: The Cursor AI coding platform auto-executes malicious code embedded in poisoned repositories. The vulnerability was reported to Cursor in December 2025 but remains unpatched as of July 2026.
- **Impact**: Developers cloning or interacting with malicious repositories can inadvertently execute attacker-controlled code on their workstations, leading to full system compromise, credential theft, and supply chain contamination.
- **Status**: Unpatched, actively exploitable. No fix released despite responsible disclosure.
- **CVE ID**: Specific CVE ID not disclosed in the source article.

## Affected Systems and Products

- **Microsoft Windows (all supported versions)**: 570–622 vulnerabilities patched in July 2026 Patch Tuesday, including two actively exploited zero-days and 60+ critical flaws
- **Microsoft Office, Exchange, SharePoint, and related productivity suite**: Included in the record Patch Tuesday release
- **Windows 10 (Extended Security Updates)**: KB5099539 includes all July 2026 fixes for 570 vulnerabilities plus additional security updates
- **Windows 11 (versions 25H2, 24H2, 23H2)**: KB5101650 and KB5099414 cumulative updates addressing 570+ security issues
- **SonicWall SMA1000 Series Appliances**: Firmware versions prior to the emergency July 2026 release vulnerable to CVE-2026-15409 and CVE-2026-15410
- **Progress ShareFile Storage Zone Controllers**: All versions prior to the emergency security update released after the zero-day exploitation
- **SAP NetWeaver Application Server ABAP**: Versions affected by the CVSS 9.9 flaw and two additional critical vulnerabilities in Commerce Cloud and AppRouter
- **Cursor IDE (AI Coding Platform)**: All current versions vulnerable to auto-execution of malicious code in poisoned repositories
- **RabbitMQ Message Broker**: Versions with access control flaws allowing OAuth secret leakage and cross-tenant queue metadata exposure
- **6 GHz Wi-Fi Automated Frequency Coordination (AFC) Systems**: Systems trusting client-side location data by default, enabling spoofing attacks
- **Microsoft Entra ID**: Tenants vulnerable to OAuth client ID spoofing used to validate stolen credentials
- **Microsoft 365 Accounts**: Targeted by Jalisco and OmegaLord phishing kits that defeat MFA
- **Linux Systems with UEFI Secure Boot**: Systems using any of 11 old Microsoft-signed UEFI shims vulnerable to Secure Boot bypass
- **Chrome Browser with Claude Extension**: Users vulnerable to rogue extensions triggering unauthorized Gmail, Google Docs, and Calendar access
- **LastPass and Bitwarden Users**: Targeted by phishing campaigns using fake security alerts

## Attack Vectors and Techniques

- **OAuth Client ID Spoofing**: Attackers spoof legitimate OAuth client IDs to validate stolen Microsoft Entra ID credentials against Microsoft's authentication endpoints. The technique evades standard telemetry by mimicking legitimate application behavior, allowing threat actors to enumerate valid credentials without triggering alerts.
- **ClickFix Attack Framework**: A social engineering technique where victims are tricked into executing malicious PowerShell commands via "fix" prompts (e.g., fake CAPTCHA verifications, error dialogs). The framework is now available as a rented service at scale, with built-in AV/EDR evasion. YARA rule analysis remains the most reliable detection method.
- **MFA-Bypassing Phishing Kits (Jalisco & OmegaLord)**: Purpose-built phishing frameworks targeting Microsoft 365 that use adversary-in-the-middle (AiTM) techniques, real-time session hijacking, and token replay to defeat multi-factor authentication protections.
- **GitHub Repository Impersonation & Typosquatting**: Nearly 300 malicious repositories mimic legitimate software projects and security tools. Attackers leverage typo-squatted names, copied READMEs, and fake release artifacts to trick developers into downloading infostealer malware.
- **Fake Security Alert Phishing**: Campaigns targeting password manager users (LastPass, Bitwarden) with fraudulent security notifications directing victims to credential-harvesting sites that mimic official login portals.
- **LabubaRAT Masquerading**: Rust-based remote access trojan disguises itself as legitimate NVIDIA software (filenames, metadata, installation paths) to blend into gaming and workstation environments, evading heuristic analysis.
- **Claude for Chrome Extension Abuse**: Any browser extension with script execution permission on claude.ai can trigger the Claude extension to read Gmail, access Google Docs and comments, and view Calendar data—no direct compromise of the Claude extension required.
- **UEFI Secure Boot Bypass via Legacy Shims**: Attackers chain 11 old Microsoft-signed UEFI applications (shims) to bypass Secure Boot on modern systems, enabling bootkit installation and pre-OS persistence.
- **RabbitMQ Access Control Bypass**: Two flaws in RabbitMQ's permission model allow unauthorized users to read OAuth client secrets from other vhosts and enumerate queue metadata across tenant boundaries in multi-tenant deployments.
- **6 GHz Wi-Fi AFC Location Spoofing**: Automated Frequency Coordination systems accept client-reported location data without server-side validation, enabling attackers to spoof coordinates and disrupt incumbent protection mechanisms for critical infrastructure.
- **Poisoned Repository Supply Chain Attack**: Malicious code embedded in repository files (e.g., configuration, documentation, test data) auto-executes when opened in Cursor IDE, turning code review and dependency inspection into attack vectors.

## Threat Actor Activities

- **Spanish Cyber Fraud Organization (Dismantled)**: A structured cybercrime and money-laundering group generated €140 million ($160 million) through investment fraud schemes and business email compromise (BEC) attacks. Spanish National Police arrested four core members and seized infrastructure in a coordinated takedown.
- **OAuth Client ID Spoofing Operators (Two Distinct Groups)**: At least two separate threat actors independently weaponized OAuth client ID spoofing in cloud-focused campaigns against Microsoft Entra ID tenants. Both groups use the technique for credential validation and enumeration while avoiding detection by standard identity telemetry.
- **GitHub Supply Chain Campaign Operator**: A single threat actor or group created and maintained nearly 300 fake repositories over an extended period, systematically impersonating legitimate open-source projects and security tools to distribute infostealer payloads to developers.
- **LabubaRAT Operators**: Deploy a previously undocumented Rust-based RAT masquerading as NVIDIA software. The malware's use of Rust and legitimate software disguise suggests a sophistication level above commodity malware, potentially indicating a targeted espionage or high-value financial crime group.
- **Jalisco & OmegaLord Phishing Kit Operators**: Developers and affiliates behind two new phishing-as-a-service kits specifically engineered to defeat MFA on Microsoft 365. The kits' modular design suggests an ecosystem model with kit authors, infrastructure providers, and campaign operators.
- **Ransomware Enablers (Sanctioned by OFAC)**: Two individuals and one entity designated by the U.S. Treasury Department's Office of Foreign Assets Control for providing bulletproof VPN hosting and malware development services that directly facilitated ransomware attacks against U.S. critical infrastructure and private sector organizations.
- **ClickFix Framework Affiliates**: Multiple threat groups renting access to the ClickFix social engineering platform, which provides template generation, hosting, and evasion tooling as a managed service—lowering the barrier for credential theft and initial access operations.

## Source Attribution

- **Records Are Made to Be Broken: Patch Tuesday Raises Triage Stakes**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/records-broken-patch-tuesday-raises-triage-stakes
- **SonicWall warns of SMA1000 flaws exploited in zero-day attacks, patch now**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-sma1000-flaws-exploited-in-zero-day-attacks-patch-now/
- **Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack**: The Hacker News - https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html
- **Spanish Police take down €140 million cyber fraud ring, arrest four**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/spanish-police-take-down-140-million-cyber-fraud-ring-arrest-four/
- **6 GHz Wi-Fi Flaws Could Disrupt Critical Systems**: Dark Reading - https://www.darkreading.com/perimeter/6-ghz-wi-fi-flaws-disrupt-critical-systems
- **Microsoft Patches a Record 570 Security Flaws**: Krebs on Security - https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/
- **Nearly 300 GitHub repos pose as legit software to push malware**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/nearly-300-github-repos-pose-as-legit-software-to-push-malware/
- **Microsoft releases Windows 10 KB5099539 extended security update**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-10-kb5099539-extended-security-update/
- **SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data**: The Hacker News - https://thehackernews.com/2026/07/sap-patches-cvss-99-netweaver-abap-flaw.html
- **Microsoft July 2026 Patch Tuesday fixes massive 570 flaws, 3 zero-days**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2026-patch-tuesday-fixes-massive-570-flaws-3-zero-days/
- **Manage Vendor Risk in a Few Practical Steps**: Dark Reading - https://www.darkreading.com/cyber-risk/manage-vendor-risk-in-a-few-practical-steps
- **Windows 11 KB5101650 \& KB5099414 cumulative updates released**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5101650-and-kb5099414-cumulative-updates-released/
- **Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads**: The Hacker News - https://thehackernews.com/2026/07/claude-for-chrome-flaw-lets-other.html
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
