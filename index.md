# Exploitation Report

## Executive Summary

Critical exploitation activity surged in July 2026 with multiple zero-day vulnerabilities under active attack across diverse technology stacks. Microsoft's record-breaking Patch Tuesday addressed 570–622 flaws including two to three actively exploited zero-days, while SonicWall confirmed active exploitation of two SMA 1000 zero-days (CVE-2026-15409 and CVE-2026-15410) enabling arbitrary command execution. CISA issued urgent warnings for three actively exploited SharePoint Server vulnerabilities, and Progress Software confirmed a high-severity zero-day behind the emergency shutdown of ShareFile Storage Zone Controllers.

Supply chain attacks intensified with four compromised @asyncapi npm packages delivering multi-stage botnet malware and nearly 300 fake GitHub repositories distributing infostealers. Developer environments emerged as prime targets: Cursor's automatic execution of git.exe in project roots enables zero-click code execution, while a separate two-click exploit grants access to secrets and source code. Threat actors continue leveraging bulletproof hosting services—three Russian nationals were charged for facilitating over $62 million in ransomware damage—while Spanish authorities dismantled a €140 million cyber fraud ring conducting investment fraud and BEC attacks.

New attack vectors include the ClickFix ecosystem now available for rent at scale with AV/EDR evasion capabilities, phishing campaigns targeting LastPass and Bitwarden users via fake security alerts, and a previously undocumented Rust-based RAT (LabubaRAT) masquerading as NVIDIA software. Researchers also disclosed a Claude for Chrome extension flaw allowing rogue extensions to access Gmail, Google Docs, and Calendar data, while a Windows User Profile Service zero-day (LegacyHive) received public PoC code hours after Patch Tuesday.

## Active Exploitation Details

### SonicWall SMA 1000 Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting SonicWall Secure Mobile Access (SMA) 1000 series appliances. One vulnerability enables arbitrary command execution with administrative privileges.
- **Impact**: Attackers can achieve full administrative control over affected SMA 1000 appliances, potentially pivoting into internal networks behind the VPN gateway.
- **Status**: Actively exploited in zero-day attacks. SonicWall has released emergency patches and urges immediate installation.
- **CVE ID**: CVE-2026-15409
- **CVE ID**: CVE-2026-15410

### Microsoft July 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's largest Patch Tuesday on record addressed 570–622 vulnerabilities, including two to three zero-days confirmed under active exploitation and one publicly disclosed zero-day.
- **Impact**: Varies by vulnerability; active exploitation indicates weaponized capabilities in threat actor arsenals targeting Windows and associated Microsoft products.
- **Status**: Patches released July 2026. Two to three zero-days were actively exploited at time of patch release; one additional zero-day was publicly disclosed but not yet exploited.
- **CVE ID**: [Specific CVE IDs not provided in source articles]

### SharePoint Server Actively Exploited Vulnerabilities
- **Description**: Three vulnerabilities in Internet-exposed on-premises SharePoint Server installations are being actively exploited by threat actors.
- **Impact**: Remote code execution and potential compromise of SharePoint servers exposed to the internet, leading to data theft and lateral movement.
- **Status**: Actively exploited. CISA has added these to the Known Exploited Vulnerabilities catalog and mandated federal agencies to patch immediately.
- **CVE ID**: [Specific CVE IDs not provided in source articles]

### Progress ShareFile Storage Zone Controller Zero-Day
- **Description**: A high-severity zero-day vulnerability in ShareFile Storage Zone Controllers triggered an emergency shutdown of the service last week.
- **Impact**: Likely remote code execution or authentication bypass enabling unauthorized access to managed file transfer infrastructure.
- **Status**: Actively exploited (prompted emergency shutdown). Progress Software has released security updates to patch the flaw.
- **CVE ID**: [Specific CVE ID not provided in source articles]

### SAP NetWeaver Application Server ABAP Critical Flaw
- **Description**: A critical vulnerability in SAP NetWeaver Application Server ABAP with a CVSS score of 9.9, addressed in SAP's July 2026 security updates.
- **Impact**: Could allow attackers to expose or modify sensitive business data processed by the ABAP application server.
- **Status**: Patched in July 2026 SAP security updates. Exploitation status not explicitly confirmed in source articles.
- **CVE ID**: [Specific CVE ID not provided in source articles]

### Cursor Automatic Code Execution via git.exe
- **Description**: Cursor IDE on Windows automatically executes any file named git.exe present in a project root when the repository is opened, with no user interaction, approval dialog, or warning.
- **Impact**: Zero-click remote code execution when developers clone and open malicious repositories. Attackers can place malicious git.exe binaries in repositories distributed via GitHub or other sources.
- **Status**: Unpatched as of reporting. No mitigation beyond avoiding untrusted repositories.
- **CVE ID**: [CVE ID not provided in source articles]

