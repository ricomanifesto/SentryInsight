# Exploitation Report

## Executive Summary

Critical exploitation activity surged in July 2026 with multiple zero-day vulnerabilities under active attack across diverse platforms. SonicWall SMA 1000 appliances face two actively exploited zero-days (CVE-2026-15409 and CVE-2026-15410), one enabling arbitrary command execution as administrator. Microsoft's record-breaking Patch Tuesday addressed 570–622 vulnerabilities including three zero-days, two of which were already exploited in the wild. CISA issued an urgent warning for three actively exploited flaws in on-premises SharePoint Server, while Progress Software confirmed a high-severity zero-day behind the emergency shutdown of ShareFile Storage Zone Controllers.

Supply chain and social engineering campaigns continue to expand in sophistication. Four compromised npm packages in the @asyncapi namespace delivered multi-stage botnet malware, while nearly 300 fake GitHub repositories impersonated legitimate software to distribute infostealers. The ClickFix attack ecosystem has matured into a rented service that evades AV and EDR, and new phishing kits (Jalisco and OmegaLord) now defeat MFA protections targeting Microsoft 365 accounts. A previously undocumented Rust-based RAT dubbed LabubaRAT masquerades as NVIDIA software, and the Cursor IDE remains vulnerable to auto-execution of malicious code from poisoned repositories months after disclosure.

Law enforcement actions disrupted significant criminal infrastructure. U.S. prosecutors charged three Russian nationals for operating bulletproof hosting services that facilitated over $62 million in ransomware damage. Spanish police dismantled a cybercrime ring responsible for €140 million in investment fraud and business email compromise attacks. These developments underscore the convergence of vulnerability exploitation, supply chain compromise, and organized cybercrime as dominant threat vectors.

## Active Exploitation Details

### SonicWall SMA 1000 Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting SonicWall Secure Mobile Access (SMA) 1000 series appliances. One vulnerability enables arbitrary command execution with administrative privileges.
- **Impact**: Attackers can achieve full administrative control over affected SMA 1000 appliances, potentially compromising VPN access, network segmentation, and sensitive corporate resources.
- **Status**: Actively exploited in zero-day attacks. SonicWall has released security updates and urges immediate patching.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Microsoft July 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's largest Patch Tuesday on record addressed 570–622 vulnerabilities, including three zero-days. Two zero-days were under active exploitation at the time of patch release, and one was publicly disclosed but not yet exploited.
- **Impact**: The exploited zero-days allow attackers to compromise Windows systems and other Microsoft products. Specific impact varies by vulnerability but includes remote code execution and privilege escalation.
- **Status**: Patches released July 2026. Two zero-days confirmed exploited in the wild; one publicly disclosed zero-day patched preemptively.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### SharePoint Server Actively Exploited Flaws
- **Description**: CISA warned that attackers are actively exploiting three vulnerabilities in Internet-exposed on-premises SharePoint Server installations.
- **Impact**: Successful exploitation allows attackers to compromise SharePoint servers, potentially leading to data theft, lateral movement, and persistence in organizational networks.
- **Status**: Actively exploited. CISA added these vulnerabilities to the Known Exploited Vulnerabilities (KEV) catalog, mandating federal agency patching and urging all organizations to apply updates immediately.

### Progress ShareFile Zero-Day Vulnerability
- **Description**: A high-severity zero-day vulnerability in Progress ShareFile Storage Zone Controllers triggered an emergency shutdown of the service. Progress Software confirmed the flaw and released security updates.
- **Impact**: The vulnerability could allow attackers to compromise Storage Zone Controllers, potentially accessing or exfiltrating sensitive file transfer data.
- **Status**: Zero-day exploited in the wild. Emergency patches released following service shutdown.

### Compromised @asyncapi npm Packages
- **Description**: Four npm packages in the @asyncapi namespace were compromised and weaponized to deliver a multi-stage botnet loader. The supply chain attack was discovered by OX Security, SafeDep, Socket, and StepSecurity.
- **Impact**: Organizations installing the compromised packages inadvertently deploy a multi-stage botnet capable of persistent access, command execution, and lateral movement.
- **Status**: Actively exploited via supply chain. Malicious packages identified and reported; developers urged to audit dependencies and rotate credentials.

### Fake GitHub Repository Campaign
- **Description**: A threat actor published nearly 300 fake GitHub repositories impersonating legitimate software and security projects to distribute infostealer malware.
- **Impact**: Developers and security researchers cloning or executing code from these repositories risk credential theft, session hijacking, and system compromise via infostealer payloads.
- **Status**: Active campaign. Repositories mimic legitimate projects with convincing documentation and release artifacts.

### LabubaRAT Campaign
- **Description**: A previously undocumented Rust-based remote access trojan (RAT) codenamed LabubaRAT masquerades as NVIDIA software to blend into target environments.
- **Impact**: Provides attackers with full remote control over infected Windows hosts, including command execution, file management, and persistence capabilities.
- **Status**: Active in the wild. Rust implementation suggests modern tooling and potential evasion of traditional detection signatures.

