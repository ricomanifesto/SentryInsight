# Exploitation Report

The current threat landscape reveals a concerning shift toward AI-powered attacks and sophisticated cloud-based exploitation campaigns. Multiple threat actors are leveraging artificial intelligence to automate reconnaissance, credential harvesting, and data encryption operations. Notable activities include Storm-0501's evolution from traditional ransomware to cloud-focused attacks targeting Azure environments, the emergence of PromptLock as the first AI-powered ransomware, and active exploitation of FreePBX zero-day vulnerabilities. State-sponsored groups continue to target critical infrastructure, with Chinese APT groups hijacking captive portals for espionage and conducting widespread supply chain attacks affecting hundreds of organizations globally.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: An actively exploited zero-day vulnerability affecting FreePBX systems with the Administrator Control Panel (ACP) exposed to the internet
- **Impact**: Allows attackers to compromise FreePBX servers and gain unauthorized access to telecommunications infrastructure
- **Status**: Emergency fix has been released by the Sangoma FreePBX Security Team; active exploitation ongoing

### PromptLock AI-Powered Ransomware
- **Description**: First AI-powered ransomware using Lua scripts to automate data theft and encryption across multiple operating systems
- **Impact**: Cross-platform data encryption and theft affecting Windows, macOS, and Linux systems
- **Status**: Experimental ransomware currently in active development and deployment

### Anthropic Claude Code Service Abuse
- **Description**: Threat actors abusing Anthropic's Claude Code service to automate data extortion campaigns
- **Impact**: Unprecedented automation of reconnaissance, intrusions, and credential harvesting operations
- **Status**: Active abuse reported by Anthropic with automated attack campaigns ongoing

## Affected Systems and Products

- **FreePBX Systems**: Telecommunications servers with Administrator Control Panel exposed to internet
- **Azure Cloud Environments**: Microsoft Azure infrastructure targeted by Storm-0501 for data exfiltration and deletion
- **Entra ID Systems**: Microsoft identity management systems compromised for hybrid cloud attacks
- **Salesforce Platforms**: Customer data accessed through compromised OAuth tokens via third-party Salesloft Drift application
- **Swedish Municipal Systems**: Over 200 municipalities affected through Miljödata IT systems supplier compromise
- **Nevada State Agencies**: Multiple state government systems shut down following cyberattack
- **Multi-Platform Systems**: Windows, macOS, and Linux systems targeted by AI-powered ransomware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched FreePBX vulnerabilities through internet-exposed control panels
- **AI-Automated Attacks**: Use of artificial intelligence for automated reconnaissance, credential harvesting, and data encryption
- **Cloud Infrastructure Targeting**: Direct attacks on cloud environments for data exfiltration and deletion rather than traditional endpoint encryption
- **OAuth Token Compromise**: Exploitation of third-party application OAuth tokens to access cloud-based customer data
- **Captive Portal Hijacking**: Redirection of Google Chrome browsers to phishing sites when connecting to new networks
- **Supply Chain Attacks**: Targeting IT service providers to impact hundreds of downstream organizations
- **Hybrid Cloud Exploitation**: Leveraging compromised on-premises systems to access cloud environments

## Threat Actor Activities

- **Storm-0501**: Evolved operations from traditional ransomware to cloud-focused attacks, targeting Azure environments for data exfiltration and deletion using compromised Entra ID credentials
- **Mustang Panda APT**: Chinese state-sponsored group hijacking captive portals to redirect Chrome browsers to phishing sites targeting Asian diplomats
- **UNC6395**: Conducted widespread data theft through compromised OAuth tokens from Salesloft Drift third-party application affecting Salesforce customers
- **Salt Typhoon**: Chinese state-sponsored group linked to global hacking campaigns affecting telecommunications infrastructure across multiple countries
- **ZipLine Campaign**: Sophisticated phishing operation targeting dozens of organizations across multiple industry sectors using reverse social engineering tactics
- **PromptLock Operators**: Threat researchers discovered operators deploying the first AI-powered ransomware across multiple operating systems