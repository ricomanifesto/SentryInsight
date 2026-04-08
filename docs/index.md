# Exploitation Report

Current threat landscape reveals intense exploitation activity across multiple attack vectors, with threat actors actively targeting critical infrastructure, enterprise systems, and popular development platforms. Iranian-linked hackers are systematically compromising internet-exposed programmable logic controllers across U.S. critical infrastructure, while Russian state-sponsored APT28 has orchestrated a massive DNS hijacking campaign through compromised SOHO routers to steal Microsoft 365 authentication tokens. Multiple maximum-severity vulnerabilities are under active exploitation, including critical flaws in WordPress plugins, Docker Engine, and AI platforms, with threat actors deploying ransomware at unprecedented speeds and distributing malicious packages across major software repositories.

## Active Exploitation Details

### Flowise Remote Code Execution Vulnerability
- **Description**: Maximum-severity vulnerability in the open-source Flowise AI platform for building custom LLM applications and agentic systems
- **Impact**: Allows attackers to execute arbitrary code on affected systems with over 12,000 exposed instances identified
- **Status**: Actively exploited in the wild with CVSS 10.0 severity rating
- **CVE ID**: CVE-2025-59528

### Ninja Forms WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress allowing arbitrary file uploads without authentication
- **Impact**: Enables remote code execution through malicious file uploads, compromising WordPress websites
- **Status**: Actively exploited by threat actors targeting WordPress installations

### Docker Engine Authorization Bypass Vulnerability
- **Description**: High-severity vulnerability in Docker Engine that allows attackers to bypass authorization plugins under specific circumstances
- **Impact**: Enables unauthorized access to Docker hosts and container environments
- **Status**: Patched vulnerability with ongoing exploitation concerns
- **CVE ID**: CVE-2026-34040

### Router DNS Hijacking Campaign
- **Description**: Exploitation of known flaws in older MikroTik and TP-Link routers to modify DNS settings and harvest authentication tokens
- **Impact**: Mass harvest of Microsoft Office authentication tokens through DNS redirection attacks
- **Status**: Actively exploited by Russian military intelligence units; law enforcement disruption operation conducted

### Critical Infrastructure PLC Targeting
- **Description**: Systematic targeting of internet-facing Rockwell/Allen-Bradley programmable logic controllers on critical infrastructure networks
- **Impact**: Potential disruption of critical infrastructure operations including power grids, water systems, and manufacturing facilities
- **Status**: Ongoing active exploitation by Iranian-linked threat actors

## Affected Systems and Products

- **Flowise AI Platform**: Over 12,000 internet-exposed instances vulnerable to remote code execution
- **WordPress Sites**: Websites using Ninja Forms File Uploads premium add-on susceptible to arbitrary file upload attacks
- **Docker Environments**: Docker Engine installations affected by authorization bypass vulnerability
- **SOHO Routers**: MikroTik and TP-Link routers compromised for DNS hijacking operations
- **Critical Infrastructure PLCs**: Rockwell/Allen-Bradley programmable logic controllers on U.S. critical infrastructure networks
- **Package Repositories**: npm, PyPI, Go, and Rust ecosystems infiltrated with 1,700 malicious packages
- **ComfyUI Instances**: Over 1,000 exposed stable diffusion platform instances targeted for cryptocurrency mining
- **Grafana AI Components**: AI-enabled Grafana instances vulnerable to prompt injection attacks
- **Snowflake Customers**: Multiple organizations affected through compromised SaaS integrator authentication tokens

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of maximum-severity vulnerabilities in AI platforms and WordPress plugins to execute arbitrary code
- **DNS Hijacking**: Compromise of SOHO routers to redirect traffic and steal authentication credentials
- **Supply Chain Attacks**: Distribution of malicious packages across multiple software repositories targeting developers
- **Infrastructure Targeting**: Direct attacks on internet-exposed industrial control systems and programmable logic controllers
- **Token Theft**: Harvesting of Microsoft 365 and other cloud service authentication tokens through compromised network infrastructure
- **Privilege Escalation**: GPUBreach attacks using RowHammer techniques on GPU memory to escalate system privileges
- **Prompt Injection**: AI-targeted attacks using hidden malicious instructions to extract sensitive data
- **Cryptocurrency Mining**: Botnet recruitment of exposed AI platform instances for mining operations

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Russian state-linked group conducting global DNS hijacking campaign through compromised routers to steal Microsoft 365 credentials
- **Iranian-Linked Actors**: Systematically targeting U.S. critical infrastructure by exploiting internet-exposed programmable logic controllers
- **Storm-1175**: China-linked threat actor deploying Medusa ransomware at high velocity using combination of zero-day and N-day vulnerabilities
- **North Korean Contagious Interview Campaign**: Distributing 1,700 malicious packages across npm, PyPI, Go, and Rust ecosystems targeting software developers
- **Cryptocurrency Mining Groups**: Actively recruiting exposed ComfyUI instances into mining and proxy botnets
- **WordPress Attackers**: Exploiting Ninja Forms vulnerability for website compromise and potential data theft
- **REvil and GandCrab Operators**: German authorities identified Russian nationals as leaders of major ransomware operations between 2019-2021