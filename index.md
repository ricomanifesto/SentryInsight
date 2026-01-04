# Exploitation Report

Critical cybersecurity threats are actively being exploited across multiple sectors, with significant focus on Fortinet firewall vulnerabilities, supply chain attacks targeting cryptocurrency platforms, and sophisticated botnet campaigns. Over 10,000 Fortinet firewalls remain vulnerable to a five-year-old two-factor authentication bypass vulnerability that is being actively exploited. The Shai-Hulud supply chain attack continues to evolve, impacting Trust Wallet and draining $8.5 million from cryptocurrency users. Additionally, new botnet campaigns including RondoDox and Kimwolf are targeting IoT devices and network infrastructure, while threat actors like Transparent Tribe are launching fresh RAT attacks against government and academic institutions.

## Active Exploitation Details

### Fortinet Two-Factor Authentication Bypass
- **Description**: A five-year-old vulnerability in Fortinet firewalls that allows attackers to bypass two-factor authentication mechanisms
- **Impact**: Complete authentication bypass, potentially allowing unauthorized administrative access to firewall systems
- **Status**: Actively exploited with over 10,000 Internet-exposed devices still vulnerable

### React2Shell Critical Vulnerability
- **Description**: Critical flaw exploited by the RondoDox botnet to compromise IoT devices and web servers
- **Impact**: Complete device compromise, enrollment into botnet infrastructure for malicious activities
- **Status**: Actively exploited in persistent nine-month campaign targeting IoT devices and web applications

### SmarterMail Remote Code Execution
- **Description**: Maximum-severity security flaw in SmarterTools SmarterMail email software
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Critical vulnerability with active exploitation potential
- **CVE ID**: CVE-2025-13915

### IBM API Connect Authentication Bypass
- **Description**: Critical security flaw in IBM API Connect authentication system
- **Impact**: Remote access to application, complete authentication bypass
- **Status**: Newly disclosed critical vulnerability
- **CVE ID**: CVE-2025-13915

## Affected Systems and Products

- **Fortinet Firewalls**: Over 10,000 Internet-exposed devices vulnerable to 2FA bypass
- **Trust Wallet Chrome Extension**: Cryptocurrency wallet platform affected by supply chain attack
- **macOS Systems**: Targeted by GlassWorm malware campaign through trojanized crypto wallet applications
- **IoT Devices**: Compromised by RondoDox botnet through React2Shell vulnerability exploitation
- **SmarterTools SmarterMail**: Email software vulnerable to remote code execution
- **IBM API Connect**: Authentication system vulnerable to remote access attacks
- **npm Registry**: Targeted by modified Shai-Hulud worm variants
- **Browser Extensions**: 8.8 million users impacted by DarkSpectre campaign across multiple platforms

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Shai-Hulud campaigns targeting npm packages and browser extensions
- **Malicious Browser Extensions**: DarkSpectre campaign impacting 2.2 million users through ShadyPanda and GhostPoster variants
- **Trojanized Applications**: GlassWorm campaign using malicious VSCode/OpenVSX extensions to deliver compromised crypto wallets
- **Botnet Enrollment**: RondoDox leveraging React2Shell vulnerability for persistent IoT device compromise
- **Authentication Bypass**: Multi-year exploitation of Fortinet 2FA vulnerabilities
- **Remote Access Trojans**: Transparent Tribe deploying new RAT variants against government targets
- **Phishing Campaigns**: Abuse of Google Cloud Application Integration features for multi-stage attacks

## Threat Actor Activities

- **ShinyHunters**: Claims breach of cybersecurity firm Resecurity, though firm reports it was a honeypot operation
- **Transparent Tribe**: Launching fresh RAT attacks targeting Indian governmental, academic, and strategic entities
- **RondoDox Operators**: Conducting persistent nine-month campaign targeting IoT devices and web applications
- **Shai-Hulud Attackers**: Evolving supply chain attack methodology with modified worm variants on npm registry
- **DarkSpectre Campaign**: Attribution to threat actor behind ShadyPanda and GhostPoster browser extension campaigns
- **Cryptocurrency Thieves**: Ongoing exploitation of 2022 LastPass breach data for wallet compromise operations
- **GlassWorm Campaign**: Fourth wave targeting macOS developers through malicious development tool extensions