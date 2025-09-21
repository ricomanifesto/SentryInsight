# Exploitation Report

Critical vulnerabilities are currently being exploited across multiple platforms, with the most severe being a maximum severity command injection flaw in Fortra GoAnywhere MFT's License Servlet (CVE-2025-10035) that allows arbitrary command execution. Additionally, threat actors are actively exploiting Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428) with sophisticated malware campaigns, while Iranian state-sponsored groups are conducting highly targeted attacks against telecommunications companies. A concerning zero-click vulnerability in OpenAI ChatGPT's Deep Research agent enables data exfiltration through crafted emails, and AI-powered malware is emerging with LLM capabilities for dynamic attack generation.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows command injection attacks
- **Impact**: Attackers can execute arbitrary commands on vulnerable systems
- **Status**: Critical patches have been released by Fortra; exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Authentication Bypass Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile being actively exploited with custom malware kits
- **Impact**: Complete system compromise with deployment of sophisticated malware strains
- **Status**: Active exploitation confirmed by CISA with malware analysis published
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak Zero-Click Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that allows data exfiltration through crafted emails
- **Impact**: Attackers can leak sensitive Gmail inbox data without user interaction
- **Status**: Actively exploitable vulnerability requiring only a single crafted email

### MalTerminal AI-Powered Malware
- **Description**: First known malware incorporating Large Language Model capabilities for dynamic attack generation
- **Impact**: Can create ransomware and reverse shells on-demand using GPT-4 integration
- **Status**: Active in the wild representing new evolution in malware sophistication

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple authentication bypass vulnerabilities with active exploitation
- **OpenAI ChatGPT**: Deep Research agent susceptible to zero-click data exfiltration
- **macOS Systems**: Targeted by Atomic Infostealer through fake GitHub repositories
- **Windows Systems**: Affected by MalTerminal AI-powered malware
- **Telecommunications Infrastructure**: European telecom companies compromised by UNC1549 operations
- **Microsoft Azure Entra ID**: Critical IAM vulnerability (patched prior to disclosure)

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **Zero-Click Email Attacks**: ShadowLeak technique using crafted emails to trigger ChatGPT data exfiltration
- **Social Engineering**: LinkedIn job lures used by UNC1549 to deploy MINIBIKE malware
- **Repository Poisoning**: Fake GitHub repositories distributing Atomic Infostealer on macOS
- **AI-Enhanced Malware**: LLM integration for dynamic payload generation and attack adaptation
- **Proxy Network Abuse**: SystemBC malware powering REM Proxy with 1,500 daily victims across 80 C2 servers
- **Phishing-as-a-Service**: Lighthouse and Lucid platforms managing 17,500 domains targeting 316 brands

## Threat Actor Activities

- **UNC1549**: Iranian-nexus group successfully compromised 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla**: Russian state groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in connection with August 2024 Transport for London cyber attack
- **Charming Kitten Subgroup**: Conducting highly bespoke attacks against telecommunications and satellite companies with unprecedented customization
- **Criminal Networks**: TradeOgre cryptocurrency exchange dismantled with $40 million in seized criminal proceeds
- **PhaaS Operators**: Lighthouse and Lucid services facilitating attacks across 74 countries targeting major global brands