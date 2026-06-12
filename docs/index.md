# Exploitation Report

The cybersecurity landscape is experiencing heightened exploitation activity across multiple fronts, with threat actors rapidly weaponizing newly disclosed vulnerabilities. The most critical concern involves the ShinyHunters extortion group exploiting a zero-day vulnerability in Oracle PeopleSoft Suite (CVE-2026-35273) to conduct widespread data theft attacks targeting universities. Additionally, a maximum severity Ivanti Sentry vulnerability was exploited within 24 hours of its disclosure, prompting emergency government patching directives. AI-powered systems are also under active attack through novel "Agentjacking" techniques targeting coding agents and vulnerabilities in LangGraph and OpenClaw platforms. The exploitation landscape is further complicated by new attack methods including the GreatXML BitLocker bypass and sophisticated supply chain attack indicators emerging from dark web activities.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Enables attackers to break into enterprise systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Actively exploited by ShinyHunters group; Oracle has released mitigations
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Critical Vulnerability
- **Description**: Maximum severity vulnerability in Ivanti Sentry platform exploited within 24 hours of disclosure
- **Impact**: Allows attackers rapid system compromise with initial evidence suggesting pre-planned asset reconnaissance
- **Status**: Under active exploitation; CISA mandated federal agencies patch within three days
- **CVE ID**: Not specified in articles

### LangGraph Vulnerability Chain
- **Description**: Three security flaws in LangGraph affecting self-hosted AI agents, including a critical vulnerability chain
- **Impact**: Can result in remote code execution on AI agent systems
- **Status**: Vulnerabilities have been patched
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems across universities and organizations
- **Ivanti Sentry**: Access management and security platforms in federal and enterprise environments
- **LangGraph**: Self-hosted AI agent frameworks and development platforms
- **OpenClaw**: Popular self-hosted AI agent systems vulnerable to code execution and data leakage
- **Windows BitLocker**: Recovery partition vulnerabilities enabling encryption bypass
- **AI Coding Agents**: Development environments susceptible to agentjacking attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate weaponization of undisclosed vulnerabilities for maximum impact
- **Agentjacking**: Novel attack class tricking AI coding agents into executing malicious code on developer machines
- **GreatXML Exploit**: Windows BitLocker bypass technique using recovery partition XML file manipulation
- **Supply Chain Targeting**: Dark web activities involving GitHub access sales, leaked repositories, and stolen API keys
- **AI Agent Manipulation**: Attacks against OpenClaw and similar platforms to execute attacker-controlled code and extract sensitive data

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) in targeted campaigns against universities for data theft and extortion
- **The Gentlemen Ransomware**: Operating as affiliates conducting double extortion attacks with worm-like spreading capabilities, claiming 478 victims
- **OceanLotus (APT32)**: Vietnam-aligned group conducting SPECTRALVIPER campaigns targeting domestic entities and stock investors through FireAnt attacks
- **AudiA6 Service Operators**: Cryptocurrency laundering service used by ransomware gangs disrupted by Europol, having processed over $380 million
- **Sniper Dz Platform**: Decade-long phishing-as-a-service operation disrupted by INTERPOL Operation Ramz