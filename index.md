# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple vectors, with threat actors increasingly leveraging AI technologies and cloud environments for sophisticated attacks. Critical zero-day vulnerabilities are being actively exploited in FreePBX systems, while established threat groups like Storm-0501 and Mustang Panda are evolving their tactics to target cloud infrastructure and diplomatic entities. The emergence of AI-powered ransomware and automated data extortion campaigns represents a concerning evolution in cybercriminal capabilities, demonstrating how artificial intelligence is being weaponized for malicious purposes.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: A zero-day vulnerability affecting FreePBX systems with the Administrator Control Panel (ACP) exposed to the internet
- **Impact**: Allows attackers to compromise FreePBX servers and gain unauthorized access to telecommunications infrastructure
- **Status**: Actively exploited in the wild; emergency fix has been released by Sangoma FreePBX Security Team

### PromptLock AI-Powered Ransomware
- **Description**: First AI-powered ransomware using Lua scripts to automate data theft and encryption across multiple operating systems
- **Impact**: Capable of stealing and encrypting data on Windows, macOS, and Linux systems with enhanced automation capabilities
- **Status**: Experimental ransomware discovered by threat researchers, representing a new evolution in ransomware technology

### Anthropic Claude AI Service Abuse
- **Description**: Threat actors abusing Anthropic's Claude Code service to automate various stages of cyberattacks
- **Impact**: Enables automated reconnaissance, intrusions, and credential harvesting at unprecedented scale
- **Status**: Actively being exploited for data extortion campaigns with significant automation capabilities

## Affected Systems and Products

- **FreePBX Systems**: Telecommunications systems with Administrator Control Panel exposed to internet
- **Anthropic Claude Code Service**: AI service being abused for automated attack campaigns
- **Windows, macOS, and Linux Systems**: Targeted by PromptLock AI-powered ransomware
- **Azure Cloud Environments**: Targeted by Storm-0501 for data exfiltration and deletion
- **Salesforce Platforms**: Compromised through third-party OAuth tokens via Salesloft Drift application
- **Google Chrome Browsers**: Hijacked through captive portal attacks targeting diplomatic entities
- **Swedish Municipal IT Systems**: Over 200 municipalities affected through Miljödata IT supplier compromise
- **Nevada State Government Systems**: Multiple state agencies shut down due to cyberattack

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched FreePBX vulnerabilities through internet-exposed control panels
- **AI-Powered Automation**: Leveraging artificial intelligence services for automated reconnaissance, intrusion, and data harvesting
- **Cloud Environment Targeting**: Exploiting Entra ID to access and manipulate Azure cloud data
- **OAuth Token Compromise**: Abusing third-party application tokens to gain unauthorized access to Salesforce environments
- **Captive Portal Hijacking**: Redirecting browser connections to phishing sites during network authentication
- **Supply Chain Attacks**: Targeting IT service providers to impact multiple downstream organizations
- **Reverse Phishing Campaigns**: ZipLine campaign where victims initiate contact, flipping traditional phishing scripts

## Threat Actor Activities

- **Storm-0501**: Evolved operations from traditional ransomware to cloud-focused data exfiltration and extortion, specifically targeting hybrid cloud environments through Entra ID exploitation
- **Mustang Panda APT**: Conducting sophisticated espionage operations against Asian diplomats by hijacking Google Chrome browsers through captive portal manipulation
- **UNC6395**: Engaged in widespread data theft through compromised OAuth tokens from Salesloft Drift third-party application
- **ZipLine Campaign Operators**: Running sophisticated phishing operations affecting dozens of organizations across multiple industry sectors with victims initiating contact
- **Salt Typhoon**: Global hacking campaigns linked to Chinese technology firms, representing state-sponsored cyber espionage activities
- **PromptLock Developers**: Creating experimental AI-powered ransomware demonstrating the weaponization of artificial intelligence for cybercriminal purposes