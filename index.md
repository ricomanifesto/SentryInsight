# Exploitation Report

Multiple critical vulnerabilities are currently being exploited in active campaigns targeting enterprise systems and individual users. The most significant activity includes zero-day exploits affecting OpenAI's ChatGPT Deep Research agent, maximum severity command injection vulnerabilities in Fortra GoAnywhere MFT systems, and sophisticated malware campaigns leveraging AI capabilities. Notable threat activity includes Iranian state-sponsored groups targeting telecommunications infrastructure, Russian collaboration in Ukrainian attacks, and widespread phishing-as-a-service operations affecting global organizations.

## Active Exploitation Details

### ShadowLeak Zero-Click Flaw in OpenAI ChatGPT Deep Research Agent
- **Description**: A zero-click vulnerability that allows attackers to leak sensitive Gmail inbox data through OpenAI's ChatGPT Deep Research agent with a single crafted email
- **Impact**: Unauthorized access to Gmail data and potential corporate information exfiltration via OpenAI's infrastructure without leaving traces on enterprise systems
- **Status**: Actively exploitable, allowing invisible data theft operations

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: Maximum severity vulnerability in GoAnywhere MFT's License Servlet enabling command injection attacks
- **Impact**: Arbitrary command execution on affected systems, potentially leading to complete system compromise
- **Status**: Critical patch available, exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile systems being exploited with custom malware kits
- **Impact**: Deployment of sophisticated malware strains allowing persistent access and data exfiltration
- **Status**: Active exploitation with malware kits analyzed by CISA
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **OpenAI ChatGPT**: Deep Research agent susceptible to zero-click data exfiltration
- **Ivanti EPMM**: Endpoint Manager Mobile systems compromised with custom malware
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories
- **European Telecommunications**: Infrastructure compromised via MINIBIKE malware campaigns
- **Steam Gaming Platform**: Upcoming compatibility changes affecting 32-bit Windows systems

## Attack Vectors and Techniques

- **Zero-Click Email Exploitation**: ShadowLeak technique requiring no user interaction to compromise Gmail data
- **Command Injection**: Direct exploitation of GoAnywhere MFT License Servlet for system compromise
- **Social Engineering**: Fake GitHub repositories distributing malware-laced programs masquerading as legitimate software
- **LinkedIn Job Lures**: Professional networking platform used to deliver MINIBIKE malware to telecommunications targets
- **AI-Powered Malware**: GPT-4-enabled MalTerminal creating ransomware and reverse shell capabilities
- **Proxy Network Operations**: SystemBC malware powering REM Proxy with 1,500 daily VPS victims across 80 C2 servers

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Successfully infiltrated 34 devices across 11 European telecommunications organizations using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla (Russian)**: Collaborative operations deploying Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Two teen members arrested in connection with August 2024 Transport for London cyber attack
- **Lighthouse and Lucid PhaaS**: Operating 17,500 phishing domains targeting 316 brands across 74 countries
- **Unknown Advanced Actors**: Deploying GPT-4-powered MalTerminal malware with unprecedented AI integration capabilities