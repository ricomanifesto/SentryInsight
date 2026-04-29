# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems, with threat actors leveraging sophisticated attack vectors including social engineering, supply chain compromises, and privilege escalation vulnerabilities. Notable active exploits include a critical SQL injection vulnerability in LiteLLM (CVE-2026-42208), a remote code execution flaw in GitHub Enterprise Server (CVE-2026-3854), and a Windows Shell vulnerability (CVE-2026-32202) confirmed by Microsoft as being exploited in the wild. Additionally, an unpatched Hugging Face LeRobot vulnerability (CVE-2026-25874) poses significant remote code execution risks. Threat actors are also conducting sophisticated supply chain attacks through malicious VS Code extensions, targeting cryptocurrency executives with AI-enhanced social engineering, and exploiting cloud infrastructure for persistent access.

## Active Exploitation Details

### LiteLLM SQL Injection Vulnerability
- **Description**: A critical pre-authentication SQL injection flaw in the LiteLLM open-source large-language model gateway
- **Impact**: Attackers can access sensitive information stored in the LiteLLM gateway without authentication
- **Status**: Currently being actively exploited by hackers
- **CVE ID**: CVE-2026-42208

### GitHub Remote Code Execution Vulnerability
- **Description**: A critical security vulnerability in GitHub.com and GitHub Enterprise Server that allows authenticated users to obtain remote code execution
- **Impact**: Authenticated attackers can execute arbitrary code through a single Git push operation
- **Status**: Vulnerability disclosed, patch status not specified in articles
- **CVE ID**: CVE-2026-3854

### Windows Shell Vulnerability
- **Description**: A high-severity security flaw impacting Windows Shell components
- **Impact**: Enables unauthorized access and potential system compromise
- **Status**: Patched by Microsoft, but confirmed as actively exploited in the wild
- **CVE ID**: CVE-2026-32202

### Hugging Face LeRobot Remote Code Execution
- **Description**: A critical unpatched flaw in LeRobot, Hugging Face's open-source robotics platform with nearly 24,000 GitHub stars
- **Impact**: Could be exploited for unauthenticated remote code execution
- **Status**: Currently unpatched and vulnerable
- **CVE ID**: CVE-2026-25874

### PhantomRPC Windows Privilege Escalation
- **Description**: An architectural weakness in Windows Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Enables privilege escalation through five different exploit paths
- **Status**: Currently unpatched

## Affected Systems and Products

- **LiteLLM Gateway**: Open-source large-language model gateway systems
- **GitHub Enterprise Server**: Both GitHub.com and on-premises Enterprise Server installations
- **Windows Systems**: All Windows versions with Shell components, particularly affected by CVE-2026-32202
- **Hugging Face LeRobot**: Robotics platform installations
- **Visual Studio Code**: Development environments using OpenVSX extensions
- **Microsoft Teams**: Cloud collaboration platforms being abused for social engineering
- **AWS S3 Buckets**: Cloud storage services being leveraged for malware hosting
- **Minecraft Gaming Platforms**: Targeted by LofyStealer malware campaigns

## Attack Vectors and Techniques

- **SQL Injection**: Pre-authentication attacks against LiteLLM gateways to access sensitive data
- **Git Push Exploitation**: Single Git push operations triggering remote code execution in GitHub systems
- **Supply Chain Poisoning**: Malicious VS Code extensions distributed through OpenVSX marketplace with 73 "sleeper" extensions
- **Social Engineering**: Fake Zoom calls using AI-generated avatars and stolen victim videos
- **Cloud Infrastructure Abuse**: Leveraging AWS S3 buckets and Microsoft Teams for malware distribution and command and control
- **SMS Blasting**: Devices pretending to be cellular towers to send phishing texts to nearby phones
- **Account Creation Abuse**: Exploiting Robinhood's account creation process to inject phishing messages into legitimate emails

## Threat Actor Activities

- **BlueNoroff**: North Korean group targeting cryptocurrency executives using fake Zoom calls, AI-generated avatars, and stolen victim videos to scale malware attacks
- **LofyGang**: Brazilian cybercrime group resurging after three years with LofyStealer campaign targeting Minecraft players
- **Scattered Spider**: Prolific hacking group with members facing federal charges for extensive cybercriminal activities
- **LAPSUS$**: Threat group confirmed to have leaked stolen data from Checkmarx's private GitHub repository
- **UNC6692**: Newly discovered threat actor combining Microsoft Teams, AWS S3 buckets, and custom "Snow" malware in multipronged campaigns
- **Silk Typhoon**: Chinese state-sponsored group conducting cyberespionage operations, with members being extradited for prosecution
- **VECT 2.0 Ransomware Operators**: Cybercriminals deploying flawed ransomware that acts as a data wiper for files over 131KB across Windows, Linux, and ESXi systems
- **GlassWorm Campaign Operators**: Attackers scaling supply chain attacks through seemingly benign VS Code extensions that become malicious after updates