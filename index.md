# Exploitation Report

The current threat landscape reveals multiple critical vulnerabilities under active exploitation, with threat actors demonstrating unprecedented speed in weaponizing newly disclosed flaws. Most notably, a critical SQL injection vulnerability in LiteLLM has been exploited within just 36 hours of its public disclosure, highlighting the shrinking window between vulnerability disclosure and active exploitation. Additionally, CISA has added ConnectWise ScreenConnect and Windows vulnerabilities to its Known Exploited Vulnerabilities catalog, indicating ongoing widespread exploitation in the wild. The exploitation activity spans various platforms including Windows systems, GitHub infrastructure, cloud services, and development tools, with attackers leveraging both traditional attack vectors and sophisticated social engineering campaigns.

## Active Exploitation Details

### LiteLLM SQL Injection Vulnerability
- **Description**: A critical pre-authentication SQL injection flaw in BerriAI's LiteLLM Python package that allows unauthorized access to sensitive information stored in the large-language model gateway
- **Impact**: Attackers can extract sensitive data and potentially gain unauthorized access to LLM gateway infrastructure
- **Status**: Actively exploited within 36 hours of disclosure, demonstrating rapid threat actor response
- **CVE ID**: CVE-2026-42208

### ConnectWise ScreenConnect Vulnerability
- **Description**: Security flaw in ConnectWise ScreenConnect remote access software that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Potential unauthorized remote access to systems and networks
- **Status**: Actively exploited in the wild, CISA has mandated federal agencies to patch by specific deadline

### Windows Shell Vulnerability
- **Description**: High-severity security flaw impacting Windows Shell component that Microsoft has confirmed is being actively exploited
- **Impact**: Potential system compromise and unauthorized access to Windows systems
- **Status**: Actively exploited in the wild, Microsoft has issued patches
- **CVE ID**: CVE-2026-32202

### GitHub Remote Code Execution Flaw
- **Description**: Critical security vulnerability in GitHub.com and GitHub Enterprise Server that allows authenticated users to obtain remote code execution through a single Git push operation
- **Impact**: Complete compromise of GitHub infrastructure and potential access to source code repositories
- **Status**: Disclosed by researchers, patch status requires verification
- **CVE ID**: CVE-2026-3854

### Hugging Face LeRobot RCE Vulnerability
- **Description**: Critical unpatched security flaw in Hugging Face's LeRobot open-source robotics platform affecting nearly 24,000 GitHub stars
- **Impact**: Unauthenticated remote code execution on robotics platforms and infrastructure
- **Status**: Currently unpatched and vulnerable to exploitation

## Affected Systems and Products

- **LiteLLM Python Package**: Open-source large-language model gateway vulnerable to SQL injection attacks
- **ConnectWise ScreenConnect**: Remote access software with actively exploited vulnerabilities
- **Microsoft Windows**: Windows Shell component affected by high-severity exploitation
- **GitHub Platform**: Both GitHub.com and GitHub Enterprise Server vulnerable to RCE attacks
- **Hugging Face LeRobot**: Open-source robotics platform with critical unpatched RCE flaw
- **Visual Studio Code Extensions**: OpenVSX ecosystem targeted by 73 malicious "sleeper" extensions
- **Microsoft Teams**: Platform abused for social engineering and malware distribution
- **Robinhood Platform**: Account creation process exploited for phishing email injection

## Attack Vectors and Techniques

- **Rapid Exploitation**: Threat actors weaponizing vulnerabilities within 36 hours of public disclosure
- **Supply Chain Attacks**: Malicious Visual Studio Code extensions in OpenVSX ecosystem acting as "sleeper" agents
- **Social Engineering**: Fake Zoom calls using AI-generated avatars and stolen victim videos
- **Phishing Campaigns**: Exploitation of legitimate platforms like Robinhood for phishing email distribution
- **Cloud Infrastructure Abuse**: Use of AWS S3 buckets and Microsoft Teams for malware distribution
- **SMS Blaster Attacks**: Physical devices mimicking cellular towers to send phishing messages
- **Git-based Attacks**: Single Git push operations leading to remote code execution on GitHub platforms

## Threat Actor Activities

- **BlueNoroff Group**: North Korean threat actors using fake Zoom calls with AI-generated avatars to target cryptocurrency executives, converting victims into attack lures
- **LofyGang**: Brazilian cybercrime group resurging after three-year hiatus with new LofyStealer campaign targeting Minecraft players
- **UNC6692**: Newly discovered threat actor combining social engineering, custom "Snow" malware, and cloud infrastructure abuse in multipronged campaigns
- **Scattered Spider**: Member arrested in Finland facing federal charges for prolific hacking activities
- **LAPSUS$ Group**: Confirmed leak of stolen data from application security company Checkmarx's private GitHub repository
- **Silk Typhoon**: Chinese hacking group member extradited to U.S. for cyberattacks targeting COVID research facilities
- **GlassWorm Campaign**: Continued supply chain attacks through malicious VS Code extensions with self-propagating capabilities
- **VECT 2.0 Operators**: Ransomware group with flawed encryption implementation causing permanent data destruction rather than encryption
- **Vidar Operators**: Information stealer malware rising to dominance in the chaotic infostealer market following law enforcement takedowns