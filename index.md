# Exploitation Report

Critical zero-day exploitation activity has intensified with multiple high-severity vulnerabilities being actively exploited in the wild. The most significant threat involves CVE-2026-35273, a critical Oracle PeopleSoft zero-day vulnerability that enables unauthenticated remote code execution, which has been actively exploited by the ShinyHunters extortion crew to breach universities and steal sensitive data. Additionally, a maximum-severity Ivanti Sentry vulnerability is being exploited within 24 hours of its disclosure, demonstrating the rapid weaponization capabilities of threat actors. Other concerning developments include active exploitation of CVE-2026-5027 in the Langflow AI development platform and the emergence of new attack techniques targeting AI systems and BitLocker encryption.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and extortion attacks against enterprise systems
- **Status**: Actively exploited by ShinyHunters crew; Oracle has issued mitigation guidance
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum Severity Vulnerability
- **Description**: Maximum-severity flaw in Ivanti Sentry secure mobile gateways
- **Impact**: Code execution with root privileges on Internet-exposed gateways
- **Status**: Actively exploited within 24 hours of disclosure; patches available

### Langflow Path Traversal Vulnerability
- **Description**: High-severity path traversal vulnerability in the AI development platform Langflow
- **Impact**: Arbitrary file write capabilities on exposed servers
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-5027

### GreatXML BitLocker Bypass
- **Description**: New Windows BitLocker bypass technique exploiting recovery partition XML files
- **Impact**: Complete circumvention of BitLocker disk encryption protection
- **Status**: Exploit code publicly released by security researcher

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems across universities and organizations
- **Ivanti Sentry**: Secure mobile gateways with Internet exposure
- **Langflow Platform**: AI development platforms with exposed servers
- **Windows BitLocker**: Windows disk encryption systems vulnerable to XML-based bypass
- **OpenClaw AI Agent**: Self-hosted AI agents susceptible to code execution and data leakage attacks
- **npm Ecosystem**: JavaScript package management systems targeted by supply chain attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Rapid weaponization of unpatched vulnerabilities within hours of disclosure
- **Supply Chain Attacks**: Malicious npm packages and install scripts targeting development environments
- **AI Agent Manipulation**: Novel attacks tricking AI agents into executing malicious code and leaking sensitive data
- **Encryption Bypass**: XML-based techniques to circumvent BitLocker disk encryption
- **Worm Propagation**: Self-spreading malware capabilities demonstrated by The Gentlemen ransomware
- **Path Traversal Exploitation**: Directory traversal attacks enabling arbitrary file manipulation

## Threat Actor Activities

- **ShinyHunters**: Actively exploiting Oracle PeopleSoft zero-day (CVE-2026-35273) to breach universities and conduct data theft extortion campaigns
- **The Gentlemen Ransomware**: Operating as affiliates conducting double extortion attacks with worm-like spreading capabilities, claiming 478 victims
- **OceanLotus (APT32)**: Vietnam-aligned threat actor targeting domestic entities and stock investors using SPECTRALVIPER backdoor in FireAnt campaigns
- **Chinese and North Korean Groups**: Expanding operations in Asia-Pacific region with state-sponsored cybercrime contributing to GDP growth
- **Unknown Attackers**: Rapidly exploiting Ivanti Sentry and Langflow vulnerabilities, suggesting pre-mapped infrastructure and coordinated exploitation efforts