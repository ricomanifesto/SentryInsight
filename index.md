# Exploitation Report

Critical exploitation activity is dominated by sophisticated supply chain attacks targeting development infrastructure and authentication bypass vulnerabilities. TeamPCP has emerged as a persistent threat actor conducting extensive supply chain compromises affecting popular development tools and packages, including the LiteLLM Python package, Trivy CI/CD systems, and Checkmarx GitHub Actions. Meanwhile, attackers are actively exploiting a critical authentication bypass vulnerability in TP-Link Archer NX routers that allows firmware uploads without authentication. Additional concerning activity includes device code phishing campaigns targeting Microsoft 365 organizations, malvertising campaigns using tax-related search terms to deliver ScreenConnect malware, and AI-assisted campaigns distributing hundreds of malicious packages across development platforms.

## Active Exploitation Details

### TP-Link Archer NX Router Authentication Bypass
- **Description**: Critical vulnerability allowing attackers to bypass authentication mechanisms and upload malicious firmware to affected routers
- **Impact**: Complete device compromise, ability to install persistent malware, potential for network lateral movement
- **Status**: Patches available from TP-Link, users urged to update immediately

### TeamPCP Supply Chain Compromises
- **Description**: Coordinated attacks compromising CI/CD pipelines and popular development packages to inject credential-harvesting malware
- **Impact**: Theft of developer credentials, authentication tokens, and potential access to enterprise development environments
- **Status**: Ongoing active campaign with multiple compromised packages and tools

### PTC Windchill and FlexPLM Remote Code Execution
- **Description**: Critical vulnerability in widely-used product lifecycle management solutions allowing remote code execution
- **Impact**: Complete system compromise, unauthorized access to sensitive product data and intellectual property
- **Status**: PTC warning of imminent exploitation threat

### Microsoft 365 Device Code Phishing
- **Description**: Active OAuth abuse campaign using device code authentication flow to compromise Microsoft 365 identities
- **Impact**: Unauthorized access to corporate Microsoft 365 environments and sensitive organizational data
- **Status**: Ongoing attacks across 340+ organizations in multiple countries

## Affected Systems and Products

- **TP-Link Archer NX Router Series**: Multiple models vulnerable to authentication bypass allowing firmware upload
- **LiteLLM Python Package**: Versions 1.82.7-1.82.8 compromised with credential-harvesting backdoors
- **PTC Windchill and FlexPLM**: Product lifecycle management solutions vulnerable to remote code execution
- **Microsoft 365 Organizations**: 340+ organizations across US, Canada, Australia affected by device code phishing
- **Trivy Security Scanner**: CI/CD systems compromised leading to supply chain attacks
- **Checkmarx KICS**: Code scanning tools compromised via GitHub Actions credential theft
- **npm Package Ecosystem**: Multiple malicious packages targeting cryptocurrency wallets and developer credentials
- **GitHub Development Platform**: Over 300 poisoned packages targeting developer tools and gaming applications
- **ConnectWise ScreenConnect**: Malicious installers distributed through tax-related search advertising

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Systematic targeting of CI/CD pipelines and package repositories to inject malicious code
- **Device Code Phishing**: Abuse of OAuth device authentication flow to bypass traditional MFA protections
- **Malvertising**: Tax-themed search advertisements delivering malware-laden software installers
- **Credential Harvesting**: Deployment of information stealers to capture authentication tokens and sensitive data
- **Authentication Bypass**: Direct exploitation of router firmware upload vulnerabilities without credential requirements
- **Social Engineering**: Fake resume campaigns targeting French corporate environments with embedded malware
- **Package Poisoning**: Creation of legitimate-looking packages containing hidden malicious functionality

## Threat Actor Activities

- **TeamPCP**: Persistent supply chain attacks targeting development infrastructure including Trivy, Checkmarx KICS, LiteLLM, and GitHub Actions workflows
- **TA551 Botnet Operators**: Russian-managed botnet infrastructure used for BitPaymer ransomware deployment against 72 U.S. companies
- **State-Sponsored AI Agent Campaign**: Anthropic-disclosed autonomous cyber espionage operation targeting 30 global entities with 80-90% AI automation
- **Yanluowang Ransomware Affiliates**: Initial access brokers facilitating ransomware deployment through compromised enterprise networks
- **ShinyHunters**: Data theft operations targeting educational institutions including Infinite Campus K-12 systems
- **Ghost Campaign**: Cryptocurrency theft operation using 7 malicious npm packages to target digital wallets
- **Tax Season Malvertisers**: Large-scale campaign exploiting seasonal tax document searches to distribute ScreenConnect malware
- **Iranian Hacktivists**: Coordinated but largely ineffective operations targeting Gulf region infrastructure