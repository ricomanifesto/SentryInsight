# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple attack vectors, with critical zero-day vulnerabilities being actively exploited in production environments. The most severe incidents include authentication bypass vulnerabilities in web hosting infrastructure, supply chain attacks targeting development environments, and local privilege escalation flaws affecting major Linux distributions. Notably, a maximum severity remote code execution vulnerability in Google's Gemini CLI has been addressed, while authentication bypass vulnerabilities in cPanel and WHM continue to face active exploitation attempts. The period has also seen extensive supply chain compromise campaigns targeting popular development packages and frameworks, demonstrating the evolving sophistication of threat actors in targeting software development pipelines.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass vulnerability affecting cPanel, WHM, and WP Squared hosting management platforms
- **Impact**: Allows attackers to bypass authentication mechanisms and gain unauthorized access to hosting control panels
- **Status**: Currently being exploited in the wild with active exploitation attempts detected since late February 2026, proof-of-concept exploit code now publicly available
- **CVE ID**: CVE-2026-41940

### Linux Copy Fail Local Privilege Escalation
- **Description**: Local privilege escalation vulnerability affecting Linux kernels released since 2017, dubbed "Copy Fail"
- **Impact**: Allows unprivileged local attackers to gain root access on affected systems
- **Status**: Exploit code has been published and is actively being used to compromise Linux systems across major distributions

### Google Gemini CLI Remote Code Execution
- **Description**: Maximum severity security flaw in Google's Gemini CLI npm package and GitHub Actions workflow
- **Impact**: Could allow remote code execution in CI/CD environments and development pipelines
- **Status**: Recently patched by Google, previously posed critical risk to development infrastructure

### Quick Page/Post Redirect WordPress Plugin Backdoor
- **Description**: Dormant backdoor discovered in popular WordPress redirect plugin that remained hidden for five years
- **Impact**: Enables injection of arbitrary code into WordPress sites, potentially compromising over 70,000 installations
- **Status**: Backdoor was embedded years ago and has been dormant, now discovered and being addressed

## Affected Systems and Products

- **cPanel and WHM**: Web hosting control panel software used by hosting providers globally
- **WP Squared**: WordPress management platform integrated with cPanel/WHM environments
- **Linux Distributions**: Major Linux distributions running kernels released since 2017, including enterprise and desktop versions
- **Google Gemini CLI**: Development tool for Google's AI platform integration (@google/gemini-cli npm package)
- **GitHub Actions**: CI/CD workflows using google-github-actions/run-gemini-cli
- **WordPress Sites**: Over 70,000 installations using Quick Page/Post Redirect plugin
- **PyTorch Lightning**: Popular Python machine learning framework
- **SAP npm Packages**: Official SAP development packages for cloud application development
- **Ruby Gems and Go Modules**: Development packages used in CI/CD pipelines

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct exploitation of authentication mechanisms in web hosting platforms
- **Supply Chain Poisoning**: Compromising legitimate software packages to distribute malicious payloads
- **Sleeper Package Attacks**: Deploying seemingly benign packages that later push malicious updates
- **CI/CD Pipeline Exploitation**: Targeting continuous integration systems to steal credentials and manipulate workflows
- **Local Privilege Escalation**: Exploiting kernel vulnerabilities to gain elevated system access
- **Backdoor Injection**: Installing persistent access mechanisms in popular software plugins
- **Credential Harvesting**: Stealing authentication tokens, API keys, and development credentials
- **GitHub Repository Spoofing**: Creating fake administrative tool repositories to distribute malware

## Threat Actor Activities

- **TeamPCP**: Conducting supply chain attacks against SAP npm packages and other development tools using "Mini Shai-Hulud" attack techniques
- **BlackCat Ransomware Operators**: Former cybersecurity professionals sentenced for facilitating ransomware attacks, highlighting insider threat risks
- **Supply Chain Attackers**: Multiple groups targeting Python packages (PyTorch Lightning), Ruby gems, and Go modules for credential theft
- **EtherRAT Campaign**: Sophisticated operation targeting high-privilege professional accounts through GitHub repository spoofing
- **Bluekit Phishing Service**: New phishing-as-a-service platform offering AI-assisted campaign generation with over 40 templates
- **DEEP#DOOR Operators**: Deploying Python-based backdoor framework with tunneling capabilities for persistent access and credential harvesting
- **Anti-DDoS Firm Abuse**: Brazilian company enabling botnet operations while purporting to provide DDoS protection services