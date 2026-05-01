# Exploitation Report

A critical wave of active exploits is targeting multiple platforms and supply chain components across the cybersecurity landscape. The most significant threats include a zero-day authentication bypass vulnerability in cPanel and WHM systems (CVE-2026-41940) that has been actively exploited since late February, a newly disclosed Linux privilege escalation flaw dubbed "Copy Fail" affecting kernels since 2017, and widespread supply chain attacks compromising official SAP npm packages and popular Python libraries. Additionally, a maximum severity vulnerability (CVSS 10.0) was recently patched in Google's Gemini CLI tools, while a dormant backdoor in a widely-used WordPress plugin has been discovered after remaining hidden for five years.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass Vulnerability
- **Description**: A critical authentication bypass vulnerability affecting cPanel, WHM, and WP Squared hosting management platforms
- **Impact**: Allows attackers to bypass authentication mechanisms and gain unauthorized access to web hosting control panels
- **Status**: Currently being actively exploited in the wild since late February 2026, with proof-of-concept exploit code now publicly available
- **CVE ID**: CVE-2026-41940

### Linux "Copy Fail" Privilege Escalation
- **Description**: A local privilege escalation vulnerability affecting Linux kernels released since 2017 that allows unprivileged users to gain root access
- **Impact**: Enables local attackers to escalate privileges to root level on major Linux distributions
- **Status**: Exploit code has been published and is available for exploitation; patches are available for affected distributions

### Google Gemini CLI Remote Code Execution
- **Description**: Maximum severity security flaw in Google's Gemini CLI npm package and GitHub Actions workflow
- **Impact**: Could allow attackers to achieve remote code execution in continuous integration environments
- **Status**: Recently patched by Google; affects "@google/gemini-cli" npm package and "google-github-actions/run-gemini-cli" GitHub Actions workflow

### Quick Page/Post Redirect WordPress Plugin Backdoor
- **Description**: A dormant backdoor discovered in the popular WordPress redirect plugin that had been hidden for five years
- **Impact**: Allows injection of arbitrary code into WordPress sites using the plugin
- **Status**: Backdoor was active and undetected for years; affects over 70,000 WordPress installations

## Affected Systems and Products

- **cPanel and WHM**: Web hosting control panel systems vulnerable to authentication bypass
- **Linux Distributions**: Major distributions with kernels released since 2017 affected by privilege escalation
- **Google Gemini CLI**: npm package and GitHub Actions workflow components
- **WordPress Sites**: Over 70,000 sites using Quick Page/Post Redirect plugin
- **SAP Development Ecosystem**: Official npm packages compromised in supply chain attack
- **Python Package Repositories**: PyTorch Lightning and Intercom-client packages compromised
- **Ruby and Go Ecosystems**: Poisoned gems and modules targeting CI/CD pipelines

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromise of legitimate software packages including SAP npm packages, Python libraries, Ruby gems, and Go modules
- **Authentication Bypass**: Direct exploitation of authentication mechanisms in web hosting platforms
- **Local Privilege Escalation**: Exploitation of kernel vulnerabilities to gain root access on Linux systems
- **CI/CD Pipeline Exploitation**: Targeting continuous integration environments through compromised development tools
- **Credential Theft**: Malicious packages designed to harvest authentication tokens and credentials from developer systems
- **Backdoor Injection**: Long-term persistence through dormant backdoors in popular software components

## Threat Actor Activities

- **TeamPCP**: Conducting sophisticated supply chain attacks targeting SAP development packages and expanding operations to broader software ecosystems
- **BlackCat/ALPHV Ransomware**: Continued operations despite law enforcement actions, with former cybersecurity professionals sentenced for facilitating attacks
- **Python Package Attackers**: Targeting PyTorch Lightning and other popular Python libraries for credential theft
- **CI/CD Threat Actors**: Exploiting development pipelines through poisoned Ruby gems and Go modules to steal credentials and tamper with GitHub Actions