# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and services, with attackers leveraging supply chain compromises, zero-day vulnerabilities, and authentication bypass flaws. Notable incidents include the compromise of official SAP npm packages in a TeamPCP supply-chain attack designed to steal developer credentials, active exploitation of remote code execution flaws in the Qinglong task scheduler for cryptomining operations, and zero-day attacks against Windows systems prompting emergency CISA directives. Authentication bypass vulnerabilities in cPanel and GitHub's remote code execution flaw represent significant risks to web hosting infrastructure and code repositories respectively.

## Active Exploitation Details

### Windows Zero-Day Vulnerability
- **Description**: A vulnerability in Microsoft Windows systems being exploited in active zero-day attacks
- **Impact**: Unauthorized system access and potential compromise of federal systems
- **Status**: CISA has ordered federal agencies to patch immediately, indicating active exploitation

### LiteLLM SQL Injection Vulnerability
- **Description**: Critical pre-authentication SQL injection flaw in BerriAI's LiteLLM Python package
- **Impact**: Unauthorized access to sensitive information stored in the large-language model gateway
- **Status**: Actively exploited within 36 hours of public disclosure
- **CVE ID**: CVE-2026-42208

### Qinglong Task Scheduler RCE Vulnerabilities
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Remote code execution leading to cryptominer deployment on developers' servers
- **Status**: Currently being exploited for cryptocurrency mining operations

### GitHub Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability affecting GitHub.com and GitHub Enterprise Server
- **Impact**: Authenticated users could gain remote code execution and access millions of private repositories
- **Status**: Patched in March, but previously exploitable via single Git push
- **CVE ID**: CVE-2026-3854

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software
- **Impact**: Unauthorized access to remote systems and potential lateral movement
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation

### cPanel Authentication Bypass
- **Description**: Critical vulnerability affecting authentication paths in cPanel and WebHost Manager (WHM)
- **Impact**: Unauthorized access to control panel without authentication
- **Status**: Emergency update released, affects all versions except the latest

## Affected Systems and Products

- **SAP npm packages**: Multiple official packages compromised in supply chain attack
- **WordPress Quick Page/Post Redirect plugin**: Over 70,000 sites affected by dormant backdoor
- **Qinglong task scheduler**: Open-source tool used by developers
- **GitHub.com and GitHub Enterprise Server**: Code repository platforms
- **ConnectWise ScreenConnect**: Remote access management software
- **cPanel and WebHost Manager**: Web hosting control panels
- **LiteLLM**: Python package for large language model gateway
- **OpenEMR**: Electronic health record platform used by 100,000+ healthcare providers
- **Microsoft Windows**: Various versions affected by zero-day vulnerability
- **Vimeo**: Video service affected through third-party Anodot breach

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious code injection into legitimate npm packages to steal credentials
- **Authentication Bypass**: Circumventing login mechanisms in web applications and control panels
- **Remote Code Execution**: Exploiting RCE vulnerabilities for cryptomining and system compromise
- **SQL Injection**: Pre-authentication database attacks against AI/ML platforms
- **Backdoor Deployment**: Long-term persistence through hidden backdoors in plugins
- **Git Repository Manipulation**: Exploiting version control systems for code execution
- **Social Engineering**: Fake Zoom calls and AI-generated content for credential theft
- **Ransomware/Wiper Operations**: VECT 2.0 ransomware with encryption flaws causing data destruction

## Threat Actor Activities

- **TeamPCP Group**: Conducting supply chain attacks against SAP npm packages and deploying VECT ransomware
- **BlueNoroff (North Korea)**: Using AI-generated avatars and stolen victim videos in fake Zoom calls targeting cryptocurrency executives
- **DPRK-affiliated actors**: Leveraging AI to insert malicious npm packages and deploy remote access trojans
- **Various Cryptomining Groups**: Exploiting Qinglong vulnerabilities for cryptocurrency mining operations
- **Ukrainian Cybercriminals**: Hijacked 610,000 Roblox accounts for $225,000 profit before arrest
- **Lotus Wiper Operators**: Targeting Venezuelan energy firms and utilities with destructive malware using living-off-the-land techniques
- **Feuding Ransomware Groups**: 0APT and KryBit attacking each other and exposing operational infrastructure