### Cursor IDE Poisoned Repository Vulnerability
- **Description**: The Cursor AI coding platform auto-executes malicious code from poisoned repositories. The vulnerability was reported to Cursor in December 2025 but remains unpatched as of July 2026.
- **Impact**: Developers opening or interacting with malicious repositories in Cursor IDE can trigger arbitrary code execution without explicit user action.
- **Status**: Unpatched zero-day (reported December 2025). Active exploitation possible via supply chain or social engineering.

### Claude for Chrome Extension Flaw
- **Description**: A flaw in the Claude for Chrome extension allows any other browser extension with script execution capabilities on claude.ai to trigger Claude tasks targeting Gmail, Google Docs, and Calendar data.
- **Impact**: Rogue or compromised extensions can exfiltrate sensitive email content, document data, and calendar information without user consent.
- **Status**: Vulnerability disclosed by researchers. Exploitation requires a malicious or compromised co-installed extension.

### ClickFix Attack Ecosystem
- **Description**: The ClickFix attack vector has evolved into a mature ecosystem available for rent at scale. The technique evades antivirus and EDR solutions, with YARA analysis identified as the primary detection method.
- **Impact**: Lowers barrier to entry for attackers; enables widespread deployment of social engineering lures that bypass modern endpoint protections.
- **Status**: Actively offered as a service. Ongoing campaigns leveraging ClickFix infrastructure.

### Jalisco and OmegaLord Phishing Kits
- **Description**: Two new phishing kits (Jalisco and OmegaLord) target Microsoft 365 accounts using techniques that defeat multi-factor authentication (MFA).
- **Impact**: Attackers can compromise MFA-protected Microsoft 365 accounts, gaining access to email, SharePoint, Teams, and associated cloud resources.
- **Status**: Active in the wild. Kits distributed via underground markets and used in ongoing credential harvesting campaigns.

## Affected Systems and Products

- **SonicWall SMA 1000 Series Appliances**: Secure Mobile Access 1000 series firmware versions prior to the July 2026 security update. Affected platforms include SMA 1002, 1004, 1008, and 1010 appliances.
- **Microsoft Windows and Software Ecosystem**: Windows 10, Windows 11 (versions 23H2, 24H2, 25H2), Windows Server, Microsoft Office, SharePoint Server (on-premises), and related Microsoft products covered by the July 2026 Patch Tuesday release (570–622 CVEs).
- **Progress ShareFile Storage Zone Controllers**: On-premises Storage Zone Controller versions prior to the emergency July 2026 security update. Cloud-hosted zones not affected.
- **@asyncapi npm Packages**: Four specific packages in the @asyncapi namespace (package names and versions detailed in OX Security, SafeDep, Socket, and StepSecurity advisories). All projects using these packages as dependencies.
- **GitHub Repository Consumers**: Developers, CI/CD pipelines, and automated tooling cloning or executing code from the nearly 300 identified malicious repositories impersonating legitimate projects.
- **Cursor IDE Users**: All versions of the Cursor AI coding platform that have not received a fix for the auto-execution vulnerability (reported December 2025, unpatched as of July 2026).
- **Claude for Chrome Extension Users**: Users with the Claude for Chrome extension installed alongside any other extension capable of running scripts on claude.ai.
- **Microsoft 365 Tenants**: Organizations using Microsoft 365 with MFA enabled, targeted by Jalisco and OmegaLord phishing kits employing MFA-bypass techniques.
- **NVIDIA Software Environments**: Windows hosts where LabubaRAT masquerades as legitimate NVIDIA processes (e.g., NVIDIA GeForce Experience, NVIDIA Container Toolkit components).
- **RabbitMQ Message Broker Deployments**: Instances affected by two access control flaws allowing OAuth secret leakage and cross-tenant queue metadata exposure (CVEs not specified in source articles).
- **SAP NetWeaver Application Server ABAP**: Versions affected by the CVSS 9.9 critical flaw patched in SAP July 2026 security updates (specific CVE not provided in source article).
- **Linux Systems with UEFI Secure Boot**: Systems using any of the 11 old Microsoft-signed UEFI shims that could be abused to bypass Secure Boot protections.

## Attack Vectors and Techniques

