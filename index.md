# Exploitation Report

Current threat activity reveals several critical exploitation campaigns targeting diverse platforms and organizations. Most notably, a maximum severity vulnerability in Fortra GoAnywhere MFT (CVE-2025-10035) poses immediate command injection risks, while active exploitation of Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428) has led to malware deployment in enterprise environments. Additional zero-click vulnerabilities in OpenAI's ChatGPT infrastructure demonstrate the evolving attack surface in AI-powered services. Nation-state actors from North Korea and Iran continue sophisticated social engineering campaigns, while cybercriminals leverage AI-powered malware and phishing-as-a-service platforms to scale their operations globally.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity flaw in GoAnywhere MFT's License Servlet that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise through command injection attacks
- **Status**: Critical patch released by Fortra; immediate patching required
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile allowing malware deployment and system compromise
- **Impact**: Advanced persistent threat establishment, data exfiltration, and network lateral movement
- **Status**: Actively exploited in the wild with confirmed malware deployment
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Zero-Click Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that enables Gmail data exfiltration through crafted emails
- **Impact**: Sensitive email data theft without user interaction, potential corporate data breaches
- **Status**: Recently disclosed vulnerability affecting ChatGPT infrastructure

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple components affected by exploitation campaigns
- **OpenAI ChatGPT**: Deep Research agent functionality susceptible to data exfiltration
- **Apple macOS**: Targeted by Atomic Infostealer through fake GitHub repositories
- **European Telecommunications Infrastructure**: 34 devices across 11 organizations compromised
- **TradeOgre Cryptocurrency Exchange**: Dismantled by Canadian authorities with $40 million seized

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: DPRK actors using fake error messages to deliver BeaverTail malware in cryptocurrency job scams
- **Malicious GitHub Repositories**: Distribution of Atomic Infostealer targeting macOS through fake legitimate software
- **LinkedIn Job Lures**: UNC1549 using professional networking for MINIBIKE malware delivery
- **AI-Powered Malware**: MalTerminal leveraging GPT-4 capabilities for ransomware and reverse shell creation
- **Phishing-as-a-Service (PhaaS)**: Lighthouse and Lucid platforms operating 17,500 domains targeting 316 brands
- **SystemBC Proxy Networks**: REM Proxy botnet utilizing 1,500 daily VPS victims across 80 command and control servers

## Threat Actor Activities

- **DPRK Hackers**: Conducting cryptocurrency-focused social engineering campaigns using ClickFix techniques and BeaverTail malware
- **UNC1549 (Iran-linked)**: Targeting European telecommunications companies with LinkedIn-based social engineering and MINIBIKE malware deployment
- **Gamaredon and Turla (Russian)**: Collaborative operations deploying Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Two teenage members arrested in connection with Transport for London cyber attack
- **Charming Kitten Subgroup**: Performing sophisticated, bespoke attacks against telecommunications and satellite companies