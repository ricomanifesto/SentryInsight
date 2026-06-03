# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities and active exploitation campaigns targeting high-value systems and users. Most concerning are zero-day attacks affecting Visual Studio Code that enable GitHub token theft through one-click exploitation, maximum-severity zero-days in Acer Wave 7 routers, and an actively exploited Android Framework vulnerability. Additionally, threat actors are leveraging AI-powered tools and automated attack frameworks to accelerate exploitation timelines, while established groups like Gamaredon continue exploiting known WinRAR vulnerabilities and emerging campaigns target WordPress installations through privilege escalation flaws.

## Active Exploitation Details

### Visual Studio Code GitHub Token Theft Zero-Day
- **Description**: A zero-day vulnerability in Microsoft Visual Studio Code that allows attackers to steal GitHub OAuth tokens through a one-click attack vector
- **Impact**: Complete theft of GitHub authentication tokens, potentially providing attackers with full access to victims' repositories and associated resources
- **Status**: Currently unpatched zero-day vulnerability with publicly available exploit code

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer Wave 7 mesh routers
- **Impact**: Complete compromise of router devices, potentially enabling network infiltration and lateral movement
- **Status**: Acer is working to patch these vulnerabilities, but fixes are not yet available

### Android Framework Zero-Day
- **Description**: High-severity vulnerability in Android's Framework component being actively exploited in targeted attacks
- **Impact**: System compromise on Android devices through targeted exploitation
- **Status**: Patched in Google's June 2026 Android security update

### Oracle WebLogic Server Vulnerability
- **Description**: High-severity flaw in Oracle WebLogic Server that has been actively exploited in attacks
- **Impact**: Server compromise and potential lateral movement within enterprise environments
- **Status**: Previously patched vulnerability now confirmed as actively exploited, added to CISA's KEV catalog
- **CVE ID**: CVE-2024-21182

### Kirki WordPress Plugin Privilege Escalation
- **Description**: Critical privilege escalation vulnerability in the Kirki plugin for WordPress
- **Impact**: Complete takeover of WordPress user accounts, including administrator accounts
- **Status**: Actively exploited in the wild to hijack WordPress admin accounts
- **CVE ID**: CVE-2026-8206

### Windows Search URI Hash Disclosure
- **Description**: Unpatched vulnerability in Windows Search URI functionality that allows attackers to steal NTLMv2 hashes
- **Impact**: Credential theft enabling further network compromise and lateral movement
- **Status**: Currently unpatched with active exploitation potential

### HTTP/2 Bomb DoS Vulnerability
- **Description**: Remote denial-of-service vulnerability affecting major web servers including NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora
- **Impact**: Service disruption through remote DoS attacks on web infrastructure
- **Status**: Active exploitation capability demonstrated against multiple major web server platforms

## Affected Systems and Products

- **Microsoft Visual Studio Code**: All versions vulnerable to GitHub token theft attack
- **Acer Wave 7 Routers**: All models affected by maximum-severity zero-day vulnerabilities
- **Android Framework**: Devices running vulnerable versions prior to June 2026 security patches
- **Oracle WebLogic Server**: Servers running unpatched versions vulnerable to active exploitation
- **WordPress with Kirki Plugin**: Sites using vulnerable Kirki plugin versions face privilege escalation risks
- **Windows Systems**: All Windows versions with Search URI functionality vulnerable to hash disclosure
- **Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora affected by HTTP/2 DoS vulnerability
- **WinRAR**: Continued exploitation by threat actors for malware delivery
- **Minecraft Gaming Platforms**: Over 116,000 systems infected through targeted malware campaigns

## Attack Vectors and Techniques

- **One-Click Exploitation**: VS Code vulnerability exploited through malicious links requiring single user interaction
- **Supply Chain Attacks**: Miasma campaign compromising Red Hat npm packages with credential-stealing worms
- **Social Engineering**: ClickFix and FakeUpdate campaigns using compromised websites for malware distribution
- **AI-Powered Automation**: Ransomware toolkits using artificial intelligence for EDR evasion and Active Directory discovery
- **Malware-as-a-Service**: WeedHack campaign targeting Minecraft players through YouTube-distributed malware
- **Archive Exploitation**: Continued use of WinRAR vulnerabilities for malware delivery and system compromise
- **HTTP/2 Protocol Abuse**: Denial-of-service attacks targeting web server implementations
- **AI Support Tool Manipulation**: Abuse of Meta's AI support systems to hijack Instagram accounts

## Threat Actor Activities

- **Gamaredon Group**: Russian-aligned group continuing to exploit WinRAR vulnerabilities to deliver GammaWorm and GammaSteel malware against Ukrainian targets
- **SideCopy Group**: Pakistan-linked actors targeting Afghanistan's Ministry of Finance with Xeno RAT through spear-phishing campaigns
- **DriveSurge Campaign**: Large-scale malware distribution using ClickFix and FakeUpdates techniques across thousands of compromised websites
- **WeedHack Operators**: Malware-as-a-service campaign infecting over 116,000 Minecraft gaming systems since January
- **Miasma Campaign**: Mini Shai-Hulud supply chain attackers compromising developer environments through poisoned npm packages
- **AI-Enhanced Threat Actors**: Various groups adopting artificial intelligence tools for automated reconnaissance, evasion, and attack execution
- **Instagram Account Hijackers**: Attackers manipulating Meta's AI-powered support tools to seize high-profile social media accounts