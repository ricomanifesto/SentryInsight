# Exploitation Report

The cybersecurity landscape is experiencing a surge in sophisticated supply chain attacks and zero-day exploitations targeting critical infrastructure and development environments. Multiple high-severity vulnerabilities are being actively exploited, including a critical authentication bypass vulnerability in cPanel and WHM platforms (CVE-2026-41940), a Linux privilege escalation flaw dubbed "Copy Fail," and widespread supply chain compromises affecting SAP npm packages and popular Python libraries. The emergence of AI-assisted attack tools and the exploitation of newly discovered vulnerabilities in widely-used platforms demonstrates the evolving threat landscape facing organizations worldwide.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting all but the latest versions of cPanel and WebHost Manager (WHM) dashboard
- **Impact**: Allows attackers to obtain access to the control panel without authentication, potentially leading to complete server compromise
- **Status**: Actively exploited as a zero-day since late February 2026; emergency patch now available
- **CVE ID**: CVE-2026-41940

### Linux Copy Fail Privilege Escalation
- **Description**: Local privilege escalation vulnerability affecting Linux kernels released since 2017, allowing unprivileged users to gain root access
- **Impact**: Complete system compromise through privilege escalation from unprivileged user to root access
- **Status**: Exploit code published; affects major Linux distributions

### Qinglong Task Scheduler Remote Code Execution
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Remote code execution enabling deployment of cryptocurrency miners on developers' servers
- **Status**: Actively exploited for cryptomining operations

### SAP npm Package Compromise
- **Description**: Multiple official SAP npm packages compromised in TeamPCP supply chain attack campaign known as "Mini Shai-Hulud"
- **Impact**: Credential and authentication token theft from developers' systems
- **Status**: Active supply chain attack targeting SAP cloud application development ecosystem

### Google Gemini CLI Critical Vulnerability
- **Description**: Maximum severity security flaw in Gemini CLI npm package and GitHub Actions workflow
- **Impact**: Remote code execution in continuous integration environments
- **Status**: Patched by Google; CVSS score of 10.0

## Affected Systems and Products

- **cPanel and WHM**: All versions prior to latest emergency update vulnerable to authentication bypass
- **Linux Distributions**: Major distributions running kernels released since 2017 affected by Copy Fail vulnerability
- **SAP Development Tools**: Multiple official SAP npm packages compromised in supply chain attacks
- **PyTorch Lightning**: Popular Python package compromised for credential theft
- **Intercom-client**: Python package targeted in supply chain attacks
- **Quick Page/Post Redirect Plugin**: WordPress plugin with 70,000+ installations containing 5-year-old backdoor
- **Qinglong Task Scheduler**: Open-source tool exploited for cryptomining deployment
- **OpenEMR Platform**: Healthcare platform with 38 newly discovered security flaws affecting 100,000+ providers
- **Google Gemini CLI**: CI/CD environments using affected npm package and GitHub Actions workflow
- **Windows 11**: KB5083769 update causing backup software failures on 24H2 and 25H2 versions

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: TeamPCP group compromising legitimate npm packages to inject malicious code
- **Zero-Day Exploitation**: Active exploitation of unpatched authentication bypass vulnerabilities
- **AI-Assisted Attacks**: Use of large language models to inject malicious dependencies into projects
- **Credential Harvesting**: Deployment of backdoors and malware to steal authentication tokens and browser credentials
- **Cryptomining Deployment**: Exploitation of RCE vulnerabilities to install cryptocurrency miners
- **GitHub Repository Spoofing**: Creation of fake administrative tool repositories to distribute EtherRAT malware
- **Dormant Backdoors**: Long-term persistence through backdoors hidden in popular plugins for years
- **Phishing-as-a-Service**: Bluekit platform offering AI-assisted phishing campaign generation with 40+ templates

## Threat Actor Activities

- **TeamPCP**: Conducting widespread supply chain attacks targeting SAP packages and deploying Vect 2.0 ransomware (which acts as a wiper due to design flaws)
- **DPRK-linked Groups**: Utilizing AI-inserted npm malware, fake companies, and remote access trojans in sophisticated campaigns
- **EtherRAT Operators**: Targeting high-privilege professional accounts through spoofed GitHub repositories containing administrative tools
- **Cybercriminal Networks**: FBI-linked surge in cyber-enabled cargo theft with estimated losses reaching significant levels in US and Canada
- **DEEP#DOOR Framework Users**: Deploying Python-based backdoors using tunneling services to maintain persistent access and harvest credentials
- **Cryptocurrency Scammers**: International operation dismantled 9 crypto investment fraud centers with 276 arrests
- **Roblox Account Hijackers**: Ukrainian operation compromised 610,000 gaming accounts for $225,000 profit before arrest