- **Zero-Day Exploitation of Network Edge Devices**: Attackers target Internet-exposed SonicWall SMA 1000 appliances using two zero-days (CVE-2026-15409, CVE-2026-15410) for unauthenticated remote code execution and administrative command execution.
- **Supply Chain Compromise via npm Registry**: Malicious actors compromised legitimate @asyncapi namespace packages, injecting multi-stage botnet loaders that execute upon installation via standard dependency management workflows.
- **Typosquatting and Impersonation on GitHub**: Threat actors create hundreds of repositories mimicking legitimate software projects with convincing metadata, README files, and release artifacts to trick developers into downloading infostealer malware.
- **Poisoned Repository Auto-Execution in AI IDEs**: The Cursor IDE automatically executes code from repository contents (e.g., configuration files, scripts) without explicit user consent, enabling drive-by compromise when developers open malicious repositories.
- **Browser Extension Cross-Origin Abuse**: A flaw in the Claude for Chrome extension allows any co-installed extension with script access to claude.ai to trigger privileged actions targeting Gmail, Google Docs, and Calendar data.
- **MFA-Bypass Phishing Kits**: Jalisco and OmegaLord phishing kits employ advanced techniques (likely adversary-in-the-middle or session hijacking) to defeat multi-factor authentication protecting Microsoft 365 accounts.
- **ClickFix Social Engineering at Scale**: Attackers rent ClickFix infrastructure to deploy fake verification pages (e.g., "I'm not a robot," CAPTCHA mimics) that trick users into executing malicious PowerShell commands via clipboard manipulation.
- **Rust-Based Malware Masquerading as Legitimate Software**: LabubaRAT uses Rust for memory safety and evasion benefits, disguising its processes and files as NVIDIA software components to avoid suspicion in process lists and file system inspections.
- **Bulletproof Hosting for Ransomware Operations**: Russian nationals allegedly operated hosting infrastructure specifically designed to resist takedown and law enforcement action, enabling ransomware gangs to maintain C2, payment portals, and data leak sites.
- **Business Email Compromise and Investment Fraud**: Spanish cybercrime ring combined BEC tactics with investment fraud schemes, leveraging social engineering and compromised email accounts to authorize fraudulent transfers totaling €140 million.
- **SharePoint Server Exploitation via Internet Exposure**: Attackers scan for and exploit on-premises SharePoint servers directly exposed to the Internet, leveraging three actively exploited vulnerabilities for initial access and lateral movement.
- **ShareFile Storage Zone Controller Zero-Day Exploitation**: Attackers exploited a high-severity zero-day in Progress ShareFile Storage Zone Controllers, prompting an emergency service shutdown and patch deployment.

## Threat Actor Activities

- **Russian Bulletproof Hosting Operators (Three Charged Nationals)**: U.S. prosecutors unsealed charges against three Russian nationals for providing bulletproof hosting services to ransomware gangs. Their infrastructure facilitated over $62 million in ransomware damage. The operators deliberately configured hosting to resist legal process, abuse complaints, and takedown efforts.
- **Spanish Cyber Fraud Ring (Four Arrested)**: Spanish Police dismantled a cybercrime and money-laundering organization responsible for €140 million ($160 million) in losses from investment fraud and business email compromise attacks. The group used sophisticated social engineering and compromised corporate email accounts to authorize fraudulent wire transfers.
- **AsyncAPI Supply Chain Attackers (Unknown Operators)**: Unknown threat actors compromised four npm packages in the @asyncapi namespace, injecting a multi-stage botnet loader. The attack demonstrates advanced supply chain tradecraft targeting developer tooling ecosystems.
- **GitHub Impersonation Campaign Operator (Unknown Actor)**: A single threat actor or group created nearly 300 fake repositories impersonating legitimate software and security projects. The campaign distributes infostealer malware targeting developer credentials and sensitive data.
- **LabubaRAT Operators (Unknown)**: Operators of the previously undocumented Rust-based RAT LabubaRAT, which masquerades as NVIDIA software. The use of Rust and deliberate masquerading suggests a capability-focused actor investing in custom tooling.
- **ClickFix Ecosystem Operators (Service Providers)**: The ClickFix attack vector has been commoditized into a rented service. Operators maintain the infrastructure (phishing pages, command delivery, evasion techniques) and lease access to affiliates or customers.
- **Jalisco and OmegaLord Phishing Kit Operators**: Developers and distributors of two new MFA-bypass phishing kits targeting Microsoft 365. Kits are sold or leased on underground markets and used by multiple threat actors in credential harvesting campaigns.
- **SonicWall SMA 1000 Zero-Day Exploiters (Unknown)**: Threat actors actively exploiting CVE-2026-15409 and CVE-2026-15410 in the wild prior to patch availability. Targeting suggests focus on VPN edge infrastructure for initial access.
- **SharePoint Server Exploiters (Unknown)**: Actors exploiting three vulnerabilities in Internet-exposed on-premises SharePoint Server instances. CISA's KEV catalog addition indicates confirmed exploitation activity.
- **ShareFile Zero-Day Exploiters (Unknown)**: Attackers who exploited the high-severity zero-day in Progress ShareFile Storage Zone Controllers, triggering the emergency shutdown. Identity and attribution not publicly disclosed.

## Source Attribution

- **CISA warns admins to patch actively exploited SharePoint flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-patch-actively-exploited-sharepoint-flaws/
- **Compromised AsyncAPI npm Packages Deliver Multi-Stage Botnet Malware**: The Hacker News - https://thehackernews.com/2026/07/compromised-asyncapi-npm-packages.html
- **Microsoft: Some Dell PCs shut down after recent Windows updates**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-some-dell-devices-shut-down-after-windows-update/
- **Nigeria Deepens Cybersecurity Efforts as Cybercriminals See More Profits**: Dark Reading - https://www.darkreading.com/cyber-risk/nigeria-cybersecurity-efforts-cybercriminals-profits
- **US charges alleged operators of Russian bulletproof hosting service**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-alleged-russian-bulletproof-hosting-service-operators/
- **Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands**: The Hacker News - https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html
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
