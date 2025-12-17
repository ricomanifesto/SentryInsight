# Exploitation Report

Current cybersecurity threats are dominated by sophisticated state-sponsored campaigns and critical infrastructure attacks. Russian GRU operations are actively exploiting misconfigured edge network devices to target critical organizations globally, particularly in the energy sector. Simultaneously, threat actors are exploiting newly disclosed Fortinet authentication bypass vulnerabilities and the React2Shell vulnerability to deploy Linux backdoors. The GhostPoster campaign demonstrates the evolution of browser-based attacks, embedding malicious JavaScript in Firefox extensions to hijack affiliate links and monitor user activity. These threats are compounded by ongoing malware-as-a-service operations like Cellik targeting Android devices and supply chain attacks through compromised NuGet packages.

## Active Exploitation Details

### Fortinet FortiGate SAML SSO Authentication Bypass
- **Description**: Critical security flaws in Fortinet FortiGate devices allowing authentication bypass through SAML SSO implementations
- **Impact**: Threat actors can gain unauthorized admin access and steal system configuration files
- **Status**: Actively exploited less than a week after public disclosure, patches available

### React2Shell Vulnerability
- **Description**: Security vulnerability in React applications enabling command injection attacks
- **Impact**: Attackers can deploy Linux backdoors including KSwapDoor and ZnDoor malware families
- **Status**: Currently being exploited in active campaigns

### Russian GRU Edge Device Exploitation
- **Description**: Long-running campaign targeting misconfigured edge network devices and cloud infrastructure
- **Impact**: Unauthorized access to critical infrastructure organizations, particularly energy sector
- **Status**: Multi-year campaign from 2021-2025, recently disrupted by Amazon

### GhostPoster Firefox Extension Campaign
- **Description**: Malicious JavaScript code embedded in Firefox addon logo files across 17 extensions
- **Impact**: Affiliate link hijacking, tracking code injection, and browser activity monitoring
- **Status**: Over 50,000 downloads affected, campaign ongoing

## Affected Systems and Products

- **Fortinet FortiGate**: Authentication bypass vulnerabilities in multiple products
- **Firefox Browser Extensions**: 17 malicious addons with embedded JavaScript in logo files
- **Edge Network Devices**: Misconfigured routers, firewalls, and network appliances
- **Amazon Web Services**: IAM credential compromise leading to cryptocurrency mining
- **React Applications**: Applications vulnerable to command injection through React2Shell
- **Android Devices**: Google Play Store apps targeted by Cellik malware-as-a-service
- **NuGet Packages**: .NET development ecosystem targeted through typosquatting attacks
- **SoundCloud Platform**: Audio streaming service experiencing data breach
- **PDVSA Oil Company**: Venezuelan state-owned petroleum company hit by cyberattack

## Attack Vectors and Techniques

- **SAML Authentication Bypass**: Exploiting authentication flaws in single sign-on implementations
- **Edge Device Misconfiguration**: Targeting improperly configured network infrastructure
- **Browser Extension Malware**: Hiding malicious code in legitimate-looking browser addons
- **Supply Chain Attacks**: Compromising software packages and development tools
- **Cloud IAM Exploitation**: Using stolen credentials for cryptocurrency mining operations
- **Typosquatting**: Creating malicious packages that mimic legitimate software libraries
- **Steganography**: Embedding JavaScript code in image files to evade detection
- **Social Engineering**: Call center fraud operations targeting European victims

## Threat Actor Activities

- **Russian GRU (Military Intelligence)**: Multi-year campaign targeting Western critical infrastructure, particularly energy sector organizations
- **Ink Dragon (Jewelbug)**: China-linked group expanding focus to European government targets while maintaining operations in Southeast Asia and South America
- **GhostPoster Campaign**: Browser-based attack campaign targeting Firefox users through malicious extensions
- **Cellik MaaS Operators**: Android malware-as-a-service providers offering embedding capabilities in legitimate apps
- **RansomHouse**: Ransomware group responsible for attacks against Japanese e-commerce company Askul
- **Call Center Fraud Networks**: Ukrainian-based operations scamming European victims for over 10 million euros