# Exploitation Report

Critical vulnerabilities across multiple platforms are being actively exploited in the wild, with several zero-day attacks targeting enterprise infrastructure. The most severe exploitation activity includes authentication bypass flaws in cPanel and WHM hosting platforms being exploited as zero-days, remote code execution vulnerabilities in Qinglong task schedulers used for cryptomining campaigns, and compromised npm packages in supply chain attacks targeting SAP development environments. Additional concerning activity includes Windows vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog and a GitHub remote code execution flaw that provided access to millions of private repositories.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass vulnerability affecting cPanel, WHM, and WP Squared platforms that allows attackers to gain unauthorized access to control panel software without authentication
- **Impact**: Complete compromise of web hosting control panels, potentially affecting thousands of websites and servers
- **Status**: Actively exploited as zero-day since late February, emergency updates now available
- **CVE ID**: CVE-2026-41940

### Qinglong Task Scheduler Remote Code Execution
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool that allow remote code execution
- **Impact**: Deployment of cryptocurrency miners on compromised developer servers
- **Status**: Currently being exploited in the wild for cryptomining operations

### GitHub Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw in GitHub's infrastructure that could provide unauthorized access to private repositories
- **Impact**: Potential access to millions of private repositories and sensitive source code
- **Status**: Patched in early March after active exploitation concerns
- **CVE ID**: CVE-2026-3854

### LiteLLM SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in BerriAI's LiteLLM Python package
- **Impact**: Database compromise and potential remote code execution
- **Status**: Exploited within 36 hours of public disclosure
- **CVE ID**: CVE-2026-42208

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software
- **Impact**: Unauthorized remote access to managed systems
- **Status**: Added to CISA Known Exploited Vulnerabilities catalog, actively exploited

### Microsoft Windows Zero-Day Vulnerability
- **Description**: Windows vulnerability being exploited in zero-day attacks
- **Impact**: System compromise and privilege escalation
- **Status**: CISA ordered federal agencies to patch immediately due to active exploitation

### Linux "Copy Fail" Local Privilege Escalation
- **Description**: High-severity Linux local privilege escalation vulnerability that allows unprivileged users to obtain root access
- **Impact**: Complete system compromise from local access
- **Status**: Affects major Linux distributions, patches available

## Affected Systems and Products

- **cPanel and WHM**: Web hosting control panel software used by hosting providers worldwide
- **Qinglong Task Scheduler**: Open-source task scheduling tool used by developers
- **GitHub Enterprise**: Source code repositories and development platforms
- **LiteLLM**: Python package for AI/ML applications
- **ConnectWise ScreenConnect**: Remote access and support software
- **Microsoft Windows**: Enterprise and consumer operating systems
- **Linux Distributions**: Major distributions including Ubuntu, Red Hat, and others
- **SAP npm Packages**: Official SAP development packages in npm registry
- **WordPress Sites**: Sites using Quick Page/Post Redirect plugin (70,000+ installations)
- **OpenEMR Platform**: Electronic health record system used by 100,000+ healthcare providers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple vulnerabilities exploited before patches were available
- **Supply Chain Attacks**: Compromised npm packages containing credential-stealing malware
- **Authentication Bypass**: Direct circumvention of authentication mechanisms in web applications
- **SQL Injection**: Database compromise through malicious SQL queries
- **Remote Code Execution**: Direct execution of arbitrary code on target systems
- **Cryptomining Deployment**: Installation of cryptocurrency mining software on compromised systems
- **Backdoor Installation**: Long-term persistent access through hidden backdoors
- **Social Engineering**: Use of fake Zoom calls and AI-generated content to target victims

## Threat Actor Activities

- **TeamPCP Group**: Conducting supply chain attacks against SAP-related npm packages and deploying VECT 2.0 ransomware
- **BlueNoroff (North Korean APT)**: Using AI-generated avatars and fake Zoom calls to target cryptocurrency executives with malware
- **DPRK-linked Groups**: Deploying AI-inserted npm malware and using fake companies as attack infrastructure
- **Cryptomining Operations**: Opportunistic attackers exploiting Qinglong vulnerabilities for cryptocurrency mining
- **WordPress Backdoor Operators**: Long-term campaign maintaining dormant backdoors in popular WordPress plugins for five years
- **Financial Fraud Networks**: Organized crime groups running cryptocurrency investment scams with combined losses exceeding €50 million