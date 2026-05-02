# Exploitation Report

The current threat landscape reveals a sophisticated array of cyberattacks targeting critical infrastructure, software supply chains, and enterprise environments. Cybercriminals are leveraging advanced techniques including phishing campaigns through legitimate services like Google AppSheet, supply chain attacks against popular Python packages, and vishing combined with SSO abuse for rapid SaaS extortion. Notable incidents include North Korean threat actors controlling 76% of stolen cryptocurrency in 2026, Chinese-linked espionage campaigns targeting Asian governments and NATO states, and a surge in cyber-enabled cargo theft attacks. The exploitation landscape is further complicated by AI-assisted attacks and the compromise of development ecosystems including npm packages for SAP cloud applications.

## Active Exploitation Details

### Google AppSheet Phishing Campaign
- **Description**: Vietnamese-linked operation using Google AppSheet as a "phishing relay" to distribute phishing emails targeting Facebook accounts
- **Impact**: Compromise of approximately 30,000 Facebook accounts through sophisticated phishing techniques
- **Status**: Active ongoing campaign with threat actors leveraging legitimate Google services to bypass security controls

### Supply Chain Attacks on Python Packages
- **Description**: Malicious compromises of popular Python packages including PyTorch Lightning and Intercom-client to conduct credential theft
- **Impact**: Credential theft from developers and organizations using these widely-deployed packages
- **Status**: Active supply chain attacks targeting the Python Package Index (PyPI) ecosystem

### SAP Ecosystem Supply Chain Attacks
- **Description**: TeamPCP threat group compromising npm packages for SAP's cloud application development ecosystem using "Mini Shai-Hulud" attack techniques
- **Impact**: Compromise of SAP development environments and potential access to enterprise cloud applications
- **Status**: Active attacks broadening across SAP development tools and packages

### Ruby Gems and Go Modules CI Pipeline Exploitation
- **Description**: Sleeper packages deployed as conduits to push malicious payloads targeting CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and compromise of software development infrastructure
- **Status**: Active campaign exploiting continuous integration pipelines for persistent access

### 9-Year-Old Linux Vulnerability
- **Description**: AI-assisted software scanning revealed a previously undetected Linux kernel vulnerability present for nine years
- **Impact**: Potential system compromise through a 10-line proof-of-concept exploit
- **Status**: Patch available, but widespread deployment may be affected due to the vulnerability's age

## Affected Systems and Products

- **PyTorch Lightning**: Popular Python machine learning framework compromised in supply chain attack
- **Intercom-client**: Python package compromised for credential theft operations
- **SAP Cloud Development Tools**: npm packages in SAP ecosystem targeted by TeamPCP attacks
- **Google AppSheet**: Legitimate service abused as phishing relay platform
- **Facebook Accounts**: 30,000 accounts compromised through phishing campaigns
- **Ruby Gems and Go Modules**: Development packages weaponized for CI/CD pipeline attacks
- **Windows 11**: KB5083769 update causing backup software failures across multiple vendors
- **Linux Kernel**: 9-year-old vulnerability affecting potentially millions of systems
- **Transportation and Logistics Systems**: Cyber-enabled cargo theft targeting industry infrastructure

## Attack Vectors and Techniques

- **Phishing Relay Services**: Abuse of legitimate Google AppSheet to distribute phishing emails and evade detection
- **Supply Chain Poisoning**: Deployment of malicious packages in popular software repositories (PyPI, npm, Ruby Gems)
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for rapid SaaS environment compromise
- **Sleeper Package Technique**: Long-term deployment of dormant malicious packages activated later for credential theft
- **AI-Assisted Vulnerability Discovery**: Use of artificial intelligence to identify previously unknown security flaws
- **CI/CD Pipeline Exploitation**: Targeting continuous integration systems for persistent access and credential harvesting
- **DDoS Botnet Operations**: Anti-DDoS firms paradoxically enabling large-scale distributed denial-of-service attacks

## Threat Actor Activities

- **North Korean Groups**: Conducting historic cryptocurrency heists with AI assistance, controlling 76% of stolen crypto in 2026
- **Vietnamese-Linked Operators**: Executing large-scale phishing campaigns targeting 30,000 Facebook accounts via Google AppSheet
- **Chinese-Aligned Groups**: Running espionage campaigns against South, East, and Southeast Asian governments plus NATO states
- **TeamPCP**: Expanding supply chain attacks from general npm packages to SAP-specific development tools
- **BlackCat Ransomware Affiliates**: Cybersecurity professionals sentenced for facilitating ransomware attacks using insider knowledge
- **Brazilian DDoS Operations**: Anti-DDoS firm enabling botnet attacks against ISPs in sophisticated protection racket scheme
- **Romanian Swatting Ring**: Online harassment campaigns targeting over 75 public officials, journalists, and religious institutions
- **Rapid SaaS Extortion Groups**: Two distinct cybercrime organizations conducting high-impact attacks within SaaS environments