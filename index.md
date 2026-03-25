# Exploitation Report

Current cybersecurity landscape reveals a complex threat environment characterized by sophisticated supply chain attacks, AI-enhanced exploitation campaigns, and critical infrastructure vulnerabilities. Most notably, TeamPCP threat actors are conducting a sustained supply chain compromise campaign targeting developer toolchains through malicious packages and CI/CD pipeline infiltration. Simultaneously, advanced persistent threats are leveraging AI coding agents for autonomous cyber espionage operations, while traditional attack vectors continue to target critical authentication bypasses and remote code execution vulnerabilities across enterprise infrastructure.

## Active Exploitation Details

### TP-Link Router Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in TP-Link Archer NX router series allowing attackers to circumvent security controls and upload malicious firmware
- **Impact**: Complete device compromise, unauthorized firmware installation, and potential network infiltration
- **Status**: Patched by TP-Link, users urged to update immediately

### PTC Windchill and FlexPLM Remote Code Execution
- **Description**: Critical remote code execution vulnerability affecting PTC's widely-used product lifecycle management solutions
- **Impact**: Remote code execution on enterprise PLM systems, potential for complete system compromise
- **Status**: PTC warns of imminent threat, critical security updates required

### LiteLLM Python Package Supply Chain Compromise
- **Description**: Popular Python package backdoored by TeamPCP threat actors through CI/CD pipeline compromise
- **Impact**: Credential harvesting, authentication token theft affecting hundreds of thousands of developers
- **Status**: Versions 1.82.7-1.82.8 confirmed malicious, immediate package updates required

### Trivy Security Scanner CI/CD Compromise
- **Description**: Aqua Security's Trivy vulnerability scanner compromised through stolen CI credentials
- **Impact**: Malicious code injection into security toolchain, potential for widespread developer environment compromise
- **Status**: Active compromise confirmed, security teams advised to verify Trivy installations

### Checkmarx KICS Code Scanner Compromise
- **Description**: Checkmarx's KICS security scanner targeted through GitHub Actions workflow compromise
- **Impact**: Security toolchain infiltration allowing for credential theft and malware distribution
- **Status**: Ongoing investigation, users advised to review recent KICS deployments

## Affected Systems and Products

- **TP-Link Archer NX Series**: Critical authentication bypass requiring immediate firmware updates
- **PTC Windchill**: Enterprise PLM systems vulnerable to remote code execution
- **PTC FlexPLM**: Product lifecycle management platforms at critical risk
- **LiteLLM Python Package**: Versions 1.82.7-1.82.8 containing malicious backdoors
- **Aqua Security Trivy**: CI/CD pipeline compromise affecting security scanning operations
- **Checkmarx KICS**: GitHub Actions workflows compromised for credential harvesting
- **Microsoft 365**: Over 340 organizations targeted through OAuth device code phishing
- **ConnectWise ScreenConnect**: Malware distribution through malvertising campaigns
- **npm Ecosystem**: Seven malicious packages identified in Ghost Campaign targeting cryptocurrency wallets

## Attack Vectors and Techniques

- **Supply Chain Infiltration**: TeamPCP actors compromising CI/CD pipelines and package repositories
- **Device Code Phishing**: OAuth abuse targeting Microsoft 365 environments across multiple countries
- **AI-Enhanced Espionage**: Autonomous AI coding agents conducting 80-90% of attack operations
- **Malvertising Campaigns**: Tax-themed search advertisements delivering ScreenConnect malware
- **Social Engineering**: Fake resume campaigns targeting French-speaking corporate environments
- **EDR Bypass Techniques**: Abuse of legitimate Huawei drivers to disable endpoint detection systems
- **Credential Harvesting**: Systematic theft of authentication tokens and developer credentials
- **Botnet Operations**: TA551 botnet infrastructure supporting ransomware deployment

## Threat Actor Activities

- **TeamPCP**: Conducting extensive supply chain attacks against developer toolchains including Trivy, KICS, and LiteLLM packages
- **State-Sponsored AI Operations**: Autonomous cyber espionage campaigns targeting 30 global organizations using AI coding agents
- **Yanluowang Ransomware Group**: Initial access broker operations resulting in 81-month prison sentence for Russian national
- **TA551 Operators**: Botnet management supporting ransomware attacks against 72 U.S. companies
- **Iranian Hacktivists**: Gulf region targeting with limited operational impact
- **ShinyHunters**: Data theft claims against Infinite Campus K-12 systems
- **Ghost Campaign Operators**: Cryptocurrency wallet theft through seven malicious npm packages
- **French-Targeting Groups**: Resume-based phishing campaigns deploying cryptocurrency miners and information stealers