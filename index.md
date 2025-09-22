# Exploitation Report

The current threat landscape reveals several critical vulnerabilities under active exploitation, with attackers increasingly targeting enterprise systems and leveraging sophisticated social engineering techniques. Most concerning are the maximum severity vulnerabilities in Fortra GoAnywhere MFT systems (CVE-2025-10035) and Ivanti Endpoint Manager Mobile platforms (CVE-2025-4427, CVE-2025-4428), both allowing command injection and system compromise. Nation-state actors, particularly from North Korea and Iran, continue to demonstrate advanced persistent threat capabilities through targeted campaigns against telecommunications and cryptocurrency sectors. Additionally, a previously unknown zero-click vulnerability in OpenAI's ChatGPT Deep Research agent poses significant data exfiltration risks to enterprise environments.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity flaw in GoAnywhere MFT's License Servlet that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise with ability to execute malicious code and potentially gain full administrative control
- **Status**: Critical patch released by Fortra, immediate patching required
- **CVE ID**: CVE-2025-10035

### Ivanti Endpoint Manager Mobile Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti EPMM systems being actively exploited by threat actors to deploy custom malware
- **Impact**: System compromise leading to deployment of sophisticated malware kits including backdoors and persistence mechanisms
- **Status**: Active exploitation observed with CISA releasing detailed malware analysis
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak Zero-Click ChatGPT Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that enables data exfiltration from Gmail inboxes through crafted email attacks
- **Impact**: Sensitive corporate email data can be stolen without user interaction, with exfiltration occurring through OpenAI's infrastructure leaving no enterprise traces
- **Status**: Publicly disclosed vulnerability affecting ChatGPT Deep Research functionality

### Microsoft Entra ID Tenant Hijacking Vulnerability
- **Description**: A critical combination of legacy components in Microsoft Entra ID that could allow complete takeover of any company's tenant
- **Impact**: Full administrative access to organizational identity systems, potentially affecting authentication and authorization for entire enterprises
- **Status**: Vulnerability has been fixed by Microsoft prior to public disclosure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management platforms across multiple versions
- **Microsoft Entra ID**: Identity and access management systems with legacy component configurations
- **OpenAI ChatGPT**: Deep Research agent functionality affecting enterprise users
- **Apple macOS**: Systems targeted through malicious GitHub repositories distributing Atomic Infostealer
- **Windows Systems**: Platforms affected by BeaverTail malware campaigns and GPT-4-powered MalTerminal threats

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of input validation flaws in enterprise software to execute arbitrary system commands
- **Zero-Click Email Attacks**: Sophisticated attacks requiring no user interaction to exfiltrate sensitive data through AI platform vulnerabilities
- **Social Engineering via Professional Networks**: LinkedIn job lures used to deliver MINIBIKE malware to telecommunications targets
- **Fake Repository Distribution**: Malicious GitHub repositories masquerading as legitimate software to distribute macOS infostealers
- **ClickFix-Style Lures**: Deceptive user interface elements used to trick victims into downloading and executing malware
- **Phishing-as-a-Service Infrastructure**: Large-scale operations using 17,500+ domains targeting 316 brands across 74 countries

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Successfully infiltrated 34 devices across 11 European telecommunications organizations using LinkedIn job lures and MINIBIKE malware
- **DPRK-linked Groups**: Leveraging ClickFix techniques to deliver BeaverTail malware through cryptocurrency job scam campaigns
- **Gamaredon and Turla Collaboration**: Russian state-sponsored groups working together to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen hackers linked to August 2024 Transport for London cyber attack, with two members arrested by UK authorities
- **SystemBC Operators**: Managing REM Proxy botnet with 1,500 daily VPS victims across 80 command and control servers
- **PhaaS Operators**: Running Lighthouse and Lucid services targeting global brands through sophisticated phishing infrastructure