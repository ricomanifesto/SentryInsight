# Exploitation Report

Based on the analyzed security articles, several critical exploitation activities are currently impacting organizations globally. Notable threats include sophisticated supply chain attacks targeting Python packages like PyTorch Lightning and npm packages for SAP ecosystems, where threat actors are compromising legitimate software repositories to steal credentials and tamper with CI/CD pipelines. North Korean threat actors continue their aggressive cryptocurrency theft operations, reportedly controlling 76% of all crypto stolen in 2026. Additionally, cybercrime groups are executing rapid SaaS-based extortion attacks using vishing techniques and SSO abuse, while Vietnamese-linked actors have successfully compromised 30,000 Facebook accounts through Google AppSheet phishing campaigns.

## Active Exploitation Details

### PyTorch Lightning Package Compromise
- **Description**: Threat actors compromised the popular Python package Lightning, pushing two malicious versions to the PyPI repository to conduct credential theft
- **Impact**: Attackers can steal developer credentials and potentially access development environments and source code repositories
- **Status**: Active supply chain attack targeting Python development environments

### Intercom-client Package Attack
- **Description**: The Intercom-client package was compromised in a coordinated supply chain attack alongside PyTorch Lightning
- **Impact**: Credential theft and potential unauthorized access to communication platforms and customer data
- **Status**: Active exploitation through compromised package distribution

### SAP npm Package Poisoning
- **Description**: TeamPCP threat group compromised several npm packages for SAP's cloud application development ecosystem in the "Mini Shai-Hulud" attack campaign
- **Impact**: Compromise of SAP development environments and potential access to enterprise cloud applications
- **Status**: Active supply chain attack targeting SAP development tools

### 9-Year-Old Linux Vulnerability
- **Description**: AI-assisted security scanning revealed a previously unknown Linux vulnerability that has existed for nine years
- **Impact**: Potential system compromise with a proof-of-concept exploit requiring only 10 lines of code
- **Status**: Newly discovered but patch already available

### Ruby Gems and Go Modules CI Pipeline Exploitation
- **Description**: Sleeper packages in Ruby Gems and Go modules are being used to push malicious payloads targeting CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and compromise of software development workflows
- **Status**: Active attacks targeting development infrastructure

## Affected Systems and Products

- **PyTorch Lightning**: Python machine learning framework with compromised packages on PyPI
- **Intercom-client**: Communication platform integration package compromised through supply chain attack
- **SAP Cloud Development Tools**: npm packages for SAP's cloud application development ecosystem
- **Linux Systems**: Nine-year-old vulnerability affecting Linux distributions (patch available)
- **Ruby Gems Repository**: Poisoned packages targeting Ruby development environments
- **Go Modules**: Compromised packages affecting Go-based development projects
- **Facebook Platform**: 30,000 accounts compromised through Google AppSheet phishing
- **Canvas Learning Platform**: Instructure's educational technology platform affected by cybersecurity incident
- **France Titres (ANTS)**: French government agency for administrative documents breached
- **Windows 11 Systems**: KB5083769 update causing backup software failures

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Compromising legitimate software packages to distribute malware and steal credentials
- **Phishing Relay**: Using Google AppSheet as an intermediary platform to distribute phishing emails
- **Vishing and SSO Abuse**: Voice phishing combined with single sign-on exploitation for rapid SaaS environment compromise
- **CI/CD Pipeline Targeting**: Exploiting continuous integration and deployment systems for credential theft
- **Sleeper Package Strategy**: Deploying dormant malicious packages that activate later to avoid detection
- **GitHub Actions Tampering**: Manipulating automated workflows in development environments

## Threat Actor Activities

- **North Korean Groups**: Conducting historic cryptocurrency heists, controlling 76% of crypto stolen in 2026, potentially using AI assistance
- **TeamPCP**: Executing "Mini Shai-Hulud" attacks against SAP development packages, broadening supply chain attack operations
- **Vietnamese-linked Operators**: Running large-scale Facebook account compromise campaign using Google AppSheet phishing relay affecting 30,000 accounts
- **China-aligned Espionage Groups**: Targeting government and defense sectors across South, East, and Southeast Asia, plus one European government and NATO state
- **BlackCat Ransomware Affiliates**: Former cybersecurity professionals sentenced for facilitating ransomware attacks against U.S. companies
- **Cybercrime SaaS Groups**: Two identified groups conducting rapid, high-impact attacks within SaaS environments while leaving minimal forensic traces
- **Romanian Swatting Ring**: Organized group targeting over 75 public officials, journalists, and religious institutions
- **Brazilian DDoS Operators**: Anti-DDoS firm enabling botnet responsible for massive DDoS attacks against Brazilian ISPs