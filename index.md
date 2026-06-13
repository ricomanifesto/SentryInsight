# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities being actively exploited in the wild, with significant impact across enterprise environments and open-source ecosystems. Most notably, the ShinyHunters extortion crew has successfully exploited CVE-2026-35273, an Oracle PeopleSoft zero-day vulnerability allowing unauthenticated remote code execution, specifically targeting American universities for data theft. Additionally, CISA has issued emergency directives for federal agencies to patch an actively exploited Ivanti Sentry flaw within 72 hours, demonstrating the rapid weaponization of newly disclosed vulnerabilities. The security community has also witnessed a massive supply chain compromise affecting over 400 Arch Linux AUR packages, which were hijacked to deploy credential stealers and eBPF rootkits, alongside sophisticated attacks targeting AI coding agents and self-hosted AI systems.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle's PeopleSoft Suite enabling unauthenticated remote code execution
- **Impact**: Allows attackers to break into enterprise systems, steal sensitive data, and conduct extortion campaigns
- **Status**: Actively exploited by ShinyHunters group targeting universities; Oracle has released mitigation measures
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Critical Flaw
- **Description**: Maximum severity vulnerability in Ivanti Sentry software exploited within 24 hours of public disclosure
- **Impact**: Enables unauthorized access to enterprise systems and sensitive data
- **Status**: Actively exploited in the wild; CISA has mandated federal agencies patch within 3 days
- **CVE ID**: Not specified in articles

### phpBB Authentication Bypass
- **Description**: 10-year-old authentication bypass vulnerability in phpBB forum software
- **Impact**: Allows attackers to log in as any user, including administrators
- **Status**: Recently patched after a decade of exposure
- **CVE ID**: Not specified in articles

### LangGraph AI Framework Vulnerabilities
- **Description**: Critical vulnerability chain in LangGraph framework affecting self-hosted AI agents
- **Impact**: Enables remote code execution on systems running AI agents
- **Status**: Three security flaws have been patched
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning software disproportionately affecting American universities
- **Ivanti Sentry**: Enterprise security management platform used by federal agencies and organizations
- **Arch Linux AUR Packages**: Over 400 packages in the Arch User Repository compromised with malicious build scripts
- **phpBB Forum Software**: Popular open-source forum platform with 10-year-old authentication bypass
- **LangGraph Framework**: AI agent development platform used in self-hosted environments
- **OpenClaw AI Agent**: Popular self-hosted AI agent platform vulnerable to code execution attacks
- **Windows BitLocker**: Microsoft's disk encryption system bypassed via GreatXML exploit targeting recovery partition XML files
- **Linux Login Systems**: Login software backdoored by China-linked threat actors for nearly a decade

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Rapid weaponization of newly disclosed vulnerabilities, with Ivanti flaw exploited within 24 hours
- **Supply Chain Compromise**: Hijacking of legitimate software repositories to distribute malware through trusted distribution channels
- **Agentjacking Attacks**: Novel attack class targeting AI coding agents to execute malicious code on developer machines
- **AI Agent Manipulation**: Tricking self-hosted AI systems into running attacker-controlled code or leaking sensitive information
- **Authentication Bypass**: Long-standing vulnerabilities enabling unauthorized access to administrative functions
- **Phishing-as-a-Service**: Decade-long platforms providing phishing infrastructure to cybercriminals
- **BitLocker Bypass**: GreatXML exploit targeting Windows recovery partition XML files to circumvent disk encryption
- **eBPF Rootkit Deployment**: Advanced persistence techniques using extended Berkeley Packet Filter technology

## Threat Actor Activities

- **ShinyHunters**: Exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) in targeted campaigns against American universities for data theft and extortion
- **China-Linked Groups**: Multi-year campaign backdooring Linux login systems for persistent access, tracked as "Velvet Ant" by Sygnia
- **Package Hijackers**: Compromising over 400 Arch Linux AUR packages to deploy credential stealers and eBPF rootkits targeting developer environments
- **Chinese Smishing Network**: Using Google's Gemini AI to enhance phishing text message campaigns targeting American consumers
- **The Gentlemen Ransomware**: Operating as affiliates conducting double extortion attacks with worm-like spreading capabilities, claiming 478 victims
- **Conti Ransomware Operation**: Continued law enforcement actions with Ukrainian national pleading guilty to conspiracy charges
- **Sniper Dz PhaaS**: Decade-long phishing-as-a-service platform disrupted by INTERPOL Operation Ramz
- **AudiA6 Operators**: Cryptocurrency laundering service used by ransomware gangs dismantled by European authorities, having laundered over $380 million