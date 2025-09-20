# Exploitation Report

Critical vulnerabilities are currently being exploited across multiple enterprise systems, with the most severe being a maximum severity command injection flaw in Fortra GoAnywhere MFT tracked as CVE-2025-10035. Threat actors are actively exploiting vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) tracked as CVE-2025-4427 and CVE-2025-4428, deploying sophisticated malware payloads. Iranian state-sponsored groups continue their aggressive targeting of telecommunications and satellite companies, while SystemBC malware operators maintain extensive proxy networks compromising over 1,500 VPS systems daily. Additionally, novel attack techniques like the ShadowLeak method against ChatGPT demonstrate evolving threats in AI-powered environments.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere MFT's License Servlet that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Complete system compromise and command execution capabilities for attackers
- **Status**: Actively exploitable, patches available from Fortra
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Two distinct vulnerabilities in Ivanti Endpoint Manager Mobile being exploited to deploy malware payloads
- **Impact**: System compromise and malware deployment on enterprise mobile management systems
- **Status**: Active exploitation confirmed by CISA with deployed malware strains discovered
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Attack
- **Description**: A novel attack technique targeting ChatGPT that allows invisible exfiltration of company data through OpenAI's infrastructure
- **Impact**: Covert data exfiltration with no traces left on enterprise systems
- **Status**: Newly discovered attack method being actively researched

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component affected across all exposed installations
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile management systems vulnerable to malware deployment
- **OpenAI ChatGPT**: AI systems susceptible to ShadowLeak data exfiltration techniques
- **Commercial VPS Systems**: Over 1,500 systems daily compromised by SystemBC malware
- **SonicWall MySonicWall Service**: Cloud backup systems breached affecting firewall configuration data
- **Telecommunications Infrastructure**: European telecom companies targeted by Iranian APT groups
- **Satellite Companies**: Communication infrastructure under active threat from state-sponsored actors

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT License Servlet for arbitrary command execution
- **LinkedIn Social Engineering**: UNC1549 using fake job opportunities to target telecommunications employees
- **MINIBIKE Malware Deployment**: Custom malware deployed by Iranian threat actors against telecom infrastructure
- **Proxy Network Operations**: SystemBC malware creating proxy highways through compromised VPS systems
- **AI Infrastructure Abuse**: ShadowLeak technique leveraging ChatGPT for covert data exfiltration
- **Phishing-as-a-Service**: Lighthouse and Lucid PhaaS platforms targeting 316 brands across 74 countries
- **Credential Harvesting**: Fake FBI crime reporting portals used to collect user credentials

## Threat Actor Activities

- **UNC1549 (Iranian APT)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn lures and MINIBIKE malware
- **Gamaredon and Turla Collaboration**: Russian hacking groups working together to deploy Kazuar backdoor against Ukrainian entities
- **Scattered Spider**: Teen members arrested in UK for Transport for London cyberattack in August 2024
- **SystemBC Operators**: Maintaining REM Proxy network with approximately 1,500 daily VPS victims across 80 command and control servers
- **PhaaS Operators**: Lighthouse and Lucid services managing over 17,500 phishing domains targeting global brands
- **Iranian State APT**: Performing highly bespoke attacks against telecommunications and satellite companies for intelligence gathering