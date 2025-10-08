# Exploitation Report

Critical exploitation activity is dominated by several high-severity vulnerabilities being actively exploited in the wild. The most significant threats include a 13-year-old Redis flaw with a maximum CVSS 10.0 score enabling remote code execution, an Oracle E-Business Suite zero-day exploited by the Clop ransomware gang since August for data theft operations, and CVE-2025-10035 affecting Fortra GoAnywhere being exploited by Medusa ransomware actors. These vulnerabilities represent immediate risks to organizations, with threat actors successfully leveraging them for ransomware deployment, data exfiltration, and complete system compromise across cloud and enterprise environments.

## Active Exploitation Details

### Redis Remote Code Execution Vulnerability
- **Description**: A 13-year-old maximum-severity security flaw in Redis in-memory database software that enables remote code execution under certain circumstances
- **Impact**: Attackers can achieve full host takeover with complete system compromise. Over 300,000 Redis instances are currently exposed to this vulnerability
- **Status**: Recently disclosed by Redis with patches available. Dubbed "RediShell" by researchers due to its shell access capabilities
- **CVE ID**: CVSS 10.0 rated vulnerability (specific CVE number not provided in source)

### Oracle E-Business Suite Zero-Day
- **Description**: A critical zero-day vulnerability in Oracle E-Business Suite (EBS) that has been actively exploited for data theft operations
- **Impact**: Enables unauthorized access to sensitive business data and facilitates large-scale data exfiltration campaigns
- **Status**: Exploited in the wild since at least early August 2025 by the Clop ransomware gang. Patch status unclear as this remains a zero-day
- **CVE ID**: Not specified in available reporting

### Fortra GoAnywhere Critical Flaw
- **Description**: A critical vulnerability in Fortra GoAnywhere file transfer software that requires exploitation of a private key
- **Impact**: Allows threat actors to gain unauthorized access to file transfer systems and deploy ransomware
- **Status**: Actively exploited by Medusa ransomware group (Storm-1175). Method of private key acquisition remains unclear to researchers
- **CVE ID**: CVE-2025-10035

### Figma MCP Remote Code Execution
- **Description**: A severe vulnerability in the figma-developer-mcp Model Context Protocol (MCP) server that allows attackers to achieve code execution
- **Impact**: Remote code execution capabilities that could lead to system compromise
- **Status**: Now patched following responsible disclosure by cybersecurity researchers
- **CVE ID**: Not specified in available reporting

## Affected Systems and Products

- **Redis In-Memory Database**: All versions containing the 13-year-old flaw, with over 300,000 exposed instances globally
- **Oracle E-Business Suite (EBS)**: Specific versions targeted in Clop zero-day exploitation campaign
- **Fortra GoAnywhere**: File transfer software affected by critical vulnerability requiring private key exploitation
- **Figma MCP Server**: Model Context Protocol server implementations in development environments
- **Salesforce Customer Systems**: Impacted by widespread data theft attacks affecting multiple customers
- **DraftKings Accounts**: Sports betting platform accounts compromised through credential stuffing attacks
- **Asahi Brewery Systems**: Japanese brewery systems affected by ransomware causing operational disruptions
- **Google Workspace Integrations**: OAuth integrations vulnerable to trusted integration bypass attacks
- **Avnet Systems**: Electronic components distributor systems breached with encrypted data stolen

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Clop ransomware gang leveraging unpatched Oracle EBS vulnerability for sustained data theft campaigns
- **Remote Code Execution**: Redis vulnerability enabling complete host takeover through database software exploitation
- **Credential Stuffing**: Large-scale automated attacks against DraftKings customer accounts using reused credentials
- **Social Engineering**: Job-themed phishing campaigns targeting influencers and professionals with fake Tesla and Red Bull opportunities
- **Voice Phishing (Vishing)**: ShinyHunters group using voice-based social engineering to steal over one billion records from Salesforce customers
- **Supply Chain Attacks**: Targeting trusted OAuth integrations to bypass traditional security controls in Google Workspace environments
- **ASCII Smuggling**: New attack technique against Google Gemini AI using hidden ASCII characters to manipulate AI responses
- **Ransomware-as-a-Service**: Strategic alliance formation between LockBit, Qilin, and DragonForce groups expanding operational capabilities
- **Open Source Tool Weaponization**: China-nexus actors leveraging Nezha remote monitoring tool for malicious purposes

## Threat Actor Activities

- **Clop Ransomware Gang**: Conducting sustained data theft operations since early August using Oracle EBS zero-day vulnerability for unauthorized access to enterprise systems
- **ShinyHunters Cybercriminal Group**: Operating broad corporate extortion campaigns using voice phishing attacks, successfully stealing over one billion records from Salesforce customers and launching public data leak threats
- **Medusa Ransomware Group (Storm-1175)**: Actively exploiting CVE-2025-10035 in Fortra GoAnywhere systems, though their method of obtaining required private keys remains unclear to security researchers
- **BatShadow (Vietnamese Threat Actor)**: Deploying new Go-based "Vampire Bot" malware through social engineering campaigns targeting job seekers and digital marketing professionals
- **North Korean State Actors**: Achieving record-breaking cryptocurrency theft totaling over $2 billion in 2025, marking the largest annual theft on record
- **LockBit, Qilin, and DragonForce Alliance**: Forming strategic ransomware coalition to dominate the ecosystem through coordinated operations and shared resources
- **China-Nexus Actors**: Weaponizing legitimate Nezha open source remote monitoring tool for malicious remote access and system control
- **Russian, North Korean, and Chinese Groups**: Misusing OpenAI's ChatGPT platform for malware development and cyberattack facilitation before disruption by the company