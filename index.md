# Exploitation Report

Current threat landscapes reveal several critical exploitation activities across multiple vectors. The most significant active exploitation involves a critical flaw in Oracle Identity Manager (CVE-2025-61757) being actively exploited in the wild. Additionally, threat actors are leveraging sophisticated social engineering campaigns, including JackFix attacks that use fake Windows Update screens to bypass ClickFix mitigations, and targeting AI infrastructure through Ray framework vulnerabilities in ShadowRay 2.0 campaigns. Supply chain attacks have intensified with the resurgence of Shai-Hulud malware affecting over 500 npm packages, while advanced persistent threat groups like ToddyCat are deploying new custom tools to steal corporate email data and Microsoft 365 access tokens.

## Active Exploitation Details

### Oracle Identity Manager Critical Vulnerability
- **Description**: A critical vulnerability in Oracle Identity Manager that allows unauthorized access to identity management systems
- **Impact**: Attackers can gain unauthorized access to identity and access management infrastructure, potentially compromising entire organizational authentication systems
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2025-61757

### ShadowRay 2.0 Ray Framework Exploitation
- **Description**: A vulnerability in the Ray framework that allows threat actors to hijack AI infrastructure and computational clusters
- **Impact**: Attackers can convert AI clusters into cryptocurrency mining botnets and steal sensitive data from AI workloads
- **Status**: Active exploitation targeting AI infrastructure worldwide with self-propagating capabilities

### Fluent Bit Remote Code Execution Chain
- **Description**: Five vulnerabilities in Fluent Bit telemetry agent that can be chained together for comprehensive system compromise
- **Impact**: Complete takeover of cloud infrastructures through remote code execution and stealthy infrastructure intrusions
- **Status**: Newly discovered vulnerabilities with potential for widespread cloud infrastructure compromise

### Commercial Spyware Campaigns
- **Description**: Active campaigns leveraging commercial spyware and remote access trojans targeting high-value communication platforms
- **Impact**: Hijacking of Signal and WhatsApp accounts belonging to high-value targets for surveillance and data collection
- **Status**: Actively warned about by CISA, indicating ongoing exploitation

## Affected Systems and Products

- **Oracle Identity Manager**: Identity and access management systems vulnerable to unauthorized access
- **Ray Framework**: AI infrastructure and machine learning clusters being converted into botnets
- **Fluent Bit**: Cloud telemetry and logging infrastructure across multiple cloud providers
- **Signal and WhatsApp**: Encrypted messaging platforms targeted by commercial spyware
- **npm Registry**: Over 500 packages infected with Shai-Hulud malware including popular libraries
- **Blender 3D Assets**: 3D modeling files on marketplaces like CGTrader delivering StealC V2 malware
- **Oracle E-Business Suite**: Enterprise resource planning systems targeted by Clop extortion gang
- **Android TV Streaming Devices**: Superbox and similar devices incorporated into botnets
- **Microsoft 365**: Email and collaboration platforms targeted by ToddyCat's new tools

## Attack Vectors and Techniques

- **JackFix Social Engineering**: Fake Windows Update screens in full-screen browser pages hiding malicious code in images to bypass traditional ClickFix mitigations
- **Supply Chain Poisoning**: Trojanized npm packages with names similar to legitimate libraries like Zapier, ENS Domains, PostHog, and Postman
- **Malicious 3D Assets**: Weaponized Blender files distributed through legitimate 3D model marketplaces
- **Voice Phishing**: Sophisticated vishing attacks targeting university systems and financial institutions
- **Commercial Spyware Deployment**: Advanced persistent surveillance tools targeting encrypted communication platforms
- **AI Infrastructure Hijacking**: Exploitation of Ray framework vulnerabilities to create self-propagating cryptocurrency mining botnets
- **Cloud Infrastructure Chaining**: Multi-vulnerability exploitation chains in telemetry systems for complete infrastructure takeover

## Threat Actor Activities

- **ToddyCat**: Advanced persistent threat group deploying new custom tools including TCSectorCopy to steal corporate email data and Microsoft 365 access tokens
- **Clop Extortion Gang**: Actively targeting educational institutions and enterprises through Oracle E-Business Suite vulnerabilities, with confirmed attacks on Dartmouth College
- **Russian-linked Campaigns**: Distributing StealC V2 information stealer through malicious Blender files and sophisticated supply chain attacks
- **ShadowRay Operators**: Coordinating large-scale AI infrastructure hijacking campaigns for cryptocurrency mining and data theft
- **Financial Institution Impersonators**: FBI reports over $262 million stolen through account takeover fraud schemes targeting banking customers
- **Chinese State-linked Hackers**: Conducting espionage operations against Russian IT organizations using commercial cloud services for command-and-control communications