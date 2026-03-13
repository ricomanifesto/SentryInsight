# Exploitation Report

Critical exploitation activity has intensified across multiple platforms, with Google addressing two new Chrome zero-day vulnerabilities being actively exploited in attacks. Law enforcement agencies have successfully disrupted the SocksEscort proxy botnet that compromised 369,000 IP addresses across 163 countries using Linux malware. CISA has added an n8n remote code execution vulnerability to its Known Exploited Vulnerabilities catalog, with over 24,700 instances remaining exposed. Apple has released security updates for older iOS devices to address vulnerabilities targeted by the Coruna exploit kit in cyberespionage and crypto-theft operations. Additionally, Veeam has patched seven critical vulnerabilities in its Backup & Replication software that could allow remote code execution, while threat actors continue deploying AI-generated malware and sophisticated banking trojans targeting Brazilian financial institutions.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Google Chrome being exploited in zero-day attacks
- **Impact**: Active exploitation allows attackers to compromise Chrome browsers and potentially execute arbitrary code
- **Status**: Patched via emergency security updates from Google

### n8n Remote Code Execution Vulnerability
- **Description**: Critical security flaw in n8n workflow automation platform allowing remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable n8n instances
- **Status**: Actively exploited in the wild; added to CISA KEV catalog with 24,700 instances remaining exposed

### Apple WebKit Vulnerabilities (Coruna Exploit Kit)
- **Description**: Security flaws in WebKit engine targeted by the Coruna exploit kit
- **Impact**: Used in cyberespionage and cryptocurrency theft attacks against iOS and macOS users
- **Status**: Patches backported to older iOS, iPadOS, and macOS Sonoma versions

### AVRecon Malware Compromised Edge Devices
- **Description**: Linux malware compromising edge devices to build the SocksEscort proxy network
- **Impact**: Enslaved thousands of residential routers into a criminal botnet for proxy services
- **Status**: Network disrupted by international law enforcement operation

## Affected Systems and Products

- **Google Chrome**: All versions prior to emergency security updates containing zero-day patches
- **n8n Workflow Platform**: Over 24,700 exposed instances worldwide vulnerable to RCE attacks
- **Apple iOS/iPadOS/macOS**: Older devices targeted by Coruna exploit kit attacks
- **Veeam Backup & Replication**: Multiple versions containing seven critical RCE vulnerabilities
- **WordPress Sites**: 250,000+ installations using vulnerable Elementor Ally plugin with SQL injection flaw
- **Residential Routers**: 369,000 IP addresses across 163 countries compromised by AVRecon malware
- **Brazilian Banking Systems**: 33 banks targeted by VENON malware with credential-stealing overlays
- **Android Devices**: Multiple malware families targeting Pix payments, banking apps, and crypto wallets

## Attack Vectors and Techniques

- **Zero-Day Browser Exploitation**: Active exploitation of unpatched Chrome vulnerabilities for initial access
- **Remote Code Execution**: Multiple attack vectors through n8n workflow platform and Veeam backup systems
- **Proxy Network Abuse**: Compromised edge devices used for criminal proxy services and traffic routing
- **AI-Generated Malware**: Slopoly malware created using generative AI tools for persistent access
- **SQL Injection**: WordPress plugin vulnerabilities allowing database compromise and data theft
- **WebKit Exploitation**: Browser-based attacks through Safari and other WebKit-dependent applications
- **Banking Overlay Attacks**: Credential theft through fake banking interfaces on compromised Android devices
- **Ransomware Deployment**: Multiple groups using various initial access methods for encryption attacks

## Threat Actor Activities

- **Hive0163**: Utilizing AI-assisted Slopoly malware for persistent access in ransomware operations
- **SocksEscort Operators**: Criminal proxy service operators enslaving residential routers for botnet operations
- **BlackCat (ALPHV) Ransomware**: Continued operations with insider assistance from compromised negotiators
- **INC Ransomware Group**: Targeting healthcare organizations across Australia, New Zealand, and Tonga
- **Iranian APT Groups**: Collaboration between MOIS and cybercriminal groups to enhance attack capabilities
- **Brazilian Banking Malware Authors**: Deployment of Rust-based VENON malware targeting financial institutions
- **Interlock Ransomware Operators**: Using AI-generated malware for extended network persistence
- **AiLock Ransomware Gang**: Targeting sports organizations including England Hockey
- **Android Malware Developers**: Six new malware families targeting mobile financial applications