# Exploitation Report

Critical vulnerability exploitation activity is currently centered around several high-impact vulnerabilities across enterprise systems and AI platforms. The most severe threat involves CVE-2025-10035, a maximum severity command injection vulnerability in Fortra GoAnywhere MFT's License Servlet that allows arbitrary command execution. Additionally, threat actors are actively exploiting CVE-2025-4427 and CVE-2025-4428 in Ivanti EPMM systems, with CISA confirming the deployment of sophisticated malware strains following successful exploitation. A concerning zero-click vulnerability dubbed "ShadowLeak" has been discovered in OpenAI's ChatGPT Deep Research agent, enabling Gmail data exfiltration through crafted emails without user interaction.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in GoAnywhere MFT's License Servlet component that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise through arbitrary command execution, potentially leading to data theft, system manipulation, and lateral movement within enterprise networks
- **Status**: Critical patch available from Fortra; exploitation highly dependent on internet exposure of affected systems
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities with Active Malware Deployment
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) being exploited to deploy sophisticated malware kits in targeted attacks
- **Impact**: Enterprise mobile device management system compromise, deployment of persistent malware, potential access to managed mobile devices and corporate data
- **Status**: Actively exploited with confirmed malware deployment; CISA has published detailed analysis of attack methods
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Zero-Click Vulnerability
- **Description**: A zero-click vulnerability in OpenAI ChatGPT's Deep Research agent that allows attackers to exfiltrate Gmail inbox data through specially crafted emails
- **Impact**: Silent data exfiltration from Gmail accounts without user interaction, potential corporate data theft through AI infrastructure abuse
- **Status**: Recently disclosed; exploitation leaves no trace on enterprise systems as data flows through OpenAI infrastructure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platforms actively targeted
- **OpenAI ChatGPT Deep Research Agent**: AI-powered research tool vulnerable to email-based exploitation
- **Gmail Integration Systems**: Email platforms accessible through ChatGPT integrations at risk of data exfiltration
- **macOS Systems**: Targeted by fake GitHub repositories distributing Atomic Infostealer malware
- **European Telecommunications Infrastructure**: 34 devices across 11 organizations compromised by UNC1549 operations

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of input validation flaws in web servlets to execute system commands
- **Malware Kit Deployment**: Post-exploitation installation of sophisticated malware suites for persistence and data collection
- **Zero-Click Email Exploitation**: Crafted emails triggering automatic data exfiltration through AI agent vulnerabilities
- **Social Engineering via LinkedIn**: Fake job postings used to deliver MINIBIKE malware to telecommunications targets
- **Fake Repository Attacks**: Malicious GitHub repositories distributing macOS malware disguised as legitimate software
- **AI-Powered Malware**: GPT-4 integrated malware (MalTerminal) capable of generating ransomware and reverse shells dynamically

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Targeting European telecommunications companies through LinkedIn job lures, successfully compromising 34 devices across 11 organizations using MINIBIKE malware
- **Gamaredon and Turla Collaboration**: Russian state-sponsored groups working together to deploy Kazuar backdoor in Ukrainian entities, representing unprecedented cooperation between APT groups
- **Scattered Spider Operations**: Teen hackers linked to August 2024 Transport for London cyber attack, with recent arrests in the UK
- **SystemBC Botnet Operators**: Managing REM Proxy network with approximately 1,500 daily VPS victims across 80 command-and-control servers
- **Lighthouse and Lucid PhaaS Operators**: Operating phishing-as-a-service platforms targeting 316 brands across 74 countries through 17,500 malicious domains
- **TradeOgre Exchange Operators**: Cryptocurrency exchange facilitating criminal activities, resulting in $40 million seizure by Canadian authorities