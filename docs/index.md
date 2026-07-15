# Exploitation Report

## Executive Summary

Critical zero-day exploitation activity surged in July 2026, with multiple vendors confirming active attacks against unpatched vulnerabilities. SonicWall disclosed that two SMA1000 appliance flaws (CVE-2026-15409 and CVE-2026-15410) are being exploited in the wild, while Microsoft's record-breaking Patch Tuesday addressed 570–622 vulnerabilities including two to three actively exploited zero-days across Windows and associated products. Progress Software separately confirmed a high-severity zero-day in ShareFile Storage Zone Controllers that prompted an emergency shutdown, and SAP patched a critical CVSS 9.9 NetWeaver ABAP vulnerability among 16 total fixes.

Beyond vendor patches, threat actors are diversifying initial access techniques. At least two distinct groups are leveraging OAuth client ID spoofing to validate stolen Microsoft Entra credentials while evading telemetry, and new phishing kits—Jalisco and OmegaLord—are defeating MFA to compromise Microsoft 365 accounts. A large-scale GitHub supply chain campaign deployed nearly 300 typosquatted repositories distributing infostealer malware, while the Rust-based LabubaRAT masquerades as NVIDIA software to establish persistent remote access. Law enforcement disruption continues, with Spanish authorities dismantling a €140 million cyber fraud ring combining investment scams and business email compromise.

## Active Exploitation Details

### SonicWall SMA1000 Zero-Day Vulnerabilities
- **Description**: Two vulnerabilities in SonicWall SMA1000 series secure mobile access appliances are being actively exploited as zero-days. The flaws allow threat actors to compromise the appliances without authentication.
- **Impact**: Attackers can gain unauthorized access to corporate VPN appliances, potentially leading to network intrusion, lateral movement, and data exfiltration from organizations using these devices for remote access.
- **Status**: Actively exploited in zero-day attacks. SonicWall has released emergency patches and urges immediate installation.
- **CVE ID**: CVE-2026-15409
- **CVE ID**: CVE-2026-15410

### Microsoft July 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's largest Patch Tuesday on record addressed 570–622 security flaws across Windows, Office, and associated components. Two to three of these vulnerabilities were confirmed as zero-days under active exploitation at the time of release.
- **Impact**: Exploitation of these zero-days could allow remote code execution, elevation of privilege, security feature bypass, and information disclosure depending on the specific component affected.
- **Status**: Patches released as part of July 2026 security updates (KB5099539 for Windows 10, KB5101650/KB5099414 for Windows 11). Active exploitation confirmed prior to patch availability.
- **CVE ID**: Specific CVE identifiers for the exploited zero-days were not disclosed in the source articles.

### Progress ShareFile Storage Zone Controller Zero-Day
- **Description**: A high-severity zero-day vulnerability in Progress Software's ShareFile Storage Zone Controllers prompted an emergency shutdown of the service last week. The flaw resides in the storage zone component that handles file storage and transfer.
- **Impact**: Successful exploitation could allow unauthorized access to stored files, data theft, and potential compromise of the underlying infrastructure hosting the storage zones.
- **Status**: Progress has confirmed the zero-day and released security updates to patch the vulnerability. Storage Zone Controllers were temporarily shut down as a containment measure.
- **CVE ID**: CVE identifier not specified in the source article.

### SAP NetWeaver ABAP Critical Flaw
- **Description**: A critical vulnerability in SAP NetWeaver Application Server ABAP with a CVSS score of 9.9 was addressed in SAP's July 2026 security updates. The flaw could allow unauthorized exposure or modification of data.
- **Impact**: Attackers could potentially read, modify, or delete sensitive business data processed through the NetWeaver ABAP platform, affecting core ERP and business-critical applications.
- **Status**: Patched as part of SAP's July 2026 security updates covering 16 vulnerabilities across multiple products including NetWeaver, Commerce Cloud, and AppRouter.
- **CVE ID**: CVE identifier not specified in the source articles.

