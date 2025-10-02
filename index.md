# Exploitation Report

Recent security analysis reveals a diverse landscape of active exploitation targeting critical enterprise infrastructure and consumer applications. Key exploitation activities include ransomware attacks on dealership software providers affecting 766,000 customers, a new Android banking trojan called Klopatra infecting over 3,000 devices across Europe through VNC remote access capabilities, and sophisticated attacks against Milesight industrial cellular routers being exploited for SMS phishing campaigns. Hardware-level vulnerabilities are also being exploited, with researchers demonstrating attacks against Intel SGX security features and cloud processor protections. Additionally, China-linked APT groups have been actively exploiting VMware vulnerabilities for nearly a year, while nation-state actors continue deploying advanced backdoors like CABINETRAT through targeted campaigns.

## Active Exploitation Details

### Milesight Industrial Cellular Router Exploitation
- **Description**: Unknown threat actors are actively exploiting vulnerabilities in Milesight industrial cellular routers to send SMS messages as part of smishing campaigns
- **Impact**: Attackers can send fraudulent SMS messages through compromised routers, targeting users with phishing content
- **Status**: Ongoing exploitation since at least February 2022, primarily affecting European users

### VMware Privilege Escalation Vulnerability
- **Description**: China-linked attackers have been exploiting a privilege escalation vulnerability in VMware and other software platforms
- **Impact**: Allows attackers to escalate privileges and gain elevated access to compromised systems
- **Status**: Actively exploited for nearly a year before discovery and patching

### Intel SGX Security Bypass
- **Description**: Researchers demonstrated the WireTap attack that extracts Intel SGX ECDSA keys through DDR4 memory-bus interposition
- **Impact**: Compromises the security guarantees of Intel's Software Guard Extensions, potentially exposing encrypted data
- **Status**: Proof-of-concept demonstrated, affects Intel SGX implementations

### Battering RAM Attack on Cloud Processors
- **Description**: Academic researchers developed a $50 hardware attack that bypasses latest defenses on Intel and AMD cloud processors
- **Impact**: Breaks confidential computing protections, potentially exposing encrypted data in cloud environments
- **Status**: Successfully demonstrated attack method affecting modern processor security features

### OneLogin Identity Management Vulnerability
- **Description**: High-severity security flaw in One Identity OneLogin IAM solution allows exploitation through API keys
- **Impact**: Attackers can steal OpenID Connect (OIDC) secrets and impersonate applications
- **Status**: Security flaw disclosed and requires patching

### Red Hat OpenShift AI Infrastructure Takeover
- **Description**: Severe security flaw allows attackers to escalate privileges in Red Hat OpenShift AI service
- **Impact**: Complete infrastructure takeover possible under certain conditions
- **Status**: Critical vulnerability disclosed, affects hybrid cloud environments

## Affected Systems and Products

- **Motility Software Solutions**: Dealership management software (DMS) affected by ransomware attack
- **Adobe Analytics**: Customer tracking data leaked between tenant instances due to ingestion bug
- **Microsoft Outlook Classic**: Email client experiencing crash-on-launch issues requiring support intervention
- **Android Devices**: Over 3,000 devices infected with Klopatra banking trojan across Spain and Italy
- **Milesight Routers**: Industrial cellular routers compromised for SMS phishing campaigns
- **Intel SGX Systems**: Processors with Software Guard Extensions vulnerable to WireTap attack
- **VMware Environments**: Various VMware products affected by privilege escalation exploits
- **Cloud Infrastructure**: Intel and AMD processors in cloud environments vulnerable to Battering RAM attack
- **OneLogin IAM**: Identity and Access Management solution with API key vulnerability
- **Red Hat OpenShift AI**: Hybrid cloud AI platform susceptible to privilege escalation

## Attack Vectors and Techniques

- **Ransomware Deployment**: Direct attacks on software providers to access customer databases and systems
- **VNC Remote Access**: Klopatra trojan uses hidden VNC connections to provide hands-on device control to attackers
- **SMS Phishing Campaigns**: Exploitation of compromised routers to send fraudulent messages to mobile users
- **Hardware Interposition**: Physical attacks using DDR4 memory-bus interposers to extract encryption keys
- **API Key Exploitation**: Abuse of legitimate API access to steal authentication secrets and impersonate applications
- **XLL Add-ins Distribution**: CABINETRAT backdoor spread through malicious Excel add-ins via compressed archives
- **Privilege Escalation**: Systematic exploitation of elevation vulnerabilities in enterprise software platforms
- **Memory-based Attacks**: Hardware-level exploitation targeting processor security features and encrypted memory

## Threat Actor Activities

- **China-linked APT Groups**: Actively exploiting VMware vulnerabilities for nearly a year, demonstrating persistence and advanced capabilities against enterprise targets
- **Unknown European Actors**: Operating Milesight router exploitation campaign since February 2022, focusing on SMS-based phishing across European countries
- **Ransomware Operators**: Targeting software service providers like Motility to maximize impact across customer bases, affecting hundreds of thousands of users
- **Klopatra Campaign**: Banking trojan operators targeting over 3,000 Android devices primarily in Spain and Italy through disguised IPTV and VPN applications
- **CABINETRAT Operators**: Conducting targeted attacks in Ukraine using backdoor malware distributed through compressed archives containing XLL add-ins
- **Phantom Taurus APT**: New China-linked group demonstrating deep Windows environment knowledge with advanced fileless backdoors like IIServerCore that execute in memory