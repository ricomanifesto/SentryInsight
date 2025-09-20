# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with the most severe being a maximum severity command injection flaw in Fortra GoAnywhere MFT (CVE-2025-10035) and vulnerabilities in Ivanti Endpoint Manager Mobile (CVE-2025-4427 and CVE-2025-4428). Nation-state actors, particularly Iranian groups, are conducting sophisticated campaigns targeting telecommunications and satellite companies, while malware operations like SystemBC are powering extensive proxy networks. Additionally, new attack vectors including ShadowLeak attacks against ChatGPT and widespread phishing-as-a-service operations are expanding the threat landscape.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows command injection attacks
- **Impact**: Enables attackers to execute arbitrary commands on vulnerable systems
- **Status**: Critical patch available; exploitation highly dependent on Internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile that are being actively exploited with custom malware
- **Impact**: Allows deployment of specialized malware strains for persistent access and lateral movement
- **Status**: Active exploitation detected by CISA with custom malware deployment
- **CVE ID**: CVE-2025-4427 and CVE-2025-4428

### ShadowLeak ChatGPT Attack
- **Description**: A novel attack technique that exploits loopholes in ChatGPT to exfiltrate company data through OpenAI's infrastructure
- **Impact**: Enables invisible data theft without leaving traces on enterprise systems
- **Status**: Active exploitation technique identified

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection
- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple vulnerabilities being exploited with custom malware
- **OpenAI ChatGPT**: Vulnerable to ShadowLeak data exfiltration attacks
- **Commercial VPS Systems**: Targeted by SystemBC malware for proxy network creation
- **Telecommunications Infrastructure**: Targeted by Iranian APT groups across European companies
- **SonicWall MySonicWall Service**: Breached with firewall configuration backup files exposed
- **Transport for London Systems**: Compromised in August 2024 attack by Scattered Spider group

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **LinkedIn Social Engineering**: UNC1549 using fake job lures to target telecommunications employees
- **MINIBIKE Malware**: Custom malware deployed by Iranian actors for persistent access
- **Proxy Network Creation**: SystemBC malware converting infected VPS systems into proxy infrastructure
- **Phishing-as-a-Service (PhaaS)**: Large-scale operations using 17,500+ domains targeting 316 brands across 74 countries
- **Data Exfiltration via AI**: ShadowLeak technique using OpenAI infrastructure for invisible data theft
- **Fake FBI Portals**: Cybercriminals impersonating FBI's Internet Crime Complaint Center for malicious activities

## Threat Actor Activities

- **UNC1549 (Iranian APT)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Gamaredon and Turla**: Russian hacking groups collaborating to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in connection with Transport for London cyberattack in August 2024
- **SystemBC Operators**: Maintaining average of 1,500 daily VPS victims across 80 C2 servers for REM Proxy network
- **Lighthouse and Lucid PhaaS**: Operating massive phishing infrastructure targeting global brands
- **Charming Kitten Subgroup**: Conducting sophisticated bespoke cyberattacks against telecommunications and satellite companies