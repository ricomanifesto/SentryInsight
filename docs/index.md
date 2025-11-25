# Exploitation Report

Multiple critical zero-day vulnerabilities and active exploitation campaigns are currently threatening organizations worldwide. The most significant threats include CVE-2025-61757 in Oracle Identity Manager being actively exploited, a critical flaw in the Ray framework (ShadowRay 2.0) enabling AI infrastructure hijacking, and sophisticated social engineering attacks like JackFix that circumvent existing ClickFix mitigations. Supply chain attacks are proliferating through compromised npm packages and Blender 3D assets, while threat actors are leveraging fake Windows Update screens and commercial spyware to target high-value users. Additionally, vulnerabilities in Fluent Bit expose cloud infrastructures to remote code execution, and ShadowPad malware is actively exploiting WSUS vulnerabilities for full system access.

## Active Exploitation Details

### Oracle Identity Manager Critical Flaw
- **Description**: A critical vulnerability in Oracle Identity Manager that allows unauthorized access to identity management systems
- **Impact**: Full system access and potential compromise of identity management infrastructure
- **Status**: Currently under active exploitation by threat actors
- **CVE ID**: CVE-2025-61757

### ShadowRay 2.0 Ray Framework Vulnerability
- **Description**: A vulnerability in the Ray framework that enables threat actors to hijack AI clusters and infrastructure
- **Impact**: Complete compromise of AI infrastructure, cryptocurrency mining operations, and data theft capabilities
- **Status**: Active exploitation with self-propagating botnet distribution

### WSUS Vulnerability
- **Description**: A recently patched security flaw in Microsoft Windows Server Update Services (WSUS) that allows malware distribution
- **Impact**: Full system access and malware deployment across Windows Server environments
- **Status**: Actively exploited by ShadowPad malware operators

### Fluent Bit Remote Code Execution Vulnerabilities
- **Description**: Five vulnerabilities in Fluent Bit telemetry agent that can be chained together for infrastructure compromise
- **Impact**: Remote code execution and complete takeover of cloud infrastructures
- **Status**: Newly discovered vulnerabilities with potential for active exploitation

## Affected Systems and Products

- **Oracle Identity Manager**: Critical vulnerability affecting identity management systems
- **Ray Framework**: AI infrastructure and machine learning clusters worldwide
- **Microsoft WSUS**: Windows Server Update Services infrastructure
- **Fluent Bit**: Cloud infrastructure using the open-source telemetry agent
- **npm Registry**: Over 500 packages infected with Shai-Hulud malware, affecting 25,000+ repositories
- **Blender Foundation**: 3D modeling files distributed through CGTrader and other marketplaces
- **Android TV Streaming Devices**: Superbox and similar devices forming botnet infrastructure
- **Signal and WhatsApp**: Messaging platforms targeted by commercial spyware campaigns
- **Microsoft 365**: Access tokens and Outlook emails targeted by ToddyCat threat actor

## Attack Vectors and Techniques

- **JackFix Social Engineering**: Enhanced ClickFix variant using fake Windows Update screens and adult website lures
- **Supply Chain Poisoning**: Malicious npm packages and Blender 3D assets delivering StealC V2 infostealer
- **Fake Windows Updates**: Full-screen browser animations hiding malicious code in images
- **Voice Phishing (Vishing)**: Targeting university systems and alumni databases
- **Commercial Spyware**: RATs targeting high-value Signal and WhatsApp users
- **Credential Theft**: Code beautifiers exposing sensitive data from banks, government, and tech organizations
- **AI Infrastructure Hijacking**: Cryptocurrency mining and data theft through compromised Ray clusters

## Threat Actor Activities

- **ToddyCat**: Deploying new tools like TCSectorCopy to steal Microsoft 365 access tokens and Outlook emails
- **Clop Extortion Gang**: Attacking educational institutions like Dartmouth College through Oracle E-Business Suite vulnerabilities
- **ShadowPad Operators**: Exploiting WSUS vulnerabilities to distribute advanced malware across Windows Server environments
- **Shai-Hulud Campaign**: Second wave of supply chain attacks targeting npm repositories with credential theft capabilities
- **Russian-linked Groups**: Distributing StealC V2 malware through compromised Blender files on 3D model marketplaces
- **Commercial Spyware Operators**: CISA-warned campaigns targeting high-value individuals using Signal and WhatsApp