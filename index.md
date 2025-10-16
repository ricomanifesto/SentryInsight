# Exploitation Report

Critical exploitation activity is currently dominated by several maximum-severity vulnerabilities actively being exploited in the wild. CISA has flagged a perfect 10.0 CVSS score Adobe Experience Manager flaw that attackers are actively exploiting to execute code on unpatched systems. Additionally, two new Windows zero-day vulnerabilities are under active exploitation, with one affecting every version of Windows ever shipped. The threat landscape is further complicated by sophisticated attack campaigns including North Korean hackers using blockchain-based malware hiding techniques, Chinese threat groups infiltrating Russian networks, and ransomware operations targeting major institutions through Oracle zero-day attacks. Supply chain risks are also emerging with over 100 VS Code extensions exposing developers to hidden threats, while industrial control systems face critical risks from newly disclosed remote terminal unit vulnerabilities.

## Active Exploitation Details

### Adobe Experience Manager Vulnerability
- **Description**: Maximum-severity vulnerability in Adobe Experience Manager with a perfect 10.0 CVSS score
- **Impact**: Allows attackers to execute arbitrary code on unpatched systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities (KEV) catalog

### Windows Zero-Day Vulnerabilities
- **Description**: Two new zero-day vulnerabilities affecting Windows systems, with one impacting every version of Windows ever shipped
- **Impact**: Active exploitation allowing unauthorized system access and control
- **Status**: Microsoft released fixes for these vulnerabilities as part of addressing 183 security flaws

### Cisco IOS Software SNMP Vulnerability
- **Description**: Security flaw in Cisco IOS Software and IOS XE Software exploited in "Zero Disco" attacks
- **Impact**: Allows deployment of Linux rootkits on older systems
- **Status**: Recently disclosed and actively exploited to compromise network infrastructure

### ICTBroadcast Cookie Exploit
- **Description**: Critical security flaw in ICTBroadcast autodialer software from ICT Innovations
- **Impact**: Remote shell access through cookie exploitation
- **Status**: Under active exploitation in the wild

### Oracle Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Oracle systems exploited by Clop ransomware group
- **Impact**: Data theft and system compromise affecting major institutions
- **Status**: Actively exploited in targeted attacks against Oracle customers

### F5 BIG-IP Vulnerabilities
- **Description**: Multiple security vulnerabilities in F5 BIG-IP systems, with details stolen during a nation-state breach
- **Impact**: Potential system compromise and unauthorized access
- **Status**: Patches released for vulnerabilities exposed through the breach

## Affected Systems and Products

- **Adobe Experience Manager**: Critical vulnerability requiring immediate patching
- **Windows Systems**: All versions affected by at least one zero-day vulnerability
- **Cisco IOS/IOS XE**: Network devices vulnerable to SNMP-based attacks
- **ICTBroadcast**: Autodialer software systems exposed to cookie-based exploits
- **Oracle Systems**: Various Oracle products targeted in zero-day attacks
- **F5 BIG-IP**: Network infrastructure devices compromised in nation-state attack
- **Red Lion Sixnet RTUs**: Industrial control systems with two CVSS 10.0 vulnerabilities
- **VS Code Extensions**: Over 100 extensions with leaked access tokens
- **Windows Server 2025**: Active Directory issues from September security updates

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean hackers hiding malware on blockchain networks for stealth and resilience
- **Cookie Exploitation**: Remote shell access through manipulated authentication cookies
- **SNMP Protocol Abuse**: Exploiting network management protocols to deploy rootkits
- **Zero-Day Exploitation**: Targeting unpatched vulnerabilities in widely-used software
- **Supply Chain Attacks**: Compromising development tools and extensions
- **Social Engineering**: Fake breach notifications targeting password manager users
- **Nation-State Intrusion**: Advanced persistent threats targeting critical infrastructure

## Threat Actor Activities

- **North Korean Hackers**: Employing EtherHiding tactics for cryptocurrency theft and espionage using blockchain-based malware delivery
- **Clop Ransomware Group**: Exploiting Oracle zero-day vulnerabilities to steal data from major institutions including Harvard University
- **Chinese Threat Group Jewelbug**: Five-month infiltration of Russian IT service providers, expanding operations beyond Southeast Asia
- **Mysterious Elephant**: Cyber-espionage group using sophisticated custom tools to target government and diplomatic entities in South Asia
- **Nation-State Actors**: Breaching F5 systems and stealing BIG-IP source code and vulnerability information
- **Phishing Campaigns**: Targeting LastPass and Bitwarden users with fake breach notifications leading to system hijacks