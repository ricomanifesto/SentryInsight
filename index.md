# Exploitation Report

A significant wave of supply chain attacks has dominated the cybersecurity landscape, with TeamPCP orchestrating sophisticated campaigns targeting SAP npm packages and PyTorch Lightning to steal credentials from developers. Critical zero-day exploitation is occurring against cPanel and WHM systems through CVE-2026-41940, an authentication bypass vulnerability that has been actively exploited since late February. Additionally, a newly disclosed Linux privilege escalation vulnerability dubbed "Copy Fail" affects major distributions and allows unprivileged users to gain root access. The emergence of AI-assisted attack tools and the deployment of the DEEP#DOOR Python backdoor framework indicate an escalation in attacker capabilities and persistence mechanisms.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in cPanel, WHM, and WP Squared allowing unauthorized access to control panels
- **Impact**: Attackers can gain complete administrative access to web hosting control panels without authentication
- **Status**: Actively exploited as zero-day since late February, emergency patches now available
- **CVE ID**: CVE-2026-41940

### Linux Copy Fail Privilege Escalation
- **Description**: Local privilege escalation vulnerability affecting Linux kernels released since 2017, allowing unprivileged users to gain root permissions
- **Impact**: Complete system compromise with root-level access from any local user account
- **Status**: Proof-of-concept exploit code published, patches available for major distributions

### Qinglong Task Scheduler RCE
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Remote code execution leading to cryptomining deployment on compromised servers
- **Status**: Actively exploited for cryptocurrency mining operations

### OpenEMR Electronic Health Record Platform
- **Description**: 38 security vulnerabilities discovered in the widely-used healthcare platform
- **Impact**: Database compromise, remote code execution, and sensitive health data theft
- **Status**: Affects platform used by over 100,000 healthcare providers

## Affected Systems and Products

- **SAP npm Packages**: Multiple official packages compromised in TeamPCP supply chain attack
- **PyTorch Lightning**: Python package compromised with malicious versions for credential theft
- **cPanel/WHM**: Web hosting control panel systems across all versions prior to latest updates
- **Linux Distributions**: Major distributions affected by Copy Fail vulnerability since 2017
- **WordPress**: Quick Page/Post Redirect plugin with dormant backdoor affecting 70,000+ sites
- **Qinglong**: Open-source task scheduling tool targeted for cryptomining attacks
- **OpenEMR**: Healthcare platform serving over 100,000 medical providers
- **Google Gemini CLI**: npm package and GitHub Actions workflow with maximum severity RCE
- **Intercom-client**: Python package targeted in supply chain compromise

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: TeamPCP targeting official package repositories with credential-stealing malware
- **Mini Shai-Hulud Attack**: Specific technique used against SAP ecosystem packages
- **Authentication Bypass**: Exploitation of login mechanisms in web management interfaces
- **Local Privilege Escalation**: Kernel-level vulnerabilities allowing privilege elevation
- **AI-Assisted Code Injection**: Use of large language models to insert malicious dependencies
- **GitHub Repository Spoofing**: EtherRAT campaign using fake administrative tools on GitHub
- **Tunneling Service Abuse**: DEEP#DOOR backdoor using tunneling for persistence and data exfiltration
- **Dormant Backdoors**: Long-term persistence mechanisms hidden in legitimate plugins

## Threat Actor Activities

- **TeamPCP**: Conducting broad supply chain attacks targeting SAP packages, PyTorch Lightning, and deploying Vect 2.0 ransomware
- **DPRK-linked Groups**: Using AI-inserted npm malware, fake companies, and remote access trojans in coordinated campaigns
- **EtherRAT Operators**: Targeting high-privilege professional accounts through spoofed GitHub repositories
- **Cryptomining Gangs**: Exploiting Qinglong vulnerabilities for unauthorized cryptocurrency mining
- **Romanian Swatting Ring**: Coordinated harassment campaigns targeting public officials and journalists
- **Roblox Account Thieves**: Ukrainian criminals stealing and selling over 610,000 gaming accounts for $225,000 profit
- **Anti-DDoS Firm Abuse**: Brazilian company enabling botnet attacks against internet service providers