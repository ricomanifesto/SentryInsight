# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with several zero-day vulnerabilities and actively exploited flaws creating significant security risks. Apple has patched two zero-day WebKit vulnerabilities being exploited in sophisticated attacks against specific individuals. Chinese threat actors are intensifying attacks against the React2Shell vulnerability, with Google linking five additional Chinese hacking groups to these campaigns. CISA has added a Sierra Wireless router flaw to its Known Exploited Vulnerabilities catalog due to active remote code execution attacks. Meanwhile, FreePBX systems face critical SQL injection and authentication bypass vulnerabilities that enable complete system compromise.

## Active Exploitation Details

### Apple WebKit Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities in Apple's WebKit browser engine exploited in extremely sophisticated attacks
- **Impact**: Attackers can execute arbitrary code and compromise Apple devices including iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari browsers
- **Status**: Patched by Apple in emergency security updates released Friday

### React2Shell Remote Code Execution Vulnerability
- **Description**: Maximum-severity remote code execution vulnerability being actively exploited by multiple Chinese threat groups
- **Impact**: Complete system compromise and remote code execution on affected systems
- **Status**: Under active exploitation with proof-of-concept exploits containing WAF bypass techniques flooding the internet
- **CVE ID**: CVE-2025-55182

### Sierra Wireless AirLink ALEOS Router Vulnerability
- **Description**: High-severity flaw in Sierra Wireless AirLink ALEOS routers enabling remote code execution
- **Impact**: Complete router compromise and potential network infiltration
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### FreePBX Critical Vulnerabilities
- **Description**: Multiple critical security flaws including SQL injection, file upload vulnerabilities, and AUTHTYPE bypass
- **Impact**: Authentication bypass and remote code execution on FreePBX systems
- **Status**: Patches released for the open-source PBX platform

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari browsers affected by WebKit zero-days
- **Sierra Wireless**: AirLink ALEOS routers vulnerable to remote code execution attacks
- **FreePBX**: Open-source private branch exchange platform with critical authentication and injection flaws
- **Chrome and Edge Extensions**: Browser extensions hijacked in ShadyPanda campaign affecting popular extensions
- **700Credit Systems**: Financial services platform breached exposing 5.8 million customer records
- **French Interior Ministry**: Email servers compromised in cyberattack
- **Windows Systems**: Recent security updates breaking WSL VPN functionality and Message Queuing services

## Attack Vectors and Techniques

- **WebKit Exploitation**: Sophisticated zero-day attacks targeting specific high-value individuals through browser vulnerabilities
- **Remote Code Execution**: Multiple attack vectors including React2Shell exploitation and router firmware flaws
- **Phishing Campaigns**: Advanced kits using AI and MFA bypass tactics including BlackForce, GhostFrame, InboxPrime AI, and Spiderman
- **Supply Chain Attacks**: Fake GitHub repositories distributing PyStoreRAT malware through OSINT and GPT utility projects
- **Browser Extension Hijacking**: ShadyPanda campaign compromising popular Chrome and Edge extensions
- **Malware Distribution**: Agent Tesla RAT hidden in fake movie torrents using subtitle files as infection vectors
- **Social Engineering**: PayPal subscription abuse for fake purchase notifications and sophisticated phishing emails

## Threat Actor Activities

- **Chinese APT Groups**: Five additional Chinese hacking groups linked to React2Shell vulnerability exploitation campaigns
- **CyberVolk (GLORIAMIST)**: Pro-Russian hacktivist group launched VolkLocker ransomware-as-a-service with cryptographic implementation flaws
- **ShadyPanda**: Cybercrime group conducting massive browser extension hijacking campaign targeting Chrome and Edge users
- **Phantom Stealer Operators**: Active phishing campaign targeting Russian finance sector using malicious ISO attachments
- **PyStoreRAT Campaign**: Threat actors using fake GitHub repositories to distribute JavaScript-based Remote Access Trojans