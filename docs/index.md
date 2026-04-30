# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and software components across enterprise and open-source environments. Active zero-day exploitation has been identified in Windows systems, with CISA ordering immediate federal agency remediation. Supply chain attacks have compromised official SAP npm packages and WordPress plugins affecting hundreds of thousands of installations. Several remote code execution vulnerabilities are being actively exploited, including flaws in GitHub's infrastructure that could have exposed millions of private repositories, Qinglong task schedulers being targeted for cryptomining operations, and a critical Google Gemini CLI vulnerability with maximum CVSS severity. Authentication bypass vulnerabilities in cPanel and ConnectWise ScreenConnect are also under active exploitation, while a newly disclosed SQL injection flaw in LiteLLM was exploited within 36 hours of public disclosure.

## Active Exploitation Details

### Windows Zero-Day Vulnerability
- **Description**: A Windows vulnerability that has been exploited in zero-day attacks before patches were available
- **Impact**: Unauthorized access to Windows systems and potential privilege escalation
- **Status**: Actively exploited as zero-day, CISA has ordered federal agencies to patch immediately

### Google Gemini CLI Remote Code Execution
- **Description**: A maximum severity security flaw in the "@google/gemini-cli" npm package and "google-github-actions/run-gemini-cli" GitHub Actions workflow
- **Impact**: Remote code execution in CI/CD environments and development systems
- **Status**: Fixed by Google with emergency patches released

### GitHub Remote Code Execution Vulnerability
- **Description**: A critical remote code execution vulnerability in GitHub's infrastructure
- **Impact**: Could have allowed attackers to access millions of private repositories
- **Status**: Patched in early March 2026
- **CVE ID**: CVE-2026-3854

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software
- **Impact**: Unauthorized access to remote management capabilities
- **Status**: Actively exploited, added to CISA KEV catalog

### cPanel Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting cPanel and WebHost Manager (WHM) dashboard
- **Impact**: Unauthorized access to control panel without authentication credentials
- **Status**: Emergency updates released, affects all versions except the latest

### LiteLLM SQL Injection Vulnerability
- **Description**: Critical pre-authentication SQL injection vulnerability in BerriAI's LiteLLM Python package
- **Impact**: Access to sensitive information stored in the LLM gateway
- **Status**: Exploited within 36 hours of disclosure
- **CVE ID**: CVE-2026-42208

### Qinglong Task Scheduler RCE Flaws
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Deployment of cryptominers on developers' servers
- **Status**: Actively exploited by threat actors for cryptomining operations

### Linux 'Copy Fail' Local Privilege Escalation
- **Description**: A high-severity local privilege escalation flaw affecting major Linux distributions
- **Impact**: Allows unprivileged local users to obtain root access
- **Status**: Recently disclosed with patches being developed

## Affected Systems and Products

- **Windows Systems**: All versions affected by the zero-day vulnerability under active exploitation
- **Google Gemini CLI**: "@google/gemini-cli" npm package and GitHub Actions workflow
- **GitHub Platform**: Millions of private repositories potentially at risk from RCE vulnerability
- **ConnectWise ScreenConnect**: Remote access and management software
- **cPanel/WHM**: Web hosting control panel software affecting hosting providers globally
- **LiteLLM Package**: Python package used for large language model gateway operations
- **Qinglong Task Scheduler**: Open-source task scheduling tool used by developers
- **SAP npm Packages**: Multiple official SAP packages in the npm ecosystem
- **WordPress Sites**: Quick Page/Post Redirect plugin installed on over 70,000 sites
- **OpenEMR Platform**: Electronic health record platform used by over 100,000 healthcare providers
- **Linux Distributions**: Major Linux distributions affected by Copy Fail vulnerability

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate targeting of unpatched Windows systems before public disclosure
- **Supply Chain Attacks**: Compromise of official npm packages and WordPress plugins to reach downstream users
- **Authentication Bypass**: Direct circumvention of login mechanisms in control panels and remote access tools
- **SQL Injection**: Pre-authentication database attacks targeting LLM gateway systems
- **Remote Code Execution**: Exploitation of CI/CD environments and development infrastructure
- **Local Privilege Escalation**: Escalation from unprivileged to root access on Linux systems
- **Cryptomining Operations**: Deployment of cryptocurrency miners on compromised developer servers
- **Backdoor Installation**: Long-term persistence through dormant backdoors in popular plugins

## Threat Actor Activities

- **TeamPCP Group**: Conducting supply-chain attacks targeting SAP npm packages for credential theft and authentication token harvesting
- **Unknown Cryptomining Actors**: Actively exploiting Qinglong vulnerabilities to deploy miners on developer infrastructure
- **WordPress Plugin Attackers**: Maintaining dormant backdoors in popular plugins for long-term access to thousands of websites
- **North Korean Groups (DPRK)**: Using AI-generated content and fake firms in new wave of npm malware attacks
- **BlueNoroff (North Korean)**: Using stolen victim videos and AI-generated avatars in fake Zoom calls targeting cryptocurrency executives
- **Venezuelan Energy Sector Attackers**: Deploying Lotus Wiper malware against energy firms and utilities using living-off-the-land techniques
- **Ransomware Operators**: Deploying VECT 2.0 ransomware that acts as a wiper due to design flaws in encryption handling
- **Various APT Groups**: Rapid exploitation of newly disclosed vulnerabilities within hours of public release