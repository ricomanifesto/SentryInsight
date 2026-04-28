# Exploitation Report

Current threat landscape shows active exploitation across multiple vectors, with significant focus on supply chain attacks, social engineering campaigns, and exploitation of unpatched vulnerabilities. Notable activities include the GlassWorm v2 malware campaign targeting developer environments through malicious VS Code extensions, the emergence of the UNC6692 threat group using Microsoft Teams for initial access, and active exploitation of vulnerabilities in TrueConf video conferencing software by the PhantomCore hacktivist group. CISA has added four newly exploited vulnerabilities to its Known Exploited Vulnerabilities catalog, indicating active in-the-wild exploitation. Additionally, a sophisticated FIRESTARTER backdoor was discovered persisting on federal Cisco Firepower devices, demonstrating advanced persistent threat capabilities against critical infrastructure.

## Active Exploitation Details

### TrueConf Video Conferencing Vulnerabilities
- **Description**: Multiple vulnerabilities in TrueConf video conferencing software being exploited since September 2025
- **Impact**: Allows threat actors to breach Russian networks and gain unauthorized access to video conferencing infrastructure
- **Status**: Actively exploited by PhantomCore hacktivist group

### PhantomRPC Windows Privilege Escalation Flaw
- **Description**: Architectural weakness in Windows' Remote Procedure Call (RPC) mechanism that handles connections to unavailable services
- **Impact**: Enables local privilege escalation through five different exploit paths
- **Status**: Unpatched vulnerability with active exploitation potential

### CISA KEV Catalog Additions
- **Description**: Four vulnerabilities affecting SimpleHelp, Samsung MagicINFO 9 Server, and D-Link DIR-823X series routers
- **Impact**: Various attack vectors enabling unauthorized access and system compromise
- **Status**: Active exploitation confirmed, federal agencies must patch by May 2026

### FIRESTARTER Backdoor on Cisco Firepower
- **Description**: Sophisticated backdoor targeting federal Cisco Firepower devices running Adaptive Security Appliance (ASA) software
- **Impact**: Persistent access that survives security patches and firmware updates
- **Status**: Confirmed deployment on federal civilian agency infrastructure

## Affected Systems and Products

- **TrueConf Video Conferencing Software**: Russian networks and video conferencing infrastructure
- **Windows RPC Mechanism**: All Windows systems vulnerable to PhantomRPC privilege escalation
- **SimpleHelp Remote Access Software**: Systems using vulnerable versions
- **Samsung MagicINFO 9 Server**: Digital signage and display management systems
- **D-Link DIR-823X Series Routers**: Consumer and small business networking equipment
- **Cisco Firepower/ASA Devices**: Federal civilian agency security appliances
- **OpenVSX/VS Code Extensions**: Developer environments using malicious extensions
- **PyPI Python Packages**: Developer systems using compromised elementary-data package
- **Microsoft Teams**: Organizations using Teams for communication

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious VS Code extensions in OpenVSX repository delivering GlassWorm v2 malware
- **Package Repository Compromise**: Hijacking of popular Python packages with 1.1M+ monthly downloads to deliver infostealers
- **Social Engineering via Microsoft Teams**: UNC6692 using Teams messages to deploy Snow malware suite
- **SMS Blaster Devices**: Physical devices mimicking cellular towers to send phishing messages
- **Fake CAPTCHA IRSF Scams**: International Revenue Share Fraud campaigns using fraudulent verification prompts
- **Account Creation Abuse**: Exploiting Robinhood's account registration process to inject phishing content
- **Persistent Backdoor Deployment**: FIRESTARTER maintaining access through security updates and patches

## Threat Actor Activities

- **PhantomCore**: Pro-Ukrainian hacktivist group actively targeting Russian TrueConf servers since September 2025
- **UNC6692**: Newly identified threat group combining Microsoft Teams, AWS S3 buckets, and custom Snow malware in multipronged campaigns
- **GlassWorm Operators**: Persistent campaign operators using 73 "sleeper" extensions that activate malicious functionality after updates
- **ShinyHunters**: Extortion group responsible for ADT data breach affecting 5.5 million individuals
- **Silk Typhoon**: Chinese state-sponsored group with member extradited to US for cyberespionage operations
- **Myanmar Fraud Ring**: International financial fraud operation targeting US citizens with fake investment sites