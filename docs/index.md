# Exploitation Report

Critical exploitation activity is currently targeting iOS devices, e-commerce platforms, and enterprise systems through sophisticated attack vectors. The most significant concerns include the Coruna iOS exploit kit reusing proven kernel exploits from Operation Triangulation, active PolyShell attacks targeting over half of all vulnerable Magento stores, and authentication bypass vulnerabilities in enterprise networking equipment. Payment card skimmers are evolving to bypass Content Security Policy protections using WebRTC channels, while threat actors continue to leverage popular platforms for credential theft and data exfiltration campaigns.

## Active Exploitation Details

### PolyShell Vulnerability in Magento
- **Description**: A critical vulnerability in version 2 of Magento Open Source and Adobe Commerce installations
- **Impact**: Allows attackers to compromise e-commerce platforms and potentially access sensitive customer data
- **Status**: Active exploitation targeting 56% of all vulnerable Magento stores

### Coruna iOS Kit Kernel Exploits
- **Description**: Updated kernel exploit targeting two security vulnerabilities in Apple iOS, reusing code from the 2023 Operation Triangulation campaign
- **Impact**: Enables device compromise and potential surveillance capabilities on iOS devices
- **Status**: Active mass attacks using refined exploitation techniques from previous campaigns

### Citrix NetScaler Authentication Bypass
- **Description**: Authentication bypass vulnerability in NetScaler ADC and NetScaler Gateway systems, similar to previously exploited CitrixBleed vulnerabilities
- **Impact**: Unauthorized access to enterprise network infrastructure and potential lateral movement
- **Status**: Recently patched with urgent recommendations for immediate deployment

### PTC Windchill and FlexPLM Remote Code Execution
- **Description**: Critical vulnerability in widely used product lifecycle management (PLM) solutions
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Imminent threat warning issued with active exploitation concerns

### TP-Link Router Authentication Bypass
- **Description**: Critical severity flaw in Archer NX router series allowing authentication bypass
- **Impact**: Unauthorized firmware upload and complete device takeover capabilities
- **Status**: Recently patched with active exploitation potential

## Affected Systems and Products

- **Apple iOS Devices**: Targeted by Coruna exploit kit using refined Triangulation attack methods
- **Magento E-commerce Platforms**: Version 2 of Open Source and Adobe Commerce installations under active attack
- **Citrix NetScaler**: ADC and Gateway systems vulnerable to authentication bypass attacks
- **PTC Enterprise Software**: Windchill and FlexPLM product lifecycle management solutions
- **TP-Link Routers**: Archer NX series devices with authentication bypass vulnerabilities
- **E-commerce Websites**: General targeting by WebRTC-based payment skimmers
- **Microsoft 365 Organizations**: Over 340 organizations across five countries targeted by device code phishing
- **Cryptocurrency Wallets**: 728 different crypto wallet extensions targeted by Torg Grabber malware

## Attack Vectors and Techniques

- **WebRTC Data Channel Abuse**: Payment skimmers using WebRTC channels to bypass Content Security Policy protections and exfiltrate payment card data
- **Device Code Phishing**: OAuth abuse targeting Microsoft 365 identities through device authentication flows
- **No-Code Platform Abuse**: Threat actors leveraging Bubble AI app builder to create convincing phishing applications
- **Blockchain Dead Drops**: GlassWorm malware using Solana blockchain for command and control communications
- **Job Recruitment Scams**: Long-term campaigns impersonating legitimate companies for credential harvesting
- **AI Platform Account Trading**: Underground markets selling premium AI service access for malicious purposes
- **Browser Extension Targeting**: Comprehensive data theft from 850+ browser extensions including crypto wallets

## Threat Actor Activities

- **RedLine Operation Administrators**: Armenian suspect extradited to face charges for managing prolific infostealer infrastructure
- **TA551 Botnet Operators**: Russian national sentenced for managing botnet used in BitPaymer ransomware attacks against 72 U.S. companies
- **LeakBase Forum Administration**: Russian law enforcement arrested alleged administrator of massive credential marketplace
- **State-Sponsored iOS Targeting**: Mass attack campaigns leveraging proven Triangulation exploit code for widespread device compromise
- **E-commerce Threat Groups**: Coordinated PolyShell exploitation targeting majority of vulnerable Magento installations
- **Cryptocurrency-Focused Attackers**: Development and deployment of specialized malware targeting extensive range of crypto wallet extensions
- **Phishing-as-a-Service Operations**: Sophisticated campaigns using legitimate platforms to evade detection and target enterprise credentials