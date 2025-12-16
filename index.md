# Exploitation Report

Critical zero-day vulnerabilities are currently being actively exploited across multiple platforms, with Apple WebKit flaws and Sierra Wireless router vulnerabilities leading the threat landscape. The React2Shell vulnerability continues to see widespread exploitation by multiple Chinese hacking groups, while new malware campaigns target browsers and enterprise systems. Ransomware groups are deploying new variants with implementation flaws that ironically allow victims to decrypt their own files, and sophisticated phishing campaigns are leveraging browser extensions and social engineering to bypass multi-factor authentication systems.

## Active Exploitation Details

### Apple WebKit Zero-Day Vulnerabilities
- **Description**: Two critical security flaws in Apple's WebKit browser engine that have been exploited in sophisticated attacks
- **Impact**: Attackers can execute arbitrary code and potentially gain full system control through browser exploitation
- **Status**: Actively exploited in the wild; Apple has released security updates for iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari

### Sierra Wireless AirLink ALEOS Router Vulnerability
- **Description**: High-severity flaw in Sierra Wireless AirLink ALEOS routers enabling remote code execution
- **Impact**: Attackers can achieve remote code execution on affected router devices, potentially compromising network infrastructure
- **Status**: Actively exploited; added to CISA's Known Exploited Vulnerabilities catalog

### React2Shell Remote Code Execution Vulnerability
- **Description**: Maximum-severity remote code execution vulnerability being exploited by multiple threat actors
- **Impact**: Complete system compromise through remote code execution capabilities
- **Status**: Widespread active exploitation with proof-of-concept exploits containing WAF bypass techniques
- **CVE ID**: CVE-2025-55182

### FreePBX Critical Authentication Bypass
- **Description**: Multiple vulnerabilities including SQL injection, file upload flaws, and AUTHTYPE bypass in the open-source PBX platform
- **Impact**: Authentication bypass leading to potential remote code execution on PBX systems
- **Status**: Recently patched; critical risk for unpatched systems

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari browser affected by WebKit vulnerabilities
- **Sierra Wireless Routers**: AirLink ALEOS router series vulnerable to remote code execution
- **FreePBX Systems**: Open-source private branch exchange platforms with multiple critical flaws
- **Chrome and Edge Browsers**: Extensions compromised in ShadyPanda campaign affecting millions of users
- **Windows Systems**: Recent security updates causing VPN and Message Queuing functionality failures
- **Enterprise Email Servers**: French Interior Ministry systems breached in targeted attack

## Attack Vectors and Techniques

- **Browser-Based Exploitation**: WebKit vulnerabilities exploited through malicious web content and browser interactions
- **Router Infrastructure Attacks**: Network device compromise through Sierra Wireless router vulnerabilities
- **Malicious Browser Extensions**: ShadyPanda campaign hijacking popular Chrome and Edge extensions to intercept AI chat sessions
- **ISO File Phishing**: Phantom Stealer malware distributed via malicious ISO files in phishing emails
- **GitHub Repository Abuse**: Fake OSINT and GPT utility repositories spreading PyStoreRAT malware
- **PayPal Subscription Abuse**: Legitimate PayPal billing features misused to send fraudulent purchase notifications
- **Memory-Based Malware**: SantaStealer operating in memory to evade file-based detection systems

## Threat Actor Activities

- **Chinese Hacking Groups**: Five additional groups linked to React2Shell exploitation campaigns targeting various sectors
- **ShadyPanda Campaign**: Massive browser extension hijacking operation intercepting millions of users' AI conversations
- **CyberVolk/GLORIAMIST**: Pro-Russian hacktivist group launching VolkLocker ransomware-as-a-service with cryptographic implementation flaws
- **RansomHouse**: Ransomware group responsible for Askul Corporation attack affecting 740,000 customer records
- **ShinyHunters**: Extortion gang targeting PornHub after Mixpanel data breach exposing Premium member activity
- **Financial Sector Targeting**: Active phishing campaigns hitting Russian finance sector with Phantom Stealer malware
- **French Government Targeting**: Sophisticated cyberattack compromising French Interior Ministry email servers