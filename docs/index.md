# Exploitation Report

The current threat landscape reveals a concerning escalation in sophisticated attack vectors targeting critical infrastructure and software supply chains. Multiple cybercrime groups are leveraging advanced techniques including supply chain poisoning, AI-assisted phishing campaigns, and rapid SaaS environment exploitation. Notable activities include Vietnamese-linked operations compromising 30,000 Facebook accounts through Google AppSheet abuse, China-aligned espionage campaigns targeting Asian governments and NATO states, and extensive supply chain attacks against Python package repositories. Additionally, cybercriminals are exploiting AI-enabled cargo theft operations while North Korean threat actors continue dominating cryptocurrency theft operations, accounting for 76% of all stolen cryptocurrency in 2026.

## Active Exploitation Details

### Google AppSheet Phishing Relay Exploitation
- **Description**: Vietnamese threat actors are exploiting Google AppSheet as a phishing relay platform to distribute malicious emails targeting Facebook credentials
- **Impact**: Successful compromise of approximately 30,000 Facebook accounts through sophisticated phishing campaigns
- **Status**: Active exploitation campaign ongoing with widespread credential theft

### Software Supply Chain Package Poisoning
- **Description**: Multiple supply chain attacks targeting Python package repositories including PyTorch Lightning, Ruby Gems, Go Modules, and npm packages for SAP's cloud development ecosystem
- **Impact**: Credential theft, GitHub Actions tampering, CI pipeline exploitation, and unauthorized access to development environments
- **Status**: Active ongoing campaigns with sleeper packages being used to push malicious payloads

### AI-Assisted Linux Kernel Vulnerability
- **Description**: A 9-year-old Linux kernel vulnerability discovered through AI-assisted software scanning that allows exploitation through a 10-line proof-of-concept
- **Impact**: Potential system compromise on affected Linux systems
- **Status**: Patch available, but legacy systems may remain vulnerable

### Cyber-Enabled Cargo Theft Operations
- **Description**: FBI-identified surge in cybercriminal activities targeting transportation and logistics infrastructure through cyber-enabled methods
- **Impact**: Estimated losses reaching significant amounts across United States and Canada
- **Status**: Active and escalating threat with sharp increase in incidents

## Affected Systems and Products

- **PyTorch Lightning**: Python machine learning framework compromised with malicious versions pushed to PyPI repository
- **Ruby Gems**: Ruby package ecosystem targeted with poisoned gems for credential theft
- **Go Modules**: Go programming language modules compromised for CI pipeline exploitation
- **SAP npm Packages**: SAP cloud application development packages hit by "Mini Shai-Hulud" attacks
- **Google AppSheet**: Legitimate Google service abused as phishing relay infrastructure
- **Facebook Accounts**: 30,000 accounts compromised through sophisticated phishing operations
- **Linux Kernel**: 9-year-old vulnerability affecting Linux systems across multiple distributions
- **Windows 11**: KB5083769 update causing third-party backup software failures on 24H2 and 25H2 versions

## Attack Vectors and Techniques

- **Phishing Relay Exploitation**: Using legitimate Google AppSheet platform as intermediary for phishing email distribution
- **Supply Chain Poisoning**: Injecting malicious code into popular software packages across multiple programming ecosystems
- **Sleeper Package Strategy**: Deploying dormant packages that later push malicious payloads to avoid detection
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for rapid SaaS environment compromise
- **AI-Assisted Credential Theft**: Leveraging artificial intelligence to enhance phishing campaign effectiveness
- **CI Pipeline Tampering**: Targeting continuous integration systems to inject malicious code into development workflows
- **Cargo Theft Cyber-Enabling**: Using cyber methods to facilitate physical cargo theft operations

## Threat Actor Activities

- **Vietnamese-Linked Groups**: Conducting large-scale Facebook credential harvesting through Google AppSheet phishing relays, compromising 30,000 accounts
- **China-Aligned APT**: Targeting government and defense sectors across South, East, and Southeast Asia, plus one European government and NATO state
- **TeamPCP**: Broadening supply chain attacks to include SAP package ecosystem with "Mini Shai-Hulud" attack methodology
- **North Korean Actors**: Dominating cryptocurrency theft operations, accounting for 76% of all stolen cryptocurrency in 2026 through historic heists
- **BlackCat Ransomware Affiliates**: Former cybersecurity professionals sentenced for facilitating ransomware attacks against U.S. companies
- **Brazilian DDoS Botnet**: Anti-DDoS firm paradoxically enabling massive DDoS attacks against Brazilian ISPs
- **Rapid SaaS Extortion Groups**: Two distinct cybercrime groups conducting high-impact attacks within SaaS environments using minimal forensic traces