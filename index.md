# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value platforms and systems. GitHub's infrastructure faced a severe remote code execution vulnerability (CVE-2026-3854) that could have compromised millions of private repositories through a simple Git push operation. Meanwhile, threat actors are rapidly exploiting a newly disclosed SQL injection flaw in LiteLLM (CVE-2026-42208) within just 36 hours of disclosure. CISA has mandated federal agencies patch actively exploited vulnerabilities in Windows Shell (CVE-2026-32202) and ConnectWise ScreenConnect systems. Additionally, critical authentication bypass vulnerabilities in cPanel and an unpatched remote code execution flaw in Hugging Face's LeRobot platform pose immediate risks to web hosting infrastructure and AI development environments.

## Active Exploitation Details

### GitHub Remote Code Execution Vulnerability
- **Description**: Critical remote code execution vulnerability in GitHub.com and GitHub Enterprise Server that allows authenticated users to execute arbitrary code on the platform
- **Impact**: Attackers could gain access to millions of private repositories and execute remote code through a single Git push operation
- **Status**: Patched in early March 2026
- **CVE ID**: CVE-2026-3854

### LiteLLM SQL Injection Vulnerability
- **Description**: Critical pre-authentication SQL injection vulnerability in BerriAI's LiteLLM Python package, an open-source large language model gateway
- **Impact**: Allows attackers to access sensitive information stored in LiteLLM databases without authentication
- **Status**: Actively exploited within 36 hours of disclosure
- **CVE ID**: CVE-2026-42208

### Windows Shell Vulnerability
- **Description**: High-severity security flaw in Windows Shell component that enables privilege escalation
- **Impact**: Attackers can escalate privileges on compromised Windows systems
- **Status**: Actively exploited in the wild, patches available
- **CVE ID**: CVE-2026-32202

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw affecting ConnectWise ScreenConnect remote access software
- **Impact**: Enables unauthorized access to remote management capabilities
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, actively exploited

### Critical cPanel Authentication Bypass
- **Description**: Authentication vulnerability affecting multiple authentication paths in cPanel control panel software
- **Impact**: Allows attackers to gain unauthorized access to web hosting control panels
- **Status**: Security updates released, immediate patching required

### Hugging Face LeRobot Remote Code Execution
- **Description**: Critical unpatched vulnerability in Hugging Face's LeRobot open-source robotics platform
- **Impact**: Enables unauthenticated remote code execution on robotics systems
- **Status**: Currently unpatched, affects platform with nearly 24,000 GitHub stars
- **CVE ID**: CVE-2026-25874

## Affected Systems and Products

- **GitHub Platform**: GitHub.com and GitHub Enterprise Server installations
- **LiteLLM Gateway**: BerriAI's LiteLLM Python package for large language model management
- **Windows Systems**: Microsoft Windows installations with vulnerable Shell components
- **ConnectWise ScreenConnect**: Remote access and support software deployments
- **cPanel Hosting**: Web hosting control panel installations across various authentication paths
- **Hugging Face LeRobot**: Open-source robotics platform and development environments
- **Microsoft Entra ID**: Azure Active Directory service principal configurations

## Attack Vectors and Techniques

- **Git Push Exploitation**: Single Git push operation to trigger remote code execution on GitHub infrastructure
- **Pre-Authentication SQL Injection**: Direct database access without requiring authentication credentials
- **Authentication Bypass**: Circumventing multiple authentication mechanisms in web control panels
- **Privilege Escalation**: Exploiting Windows Shell vulnerabilities to gain elevated system access
- **Supply Chain Attacks**: Malicious VS Code extensions distributed through Open VSX marketplace
- **Social Engineering**: Fake Zoom calls and AI-generated avatars for cryptocurrency targeting

## Threat Actor Activities

- **BlueNoroff Group**: North Korean cybercriminal group using stolen victim videos and AI-generated avatars in fake Zoom calls to target cryptocurrency executives
- **LofyGang**: Brazilian cybercrime group resurging after three years with LofyStealer malware targeting Minecraft players
- **Scattered Spider**: Notorious hacking group with arrested member facing federal charges for prolific cybercriminal activities
- **LAPSUS$ Group**: Data extortion group that leaked stolen data from Checkmarx's private GitHub repositories
- **Silk Typhoon**: Chinese state-sponsored group with member extradited to U.S. for COVID research cyberattacks
- **VECT 2.0 Operators**: Ransomware group deploying flawed encryption that permanently destroys files over 131KB
- **GlassWorm Campaign**: Supply chain attackers distributing malicious VS Code extensions through seemingly benign packages