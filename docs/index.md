# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise platforms and supply chain components. Oracle Identity Manager is under active zero-day exploitation with CVE-2025-61757 being leveraged for unauthorized access. Meanwhile, threat actors are exploiting vulnerabilities in the Ray framework through the ShadowRay 2.0 campaign to compromise AI infrastructure worldwide. Microsoft Windows Server Update Services (WSUS) vulnerabilities are being actively exploited by ShadowPad malware operators to gain full system access. Additionally, massive supply chain attacks are targeting npm packages through the Shai-Hulud malware campaign, affecting over 25,000 repositories and 500+ packages.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager allowing unauthorized access to identity management systems
- **Impact**: Attackers can gain full access to identity management infrastructure, potentially compromising authentication and authorization controls across enterprise environments
- **Status**: Currently under active exploitation; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Ray Framework Vulnerability (ShadowRay 2.0)
- **Description**: Security flaw in the Ray distributed computing framework used in AI and machine learning infrastructures
- **Impact**: Enables attackers to hijack AI infrastructure worldwide, establishing self-propagating cryptomining and data theft botnets
- **Status**: Actively exploited by threat actors to compromise AI clusters and convert them into cryptocurrency mining operations

### Windows Server Update Services (WSUS) Vulnerability
- **Description**: Recently patched security flaw in Microsoft Windows Server Update Services
- **Impact**: Provides attackers with full system access to Windows servers through malicious update distribution
- **Status**: Actively exploited by ShadowPad malware operators despite recent patching

### Fluent Bit Vulnerabilities
- **Description**: Five vulnerabilities discovered in Fluent Bit telemetry agent that can be chained together
- **Impact**: Allow attackers to compromise and take over cloud infrastructures through remote code execution and stealthy intrusions
- **Status**: Newly discovered vulnerabilities exposing cloud environments to significant risk

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems across organizations
- **Ray Framework**: AI and machine learning clusters worldwide used for distributed computing
- **Microsoft WSUS**: Windows Server Update Services infrastructure in enterprise environments
- **Fluent Bit**: Open-source telemetry agents deployed across cloud infrastructures
- **npm Registry**: JavaScript package repository affecting 500+ packages and 25,000+ repositories
- **Blender 3D Software**: Users downloading malicious model files from marketplaces like CGTrader
- **Android TV Streaming Devices**: Superbox and similar devices sold through retailers like BestBuy and Walmart

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Trojanized npm packages mimicking legitimate libraries like Zapier, ENS Domains, PostHog, and Postman
- **Malicious File Distribution**: StealC infostealer malware delivered through compromised Blender 3D model files on marketplaces
- **Browser Notification Abuse**: Matrix Push C2 platform leveraging browser notifications for fileless, cross-platform phishing attacks
- **Fake System Updates**: ClickFix attacks using realistic Windows Update animations to hide malicious code within images
- **Preinstall Script Exploitation**: Shai-Hulud malware executing during npm package preinstall phase to steal credentials and secrets
- **Update Service Hijacking**: ShadowPad malware distributed through compromised WSUS infrastructure
- **AI Infrastructure Compromise**: ShadowRay 2.0 exploiting Ray framework vulnerabilities to establish persistent botnet presence

## Threat Actor Activities

- **ShadowRay 2.0 Operators**: Conducting worldwide campaign targeting AI infrastructure for cryptocurrency mining and data theft operations
- **Russian-Linked Campaign**: Distributing StealC V2 information stealer through malicious Blender files on 3D model marketplaces
- **ShinyHunters Group**: Exploiting third-party applications like Gainsight to steal Salesforce customer data in repeat attacks
- **APT31 (China-Linked)**: Launching stealthy cyberattacks against Russian IT sector using cloud services for persistence and evasion
- **ShadowPad Operators**: Actively exploiting WSUS vulnerabilities to distribute advanced persistent threat malware on Windows servers
- **Shai-Hulud Campaign Actors**: Orchestrating massive supply chain attacks affecting hundreds of npm packages and thousands of repositories