# Exploitation Report

Critical exploitation activity is currently targeting multiple attack surfaces, with threat actors leveraging both zero-day vulnerabilities and recently patched flaws to achieve maximum impact. Most concerning is the active exploitation of CVE-2025-59528 in Flowise AI platforms, which carries a maximum CVSS 10.0 severity rating and affects over 12,000 exposed instances. Simultaneously, nation-state actors including APT28 and Iranian-linked groups are conducting sophisticated campaigns targeting critical infrastructure through compromised routers and programmable logic controllers. The Storm-1175 group is deploying Medusa ransomware at unprecedented velocity by chaining zero-day and N-day exploits, while supply chain attacks continue to proliferate across package repositories including npm, PyPI, Go, and Rust ecosystems.

## Active Exploitation Details

### Flowise AI Platform Remote Code Execution
- **Description**: A maximum-severity vulnerability in the open-source Flowise platform that allows building custom LLM applications and agentic systems
- **Impact**: Enables attackers to execute arbitrary code remotely without authentication, leading to complete system compromise
- **Status**: Currently under active exploitation with over 12,000 instances exposed globally
- **CVE ID**: CVE-2025-59528

### Ninja Forms WordPress Plugin File Upload Bypass
- **Description**: A critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress that allows uploading arbitrary files without authentication
- **Impact**: Enables remote code execution on WordPress installations through malicious file uploads
- **Status**: Actively exploited in the wild with patches available

### Docker Engine Authorization Bypass
- **Description**: A high-severity security vulnerability in Docker Engine that permits attackers to bypass authorization plugins (AuthZ) under specific circumstances
- **Impact**: Allows unauthorized access to Docker host systems and containers
- **Status**: Recently disclosed with patches available
- **CVE ID**: CVE-2026-34040

### Router DNS Hijacking Campaign
- **Description**: Exploitation of known flaws in older internet routers by Russian military intelligence units to harvest authentication tokens
- **Impact**: Mass theft of Microsoft Office authentication credentials through DNS manipulation
- **Status**: Active exploitation disrupted by international law enforcement operation

### Storm-1175 Zero-Day and N-Day Exploitation
- **Description**: High-velocity ransomware deployment campaign utilizing a combination of zero-day and recently patched vulnerabilities
- **Impact**: Rapid deployment of Medusa ransomware with minimal dwell time
- **Status**: Ongoing exploitation by China-linked threat actors

## Affected Systems and Products

- **Flowise AI Platform**: Over 12,000 internet-exposed instances vulnerable to remote code execution
- **WordPress Sites**: Installations using Ninja Forms File Uploads premium add-on affected by authentication bypass
- **Docker Engine**: Various versions susceptible to authorization plugin bypass
- **MikroTik and TP-Link Routers**: Internet-facing SOHO routers compromised for DNS hijacking operations
- **Rockwell/Allen-Bradley PLCs**: Programmable logic controllers on critical infrastructure networks targeted by Iranian actors
- **ComfyUI Instances**: Over 1,000 exposed stable diffusion platform instances enlisted in cryptocurrency mining botnet
- **Grafana AI Components**: AI-powered features vulnerable to data leakage through hidden instruction injection
- **Package Repositories**: 1,700+ malicious packages distributed across npm, PyPI, Go, Rust, and PHP ecosystems
- **Snowflake Customers**: Multiple organizations affected by data theft following SaaS integrator breach

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Injection of 1,700 malicious packages across multiple programming language repositories by North Korean actors
- **DNS Hijacking**: Modification of router DNS settings to redirect traffic through attacker-controlled infrastructure
- **AI Instruction Injection**: Hiding malicious instructions in web pages to manipulate AI systems into returning sensitive data
- **PLC Targeting**: Direct exploitation of internet-exposed programmable logic controllers in critical infrastructure
- **Authentication Token Theft**: Mass harvesting of Microsoft Office credentials through compromised router infrastructure
- **GPU Memory Exploitation**: GPUBreach attack inducing RowHammer bit-flips on GDDR6 memories for privilege escalation
- **Social Engineering Automation**: AI-assisted targeting of GitHub maintainers and repository configurations
- **High-Velocity Ransomware Deployment**: Rapid exploitation of vulnerability chains to minimize detection time
- **Cryptomining Botnet Recruitment**: Automated targeting of exposed AI platform instances for cryptocurrency mining operations

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Conducting global DNS hijacking campaign targeting MikroTik and TP-Link routers to steal Microsoft 365 credentials through the FrostArmada operation
- **Storm-1175**: China-linked group deploying Medusa ransomware using zero-day and N-day vulnerability combinations in high-velocity attacks
- **Iranian Cyber Actors**: Targeting U.S. critical infrastructure by exploiting internet-facing operational technology devices including PLCs
- **North Korean Contagious Interview Campaign**: Spreading 1,700 malicious packages across npm, PyPI, Go, Rust, and PHP ecosystems to target software developers
- **Russian Military Intelligence Units**: Mass harvesting Microsoft Office authentication tokens through compromised router infrastructure
- **Financially Motivated Groups**: Exploiting Flowise AI platforms and ComfyUI instances for cryptocurrency mining operations
- **Supply Chain Attackers**: Using AI-assisted social engineering to target GitHub maintainers and exploit repository misconfigurations