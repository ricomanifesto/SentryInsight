# Exploitation Report

Current cybersecurity intelligence reveals several critical exploitation activities across multiple platforms and systems. The most significant threats include active exploitation of vulnerabilities in Citrix Session Recording and Git systems, which have been added to CISA's Known Exploited Vulnerabilities catalog. Additionally, a critical container escape vulnerability in Docker Desktop poses severe risks to containerized environments. Threat actors are leveraging sophisticated attack vectors including coordinated RDP scanning campaigns, AI-based data theft techniques, and advanced phishing operations using malware loaders. Notable activities include UNC6384's targeted attacks against diplomatic entities and widespread malicious Android applications affecting millions of users.

## Active Exploitation Details

### Citrix Session Recording Vulnerabilities
- **Description**: Security flaws in Citrix Session Recording systems that are being actively exploited in the wild
- **Impact**: Attackers can potentially gain unauthorized access to session recording data and compromise enterprise environments
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog, indicating active exploitation

### Git Vulnerabilities
- **Description**: Security vulnerabilities affecting Git version control systems
- **Impact**: Could allow attackers to compromise source code repositories and development environments
- **Status**: Added to CISA's KEV catalog due to confirmed active exploitation

### Docker Desktop Container Escape Vulnerability
- **Description**: Critical security flaw in Docker Desktop for Windows and macOS that allows container escape
- **Impact**: Attackers can break out of container isolation and potentially gain access to the host system
- **Status**: Patched by Docker with critical severity rating
- **CVE ID**: CVE-2025-9074

### Apple Device Security Flaw
- **Description**: Dangerous security vulnerability affecting iPhone, iPad, and Mac devices
- **Impact**: May have already been exploited in extremely sophisticated attacks targeting specific individuals
- **Status**: Apple has released security updates to address the vulnerability

## Affected Systems and Products

- **Citrix Session Recording**: Enterprise session recording and monitoring systems
- **Git Version Control**: Source code management and version control systems
- **Docker Desktop**: Container platform for Windows and macOS environments
- **Apple Devices**: iPhone, iPad, and Mac systems across multiple versions
- **Android Devices**: Mobile devices running Android OS, particularly those with malicious apps installed
- **Microsoft RDP**: Remote Desktop Protocol authentication servers and web access systems
- **Salesforce Platform**: Cloud-based CRM and business application platform
- **AI Systems**: Large language models and AI processing systems vulnerable to prompt injection

## Attack Vectors and Techniques

- **Container Escape**: Exploitation of Docker Desktop vulnerabilities to break container isolation
- **Coordinated Network Scanning**: Large-scale scanning campaigns targeting Microsoft RDP authentication servers using nearly 2,000 IP addresses
- **AI Prompt Injection**: Novel attack technique hiding malicious prompts in downscaled images processed by AI systems
- **Captive Portal Hijacking**: UNC6384 threat group using compromised captive portals with valid certificates
- **Phishing with Malware Loaders**: Campaigns using fake voicemail emails and UpCrypter loader to deliver RAT payloads
- **Mobile Malware Distribution**: Malicious Android applications distributed through Google Play Store

## Threat Actor Activities

- **UNC6384**: China-nexus threat actor conducting targeted attacks against diplomats in Southeast Asia and other global entities using PlugX malware, captive portal hijacks, and valid certificates to advance Beijing's strategic interests
- **Android Malware Operators**: Cybercriminals distributing 77 malicious Android applications through Google Play Store, achieving over 19 million downloads before removal
- **RDP Scanning Groups**: Coordinated threat actors conducting large-scale scanning operations against Microsoft Remote Desktop services
- **Phishing Campaign Operators**: Attackers using sophisticated phishing techniques with UpCrypter malware loader in fake voicemail and purchase order campaigns
- **Salesforce Attackers**: Threat actors responsible for widespread Salesforce platform attacks affecting multiple organizations including Farmers Insurance with 1.1 million customer records compromised