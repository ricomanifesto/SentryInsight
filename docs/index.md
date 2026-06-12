# Exploitation Report

Critical exploitation activity is currently dominated by several high-severity vulnerabilities being actively targeted in the wild. The most significant threat involves the ShinyHunters extortion crew exploiting an Oracle PeopleSoft zero-day vulnerability (CVE-2026-35273) to compromise university systems and steal sensitive data. Additionally, CISA has issued emergency directives for federal agencies to patch an actively exploited Ivanti Sentry flaw within three days, highlighting the immediate risk to government infrastructure. Multiple AI-based attack vectors are also emerging, with new techniques targeting AI coding agents and platforms like LangGraph and OpenClaw, demonstrating the evolving threat landscape as artificial intelligence becomes more integrated into enterprise environments.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in Oracle PeopleSoft Suite that allows unauthenticated remote code execution
- **Impact**: Attackers can break into enterprise systems, steal sensitive data, and demand ransom payments to keep data private
- **Status**: Oracle has released mitigation measures; actively exploited by ShinyHunters in targeted campaigns against universities
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Critical Flaw
- **Description**: A maximum-severity vulnerability in Ivanti Sentry that was exploited within 24 hours of public disclosure
- **Impact**: Allows attackers to compromise government and enterprise systems
- **Status**: CISA has mandated federal agencies patch within three days; actively exploited in the wild

### LangGraph Security Flaws
- **Description**: Three security vulnerabilities in the LangGraph AI platform, including a critical vulnerability chain
- **Impact**: Could result in remote code execution on systems running self-hosted AI agents
- **Status**: Patches have been released for all three vulnerabilities

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software used by universities and large organizations; all versions vulnerable to zero-day exploit
- **Ivanti Sentry**: Identity and access management platform used by government agencies and enterprises
- **LangGraph Platform**: AI agent development framework used for building autonomous AI systems
- **AI Coding Agents**: Various AI-powered coding assistants susceptible to "Agentjacking" attacks
- **OpenClaw AI Agent**: Self-hosted AI agent platform vulnerable to code execution and data exfiltration
- **Windows BitLocker**: Encryption system bypassed by new GreatXML exploit technique
- **Tchap Messenger**: French government encrypted messaging platform affecting over 73,000 employees

## Attack Vectors and Techniques

- **Agentjacking**: New attack class that tricks AI coding agents into running arbitrary malicious code on developer machines
- **AI Agent Manipulation**: Attackers exploit AI agents to execute unauthorized code and leak sensitive information
- **Zero-Day Exploitation**: Rapid exploitation of newly disclosed vulnerabilities, particularly in enterprise software
- **GreatXML Exploit**: Technique that bypasses Windows BitLocker encryption through manipulation of recovery partition XML files
- **Supply Chain Attacks**: Threat actors targeting development environments and AI-powered tools
- **Phishing-as-a-Service**: Evolution of phishing platforms with AI-enhanced targeting capabilities

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) in targeted campaigns against universities for data theft and extortion
- **The Gentlemen Ransomware**: Operating with worm-like spreading capabilities, claiming 478 victims through double extortion tactics
- **OceanLotus (APT32)**: Vietnam-aligned threat actor conducting campaigns against domestic entities and stock investors using SPECTRALVIPER backdoor in FireAnt operations
- **AudiA6 Operators**: Cryptocurrency laundering service used by ransomware gangs disrupted by Europol after laundering over $380 million
- **Sniper Dz Platform**: Decade-long phishing-as-a-service operation dismantled by INTERPOL Operation Ramz