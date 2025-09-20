# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across various sectors. The most severe threats include a maximum severity command injection vulnerability in Fortra GoAnywhere MFT (CVE-2025-10035) that allows complete system compromise, active exploitation of Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428) with specialized malware deployment, and a zero-click vulnerability in OpenAI ChatGPT's Deep Research agent that enables Gmail data exfiltration. Iranian state-sponsored groups are conducting sophisticated campaigns against telecommunications and satellite companies, while widespread information stealer campaigns target macOS users through fake GitHub repositories. These threats demonstrate the evolving landscape of both traditional vulnerability exploitation and AI-powered attack methods.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that enables command injection attacks
- **Impact**: Allows attackers to execute arbitrary commands on vulnerable systems, potentially leading to complete system compromise
- **Status**: Critical patch released by Fortra; exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Authentication Bypass and SQL Injection
- **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile being actively exploited with specialized malware kits
- **Impact**: Enables unauthorized access and data extraction from mobile endpoint management systems
- **Status**: Actively exploited in the wild with CISA-documented malware deployment
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Zero-Click Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that allows data exfiltration through crafted emails
- **Impact**: Enables invisible theft of sensitive Gmail inbox data with no trace on enterprise systems
- **Status**: Actively exploitable with proof-of-concept attacks demonstrated

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Authentication and database systems compromised
- **OpenAI ChatGPT Deep Research Agent**: Email processing functionality exploitable
- **Apple macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories
- **SonicWall MySonicWall Service**: Firewall backup configuration data exposed
- **European Telecommunications Infrastructure**: 34 devices across 11 organizations compromised
- **Transport for London (TfL) Systems**: Attacked by Scattered Spider group members
- **Ukrainian Government and Critical Infrastructure**: Targeted by collaborative Russian APT operations

## Attack Vectors and Techniques

- **Social Engineering via LinkedIn**: UNC1549 uses fake job offers to deliver MINIBIKE malware to telecom employees
- **Fake GitHub Repositories**: Malicious macOS applications distributed as legitimate software to deploy Atomic Infostealer
- **Email-Based Zero-Click Attacks**: Crafted emails trigger automatic data exfiltration through ChatGPT Deep Research
- **Command Injection**: Direct exploitation of web application input validation flaws in file transfer systems
- **Malware-as-a-Service**: SystemBC powering REM Proxy network with 1,500 daily victims across 80 C2 servers
- **Phishing-as-a-Service (PhaaS)**: Lighthouse and Lucid platforms managing 17,500 domains targeting 316 brands
- **AI-Powered Malware**: MalTerminal using GPT-4 capabilities for dynamic ransomware and reverse shell creation

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Sophisticated espionage campaign against European telecommunications using LinkedIn lures and custom MINIBIKE malware
- **Gamaredon and Turla (Russian APTs)**: Collaborative operations deploying Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested for August 2024 Transport for London cyber attack
- **Unknown APT**: Exploitation of SonicWall MySonicWall service exposing firewall configurations of enterprise customers
- **Cybercriminal Groups**: Operating fake FBI crime reporting portals for credential harvesting and malicious activities
- **Information Stealer Operators**: Widespread macOS targeting campaign using LastPass-themed fake repositories