# Exploitation Report

Current exploitation activity reveals a concerning landscape of actively exploited vulnerabilities across multiple enterprise systems and supply chains. The most critical developments include the active exploitation of CVE-2025-61757 in Oracle Identity Manager, which has been added to CISA's Known Exploited Vulnerabilities catalog. Threat actors are also leveraging vulnerabilities in the Ray AI framework through the ShadowRay 2.0 campaign to compromise AI infrastructure worldwide, while ShadowPad malware is exploiting Microsoft WSUS vulnerabilities for full system access. Additionally, massive supply chain attacks are targeting npm repositories through the resurgent Shai-Hulud campaign, affecting over 25,000 repositories and 500 packages with credential theft capabilities.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: A critical security flaw in Oracle Identity Manager that allows unauthorized access to identity management systems
- **Impact**: Attackers can gain full system access and compromise enterprise identity infrastructure
- **Status**: Actively exploited in the wild, added to CISA's KEV catalog
- **CVE ID**: CVE-2025-61757

### ShadowRay 2.0 Ray Framework Vulnerability
- **Description**: A flaw in the Ray framework that enables attackers to hijack AI infrastructure and create self-propagating botnets
- **Impact**: Compromise of AI clusters for cryptocurrency mining and data theft operations
- **Status**: Actively exploited worldwide targeting AI infrastructure

### Microsoft WSUS Vulnerability
- **Description**: A recently patched security flaw in Microsoft Windows Server Update Services
- **Impact**: Full system access and malware distribution through enterprise update mechanisms
- **Status**: Actively exploited by ShadowPad malware operators

### Fluent Bit Vulnerabilities
- **Description**: Five vulnerabilities in the open-source telemetry agent that can be chained together
- **Impact**: Remote code execution and complete compromise of cloud infrastructures
- **Status**: Newly discovered vulnerabilities with potential for infrastructure takeover

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems exposed to zero-day exploitation
- **Ray Framework**: AI infrastructure and machine learning clusters worldwide
- **Microsoft Windows Server Update Services (WSUS)**: Enterprise Windows update systems vulnerable to malware distribution
- **Fluent Bit**: Cloud telemetry agents used in containerized environments
- **npm Registry**: JavaScript package management system with over 25,000 compromised repositories
- **Blender 3D Software**: 3D modeling application files weaponized for malware delivery
- **Android TV Streaming Boxes**: Consumer media devices compromised for botnet operations
- **Salesforce via Gainsight**: Customer relationship management platforms accessed through third-party applications

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious packages injected into npm registry affecting hundreds of legitimate packages including Zapier, ENS Domains, PostHog, and Postman
- **ClickFix Social Engineering**: Fake Windows Update screens displayed in full-screen browsers to deliver malware
- **Matrix Push C2**: Browser notification-based command and control for fileless, cross-platform attacks
- **Preinstall Script Exploitation**: Malicious code execution during package installation affecting build and runtime environments
- **Voice Phishing (Vishing)**: Social engineering attacks targeting university systems and alumni databases
- **Third-Party Application Compromise**: Exploitation of integrated applications to access primary platforms like Salesforce

## Threat Actor Activities

- **ShinyHunters**: Conducting extortion campaigns against Salesforce customers through third-party application compromises
- **Russian-linked Actors**: Distributing StealC V2 information stealer through malicious Blender model files on 3D marketplaces
- **APT31 (China-linked)**: Launching stealthy cyberattacks against Russian IT sector using cloud services for infrastructure
- **ShadowPad Operators**: Actively exploiting WSUS vulnerabilities to distribute advanced persistent threat malware
- **Shai-Hulud Campaign Actors**: Conducting massive npm supply chain attacks affecting over 500 packages and 25,000 repositories with credential harvesting capabilities
- **ShadowRay 2.0 Operators**: Creating global cryptocurrency mining botnets through AI infrastructure compromise