# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with particularly concerning developments in hardware security bypass techniques and widespread exploitation of network infrastructure. Researchers have demonstrated sophisticated attacks against Intel SGX and cloud confidential computing protections using hardware-based methods, while threat actors are actively compromising industrial routers for SMS-based phishing campaigns and exploiting Cisco firewall vulnerabilities affecting nearly 50,000 devices. New banking trojans and nation-state malware campaigns are targeting critical infrastructure and financial institutions, while identity management systems face significant security flaws that could enable application impersonation and privilege escalation.

## Active Exploitation Details

### Cisco ASA and FTD Firewall Vulnerabilities
- **Description**: Two vulnerabilities in Cisco Adaptive Security Appliance (ASA) and Firewall Threat Defense (FTD) appliances are being actively exploited by hackers
- **Impact**: Attackers can compromise network security appliances and gain unauthorized access to protected networks
- **Status**: Actively exploited with approximately 50,000 devices exposed on the public web remaining vulnerable

### WireTap Attack on Intel SGX
- **Description**: Hardware-based attack using a DDR4 memory-bus interposer to extract ECDSA keys from Intel Software Guard eXtensions (SGX)
- **Impact**: Complete compromise of SGX security guarantees, allowing extraction of cryptographic keys and sensitive data from supposedly secure enclaves
- **Status**: Proof-of-concept demonstrated by academic researchers

### Battering RAM Attack on Cloud Security
- **Description**: A $50 hardware attack that breaks through Intel and AMD processor technologies designed to protect encrypted data in memory during cloud computing
- **Impact**: Bypasses confidential computing protections, allowing attackers to access encrypted data stored in memory
- **Status**: Demonstrated attack method affecting modern cloud security implementations

### Milesight Router Exploitation for SMS Phishing
- **Description**: Unknown threat actors are compromising Milesight industrial cellular routers to conduct SMS-based phishing campaigns
- **Impact**: Enables large-scale smishing attacks using legitimate network infrastructure to bypass security controls
- **Status**: Ongoing campaign targeting European users since at least February 2022

### VMware Privilege Escalation Vulnerability
- **Description**: A seemingly benign privilege escalation flaw in VMware software that has been exploited by China-linked attackers
- **Impact**: Allows attackers to gain elevated privileges within virtualized environments
- **Status**: Exploited for nearly a year before discovery and patching

### Western Digital My Cloud Command Injection
- **Description**: Critical vulnerability in WD My Cloud NAS models allowing remote command injection
- **Impact**: Attackers can execute arbitrary system commands remotely on affected network-attached storage devices
- **Status**: Critical severity vulnerability with firmware updates released

### Red Hat OpenShift AI Infrastructure Takeover
- **Description**: Severe security flaw in Red Hat OpenShift AI service enabling privilege escalation
- **Impact**: Complete infrastructure takeover under certain conditions in hybrid cloud environments
- **Status**: Disclosed vulnerability affecting OpenShift AI deployments

### OneLogin OIDC Security Flaw
- **Description**: High-severity vulnerability in One Identity OneLogin IAM solution affecting OpenID Connect implementations
- **Impact**: Exposure of sensitive OIDC secrets and potential application impersonation capabilities
- **Status**: Disclosed vulnerability in identity and access management platform

## Affected Systems and Products

- **Cisco ASA/FTD Firewalls**: Approximately 50,000 devices exposed on public internet remain vulnerable to active exploitation
- **Intel SGX Processors**: All Intel processors with Software Guard eXtensions affected by WireTap hardware attack
- **Intel/AMD Cloud Processors**: Modern processors using confidential computing technologies vulnerable to Battering RAM attack
- **Milesight Industrial Routers**: Cellular router models being exploited for SMS phishing campaigns
- **VMware Virtualization Products**: Multiple VMware software products affected by privilege escalation vulnerability
- **Western Digital My Cloud**: Multiple NAS models vulnerable to remote command injection
- **Red Hat OpenShift AI**: AI service deployments in hybrid cloud environments at risk
- **OneLogin IAM Platform**: Identity and Access Management solution with OIDC implementation flaws
- **Android Devices**: Over 3,000 devices infected with Klopatra banking trojan, primarily in Spain and Italy

## Attack Vectors and Techniques

- **Hardware Memory-Bus Interception**: Physical interposer devices targeting DDR4 memory buses to extract cryptographic keys
- **SMS-based Phishing (Smishing)**: Compromised industrial routers used to send legitimate-appearing SMS messages for credential theft
- **Banking Trojan with Hidden VNC**: Klopatra malware uses concealed VNC functionality to remotely control infected smartphones
- **Fileless Backdoor Execution**: IIServerCore backdoor executes entirely in memory to evade detection systems
- **PDF-based Phishing**: MatrixPDF toolkit converts ordinary PDFs into interactive lures that bypass email security
- **XLL Add-in Malware**: CABINETRAT backdoor distributed through Excel add-in files via Signal messaging platform
- **Remote Command Injection**: Direct exploitation of web interfaces in network-attached storage devices
- **Privilege Escalation**: Exploitation of virtualization software flaws to gain elevated system access

## Threat Actor Activities

- **China-linked APT Groups**: Multiple sophisticated campaigns targeting government and telecommunications infrastructure across Africa, Middle East, and Asia
- **Phantom Taurus**: New China-aligned nation-state actor using advanced stealth malware including fileless backdoors against government targets
- **Unknown European SMS Threat Actors**: Ongoing smishing campaign leveraging compromised industrial routers since February 2022
- **Banking Trojan Operators**: Klopatra malware campaign primarily targeting Spanish and Italian users with over 3,000 infections
- **Ukrainian-targeted Attackers**: CABINETRAT backdoor campaign observed in September 2025 using Signal messaging for malware distribution
- **Academic Researchers**: Multiple university teams demonstrating critical hardware-based attacks against modern security technologies