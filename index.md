# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and services across various sectors. Attackers are actively exploiting vulnerabilities in widely-used systems including cPanel web hosting control panels, GitHub's code repository platform, LiteLLM AI gateways, and Qinglong task schedulers. Zero-day exploitation has been confirmed for Windows systems, while supply chain attacks are targeting npm packages and VS Code extensions. The landscape includes sophisticated threat actors employing AI-assisted attack methods, with North Korean groups launching social engineering campaigns and ransomware operators conducting destructive attacks on critical infrastructure.

## Active Exploitation Details

### Qinglong Task Scheduler Authentication Bypass
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool allowing unauthorized access
- **Impact**: Attackers can deploy cryptominers on developers' servers and gain unauthorized access to task scheduling systems
- **Status**: Actively exploited for cryptomining operations

### cPanel Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw affecting all but the latest versions of cPanel and WebHost Manager (WHM)
- **Impact**: Unauthorized access to control panels without authentication, potentially affecting thousands of web hosting environments
- **Status**: Emergency patches released by cPanel to address active exploitation

### GitHub Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability discovered through AI reverse-engineering techniques
- **Impact**: Unauthorized access to millions of private repositories and potential code execution on GitHub infrastructure
- **Status**: Patched in early March 2026
- **CVE ID**: CVE-2026-3854

### LiteLLM SQL Injection Vulnerability
- **Description**: Pre-authentication SQL injection flaw in the LiteLLM Python package for large language model gateways
- **Impact**: Access to sensitive information stored in LLM gateway databases and potential data exfiltration
- **Status**: Actively exploited within 36 hours of public disclosure
- **CVE ID**: CVE-2026-42208

### Windows Zero-Day Vulnerability
- **Description**: Unspecified Windows vulnerability being exploited in zero-day attacks
- **Impact**: System compromise and unauthorized access to Windows environments
- **Status**: CISA has ordered federal agencies to patch; actively exploited in the wild

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software
- **Impact**: Unauthorized remote access to systems and potential lateral movement
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog

## Affected Systems and Products

- **cPanel/WebHost Manager**: Web hosting control panel software affecting multiple versions prior to latest updates
- **GitHub Platform**: Code repository hosting service with millions of private repositories at risk
- **LiteLLM Gateway**: Python package for large language model integration used in AI applications
- **Qinglong Scheduler**: Open-source task scheduling tool used by developers
- **Microsoft Windows**: Operating systems vulnerable to zero-day exploitation
- **ConnectWise ScreenConnect**: Remote access and support software
- **OpenEMR Platform**: Electronic health record system used by over 100,000 healthcare providers with 38 identified vulnerabilities
- **SAP-related npm Packages**: Supply chain compromise affecting Node.js package ecosystem
- **VS Code Extensions**: Visual Studio Code marketplace extensions infected with malware

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct circumvention of authentication mechanisms in web applications and control panels
- **SQL Injection**: Pre-authentication database manipulation in AI gateway applications
- **Remote Code Execution**: Exploitation through single Git push operations and AI-assisted reverse engineering
- **Supply Chain Attacks**: Compromised npm packages and VS Code extensions spreading malware
- **Social Engineering**: AI-generated avatars and fake video calls targeting cryptocurrency executives
- **Cryptomining Deployment**: Installation of cryptocurrency miners on compromised developer servers
- **Living-off-the-Land Techniques**: Use of legitimate system tools for malicious purposes in destructive attacks

## Threat Actor Activities

- **North Korean Groups (BlueNoroff)**: Conducting sophisticated social engineering campaigns using AI-generated content and fake Zoom calls targeting cryptocurrency sector
- **LofyGang**: Brazilian cybercrime group resurging after three years with Minecraft-targeted stealer campaigns
- **DPRK-linked Actors**: Deploying AI-inserted npm malware and establishing fake companies for sustained operations
- **Scattered Spider**: Prolific hacking group with members facing federal charges for large-scale cybercriminal activities
- **Ukrainian Cybercriminals**: Arrested for hijacking over 610,000 Roblox gaming accounts generating $225,000 in profits
- **Ransomware Operators**: Deploying VECT 2.0 ransomware that acts as a wiper due to encryption flaws, and Lotus Wiper targeting Venezuelan energy infrastructure
- **Supply Chain Attackers**: Orchestrating GlassWorm campaign through malicious VS Code extensions and compromising SAP-related packages