### OAuth Client ID Spoofing Campaign
- **Description**: A novel evasion technique called OAuth client ID spoofing is being weaponized by at least two distinct threat actors in cloud campaigns targeting Microsoft Entra ID. The technique allows attackers to validate stolen credentials while slipping past telemetry and detection mechanisms.
- **Impact**: Enables credential validation and enumeration of valid Entra ID accounts without triggering standard security alerts, facilitating subsequent account takeover, privilege escalation, and lateral movement in cloud environments.
- **Status**: Actively exploited by at least two threat actor groups. No vendor patch available as this appears to be an abuse of legitimate OAuth functionality rather than a software vulnerability.
- **CVE ID**: Not applicable (technique abuse, not a CVE-tracked vulnerability)

### Jalisco and OmegaLord Phishing Kits
- **Description**: Two new phishing-as-a-service kits—Jalisco and OmegaLord—have been discovered targeting Microsoft 365 accounts with techniques specifically designed to defeat multi-factor authentication (MFA).
- **Impact**: Successful attacks result in full account compromise despite MFA protection, enabling business email compromise, data theft, and further phishing propagation from trusted accounts.
- **Status**: Actively deployed in ongoing campaigns. No software patch mitigates this; defense relies on phishing-resistant authentication (FIDO2/passkeys) and user awareness.
- **CVE ID**: Not applicable (phishing kit infrastructure, not a CVE-tracked vulnerability)

## Affected Systems and Products

- **SonicWall SMA1000 Series**: Secure mobile access appliances running vulnerable firmware versions prior to the emergency patch release
- **Microsoft Windows 10**: All supported versions receiving extended security updates (KB5099539)
- **Microsoft Windows 11**: Versions 25H2, 24H2, and 23H2 (KB5101650 and KB5099414 cumulative updates)
- **Microsoft Office and Associated Components**: Covered under the 570–622 CVE Patch Tuesday release
- **Progress ShareFile Storage Zone Controllers**: On-premises storage zone components prior to the July 2026 security update
- **SAP NetWeaver Application Server ABAP**: All versions affected by the CVSS 9.9 flaw prior to July 2026 security patch
- **SAP Commerce Cloud and AppRouter**: Additional critical flaws addressed in the same SAP security update
- **Microsoft Entra ID**: Cloud identity platform targeted by OAuth client ID spoofing campaigns
- **Microsoft 365 Accounts**: Targeted by Jalisco and OmegaLord phishing kits with MFA bypass capabilities
- **GitHub Repository Consumers**: Developers and organizations downloading from typosquatted repositories impersonating legitimate software
- **Cursor IDE Users**: Developers using the AI coding platform vulnerable to auto-execution of malicious code in poisoned repositories
- **Claude for Chrome Extension Users**: Browser extension users vulnerable to rogue extension attacks triggering unauthorized Gmail/Calendar/Google Docs access
- **RabbitMQ Message Broker Deployments**: Instances vulnerable to OAuth client secret leakage and cross-tenant queue metadata exposure
- **Systems Using Microsoft-Signed Linux UEFI Shims**: Devices with any of 11 old Microsoft-signed UEFI applications vulnerable to Secure Boot bypass
- **6 GHz Wi-Fi AFC Systems**: Automated Frequency Coordination systems trusting client-side data, vulnerable to location spoofing

## Attack Vectors and Techniques

