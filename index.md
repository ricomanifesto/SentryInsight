# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitation targeting critical infrastructure and enterprise systems. The most significant developments include a critical Docker container escape vulnerability with a CVSS score of 9.3, coordinated scanning campaigns against Microsoft RDP authentication servers involving nearly 2,000 IP addresses, and sophisticated attacks against Iranian maritime infrastructure. Additionally, threat actors are leveraging AI systems for novel attack vectors, including malicious prompt injection through downscaled images and ClickFix attacks that manipulate AI-generated content summaries. Data breaches continue to impact major organizations, with Farmers Insurance suffering a breach affecting 1.1 million customers through Salesforce attacks, while French retailer Auchan experienced exposure of hundreds of thousands of customer loyalty accounts.

## Active Exploitation Details

### Docker Container Escape Vulnerability
- **Description**: Critical security flaw affecting Docker Desktop app for Windows and macOS that allows attackers to break out of container confines
- **Impact**: Container escape leading to potential host system compromise
- **Status**: Patches released by Docker
- **CVE ID**: CVE-2025-9074

### Apple Security Vulnerability
- **Description**: Dangerous security flaw affecting iPhone, iPad, and Mac devices that Apple warns might have already been exploited
- **Impact**: Sophisticated targeted attacks against specific individuals
- **Status**: Security updates available, Apple recommends immediate patching

### Microsoft RDP Authentication Servers
- **Description**: Coordinated scanning activity targeting Microsoft Remote Desktop Web Access and RDP authentication infrastructure
- **Impact**: Reconnaissance for potential brute force attacks and unauthorized access
- **Status**: Active scanning campaign involving 1,971 IP addresses

### AI System Prompt Injection
- **Description**: Novel attack method that injects malicious prompts in downscaled images processed by AI systems before delivery to large language models
- **Impact**: Data theft through manipulation of AI processing workflows
- **Status**: Proof-of-concept demonstrated by researchers

### ClickFix AI Manipulation
- **Description**: Attack technique that tricks AI-generated content summaries into pushing malware by making malicious instructions appear to come from legitimate AI sources
- **Impact**: Increased likelihood of victim compliance due to perceived AI legitimacy
- **Status**: Active attack vector being exploited

## Affected Systems and Products

- **Docker Desktop**: Windows and macOS versions affected by container escape vulnerability
- **Apple Devices**: iPhone, iPad, and Mac systems requiring immediate security updates
- **Microsoft RDP Services**: Remote Desktop Web Access and RDP authentication servers under coordinated scanning
- **AI Language Models**: Large language models vulnerable to prompt injection through image processing
- **Salesforce Platform**: Targeted in widespread attacks affecting multiple organizations
- **Android Applications**: 77 malicious apps with 19 million downloads removed from Google Play
- **Iranian Maritime Systems**: Cargo ships and oil tankers belonging to sanctioned companies

## Attack Vectors and Techniques

- **Container Escape**: Exploitation of Docker Desktop vulnerabilities to break containment
- **Coordinated Network Scanning**: Large-scale reconnaissance using nearly 2,000 IP addresses targeting RDP infrastructure
- **AI Prompt Injection**: Embedding malicious instructions in downscaled images processed by AI systems
- **ClickFix Social Engineering**: Manipulating AI-generated summaries to deliver malware with increased trust
- **Captive Portal Hijacking**: UNC6384 using hijacked captive portals with valid certificates for PlugX deployment
- **Mobile Malware Distribution**: Malicious Android applications distributed through official Google Play store

## Threat Actor Activities

- **UNC6384**: China-nexus threat actor conducting sophisticated attacks against diplomats in Southeast Asia using PlugX malware, captive portal hijacks, and valid certificates to advance Beijing's strategic interests
- **Lab-Dookhtegen**: Claims responsibility for major attack on over 60 Iranian cargo ships and oil tankers, successfully knocking out communications systems
- **Mobile Malware Operators**: Distributed 77 malicious Android applications achieving over 19 million downloads before detection and removal
- **Salesforce Attackers**: Conducted widespread attacks against Salesforce platform affecting multiple organizations including Farmers Insurance with 1.1 million customer records compromised
- **RDP Scanning Campaign**: Coordinated effort involving nearly 2,000 IP addresses systematically probing Microsoft RDP authentication infrastructure