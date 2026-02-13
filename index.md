# Exploitation Report

Critical zero-day vulnerabilities continue to dominate the threat landscape, with Apple addressing an actively exploited zero-day used in extremely sophisticated attacks targeting specific individuals. Ivanti EPMM zero-day vulnerabilities are experiencing widespread exploitation with 83% of attacks traced to a single IP address on bulletproof hosting infrastructure. BeyondTrust Remote Support and Privileged Remote Access appliances face active exploitation of a critical pre-authentication remote code execution vulnerability following public proof-of-concept disclosure. Meanwhile, threat actors are increasingly leveraging AI tools like Google's Gemini for reconnaissance and attack support, while deploying sophisticated supply chain attacks through malicious npm and PyPI packages.

## Active Exploitation Details

### Apple Zero-Day Vulnerability
- **Description**: A zero-day vulnerability affecting iOS, macOS, and other Apple devices that enables sophisticated cyber attacks
- **Impact**: Allows attackers to conduct extremely sophisticated attacks targeting specific individuals
- **Status**: Patched by Apple in iOS, iPadOS, macOS Tahoe, tvOS, watchOS, and visionOS updates; was actively exploited before patching

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) causing an "exploit frenzy"
- **Impact**: Enables remote code execution and system compromise on enterprise mobile device management platforms
- **Status**: Under active exploitation with 83% of attacks originating from a single IP address on bulletproof hosting infrastructure

### BeyondTrust RCE Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability in BeyondTrust Remote Support and Privileged Remote Access appliances
- **Impact**: Allows attackers to achieve remote code execution without authentication on privileged access management systems
- **Status**: Now actively exploited in attacks following public proof-of-concept disclosure; patch available

### WordPress WPvivid Backup Plugin Vulnerability
- **Description**: Critical vulnerability in WPvivid Backup & Migration plugin affecting over 900,000 WordPress installations
- **Impact**: Enables remote code execution through arbitrary file upload capabilities
- **Status**: Critical vulnerability disclosed; affects widely-used WordPress plugin

### Windows 11 Notepad Vulnerability
- **Description**: Remote code execution vulnerability in Windows 11 Notepad application involving Markdown links
- **Impact**: Allows attackers to execute local or remote programs by tricking users into clicking specially crafted Markdown links
- **Status**: Fixed by Microsoft in recent Windows 11 updates

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, macOS Tahoe, tvOS, watchOS, and visionOS across multiple device types
- **Ivanti EPMM**: Enterprise mobile device management platforms and appliances
- **BeyondTrust Products**: Remote Support and Privileged Remote Access appliances used for privileged access management
- **WordPress Sites**: Over 900,000 websites using WPvivid Backup & Migration plugin
- **Windows 11**: Notepad application on Windows 11 systems
- **Chrome Browser**: 300,000+ users affected by malicious AI-themed extensions
- **macOS Systems**: Targeted by AMOS infostealer through popular AI applications

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Apple devices and Ivanti EPMM
- **Pre-Authentication RCE**: Exploitation of BeyondTrust appliances without requiring authentication
- **Malicious Browser Extensions**: Fake AI Chrome extensions stealing credentials and email content from 300,000+ users
- **Supply Chain Attacks**: Malicious packages planted in npm and PyPI ecosystems by Lazarus group
- **AI-Assisted Reconnaissance**: State-backed hackers using Google Gemini AI for target reconnaissance and attack planning
- **Social Engineering**: AMOS infostealer targeting macOS users through popular AI app marketplaces
- **Phishing Campaigns**: Microsoft Store Outlook add-in hijacked to steal over 4,000 Microsoft account credentials
- **Ransomware Deployment**: Crazy ransomware gang abusing employee monitoring software for persistence and evasion

## Threat Actor Activities

- **UNC2970 (North Korea-linked)**: Using Google Gemini AI model for reconnaissance on targets and attack support activities
- **Lazarus Group**: Orchestrating fake recruitment-themed campaign with malicious packages across npm and PyPI repositories
- **UNC1069 (North Korea)**: Targeting cryptocurrency firms using AI, deepfakes, and legitimate platforms in Web3-focused attacks
- **Crazy Ransomware Gang**: Abusing legitimate employee monitoring software and SimpleHelp remote support tools for network persistence
- **Green Blood Group**: Conducting data breaches against Senegalese national biometric database affecting nearly 20 million residents
- **Qilin Ransomware**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.
- **Unknown Actors**: Exploiting BeyondTrust vulnerabilities and coordinating Ivanti EPMM attacks from bulletproof hosting infrastructure