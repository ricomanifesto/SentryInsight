# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities under active exploitation, with particularly concerning activity targeting enterprise infrastructure and supply chain components. Most notably, CVE-2025-61757 in Oracle Identity Manager is being actively exploited and has been added to CISA's Known Exploited Vulnerabilities catalog. A recently patched Microsoft WSUS vulnerability is being leveraged to distribute ShadowPad malware, while threat actors are also exploiting the Ray framework to hijack AI infrastructure for cryptocurrency mining operations. Supply chain attacks continue to proliferate, with the Shai-Hulud malware campaign infecting over 500 npm packages and exposing secrets through GitHub repositories. Additionally, innovative attack vectors are emerging, including the use of browser notifications for command and control operations and malicious Blender model files for malware distribution.

## Active Exploitation Details

### Oracle Identity Manager Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle Identity Manager that allows unauthorized access and potential system compromise
- **Impact**: Attackers can gain unauthorized access to identity management systems and potentially escalate privileges across enterprise environments
- **Status**: Currently under active exploitation; added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-61757

### Microsoft WSUS Security Vulnerability
- **Description**: Recently patched security flaw in Microsoft Windows Server Update Services that enables malware distribution
- **Impact**: Threat actors can leverage compromised WSUS infrastructure to distribute malware including ShadowPad to Windows servers across the network
- **Status**: Actively exploited by threat actors for ShadowPad malware distribution

### Ray Framework Vulnerability (ShadowRay 2.0)
- **Description**: Security flaw in the Ray framework that enables hijacking of AI infrastructure worldwide
- **Impact**: Attackers can convert AI clusters into cryptocurrency mining botnets while stealing sensitive data
- **Status**: Actively exploited to create self-propagating cryptomining and data theft botnets

### Fluent Bit Vulnerabilities
- **Description**: Five security vulnerabilities discovered in Fluent Bit telemetry agent that can be chained together
- **Impact**: Complete compromise and takeover of cloud infrastructures through remote code execution
- **Status**: Newly discovered vulnerabilities exposing cloud environments to stealthy infrastructure intrusions

## Affected Systems and Products

- **Oracle Identity Manager**: Enterprise identity management systems vulnerable to zero-day exploitation
- **Microsoft Windows Server Update Services (WSUS)**: Update infrastructure being exploited for malware distribution
- **Ray Framework**: AI and machine learning infrastructure worldwide susceptible to botnet conversion
- **Fluent Bit**: Open-source telemetry agents used in cloud infrastructures
- **npm Registry**: JavaScript package repository affected by supply chain attacks targeting over 500 packages
- **Blender 3D Software**: Model files being weaponized on marketplaces like CGTrader
- **Android TV Streaming Devices**: Superbox devices potentially part of botnet operations
- **WhatsApp API**: Contact discovery functionality allowing mass account scraping

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages injected into npm registry affecting well-known packages like Zapier, ENS Domains, PostHog, and Postman
- **Browser Notification Hijacking**: Matrix Push C2 platform leveraging browser notifications for fileless, cross-platform phishing attacks
- **Fake Windows Update Screens**: ClickFix attacks using realistic Windows Update animations to hide malicious code in images
- **Malicious 3D Model Files**: StealC V2 information stealer distributed through Blender model files on marketplaces
- **Voice Phishing (Vishing)**: Social engineering attacks targeting university systems to compromise alumni and donor databases
- **Preinstall Script Abuse**: Shai-Hulud malware executing during npm package preinstall phase to steal credentials and secrets

## Threat Actor Activities

- **ShinyHunters Extortion Group**: Targeting Salesforce customers through third-party application Gainsight to steal organizational data
- **Russian-Linked Campaigns**: Distributing StealC V2 malware through malicious Blender files on 3D model marketplaces
- **APT31 (China-Linked)**: Conducting stealthy cyberattacks against Russian IT sector using cloud services for persistence
- **ShadowPad Operators**: Exploiting WSUS vulnerabilities to distribute advanced malware to Windows server environments
- **Supply Chain Attackers**: Orchestrating massive npm poisoning campaigns affecting 25,000+ repositories and leaking secrets to GitHub