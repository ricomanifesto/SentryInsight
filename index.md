# Exploitation Report

Critical exploitation activity is currently centered around several high-severity vulnerabilities and sophisticated threat actor campaigns. The most urgent concern involves a maximum severity command injection flaw in Fortra's GoAnywhere MFT software (CVE-2025-10035), which carries a CVSS score of 10.0 and enables arbitrary command execution. Simultaneously, CISA has exposed active exploitation of Ivanti Endpoint Manager Mobile vulnerabilities (CVE-2025-4427 and CVE-2025-4428) with custom malware deployments. Iranian state-sponsored groups continue aggressive campaigns against telecommunications infrastructure, while the SystemBC malware operates a massive proxy botnet with 1,500 daily victims across 80 command-and-control servers.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows attackers to execute arbitrary commands on vulnerable systems
- **Impact**: Complete system compromise, unauthorized command execution, and potential lateral movement within enterprise networks
- **Status**: Actively exploitable with patches available; exploitation highly dependent on Internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile that enable malware deployment and system compromise
- **Impact**: Successful deployment of two distinct malware strains, allowing persistent access and data exfiltration
- **Status**: Actively exploited in the wild with custom malware kits identified by CISA
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Attack
- **Description**: A novel attack technique that exploits OpenAI's infrastructure to invisibly exfiltrate company data through ChatGPT interactions
- **Impact**: Covert data theft with no trace left on enterprise systems, bypassing traditional security monitoring
- **Status**: Active attack vector with demonstrated capability for email theft and corporate data exfiltration

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component in managed file transfer systems, particularly those exposed to the Internet
- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management platforms vulnerable to malware injection
- **OpenAI ChatGPT**: Corporate environments using ChatGPT for business operations vulnerable to data exfiltration
- **SonicWall MySonicWall**: Cloud backup service exposing firewall configuration files for under 5% of customer base
- **Commercial VPS Systems**: Virtual private servers targeted by SystemBC malware for proxy botnet operations
- **European Telecommunications**: Infrastructure targeted by Iranian APT groups across 11 organizations
- **Transport for London**: Critical infrastructure compromised by Scattered Spider threat actors

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT's License Servlet to execute arbitrary system commands
- **Malware Deployment**: Custom malware kits deployed against Ivanti EPMM vulnerabilities for persistent access
- **Social Engineering**: LinkedIn job lures used by UNC1549 to target telecommunications employees
- **AI Infrastructure Abuse**: Leveraging ChatGPT's processing capabilities to covertly exfiltrate sensitive corporate data
- **Proxy Botnet Operations**: SystemBC malware converting infected VPS systems into traffic routing infrastructure
- **Phishing-as-a-Service**: Lighthouse and Lucid PhaaS platforms generating over 17,500 malicious domains targeting 316 brands
- **Cloud Service Compromise**: Unauthorized access to SonicWall's MySonicWall backup service exposing configuration data

## Threat Actor Activities

- **UNC1549 (Iranian APT)**: Conducting sophisticated espionage campaign against European telecommunications companies, successfully compromising 34 devices across 11 organizations using LinkedIn recruitment lures and MINIBIKE malware
- **Scattered Spider**: Teen hackers arrested in connection with August 2024 Transport for London cyberattack, demonstrating continued targeting of critical infrastructure
- **Gamaredon and Turla**: Russian state-sponsored groups collaborating to deploy Kazuar backdoor against Ukrainian entities, representing unprecedented cooperation between APT groups
- **SystemBC Operators**: Maintaining large-scale proxy botnet with approximately 1,500 daily victims across 80 C2 servers, primarily targeting commercial VPS infrastructure
- **PhaaS Operators**: Lighthouse and Lucid services enabling widespread phishing campaigns across 74 countries, targeting major brands and financial institutions