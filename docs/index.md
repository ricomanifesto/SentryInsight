# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple enterprise systems and platforms. The most significant threats include CVE-2025-61757 affecting Oracle Identity Manager, which has been added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation. Additional concerning activity includes the ShadowRay 2.0 campaign hijacking AI infrastructure through Ray framework vulnerabilities, ShadowPad malware exploiting WSUS vulnerabilities for full system access, and widespread supply chain attacks targeting npm repositories. These exploitation campaigns demonstrate sophisticated threat actors leveraging both zero-day vulnerabilities and recently patched flaws to compromise enterprise environments and cloud infrastructure.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager allowing remote code execution and unauthorized access
- **Impact**: Attackers can gain full administrative access to identity management systems and potentially compromise entire enterprise authentication infrastructure
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Ray Framework Vulnerability (ShadowRay 2.0)
- **Description**: Flaw in the Ray distributed computing framework used in AI and machine learning clusters
- **Impact**: Enables threat actors to hijack AI infrastructure worldwide, deploy cryptomining botnets, and conduct data theft operations
- **Status**: Actively exploited to create self-propagating botnets targeting AI clusters

### WSUS Vulnerability
- **Description**: Recently patched security flaw in Microsoft Windows Server Update Services
- **Impact**: Allows distribution of malware through legitimate update mechanisms, providing full system access
- **Status**: Actively exploited by ShadowPad malware operators to target Windows Servers

### Fluent Bit Vulnerabilities
- **Description**: Five vulnerabilities discovered in the open-source telemetry agent used in cloud environments
- **Impact**: Can be chained together to achieve remote code execution and complete compromise of cloud infrastructures
- **Status**: Recently disclosed with potential for exploitation in cloud environments

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity and access management systems across multiple organizations
- **Ray Framework**: AI and machine learning clusters, distributed computing environments
- **Microsoft WSUS**: Windows Server Update Services infrastructure in enterprise environments
- **Fluent Bit**: Cloud telemetry and logging infrastructure using the lightweight agent
- **npm Registry**: Over 500 trojanized packages affecting JavaScript development environments
- **Android TV Streaming Devices**: Superbox media streaming devices creating botnet infrastructure
- **Blender 3D Modeling Software**: Files distributed through CGTrader and other 3D model marketplaces
- **WhatsApp API**: Contact discovery functionality affecting billions of accounts

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious packages injected into npm registry targeting popular libraries like Zapier, ENS Domains, PostHog, and Postman
- **Preinstall Credential Theft**: Shai-Hulud malware executes during npm preinstall phase, significantly increasing exposure in build and runtime environments
- **Social Engineering**: ClickFix attacks using realistic Windows Update screens to deliver malware through full-screen browser deception
- **Third-Party Application Abuse**: Exploitation of Gainsight integration to access Salesforce customer data
- **Browser Notification Hijacking**: Matrix Push C2 platform leverages browser notifications for fileless, cross-platform phishing attacks
- **Voice Phishing (Vishing)**: Harvard University breach through social engineering targeting alumni and donor systems
- **Malicious File Distribution**: StealC V2 infostealer delivered through compromised Blender model files

## Threat Actor Activities

- **ShadowRay 2.0 Operators**: Conducting global campaign to hijack AI infrastructure for cryptomining and data theft operations
- **ShadowPad Affiliates**: Targeting Windows Server environments through WSUS exploitation for persistent access
- **Russian-Linked Actors**: Distributing StealC V2 malware through compromised 3D modeling files and marketplaces
- **Shai-Hulud Operators**: Conducting sophisticated npm supply chain attacks affecting over 25,000 repositories
- **ShinyHunters Group**: Exploiting third-party applications to steal Salesforce customer data in repeated attack campaigns
- **APT31 (China-Linked)**: Launching stealthy cyberattacks against Russian IT sector using cloud services and advanced persistence techniques
- **ClickFix Campaign Actors**: Developing new variants of browser-based social engineering attacks with realistic system update interfaces