### Cursor Two-Click Dev Environment Takeover
- **Description**: A two-click exploit chain targeting Cursor IDE that leverages "simple age-old bugs" to access developers' secrets and source code-rich environments.
- **Impact**: Full compromise of developer environments including access to API keys, credentials, source code, and potentially production infrastructure access.
- **Status**: Actively exploitable. Details suggest low complexity exploitation.
- **CVE ID**: [CVE ID not provided in source articles]

### Windows User Profile Service Zero-Day (LegacyHive)
- **Description**: Security researcher Chaotic Eclipse (aka Nightmare-Eclipse) released a proof-of-concept exploit called LegacyHive targeting the Windows User Profile Service arbitrary hive load vulnerability, hours after Microsoft's July Patch Tuesday.
- **Impact**: Potential privilege escalation or arbitrary code execution via malicious registry hive loading.
- **Status**: Public PoC available. Microsoft patched 570–622 vulnerabilities in July Patch Tuesday; unclear if this specific flaw was addressed.
- **CVE ID**: [CVE ID not provided in source articles]

### Claude for Chrome Extension Flaw
- **Description**: Any browser extension capable of running scripts on claude.ai can trigger Claude for Chrome tasks targeting users' Gmail, Google Docs (including comments), and Calendar data.
- **Impact**: Cross-extension data theft enabling access to email communications, documents, and scheduling information without user consent.
- **Status**: Disclosed by researchers. Remediation status not specified in source articles.
- **CVE ID**: [CVE ID not provided in source articles]

## Affected Systems and Products

- **SonicWall SMA 1000 Series Appliances**: Secure Mobile Access 1000 series VPN appliances running vulnerable firmware versions prior to emergency patches for CVE-2026-15409 and CVE-2026-15410
- **Microsoft Windows and Associated Products**: All supported Windows versions (Windows 10, Windows 11 23H2/24H2/25H2), Windows Server, Office, and other Microsoft software covered by the 570–622 CVE July 2026 Patch Tuesday release
- **On-Premises SharePoint Server**: Internet-exposed SharePoint Server installations (versions not specified in source articles) vulnerable to three actively exploited flaws
- **Progress ShareFile Storage Zone Controllers**: On-premises Storage Zone Controller deployments affected by the high-severity zero-day prompting emergency shutdown
- **SAP NetWeaver Application Server ABAP**: ABAP-based SAP NetWeaver Application Server installations prior to July 2026 security patch release
- **Cursor IDE on Windows**: All Windows versions of Cursor IDE vulnerable to automatic git.exe execution and two-click exploit chain
- **Google Chrome with Claude Extension**: Chrome browsers with the Claude for Chrome extension installed, exposed to cross-extension data access from any script-capable extension
- **@asyncapi npm Packages**: Four compromised packages in the @asyncapi namespace on npm registry distributing multi-stage botnet loader
- **GitHub Repository Ecosystem**: Nearly 300 fake repositories impersonating legitimate software and security projects to distribute infostealer malware
- **LastPass and Bitwarden Users**: Users of both password managers targeted by phishing campaigns using fake security alerts

## Attack Vectors and Techniques

- **Zero-Day Exploitation of VPN/Remote Access Gateways**: Active exploitation of SonicWall SMA 1000 zero-days (CVE-2026-15409, CVE-2026-15410) for initial access and administrative command execution on network perimeter devices
- **Supply Chain Compromise via npm Packages**: Four @asyncapi namespace packages compromised to deliver multi-stage botnet malware, leveraging developer trust in official organizational packages
- **Typosquatting/Impersonation on GitHub**: Nearly 300 fake repositories mimicking legitimate software and security projects to distribute infostealer malware to developers and security practitioners
- **Developer Environment Targeting via IDE Flaws**: 
  - Zero-click code execution via malicious git.exe in cloned repositories (Cursor on Windows)
  - Two-click exploit chain leveraging "age-old bugs" in Cursor for secrets and source code theft
