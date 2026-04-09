# Exploitation Report

Critical exploitation activity has escalated across multiple attack vectors, with several high-impact vulnerabilities under active attack. CISA has ordered federal agencies to patch a critical Ivanti EPMM vulnerability exploited since January, while hackers actively exploit a maximum-severity remote code execution flaw in Flowise (CVE-2025-59528). Russian APT28 actors are conducting large-scale DNS hijacking campaigns through compromised routers, and Iranian threat actors are disrupting U.S. critical infrastructure by targeting exposed industrial control systems. Additional active exploits include a critical WordPress plugin vulnerability and a newly discovered 13-year-old Apache ActiveMQ bug enabling remote command execution.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Critical Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti Endpoint Manager Mobile that allows unauthorized access and system compromise
- **Impact**: Full system compromise and potential lateral movement within enterprise networks
- **Status**: Currently being exploited in the wild since January; CISA has mandated federal agencies patch by Sunday

### Flowise Remote Code Execution Vulnerability
- **Description**: Maximum-severity vulnerability in the open-source platform Flowise used for building custom LLM applications and agentic systems
- **Impact**: Arbitrary code execution allowing complete system takeover
- **Status**: Currently being exploited in attacks
- **CVE ID**: CVE-2025-59528

### Ninja Forms WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on allowing arbitrary file upload without authentication
- **Impact**: Remote code execution through malicious file uploads on WordPress sites
- **Status**: Currently being exploited by attackers

### Apache ActiveMQ Classic Remote Code Execution
- **Description**: 13-year-old undetected vulnerability in Apache ActiveMQ Classic message broker
- **Impact**: Remote command execution allowing complete system compromise
- **Status**: Recently discovered and potentially exploitable

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems across federal agencies
- **Flowise Platform**: Open-source LLM application building platforms and agentic systems
- **Ninja Forms WordPress Plugin**: WordPress websites using the File Uploads premium add-on
- **Apache ActiveMQ Classic**: Enterprise message broker systems that have been running vulnerable versions for up to 13 years
- **MikroTik and TP-Link Routers**: Small office/home office routers compromised for DNS hijacking
- **Rockwell/Allen-Bradley PLCs**: Internet-exposed programmable logic controllers in critical infrastructure
- **Snowflake Customer Environments**: Multiple companies affected through SaaS integrator breach

## Attack Vectors and Techniques

- **DNS Hijacking**: Compromising SOHO routers to redirect traffic and steal authentication credentials
- **File Upload Bypass**: Exploiting authentication bypasses in WordPress plugins to upload malicious files
- **OT Device Targeting**: Direct attacks against internet-exposed industrial control systems
- **Token Theft**: Harvesting Microsoft Office authentication tokens through compromised network infrastructure
- **Supply Chain Compromise**: Targeting SaaS integrators to access multiple downstream customers
- **Malicious Package Distribution**: Spreading 1,700+ malicious packages across npm, PyPI, Go, and Rust ecosystems
- **ClickFix Social Engineering**: Using Script Editor abuse in macOS to deliver Atomic Stealer malware

## Threat Actor Activities

- **APT28 (Forest Blizzard/Pawn Storm)**: Conducting global DNS hijacking campaigns through compromised MikroTik and TP-Link routers; deploying PRISMEX malware against Ukraine and NATO allies
- **Iranian Threat Actors**: Systematically targeting U.S. critical infrastructure through exposed PLCs, causing operational disruption and financial losses across multiple sectors
- **North Korean Hackers (Contagious Interview)**: Distributing malicious packages across multiple programming language ecosystems including Go, Rust, and PHP
- **Storm-1175**: Deploying Medusa ransomware at high velocity, exploiting both N-day and zero-day vulnerabilities
- **Chaos Botnet Operators**: Expanding targeting to include misconfigured cloud deployments with new SOCKS proxy capabilities
- **Masjesu Botnet**: Operating DDoS-for-hire services targeting global IoT devices through Telegram advertising