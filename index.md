# Exploitation Report

Multiple critical vulnerabilities are being actively exploited in the wild, including a maximum severity command injection flaw in Fortra GoAnywhere MFT and vulnerabilities in Ivanti EPMM systems. North Korean threat actors continue sophisticated social engineering campaigns targeting cryptocurrency professionals, while Iranian state-sponsored groups are conducting highly targeted espionage operations against telecommunications companies. Additionally, a zero-click vulnerability in OpenAI's ChatGPT Deep Research agent demonstrates the emerging attack surface in AI-powered applications.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows command injection attacks
- **Impact**: Attackers can execute arbitrary commands on affected systems
- **Status**: Patches available; exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile being exploited to deploy malware
- **Impact**: Successful exploitation allows attackers to deploy custom malware payloads on enterprise mobile management systems
- **Status**: Active exploitation observed with deployment of specialized malware kits
- **CVE ID**: CVE-2025-4427 and CVE-2025-4428

### OpenAI ChatGPT Deep Research Agent Zero-Click Vulnerability (ShadowLeak)
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that can leak sensitive Gmail inbox data
- **Impact**: Attackers can exfiltrate Gmail data through a single crafted email without user interaction, leaving no trace on enterprise systems
- **Status**: Vulnerability disclosed, exploitation demonstrated by researchers

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platforms
- **OpenAI ChatGPT**: Deep Research agent feature vulnerable to data exfiltration
- **Apple macOS**: Targeted by information stealer campaigns through fake GitHub repositories
- **Telecommunications Infrastructure**: European telecom companies targeted by Iranian threat actors

## Attack Vectors and Techniques

- **ClickFix-Style Lures**: DPRK hackers using fake technical error messages to deliver BeaverTail malware
- **LinkedIn Job Scams**: Social engineering targeting cryptocurrency professionals with fraudulent job opportunities
- **Fake GitHub Repositories**: Distribution of Atomic Infostealer through legitimate-looking software repositories
- **Command Injection**: Exploitation of servlet vulnerabilities for arbitrary command execution
- **Zero-Click Email Attacks**: Crafted emails that trigger data exfiltration without user interaction
- **AI-Powered Malware Generation**: MalTerminal malware using GPT-4 capabilities to create ransomware and reverse shells

## Threat Actor Activities

- **DPRK-linked Threat Actors**: Conducting sophisticated cryptocurrency-focused job scam campaigns using ClickFix techniques and BeaverTail malware
- **UNC1549 (Iranian)**: Successfully infiltrating 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla (Russian)**: Collaborative operations deploying Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in connection with August 2024 Transport for London cyber attack
- **Charming Kitten Subgroup**: Performing highly customized attacks against telecommunications and satellite companies for target selection