# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple attack vectors, with critical vulnerabilities being actively exploited in enterprise environments. Notable threats include CISA's addition of actively exploited flaws to the Known Exploited Vulnerabilities catalog, including CVE-2024-37079 affecting VMware vCenter Server and CVE-2026-20045 in Cisco UC systems. Additionally, a critical authentication bypass vulnerability in GNU InetUtils telnetd (CVE-2026-24061) that remained undetected for 11 years is now under active exploitation. The threat landscape is further complicated by sophisticated phishing campaigns targeting SSO accounts, nation-state attacks on critical infrastructure, and the emergence of new ransomware families utilizing advanced evasion techniques.

## Active Exploitation Details

### VMware vCenter Server Authentication Bypass
- **Description**: Critical security flaw affecting Broadcom VMware vCenter Server that was patched in June 2024
- **Impact**: Successful exploitation could lead to unauthorized access to vCenter management infrastructure
- **Status**: Actively exploited in the wild, patch available since June 2024
- **CVE ID**: CVE-2024-37079

### Cisco UC Critical Zero-Day
- **Description**: Critical zero-day vulnerability in Cisco Unified Communications systems
- **Impact**: Successful exploitation could lead to complete system takeover
- **Status**: Mass scanning campaigns underway, zero-day vulnerability
- **CVE ID**: CVE-2026-20045

### GNU InetUtils Telnetd Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in GNU InetUtils telnet daemon that remained undetected for 11 years
- **Impact**: Attackers can bypass login mechanisms and gain root access
- **Status**: Coordinated exploitation campaigns observed, rated 9.8/10.0 severity
- **CVE ID**: CVE-2026-24061

### FortiCloud SSO Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiCloud SSO affecting fully patched FortiGate firewalls
- **Impact**: Allows unauthorized access to firewall management and configuration theft
- **Status**: Active exploitation confirmed on fully patched systems, incomplete patch coverage

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools' SmarterMail email server
- **Impact**: Allows attackers to reset admin passwords and hijack administrator accounts
- **Status**: Active exploitation observed targeting admin account takeover

## Affected Systems and Products

- **VMware vCenter Server**: Critical infrastructure management systems patched in June 2024
- **Cisco Unified Communications**: Enterprise communication systems under mass scanning attacks
- **GNU InetUtils telnetd**: Unix/Linux systems running telnet daemon services for 11+ years
- **FortiGate Firewalls**: Network security appliances with FortiCloud SSO integration
- **SmarterMail Server**: Email and collaboration platforms in enterprise environments
- **Vehicle Infotainment Systems**: Automotive systems with 76 zero-day vulnerabilities discovered at Pwn2Own
- **EV Charging Infrastructure**: Electric vehicle charging stations with multiple security flaws
- **VSCode Marketplace**: Developer environments with malicious AI extensions installed 1.5 million times

## Attack Vectors and Techniques

- **Voice Phishing (Vishing)**: Custom phishing kits targeting Okta, Microsoft, and Google SSO accounts using social engineering
- **Mass Scanning Campaigns**: Automated reconnaissance targeting recently disclosed vulnerabilities
- **Configuration File Theft**: Exploitation of firewall vulnerabilities to steal sensitive configuration data
- **Remote Code Execution**: Zero-day exploitation leading to complete system compromise
- **Supply Chain Attacks**: Malicious extensions in developer marketplaces stealing credentials and source code
- **Bring Your Own Vulnerable Driver (BYOVD)**: Ransomware using legitimate but vulnerable drivers for privilege escalation
- **Multi-Stage AitM Phishing**: Advanced adversary-in-the-middle attacks targeting energy sector organizations

## Threat Actor Activities

- **Sandworm (Russian APT)**: Deployed new DynoWiper malware in attempted attack on Polish power sector infrastructure
- **ShinyHunters**: Claims responsibility for ongoing vishing campaigns targeting SSO accounts across major cloud providers
- **Osiris Ransomware Group**: New ransomware family targeting Southeast Asian food service operators using POORTRY driver in BYOVD attacks
- **Venezuelan ATM Fraudsters**: Convicted cybercriminals who deployed malware for ATM jackpotting schemes targeting U.S. banking infrastructure
- **Unknown Threat Actors**: Coordinated campaigns exploiting telnetd vulnerabilities and conducting phishing attacks against energy firms