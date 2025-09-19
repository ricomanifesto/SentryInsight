# Exploitation Report

Critical vulnerabilities are actively threatening enterprise environments, with the most severe being a maximum CVSS 10.0 command injection flaw in Fortra GoAnywhere MFT (CVE-2025-10035) requiring immediate patching. Simultaneously, threat actors are exploiting Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428) to deploy sophisticated malware campaigns. Iranian state-sponsored groups continue targeting telecommunications infrastructure through social engineering attacks, while ransomware operators maintain high success rates despite known defensive technologies. Additional concerns include a novel ChatGPT attack vector enabling invisible data exfiltration and the compromise of SonicWall's cloud backup infrastructure exposing firewall configurations.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity command injection vulnerability in GoAnywhere MFT's License Servlet component allowing arbitrary command execution
- **Impact**: Attackers can execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Critical patch available, exploitation highly dependent on internet exposure
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Multiple vulnerabilities in Ivanti Endpoint Manager Mobile being actively exploited in the wild
- **Impact**: Successful exploitation allows deployment of custom malware strains and persistent network access
- **Status**: Under active exploitation with malware deployment confirmed by CISA
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Attack
- **Description**: A novel attack vector exploiting ChatGPT's infrastructure to invisibly exfiltrate company data
- **Impact**: Data theft via OpenAI's infrastructure leaving no trace on enterprise systems
- **Status**: Active attack technique identified, mitigation strategies under development

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component in internet-exposed installations
- **Ivanti Endpoint Manager Mobile (EPMM)**: All versions affected by the identified vulnerabilities
- **OpenAI ChatGPT Infrastructure**: Enterprise integrations vulnerable to ShadowLeak technique
- **SonicWall MySonicWall Service**: Cloud backup infrastructure affecting under 5% of customer base
- **European Telecommunications Companies**: 34 devices across 11 organizations compromised
- **Virtual Private Servers (VPS)**: Commercial VPS systems targeted by SystemBC malware
- **Transport for London Systems**: Infrastructure compromised in August 2024 attack

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of GoAnywhere MFT's License Servlet for arbitrary command execution
- **Social Engineering via LinkedIn**: UNC1549 using fake job opportunities to target telecommunications employees
- **Malware Deployment**: Custom malware strains deployed through Ivanti EPMM vulnerabilities
- **AI Infrastructure Abuse**: ShadowLeak technique using ChatGPT for invisible data exfiltration
- **Proxy Network Operations**: SystemBC malware converting infected VPS systems into proxy infrastructure
- **Phishing-as-a-Service**: 17,500 domains targeting 316 brands across 74 countries
- **Configuration File Theft**: SonicWall cloud backup breach exposing firewall configurations

## Threat Actor Activities

- **UNC1549 (Iran-nexus)**: Sophisticated LinkedIn-based social engineering targeting European telecommunications, deploying MINIBIKE malware across 34 devices in 11 organizations
- **Scattered Spider**: Two teenagers arrested in UK connection with Transport for London cyberattack, demonstrating continued youth involvement in major infrastructure attacks
- **Gamaredon and Turla Collaboration**: Russian state groups working together to deploy Kazuar backdoor against Ukrainian entities
- **SystemBC Operators**: Maintaining 1,500 daily VPS victims across 80 command and control servers for proxy network operations
- **Lighthouse and Lucid PhaaS**: Operating massive phishing infrastructure with 17,500 domains targeting global brands
- **SonicWall Attackers**: Successful breach of MySonicWall cloud service exposing customer firewall backup configurations