# Exploitation Report

Multiple critical zero-day vulnerabilities and ransomware campaigns are currently threatening organizations worldwide. Apple has patched two WebKit vulnerabilities that were actively exploited in sophisticated attacks, while CISA has added a Sierra Wireless router flaw to its Known Exploited Vulnerabilities catalog due to ongoing remote code execution attacks. The React2Shell vulnerability continues to see widespread exploitation by multiple Chinese hacking groups, with proof-of-concept exploits now including WAF bypass techniques. Additionally, several major data breaches have been confirmed, including incidents affecting SoundCloud, Askul Corporation, and 700Credit, impacting millions of users. New malware families including SantaStealer, VolkLocker ransomware, and PyStoreRAT are actively being deployed through various attack vectors.

## Active Exploitation Details

### Apple WebKit Vulnerabilities
- **Description**: Two security flaws in Apple's WebKit engine discovered and exploited in sophisticated attacks
- **Impact**: Attackers can execute arbitrary code on affected Apple devices through malicious web content
- **Status**: Patches released by Apple for iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari browser

### Sierra Wireless AirLink ALEOS Router Vulnerability
- **Description**: High-severity flaw in Sierra Wireless AirLink ALEOS routers enabling remote code execution
- **Impact**: Attackers can gain unauthorized remote access and execute arbitrary commands on affected router systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### React2Shell Vulnerability
- **Description**: Maximum-severity remote code execution vulnerability being exploited by multiple threat actors
- **Impact**: Enables complete system compromise through remote code execution
- **Status**: Widespread exploitation ongoing with WAF bypass techniques being incorporated into proof-of-concept exploits
- **CVE ID**: CVE-2025-55182

### FreePBX Multiple Critical Vulnerabilities
- **Description**: Multiple security vulnerabilities including SQL injection, file upload, and authentication bypass flaws
- **Impact**: Remote code execution and complete system compromise of FreePBX installations
- **Status**: Critical patches released for the open-source PBX platform

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS devices and Safari browser affected by WebKit vulnerabilities
- **Sierra Wireless Routers**: AirLink ALEOS router models vulnerable to remote code execution attacks
- **FreePBX Systems**: Open-source private branch exchange platforms with multiple critical security flaws
- **SoundCloud Platform**: Audio streaming service compromised with user database stolen and VPN access disrupted
- **Google Chrome Extensions**: Millions of users affected by malicious browser extensions intercepting AI chat data
- **700Credit Services**: Financial services platform breach affecting 5.8 million vehicle dealership customers
- **Askul Corporation**: Japanese e-commerce platform with 740,000 customer records stolen
- **French Interior Ministry**: Government email servers compromised in cyberattack

## Attack Vectors and Techniques

- **Browser-Based Exploitation**: Malicious web content targeting WebKit vulnerabilities in Apple devices
- **Network Infrastructure Attacks**: Remote exploitation of router vulnerabilities for persistent access
- **Malicious Browser Extensions**: Chrome extensions with millions of users silently intercepting AI chatbot interactions
- **Ransomware Campaigns**: RansomHouse group targeting major corporations for data theft and encryption
- **Phishing and Social Engineering**: ISO file attachments delivering Phantom Stealer malware to Russian finance sector
- **GitHub Repository Abuse**: Fake OSINT and GPT utility repositories distributing PyStoreRAT malware
- **Malware-as-a-Service**: SantaStealer operating as MaaS platform for credential theft from browsers and crypto wallets
- **PayPal Subscription Abuse**: Legitimate PayPal billing features exploited to send convincing fake purchase notifications

## Threat Actor Activities

- **Chinese Hacking Groups**: Five additional Chinese groups linked to React2Shell exploitation campaigns targeting critical infrastructure
- **CyberVolk/GLORIAMIST**: Pro-Russian hacktivist group deploying VolkLocker ransomware with implementation flaws allowing free decryption
- **RansomHouse**: Active ransomware operations against major corporations including Askul Corporation with large-scale data theft
- **ShinyHunters**: Extortion gang targeting PornHub after allegedly stealing Premium member activity data through Mixpanel breach
- **ShadyPanda Campaign**: Large-scale browser extension hijacking campaign affecting millions of Chrome and Edge users
- **Russian Finance Sector Targeting**: Phantom Stealer campaigns specifically targeting Russian financial institutions through phishing emails