- **Zero-Day Appliance Exploitation**: Direct network exploitation of internet-facing VPN/appliance interfaces (SonicWall SMA1000, ShareFile Storage Zones) without authentication requirements
- **OAuth Client ID Spoofing**: Abuse of legitimate OAuth flows by registering malicious applications that mimic legitimate client IDs, enabling credential validation while evading telemetry in Microsoft Entra ID
- **MFA-Bypass Phishing Kits**: Adversary-in-the-middle (AiTM) and session hijacking techniques packaged as-a-service (Jalisco, OmegaLord) to defeat Microsoft 365 MFA including push notifications and TOTP
- **Typosquatted Supply Chain Attack**: Publication of nearly 300 fake GitHub repositories impersonating legitimate software/security projects to distribute infostealer malware to developers
- **Rust-Based RAT Masquerading**: LabubaRAT disguising as NVIDIA software (filenames, descriptions, digital signatures) to blend into target environments and establish persistent remote access
- **AI IDE Poisoned Repository Exploitation**: Cursor IDE automatically executing malicious code from compromised repositories during AI-assisted code analysis without user interaction
- **Browser Extension Cross-Origin Abuse**: Rogue Chrome extensions exploiting Claude for Chrome's permissions to trigger unauthorized reads of Gmail, Google Docs, and Calendar data
- **Business Email Compromise (BEC)**: Social engineering and credential theft enabling fraudulent wire transfers and invoice manipulation (€140M Spanish fraud ring)
- **ClickFix Attack Vector Rental**: Social engineering technique tricking users into executing malicious PowerShell commands via fake error pages, now available as-a-service at scale with AV/EDR evasion
- **AFC Client-Side Trust Exploitation**: Manipulation of client-reported location data in 6 GHz Wi-Fi Automated Frequency Coordination systems to spoof location and disrupt critical communications
- **UEFI Secure Boot Bypass**: Abuse of 11 legacy Microsoft-signed Linux UEFI shim binaries to load unsigned code during boot process, bypassing Secure Boot protections
- **Fake Security Alert Phishing**: Campaigns impersonating LastPass and Bitwarden security notifications to direct users to credential harvesting sites
- **Malware/VPN Provider Sanctions Evasion**: OFAC-sanctioned entities providing infrastructure (VPN, malware) enabling ransomware affiliate ransomware operations against U.S. organizations

## Threat Actor Activities

- **Unknown Actors (SonicWall Zero-Day Exploitation)**: Actively exploiting CVE-2026-15409 and CVE-2026-15410 against SMA1000 appliances in the wild prior to patch availability. Attribution not disclosed in source articles.
- **Multiple Unnamed Threat Groups (Microsoft Zero-Day Exploitation)**: At least two to three distinct zero-days under active exploitation suggest multiple actor groups or a sophisticated actor with diverse capabilities targeting Microsoft ecosystem.
- **Unknown Actor (ShareFile Zero-Day)**: Exploited the high-severity ShareFile Storage Zone Controller flaw prompting emergency shutdown. Attribution not disclosed.
- **At Least Two Distinct Threat Actors (OAuth Client ID Spoofing)**: Separate groups independently weaponizing OAuth client ID spoofing for Entra ID credential validation and cloud reconnaissance campaigns.
- **Phishing Kit Operators (Jalisco & OmegaLord)**: Cybercrime actors developing and operating MFA-bypass phishing-as-a-service platforms targeting Microsoft 365 enterprise environments.
- **GitHub Supply Chain Actor**: Single threat actor or group publishing nearly 300 typosquatted repositories impersonating legitimate software and security tools to distribute infostealer malware.
- **LabubaRAT Operators**: Unknown group deploying a previously undocumented Rust-based RAT masquerading as NVIDIA software for Windows host compromise and persistent access.
- **Spanish Cyber Fraud Ring**: Organized crime group dismantled by Spanish Police, generating €140 million ($160M) through investment fraud and BEC attacks. Four individuals arrested.
- **ClickFix Ecosystem Operators**: Multiple threat actors renting ClickFix attack infrastructure at scale, using social engineering to bypass AV/EDR via YARA-evading PowerShell execution.
- **Ransomware-Affiliated Infrastructure Providers**: Two individuals and one entity sanctioned by OFAC for providing VPN services and malware enabling ransomware attacks against U.S. organizations.

## Source Attribution

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
- **Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read**: The Hacker News - https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html
