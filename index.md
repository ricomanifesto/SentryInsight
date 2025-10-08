# Exploitation Report

Current threat landscape reveals active exploitation of critical zero-day vulnerabilities and recently disclosed security flaws. The Clop ransomware gang has been exploiting an Oracle E-Business Suite zero-day since early August for data theft operations, while the Storm-1175 threat group is actively leveraging a maximum severity GoAnywhere vulnerability to deploy Medusa ransomware. Additionally, a 13-year-old Redis vulnerability with a perfect CVSS 10.0 score poses significant risks to cloud infrastructure, and threat actors are exploiting a Zimbra zero-day using sophisticated social engineering tactics. These exploitation activities represent immediate threats requiring urgent attention from security teams.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle E-Business Suite being actively exploited by the Clop ransomware gang for data theft operations
- **Impact**: Enables unauthorized access to sensitive business data and systems, facilitating large-scale data exfiltration campaigns
- **Status**: Under active exploitation since early August 2024, recently patched by Oracle
- **CVE ID**: CVE-2025-61882

### GoAnywhere MFT Critical Vulnerability
- **Description**: Maximum severity vulnerability in Fortra GoAnywhere managed file transfer software being exploited to deploy ransomware
- **Impact**: Allows threat actors to achieve remote code execution and deploy ransomware payloads, specifically Medusa ransomware
- **Status**: Under active exploitation by Storm-1175 group for nearly a month in ransomware campaigns
- **CVE ID**: CVE-2025-10035

### Redis Remote Code Execution Vulnerability
- **Description**: 13-year-old vulnerability in Redis in-memory database software with maximum CVSS 10.0 severity score
- **Impact**: Enables remote code execution leading to full host takeover in cloud environments
- **Status**: Over 300,000 instances currently exposed, patch available
- **CVE ID**: CVE-2025-61882

### Zimbra Zero-Day Email Exploitation
- **Description**: Zero-day vulnerability in Zimbra email platform being exploited through malicious ICS (Internet Calendar Scheduling) files
- **Impact**: Allows attackers to compromise email systems and conduct targeted attacks against military and government organizations
- **Status**: Active exploitation observed with sophisticated social engineering campaigns targeting Brazil's military

### Figma MCP Server Vulnerability
- **Description**: Critical vulnerability in the figma-developer-mcp Model Context Protocol server
- **Impact**: Enables remote code execution through the popular development tool
- **Status**: Now patched, details disclosed to facilitate remediation efforts

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software used by organizations globally
- **Fortra GoAnywhere MFT**: Managed file transfer solutions used for secure data exchange
- **Redis Database**: In-memory data structure store used extensively in cloud applications and microservices
- **Zimbra Email Platform**: Enterprise email and collaboration software
- **Figma Developer Tools**: Model Context Protocol servers used in development workflows
- **Cloud Infrastructure**: Over 300,000 Redis instances exposed across various cloud platforms
- **Enterprise Networks**: Organizations using affected Oracle, GoAnywhere, and Zimbra deployments

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of previously unknown vulnerabilities in Oracle EBS and Zimbra platforms
- **Social Engineering via ICS Files**: Sophisticated attacks using malicious calendar invitation files to exploit Zimbra systems
- **Ransomware Deployment**: Direct exploitation of GoAnywhere vulnerabilities to install Medusa ransomware
- **Data Exfiltration**: Systematic theft of sensitive business data through Oracle EBS compromises
- **Cloud Infrastructure Targeting**: Mass exploitation attempts against exposed Redis instances in cloud environments
- **Supply Chain Attacks**: Targeting of widely-used development tools like Figma MCP servers
- **Credential-Based Attacks**: Exploitation requiring private keys and authenticated access in some scenarios

## Threat Actor Activities

- **Clop Ransomware Gang**: Conducting systematic data theft operations against Oracle E-Business Suite customers since early August, demonstrating sophisticated zero-day exploitation capabilities
- **Storm-1175 Group**: Microsoft-tracked threat actor actively exploiting GoAnywhere vulnerabilities to deploy Medusa ransomware in targeted campaigns
- **Graceful Spider**: CrowdStrike-tracked actor attributed with moderate confidence to Oracle EBS exploitation activities
- **BatShadow Group**: Vietnamese threat actor using social engineering tactics against job seekers to deliver Go-based 'Vampire Bot' malware
- **State-Sponsored Actors**: Multiple nation-state groups from Russia, North Korea, and China misusing AI tools like ChatGPT for malware development and cyber operations
- **Libyan Navy Impersonators**: Threat actors impersonating official entities to target military organizations using Zimbra zero-day exploits