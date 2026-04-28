# Exploitation Report

Critical security incidents are unfolding across multiple fronts, with active exploitation targeting Windows systems, supply chain attacks through developer tools, and sophisticated threat actor campaigns. Microsoft has confirmed active exploitation of CVE-2026-32202, a high-severity Windows Shell vulnerability that has been weaponized in the wild. Simultaneously, the GlassWorm malware campaign has escalated with 73 malicious VS Code extensions deployed as "sleeper" agents in the OpenVSX ecosystem, while the elementary-data Python package with 1.1 million monthly downloads was compromised to distribute infostealers. Critical unpatched vulnerabilities continue to pose immediate threats, including CVE-2026-25874 affecting Hugging Face's LeRobot platform and the PhantomRPC architectural flaw in Windows RPC mechanisms that enables privilege escalation through five distinct attack paths.

## Active Exploitation Details

### Windows Shell Vulnerability
- **Description**: High-severity security flaw impacting Windows Shell that has been actively exploited in the wild
- **Impact**: Enables attackers to compromise Windows systems through Shell exploitation
- **Status**: Patched by Microsoft, but confirmed active exploitation ongoing
- **CVE ID**: CVE-2026-32202

### Hugging Face LeRobot Remote Code Execution
- **Description**: Critical security flaw in LeRobot, Hugging Face's open-source robotics platform with nearly 24,000 GitHub stars
- **Impact**: Allows unauthenticated remote code execution on affected systems
- **Status**: Currently unpatched, actively exploitable
- **CVE ID**: CVE-2026-25874

### PhantomRPC Windows Privilege Escalation
- **Description**: Architectural weakness in Windows Remote Procedure Call (RPC) mechanism handling connections to unavailable services
- **Impact**: Enables privilege escalation through five different exploit paths
- **Status**: Unpatched vulnerability with multiple attack vectors

### GlassWorm Supply Chain Attacks
- **Description**: Malicious VS Code extensions deployed as "sleeper" agents in the OpenVSX ecosystem
- **Impact**: Self-propagating malware distribution through developer tools and IDE extensions
- **Status**: Ongoing campaign with 73 malicious extensions identified

### PyPI Package Compromise
- **Description**: The elementary-data Python package with 1.1 million monthly downloads was compromised
- **Impact**: Infostealer malware targeting developer data and cryptocurrency wallets
- **Status**: Malicious version distributed through compromised package maintainer account

## Affected Systems and Products

- **Microsoft Windows**: Windows Shell components affected by CVE-2026-32202 and PhantomRPC RPC mechanism vulnerability
- **Hugging Face LeRobot**: Open-source robotics platform vulnerable to unauthenticated RCE
- **VS Code Extensions**: OpenVSX marketplace with 73 compromised extensions containing GlassWorm malware
- **Python PyPI**: elementary-data package affecting 1.1 million monthly downloads
- **Microsoft Entra ID**: AI agent administrative roles enabling privilege escalation and identity takeover
- **Robinhood Platform**: Account creation process vulnerable to phishing email injection
- **ADT Security Systems**: 5.5 million customer records compromised in data breach
- **Medtronic Medical Devices**: Corporate IT systems breached with potential access to 9 million records
- **Checkmarx**: Private GitHub repository data leaked by LAPSUS$ threat group

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious VS Code extensions deployed as legitimate tools that turn malicious after updates
- **Package Repository Compromise**: Direct takeover of popular Python packages to distribute malware
- **Social Engineering**: UNC6692 threat actor combining Microsoft Teams abuse with custom "Snow" malware
- **Email Injection**: Exploitation of account creation processes to send legitimate-appearing phishing emails
- **SMS Blasting**: Use of fake cellular tower devices to send phishing messages to nearby mobile devices
- **Privilege Escalation**: Multiple exploit paths through Windows RPC architectural weaknesses
- **Identity Takeover**: Exploitation of AI agent roles in Microsoft Entra ID for service principal compromise

## Threat Actor Activities

- **Scattered Spider**: 19-year-old dual US-Estonian citizen arrested in Finland facing federal charges for prolific hacking activities
- **LAPSUS$ Group**: Successfully breached Checkmarx systems and leaked stolen GitHub repository data on dark web
- **VECT 2.0 Operators**: Deploying destructive ransomware with critical encryption flaws affecting Windows, Linux, and ESXi systems
- **UNC6692**: Newly discovered threat actor using Microsoft Teams, AWS S3 buckets, and custom Snow malware in multipronged campaigns
- **Silk Typhoon**: Chinese national Xu Zewei extradited to US for COVID research cyberattacks and cyberespionage operations
- **ShinyHunters**: Extortion group responsible for ADT data breach affecting 5.5 million individuals
- **GlassWorm Campaign**: Sophisticated supply chain attackers targeting developer ecosystems through malicious extensions