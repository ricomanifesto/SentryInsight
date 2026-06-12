# Exploitation Report

Critical zero-day and recently disclosed vulnerabilities are being actively exploited across multiple platforms, with particularly concerning activity targeting Oracle PeopleSoft systems and Ivanti infrastructure. The ShinyHunters extortion crew has leveraged a PeopleSoft zero-day to breach university systems for data theft, while attackers rapidly exploited a maximum-severity Ivanti Sentry vulnerability within 24 hours of public disclosure. Additional exploitation activity includes attacks on AI development platforms and credential-stealing operations targeting open-source ecosystems.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise enabling data theft and extortion attacks
- **Status**: Actively exploited by ShinyHunters group; Oracle has issued mitigation guidance
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum-Severity Vulnerability
- **Description**: Maximum-severity flaw in Ivanti Sentry secure mobile gateways
- **Impact**: Remote code execution with root privileges on Internet-exposed systems
- **Status**: Exploited within 24 hours of disclosure; patches available

### Langflow Path Traversal Vulnerability
- **Description**: High-severity path traversal vulnerability in the AI development platform Langflow
- **Impact**: Arbitrary file write capabilities on exposed servers
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-5027

### Windows BitLocker Recovery Partition Bypass
- **Description**: New GreatXML exploit bypasses Windows BitLocker encryption via manipulation of recovery partition XML files
- **Impact**: Complete bypass of disk encryption protection
- **Status**: Exploit code publicly released by security researcher

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems, particularly affecting universities and educational institutions
- **Ivanti Sentry**: Secure mobile gateways with Internet exposure
- **Langflow Platform**: AI development platforms with exposed servers
- **Windows BitLocker**: Windows disk encryption systems with recovery partitions
- **OpenClaw AI Agent**: Self-hosted AI agents vulnerable to code execution and data leakage attacks
- **npm Ecosystem**: JavaScript package management systems targeted by supply-chain attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate weaponization of undisclosed vulnerabilities in enterprise systems
- **Supply-Chain Attacks**: Miasma worm targeting open-source ecosystems through credential theft
- **AI Agent Manipulation**: Techniques to trick AI agents into executing malicious code and exposing sensitive data
- **Rapid Exploitation**: Attackers exploiting vulnerabilities within 24 hours of public disclosure
- **XML File Manipulation**: Novel technique using recovery partition XML files to bypass encryption
- **Path Traversal Attacks**: File system traversal to achieve arbitrary file write capabilities

## Threat Actor Activities

- **ShinyHunters**: Extortion crew exploiting Oracle PeopleSoft zero-day for university breaches and data theft operations
- **OceanLotus**: Vietnam-aligned threat actor conducting targeted campaigns against domestic entities and stock investors using SPECTRALVIPER backdoor
- **The Gentlemen Ransomware**: Operating as worm-capable ransomware with 478 claimed victims, initially functioning as affiliate for double extortion attacks
- **Generic Exploitation Groups**: Multiple unnamed actors rapidly exploiting Ivanti vulnerabilities and conducting AI platform attacks
- **Supply-Chain Attackers**: Groups leveraging the Miasma framework for credential theft and ecosystem compromise