- **Cross-Extension Data Theft in Browser**: Malicious or compromised Chrome extensions exploiting Claude for Chrome's overly permissive message passing to access Gmail, Google Docs, and Calendar data
- **Phishing via Fake Security Alerts**: Campaigns impersonating LastPass and Bitwarden security notifications to credential-harvesting pages
- **ClickFix Attack Ecosystem**: Social engineering technique now available "for rent at scale" that evades AV/EDR, requiring YARA-based detection approaches
- **Bulletproof Hosting for Ransomware Operations**: Russian bulletproof hosting service (charged by US prosecutors) providing infrastructure for ransomware gangs causing over $62 million in damages
- **Business Email Compromise and Investment Fraud**: Spanish police dismantled operation generating €140 million ($160 million) through BEC and investment fraud schemes
- **Rust-Based RAT Masquerading as Legitimate Software**: LabubaRAT disguises itself as NVIDIA software to blend into target environments and maintain persistence
- **Public PoC Release for Windows Kernel Vulnerability**: LegacyHive exploit for Windows User Profile Service arbitrary hive load released immediately post-Patch Tuesday
- **Automated Frequency Coordination Spoofing**: 6 GHz Wi-Fi AFC systems trusting client-side data enabling location spoofing attacks (theoretical/research stage)

## Threat Actor Activities

- **Chaotic Eclipse / Nightmare-Eclipse**: Security researcher who released the LegacyHive PoC exploit for Windows User Profile Service vulnerability hours after Microsoft's July 2026 Patch Tuesday
- **Russian Bulletproof Hosting Operators**: Three Russian nationals charged by US federal prosecutors for providing bulletproof hosting services to ransomware gangs responsible for over $62 million in damages
- **AsyncAPI Supply Chain Attackers**: Unknown threat actors who compromised four @asyncapi npm packages to distribute multi-stage botnet loader (attribution per OX Security, SafeDep, Socket, StepSecurity findings)
- **GitHub Repository Impersonation Campaign**: Unknown threat actor operating nearly 300 fake repositories impersonating legitimate software and security projects to distribute infostealer malware
- **Spanish Cyber Fraud Ring**: Dismantled organization conducting investment fraud and business email compromise (BEC) attacks generating €140 million ($160 million) in illicit proceeds; four arrests made by Spanish Police
- **ClickFix Ecosystem Operators**: Threat actors offering ClickFix social engineering attack infrastructure "for rent at scale" with built-in AV/EDR evasion capabilities
- **Password Manager Phishing Actors**: Unknown operators conducting phishing campaigns using fake security alerts targeting LastPass and Bitwarden users
- **LabubaRAT Operators**: Unknown threat actors deploying previously undocumented Rust-based RAT masquerading as NVIDIA software for Windows host control
- **SonicWall SMA 1000 Exploitation Actors**: Unknown threat actors actively exploiting CVE-2026-15409 and CVE-2026-15410 in zero-day attacks against SMA 1000 appliances
- **SharePoint Exploitation Actors**: Unknown threat actors actively exploiting three vulnerabilities in Internet-exposed on-premises SharePoint Server installations
- **ShareFile Zero-Day Exploitation Actors**: Unknown threat actors leveraging high-severity zero-day in ShareFile Storage Zone Controllers prompting emergency shutdown

## Source Attribution

- **2-Click Cursor Exploit Enables Dev Environment Takeover**: Dark Reading - https://www.darkreading.com/application-security/2-click-cursor-exploit-dev-environment-takeover
- **SASE Has An AI Blind Spot. Inspecting Packets Is No Longer Enough.**: The Hacker News - https://thehackernews.com/2026/07/sase-has-ai-blind-spot-inspecting.html
- **Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday**: The Hacker News - https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html
- **New Webinar: Closing the Approval Gap in AI-Era Ad Tech**: The Hacker News - https://thehackernews.com/2026/07/new-webinar-closing-approval-gap-in-ai.html
- **Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution**: The Hacker News - https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html
- **CISA warns admins to patch actively exploited SharePoint flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-patch-actively-exploited-sharepoint-flaws/
- **Compromised AsyncAPI npm Packages Deliver Multi-Stage Botnet Malware**: The Hacker News - https://thehackernews.com/2026/07/compromised-asyncapi-npm-packages.html
- **Microsoft: Some Dell PCs shut down after recent Windows updates**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-some-dell-devices-shut-down-after-windows-update/
- **Nigeria Deepens Cybersecurity Efforts as Cybercriminals See More Profits**: Dark Reading - https://www.darkreading.com/cyber-risk/nigeria-cybersecurity-efforts-cybercriminals-profits
- **US charges alleged operators of Russian bulletproof hosting service**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/us-charges-alleged-russian-bulletproof-hosting-service-operators/
- **Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands**: The Hacker News - https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html
- **Cribl Adds Agentic Detection Engineering \&amp; Boosts SecOps With CardinalOps Deal**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cribl-adds-agentic-detection-engineering-boosts-secops-with-cardinalops-deal
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
