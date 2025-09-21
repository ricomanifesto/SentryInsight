# Exploitation Report

Critical security vulnerabilities are being actively exploited across multiple platforms, with several high-severity flaws posing immediate threats to organizations worldwide. The most concerning developments include a maximum severity vulnerability in Fortra's GoAnywhere MFT platform, active exploitation of Ivanti Endpoint Manager Mobile vulnerabilities, a zero-click flaw in OpenAI's ChatGPT Deep Research agent, and sophisticated malware campaigns leveraging AI capabilities. State-sponsored threat actors continue to target telecommunications companies and critical infrastructure, while phishing-as-a-service operations have reached unprecedented scale with over 17,500 malicious domains targeting hundreds of brands globally.

## Active Exploitation Details

### Fortra GoAnywhere MFT License Servlet Vulnerability
- **Description**: A maximum severity command injection vulnerability affecting GoAnywhere Managed File Transfer software's License Servlet component
- **Impact**: Allows attackers to execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Critical security updates have been released by Fortra; immediate patching required
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile being actively exploited by threat actors who have deployed sophisticated malware toolkits
- **Impact**: Successful exploitation allows attackers to deploy custom malware strains and maintain persistent access to enterprise mobile device management systems
- **Status**: CISA has published detailed analysis of malware deployed in attacks; patches available
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Zero-Click Vulnerability
- **Description**: A zero-click vulnerability in OpenAI's ChatGPT Deep Research agent that allows attackers to exfiltrate sensitive Gmail data through crafted emails
- **Impact**: Enables invisible data theft from enterprise email systems without any user interaction, leaving no trace on victim systems
- **Status**: Actively being researched and disclosed; exploitation requires minimal user interaction

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component in managed file transfer software
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platform
- **OpenAI ChatGPT Deep Research Agent**: AI-powered research functionality within ChatGPT
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories
- **European Telecommunications Companies**: 34 devices across 11 organizations compromised
- **Gmail and Enterprise Email Systems**: Vulnerable to data exfiltration through ChatGPT integration

## Attack Vectors and Techniques

- **Command Injection**: Maximum severity vulnerability in GoAnywhere MFT allowing arbitrary code execution
- **Zero-Click Exploitation**: ShadowLeak technique requiring only email delivery to exfiltrate data
- **Social Engineering**: Fake GitHub repositories distributing macOS malware masquerading as legitimate software
- **AI-Powered Malware**: MalTerminal malware incorporating GPT-4 capabilities for dynamic attack generation
- **LinkedIn Job Lures**: UNC1549 using professional networking platform to deliver MINIBIKE malware
- **Phishing-as-a-Service**: Lighthouse and Lucid platforms generating over 17,500 malicious domains

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla (Russian)**: Unprecedented collaboration between two Russian state-sponsored groups deploying Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Two teenage members arrested in connection with August 2024 Transport for London cyber attack
- **Charming Kitten Subgroup**: Conducting highly sophisticated, bespoke attacks against telecommunications and satellite companies
- **SystemBC Operators**: Managing REM Proxy network with approximately 1,500 daily VPS victims across 80 command and control servers
- **LastPass Campaign Actors**: Distributing Atomic Infostealer through fake macOS applications in widespread GitHub repository campaign