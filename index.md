# Exploitation Report

The cybersecurity landscape is currently dominated by several critical exploitation activities targeting enterprise infrastructure. A maximum severity vulnerability in Fortra GoAnywhere MFT's License Servlet (CVE-2025-10035) poses immediate command injection risks, while active exploitation of Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428) has resulted in sophisticated malware deployments. Concurrently, Iranian state-sponsored groups are conducting targeted espionage campaigns against telecommunications companies, and the SystemBC malware botnet continues to compromise VPS systems for proxy operations. These threats are compounded by novel attack vectors including ChatGPT-based data exfiltration techniques and extensive phishing-as-a-service operations targeting hundreds of global brands.

## Active Exploitation Details

### Fortra GoAnywhere MFT License Servlet Vulnerability
- **Description**: A maximum severity command injection vulnerability in GoAnywhere Managed File Transfer software's License Servlet component
- **Impact**: Allows attackers to execute arbitrary commands on vulnerable systems, potentially leading to complete system compromise
- **Status**: Critical patch released by Fortra; exploitation highly dependent on internet exposure of vulnerable systems
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Security flaws in Ivanti Endpoint Manager Mobile that have been actively exploited to deploy malware
- **Impact**: Successful exploitation leads to deployment of sophisticated malware toolkits for persistent access and data exfiltration
- **Status**: Actively exploited in the wild with CISA publishing detailed malware analysis
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Attack Vector
- **Description**: A novel attack technique that exploits OpenAI's ChatGPT infrastructure to exfiltrate corporate data invisibly
- **Impact**: Enables data theft without leaving traces on enterprise systems, bypassing traditional monitoring solutions
- **Status**: Proof-of-concept demonstrated; organizations using ChatGPT integrations at risk

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component in managed file transfer solutions
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management platforms
- **OpenAI ChatGPT**: AI systems with enterprise integrations vulnerable to ShadowLeak techniques
- **Commercial VPS Systems**: Virtual private servers targeted by SystemBC malware operations
- **SonicWall MySonicWall**: Cloud backup service affecting firewall configuration data
- **Telecommunications Infrastructure**: European telecom companies targeted by UNC1549 operations
- **Transport for London Systems**: Critical infrastructure targeted in Scattered Spider attacks

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **Malware Deployment**: Custom toolkits deployed through Ivanti EPMM vulnerabilities for persistence
- **Social Engineering via LinkedIn**: UNC1549 using fake job offers to target telecommunications employees
- **ChatGPT Infrastructure Abuse**: ShadowLeak technique for invisible data exfiltration through AI platforms
- **VPS Compromise**: SystemBC malware targeting commercial virtual private servers for proxy operations
- **Phishing-as-a-Service**: Lighthouse and Lucid platforms enabling large-scale phishing operations
- **Cloud Service Breach**: Unauthorized access to MySonicWall backup configurations

## Threat Actor Activities

- **UNC1549 (Iranian APT)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware, demonstrating sophisticated targeting of critical infrastructure
- **Scattered Spider**: Teen members arrested in connection with August 2024 Transport for London cyberattack, highlighting the group's continued focus on critical infrastructure
- **Gamaredon and Turla Collaboration**: Russian hacking groups working together to deploy Kazuar backdoor against Ukrainian entities, representing unprecedented cooperation between state-sponsored groups
- **SystemBC Operators**: Maintaining an average of 1,500 compromised VPS systems daily across 80 command-and-control servers for REM Proxy operations
- **Lighthouse and Lucid PhaaS Operators**: Orchestrating campaigns across 17,500 phishing domains targeting 316 brands in 74 countries
- **SonicWall Breach Actors**: Successfully compromised MySonicWall cloud service, exposing firewall backup configurations for under 5% of customers