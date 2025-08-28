# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across various sectors. The most significant threats include a zero-day vulnerability in FreePBX systems with exposed Administrator Control Panels being actively exploited, a critical remote code execution flaw in Citrix devices affecting over 28,000 instances worldwide, and sophisticated state-sponsored campaigns by Chinese threat actors targeting diplomatic entities and cloud environments. Additionally, the emergence of PromptLock, the first AI-powered ransomware using OpenAI's gpt-oss:20b model, represents a concerning evolution in ransomware capabilities across Windows, macOS, and Linux platforms.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: A zero-day vulnerability affecting FreePBX systems with the Administrator Control Panel (ACP) exposed to the internet
- **Impact**: Allows attackers to compromise FreePBX servers and gain unauthorized access to telecommunications infrastructure
- **Status**: Actively exploited in the wild; emergency fix has been released by Sangoma FreePBX Security Team

### Citrix Remote Code Execution Vulnerability
- **Description**: Critical remote code execution vulnerability in Citrix devices allowing attackers to execute arbitrary code
- **Impact**: Complete system compromise and potential lateral movement within enterprise networks
- **Status**: Actively exploited in the wild with over 28,200 vulnerable instances identified globally
- **CVE ID**: CVE-2025-7775

### PromptLock AI-Powered Ransomware
- **Description**: First artificial intelligence-powered ransomware written in Golang that uses OpenAI's gpt-oss:20b model with Lua scripts for encryption and data theft
- **Impact**: Cross-platform data encryption and exfiltration capabilities targeting Windows, macOS, and Linux systems
- **Status**: Experimental ransomware discovered by threat researchers, representing new evolution in ransomware technology

## Affected Systems and Products

- **FreePBX Systems**: Telecommunications systems with Administrator Control Panel exposed to internet
- **Citrix Devices**: Over 28,200 instances globally vulnerable to remote code execution
- **Multi-Platform Systems**: Windows, macOS, and Linux systems targeted by PromptLock ransomware
- **Salesforce Environments**: Compromised via third-party OAuth tokens from Salesloft Drift application
- **Azure Cloud Environments**: Hybrid cloud infrastructures targeted through Entra ID exploitation
- **Swedish Municipal Systems**: Over 200 municipalities affected through Miljödata IT supplier compromise
- **Nevada State Agencies**: Government systems requiring complete shutdown of in-person services
- **Google Chrome Browsers**: Hijacked during captive portal connections for phishing redirects

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched FreePBX vulnerabilities in internet-exposed systems
- **Remote Code Execution**: Exploitation of critical Citrix vulnerability for system compromise
- **AI-Enhanced Encryption**: Use of artificial intelligence models for sophisticated ransomware operations
- **OAuth Token Compromise**: Exploitation of third-party application tokens for unauthorized access to cloud services
- **Captive Portal Hijacking**: Redirection of browser connections to phishing sites during network authentication
- **Hybrid Cloud Attacks**: Exploitation of Entra ID for data exfiltration and deletion in Azure environments
- **Supply Chain Attacks**: Targeting IT service providers to impact multiple downstream organizations

## Threat Actor Activities

- **Storm-0501**: Financially motivated group refining tactics for cloud environment data exfiltration and extortion attacks targeting hybrid infrastructures
- **Mustang Panda APT**: Chinese state-sponsored group hijacking Google Chrome browsers during captive portal connections to redirect Asian diplomats to phishing sites
- **UNC6395**: Threat group engaged in widespread data theft via compromised OAuth tokens from Salesloft Drift third-party application
- **Salt Typhoon**: Chinese state-sponsored campaign linked to three China-based technology firms conducting global hacking operations against telecommunications and government targets
- **ZipLine Phishing Campaign**: Sophisticated operation affecting dozens of organizations across multiple industry sectors using reverse social engineering tactics