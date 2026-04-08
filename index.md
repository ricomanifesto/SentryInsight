# Exploitation Report

Current threat activity shows a surge in critical infrastructure targeting, with Iranian threat actors actively compromising U.S. operational technology systems and Russian APT28 conducting sophisticated DNS hijacking campaigns. Several zero-day and recently patched vulnerabilities are being exploited in the wild, including a critical WordPress plugin flaw and a maximum-severity remote code execution vulnerability in Flowise. North Korean hackers continue their supply chain attacks through malicious packages across multiple development ecosystems, while Storm-1175 demonstrates rapid deployment of ransomware using both N-day and zero-day exploits.

## Active Exploitation Details

### Ninja Forms File Uploads WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on that allows uploading arbitrary files without authentication
- **Impact**: Remote code execution on affected WordPress sites
- **Status**: Currently being exploited in the wild by threat actors

### Flowise Remote Code Execution Vulnerability
- **Description**: Maximum-severity vulnerability in the open-source Flowise platform used for building custom LLM applications and agentic systems
- **Impact**: Allows attackers to execute arbitrary code on affected systems
- **Status**: Active exploitation detected in attacks
- **CVE ID**: CVE-2025-59528

### Docker Engine Authorization Bypass
- **Description**: High-severity vulnerability that permits attackers to bypass authorization plugins (AuthZ) under specific circumstances
- **Impact**: Unauthorized access to Docker host systems
- **Status**: Vulnerability disclosed with patch available
- **CVE ID**: CVE-2026-34040

### Grafana AI Integration Vulnerability
- **Description**: Bug in Grafana's AI functionality that could lead to data leakage through malicious instruction injection
- **Impact**: Potential exposure of sensitive user data through AI prompt manipulation
- **Status**: Patched by Grafana

## Affected Systems and Products

- **WordPress Sites**: Ninja Forms File Uploads premium add-on users vulnerable to unauthenticated file upload
- **Flowise Platforms**: Open-source LLM application building platforms exposed to RCE attacks
- **Docker Engine**: Containerized environments with authorization plugins at risk
- **Critical Infrastructure**: U.S. water treatment, energy, and manufacturing facilities with exposed PLCs
- **MikroTik and TP-Link Routers**: SOHO routers compromised for DNS hijacking operations
- **Rockwell/Allen-Bradley PLCs**: Internet-exposed programmable logic controllers in critical infrastructure
- **Development Environments**: npm, PyPI, Go, Rust, and PHP ecosystems targeted with malicious packages
- **ComfyUI Instances**: Over 1,000 exposed stable diffusion platform installations targeted for cryptomining
- **Snowflake Customers**: Multiple companies affected through SaaS integrator breach

## Attack Vectors and Techniques

- **Unauthenticated File Upload**: Exploitation of WordPress plugin allowing arbitrary file uploads leading to RCE
- **DNS Hijacking**: Modification of router DNS settings to redirect traffic and steal authentication tokens
- **Supply Chain Poisoning**: Distribution of malicious packages across multiple development platforms
- **PLC Manipulation**: Direct targeting of internet-exposed operational technology devices
- **Spear-Phishing**: Targeted email campaigns deploying PRISMEX malware
- **Token Theft**: Mass harvesting of Microsoft Office authentication tokens through compromised routers
- **Cryptomining Botnet**: Targeting of AI platforms for cryptocurrency mining operations
- **Authorization Bypass**: Exploitation of Docker authorization plugin vulnerabilities

## Threat Actor Activities

- **APT28 (Forest Blizzard/Pawn Storm)**: Conducting global DNS hijacking campaign through compromised SOHO routers and deploying PRISMEX malware against Ukraine and NATO allies
- **Iranian Threat Actors**: Systematically targeting U.S. critical infrastructure through exposed PLCs, causing operational disruption and financial losses
- **Storm-1175**: Deploying Medusa ransomware at high velocity using both N-day and zero-day vulnerabilities
- **North Korean Hackers (Contagious Interview Campaign)**: Spreading 1,700 malicious packages across npm, PyPI, Go, Rust, and PHP ecosystems
- **Financially Motivated Groups**: Targeting exposed ComfyUI instances for cryptomining botnet operations and exploiting SaaS integrators for data theft