# Exploitation Report

Critical exploitation activity is escalating across multiple platforms, with attackers rapidly targeting newly disclosed vulnerabilities and leveraging sophisticated supply chain attacks. The most concerning developments include zero-day exploitation of Windows systems ordered to be patched by CISA, critical authentication bypass vulnerabilities in cPanel affecting web hosting infrastructure, and widespread compromise of SAP npm packages in TeamPCP supply chain attacks. Threat actors are demonstrating remarkable speed in exploiting newly disclosed flaws, with some vulnerabilities being actively exploited within 36 hours of public disclosure. Additionally, attackers are increasingly using AI-enhanced techniques and targeting critical infrastructure, including financial services and healthcare platforms.

## Active Exploitation Details

### Windows Zero-Day Vulnerability
- **Description**: A critical Windows vulnerability that has been exploited in zero-day attacks before patches were available
- **Impact**: Allows attackers to compromise Windows systems and potentially gain unauthorized access to federal networks
- **Status**: CISA has ordered federal agencies to immediately patch their systems, indicating active exploitation in the wild

### LiteLLM SQL Injection Vulnerability
- **Description**: Critical pre-authentication SQL injection vulnerability in the BerriAI LiteLLM Python package used for large language model gateways
- **Impact**: Attackers can access sensitive information stored in LiteLLM systems without authentication
- **Status**: Actively exploited within 36 hours of public disclosure
- **CVE ID**: CVE-2026-42208

### cPanel and WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting all but the latest versions of cPanel and WebHost Manager dashboard
- **Impact**: Allows attackers to obtain access to web hosting control panels without proper authentication credentials
- **Status**: Emergency updates released by cPanel to address active exploitation concerns

### GitHub Remote Code Execution Vulnerability
- **Description**: Critical RCE vulnerability that could allow authenticated users to execute remote code and access millions of private repositories
- **Impact**: Potential unauthorized access to private source code repositories and sensitive development data
- **Status**: Patched by GitHub in March after discovery through AI-assisted reverse engineering
- **CVE ID**: CVE-2026-3854

### Qinglong Task Scheduler RCE Flaws
- **Description**: Two authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool
- **Impact**: Enables deployment of cryptocurrency miners on developers' servers
- **Status**: Actively exploited by hackers for cryptomining operations

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw affecting ConnectWise ScreenConnect remote access software
- **Impact**: Allows unauthorized access to remote systems and potential lateral movement
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation

## Affected Systems and Products

- **SAP npm Packages**: Multiple official packages compromised in TeamPCP supply chain attacks targeting developer credentials
- **WordPress Sites**: Quick Page/Post Redirect plugin with dormant backdoor affecting over 70,000 installations
- **OpenEMR Platform**: 38 security flaws discovered affecting healthcare providers using the electronic health record system
- **Roblox Gaming Platform**: Over 610,000 accounts hijacked and sold by Ukrainian threat actors
- **GitHub Repositories**: Millions of private repositories potentially accessible through RCE vulnerability
- **Web Hosting Infrastructure**: cPanel and WHM installations vulnerable to authentication bypass
- **LiteLLM Deployments**: Large language model gateway systems exposed to SQL injection attacks
- **Qinglong Installations**: Open-source task schedulers compromised for cryptomining
- **Windows Systems**: Federal and enterprise environments targeted through zero-day exploitation
- **ConnectWise ScreenConnect**: Remote access software installations under active attack

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious code injection into legitimate npm packages to steal developer credentials and authentication tokens
- **Authentication Bypass**: Exploitation of flaws in authentication mechanisms to gain unauthorized access to control panels and systems
- **SQL Injection**: Pre-authentication database attacks against LiteLLM implementations to extract sensitive information
- **Remote Code Execution**: Git push-based attacks against GitHub infrastructure and authenticated RCE exploitation
- **Backdoor Activation**: Long-dormant backdoors in WordPress plugins activated after years of remaining hidden
- **Zero-Day Exploitation**: Immediate targeting of unpatched Windows vulnerabilities before public disclosure
- **AI-Enhanced Attacks**: Use of artificial intelligence for automated malware insertion and attack scaling
- **Cryptomining Deployment**: Exploitation of RCE vulnerabilities to install cryptocurrency miners on compromised servers
- **Account Takeover**: Large-scale hijacking of gaming platform accounts for resale on underground markets

## Threat Actor Activities

- **TeamPCP Group**: Conducting sophisticated supply chain attacks targeting SAP-related npm packages and deploying Vect 2.0 ransomware
- **BlueNoroff (North Korean)**: Using fake Zoom calls, AI-generated avatars, and stolen victim videos to target cryptocurrency executives
- **DPRK-Affiliated Actors**: Deploying AI-inserted npm malware through fake companies and remote access trojans
- **Ukrainian Cybercriminals**: Arrested for hijacking over 610,000 Roblox accounts and selling them for $225,000 profit
- **Unknown Windows Exploiters**: Actively targeting federal systems with zero-day Windows vulnerabilities
- **Cryptomining Groups**: Rapidly exploiting Qinglong vulnerabilities to deploy miners on developer infrastructure
- **Ransomware Operators**: Multiple groups including 0APT and KryBit engaged in public feuds while continuing attack operations
- **Venezuelan Infrastructure Attackers**: Using Lotus Wiper malware with living-off-the-land techniques against energy firms and utilities