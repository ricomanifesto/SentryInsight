# Exploitation Report

Critical exploitation activity is currently targeting multiple systems across various platforms, with attackers actively exploiting zero-day vulnerabilities and recently patched flaws. The most severe threats include active exploitation of authentication bypass vulnerabilities in SmarterMail email servers, critical remote code execution flaws in Cisco Unified Communications products (CVE-2026-20045), and authentication vulnerabilities in Fortinet FortiGate firewalls (CVE-2025-59718). Additionally, a critical 11-year-old vulnerability in GNU InetUtils telnet daemon (CVE-2026-24061) has been disclosed, allowing complete authentication bypass and root access. North Korean threat actors are conducting sophisticated campaigns using fake job interviews and Visual Studio Code tunnels to establish persistent access to victim systems.

## Active Exploitation Details

### SmarterMail Authentication Bypass Vulnerability
- **Description**: Authentication bypass flaw in SmarterTools SmarterMail email server allowing attackers to reset administrator passwords without proper authentication
- **Impact**: Complete administrative account takeover, unauthorized access to email systems and collaboration tools
- **Status**: Actively exploited in the wild just two days after patch release

### Cisco Unified Communications Remote Code Execution
- **Description**: Critical remote code execution vulnerability affecting Cisco Unified Communications Manager (CM) and Webex Calling Dedicated Instance
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Actively exploited as zero-day before patch, now fixed
- **CVE ID**: CVE-2026-20045

### Fortinet FortiGate Authentication Bypass
- **Description**: Critical authentication vulnerability in FortiGate firewalls with patch bypass techniques being exploited
- **Impact**: Unauthorized access to firewall configurations, creation of rogue accounts, and theft of sensitive network data
- **Status**: Actively exploited despite patches being available, automated attacks observed
- **CVE ID**: CVE-2025-59718

### GNU InetUtils Telnet Daemon Vulnerability
- **Description**: Critical authentication bypass vulnerability in GNU InetUtils telnet daemon that remained undetected for nearly 11 years
- **Impact**: Complete authentication bypass allowing attackers to gain root access without valid credentials
- **Status**: Recently disclosed, high risk for exploitation
- **CVE ID**: CVE-2026-24061

### Pwn2Own Automotive Zero-Days
- **Description**: Multiple zero-day vulnerabilities demonstrated at Pwn2Own Automotive competition
- **Impact**: Various impacts across automotive systems and related technologies
- **Status**: 29 zero-day vulnerabilities successfully exploited during competition

## Affected Systems and Products

- **SmarterMail Email Server**: All versions prior to latest security update, email and collaboration platforms
- **Cisco Unified Communications Manager**: Multiple CM products and Webex Calling Dedicated Instance
- **Fortinet FortiGate Firewalls**: Network security appliances with FortiCloud SSO integration
- **GNU InetUtils**: Telnet daemon implementations across Linux and Unix systems
- **Automotive Systems**: Various automotive technologies demonstrated at security competitions
- **Chainlit AI Framework**: Open-source conversational AI applications and cloud environments
- **Android Devices**: Mobile platforms targeted by AI-powered click-fraud malware
- **Visual Studio Code**: Development environments used as attack vectors by North Korean actors

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct exploitation of authentication flaws to gain administrative access
- **Remote Code Execution**: Exploitation of RCE vulnerabilities for complete system compromise
- **Automated Attacks**: Large-scale automated exploitation campaigns targeting multiple organizations
- **Social Engineering**: Fake job interview campaigns using trusted development tools
- **VS Code Tunnels**: Abuse of Microsoft Visual Studio Code remote access features for persistence
- **BYOVD (Bring Your Own Vulnerable Driver)**: Use of POORTRY driver in ransomware operations
- **AI-Powered Attacks**: Machine learning models used for automated ad clicking and evasion
- **Supply Chain Attacks**: Malicious PyPI packages impersonating legitimate libraries
- **Configuration Manipulation**: Unauthorized firewall configuration changes through SSO exploitation

## Threat Actor Activities

- **North Korean Groups**: Conducting "Contagious Interview" campaigns targeting 3,136 IP addresses across 20 organizations in artificial intelligence, cryptocurrency, and technology sectors
- **PurpleBravo Campaign**: Large-scale North Korean operation using fake job interviews and VS Code infrastructure
- **Osiris Ransomware Group**: New ransomware family targeting food service operators in Southeast Asia using BYOVD techniques
- **INC Ransomware Gang**: Operational security failures allowed data recovery for 12 US organizations
- **Automated Threat Actors**: Conducting systematic attacks against FortiGate devices and SmarterMail servers
- **Cryptocurrency Miners**: Deploying XMRig miners through malicious PyPI packages targeting Linux hosts