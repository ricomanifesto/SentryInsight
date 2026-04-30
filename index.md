# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation across web hosting platforms, development tools, and enterprise software. The most severe activity involves a zero-day authentication bypass vulnerability in cPanel and WHM (CVE-2026-41940) that has been exploited since late February, alongside rapid exploitation of a SQL injection flaw in LiteLLM (CVE-2026-42208) within 36 hours of disclosure. Additional critical exploitation includes remote code execution flaws in GitHub (CVE-2026-3854), Google Gemini CLI with maximum CVSS 10 severity, ConnectWise ScreenConnect, and authentication bypass vulnerabilities in Qinglong task scheduler. Supply chain attacks targeting SAP npm packages and sophisticated malware campaigns including DEEP#DOOR backdoor and EtherRAT distribution are also actively compromising systems.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting all versions of cPanel and WebHost Manager (WHM) dashboard except the latest versions
- **Impact**: Attackers can obtain unauthorized access to control panels without authentication, potentially compromising web hosting infrastructure
- **Status**: Actively exploited as zero-day since late February, emergency patches released, PoC code now available
- **CVE ID**: CVE-2026-41940

### LiteLLM SQL Injection
- **Description**: Critical SQL injection vulnerability in BerriAI's LiteLLM Python package
- **Impact**: Database compromise and potential remote code execution in AI/ML environments
- **Status**: Exploited within 36 hours of public disclosure, actively targeted by threat actors
- **CVE ID**: CVE-2026-42208

### GitHub Remote Code Execution
- **Description**: Critical remote code execution vulnerability in GitHub's infrastructure
- **Impact**: Could allow attackers to access millions of private repositories and execute arbitrary code
- **Status**: Patched in early March after discovery through AI-assisted reverse engineering
- **CVE ID**: CVE-2026-3854

### Google Gemini CLI Remote Code Execution
- **Description**: Maximum severity vulnerability in "@google/gemini-cli" npm package and "google-github-actions/run-gemini-cli" GitHub Actions workflow
- **Impact**: Remote code execution in CI/CD environments and development workflows
- **Status**: Recently patched by Google, CVSS 10 severity rating

### Qinglong Task Scheduler Authentication Bypass
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Deployment of cryptocurrency miners on developers' servers
- **Status**: Actively exploited for cryptomining operations

### Linux 'Copy Fail' Privilege Escalation
- **Description**: High-severity local privilege escalation flaw affecting major Linux distributions
- **Impact**: Allows unprivileged local users to obtain root access
- **Status**: Recently disclosed, affects multiple major distributions

### Windows Zero-Day Vulnerability
- **Description**: Windows vulnerability exploited in zero-day attacks
- **Impact**: System compromise on Windows environments
- **Status**: Actively exploited, CISA ordered federal agencies to patch immediately

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software
- **Impact**: Potential remote access and system compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, actively exploited

## Affected Systems and Products

- **cPanel and WHM**: Web hosting control panels, all versions except latest updates
- **LiteLLM Python Package**: AI/ML development environments using BerriAI's package
- **GitHub Infrastructure**: Millions of private repositories and development environments
- **Google Gemini CLI**: CI/CD pipelines using Google's Gemini CLI tools and GitHub Actions
- **Qinglong Task Scheduler**: Open-source task scheduling deployments
- **Linux Distributions**: Major distributions affected by 'Copy Fail' vulnerability
- **Microsoft Windows**: Federal agencies and enterprise Windows deployments
- **ConnectWise ScreenConnect**: Remote access management systems
- **SAP npm Packages**: Development environments using official SAP npm packages
- **WordPress Sites**: Over 70,000 sites using Quick Page/Post Redirect plugin
- **OpenEMR Platform**: Electronic health record systems used by 100,000+ healthcare providers

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct access to control panels and administrative interfaces without credentials
- **SQL Injection**: Database compromise through malicious SQL queries in web applications
- **Supply Chain Attacks**: Compromise of legitimate npm packages to distribute malware
- **Zero-Day Exploitation**: Targeting unpatched vulnerabilities before fixes are available
- **AI-Assisted Attacks**: Using large language models to insert malicious code and automate attack processes
- **Social Engineering**: Fake Zoom calls and AI-generated avatars for targeted deception
- **Tunneling Services**: DEEP#DOOR backdoor using tunneling for persistent access and credential theft
- **GitHub Facades**: EtherRAT distribution spoofing administrative tools through fake repositories
- **Dormant Backdoors**: WordPress plugin backdoors remaining hidden for years before activation

## Threat Actor Activities

- **TeamPCP Group**: Conducting supply chain attacks against SAP npm packages and deploying VECT 2.0 ransomware
- **BlueNoroff (North Korean)**: Using stolen victim videos and AI-generated avatars in fake Zoom calls targeting cryptocurrency executives
- **DPRK Actors**: New wave of attacks using AI-inserted npm malware, fake firms, and remote access trojans
- **Cryptocurrency Scammers**: International operations with 276 arrests across 9 fraud centers, €50 million fraud ring dismantled
- **Roblox Account Hijackers**: Ukrainian criminals arrested for compromising 610,000 gaming accounts for $225,000 profit
- **Venezuelan Energy Attackers**: Lotus Wiper deployment targeting energy firms and utilities with sophisticated living-off-the-land techniques
- **Atos Threat Research Identified Campaign**: Sophisticated operation targeting high-privilege professional accounts through administrative tool spoofing