# Exploitation Report

Critical zero-day vulnerabilities are actively being exploited across multiple platforms, with several high-severity flaws requiring immediate attention. The most significant threats include CVE-2026-41940, an authentication bypass vulnerability in cPanel and WHM that has been actively exploited since late February, and CVE-2026-3854, a remote code execution flaw in GitHub that could have provided access to millions of private repositories. Additional concerns include the "Copy Fail" Linux privilege escalation vulnerability affecting kernels since 2017, authentication bypass flaws in Qinglong task scheduler being exploited for cryptomining operations, and a maximum severity Google Gemini CLI vulnerability. Supply chain attacks are also prominent, with compromised SAP npm packages and WordPress plugins containing backdoors posing significant risks to developers and website operators.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting cPanel, WHM, and WP Squared control panels
- **Impact**: Allows attackers to obtain access to control panels without authentication credentials
- **Status**: Actively exploited in the wild since late February 2026, emergency patches available
- **CVE ID**: CVE-2026-41940

### GitHub Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in GitHub's infrastructure
- **Impact**: Could have allowed attackers to access millions of private repositories
- **Status**: Patched in early March 2026, previously active exploitation possible
- **CVE ID**: CVE-2026-3854

### Linux Copy Fail Privilege Escalation
- **Description**: Local privilege escalation vulnerability in Linux kernels released since 2017
- **Impact**: Allows unprivileged local attackers to gain root permissions on major distributions
- **Status**: Exploit code published, affects multiple major Linux distributions

### Qinglong Task Scheduler Authentication Bypass
- **Description**: Two authentication bypass vulnerabilities in the open-source task scheduling tool
- **Impact**: Enables deployment of cryptominers on developers' servers
- **Status**: Actively exploited for cryptomining operations

### Windows Zero-Day Vulnerability
- **Description**: Unspecified vulnerability in Windows systems being exploited in zero-day attacks
- **Impact**: Active exploitation in the wild affecting Windows environments
- **Status**: CISA has ordered federal agencies to patch immediately

## Affected Systems and Products

- **cPanel and WHM**: All versions prior to latest emergency updates, affecting web hosting control panels
- **GitHub**: Millions of private repositories potentially accessible before March patch
- **Linux Distributions**: Major distributions with kernels released since 2017 affected by Copy Fail
- **Qinglong**: Open-source task scheduler used by developers
- **Windows Systems**: Federal systems ordered to patch by CISA
- **SAP npm Packages**: Multiple official packages compromised in supply chain attack
- **WordPress Sites**: Over 70,000 sites using Quick Page/Post Redirect plugin with dormant backdoor
- **OpenEMR**: 38 security flaws discovered in platform used by 100,000+ healthcare providers
- **Google Gemini CLI**: Maximum severity vulnerability in npm package and GitHub Actions workflow

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct access to control panels without credentials in cPanel/WHM systems
- **Supply Chain Attacks**: Compromised npm packages targeting SAP-related development tools
- **Backdoor Injection**: Dormant backdoor in WordPress plugin allowing arbitrary code injection
- **Privilege Escalation**: Local exploitation of Copy Fail vulnerability for root access
- **Remote Code Execution**: GitHub vulnerability enabling repository access
- **Cryptomining Deployment**: Exploitation of Qinglong vulnerabilities for cryptocurrency mining
- **AI-Enhanced Attacks**: Use of LLMs to insert malicious dependencies in development projects
- **Social Engineering**: EtherRAT campaign spoofing administrative tools via fake GitHub repositories
- **DDoS Operations**: Brazilian anti-DDoS firm enabling botnet attacks against ISPs

## Threat Actor Activities

- **TeamPCP Group**: Conducting supply chain attacks targeting SAP npm packages and deploying Vect 2.0 ransomware
- **DPRK-affiliated Actors**: Using AI-inserted npm malware and fake companies to distribute RATs
- **Ukrainian Cybercriminals**: Hijacked 610,000 Roblox gaming accounts generating $225,000 in profits
- **EtherRAT Campaign**: Sophisticated operation targeting high-privilege professional accounts through spoofed GitHub repositories
- **Cryptocurrency Scammers**: International operations with 276 arrests across 9 fraud centers, causing over €50 million in losses
- **Brazilian DDoS Operators**: Anti-DDoS firm enabling massive attacks against internet service providers
- **Automated Attack Groups**: Rapid scanning and compromise of new assets within 24 hours of deployment