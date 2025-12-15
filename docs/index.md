# Exploitation Report

Critical zero-day vulnerabilities are under active exploitation across multiple platforms, with Apple WebKit flaws targeting specific individuals through sophisticated attacks, while FreePBX systems face remote code execution threats through authentication bypass vulnerabilities. Chinese threat actors have significantly escalated React2Shell exploitation campaigns, prompting emergency federal response directives. Additionally, Sierra Wireless router vulnerabilities are being actively exploited to enable remote code execution attacks, with CISA adding the flaw to its Known Exploited Vulnerabilities catalog.

## Active Exploitation Details

### Apple WebKit Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities in Apple's WebKit engine affecting Safari and other Apple applications across multiple platforms
- **Impact**: Attackers can execute sophisticated attacks targeting specific individuals, potentially leading to device compromise
- **Status**: Apple has released emergency security updates across all platforms including iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and Safari

### React2Shell Remote Code Execution Vulnerability
- **Description**: Maximum-severity remote code execution vulnerability that has escalated into large-scale global attacks
- **Impact**: Enables complete system compromise through remote code execution
- **Status**: Under active exploitation by multiple Chinese hacking groups; CISA has mandated federal agencies patch by December 12, 2025
- **CVE ID**: CVE-2025-55182

### Sierra Wireless Router Remote Code Execution Flaw
- **Description**: High-severity vulnerability in Sierra Wireless AirLink ALEOS routers
- **Impact**: Enables remote code execution attacks on affected router infrastructure
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### FreePBX Critical Authentication Bypass
- **Description**: Multiple critical vulnerabilities including SQL injection, file upload flaws, and AUTHTYPE bypass in FreePBX platform
- **Impact**: Can result in authentication bypass and remote code execution under certain conditions
- **Status**: Patches have been released by FreePBX

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS devices and Safari browser across all supported versions
- **React Applications**: Web applications utilizing React Server Components (RSC) vulnerable to denial-of-service and source code exposure
- **Sierra Wireless Routers**: AirLink ALEOS router models enabling critical infrastructure compromise
- **FreePBX Systems**: Open-source private branch exchange platforms with authentication and file upload vulnerabilities
- **Russian Finance Sector**: Organizations targeted by Phantom Stealer malware campaigns via ISO phishing emails

## Attack Vectors and Techniques

- **Browser-Based Exploitation**: WebKit vulnerabilities exploited through sophisticated web-based attacks targeting specific individuals
- **Mass Scanning Campaigns**: React2Shell exploits flooding the internet with automated scanning and exploitation attempts
- **WAF Bypass Techniques**: Proof-of-concept React2Shell exploits containing bypasses for web application firewall rules
- **Phishing with ISO Attachments**: Phantom Stealer distributed through malicious ISO files in targeted email campaigns
- **GitHub Repository Poisoning**: Fake OSINT and GPT utility repositories distributing PyStoreRAT malware payloads
- **Browser Extension Hijacking**: ShadyPanda campaign compromising popular Chrome and Edge extensions at massive scale
- **Torrent-Based Malware**: Fake movie torrents hiding malicious PowerShell loaders in subtitle files

## Threat Actor Activities

- **Chinese Hacking Groups**: Five additional Chinese groups linked to React2Shell exploitation campaigns, representing significant escalation in attack volume
- **ShadyPanda Campaign**: Cybercrime operation that hijacked popular browser extensions on Chrome and Edge at massive scale
- **CyberVolk/GLORIAMIST**: Pro-Russian hacktivist group launched VolkLocker ransomware-as-a-service with cryptographic implementation flaws
- **Phantom Stealer Operators**: Active phishing campaigns targeting Russian financial sector organizations with credential theft malware
- **PyStoreRAT Distributors**: Campaign leveraging GitHub-hosted repositories to distribute JavaScript-based remote access trojans