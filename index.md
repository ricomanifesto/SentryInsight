# Exploitation Report

## Executive Summary

Microsoft's July 2026 Patch Tuesday has set a new record with 570 to 622 vulnerabilities addressed, including three zero-day flaws—two confirmed under active exploitation and one publicly disclosed. This unprecedented volume significantly raises the stakes for vulnerability triage and patch deployment across enterprise environments. Simultaneously, active zero-day exploitation campaigns targeting SonicWall SMA1000 appliances and Progress ShareFile Storage Zone Controllers demand immediate remediation, as threat actors are leveraging these vulnerabilities in real-world attacks.

Beyond vendor patches, the threat landscape shows a surge in identity-focused and supply-chain attack vectors. At least two distinct threat actors are weaponizing OAuth client ID spoofing to validate stolen Microsoft Entra credentials, while new phishing kits—Jalisco and OmegaLord—are defeating multi-factor authentication to compromise Microsoft 365 accounts. A massive campaign involving nearly 300 malicious GitHub repositories impersonating legitimate software delivers infostealer malware, and the Cursor AI coding platform remains vulnerable to poisoned repository attacks that auto-execute malicious code.

Law enforcement and regulatory actions underscore the scale of cybercrime operations. Spanish authorities dismantled a €140 million fraud ring combining investment scams and business email compromise, while the U.S. Treasury sanctioned VPN and malware providers facilitating ransomware attacks. Emerging research highlights systemic risks in 6 GHz Wi-Fi automated frequency coordination, legacy Microsoft-signed UEFI shims bypassing Secure Boot, and RabbitMQ access control flaws exposing OAuth secrets across tenant boundaries.

## Active Exploitation Details

### Microsoft July 2026 Patch Tuesday Zero-Days
- **Description**: Microsoft's record-breaking Patch Tuesday release addressed 570–622 vulnerabilities across Windows and other Microsoft products. Three zero-day vulnerabilities were patched, with two confirmed as actively exploited in the wild and one publicly disclosed prior to the patch.
- **Impact**: Attackers exploiting the two active zero-days could achieve remote code execution, privilege escalation, or security feature bypass depending on the specific component affected. The breadth of the release—spanning Windows OS, Office, Azure, and development tools—means a wide attack surface is exposed until patches are applied.
- **Status**: Patches released July 2026. Active exploitation confirmed for two zero-days; one publicly disclosed. Organizations should prioritize deployment given the confirmed exploitation activity.
- **CVE ID**: Specific CVE IDs for the zero-days were not disclosed in the source articles.

### SonicWall SMA1000 Zero-Day Vulnerabilities
- **Description**: SonicWall disclosed two vulnerabilities in SMA1000 series appliances that are being exploited in zero-day attacks. The flaws affect the management interface of the secure mobile access appliances.
- **Impact**: Successful exploitation could allow unauthenticated attackers to execute arbitrary code, bypass authentication, or gain administrative access to the appliance, potentially providing a foothold into corporate networks via VPN access.
- **Status**: Actively exploited in the wild. SonicWall has released security updates and urges immediate patching.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

### Progress ShareFile Storage Zone Controller Zero-Day
- **Description**: Progress Software confirmed a high-severity zero-day vulnerability in ShareFile Storage Zone Controllers that prompted an emergency shutdown of the service last week. The flaw allows attackers to compromise the storage zone infrastructure.
- **Impact**: Exploitation could lead to unauthorized access to sensitive file shares, data exfiltration, or lateral movement within connected environments. The emergency shutdown indicates active, credible exploitation.
- **Status**: Security updates released following the emergency shutdown. Customers must apply patches and verify Storage Zone Controller integrity.
- **CVE ID**: Specific CVE ID not disclosed in the source article.

### OAuth Client ID Spoofing in Microsoft Entra ID
- **Description**: A novel evasion technique allowing attackers to spoof OAuth client IDs, enabling validation of stolen Microsoft Entra credentials while evading telemetry and detection. The technique abuses the OAuth authentication flow to enumerate and verify compromised credentials.
- **Impact**: Attackers can silently validate large volumes of stolen credentials, identify high-value accounts, and bypass conditional access policies without triggering standard authentication alerts.
- **Status**: Actively weaponized by at least two distinct threat actors in ongoing cloud campaigns. No patch available; requires detection logic updates and conditional access hardening.
- **CVE ID**: No CVE ID assigned; this is a technique exploiting protocol behavior.

