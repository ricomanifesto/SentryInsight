# Exploitation Report

Current cybersecurity landscape reveals critical active exploitation across multiple attack vectors. Most notably, over 10,000 Fortinet firewalls remain vulnerable to a five-year-old two-factor authentication bypass vulnerability that attackers are actively exploiting. The RondoDox botnet has been conducting a persistent nine-month campaign exploiting the React2Shell vulnerability to compromise IoT devices and web servers. Additionally, the Kimwolf botnet is exploiting vulnerabilities that have been active for months, posing significant threats to local networks. Supply chain attacks continue to plague the ecosystem, with the Shai-Hulud attack linked to major cryptocurrency thefts, including an $8.5 million breach of Trust Wallet and the compromise of over 8.8 million users through malicious browser extensions.

## Active Exploitation Details

### **Fortinet Firewall 2FA Bypass Vulnerability**
- **Description**: A five-year-old two-factor authentication bypass vulnerability affecting Fortinet firewalls
- **Impact**: Attackers can bypass 2FA mechanisms to gain unauthorized access to firewall systems
- **Status**: Actively exploited with over 10,000 Internet-exposed devices still vulnerable

### **React2Shell Vulnerability**
- **Description**: Critical vulnerability being exploited by the RondoDox botnet in a nine-month-long persistent campaign
- **Impact**: Allows attackers to hijack IoT devices and web servers, enrolling them into botnets
- **Status**: Active exploitation ongoing for nine months targeting IoT infrastructure

### **Kimwolf Botnet Exploited Vulnerability**
- **Description**: Vulnerability that has been exploited for months by the Kimwolf botnet
- **Impact**: Enables botnet operators to compromise local network infrastructure
- **Status**: Active exploitation for several months with urgent security advisory issued

### **IBM API Connect Authentication System Flaw**
- **Description**: Critical authentication system vulnerability in IBM API Connect
- **Impact**: Could allow attackers to gain remote access to API Connect applications
- **Status**: Critical severity with CVSS score of 9.8
- **CVE ID**: CVE-2025-13915

## Affected Systems and Products

- **Fortinet Firewalls**: Over 10,000 Internet-exposed devices vulnerable to 2FA bypass attacks
- **IoT Devices**: Targeted by RondoDox botnet through React2Shell vulnerability exploitation
- **Web Servers**: Compromised by RondoDox botnet operations for nine months
- **npm Registry**: Affected by Shai-Hulud worm variants targeting JavaScript package ecosystem
- **Trust Wallet Chrome Extension**: $8.5 million cryptocurrency theft linked to supply chain compromise
- **Browser Extensions**: Over 8.8 million users impacted by DarkSpectre campaigns including ShadyPanda and GhostPoster
- **macOS Systems**: Targeted by GlassWorm malware campaign through trojanized crypto wallet applications
- **Discord Platforms**: Targeted by VVS Stealer malware harvesting credentials and tokens
- **IBM API Connect**: Critical authentication vulnerability affecting API management systems
- **Local Networks**: Compromised by Kimwolf botnet operations

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Shai-Hulud worm exploiting npm package dependencies to compromise downstream applications
- **Malicious Browser Extensions**: DarkSpectre campaigns distributing malware through compromised browser extensions
- **Trojanized Applications**: GlassWorm campaign using malicious VSCode/OpenVSX extensions to deliver cryptocurrency wallet trojans
- **Phishing Campaigns**: Multi-stage attacks abusing Google Cloud Application Integration features for credential theft
- **Python-based Information Stealing**: VVS Stealer using obfuscated Python code to harvest Discord credentials
- **Botnet Operations**: RondoDox and Kimwolf botnets conducting persistent campaigns against IoT and network infrastructure
- **Authentication Bypass**: Exploitation of 2FA bypass vulnerabilities in enterprise firewall systems
- **Remote Access Trojan Deployment**: Transparent Tribe targeting Indian entities with custom RAT malware

## Threat Actor Activities

- **ShinyHunters**: Claimed breach of cybersecurity firm Resecurity, though firm states it was a honeypot operation
- **Transparent Tribe**: Launching fresh RAT attacks against Indian governmental, academic, and strategic entities
- **RondoDox Operators**: Conducting nine-month persistent botnet campaign targeting IoT devices and web servers
- **Kimwolf Botnet Operators**: Active exploitation of local network vulnerabilities for months
- **DarkSpectre Campaign**: Attributed to threat actor behind ShadyPanda and GhostPoster browser extension attacks affecting 8.8 million users
- **Shai-Hulud Actors**: Conducting supply chain attacks against npm registry with modified worm variants
- **Cryptocurrency Thieves**: Leveraging 2022 LastPass breach data to conduct ongoing wallet drainage attacks
- **VVS Stealer Operators**: Deploying Python-based malware specifically targeting Discord user credentials