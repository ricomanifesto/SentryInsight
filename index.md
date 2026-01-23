# Exploitation Report

Critical security vulnerabilities are being actively exploited across multiple platforms, with several zero-day attacks and recently patched vulnerabilities under active assault. The most severe incidents include a critical GNU InetUtils telnet daemon vulnerability (CVE-2026-24061) that allows complete login bypass and root access, a Cisco Unified Communications zero-day (CVE-2026-20045) enabling remote code execution, and an authentication bypass flaw in SmarterMail that is being exploited to hijack administrator accounts. Automated attacks are targeting Fortinet FortiGate devices to steal firewall configurations, while threat actors are leveraging legitimate tools like VS Code tunnels for persistent access. Additionally, 29 zero-day vulnerabilities were successfully exploited during the Pwn2Own Automotive competition, demonstrating the widespread nature of current security weaknesses.

## Active Exploitation Details

### GNU InetUtils Telnet Daemon Critical Flaw
- **Description**: A critical authentication bypass vulnerability in the GNU InetUtils telnet daemon that went unnoticed for nearly 11 years
- **Impact**: Attackers can bypass login authentication and gain root access to affected systems
- **Status**: Actively exploitable, patch status unclear
- **CVE ID**: CVE-2026-24061

### Cisco Unified Communications Zero-Day
- **Description**: Critical remote code execution vulnerability in Cisco Unified Communications (CM) products and Webex Calling Dedicated Instance
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited as zero-day, patches now released by Cisco
- **CVE ID**: CVE-2026-20045

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools SmarterMail email server and collaboration tool
- **Impact**: Allows attackers to reset administrator passwords and hijack admin accounts
- **Status**: Actively exploited in the wild just two days after patch release

### Pwn2Own Automotive Zero-Days
- **Description**: Multiple zero-day vulnerabilities discovered and exploited during security competition
- **Impact**: Various impacts across automotive systems and components
- **Status**: 29 zero-day vulnerabilities successfully exploited on second day of competition

## Affected Systems and Products

- **GNU InetUtils telnetd**: Critical vulnerability affecting telnet daemon service
- **Cisco Unified Communications**: Multiple CM products and Webex Calling Dedicated Instance affected by zero-day
- **SmarterTools SmarterMail**: Email server and collaboration platform vulnerable to authentication bypass
- **Fortinet FortiGate**: Firewall devices targeted in automated configuration theft attacks
- **Automotive Systems**: Various automotive platforms and components affected by multiple zero-days
- **PyPI Package Repository**: Malicious packages impersonating legitimate libraries like SymPy
- **Zendesk Support Systems**: Unsecured ticket systems hijacked for massive spam campaigns
- **Chainlit AI Framework**: Open-source conversational AI applications vulnerable to file disclosure
- **Android Devices**: New malware family targeting mobile platforms with AI-powered ad clicking

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploiting flaws in login mechanisms to gain unauthorized access
- **Remote Code Execution**: Leveraging vulnerabilities to execute arbitrary commands on target systems
- **Automated Configuration Theft**: Systematic attacks against firewall devices to steal configuration data
- **VS Code Tunnels**: Abuse of legitimate Microsoft development infrastructure for persistent access
- **Supply Chain Attacks**: Malicious packages deployed through trusted software repositories
- **Adversary-in-the-Middle (AitM)**: Multi-stage phishing campaigns targeting energy sector organizations
- **Voice Phishing (Vishing)**: Custom phishing kits designed for voice-based social engineering attacks
- **BYOVD (Bring Your Own Vulnerable Driver)**: Osiris ransomware using POORTRY driver for system compromise
- **AI-Powered Malware**: Android trojans using TensorFlow models for automated ad fraud

## Threat Actor Activities

- **DPRK-Linked Groups**: Conducting spear-phishing campaigns using VS Code tunnels and "Contagious Interview" attacks targeting developers
- **Osiris Ransomware Group**: Deploying new ransomware strain targeting food service operators in Southeast Asia using vulnerable driver techniques
- **INC Ransomware**: Operational security failure exposed data from 12 U.S. organizations, allowing data recovery
- **Energy Sector Attackers**: Sophisticated multi-stage campaigns combining AitM phishing and business email compromise against energy companies
- **FortiGate Threat Actors**: Automated attacks creating rogue accounts and stealing firewall configurations from potentially patched devices
- **Supply Chain Attackers**: Deploying malicious PyPI packages to target Linux hosts with cryptocurrency miners