### Cursor IDE Poisoned Repository Code Execution
- **Description**: The Cursor AI-powered IDE automatically executes code from repository configuration files (e.g., `.cursor/rules` or similar) when a repository is opened, without user interaction or explicit approval. Researchers reported the issue in December 2025; it remains unpatched as of July 2026.
- **Impact**: Developers cloning or opening malicious repositories—such as the nearly 300 fake GitHub repos distributing infostealers—trigger automatic code execution, leading to full system compromise, credential theft, and supply chain contamination.
- **Status**: Unpatched vulnerability. Cursor has not released a fix despite responsible disclosure. Mitigation requires disabling auto-execution features or avoiding untrusted repositories.
- **CVE ID**: No CVE ID disclosed in the source article.

### SonicWall SMA1000 Zero-Day Vulnerabilities
- **Description**: SonicWall disclosed two vulnerabilities in SMA1000 series appliances that are being exploited in zero-day attacks. The flaws affect the management interface of the secure mobile access appliances.
- **Impact**: Successful exploitation could allow unauthenticated attackers to execute arbitrary code, bypass authentication, or gain administrative access to the appliance, potentially providing a foothold into corporate networks via VPN access.
- **Status**: Actively exploited in the wild. SonicWall has released security updates and urges immediate patching.
- **CVE ID**: CVE-2026-15409, CVE-2026-15410

## Affected Systems and Products

- **Microsoft Windows (all supported versions)**: July 2026 Patch Tuesday covers 570–622 CVEs across Windows 10, Windows 11 (23H2, 24H2, 25H2), Windows Server, and associated components. Extended Security Updates (ESU) for Windows 10 delivered via KB5099539.
- **Microsoft Office and Microsoft 365 Apps**: Included in the Patch Tuesday release; phishing kits Jalisco and OmegaLord specifically target Microsoft 365 accounts with MFA evasion.
- **Microsoft Entra ID (Azure AD)**: Targeted by OAuth client ID spoofing campaigns validating stolen credentials; passkeys becoming default authentication method starting September 2026.
- **SonicWall SMA1000 Series Appliances**: Firmware versions prior to the July 2026 security update are vulnerable to CVE-2026-15409 and CVE-2026-15410 active exploitation.
- **Progress ShareFile Storage Zone Controllers**: On-premises storage zone components affected by the zero-day behind the emergency shutdown; all versions prior to the July 2026 patch.
- **SAP NetWeaver Application Server ABAP**: Critical CVSS 9.9 flaw addressed in July 2026 security updates; also affects SAP Commerce Cloud and AppRouter.
- **Cursor IDE (AI Coding Platform)**: All versions supporting automatic rule/configuration execution from repositories; vulnerability unpatched since December 2025 disclosure.
- **Claude for Chrome Browser Extension**: Vulnerable to cross-extension scripting attacks allowing rogue extensions to trigger Gmail, Google Docs, and Calendar access.
- **RabbitMQ Message Broker**: Versions with flawed access controls allowing OAuth client secret leakage and cross-tenant queue metadata exposure.
- **Linux Systems Using UEFI Secure Boot**: Systems trusting any of 11 legacy Microsoft-signed UEFI shims (GRUB2, shim loaders) that can be abused to bypass Secure Boot protections.
- **6 GHz Wi-Fi / AFC Systems**: Automated Frequency Coordination systems and client devices relying on unvalidated client-side location data.
- **GitHub / Software Supply Chain**: Nearly 300 malicious repositories impersonating legitimate tools (security scanners, CLI utilities, dev tools) distributing infostealer malware (Lumma, RedLine, etc.).
- **LastPass and Bitwarden Users**: Targeted by phishing campaigns using fake security alert emails directing to credential-harvesting sites.

## Attack Vectors and Techniques

