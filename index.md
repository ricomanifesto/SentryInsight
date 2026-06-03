# Exploitation Report

The current threat landscape reveals a concerning escalation in exploitation activities targeting diverse platforms and technologies. Critical zero-day vulnerabilities are being actively exploited across multiple vectors, including a Visual Studio Code vulnerability enabling GitHub token theft through social engineering, maximum-severity zero-days in Acer Wave 7 routers, and an unpatched Windows Search URI vulnerability exposing NTLMv2 hashes. Simultaneously, established vulnerabilities continue to be weaponized by threat actors, with Russian-linked Gamaredon exploiting WinRAR flaws and Oracle WebLogic servers being targeted in active campaigns. The emergence of AI-assisted attack toolkits and novel attack vectors like HTTP/2 bomb exploits demonstrates the evolving sophistication of modern cyber threats, while large-scale malware campaigns are successfully compromising hundreds of thousands of systems through gaming platforms and compromised websites.

## Active Exploitation Details

### Visual Studio Code GitHub Token Theft Zero-Day
- **Description**: A one-click attack vulnerability in Microsoft Visual Studio Code that allows attackers to steal GitHub OAuth tokens by tricking users into clicking malicious links
- **Impact**: Complete compromise of GitHub authentication tokens, potentially leading to unauthorized repository access and code theft
- **Status**: Zero-day vulnerability with exploit code publicly released; no patch available

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer Wave 7 mesh routers
- **Impact**: Complete system compromise with maximum CVSS severity rating
- **Status**: Actively exploitable; Acer working on patches

### Windows Search URI NTLMv2 Hash Disclosure
- **Description**: Unpatched vulnerability in Windows Search URI handling that can be exploited to disclose user NTLMv2 hashes to attackers
- **Impact**: Credential theft enabling lateral movement and privilege escalation
- **Status**: Unpatched and actively exploitable
- **CVE ID**: CVE-2026-33829

### Android Framework Zero-Day
- **Description**: High-severity vulnerability in Android Framework component being exploited in targeted attacks
- **Impact**: Potential for privilege escalation and unauthorized access on affected Android devices
- **Status**: Patched in June 2026 Android security update but previously exploited in the wild

### Oracle WebLogic Server Vulnerability
- **Description**: High-severity vulnerability in Oracle WebLogic Server that has been added to CISA's KEV catalog
- **Impact**: Remote code execution and system compromise
- **Status**: Actively exploited despite being patched two years ago
- **CVE ID**: CVE-2024-21182

### WordPress Kirki Plugin Privilege Escalation
- **Description**: Critical privilege escalation vulnerability in the Kirki plugin for WordPress enabling account takeover
- **Impact**: Complete takeover of WordPress administrator accounts and site compromise
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-8206

### HTTP/2 Bomb DoS Vulnerability
- **Description**: Remote denial-of-service exploit affecting major web servers through HTTP/2 protocol manipulation
- **Impact**: Service disruption and potential server crashes
- **Status**: Affects multiple major web server platforms including NGINX, Apache, IIS, Envoy, and Cloudflare

### WinRAR Vulnerability
- **Description**: Vulnerability in WinRAR being exploited by Russian threat actors to deliver malware
- **Impact**: Malware delivery and system compromise targeting Ukrainian entities
- **Status**: Actively exploited by Gamaredon group

## Affected Systems and Products

- **Microsoft Visual Studio Code**: All versions vulnerable to GitHub token theft attack
- **Acer Wave 7 Mesh Routers**: All models affected by maximum-severity zero-days
- **Windows Operating Systems**: All versions with Search URI functionality vulnerable to NTLMv2 hash disclosure
- **Android Devices**: Framework component affected in targeted attacks, patched in June 2026
- **Oracle WebLogic Server**: All unpatched versions vulnerable to remote exploitation
- **WordPress Kirki Plugin**: All versions prior to security update vulnerable to privilege escalation
- **Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora affected by HTTP/2 bomb
- **WinRAR Applications**: Versions vulnerable to exploitation by Gamaredon group
- **Red Hat npm Packages**: @redhat-cloud-services packages compromised in supply chain attack
- **Minecraft Gaming Platform**: Over 116,000 systems infected through WeedHack campaign

## Attack Vectors and Techniques

- **Social Engineering via VS Code**: One-click attacks through malicious links targeting developer workflows
- **Router Exploitation**: Direct targeting of consumer networking equipment with zero-day exploits
- **Protocol Manipulation**: HTTP/2 bomb attacks causing denial-of-service through protocol abuse
- **Supply Chain Attacks**: Compromise of legitimate npm packages to deliver credential-stealing worms
- **Gaming Platform Targeting**: Malware distribution through Minecraft-focused campaigns on YouTube
- **AI-Assisted Social Engineering**: Abuse of Meta's AI support systems to hijack Instagram accounts
- **Brute Force Attacks**: Password vault targeting through automated credential attacks
- **Website Compromise**: Large-scale injection of ClickFix and FakeUpdate attack scripts
- **Archive File Exploitation**: WinRAR vulnerability exploitation for malware delivery
- **WordPress Plugin Attacks**: Direct exploitation of CMS plugin vulnerabilities for privilege escalation

## Threat Actor Activities

- **Gamaredon (Russian APT)**: Continued exploitation of WinRAR vulnerabilities to deliver GammaWorm and GammaSteel malware targeting Ukrainian infrastructure
- **SideCopy (Pakistan-linked)**: Spear-phishing campaign against Afghanistan's Ministry of Finance using Xeno RAT malware
- **DriveSurge**: Large-scale malware distribution using ClickFix and FakeUpdate techniques across thousands of compromised websites
- **WeedHack Campaign**: Targeting Minecraft players through YouTube with over 116,000 systems infected since January
- **AI-Enhanced Ransomware Groups**: Development of automated attack toolkits using artificial intelligence for EDR evasion and Active Directory discovery
- **Miasma Campaign**: Supply chain attack targeting Red Hat npm packages with credential-stealing capabilities
- **Instagram Account Hijackers**: Exploitation of Meta's AI support systems to gain unauthorized access to high-profile accounts including Obama White House and U.S. Space Force accounts