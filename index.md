# Exploitation Report

Current cybersecurity threats demonstrate a concerning landscape of active exploitation targeting critical infrastructure, enterprise systems, and development environments. The most significant activity includes active exploitation of D-Link router vulnerabilities through Mirai botnets, critical privilege escalation flaws in ASP.NET Core requiring emergency patches, and sophisticated supply chain attacks compromising npm packages and Docker repositories. Ransomware operations continue to evolve with advanced encryption techniques, while nation-state actors deploy complex backdoors using legitimate Microsoft infrastructure for command and control operations.

## Active Exploitation Details

### D-Link Router Command Injection Vulnerability
- **Description**: High-severity command injection vulnerability affecting D-Link DIR-823X routers that are end-of-life
- **Impact**: Allows attackers to execute arbitrary commands and enlist devices into Mirai botnets for DDoS attacks
- **Status**: Actively exploited by Mirai-based malware campaigns; no patches available for EOL devices
- **CVE ID**: CVE-2025-29635

### ASP.NET Core Privilege Escalation Vulnerability
- **Description**: Critical privilege escalation flaw in ASP.NET Core framework requiring emergency out-of-band patches
- **Impact**: Enables attackers to escalate privileges within ASP.NET Core applications
- **Status**: Microsoft released emergency security updates to address active exploitation concerns
- **CVE ID**: CVE-2026-40372

### Bomgar RMM Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in Bomgar remote monitoring and management tool
- **Impact**: Allows exploitation to spread ransomware and compromise supply chains through RMM infrastructure
- **Status**: Experiencing surge in exploitation activity demonstrating supply chain risks
- **CVE ID**: CVE-2026-1731

### SharePoint Spoofing Vulnerability
- **Description**: Spoofing vulnerability in Microsoft SharePoint servers that was previously exploited as a zero-day
- **Impact**: Enables spoofing attacks against SharePoint infrastructure
- **Status**: Over 1,300 servers remain unpatched and vulnerable to ongoing attacks

### Cohere AI Terrarium Sandbox Escape
- **Description**: Critical vulnerability in Python-based Terrarium sandbox environment
- **Impact**: Results in arbitrary code execution with root privileges and container escape capabilities
- **Status**: Discovered and disclosed with potential for exploitation
- **CVE ID**: CVE-2026-5752

### Windows Defender Exploitation
- **Description**: Three proof-of-concept exploits targeting Microsoft's built-in security platform
- **Impact**: Turns Windows Defender into an attacker tool for malicious purposes
- **Status**: Being used in active attacks; two exploits remain unpatched

## Affected Systems and Products

- **D-Link DIR-823X Routers**: End-of-life devices vulnerable to command injection attacks
- **ASP.NET Core Applications**: All versions prior to emergency patch deployment
- **Bomgar RMM Tools**: Remote monitoring and management infrastructure
- **Microsoft SharePoint Servers**: Over 1,300 exposed servers remain unpatched
- **Cohere AI Terrarium**: Python-based sandbox environments
- **Windows Defender**: Microsoft's built-in security platform
- **Lantronix and Silex Serial-to-IP Converters**: Industrial IoT devices with 22 newly discovered vulnerabilities
- **npm Package Repository**: Node.js development environment supply chain
- **Docker Hub**: Container registry with malicious Checkmarx KICS images
- **iOS and iPad Devices**: Apple mobile platforms with notification data retention issues

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of D-Link routers through malformed input processing
- **Supply Chain Compromise**: Self-propagating worms targeting npm packages and Docker repositories
- **Privilege Escalation**: ASP.NET Core framework exploitation for elevated access
- **Living-off-the-Land**: Using legitimate Microsoft Graph API for backdoor communications
- **Social Engineering**: DPRK fake job campaigns with self-propagating interview processes
- **Remote Code Execution**: Exploitation of RMM tools for ransomware deployment
- **Container Escape**: Sandbox bypass techniques in AI development environments
- **Spoofing Attacks**: SharePoint server exploitation for authentication bypass

## Threat Actor Activities

- **Mirai Botnet Operators**: Actively exploiting D-Link router vulnerabilities to expand botnet infrastructure for DDoS attacks
- **The Gentlemen Ransomware Gang**: Rapidly scaling operations with over 1,570 victims identified through SystemBC C2 analysis
- **Kyber Ransomware Group**: Implementing post-quantum encryption techniques targeting Windows and VMware ESXi systems
- **Harvester APT**: Deploying Linux GoGra backdoors in South Asia using Microsoft Graph API for stealthy communications
- **Mustang Panda**: Distributing new LOTUSLITE variants targeting Indian banking sector and South Korean policy organizations
- **Scattered Spider Member**: Senior cybercrime group member pleading guilty to wire fraud and identity theft charges
- **npm Supply Chain Attackers**: Operating self-propagating worms to steal developer authentication tokens
- **DPRK-linked Groups**: Conducting sophisticated fake job scams with contagious interview techniques
- **Unknown Venezuelan Attackers**: Deploying Lotus wiper malware against energy and utility infrastructure