- **Zero-Day Exploitation of Network Edge Devices**: Threat actors actively exploit unpatched vulnerabilities in VPN/appliance interfaces (SonicWall SMA1000, ShareFile Storage Zones) for initial access and persistence.
- **OAuth Client ID Spoofing**: Attackers register or manipulate OAuth application identities to mimic legitimate Microsoft first-party or trusted apps, enabling silent validation of stolen Entra credentials without triggering MFA or conditional access alerts.
- **MFA-Bypassing Phishing Kits (Jalisco, OmegaLord)**: Adversary-in-the-middle (AiTM) frameworks proxy authentication sessions in real time, capturing session tokens and bypassing Microsoft 365 MFA including number matching and FIDO2.
- **Fake Security Alert Phishing**: Social engineering emails impersonating LastPass/Bitwarden security notices lure users to credential-harvesting pages; leverages urgency and brand trust.
- **Supply Chain / Repository Poisoning**: Mass creation of typosquatted or branded GitHub repositories (300+) distributing trojanized software that delivers infostealers; combined with Cursor IDE auto-execution for developer targeting.
- **Cross-Extension Browser Exploitation**: Malicious Chrome extensions exploit over-permissive messaging APIs in legitimate extensions (Claude for Chrome) to exfiltrate Gmail, Docs, and Calendar data.
- **UEFI Secure Boot Bypass via Legacy Shims**: Attackers with local/admin access chain vulnerable Microsoft-signed UEFI applications (shims, GRUB2) to disable Secure Boot and deploy bootkits.
- **Automated Frequency Coordination (AFC) Spoofing**: Malicious 6 GHz Wi-Fi clients submit falsified geolocation data to AFC systems, causing incumbent protection failures and spectrum interference.
- **Business Email Compromise (BEC) at Scale**: Organized fraud ring combined investment scams with BEC, generating €140 million; leveraged credential harvesting, invoice manipulation, and money mule networks.
- **Ransomware Enablement via Bulletproof Services**: Sanctioned VPN providers (e.g., VPNLab-style) and malware developers (e.g., LockBit affiliates) offer infrastructure and tooling for ransomware deployment.

## Threat Actor Activities

- **Unknown Threat Actors (SonicWall SMA1000 Exploitation)**: Actively exploiting CVE-2026-15409 and CVE-2026-15410 in the wild against unpatched SMA1000 appliances; targeting VPN endpoints for network ingress.
- **Unknown Threat Actors (ShareFile Zero-Day)**: Exploited the high-severity ShareFile Storage Zone flaw prior to public disclosure, forcing Progress to emergency-shutdown the service; likely targeting sensitive file repositories.
- **Two Distinct Threat Actors (OAuth Client ID Spoofing)**: Separate campaigns weaponizing OAuth client ID spoofing to validate stolen Microsoft Entra credentials at scale; operating in cloud environments, evading telemetry via legitimate OAuth flows.
- **Jalisco and OmegaLord Phishing Kit Operators**: Deploying AiTM phishing infrastructure targeting Microsoft 365 enterprise accounts; kits sold/rented on underground forums with MFA-bypass capabilities.
- **GitHub Repository Poisoning Campaign Operator**: Single threat actor or group created nearly 300 fake repositories impersonating legitimate security and development tools; distributing Lumma, RedLine, and other infostealers to developers and CI/CD pipelines.
- **LabubaRAT Operators**: Deploying a novel Rust-based RAT masquerading as NVIDIA software (filenames, icons, metadata); targeting Windows hosts for persistent remote access and data theft.
- **Spanish Cyber Fraud Ring (Dismantled)**: Organized crime group conducting investment fraud ("pig butchering") and BEC attacks; stole €140 million ($160M); four arrests made, infrastructure seized.
- **Sanctioned Ransomware Enablers**: Two individuals and one entity designated by OFAC for providing VPN infrastructure and malware tooling to ransomware gangs (e.g., LockBit, Conti affiliates) targeting U.S. organizations.
- **ClickFix Ecosystem Operators**: Running a "phishing-as-a-service" platform renting fake CAPTCHA/verification pages that deliver malware via clipboard injection and script execution; evades AV/EDR through living-off-the-land techniques.

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
