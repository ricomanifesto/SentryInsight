# Exploitation Report

The current threat landscape reveals several critical exploitation activities across enterprise infrastructure and development environments. The most significant threats include active supply chain attacks by TeamPCP targeting popular development tools, critical authentication bypass vulnerabilities in network infrastructure devices, and sophisticated phishing campaigns leveraging AI-enhanced social engineering. Of particular concern are the Citrix NetScaler vulnerabilities that mirror previously exploited zero-day flaws, the ongoing device code phishing campaign affecting over 340 Microsoft 365 organizations, and the compromise of essential Python packages used by hundreds of thousands of developers.

## Active Exploitation Details

### Citrix NetScaler ADC and Gateway Vulnerabilities
- **Description**: Two vulnerabilities in NetScaler ADC and NetScaler Gateway, with one being very similar to the previously exploited CitrixBleed and CitrixBleed2 flaws
- **Impact**: Potential for remote code execution and system compromise, similar to previous zero-day exploits
- **Status**: Recently patched by Citrix with urgent advisory for immediate deployment

### TP-Link Archer NX Router Authentication Bypass
- **Description**: Critical-severity authentication bypass vulnerability in TP-Link Archer NX router series
- **Impact**: Attackers can bypass authentication mechanisms and upload malicious firmware to compromised devices
- **Status**: Patches available from TP-Link with immediate deployment recommended

### PTC Windchill and FlexPLM Remote Code Execution
- **Description**: Critical vulnerability in widely used product lifecycle management (PLM) solutions
- **Impact**: Remote code execution capability allowing full system compromise
- **Status**: PTC has issued warnings of imminent threat with patches available

### TeamPCP Supply Chain Compromises
- **Description**: Coordinated supply chain attacks targeting popular development tools including Trivy, Checkmarx KICS, and LiteLLM Python package
- **Impact**: Credential harvesting, authentication token theft, and backdoor deployment across development environments
- **Status**: Actively exploiting compromised packages with malicious versions 1.82.7–1.82.8 of LiteLLM identified

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: Enterprise application delivery controllers and secure remote access gateways
- **TP-Link Archer NX Series**: Consumer and small business wireless routers with critical authentication mechanisms
- **PTC Windchill and FlexPLM**: Product lifecycle management solutions used across manufacturing and engineering organizations
- **LiteLLM Python Package**: Popular PyPI package used by hundreds of thousands of developers for AI/ML applications
- **Microsoft 365 Organizations**: Over 340 organizations across five countries (US, Canada, Australia) targeted in device code phishing
- **Trivy and Checkmarx KICS**: Vulnerability scanning and infrastructure-as-code security tools
- **ConnectWise ScreenConnect**: Remote access software targeted in malvertising campaigns

## Attack Vectors and Techniques

- **Device Code Phishing**: OAuth abuse technique targeting Microsoft 365 identities using legitimate device code authentication flow
- **Supply Chain Injection**: Compromise of CI/CD pipelines to inject malicious code into trusted development tools and packages
- **Malvertising Campaigns**: Search engine advertisement poisoning targeting tax-related searches to deliver ScreenConnect malware
- **Social Engineering**: Fake resume campaigns and recruiter impersonation targeting corporate environments
- **EDR Evasion**: Use of legitimate Huawei drivers to disable endpoint detection and response systems
- **Cryptocurrency Mining Deployment**: Installation of mining software following credential theft and system compromise
- **Dead Drop Communication**: GlassWorm malware using Solana blockchain for command and control communication

## Threat Actor Activities

- **TeamPCP**: Conducting extensive supply chain attacks targeting development tool ecosystems, with successful compromises of Trivy, KICS, and LiteLLM packages affecting hundreds of thousands of developers
- **LeakBase Administrator**: Russian law enforcement arrested alleged administrator of major credential marketplace, though operations may continue
- **TA551 Botnet Operator**: Russian national sentenced to two years for managing botnet infrastructure used in BitPaymer ransomware attacks against 72 US companies
- **GlassWorm Campaign**: Evolution of existing malware campaign now incorporating Solana blockchain dead drops for enhanced stealth and persistence
- **Iranian Hacktivists**: Multiple Iran-aligned groups conducting cyber operations with limited strategic impact despite increased activity
- **French-Speaking Corporate Attackers**: Ongoing campaign using fake resumes to target French corporate environments for credential theft and crypto mining
- **AI-Enabled Threat Actors**: State-sponsored actors using AI coding agents for autonomous cyber espionage campaigns, with reported 80-90% automation in attack execution