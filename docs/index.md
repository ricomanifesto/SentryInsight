# Exploitation Report

Critical zero-day vulnerabilities and active exploitation campaigns are dominating the threat landscape, with attackers targeting everything from development tools to network infrastructure. The most severe activity includes maximum-severity zero-days in Acer Wave 7 routers, active exploitation of Android and Linux kernel vulnerabilities warned by CISA, and privilege escalation attacks against WordPress sites using the Kirki plugin (CVE-2026-8206). Additionally, threat actors are leveraging unpatched Windows Search URI vulnerabilities to steal authentication hashes, exploiting Visual Studio Code to steal GitHub tokens, and conducting sophisticated campaigns using AI-built ransomware toolkits that automate evasion techniques.

## Active Exploitation Details

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer Wave 7 mesh routers
- **Impact**: Complete system compromise with highest possible severity rating
- **Status**: Acer is actively working on patches, vulnerabilities currently unpatched

### Android and Linux Kernel Vulnerabilities
- **Description**: Multiple vulnerabilities in Linux kernel and Android operating system being actively exploited
- **Impact**: System compromise and unauthorized access to affected devices
- **Status**: CISA has issued active exploitation warnings, patches may be available

### WordPress Kirki Plugin Privilege Escalation
- **Description**: Critical privilege escalation vulnerability in the Kirki plugin for WordPress
- **Impact**: Complete takeover of user accounts, including administrator accounts
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-8206

### Visual Studio Code GitHub Token Theft
- **Description**: Zero-day vulnerability in Microsoft Visual Studio Code enabling one-click GitHub token theft
- **Impact**: Theft of GitHub authentication tokens through malicious link clicks
- **Status**: Exploit code publicly released, vulnerability unpatched

### Windows Search URI Hash Disclosure
- **Description**: Unpatched vulnerability in Windows Search URI functionality
- **Impact**: Disclosure of user NTLMv2 hashes to attackers
- **Status**: Currently unpatched, similar to previously disclosed issues

### Oracle WebLogic Server Vulnerability
- **Description**: High-severity security flaw in Oracle WebLogic Server
- **Impact**: Remote code execution and system compromise
- **Status**: Added to CISA KEV catalog due to active exploitation
- **CVE ID**: CVE-2024-21182

### HTTP/2 Bomb Vulnerability
- **Description**: Remote denial-of-service vulnerability affecting major web servers
- **Impact**: Service disruption through resource exhaustion attacks
- **Status**: Affects multiple major platforms including NGINX, Apache, Microsoft IIS, Envoy, and Cloudflare

### Android Framework Component Vulnerability
- **Description**: High-severity flaw in Android Framework component
- **Impact**: System compromise on affected Android devices
- **Status**: Actively exploited, patched in Google's June 2026 Android security update

## Affected Systems and Products

- **Acer Wave 7 Mesh Routers**: All versions affected by maximum-severity zero-days
- **Android Operating System**: Multiple versions affected by kernel and framework vulnerabilities
- **Linux Kernel**: Various distributions affected by actively exploited vulnerabilities
- **WordPress Sites**: Sites using vulnerable Kirki plugin versions
- **Microsoft Visual Studio Code**: All versions vulnerable to GitHub token theft
- **Windows Systems**: All versions affected by unpatched Search URI vulnerability
- **Oracle WebLogic Server**: Specific versions vulnerable to remote code execution
- **Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora affected by HTTP/2 vulnerability
- **WinRAR**: Exploited by Gamaredon group for malware delivery

## Attack Vectors and Techniques

- **One-Click Exploitation**: VS Code vulnerability allows GitHub token theft through malicious links
- **Privilege Escalation**: WordPress Kirki plugin exploited for administrative account takeover
- **Hash Disclosure**: Windows Search URI vulnerability used to steal NTLMv2 authentication hashes
- **Social Engineering**: Google Gemini voice assistant targeted with prompt injection for malicious notifications
- **Malware Distribution**: WeedHack campaign targeting Minecraft players through YouTube
- **AI-Assisted Attacks**: Ransomware toolkit using artificial intelligence for EDR evasion and Active Directory discovery
- **HTTP/2 Resource Exhaustion**: Denial-of-service attacks against major web server platforms
- **Archive File Exploitation**: WinRAR vulnerabilities used for malware payload delivery

## Threat Actor Activities

- **Gamaredon Group**: Russian hacking group exploiting WinRAR vulnerabilities to deliver GammaWorm and GammaSteel malware targeting Ukraine
- **Chinese APT Operations**: Dual-method spear-phishing campaigns against Czech organizations using Azureveil malware
- **WeedHack Campaign**: Large-scale operation targeting Minecraft players, infecting over 116,000 systems since January
- **DriveSurge Operation**: Wide-scale initial access broker using malicious traffic distribution systems for ClickFix and FakeUpdate attacks
- **Kali365 Phishing Service**: FBI-flagged phishing-as-a-service platform expanding from Microsoft 365 to AWS, Okta, and Russian platforms
- **AI-Powered Ransomware Groups**: Threat actors using artificial intelligence to automate attack processes and evasion techniques
- **Stock Exchange Attackers**: Sophisticated threat actors conducting months-long email campaigns against financial institutions using legitimate Windows tools