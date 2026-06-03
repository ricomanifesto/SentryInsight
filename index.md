# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and software applications through various attack vectors. The most significant threats include active exploitation of Android and Linux kernel vulnerabilities being tracked by CISA, maximum severity zero-day vulnerabilities in Acer Wave 7 routers, and a critical WordPress plugin flaw enabling administrative account takeovers. Additionally, threat actors are leveraging sophisticated social engineering campaigns, AI-powered toolkits, and novel attack techniques such as HTTP/2 bomb denial-of-service attacks that can crash web servers within seconds. Nation-state actors and cybercriminal groups are actively exploiting these vulnerabilities for data theft, system compromise, and widespread malware distribution campaigns.

## Active Exploitation Details

### Android Framework Vulnerability
- **Description**: A high-severity vulnerability in the Android Framework component that is being actively exploited in the wild
- **Impact**: Allows attackers to compromise Android devices and potentially gain unauthorized access to sensitive data
- **Status**: Patched in Google's June 2026 Android security update alongside 123 other vulnerabilities

### Linux Kernel and Android System Vulnerabilities
- **Description**: Multiple vulnerabilities in the Linux kernel and Android operating system that are being actively exploited by threat actors
- **Impact**: Enables system compromise and unauthorized access to affected devices
- **Status**: Under active exploitation with CISA warnings issued to organizations

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer Wave 7 mesh routers
- **Impact**: Complete system compromise and potential network infiltration
- **Status**: Currently unpatched with Acer working on fixes

### WordPress Kirki Plugin Privilege Escalation
- **Description**: Critical privilege escalation vulnerability in the Kirki plugin for WordPress
- **Impact**: Allows attackers to hijack any user account, including administrator accounts
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-8206

### Visual Studio Code GitHub Token Theft
- **Description**: Zero-day vulnerability in Microsoft Visual Studio Code that enables one-click attacks to steal GitHub OAuth tokens
- **Impact**: Complete compromise of GitHub authentication credentials and access to repositories
- **Status**: Exploit code publicly released, currently unpatched

### Windows Search URI NTLMv2 Hash Disclosure
- **Description**: Unpatched vulnerability in Windows Search URI functionality that exposes user NTLMv2 hashes
- **Impact**: Credential theft and potential lateral movement within networks
- **Status**: Currently unpatched with public disclosure

### WinRAR Exploitation by Gamaredon
- **Description**: Continued exploitation of a WinRAR vulnerability by the Russian Gamaredon hacking group
- **Impact**: Delivery of multiple malware families including GammaWorm and GammaSteel for data theft and network propagation
- **Status**: Active exploitation targeting Ukrainian organizations

## Affected Systems and Products

- **Android Devices**: Framework component vulnerabilities affecting mobile devices globally
- **Linux Systems**: Kernel vulnerabilities impacting various distributions and enterprise environments
- **Acer Wave 7 Mesh Routers**: Two zero-day vulnerabilities with maximum severity ratings
- **WordPress Sites**: Kirki plugin installations vulnerable to privilege escalation attacks
- **Microsoft Visual Studio Code**: Development environments at risk for GitHub token theft
- **Windows Systems**: Search URI functionality exposing NTLMv2 credentials
- **Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora vulnerable to HTTP/2 bomb attacks
- **WinRAR Applications**: Archive utility being exploited for malware delivery
- **Minecraft Gaming Platforms**: Over 116,000 systems infected through WeedHack campaign

## Attack Vectors and Techniques

- **HTTP/2 Bomb Attacks**: Novel denial-of-service technique capable of crashing web servers within seconds using malformed HTTP/2 requests
- **Social Engineering via ClickFix**: Malicious notifications and fake update prompts tricking users into executing harmful actions
- **AI-Powered Ransomware Toolkits**: Automated tools for EDR evasion and Active Directory discovery
- **Prompt Injection**: Malicious commands hidden in Google Gemini voice assistant notifications
- **One-Click Token Theft**: Sophisticated attacks targeting developer environments through VS Code vulnerabilities
- **Traffic Distribution Systems**: DriveSurge operation redirecting legitimate website traffic to malicious infrastructure
- **Spear-Phishing Campaigns**: Dual-layer attacks using Azureveil malware for data exfiltration
- **Device Code Phishing**: Kali365 phishing-as-a-service platform expanding beyond Microsoft 365 to target AWS and Okta

## Threat Actor Activities

- **Gamaredon (Russian Group)**: Actively exploiting WinRAR vulnerabilities to deliver GammaWorm and GammaSteel malware against Ukrainian targets
- **WeedHack Campaign Operators**: Large-scale malware distribution targeting Minecraft players with over 116,000 infections since January
- **Chinese State-Sponsored Groups**: Conducting dual-method cyberattacks against Czech and Taiwanese organizations using spear-phishing and Azureveil malware
- **DriveSurge Operation**: Wide-scale initial access broker (IAB) campaign hijacking thousands of websites for ClickFix and FakeUpdate attacks
- **Kali365 Operators**: FBI-flagged phishing-as-a-service platform expanding targeting scope to include AWS, Okta, and Russian platforms
- **AI-Enabled Threat Actors**: Utilizing artificial intelligence to build automated ransomware toolkits with enhanced evasion capabilities
- **Finance Sector Attackers**: Monthslong email campaign targeting global stock exchange executives using legitimate Windows tools