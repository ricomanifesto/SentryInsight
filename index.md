# Exploitation Report

Current cybersecurity threat landscape reveals critical active exploitation activities targeting AI frameworks, mobile platforms, and e-commerce systems. The most concerning developments include active attacks against the Langflow AI platform through CVE-2026-33017, sophisticated iOS exploit kits linked to previous nation-state campaigns, and widespread attacks targeting Magento e-commerce stores. Threat actors are rapidly adapting their tactics, exploiting newly disclosed vulnerabilities within hours and leveraging legitimate platforms to bypass security controls while conducting credential theft and payment card skimming operations.

## Active Exploitation Details

### Langflow AI Platform Critical Vulnerability
- **Description**: Critical code injection vulnerability in the Langflow AI workflow framework that enables attackers to hijack AI workflows
- **Impact**: Complete compromise of AI workflows, potential unauthorized access to sensitive data and model manipulation
- **Status**: Actively exploited in the wild, CISA has issued warnings about ongoing attacks
- **CVE ID**: CVE-2026-33017

### PolyShell Magento Vulnerability
- **Description**: Critical vulnerability affecting Magento Open Source version 2 and Adobe Commerce installations
- **Impact**: Remote code execution and complete store compromise
- **Status**: Actively exploited, targeting 56% of all vulnerable Magento stores worldwide

### iOS Coruna Exploit Kit
- **Description**: Advanced iOS exploit framework utilizing kernel exploits from Operation Triangulation attacks
- **Impact**: Zero-click remote code execution on iOS devices, enabling complete device compromise
- **Status**: Active exploitation framework being used in mass attacks, evolution of 2023 Triangulation campaign

### Ajax Football Club IT Systems
- **Description**: Unspecified vulnerabilities in Ajax Amsterdam's IT infrastructure
- **Impact**: Data breach exposing fan personal information and enabling ticket hijacking
- **Status**: Successfully exploited, incident disclosed by the organization

### Claude Chrome Extension XSS
- **Description**: Cross-site scripting vulnerability in Anthropic's Claude Google Chrome Extension enabling zero-click prompt injection
- **Impact**: Malicious prompt execution through simple website visits, potential AI model manipulation
- **Status**: Vulnerability disclosed and patched

## Affected Systems and Products

- **Langflow AI Framework**: All versions vulnerable to CVE-2026-33017 code injection attacks
- **Magento Open Source v2**: E-commerce platforms vulnerable to PolyShell exploitation
- **Adobe Commerce**: E-commerce installations susceptible to PolyShell attacks
- **iOS Devices**: Mobile devices targeted by Coruna exploit kit and zero-click attacks
- **Ajax IT Systems**: Football club infrastructure compromised through unspecified vulnerabilities
- **Claude Chrome Extension**: Browser extension vulnerable to XSS and prompt injection
- **Citrix NetScaler ADC/Gateway**: Network appliances requiring urgent patching for critical vulnerabilities
- **E-commerce Websites**: Payment systems targeted by WebRTC-based skimming attacks
- **Microsoft Accounts**: Credential harvesting through Bubble platform abuse
- **Cryptocurrency Wallets**: 728 different wallet types targeted by Torg Grabber infostealer

## Attack Vectors and Techniques

- **Zero-Click Exploitation**: iOS devices compromised without user interaction through iMessage exploits
- **Code Injection**: Langflow framework exploited through malicious code injection techniques
- **WebRTC Data Channels**: Payment skimmers using WebRTC to bypass Content Security Policy controls
- **No-Code Platform Abuse**: Bubble AI app builder leveraged to host Microsoft credential phishing campaigns
- **Supply Chain Attacks**: Exploitation of AI frameworks and development platforms
- **Phishing Campaign Evolution**: TikTok for Business accounts targeted with bot-resistant phishing pages
- **Cross-Site Scripting**: Zero-click XSS exploitation through malicious website visits
- **E-commerce Skimming**: Advanced payment card data theft bypassing security controls

## Threat Actor Activities

- **Red Menshen (China-linked)**: Long-term espionage campaign embedding BPFDoor implants in telecom networks for government surveillance
- **Operation Triangulation Actors**: Continued iOS exploitation activities using evolved Coruna exploit kit for mass attacks
- **PolyShell Campaign**: Widespread automated attacks targeting vulnerable Magento installations globally
- **RedLine Malware Operation**: Administrative arrests made but operations continue with Armenian suspect extradited to US
- **LeakBase Forum**: Major cybercrime marketplace disrupted with administrator arrest in Russia
- **Xinbi Marketplace**: Chinese-language cryptocurrency marketplace sanctioned by UK for selling stolen data
- **Torg Grabber Operators**: New infostealer malware targeting extensive range of cryptocurrency wallets and browser extensions
- **WebRTC Skimmer Groups**: Sophisticated payment card theft operations using advanced bypass techniques