# Exploitation Report

Current exploitation activity shows a concerning surge in supply chain attacks, zero-day exploits, and critical vulnerabilities being actively leveraged by threat actors. The most significant threats include the TeamPCP supply chain campaign compromising official SAP npm packages, active exploitation of CVE-2026-41940 in cPanel and WHM systems, authentication bypass vulnerabilities in Qinglong task schedulers being exploited for cryptomining, and the newly disclosed Linux "Copy Fail" privilege escalation flaw affecting major distributions. These attacks demonstrate sophisticated techniques including AI-assisted malware insertion, credential theft operations, and coordinated campaigns targeting development ecosystems and critical infrastructure.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in cPanel, WHM, and WP Squared allowing unauthorized access to control panels
- **Impact**: Attackers can gain complete access to hosting control panels without authentication credentials
- **Status**: Being actively exploited in the wild since late February 2026, emergency patches available
- **CVE ID**: CVE-2026-41940

### Linux Copy Fail Privilege Escalation
- **Description**: Local privilege escalation vulnerability in Linux kernels released since 2017 allowing unprivileged users to gain root access
- **Impact**: Complete system compromise through elevation to root privileges
- **Status**: Exploit code publicly available, patches distributed to major distributions

### Qinglong Task Scheduler RCE
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Remote code execution leading to cryptominer deployment on developers' servers
- **Status**: Actively being exploited for cryptocurrency mining operations

### SAP npm Package Supply Chain Attack
- **Description**: Multiple official SAP npm packages compromised by TeamPCP threat group
- **Impact**: Credential and authentication token theft from developers' systems
- **Status**: Ongoing supply chain attack campaign targeting SAP cloud development ecosystem

### PyTorch Lightning Package Compromise
- **Description**: Popular Python package Lightning compromised with two malicious versions
- **Impact**: Credential theft from affected development environments
- **Status**: Malicious versions pushed to PyPI repository for credential harvesting

### WordPress Quick Page/Post Redirect Plugin Backdoor
- **Description**: Dormant backdoor hidden in popular WordPress redirect plugin for five years
- **Impact**: Arbitrary code injection capabilities on over 70,000 WordPress sites
- **Status**: Backdoor recently activated after years of dormancy

## Affected Systems and Products

- **cPanel and WHM**: All versions prior to latest emergency updates vulnerable to authentication bypass
- **Linux Distributions**: Major distributions with kernels released since 2017 affected by Copy Fail vulnerability
- **SAP Development Ecosystem**: Multiple official npm packages compromised in supply chain attack
- **Qinglong Task Scheduler**: Open-source task scheduling tool targeted for cryptomining operations
- **PyTorch Lightning**: Popular Python machine learning framework package compromised
- **WordPress Sites**: Over 70,000 sites using Quick Page/Post Redirect plugin vulnerable to backdoor
- **OpenEMR Platform**: Electronic health record platform with 38 newly discovered security flaws
- **Google Gemini CLI**: Maximum severity vulnerability in CLI tool and GitHub Actions workflow
- **Roblox Gaming Platform**: Over 610,000 accounts compromised and sold

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: TeamPCP group targeting official packages in npm ecosystem with credential-stealing malware
- **Authentication Bypass**: Direct exploitation of authentication mechanisms in web control panels and task schedulers
- **Privilege Escalation**: Local attackers exploiting kernel vulnerabilities to gain root access on Linux systems
- **AI-Assisted Malware**: Use of AI language models to insert malicious code into npm packages and generate attack code
- **Dormant Backdoors**: Long-term persistence through backdoors hidden in legitimate plugins for years
- **Social Engineering**: EtherRAT campaign spoofing administrative tools via fake GitHub repositories
- **Phishing-as-a-Service**: Bluekit service offering AI-assisted phishing campaigns with 40+ templates

## Threat Actor Activities

- **TeamPCP Group**: Conducting extensive supply chain attacks against SAP npm packages and deploying Vect 2.0 ransomware
- **DPRK-Linked Actors**: Using AI-inserted npm malware, fake companies, and remote access trojans in sophisticated campaigns
- **EtherRAT Operators**: Targeting high-privilege professional accounts through spoofed administrative tools on GitHub
- **Ukrainian Cybercriminals**: Three individuals arrested for hijacking and selling 610,000 Roblox accounts for $225,000 profit
- **Romanian Swatting Ring**: Leader sentenced to 4 years for coordinating attacks against 75+ public officials and journalists
- **Cryptocurrency Scammers**: 276 suspects arrested in joint US-Chinese operation targeting crypto investment fraud centers
- **DEEP#DOOR Operators**: Deploying Python-based backdoor framework for persistent access and credential harvesting