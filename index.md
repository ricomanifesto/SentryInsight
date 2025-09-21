# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise environments. The most severe threat involves a maximum severity command injection vulnerability in Fortra GoAnywhere MFT's License Servlet, which poses immediate risk to organizations using this managed file transfer solution. Additionally, active exploitation campaigns are leveraging previously disclosed vulnerabilities in Ivanti Endpoint Manager Mobile systems, with CISA documenting sophisticated malware deployment techniques. A new zero-click vulnerability affecting OpenAI ChatGPT's Deep Research agent demonstrates novel attack vectors that can exfiltrate sensitive Gmail data without user interaction, while advanced persistent threat groups continue targeting telecommunications infrastructure through sophisticated social engineering and malware campaigns.

## Active Exploitation Details

### GoAnywhere MFT License Servlet Command Injection
- **Description**: A maximum severity vulnerability in Fortra GoAnywhere MFT's License Servlet that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise through command injection attacks, potentially leading to data exfiltration, lateral movement, and persistent access
- **Status**: Critical patch available; exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Multiple Vulnerabilities
- **Description**: Previously disclosed vulnerabilities in Ivanti Endpoint Manager Mobile that are being actively exploited with sophisticated malware deployment
- **Impact**: Deployment of custom malware kits allowing persistent access and data exfiltration from mobile device management infrastructure
- **Status**: Active exploitation documented by CISA with detailed malware analysis
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ChatGPT Deep Research Agent Zero-Click Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that enables data exfiltration through crafted email interactions
- **Impact**: Unauthorized access to sensitive Gmail inbox data without user interaction, data exfiltration via OpenAI infrastructure
- **Status**: Newly disclosed vulnerability with proof-of-concept attacks demonstrated

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management systems targeted with custom malware kits
- **OpenAI ChatGPT Deep Research Agent**: AI-powered research tool vulnerable to zero-click data exfiltration
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories and malicious applications
- **Telecommunications Infrastructure**: European telecom companies compromised through LinkedIn-based social engineering
- **Windows Systems**: Affected by SystemBC malware powering REM Proxy botnet operations

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **Social Engineering via LinkedIn**: Job lure campaigns targeting telecommunications employees with MINIBIKE malware
- **Fake Repository Distribution**: Malicious macOS applications distributed through counterfeit GitHub repositories
- **Zero-Click Email Exploitation**: Crafted emails triggering automatic data exfiltration through AI research agents
- **Malware Kit Deployment**: Custom malware tools deployed following Ivanti EPMM exploitation
- **Proxy Botnet Operations**: SystemBC malware creating proxy networks with approximately 1,500 daily VPS victims

## Threat Actor Activities

- **UNC1549**: Iran-nexus cyber espionage group successfully infiltrating 34 devices across 11 European telecommunications organizations using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla Collaboration**: Russian hacking groups working together to deploy Kazuar backdoor against Ukrainian entities, demonstrating unprecedented cooperation between APT groups
- **Scattered Spider**: Teen hackers linked to August 2024 Transport for London cyber attack, with two members arrested by UK law enforcement
- **Atomic Infostealer Operators**: Cybercriminals distributing macOS-targeting malware through fake GitHub repositories masquerading as legitimate applications
- **SystemBC Operators**: Cybercriminal network managing REM Proxy botnet across approximately 80 command and control servers