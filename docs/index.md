# Exploitation Report

Current threat activity reveals a complex landscape of active exploitation targeting both known and emerging vulnerabilities. Critical exploitation is occurring against LiteLLM gateways through a pre-authentication SQL injection flaw, while GitHub platforms face remote code execution attacks through a single git push vulnerability. Windows environments are under active attack through a high-severity shell vulnerability that Microsoft has confirmed is being exploited in the wild. Additionally, supply chain attacks continue to evolve with malicious VS Code extensions infiltrating developer environments, and sophisticated social engineering campaigns are leveraging AI technology and cloud services to scale attacks against high-value targets in the cryptocurrency sector.

## Active Exploitation Details

### LiteLLM Pre-Authentication SQL Injection
- **Description**: A critical vulnerability affecting the LiteLLM open-source large-language model gateway that allows pre-authentication SQL injection attacks
- **Impact**: Attackers can target and extract sensitive information stored in LiteLLM systems without requiring authentication
- **Status**: Currently being actively exploited by hackers in the wild
- **CVE ID**: CVE-2026-42208

### GitHub Remote Code Execution Flaw
- **Description**: A critical security vulnerability affecting GitHub.com and GitHub Enterprise Server that enables remote code execution through a single git push operation
- **Impact**: Authenticated users can achieve remote code execution on GitHub systems, potentially compromising source code repositories and development infrastructure
- **Status**: Critical vulnerability discovered by researchers, exploitation possible via single git push
- **CVE ID**: CVE-2026-3854

### Windows Shell Vulnerability
- **Description**: A high-severity security flaw in Windows Shell that has been confirmed as actively exploited
- **Impact**: Enables attackers to exploit Windows shell functionality for unauthorized access and potential privilege escalation
- **Status**: Microsoft has confirmed active exploitation in the wild and issued patches
- **CVE ID**: CVE-2026-32202

### Hugging Face LeRobot Unauthenticated RCE
- **Description**: A critical unpatched security flaw in LeRobot, Hugging Face's open-source robotics platform with nearly 24,000 GitHub stars
- **Impact**: Allows unauthenticated remote code execution against robotics platforms, potentially compromising AI and robotics systems
- **Status**: Critical vulnerability disclosed but remains unpatched
- **CVE ID**: CVE-2026-25874

### Windows PhantomRPC Privilege Escalation
- **Description**: An architectural weakness in Windows' Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Enables privilege escalation through five different exploit paths discovered by researchers
- **Status**: Currently unpatched with multiple exploitation vectors identified

## Affected Systems and Products

- **LiteLLM Gateway**: Open-source large-language model gateway systems vulnerable to pre-auth SQL injection
- **GitHub Platforms**: GitHub.com and GitHub Enterprise Server affected by RCE vulnerability
- **Windows Systems**: Multiple Windows versions affected by shell vulnerability and PhantomRPC flaw
- **Hugging Face LeRobot**: Open-source robotics platform with nearly 24,000 GitHub stars
- **Visual Studio Code**: OpenVSX ecosystem targeted by malicious extensions
- **Microsoft Entra ID**: Administrative roles for AI agents vulnerable to privilege escalation
- **Robinhood Platform**: Account creation process exploited for phishing campaigns
- **Vimeo Services**: Customer data exposed through Anodot breach

## Attack Vectors and Techniques

- **SQL Injection**: Pre-authentication attacks against LiteLLM gateways to extract sensitive data
- **Git Repository Exploitation**: Single git push operations triggering remote code execution on GitHub
- **Supply Chain Infiltration**: Malicious VS Code extensions deployed as "sleeper" packages that activate after updates
- **Social Engineering with AI**: Fake Zoom calls using stolen victim videos and AI-generated avatars
- **Cloud Service Abuse**: Exploitation of AWS S3 buckets and Microsoft Teams for malware distribution
- **SMS Blaster Attacks**: Device-based attacks impersonating cellular towers to send phishing messages
- **Privilege Escalation**: Multiple RPC-based exploitation paths in Windows environments
- **Account Creation Abuse**: Injection of phishing content through legitimate platform registration processes

## Threat Actor Activities

- **BlueNoroff (North Korean)**: Conducting sophisticated social engineering campaigns using fake Zoom calls, stolen victim videos, and AI-generated avatars to target cryptocurrency executives and scale malware attacks
- **VECT 2.0 Operators**: Deploying ransomware that acts more like a wiper due to encryption implementation flaws, irreversibly destroying files over 131KB across Windows, Linux, and ESXi systems
- **LofyGang (Brazilian)**: Resurfaced after three years with new LofyStealer campaign targeting Minecraft players using custom malware also known as GrabBot
- **GlassWorm Campaign**: Ongoing supply chain attacks seeding OpenVSX with 73 "sleeper" VS Code extensions that appear benign but turn malicious after updates
- **UNC6692**: Newly discovered threat actor combining social engineering, custom "Snow" malware, and cloud abuse through Microsoft Teams and AWS S3 buckets
- **LAPSUS$**: Confirmed data leak of stolen information from Checkmarx's private GitHub repository
- **Scattered Spider**: 19-year-old dual US-Estonian citizen arrested in Finland facing federal charges for prolific hacking activities
- **Silk Typhoon (Chinese)**: Member extradited to US for cyberespionage operations targeting COVID research and other sensitive information
- **0APT and KryBit**: Feuding ransomware groups that attacked each other, exposing infrastructure and operational data that provides defenders with rare insights into ransomware operations
- **Vidar Operators**: Infostealer malware rising to market dominance, filling gaps created by law enforcement takedowns of Lumma and Rhadamanthys