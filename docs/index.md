# Exploitation Report

The current threat landscape is dominated by sophisticated attacks targeting cloud environments and supply chain infrastructure. Notable activity includes automated OAuth abuse campaigns against Azure environments through ConsentFix v3 attacks, large-scale supply chain compromises affecting popular Python packages and SAP development tools, and state-sponsored cryptocurrency theft operations. North Korean threat actors continue their aggressive cryptocurrency targeting, while Vietnamese-linked operations are exploiting Google AppSheet for Facebook account compromises. Additionally, multiple software supply chain attacks are targeting developer environments through poisoned packages in Ruby Gems, Go modules, and PyPI repositories.

## Active Exploitation Details

### ConsentFix v3 OAuth Abuse
- **Description**: Automated OAuth abuse attacks targeting Azure environments with enhanced scaling and automation capabilities
- **Impact**: Unauthorized access to Azure resources through OAuth token manipulation
- **Status**: Active exploitation observed in hacker forums

### Supply Chain Package Poisoning
- **Description**: Coordinated attacks targeting PyPI packages including PyTorch Lightning and Intercom-client, along with compromised Ruby Gems and Go modules
- **Impact**: Credential theft, GitHub Actions tampering, and CI pipeline compromise
- **Status**: Multiple packages compromised with malicious payloads deployed

### TeamPCP Mini Shai-Hulud Attack
- **Description**: Supply chain attacks targeting SAP packages in the npm ecosystem
- **Impact**: Compromise of SAP cloud application development tools and environments
- **Status**: Several npm packages confirmed compromised

### Google AppSheet Phishing Relay
- **Description**: Vietnamese-linked campaign using Google AppSheet as a phishing relay to distribute Facebook credential harvesting emails
- **Impact**: Compromise of approximately 30,000 Facebook accounts
- **Status**: Active campaign with ongoing victim targeting

### Nine-Year-Old Linux Vulnerability
- **Description**: AI-assisted discovery of a previously unknown Linux vulnerability present for nine years
- **Impact**: System compromise through a 10-line proof-of-concept exploit
- **Status**: Patch available, vulnerability actively disclosed

## Affected Systems and Products

- **Microsoft Azure**: OAuth systems and authentication mechanisms targeted by ConsentFix v3
- **PyPI Ecosystem**: PyTorch Lightning and Intercom-client packages compromised
- **SAP Cloud Development**: npm packages for SAP's cloud application development tools
- **Ruby Gems Repository**: Multiple gems infected with credential-stealing payloads
- **Go Modules**: Developer packages compromised for CI pipeline attacks
- **Facebook Platform**: 30,000 accounts compromised through phishing campaigns
- **Google AppSheet**: Abused as phishing infrastructure relay
- **Linux Systems**: Nine-year-old vulnerability affecting various Linux distributions
- **Windows 11**: KB5083769 update causing backup software failures

## Attack Vectors and Techniques

- **Automated OAuth Abuse**: Scaled attacks against Azure authentication using ConsentFix v3 methodology
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages across multiple ecosystems
- **Phishing Relay**: Using legitimate Google services as intermediaries for credential harvesting
- **Social Engineering**: Vishing attacks combined with SSO abuse for rapid SaaS environment compromise
- **CI Pipeline Exploitation**: Targeting continuous integration systems through compromised development packages
- **Sleeper Packages**: Deployment of initially benign packages later updated with malicious payloads

## Threat Actor Activities

- **North Korean Groups**: Responsible for 76% of all cryptocurrency theft in 2026, conducting historic heists with potential AI assistance
- **Vietnamese-Linked Operators**: Conducting large-scale Facebook account compromises through Google AppSheet phishing campaigns
- **TeamPCP Group**: Expanding supply chain attacks to target SAP development ecosystem
- **China-Aligned Espionage Campaign**: Targeting government and defense sectors across South, East, and Southeast Asia, plus one European government
- **BlackCat Ransomware Affiliates**: Former cybersecurity professionals sentenced for facilitating ransomware attacks
- **Cybercrime Groups**: Conducting rapid SaaS extortion attacks using vishing and SSO abuse techniques
- **Romanian Swatting Ring**: Targeted over 75 public officials, journalists, and religious institutions
- **Cargo Theft Cybercriminals**: Sharp increase in cyber-enabled cargo theft operations across US and Canada