# Exploitation Report

Current exploitation activity reveals several critical threats across multiple sectors, with active attacks targeting AI frameworks, mobile devices, and cloud infrastructure. CISA has warned of active exploitation of CVE-2026-33017 in Langflow AI workflows, while sophisticated threat actors continue leveraging zero-click iOS exploits through the Coruna framework. Additional concerns include phishing campaigns targeting high-profile organizations, ransomware operations against Russian entities, and advanced payment skimmers bypassing security controls on e-commerce platforms.

## Active Exploitation Details

### Langflow AI Framework Vulnerability
- **Description**: Critical vulnerability in the Langflow framework allowing attackers to hijack AI workflows through code injection
- **Impact**: Complete compromise of AI workflow systems, potential data theft and system manipulation
- **Status**: Actively exploited by threat actors within hours of disclosure, requiring immediate patching
- **CVE ID**: CVE-2026-33017

### Coruna iOS Exploit Kit
- **Description**: Sophisticated iOS exploit framework reusing code from the 2023 Operation Triangulation campaign, targeting iPhones through zero-click iMessage exploits
- **Impact**: Complete device compromise, espionage capabilities, data exfiltration without user interaction
- **Status**: Recently discovered in mass attack campaigns, evolution of previously seen Triangulation attacks

### Claude Chrome Extension XSS Vulnerability
- **Description**: Zero-click cross-site scripting vulnerability in Anthropic's Claude Google Chrome Extension enabling prompt injection
- **Impact**: Malicious prompt execution simply by visiting a compromised web page, potential AI system manipulation
- **Status**: Vulnerability disclosed and addressed by vendor

### WebRTC Payment Skimmer
- **Description**: Advanced payment card skimmer using WebRTC data channels to bypass Content Security Policy (CSP) protections
- **Impact**: Theft of payment card data from e-commerce websites, financial fraud
- **Status**: Actively deployed against e-commerce platforms

## Affected Systems and Products

- **Langflow AI Framework**: AI workflow management systems vulnerable to code injection attacks
- **Apple iOS Devices**: iPhones targeted through zero-click iMessage exploits via Coruna framework
- **Claude Chrome Extension**: Browser extension users vulnerable to prompt injection attacks
- **E-commerce Platforms**: Payment processing systems targeted by WebRTC-based skimmers
- **Ajax Football Club Systems**: IT infrastructure compromised, exposing fan data and enabling ticket hijacking
- **European Commission AWS**: Amazon cloud infrastructure breached by threat actors
- **Dutch National Police**: Internal systems compromised through phishing attacks
- **LangChain and LangGraph**: AI frameworks with vulnerabilities exposing files, secrets, and databases

## Attack Vectors and Techniques

- **Zero-Click Exploits**: iMessage-based attacks requiring no user interaction for iOS device compromise
- **AI Prompt Injection**: Manipulation of AI systems through malicious prompts delivered via web pages
- **WebRTC Data Channels**: Novel technique bypassing CSP protections for payment data exfiltration
- **Phishing Campaigns**: Targeted attacks against law enforcement and government organizations
- **Cloud Infrastructure Exploitation**: Compromise of Amazon Web Services hosting critical EU systems
- **Vulnerability Chaining**: Multi-stage attacks combining multiple security flaws for system compromise

## Threat Actor Activities

- **Red Menshen (China-linked)**: Long-term espionage campaign embedding in telecom networks using BPFDoor implants for government surveillance
- **Bearlyfy (Pro-Ukrainian)**: Ransomware group targeting over 70 Russian companies with custom GenieLocker ransomware since January 2025
- **Various Cybercriminals**: Exploiting Langflow vulnerabilities within hours of public disclosure, demonstrating rapid weaponization capabilities
- **Payment Card Fraudsters**: Deploying sophisticated WebRTC-based skimmers to bypass modern security controls on e-commerce sites
- **Phishing Operators**: Targeting TikTok for Business accounts with bot-resistant malicious pages