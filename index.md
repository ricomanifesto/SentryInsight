# Exploitation Report

Critical security vulnerabilities across multiple platforms are experiencing active exploitation in the wild, with attackers rapidly weaponizing newly disclosed flaws. CVE-2026-42208, a critical SQL injection vulnerability in LiteLLM, was exploited within 36 hours of public disclosure, demonstrating the increasingly compressed timeline between vulnerability disclosure and active exploitation. Windows systems face ongoing threats from CVE-2026-32202, a Windows Shell vulnerability being actively exploited as a zero-day, while GitHub's infrastructure was compromised through CVE-2026-3854, a remote code execution flaw that potentially exposed millions of private repositories. Additional critical vulnerabilities remain unpatched, including an unauthenticated RCE flaw in Hugging Face's LeRobot platform and authentication bypass vulnerabilities in cPanel systems.

## Active Exploitation Details

### GitHub Remote Code Execution Vulnerability
- **Description**: A critical remote code execution vulnerability in GitHub.com and GitHub Enterprise Server that allows authenticated users to obtain remote code execution privileges through a single Git push operation
- **Impact**: Attackers could gain unauthorized access to millions of private repositories and execute arbitrary code on GitHub's infrastructure
- **Status**: Patched in early March 2026, but was exploitable prior to remediation
- **CVE ID**: CVE-2026-3854

### Windows Shell Vulnerability
- **Description**: A high-severity security flaw affecting Windows Shell components that has been confirmed as actively exploited in zero-day attacks
- **Impact**: Successful exploitation allows attackers to execute unauthorized code and potentially gain system-level access
- **Status**: Patched by Microsoft, but exploitation confirmed in the wild before patch deployment
- **CVE ID**: CVE-2026-32202

### LiteLLM SQL Injection Vulnerability
- **Description**: A critical pre-authentication SQL injection vulnerability in BerriAI's LiteLLM Python package affecting the open-source large language model gateway
- **Impact**: Attackers can extract sensitive information stored in LiteLLM databases without authentication
- **Status**: Actively exploited within 36 hours of public disclosure
- **CVE ID**: CVE-2026-42208

### ConnectWise ScreenConnect Vulnerabilities
- **Description**: Security flaws in ConnectWise ScreenConnect remote access software that enable unauthorized system access
- **Impact**: Remote attackers can gain control of systems running vulnerable ScreenConnect instances
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation

### cPanel Authentication Vulnerability
- **Description**: A critical authentication bypass vulnerability affecting various authentication paths in cPanel control panel software
- **Impact**: Attackers can gain unauthorized access to cPanel control panels, compromising web hosting environments
- **Status**: Security updates released, immediate patching required

### Hugging Face LeRobot Unauthenticated RCE
- **Description**: A critical security flaw in Hugging Face's LeRobot open-source robotics platform with nearly 24,000 GitHub stars
- **Impact**: Unauthenticated remote code execution allowing complete system compromise
- **Status**: Currently unpatched and vulnerable to exploitation

## Affected Systems and Products

- **GitHub.com and GitHub Enterprise Server**: All versions prior to March 2026 security update affected by RCE vulnerability
- **Microsoft Windows Systems**: Windows Shell components across multiple Windows versions vulnerable to zero-day exploitation
- **LiteLLM Python Package**: BerriAI's open-source large language model gateway package vulnerable to SQL injection
- **ConnectWise ScreenConnect**: Remote access software installations vulnerable to unauthorized access
- **cPanel Control Panel**: Web hosting control panel software affected by authentication bypass
- **Hugging Face LeRobot**: Open-source robotics platform with unpatched RCE vulnerability
- **Windows and Linux Systems**: VECT 2.0 ransomware targeting both platforms, also affecting ESXi environments

## Attack Vectors and Techniques

- **Single Git Push Exploitation**: Attackers can exploit GitHub RCE vulnerability through specially crafted Git push operations
- **Pre-Authentication SQL Injection**: LiteLLM vulnerability allows database compromise without requiring authentication credentials
- **Zero-Day Windows Exploitation**: Active exploitation of Windows Shell vulnerability before patches were available
- **Authentication Path Bypass**: cPanel vulnerability exploits weaknesses in multiple authentication mechanisms
- **Supply Chain Attacks**: GlassWorm campaign distributing malicious VS Code extensions through Open VSX registry
- **Social Engineering**: BlueNoroff using fake Zoom calls and AI-generated avatars to target cryptocurrency executives
- **Ransomware Data Destruction**: VECT 2.0 ransomware acting as data wiper for files larger than 131KB due to encryption implementation flaws

## Threat Actor Activities

- **BlueNoroff (North Korean Group)**: Conducting sophisticated social engineering campaigns using stolen victim videos, AI-generated avatars, and fake Zoom calls to target cryptocurrency executives and scale malware distribution
- **LAPSUS$ Threat Group**: Successfully compromised Checkmarx's private GitHub repository and leaked stolen data, demonstrating continued activity against security companies
- **LofyGang (Brazilian Origin)**: Resurfaced after three-year hiatus with LofyStealer campaign targeting Minecraft players through new stealer malware (GrabBot)
- **Scattered Spider**: Prolific hacking group with 19-year-old member facing federal charges in the U.S. following arrest in Finland
- **GlassWorm Campaign**: Attackers scaling supply chain attacks through malicious VS Code extensions distributed via Open VSX registry
- **Chinese Silk Typhoon**: Member extradited to U.S. over cyberattacks targeting COVID-19 research institutions
- **VECT 2.0 Operators**: Cybercriminal operation deploying flawed ransomware that irreversibly destroys files across Windows, Linux, and ESXi systems