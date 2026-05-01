# Exploitation Report

Current threat intelligence reveals a significant escalation in vulnerability exploitation activities across multiple domains. Critical zero-day exploitation is occurring against cPanel and WHM infrastructure through CVE-2026-41940, an authentication bypass vulnerability that has been actively exploited since late February 2026. Additionally, a newly disclosed local privilege escalation vulnerability dubbed "Copy Fail" is affecting Linux distributions, allowing unprivileged attackers to gain root access. The threat landscape is further complicated by sophisticated supply chain attacks targeting popular development packages including PyTorch Lightning, Ruby Gems, and Go modules, alongside emerging phishing-as-a-service platforms incorporating AI capabilities.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass vulnerability affecting cPanel, WHM, and WP Squared management interfaces
- **Impact**: Complete administrative access bypass, allowing attackers to gain unauthorized control over web hosting infrastructure
- **Status**: Zero-day exploitation confirmed since late February 2026, proof-of-concept exploit code now publicly available
- **CVE ID**: CVE-2026-41940

### Linux "Copy Fail" Privilege Escalation
- **Description**: Local privilege escalation flaw affecting Linux kernels released since 2017
- **Impact**: Allows unprivileged local attackers to gain root permissions on affected systems
- **Status**: Public exploit available, affects major Linux distributions

### PyTorch Lightning Supply Chain Compromise
- **Description**: Malicious versions of the popular Python package Lightning were pushed to conduct credential theft
- **Impact**: Credential harvesting from development environments and CI/CD pipelines
- **Status**: Active compromise affecting Python package repositories

## Affected Systems and Products

- **cPanel/WHM**: Web hosting control panel systems and WP Squared installations
- **Linux Distributions**: Major distributions using kernels from 2017 onwards affected by Copy Fail vulnerability
- **Python Packages**: PyTorch Lightning and Intercom-client packages compromised in supply chain attacks
- **Ruby Gems**: Poisoned packages targeting CI pipeline credentials
- **Go Modules**: Compromised packages exploiting continuous integration environments
- **SAP Cloud Packages**: npm packages in SAP's cloud application development ecosystem targeted by TeamPCP
- **Windows 11**: Backup software failures caused by KB5083769 security update on 24H2 and 25H2 versions
- **France Titres (ANTS)**: French government administrative document agency compromised

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in web hosting infrastructure
- **Supply Chain Attacks**: Compromise of popular development packages to target CI/CD pipelines and steal credentials
- **Sleeper Package Strategy**: Use of dormant malicious packages that activate to deliver secondary payloads
- **Vishing and SSO Abuse**: Rapid SaaS environment attacks using voice phishing combined with single sign-on exploitation
- **AI-Enhanced Phishing**: Bluekit phishing service incorporating AI assistants for campaign generation
- **GitHub Actions Tampering**: Manipulation of CI/CD workflows through compromised packages
- **Cargo Theft Cyber-Enablement**: Cybercriminals facilitating physical cargo theft through digital means

## Threat Actor Activities

- **TeamPCP**: Conducting supply chain attacks against SAP packages using "Mini Shai-Hulud" techniques
- **China-Linked APT Groups**: Targeting Asian governments, NATO states, journalists, and activists across South, East, and Southeast Asia
- **BlackCat/ALPHV Ransomware Operators**: Continued operations despite law enforcement actions, with insider threats from cybersecurity professionals
- **Brazilian DDoS Botnet**: Anti-DDoS firm paradoxically enabling massive DDoS campaigns against Brazilian ISPs
- **Romanian Swatting Ring**: Organized campaigns targeting over 75 public officials and journalists
- **SaaS Extortion Groups**: Two distinct cybercrime groups conducting rapid, high-impact attacks within SaaS environments