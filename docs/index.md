# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems with several high-impact vulnerabilities under active attack. The most severe concerns include a critical remote code execution flaw in MetInfo CMS (CVE-2026-29014), a critical authentication bypass vulnerability in Weaver E-cology (CVE-2026-22679) that has been exploited since March, and a critical authentication bypass flaw affecting Progress MOVEit Automation systems. Additional threats include sophisticated supply chain attacks by North Korean APT groups, widespread phishing campaigns leveraging legitimate cloud services, and multiple data breaches affecting major platforms including Vimeo and Trellix.

## Active Exploitation Details

### MetInfo CMS Remote Code Execution
- **Description**: Critical security flaw in the open-source MetInfo content management system enabling remote code execution attacks
- **Impact**: Complete system compromise allowing attackers to execute arbitrary code on affected servers
- **Status**: Under active exploitation in the wild according to VulnCheck findings
- **CVE ID**: CVE-2026-29014

### Weaver E-cology Debug API Vulnerability
- **Description**: Critical remote code execution vulnerability in the Weaver (Fanwei) E-cology enterprise office automation platform exploitable via debug API
- **Impact**: Allows attackers to execute discovery commands and potentially gain full system access
- **Status**: Actively exploited since mid-March 2025
- **CVE ID**: CVE-2026-22679

### Progress MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress MOVEit Automation enterprise-grade managed file transfer application
- **Impact**: Complete authentication bypass allowing unauthorized access to file transfer systems
- **Status**: Recently patched by Progress Software, exploitation status unclear

### Microsoft Edge Password Storage Vulnerability
- **Description**: Security issue where Microsoft Edge stores passwords in process memory, exposing them to extraction
- **Impact**: Administrative users can exploit this to steal stored passwords for further malicious activity
- **Status**: Proof-of-concept exploit available, poses enterprise risk

## Affected Systems and Products

- **MetInfo CMS**: Open-source content management system vulnerable to remote code execution
- **Weaver E-cology**: Enterprise office automation and collaboration platform with debug API vulnerability
- **Progress MOVEit Automation**: Enterprise managed file transfer application with authentication bypass flaw
- **Microsoft Edge**: Password storage vulnerability affecting enterprise deployments
- **Vimeo Platform**: Video platform compromised by ShinyHunters gang affecting 119,000 users
- **Trellix Systems**: Cybersecurity firm's source code repository compromised in data breach
- **Gaming Platforms**: Video game platforms compromised for supply chain attacks
- **PyTorch Lightning**: Malicious package on Python Package Index delivering credential stealers

## Attack Vectors and Techniques

- **Supply Chain Attacks**: North Korean ScarCruft group compromising gaming platforms to deploy BirdCall malware on Android and Windows systems
- **Phishing Campaigns**: Large-scale credential theft targeting 35,000 users across 26 countries using code of conduct themes
- **RMM Tool Abuse**: Attackers leveraging SimpleHelp and ScreenConnect remote monitoring tools to evade detection across 80+ organizations
- **Cloud Service Abuse**: Amazon SES increasingly used for phishing to bypass security filters and reputation-based blocks
- **OAuth Token Exploitation**: Persistent OAuth tokens from AI tools and productivity apps creating backdoor access
- **Package Repository Compromise**: Backdoored PyTorch Lightning packages delivering credential-stealing payloads

## Threat Actor Activities

- **ScarCruft (APT37)**: North Korean state-sponsored group conducting supply chain espionage through compromised gaming platforms, deploying BirdCall backdoor on Android and Windows
- **UAT-8302**: China-linked APT group targeting government entities in South America and southern regions using shared malware infrastructure
- **ShinyHunters**: Extortion gang responsible for Vimeo data breach exposing 119,000 users' personal information
- **Silver Fox**: China-backed APT group conducting tax-themed attacks against organizations in India and Russia, targeting over 1,600 victims with ABCDoor backdoor and ValleyRAT
- **Karakurt Group**: Russian ransomware operation with members receiving prison sentences for extortion activities
- **CloudZ Operators**: Deploying new malware variants that abuse Microsoft Phone Link to steal SMS and OTP codes