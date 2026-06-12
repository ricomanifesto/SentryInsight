# Exploitation Report

Critical zero-day exploitation is dominating the current threat landscape, with the ShinyHunters extortion crew actively exploiting CVE-2026-35273, an Oracle PeopleSoft zero-day vulnerability that enables unauthenticated remote code execution. This campaign has specifically targeted universities for data theft operations. Simultaneously, CISA has issued emergency directives requiring federal agencies to patch an actively exploited Ivanti Sentry flaw within 72 hours, highlighting the severity of ongoing attacks. The threat environment is further complicated by emerging AI-focused attack vectors, including Agentjacking attacks targeting AI coding agents and exploitation techniques against LangGraph and OpenClaw AI systems, demonstrating how threat actors are rapidly adapting to target AI-driven infrastructure.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle PeopleSoft Suite that allows unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and unauthorized access to enterprise systems
- **Status**: Actively exploited by ShinyHunters extortion crew; Oracle has issued mitigations
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Critical Vulnerability
- **Description**: Maximum severity vulnerability in Ivanti Sentry that was exploited within 24 hours of public disclosure
- **Impact**: Complete system compromise with evidence of rapid exploitation following disclosure
- **Status**: Under active exploitation; CISA has mandated federal agencies patch within 3 days under new Binding Operational Directive 26-04

### LangGraph Remote Code Execution Chain
- **Description**: Critical vulnerability chain in LangGraph affecting self-hosted AI agents
- **Impact**: Remote code execution on systems running LangGraph AI agents
- **Status**: Now patched, but was exploitable in self-hosted environments

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise systems across universities and organizations, particularly vulnerable to data theft attacks
- **Ivanti Sentry**: Federal government systems and enterprise infrastructure requiring immediate patching
- **AI Coding Agents**: Development environments using AI coding assistants susceptible to Agentjacking attacks
- **LangGraph AI Systems**: Self-hosted AI agent deployments vulnerable to remote code execution
- **OpenClaw AI Agent**: Popular self-hosted AI agents vulnerable to code execution and data exfiltration
- **Windows BitLocker**: Systems vulnerable to GreatXML bypass technique via recovery partition XML files
- **Microsoft Defender**: Systems affected by new exploit techniques from security researcher

## Attack Vectors and Techniques

- **Agentjacking**: New attack class that tricks AI coding agents into executing arbitrary code on developer machines
- **Zero-Day Exploitation**: Rapid weaponization of Oracle PeopleSoft vulnerability for data theft campaigns
- **AI Agent Manipulation**: Techniques to trick OpenClaw and other AI agents into running attacker-controlled code or leaking sensitive data
- **GreatXML BitLocker Bypass**: Novel technique exploiting Windows recovery partition XML files to bypass BitLocker encryption
- **Worm-Like Propagation**: The Gentlemen ransomware demonstrating self-propagating capabilities across networks

## Threat Actor Activities

- **ShinyHunters Extortion Crew**: Actively exploiting CVE-2026-35273 to breach university systems, steal data, and demand payment for data privacy
- **OceanLotus (Vietnam-aligned)**: Conducting SPECTRALVIPER backdoor campaigns targeting domestic Vietnamese entities and stock investors through FireAnt attacks
- **The Gentlemen Ransomware Group**: Operating double extortion attacks with 478 claimed victims, utilizing worm-like spreading capabilities
- **INTERPOL Operation Ramz**: Successful takedown of Sniper Dz phishing-as-a-service platform that operated for over a decade
- **Europol AudiA6 Disruption**: Dismantling of cryptocurrency laundering service used by ransomware gangs to process over $380 million in illicit funds