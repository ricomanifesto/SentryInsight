# Exploitation Report

Several critical vulnerabilities are currently being exploited in the wild, with the most severe being a maximum severity command injection flaw in Fortra GoAnywhere MFT and active exploitation of Ivanti Endpoint Manager Mobile vulnerabilities. Iranian state-sponsored threat actors are conducting sophisticated attacks against telecommunications companies, while SystemBC malware operators maintain a large-scale proxy botnet compromising approximately 1,500 VPS systems daily. Additionally, threat actors have successfully breached SonicWall's cloud infrastructure, exposing firewall configuration backup files.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows command injection attacks through exploitation of the License Servlet component
- **Impact**: Attackers can execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Critical patch available; exploitation highly dependent on whether systems are exposed to the Internet
- **CVE ID**: CVE-2025-10035

### Ivanti Endpoint Manager Mobile (EPMM) Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti EPMM systems that are being actively exploited by threat actors deploying specialized malware
- **Impact**: Complete system compromise with deployment of custom malware strains for persistent access and data exfiltration
- **Status**: Active exploitation with CISA releasing detailed malware analysis
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ChatGPT ShadowLeak Attack
- **Description**: A novel attack technique that exploits OpenAI's ChatGPT infrastructure to invisibly exfiltrate company emails and sensitive data
- **Impact**: Complete data exfiltration through AI infrastructure, leaving no trace on enterprise systems
- **Status**: Active exploitation technique allowing invisible data theft through AI platforms

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management systems compromised with custom malware
- **OpenAI ChatGPT**: AI platform exploited for invisible data exfiltration through ShadowLeak technique
- **SonicWall MySonicWall**: Cloud backup service breached exposing firewall configuration files
- **VPS Systems**: Commercial virtual private servers infected by SystemBC malware for proxy operations
- **European Telecommunications Companies**: 11 organizations with 34 devices compromised by Iranian actors

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **Social Engineering**: LinkedIn job lures used by UNC1549 to target telecommunications employees
- **AI Infrastructure Abuse**: ShadowLeak technique leveraging ChatGPT for invisible data exfiltration
- **Malware Deployment**: Custom malware strains deployed on compromised Ivanti EPMM systems
- **Proxy Network Operations**: SystemBC malware converting infected VPS systems into proxy infrastructure
- **Cloud Service Breach**: Direct compromise of SonicWall's cloud backup infrastructure

## Threat Actor Activities

- **UNC1549 (Iranian State APT)**: Conducting highly sophisticated campaigns against European telecommunications companies using LinkedIn recruitment lures and MINIBIKE malware, successfully infiltrating 34 devices across 11 organizations
- **Gamaredon and Turla Collaboration**: Russian hacking groups working together to deploy Kazuar backdoor against Ukrainian entities in unprecedented collaboration
- **Scattered Spider**: Teen members arrested in UK for August 2024 Transport for London cyber attack, demonstrating continued activity of this prominent ransomware affiliate group
- **SystemBC Operators**: Maintaining large-scale proxy botnet with approximately 1,500 daily VPS victims across 80 command and control servers for REM Proxy network operations
- **Phishing-as-a-Service Groups**: Lighthouse and Lucid PhaaS operations targeting 316 brands across 74 countries with over 17,500 malicious domains