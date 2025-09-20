# Exploitation Report

The current threat landscape reveals several critical exploitation campaigns targeting high-value systems across multiple sectors. Most notably, threat actors are actively exploiting vulnerabilities in Fortra GoAnywhere MFT systems, with CVE-2025-10035 receiving a maximum severity score of 10.0 CVSS for command injection attacks. Iranian state-sponsored groups continue aggressive campaigns against telecommunications companies, while multiple malware families are leveraging AI capabilities for enhanced attacks. Additionally, CISA has identified active exploitation of Ivanti EPMM vulnerabilities with custom malware deployment, and a zero-click flaw in OpenAI's ChatGPT Deep Research agent poses significant data exfiltration risks.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise through command injection, enabling unauthorized access and control of managed file transfer systems
- **Status**: Critical patch available, active exploitation potential high for internet-exposed systems
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) systems being exploited with custom malware deployment
- **Impact**: Device compromise and persistent access through specialized malware kits designed for mobile endpoint management systems
- **Status**: Active exploitation confirmed by CISA with detailed malware analysis published
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak Zero-Click ChatGPT Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent allowing Gmail data exfiltration through crafted emails
- **Impact**: Sensitive email data can be leaked without user interaction, potentially exposing corporate communications and confidential information
- **Status**: Newly disclosed vulnerability with proof-of-concept demonstration, patch status unclear

### SonicWall MySonicWall Service Breach
- **Description**: Unauthorized access to SonicWall's MySonicWall service exposing firewall backup configuration files
- **Impact**: Exposure of network security configurations affecting fewer than 5% of the install base, potentially revealing network topology and security settings
- **Status**: Active breach disclosed by vendor, containment measures implemented

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks, particularly systems with internet exposure
- **Ivanti EPMM**: Mobile endpoint management systems compromised through targeted malware campaigns
- **OpenAI ChatGPT**: Deep Research agent functionality vulnerable to data exfiltration attacks
- **SonicWall Firewalls**: Backup configuration data exposed through MySonicWall service compromise
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories and malicious software packages
- **Telecommunications Infrastructure**: European telecom companies infiltrated across 34 devices in 11 organizations
- **Windows Systems**: Infected with AI-powered MalTerminal malware and SystemBC proxy network components

## Attack Vectors and Techniques

- **Social Engineering via LinkedIn**: Iran-linked UNC1549 group using fake job offers to target telecommunications employees
- **Fake Repository Distribution**: Malicious GitHub repositories distributing Atomic Infostealer to macOS users
- **Zero-Click Email Exploitation**: Crafted emails triggering automatic data exfiltration through ChatGPT Deep Research agent
- **Command Injection**: Direct system compromise through vulnerable web interfaces in file transfer systems
- **AI-Enhanced Malware**: GPT-4-powered MalTerminal creating dynamic ransomware and reverse shell capabilities
- **Proxy Network Infrastructure**: SystemBC malware powering REM Proxy with 1,500 daily victims across 80 command and control servers
- **Phishing-as-a-Service**: Lighthouse and Lucid platforms managing over 17,500 phishing domains targeting 316 brands globally

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Sophisticated espionage campaign targeting European telecommunications companies using MINIBIKE malware and LinkedIn social engineering, successfully compromising 34 devices across 11 organizations
- **Gamaredon and Turla**: Russian state-sponsored groups collaborating to deploy Kazuar backdoor against Ukrainian entities, demonstrating unprecedented cooperation between APT groups
- **Scattered Spider**: Teen hackers linked to August 2024 Transport for London cyber attack, with two members arrested in the UK
- **SystemBC Operators**: Managing extensive proxy network infrastructure with daily victim counts exceeding 1,500 systems
- **Atomic Infostealer Campaign**: Large-scale information theft operation targeting macOS users through fake software repositories
- **REM Proxy Network**: Criminal infrastructure leveraging SystemBC malware to provide proxy services to cybercriminals