# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms through sophisticated attack vectors. CISA has identified active exploitation of a Magento RCE vulnerability CVE-2026-45247 affecting Cache Warmer extensions, prompting its addition to the Known Exploited Vulnerabilities catalog. Attackers are actively exploiting Android and Linux kernel vulnerabilities, while Acer Wave 7 routers face maximum-severity zero-day vulnerabilities. Additional concerns include unpatched Windows Search URI vulnerabilities enabling NTLM hash theft, Microsoft 365 Android apps leaking account tokens through debug flags, and Google Gemini prompt injection flaws allowing notification-based attacks.

## Active Exploitation Details

### Magento Cache Warmer RCE Vulnerability
- **Description**: Critical remote code execution flaw in Mirasvit Cache Warmer, a popular Magento full-page cache extension
- **Impact**: Attackers can execute arbitrary code remotely on affected Magento installations
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-45247

### Android and Linux Kernel Vulnerabilities
- **Description**: Multiple vulnerabilities affecting the Linux kernel and Android operating system
- **Impact**: System compromise and privilege escalation capabilities
- **Status**: CISA warns of active exploitation targeting these platforms

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities in Acer Wave 7 mesh routers
- **Impact**: Complete device compromise with maximum CVSS severity rating
- **Status**: Zero-day vulnerabilities with patches in development

### Windows Search URI Vulnerability
- **Description**: Unpatched vulnerability in Windows Search URI handling that enables credential theft
- **Impact**: Attackers can steal NTLMv2 hashes from targeted users
- **Status**: Unpatched vulnerability with active exploitation potential

### Redis Use-After-Free Vulnerability
- **Description**: Use-after-free vulnerability in Redis blocking-client code discovered by autonomous AI tools
- **Impact**: Authenticated users can execute arbitrary OS commands on the database server
- **Status**: Patched vulnerability that existed undetected for 2 years
- **CVE ID**: CVE-2026-23479

## Affected Systems and Products

- **Magento Installations**: Sites using Mirasvit Cache Warmer extension vulnerable to RCE attacks
- **Android Devices**: Multiple Android versions affected by kernel vulnerabilities under active exploitation
- **Linux Systems**: Various Linux distributions impacted by kernel vulnerabilities
- **Acer Wave 7 Routers**: All Wave 7 mesh router models vulnerable to maximum-severity zero-days
- **Windows Systems**: All Windows versions with Search functionality vulnerable to NTLM hash theft
- **Microsoft 365 Android Apps**: Word, PowerPoint, Excel, and other M365 Android applications with token leakage
- **Redis Databases**: Redis installations vulnerable to authenticated RCE through use-after-free bug
- **Google Gemini**: Android voice assistant vulnerable to prompt injection via notifications

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of Magento Cache Warmer extension for server compromise
- **Kernel Exploitation**: Direct targeting of Linux and Android kernel vulnerabilities for system access
- **Zero-Day Exploitation**: Active use of unpatched Acer router vulnerabilities for device takeover
- **Credential Harvesting**: Windows Search URI manipulation to steal NTLMv2 authentication hashes
- **Token Theft**: Exploitation of Microsoft 365 debug flags to steal authentication tokens
- **Prompt Injection**: Malicious notifications used to hijack Google Gemini voice assistant functionality
- **HTTP/2 Bomb Attacks**: New denial-of-service technique capable of crashing web servers within minutes
- **Traffic Distribution Systems**: Fake open-source tool websites used to distribute malware through search engine manipulation

## Threat Actor Activities

- **Chinese-Speaking Groups**: Deployment of new Atlas RAT malware in European cyberattacks with expanded targeting
- **Pakistani Threat Actors**: Espionage operations against Afghan Finance Ministry using Xeno RAT malware
- **Unknown Attackers**: Five-month persistent access to major stock exchange executive's Outlook mailbox
- **Cybercriminal Operations**: Large-scale impersonation of open-source projects for malware distribution
- **Ransomware Groups**: Iranian actors utilizing sanctioned Nobitex cryptocurrency exchange for payment processing
- **Nation-State Actors**: China-linked espionage targeting at least twelve Latin American nations for geopolitical intelligence gathering