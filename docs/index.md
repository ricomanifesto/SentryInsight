# Exploitation Report

The current threat landscape is marked by a significant surge in supply chain attacks targeting popular development packages, critical authentication bypass vulnerabilities being actively exploited, and the emergence of AI-assisted attack techniques. Notable activity includes TeamPCP's "Mini Shai-Hulud" campaign compromising official SAP npm packages, active exploitation of CVE-2026-41940 in cPanel and WHM systems, and the Linux "Copy Fail" privilege escalation vulnerability affecting major distributions since 2017. Additionally, threat actors are leveraging sophisticated malware frameworks and establishing persistent access through tunneling services to steal credentials and cloud access tokens.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass vulnerability affecting cPanel, WHM, and WP Squared systems that allows unauthorized access to control panels
- **Impact**: Attackers can gain administrative access to web hosting control panels without authentication, potentially compromising entire hosting infrastructures
- **Status**: Being actively exploited in the wild since late February 2026, emergency patches have been released
- **CVE ID**: CVE-2026-41940

### Linux "Copy Fail" Privilege Escalation
- **Description**: Local privilege escalation vulnerability in Linux kernels that allows unprivileged users to gain root access
- **Impact**: Complete system compromise allowing attackers to escalate from limited user accounts to full administrative control
- **Status**: Affects Linux kernels released since 2017, exploit code has been published, patches are available for major distributions
- **CVE ID**: Not specified in articles

### Google Gemini CLI Remote Code Execution
- **Description**: Maximum severity vulnerability in Gemini CLI npm package and GitHub Actions workflow enabling remote code execution
- **Impact**: Attackers can execute arbitrary code in CI/CD environments and development systems
- **Status**: Fixed by Google with CVSS 10 severity rating
- **CVE ID**: Not specified in articles

### Qinglong Task Scheduler Authentication Bypass
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Enables deployment of cryptocurrency miners on developers' servers
- **Status**: Currently being exploited for cryptomining attacks
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **cPanel and WHM**: Web hosting control panels across multiple versions
- **Linux Distributions**: Major distributions with kernels released since 2017
- **SAP npm Packages**: Official SAP development packages in the npm ecosystem
- **PyTorch Lightning**: Popular Python machine learning framework
- **Intercom-client**: JavaScript client library for Intercom services
- **WordPress**: Quick Page/Post Redirect plugin installed on over 70,000 sites
- **Qinglong Task Scheduler**: Open-source task scheduling platform
- **OpenEMR**: Electronic health record platform used by over 100,000 healthcare providers
- **Roblox Gaming Platform**: Accounts compromised through credential theft
- **Google Gemini CLI**: Development tools and CI/CD workflows
- **Cursor IDE**: Code editor with vulnerable components

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious code injection into legitimate npm packages and development tools
- **AI-Assisted Code Injection**: Large language models used to insert malicious dependencies into projects
- **Authentication Bypass**: Exploiting flaws in authentication mechanisms to gain unauthorized access
- **Privilege Escalation**: Local vulnerabilities used to gain administrative privileges on compromised systems
- **Credential Harvesting**: Malware designed to steal authentication tokens, browser credentials, and cloud access keys
- **Backdoor Implantation**: Long-term persistent access mechanisms hidden in popular software packages
- **GitHub Repository Spoofing**: Fake repositories hosting malicious administrative tools
- **Tunneling Services**: Use of legitimate tunneling infrastructure to establish covert communication channels
- **Phishing-as-a-Service**: AI-enhanced phishing kits with automated campaign generation capabilities

## Threat Actor Activities

- **TeamPCP**: Conducting widespread supply chain attacks targeting SAP npm packages with "Mini Shai-Hulud" campaign for credential theft
- **DPRK-Affiliated Groups**: Using AI-inserted npm malware, fake companies, and remote access trojans in sophisticated social engineering campaigns
- **EtherRAT Operators**: Distributing malware through spoofed administrative tools via GitHub facades, targeting high-privilege professional accounts
- **Ukrainian Cybercriminals**: Arrested for hijacking 610,000 Roblox accounts and selling them for $225,000 profit
- **Romanian Swatting Ring**: Leader sentenced to 4 years for coordinating attacks against 75+ public officials and journalists
- **Cryptocurrency Miners**: Exploiting Qinglong vulnerabilities to deploy mining operations on development servers
- **Brazilian DDoS Operators**: Anti-DDoS firm enabling botnet attacks against ISPs
- **DEEP#DOOR Framework Users**: Deploying Python-based backdoors with tunneling capabilities for persistent access and credential theft
- **Vect 2.0 Ransomware Group**: Deploying ransomware with wiper capabilities due to design flaws, affecting TeamPCP attack victims