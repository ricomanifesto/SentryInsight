# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with attackers targeting everything from AI development platforms to enterprise GitHub repositories. The most concerning activities include active exploitation of LiteLLM's pre-authentication SQL injection vulnerability (CVE-2026-42208), GitHub's remote code execution flaw (CVE-2026-3854), and Microsoft Windows Shell vulnerability (CVE-2026-32202). Additionally, threat actors are leveraging supply chain attacks through malicious VS Code extensions, PyPI packages, and sophisticated social engineering campaigns. Ransomware operations continue to evolve with destructive capabilities, while established threat groups like LAPSUS$ and Scattered Spider maintain persistent criminal operations.

## Active Exploitation Details

### LiteLLM Pre-Authentication SQL Injection
- **Description**: Critical vulnerability in the LiteLLM open-source large-language model gateway allowing pre-authentication SQL injection attacks
- **Impact**: Attackers can access sensitive information stored in LiteLLM databases without authentication
- **Status**: Currently being actively exploited by threat actors
- **CVE ID**: CVE-2026-42208

### GitHub Remote Code Execution Vulnerability
- **Description**: Critical security flaw affecting GitHub.com and GitHub Enterprise Server that enables remote code execution through authenticated access
- **Impact**: Authenticated users can achieve remote code execution via a single Git push operation
- **Status**: Vulnerability disclosed with proof-of-concept available
- **CVE ID**: CVE-2026-3854

### Microsoft Windows Shell Vulnerability
- **Description**: High-severity security flaw in Windows Shell component
- **Impact**: Enables unauthorized access and potential system compromise
- **Status**: Actively exploited in the wild, patch available from Microsoft
- **CVE ID**: CVE-2026-32202

### Hugging Face LeRobot Unauthenticated RCE
- **Description**: Critical unpatched vulnerability in Hugging Face's LeRobot open-source robotics platform
- **Impact**: Allows unauthenticated remote code execution on affected systems
- **Status**: Vulnerability disclosed, remains unpatched
- **CVE ID**: CVE-2026-25874

## Affected Systems and Products

- **LiteLLM Gateway**: Open-source large-language model gateway systems
- **GitHub Enterprise**: GitHub.com and GitHub Enterprise Server installations
- **Microsoft Windows**: Windows Shell components across multiple versions
- **Hugging Face LeRobot**: Open-source robotics platform with nearly 24,000 GitHub stars
- **Visual Studio Code**: Extensions ecosystem through OpenVSX marketplace
- **Python PyPI**: Elementary-data package with 1.1 million monthly downloads
- **Microsoft Entra ID**: Administrative roles for AI agents and service principals
- **Robinhood Trading Platform**: Account creation and email notification systems

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious VS Code extensions distributed through OpenVSX marketplace with "sleeper" functionality
- **Package Repository Compromise**: Hijacking of popular PyPI packages to distribute infostealers targeting developer credentials
- **Social Engineering**: Multi-pronged campaigns combining Microsoft Teams, AWS S3 buckets, and custom malware
- **SMS Blaster Attacks**: Physical "SMS blaster" devices impersonating cellular towers to distribute phishing messages
- **Account Creation Abuse**: Exploiting legitimate platform registration processes to inject phishing content
- **Git-based Exploitation**: Single Git push operations to trigger remote code execution
- **Pre-Authentication Attacks**: SQL injection attacks bypassing authentication mechanisms

## Threat Actor Activities

- **LAPSUS$ Group**: Successfully breached Checkmarx's private GitHub repository and leaked stolen data on dark web platforms
- **Scattered Spider**: Continued operations with arrests of key members, including a 19-year-old dual US-Estonian citizen
- **LofyGang**: Brazilian cybercrime group resurged after three years with Minecraft-targeted LofyStealer campaign
- **Silk Typhoon**: Chinese state-sponsored group member extradited to US for COVID research facility cyberattacks
- **UNC6692**: Newly discovered threat actor combining social engineering, custom "Snow" malware, and cloud service abuse
- **GlassWorm Operators**: Continued supply chain attacks through 73 malicious OpenVSX extensions with self-propagating capabilities
- **VECT 2.0 Ransomware**: Cybercriminal operation deploying flawed ransomware that acts as destructive wiper for files over 131KB