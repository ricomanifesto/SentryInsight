# Exploitation Report

Critical vulnerabilities are currently under active exploitation, with threat actors demonstrating unprecedented speed in weaponizing newly disclosed flaws. Most notably, CVE-2026-42208, a SQL injection vulnerability in LiteLLM, was exploited within just 36 hours of disclosure, highlighting the rapidly shrinking window between vulnerability publication and active exploitation. Additionally, CVE-2026-32202, a Windows Shell vulnerability, and CVE-2026-3854, a GitHub remote code execution flaw, represent significant security concerns across widely-used platforms. These incidents underscore the critical importance of rapid patch deployment and the evolving threat landscape where attackers are increasingly sophisticated in their exploitation techniques.

## Active Exploitation Details

### LiteLLM SQL Injection Vulnerability
- **Description**: Critical SQL injection vulnerability in BerriAI's LiteLLM Python package affecting the open-source large-language model gateway
- **Impact**: Allows attackers to access sensitive information stored in LiteLLM databases through pre-authentication SQL injection
- **Status**: Under active exploitation within 36 hours of disclosure
- **CVE ID**: CVE-2026-42208

### Windows Shell Vulnerability
- **Description**: High-severity security flaw impacting Windows Shell components
- **Impact**: Enables privilege escalation and potential system compromise
- **Status**: Microsoft confirms active exploitation in the wild, patch available
- **CVE ID**: CVE-2026-32202

### GitHub Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability affecting both GitHub.com and GitHub Enterprise Server
- **Impact**: Allows authenticated users to obtain remote code execution through a single Git push operation
- **Status**: Newly disclosed critical vulnerability
- **CVE ID**: CVE-2026-3854

### Hugging Face LeRobot Vulnerability
- **Description**: Critical unpatched flaw in Hugging Face's LeRobot open-source robotics platform
- **Impact**: Enables unauthenticated remote code execution on systems running LeRobot
- **Status**: Critical vulnerability remains unpatched
- **CVE ID**: CVE-2026-25874

## Affected Systems and Products

- **LiteLLM Python Package**: BerriAI's open-source large-language model gateway vulnerable to SQL injection attacks
- **Windows Shell**: Microsoft Windows systems affected by privilege escalation vulnerability
- **GitHub Platform**: Both GitHub.com and GitHub Enterprise Server susceptible to RCE through Git operations
- **Hugging Face LeRobot**: Open-source robotics platform with nearly 24,000 GitHub stars vulnerable to unauthenticated RCE
- **Microsoft Entra ID**: Administrative roles for AI agents vulnerable to privilege escalation and identity takeover
- **OpenVSX Ecosystem**: Visual Studio Code extension marketplace targeted by malicious "sleeper" extensions
- **Robinhood Platform**: Account creation process exploited for phishing email injection

## Attack Vectors and Techniques

- **Pre-Authentication SQL Injection**: Attackers exploiting LiteLLM vulnerability without requiring authentication
- **Git Push RCE**: Single Git push operations leveraged to achieve remote code execution on GitHub platforms
- **Social Engineering via Video Calls**: BlueNoroff using fake Zoom calls with stolen victim videos and AI-generated avatars
- **Supply Chain Attacks**: GlassWorm campaign deploying 73 malicious VS Code extensions that activate after updates
- **Phishing Email Injection**: Exploitation of account creation processes to embed malicious content in legitimate emails
- **SMS Blasting**: Use of fake cellular towers to send phishing texts to nearby mobile devices
- **Malware Distribution**: VECT 2.0 ransomware with flawed encryption acting as a data wiper for files over 131KB

## Threat Actor Activities

- **BlueNoroff (North Korean)**: Conducting sophisticated social engineering campaigns using fake video calls to target cryptocurrency executives, employing stolen victim videos and AI-generated avatars to scale malware distribution
- **LofyGang (Brazilian)**: Resurfaced after three-year hiatus with LofyStealer campaign targeting Minecraft players
- **Scattered Spider**: 19-year-old member arrested in Finland facing federal charges in the US for prolific hacking activities
- **LAPSUS$**: Confirmed leak of stolen data from Checkmarx's private GitHub repository
- **Silk Typhoon (Chinese)**: Member Xu Zewei extradited to US for cyberespionage operations targeting COVID research facilities
- **UNC6692**: Newly discovered threat actor combining Microsoft Teams, AWS S3 buckets, and custom "Snow" malware in multipronged campaigns
- **GlassWorm Campaign**: Continued scaling of supply chain attacks through seemingly benign VS Code extensions
- **Feuding Ransomware Groups**: 0APT and KryBit attacking each other, exposing infrastructure and operational data