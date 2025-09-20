# Exploitation Report

The current threat landscape is dominated by several critical vulnerabilities under active exploitation, with particular emphasis on a maximum severity command injection flaw in Fortra GoAnywhere MFT (CVE-2025-10035) and ongoing attacks targeting Ivanti EPMM systems (CVE-2025-4427 and CVE-2025-4428). Threat actors are leveraging sophisticated techniques including malware deployment, proxy botnets, and targeted campaigns against telecommunications infrastructure. Notable incidents include Iranian state-sponsored groups conducting bespoke attacks against European telecommunications companies, the exposure of SonicWall firewall configuration data, and the arrest of Scattered Spider members linked to major infrastructure attacks.

## Active Exploitation Details

### Fortra GoAnywhere MFT Command Injection Vulnerability
- **Description**: A maximum severity vulnerability in GoAnywhere Managed File Transfer software's License Servlet component that allows arbitrary command execution
- **Impact**: Attackers can execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Critical patch released by Fortra; exploitation highly dependent on internet exposure of systems
- **CVE ID**: CVE-2025-10035

### Ivanti EPMM Vulnerabilities
- **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile that are being actively exploited with custom malware deployment
- **Impact**: Complete compromise of affected mobile device management systems with deployment of sophisticated malware strains
- **Status**: Under active exploitation with CISA releasing detailed malware analysis
- **CVE ID**: CVE-2025-4427, CVE-2025-4428

### ShadowLeak ChatGPT Attack
- **Description**: A novel attack technique that exploits OpenAI's infrastructure to exfiltrate company data invisibly
- **Impact**: Enables data theft through ChatGPT interactions without leaving traces on enterprise systems
- **Status**: Active attack vector being used to steal sensitive emails and corporate data

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: License Servlet component vulnerable to command injection attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Multiple vulnerabilities allowing malware deployment
- **OpenAI ChatGPT Infrastructure**: Being leveraged for invisible data exfiltration attacks
- **SonicWall MySonicWall Service**: Firewall configuration backup files exposed affecting under 5% of customers
- **European Telecommunications Companies**: 34 devices across 11 organizations compromised by Iranian threat actors
- **Commercial VPS Systems**: Approximately 1,500 systems daily infected with SystemBC malware for proxy operations

## Attack Vectors and Techniques

- **Command Injection**: Exploiting web application input validation flaws to execute arbitrary system commands
- **Social Engineering via LinkedIn**: Iranian threat actors using fake job opportunities to deliver MINIBIKE malware
- **Malware-as-a-Proxy**: SystemBC malware converting infected VPS systems into proxy infrastructure with 80 C2 servers
- **Phishing-as-a-Service (PhaaS)**: Lighthouse and Lucid platforms facilitating 17,500 phishing domains targeting 316 brands across 74 countries
- **AI Infrastructure Exploitation**: Using ChatGPT's infrastructure as a covert channel for data exfiltration
- **Configuration Data Theft**: Accessing cloud backup services to obtain sensitive firewall configurations

## Threat Actor Activities

- **UNC1549 (Iranian State-Sponsored)**: Conducting sophisticated espionage campaigns against European telecommunications companies using LinkedIn job lures and custom MINIBIKE malware, successfully compromising 34 devices across 11 organizations
- **Gamaredon and Turla Collaboration**: Russian hacking groups working together to deploy Kazuar backdoor against Ukrainian entities, representing unprecedented cooperation between state-sponsored groups
- **Scattered Spider**: Two teenage members arrested in the UK for their involvement in the August 2024 Transport for London cyberattack, highlighting the group's continued targeting of critical infrastructure
- **SystemBC Operators**: Maintaining a sophisticated proxy botnet with approximately 1,500 daily victims across commercial VPS systems, providing anonymization services for criminal activities
- **Phishing-as-a-Service Providers**: Operating Lighthouse and Lucid platforms that have created over 17,500 malicious domains targeting major brands globally