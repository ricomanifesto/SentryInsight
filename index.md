# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure with multiple zero-day vulnerabilities and authentication bypass flaws being actively exploited in the wild. The most severe threats include a Cisco Unified Communications zero-day (CVE-2026-20045) affecting millions of users, a critical GNU InetUtils telnetd authentication bypass flaw (CVE-2026-24061) that has existed undetected for 11 years, and ongoing exploitation of VMware vCenter Server vulnerabilities (CVE-2024-37079). Additionally, Fortinet FortiGate firewalls are experiencing active attacks through a FortiCloud SSO authentication bypass that remains incompletely patched even on fully updated systems. Advanced persistent threats are also escalating with nation-state actors like Sandworm deploying new destructive malware against critical infrastructure, while cybercriminal groups are conducting sophisticated phishing campaigns targeting SSO providers and enterprise authentication systems.

## Active Exploitation Details

### Cisco Unified Communications Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Cisco UC systems currently under mass scanning exploitation
- **Impact**: Successful exploitation leads to complete system takeover and compromise of communications infrastructure
- **Status**: Actively exploited with ongoing mass scanning campaigns targeting vulnerable systems
- **CVE ID**: CVE-2026-20045

### GNU InetUtils telnetd Authentication Bypass
- **Description**: Critical authentication bypass flaw in GNU InetUtils telnet daemon that remained undetected for 11 years
- **Impact**: Allows attackers to completely bypass login authentication and gain root access to affected systems
- **Status**: Coordinated exploitation campaigns targeting the recently disclosed vulnerability
- **CVE ID**: CVE-2026-24061

### VMware vCenter Server Vulnerability
- **Description**: Critical security flaw affecting Broadcom VMware vCenter Server that was patched in June 2024
- **Impact**: Enables unauthorized access to virtualization infrastructure and potential lateral movement
- **Status**: Added to CISA KEV catalog due to confirmed active exploitation despite patches being available
- **CVE ID**: CVE-2024-37079

### Fortinet FortiCloud SSO Authentication Bypass
- **Description**: Authentication bypass vulnerability affecting FortiCloud SSO on FortiGate firewalls
- **Impact**: Allows unauthorized access to firewall configurations and potential network compromise
- **Status**: Actively exploited even on fully patched systems, with Fortinet confirming the vulnerability is not completely resolved

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server and collaboration platform
- **Impact**: Enables attackers to reset administrator passwords and hijack admin accounts
- **Status**: Currently being exploited to compromise email server administrative access

## Affected Systems and Products

- **Cisco Unified Communications**: Systems vulnerable to zero-day exploitation affecting millions of users
- **GNU InetUtils telnetd**: Telnet daemon servers running vulnerable versions from the past 11 years
- **VMware vCenter Server**: Broadcom VMware virtualization management platforms
- **Fortinet FortiGate Firewalls**: Network security appliances using FortiCloud SSO authentication
- **SmarterMail Email Servers**: SmarterTools email and collaboration platforms
- **Enterprise Software**: Versa and Zimbra products, plus Vite frontend tooling as confirmed by CISA
- **Automotive Systems**: Vehicle infotainment systems and EV chargers with 76 identified zero-day vulnerabilities
- **VSCode Marketplace**: Microsoft Visual Studio Code development environment with malicious AI extensions

## Attack Vectors and Techniques

- **Mass Scanning Campaigns**: Automated scanning targeting Cisco UC systems for zero-day exploitation
- **Authentication Bypass**: Direct login circumvention in telnetd and SmarterMail systems
- **Social Engineering**: Voice phishing (vishing) campaigns targeting SSO accounts at Okta, Microsoft, and Google
- **Multi-Stage Phishing**: Complex campaigns delivering Amnesia RAT and ransomware through social engineering
- **Supply Chain Attacks**: Malicious VSCode extensions exfiltrating developer data to China-based servers
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver techniques used by Osiris ransomware
- **Configuration Manipulation**: Unauthorized changes to Fortinet firewall configurations
- **Remote Access Tool Deployment**: LogMeIn RMM software installed via stolen credentials for persistent access

## Threat Actor Activities

- **Sandworm (Russian APT)**: Deployed new DynoWiper malware in attempted attack on Polish power infrastructure, described as the largest cyber attack targeting Poland's power system
- **ShinyHunters**: Claiming responsibility for wave of vishing attacks targeting SSO accounts across major providers
- **Amnesia RAT Operators**: Conducting multi-stage phishing campaigns targeting Russian users with ransomware and remote access trojans
- **Osiris Ransomware Group**: Targeted major food service franchisee in Southeast Asia using POORTRY driver in BYOVD attacks
- **Energy Sector Attackers**: Multi-stage adversary-in-the-middle phishing and business email compromise campaigns targeting energy organizations
- **Automotive Researchers**: Successfully exploited 76 zero-day vulnerabilities across vehicle systems during Pwn2Own Automotive 2026