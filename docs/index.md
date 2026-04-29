# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitation targeting critical infrastructure components and development platforms. Attackers are leveraging multiple zero-day and recently patched vulnerabilities to achieve remote code execution, privilege escalation, and data theft. The most significant exploitation activity involves CVE-2026-42208 targeting LiteLLM open-source gateways, CVE-2026-32202 affecting Windows Shell components, and CVE-2026-3854 impacting GitHub platforms. Additionally, sophisticated social engineering campaigns and supply chain attacks through compromised VS Code extensions are being actively deployed by threat actors including BlueNoroff, UNC6692, and the resurgent LofyGang.

## Active Exploitation Details

### LiteLLM Pre-Authentication SQL Injection Vulnerability
- **Description**: Critical vulnerability in the LiteLLM open-source large-language model gateway allowing pre-authentication SQL injection attacks
- **Impact**: Attackers can access sensitive information stored in LiteLLM databases without authentication
- **Status**: Currently being actively exploited by hackers targeting LLM gateway deployments
- **CVE ID**: CVE-2026-42208

### Windows Shell Security Flaw
- **Description**: High-severity security vulnerability affecting Windows Shell components
- **Impact**: Enables attackers to exploit the Windows shell for malicious activities
- **Status**: Microsoft has confirmed active exploitation in the wild and released patches
- **CVE ID**: CVE-2026-32202

### GitHub Remote Code Execution Vulnerability
- **Description**: Critical security flaw impacting GitHub.com and GitHub Enterprise Server allowing authenticated users to achieve remote code execution
- **Impact**: Authenticated attackers can execute arbitrary code through a single Git push operation
- **Status**: Vulnerability disclosed by researchers, exploitation possible via single Git push
- **CVE ID**: CVE-2026-3854

### Hugging Face LeRobot Remote Code Execution
- **Description**: Critical unpatched vulnerability in Hugging Face's LeRobot open-source robotics platform
- **Impact**: Enables unauthenticated remote code execution on systems running LeRobot
- **Status**: Remains unpatched despite disclosure, affecting platform with nearly 24,000 GitHub stars
- **CVE ID**: CVE-2026-25874

### PhantomRPC Windows Privilege Escalation
- **Description**: Architectural weakness in Windows Remote Procedure Call (RPC) mechanism handling connections to unavailable services
- **Impact**: Multiple exploit paths enable privilege escalation attacks
- **Status**: Currently unpatched with five different exploit paths identified

## Affected Systems and Products

- **LiteLLM Gateway**: Open-source large-language model gateway systems vulnerable to SQL injection
- **Windows Operating Systems**: Shell components affected by actively exploited vulnerability
- **GitHub Platforms**: Both GitHub.com and GitHub Enterprise Server susceptible to RCE attacks
- **Hugging Face LeRobot**: Open-source robotics platform with unpatched critical vulnerability
- **Visual Studio Code Extensions**: OpenVSX marketplace compromised with 73 malicious "sleeper" extensions
- **Microsoft Entra ID**: Administrative roles for AI agents vulnerable to privilege escalation
- **Robinhood Platform**: Account creation process exploited for phishing email injection
- **Windows RPC Services**: Remote Procedure Call mechanism vulnerable to privilege escalation

## Attack Vectors and Techniques

- **SQL Injection**: Pre-authentication attacks against LiteLLM gateways to access sensitive data
- **Remote Code Execution**: Single Git push exploitation of GitHub platforms and unauthenticated RCE against robotics platforms
- **Supply Chain Poisoning**: Malicious VS Code extensions deployed as "sleeper" agents in OpenVSX marketplace
- **Social Engineering**: Fake Zoom calls with AI-generated avatars and stolen victim videos
- **Privilege Escalation**: Multiple exploitation paths through Windows RPC architectural weaknesses
- **Phishing Email Injection**: Abuse of legitimate platform account creation processes
- **Identity Takeover**: Exploitation of administrative roles in cloud identity management systems

## Threat Actor Activities

- **BlueNoroff**: North Korean group conducting sophisticated social engineering campaigns using fake Zoom calls, AI-generated avatars, and stolen victim videos to target cryptocurrency executives
- **UNC6692**: Newly discovered threat actor combining Microsoft Teams abuse, AWS S3 bucket exploitation, and custom "Snow" malware in multipronged campaigns
- **LofyGang**: Brazilian cybercrime group resurging after three years with Minecraft-targeted LofyStealer campaign
- **GlassWorm Operators**: Scaling supply chain attacks through 73 compromised VS Code extensions in OpenVSX marketplace
- **Scattered Spider**: Prolific hacking group with arrested member facing federal charges for extensive cybercriminal activities
- **LAPSUS$ Group**: Confirmed data leak of stolen information from Checkmarx's private GitHub repository
- **Silk Typhoon**: Chinese state-sponsored group with member extradited to US for COVID research facility cyberattacks
- **VECT 2.0 Operators**: Ransomware group with flawed encryption implementation causing permanent data destruction rather than recovery