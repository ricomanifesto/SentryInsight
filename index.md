# Exploitation Report

Critical exploitation activity is surging with multiple zero-day vulnerabilities being actively exploited in the wild. Microsoft's October 2025 Patch Tuesday addressed 183 security flaws, including three actively exploited vulnerabilities, with two new Windows zero-days affecting every version of Windows ever shipped. Nation-state actors have compromised F5's BIG-IP systems, stealing undisclosed vulnerabilities and source code. Harvard University fell victim to an Oracle zero-day attack claimed by the Clop ransomware group, while Chinese threat actors are leveraging compromised ArcGIS servers as persistent backdoors. Additional active exploitation includes ICTBroadcast servers being targeted through cookie exploits and a critical SAP NetWeaver vulnerability allowing server takeover without authentication.

## Active Exploitation Details

### Windows Zero-Day Vulnerabilities
- **Description**: Two new zero-day vulnerabilities in Windows operating systems are being actively exploited in the wild
- **Impact**: One vulnerability affects every version of Windows ever shipped, potentially allowing attackers to compromise any Windows system
- **Status**: Patched in Microsoft's October 2025 Patch Tuesday update (183 total security fixes)

### F5 BIG-IP Zero-Day Vulnerabilities
- **Description**: Nation-state hackers breached F5 systems and stole undisclosed BIG-IP security vulnerabilities along with source code
- **Impact**: Stolen vulnerabilities could be weaponized for future attacks against F5 BIG-IP environments
- **Status**: F5 has released security updates to address the stolen vulnerabilities following breach detection on August 9, 2025

### Oracle Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in Oracle systems being exploited by Clop ransomware group
- **Impact**: Successful data theft from high-profile targets including Harvard University
- **Status**: Part of broader campaign against Oracle customers by Clop ransomware group

### ICTBroadcast Cookie Exploit
- **Description**: Critical security flaw in ICTBroadcast autodialer software being actively exploited through cookie manipulation
- **Impact**: Remote shell access to compromised servers
- **Status**: Under active exploitation in the wild

### SAP NetWeaver Command Execution Vulnerability
- **Description**: Maximum-severity vulnerability in SAP NetWeaver AS Java allowing arbitrary command execution
- **Impact**: Complete server takeover without requiring authentication credentials
- **Status**: Security fixes released by SAP with additional hardening measures

## Affected Systems and Products

- **F5 BIG-IP Systems**: Critical infrastructure components compromised by nation-state actors with source code and vulnerability details stolen
- **Windows Operating Systems**: All versions of Windows affected by at least one of the exploited zero-day vulnerabilities
- **Oracle Systems**: Multiple Oracle customers targeted, including Harvard University
- **ICTBroadcast Servers**: Autodialer software from ICT Innovations under active attack
- **SAP NetWeaver AS Java**: Enterprise application servers vulnerable to unauthenticated takeover
- **ArcGIS Servers**: Geospatial mapping software compromised and used as persistent backdoor
- **Visual Studio Code Extensions**: Over 100 VS Code extensions exposed developers to supply chain risks through leaked access tokens

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being exploited before patches were available
- **Cookie Manipulation**: ICTBroadcast servers compromised through malicious cookie exploitation techniques
- **Supply Chain Attacks**: Malicious VS Code extensions targeting developers with crypto-stealing capabilities
- **Backdoor Installation**: ArcGIS servers compromised and maintained as persistent backdoors for over a year
- **Phishing Campaigns**: Fake LastPass and Bitwarden breach alerts leading to system compromises
- **Source Code Theft**: Advanced persistent threat actors stealing vulnerability details and source code for future exploitation

## Threat Actor Activities

- **Nation-State Actors**: Sophisticated breach of F5 systems to steal BIG-IP vulnerabilities and source code for weaponization
- **Clop Ransomware Group**: Actively exploiting Oracle zero-day vulnerabilities in campaign against Oracle customers, claiming responsibility for Harvard University breach
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with sophisticated custom tools since early 2025
- **Chinese APT Groups**: Multiple activities including Jewelbug's five-month infiltration of Russian IT networks and Flax Typhoon's persistent ArcGIS server backdoor operations
- **TigerJack**: Threat actor continuously targeting developers through malicious VSCode extensions on multiple platforms to steal cryptocurrency