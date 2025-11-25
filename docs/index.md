# Exploitation Report

Critical vulnerabilities are under active exploitation across multiple sectors, with threat actors leveraging diverse attack vectors from supply chain compromises to infrastructure targeting. The most significant activities include exploitation of Oracle Identity Manager vulnerabilities, active spyware campaigns targeting high-value messaging applications, supply chain attacks through npm packages and 3D modeling files, and the deployment of sophisticated malware through trusted platforms. Threat actors are increasingly using AI infrastructure for cryptomining operations while exploiting misconfigurations in enterprise systems to deploy advanced persistent threats.

## Active Exploitation Details

### Oracle Identity Manager Vulnerability
- **Description**: Critical vulnerability in Oracle Identity Manager currently being exploited in the wild
- **Impact**: Allows attackers to gain unauthorized access to identity management systems
- **Status**: Under active exploitation following Oracle Cloud breaches earlier this year
- **CVE ID**: CVE-2025-61757

### Microsoft WSUS Vulnerability
- **Description**: Security flaw in Microsoft Windows Server Update Services exploited to distribute malware
- **Impact**: Enables threat actors to compromise Windows servers and deploy ShadowPad malware for full system access
- **Status**: Recently patched but actively exploited by threat actors targeting Windows servers

### Ray Framework Vulnerability
- **Description**: Flaw in the Ray framework being leveraged to hijack AI infrastructure worldwide
- **Impact**: Allows attackers to turn AI clusters into cryptocurrency mining botnets and data theft operations
- **Status**: ShadowRay 2.0 campaign actively exploiting this vulnerability to create self-propagating botnets

### Fluent Bit Vulnerabilities
- **Description**: Five vulnerabilities discovered in Fluent Bit, an open-source telemetry agent
- **Impact**: Can be chained together to compromise and take over cloud infrastructures with remote code execution capabilities
- **Status**: Newly discovered vulnerabilities exposing cloud environments to stealthy infrastructure intrusions

## Affected Systems and Products

- **Oracle Identity Manager**: Identity management systems vulnerable to unauthorized access
- **Microsoft Windows Server Update Services (WSUS)**: Windows servers susceptible to malware distribution
- **Ray Framework**: AI infrastructure and machine learning clusters worldwide
- **Fluent Bit**: Cloud infrastructure using this telemetry agent
- **npm Registry**: JavaScript package ecosystem with over 500 infected packages
- **Blender 3D Modeling Software**: Files distributed through CGTrader and other 3D marketplaces
- **Oracle E-Business Suite**: Systems targeted by Clop extortion campaigns
- **Signal and WhatsApp**: Messaging applications targeted by commercial spyware
- **Android TV Streaming Boxes**: Devices potentially compromised for botnet operations

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Distribution of malicious packages through npm registry and 3D model marketplaces
- **Spyware Campaigns**: Deployment of commercial spyware and remote access trojans targeting high-value users
- **Social Engineering**: ClickFix attacks using fake Windows Update screens to deliver malware
- **Browser Notification Abuse**: Matrix Push C2 platform leveraging browser notifications for fileless attacks
- **Voice Phishing (Vishing)**: Attacks targeting university systems to compromise alumni and donor data
- **Cryptomining Operations**: Hijacking AI infrastructure for unauthorized cryptocurrency mining
- **Preinstall Script Exploitation**: Shai-Hulud malware executing during package installation phases

## Threat Actor Activities

- **APT31**: China-linked group conducting stealthy cyberattacks on Russian IT sector using cloud services
- **Clop Extortion Gang**: Targeting educational institutions including Dartmouth College through Oracle E-Business Suite exploitation
- **Russian-linked Campaigns**: Distributing StealC V2 information stealer through compromised Blender files
- **ShadowPad Operators**: Actively exploiting WSUS vulnerabilities to deploy advanced malware on Windows servers
- **Shai-Hulud Campaign**: Second wave affecting 25,000+ repositories through npm preinstall credential theft
- **Commercial Spyware Operators**: CISA-warned campaigns targeting Signal and WhatsApp users with high-value profiles
- **ShadowRay 2.0 Operators**: Converting AI clusters into cryptocurrency mining botnets through Ray framework exploitation