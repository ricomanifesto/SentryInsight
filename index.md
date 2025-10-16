# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise environments. CISA has flagged an Adobe Experience Manager vulnerability with a perfect 10.0 CVSS score that is already under active attack. Microsoft's October 2025 Patch Tuesday addressed 172-183 security vulnerabilities, including at least three zero-day vulnerabilities being actively exploited in the wild, with one affecting every version of Windows ever shipped. Nation-state actors have compromised F5's BIG-IP systems, stealing undisclosed zero-day vulnerabilities and source code. Additional active exploitation includes ICTBroadcast servers being targeted through cookie exploits, Harvard University breached via Oracle zero-day attacks, and Red Lion industrial control systems exposed through critical CVSS 10.0 vulnerabilities.

## Active Exploitation Details

### Adobe Experience Manager Critical Vulnerability
- **Description**: A critical security flaw in Adobe Experience Manager with a perfect 10.0 CVSS score that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Allows attackers to gain unauthorized access to Adobe AEM systems
- **Status**: Currently under active exploitation in the wild; patches available

### Windows Zero-Day Vulnerabilities
- **Description**: Three zero-day vulnerabilities affecting Windows systems, with one impacting every version of Windows ever shipped
- **Impact**: Enables various forms of system compromise and privilege escalation
- **Status**: Actively exploited in the wild; patches released in Microsoft's October 2025 Patch Tuesday update

### F5 BIG-IP Zero-Day Vulnerabilities
- **Description**: Multiple undisclosed zero-day vulnerabilities in F5 BIG-IP systems that were stolen during a nation-state breach
- **Impact**: Potential for complete system compromise and lateral movement
- **Status**: Vulnerabilities were stolen by nation-state actors; F5 has released patches for the affected systems

### ICTBroadcast Cookie Exploitation
- **Description**: A critical security flaw in ICTBroadcast autodialer software being exploited through cookie manipulation
- **Impact**: Attackers gain remote shell access to compromised servers
- **Status**: Under active exploitation in the wild

### Oracle Zero-Day Attack
- **Description**: Zero-day vulnerability in Oracle systems exploited by the Clop ransomware group
- **Impact**: Data theft and system compromise affecting Oracle customers including Harvard University
- **Status**: Actively exploited as part of broader campaign against Oracle customers

### Red Lion RTU Critical Vulnerabilities
- **Description**: Two critical security flaws in Red Lion Sixnet remote terminal unit products with CVSS 10.0 scores
- **Impact**: Could result in code execution and full industrial control system compromise
- **Status**: Vulnerabilities disclosed; patches available

### SAP NetWeaver Command Execution Vulnerability
- **Description**: Maximum-severity vulnerability in SAP NetWeaver AS Java allowing arbitrary command execution
- **Impact**: Complete server takeover without authentication required
- **Status**: Additional hardening measures released by SAP

## Affected Systems and Products

- **Adobe Experience Manager**: All versions affected by the critical 10.0 CVSS vulnerability
- **Microsoft Windows**: Every version ever shipped affected by at least one zero-day vulnerability
- **F5 BIG-IP**: Multiple product lines compromised with source code and zero-day vulnerabilities stolen
- **ICTBroadcast**: Autodialer software from ICT Innovations under active attack
- **Oracle Systems**: Multiple Oracle customers affected by zero-day exploitation campaign
- **Red Lion Sixnet RTUs**: Industrial remote terminal units with critical vulnerabilities
- **SAP NetWeaver AS Java**: Enterprise application server vulnerable to unauthenticated takeover
- **Visual Studio Code Extensions**: Over 100 VS Code extensions exposed access tokens creating supply chain risks
- **Android Systems**: Vulnerable to new Pixnapping attack stealing MFA codes and sensitive data

## Attack Vectors and Techniques

- **Cookie Exploitation**: Manipulation of authentication cookies to gain remote shell access on ICTBroadcast servers
- **Zero-Day Exploitation**: Nation-state actors leveraging previously unknown vulnerabilities in critical infrastructure
- **Supply Chain Attacks**: Malicious VS Code extensions targeting developers with cryptocurrency theft capabilities
- **Pixnapping Attack**: Side-channel attack stealing sensitive data pixel-by-pixel from Android applications without permissions
- **Ransomware Operations**: Clop group exploiting Oracle zero-days as part of broader data theft campaigns
- **Social Engineering**: Fake LastPass and Bitwarden breach alerts leading to PC hijacks
- **Industrial System Targeting**: Exploitation of SCADA and RTU systems for potential operational disruption

## Threat Actor Activities

- **Nation-State Actors**: Compromised F5 systems to steal BIG-IP source code and undisclosed vulnerabilities; attributed to sophisticated state-sponsored groups
- **Clop Ransomware Group**: Actively exploiting Oracle zero-day vulnerabilities in campaign against university and enterprise targets
- **Mysterious Elephant**: Cyber-espionage group targeting government and diplomatic entities in South Asia with custom sophisticated tools
- **Chinese APT Jewelbug**: Five-month infiltration of Russian IT service provider, expanding operations beyond Southeast Asia
- **Flax Typhoon**: Chinese APT group compromising ArcGIS geospatial mapping servers for stealth backdoor access
- **TigerJack**: Threat actor publishing malicious cryptocurrency-stealing extensions on VSCode marketplace and OpenVSX registry
- **Matthew D. Lane**: 19-year-old sentenced to four years in prison for PowerSchool cyberattack affecting millions of student records