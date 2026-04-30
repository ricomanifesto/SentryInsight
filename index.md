# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity across multiple critical vulnerabilities. Several zero-day attacks have been confirmed, including a Windows authentication bypass flaw and ConnectWise ScreenConnect vulnerabilities that CISA has added to its Known Exploited Vulnerabilities catalog. Supply chain attacks are particularly concerning, with SAP-related npm packages compromised in TeamPCP operations and a dormant backdoor discovered in a popular WordPress plugin affecting over 70,000 sites. Critical remote code execution vulnerabilities are being actively exploited in GitHub Enterprise Server (CVE-2026-3854), LiteLLM gateway systems (CVE-2026-42208), and cPanel authentication systems. North Korean threat actors continue sophisticated campaigns targeting cryptocurrency executives and developers through AI-enhanced social engineering and malicious npm packages.

## Active Exploitation Details

### Windows Authentication Bypass Vulnerability
- **Description**: A critical authentication bypass vulnerability in Windows systems that allows attackers to circumvent security controls
- **Impact**: Unauthorized access to Windows systems and potential privilege escalation
- **Status**: Being exploited as zero-day; CISA has mandated federal agencies to patch immediately

### ConnectWise ScreenConnect Vulnerabilities
- **Description**: Critical security flaws in the ConnectWise ScreenConnect remote access platform
- **Impact**: Unauthorized remote access to managed systems and potential lateral movement
- **Status**: Actively exploited in the wild; added to CISA's Known Exploited Vulnerabilities catalog

### GitHub Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability exploitable through a single Git push operation
- **Impact**: Access to millions of private repositories and potential code theft or tampering
- **Status**: Patched in early March 2026; was exploitable against GitHub.com and Enterprise Server
- **CVE ID**: CVE-2026-3854

### LiteLLM SQL Injection Vulnerability
- **Description**: Pre-authentication SQL injection flaw in the BerriAI LiteLLM Python package
- **Impact**: Access to sensitive information stored in large language model gateways
- **Status**: Actively exploited within 36 hours of public disclosure
- **CVE ID**: CVE-2026-42208

### cPanel/WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting multiple authentication paths in cPanel and WebHost Manager
- **Impact**: Unauthorized access to web hosting control panels without authentication
- **Status**: Emergency patches released; affects all but the latest versions

### Qinglong Task Scheduler RCE Flaws
- **Description**: Two authentication bypass vulnerabilities in the open-source Qinglong task scheduling tool
- **Impact**: Remote code execution and deployment of cryptocurrency miners on developer servers
- **Status**: Actively exploited for cryptomining operations

### WordPress Quick Page/Post Redirect Plugin Backdoor
- **Description**: Dormant backdoor present in the plugin for five years, allowing arbitrary code injection
- **Impact**: Complete compromise of WordPress sites through code injection capabilities
- **Status**: Backdoor discovered affecting over 70,000 WordPress installations

## Affected Systems and Products

- **SAP npm Packages**: Multiple official packages compromised in TeamPCP supply-chain attacks
- **WordPress Sites**: Over 70,000 installations using Quick Page/Post Redirect plugin
- **GitHub Platforms**: GitHub.com and GitHub Enterprise Server vulnerable to RCE
- **LiteLLM Gateway**: Open-source large language model gateway systems
- **cPanel/WHM**: Web hosting control panel software across multiple versions
- **Qinglong Scheduler**: Open-source task scheduling platform used by developers
- **ConnectWise ScreenConnect**: Remote access and support platform
- **Windows Systems**: Microsoft Windows operating systems with authentication bypass vulnerability
- **OpenEMR Platform**: Electronic health record platform used by 100,000+ healthcare providers
- **Roblox Gaming Platform**: 610,000 user accounts compromised and sold

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Injection of malicious code into legitimate npm packages and software dependencies
- **Authentication Bypass**: Exploitation of flaws allowing unauthorized access without credentials
- **Remote Code Execution**: Direct code execution on target systems through various vulnerability classes
- **SQL Injection**: Database compromise through unsanitized input in web applications
- **Social Engineering**: AI-enhanced fake video calls and impersonation techniques
- **Cryptomining Deployment**: Installation of cryptocurrency mining software on compromised systems
- **Living-off-the-Land**: Use of legitimate system tools for malicious purposes in wiper attacks
- **OAuth Token Theft**: Stealing authentication tokens through compromised third-party integrations
- **Backdoor Implantation**: Long-term persistence mechanisms in widely-used software

## Threat Actor Activities

- **TeamPCP Group**: Conducting sophisticated supply-chain attacks targeting SAP npm packages and deploying VECT 2.0 ransomware
- **North Korean BlueNoroff**: Using AI-generated avatars and stolen victim videos in fake Zoom calls to target cryptocurrency executives
- **DPRK Operators**: Deploying AI-inserted npm malware through fake companies and remote access trojans
- **Ukrainian Cybercriminals**: Arrested for hijacking 610,000 Roblox accounts and selling them for $225,000 profit
- **Cryptomining Groups**: Exploiting Qinglong scheduler vulnerabilities for cryptocurrency mining operations
- **Ransomware Operators**: Deploying broken VECT 2.0 ransomware that acts as a data wiper due to encryption flaws
- **Venezuelan Energy Attackers**: Using Lotus wiper malware with sophisticated living-off-the-land techniques against energy firms