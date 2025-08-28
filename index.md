# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting both traditional infrastructure and emerging AI technologies. Most notably, FreePBX servers are being actively compromised through a zero-day vulnerability affecting systems with exposed Administrator Control Panels. Concurrently, sophisticated threat actors are leveraging AI services for malicious purposes, with Storm-0501 evolving their operations to focus on cloud-based attacks and data exfiltration. The emergence of AI-powered ransomware variants like PromptLock demonstrates the intersection of artificial intelligence and cybercrime, while state-sponsored groups continue to exploit network infrastructure for espionage activities.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in FreePBX systems that allows unauthorized access when the Administrator Control Panel (ACP) is exposed to the internet
- **Impact**: Complete system compromise allowing attackers to gain administrative access to FreePBX servers
- **Status**: Actively exploited in the wild; emergency fix has been released by Sangoma FreePBX Security Team

### AI Service Abuse for Data Extortion
- **Description**: Threat actors are abusing Anthropic's Claude Code service to automate various stages of cyberattacks including reconnaissance, intrusions, and credential harvesting
- **Impact**: Unprecedented automation of attack campaigns enabling large-scale data extortion operations
- **Status**: Active campaign identified with threat actors using AI services "to an unprecedented degree"

### Captive Portal Hijacking
- **Description**: Mustang Panda APT group is hijacking Google Chrome browsers during network connection attempts, redirecting users to phishing sites
- **Impact**: Credential theft and espionage targeting Asian diplomatic personnel
- **Status**: Active campaign targeting diplomatic entities across Asia

## Affected Systems and Products

- **FreePBX Systems**: Servers with Administrator Control Panel exposed to internet
- **Anthropic Claude Code Service**: AI service being abused for automated attack campaigns
- **Google Chrome Browsers**: Targeted during captive portal connections for redirection attacks
- **Salesforce Environments**: Compromised via third-party OAuth tokens from Salesloft Drift application
- **Azure Cloud Infrastructure**: Targeted by Storm-0501 for data exfiltration and deletion
- **Microsoft Entra ID**: Exploited for hybrid cloud attacks and privilege escalation
- **Swedish Municipal IT Systems**: 200+ municipalities affected through Miljödata supplier compromise
- **Nevada State Government Systems**: Multiple agencies shut down following cyberattack

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched FreePBX vulnerabilities through exposed management interfaces
- **AI-Powered Automation**: Using legitimate AI services to automate reconnaissance, intrusion, and data harvesting activities
- **Browser Hijacking**: Intercepting and redirecting browser traffic during network authentication processes
- **OAuth Token Compromise**: Exploiting third-party application integrations to gain unauthorized access to cloud services
- **Cloud Infrastructure Targeting**: Shifting from traditional ransomware to cloud-focused data exfiltration and deletion
- **Supply Chain Attacks**: Compromising IT service providers to impact multiple downstream organizations
- **Hybrid Cloud Exploitation**: Leveraging identity services to move between on-premises and cloud environments

## Threat Actor Activities

- **Storm-0501**: Evolved operations focusing on cloud-based encryption, data theft, and extortion rather than traditional device encryption; actively exploiting Entra ID for Azure data exfiltration and deletion
- **Mustang Panda APT**: Conducting espionage operations against Asian diplomats through captive portal hijacking and browser redirection attacks
- **UNC6395**: Engaged in widespread data theft via compromised OAuth tokens from Salesloft Drift third-party application
- **PromptLock Operators**: Developing and deploying AI-powered ransomware using Lua scripts for cross-platform data theft and encryption
- **ZipLine Campaign**: Sophisticated phishing operation affecting dozens of organizations across multiple industry sectors with victims initiating contact first
- **Unknown Actors**: Targeting Swedish municipal systems through IT supplier Miljödata, affecting over 200 regions
- **Nevada State Attackers**: Conducting cyberattacks against state government infrastructure, forcing shutdown of in-person services