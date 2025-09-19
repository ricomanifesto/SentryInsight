# Exploitation Report

Critical exploitation activity spans multiple attack vectors, with threat actors leveraging sophisticated techniques ranging from zero-day vulnerabilities in enterprise software to advanced phishing campaigns and malware operations. Notable campaigns include Iranian state-sponsored groups targeting telecommunications infrastructure, Russian ransomware operations utilizing new malware loaders, and widespread exploitation of Ivanti EPMM vulnerabilities. The landscape is further complicated by emerging threats such as AI-powered phishing services and proxy botnets compromising commercial VPS systems.

## Active Exploitation Details

### Ivanti EPMM Vulnerabilities
- **Description**: Critical vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) being actively exploited by threat actors
- **Impact**: Complete system compromise, malware deployment, and persistent access to enterprise mobile device management infrastructure
- **Status**: CISA has published analysis of malware deployed in active attacks
- **CVE ID**: CVE-2025-4427 and CVE-2025-4428

### GoAnywhere MFT License Servlet Vulnerability
- **Description**: Maximum severity command injection vulnerability in Fortra's GoAnywhere Managed File Transfer License Servlet component
- **Impact**: Remote code execution and arbitrary command execution on affected file transfer systems
- **Status**: Critical patch released by Fortra with CVSS score of 10.0
- **CVE ID**: Referenced but specific CVE number not provided in full

### Azure Entra ID Critical Vulnerability
- **Description**: Critical identity and access management flaw in Microsoft's Azure Entra ID platform
- **Impact**: Could have led to catastrophic attacks affecting cloud identity management systems
- **Status**: Fixed prior to public disclosure, highlighting ongoing Microsoft IAM security issues

## Affected Systems and Products

- **Ivanti EPMM**: Enterprise mobile device management platforms experiencing active malware deployment
- **GoAnywhere MFT**: Managed file transfer systems vulnerable to command injection attacks
- **Microsoft Azure Entra ID**: Cloud identity and access management infrastructure
- **SonicWall MySonicWall**: Firewall backup configuration services affecting under 5% of customer base
- **Commercial VPS Systems**: Virtual private servers being compromised for proxy botnet operations
- **Telecommunications Infrastructure**: European telecom companies targeted by Iranian state actors
- **Transport for London**: Public transportation systems compromised by Scattered Spider group

## Attack Vectors and Techniques

- **LinkedIn Social Engineering**: UNC1549 using fake job offers to target telecommunications employees
- **MINIBIKE Malware**: Custom malware deployed by Iranian actors for persistent access
- **SystemBC Proxy Botnet**: Malware converting infected VPS systems into proxy networks with 1,500 daily victims
- **CountLoader**: Multi-version malware loader used by Russian ransomware gangs to deploy Cobalt Strike
- **Kazuar Backdoor**: Advanced persistent threat tool deployed through Russian hacker collaboration
- **PhaaS Campaigns**: Phishing-as-a-Service operations using Lighthouse and Lucid platforms targeting 17,500 domains
- **Fake FBI Portals**: Cybercriminals impersonating FBI Internet Crime Complaint Center websites

## Threat Actor Activities

- **UNC1549 (Iranian APT)**: Successfully infiltrated 34 devices across 11 European telecommunications organizations using sophisticated social engineering and custom malware
- **Gamaredon and Turla (Russian APTs)**: Collaborative operations targeting Ukrainian entities with Kazuar backdoor deployment
- **Scattered Spider**: Teen hackers linked to August 2024 Transport for London cyber attack, with two members arrested in the UK
- **Russian Ransomware Gangs**: Utilizing CountLoader malware for broader operational capabilities and post-exploitation tool deployment
- **REM Proxy Operators**: Managing botnet of 1,500 daily VPS victims across 80 command and control servers
- **PhaaS Operators**: Running Lighthouse and Lucid services targeting 316 brands across 74 countries with advanced phishing infrastructure