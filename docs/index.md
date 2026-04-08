# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple vectors, with Russian state-linked actors leading aggressive campaigns targeting critical infrastructure and authentication systems. Iranian threat actors are actively disrupting U.S. critical infrastructure through internet-exposed operational technology devices, while North Korean hackers continue their supply chain attacks across multiple programming ecosystems. Notable exploitations include active attacks against the Flowise platform, Ninja Forms WordPress plugin, and Docker Engine authorization bypasses. Meanwhile, threat actors are leveraging compromised routers for DNS hijacking operations and deploying sophisticated malware campaigns targeting Ukraine and NATO allies.

## Active Exploitation Details

### Flowise Remote Code Execution Vulnerability
- **Description**: Maximum-severity vulnerability in the open-source Flowise platform for building custom LLM apps and agentic systems
- **Impact**: Allows attackers to execute arbitrary code on vulnerable systems
- **Status**: Currently being exploited in active attacks
- **CVE ID**: CVE-2025-59528

### Docker Engine Authorization Bypass
- **Description**: High-severity vulnerability that allows attackers to bypass authorization plugins (AuthZ) under specific circumstances
- **Impact**: Enables unauthorized access to Docker hosts and container environments
- **Status**: Recently disclosed vulnerability with potential for exploitation
- **CVE ID**: CVE-2026-34040

### Ninja Forms WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress allowing arbitrary file uploads without authentication
- **Impact**: Can lead to remote code execution on WordPress sites
- **Status**: Actively exploited by hackers

### Storm-1175 N-day and Zero-day Exploitation
- **Description**: Financially motivated cybercrime group exploiting both N-day and zero-day vulnerabilities
- **Impact**: Rapid deployment of Medusa ransomware at high velocity
- **Status**: Ongoing campaign with speed-focused exploitation tactics

## Affected Systems and Products

- **Flowise Platform**: Open-source LLM application building platform
- **Docker Engine**: Container runtime environment with authorization bypass vulnerability
- **Ninja Forms WordPress Plugin**: Popular WordPress form builder with file upload functionality
- **MikroTik and TP-Link Routers**: SOHO routers compromised for DNS hijacking operations
- **Rockwell/Allen-Bradley PLCs**: Programmable logic controllers in U.S. critical infrastructure
- **ComfyUI Instances**: Stable diffusion platform instances exposed to internet
- **Microsoft Office 365**: Authentication tokens targeted through router compromises
- **Snowflake Customers**: Multiple companies affected through SaaS integrator breach
- **npm, PyPI, Go, Rust Ecosystems**: Package repositories targeted with 1,700 malicious packages

## Attack Vectors and Techniques

- **DNS Hijacking**: Compromising router settings to redirect traffic for credential theft
- **Spear-phishing Campaigns**: Targeted email attacks deploying PRISMEX malware
- **Supply Chain Attacks**: Malicious packages distributed across multiple programming language ecosystems
- **Internet-exposed Device Targeting**: Direct attacks on PLCs and OT devices with internet connectivity
- **Authentication Token Harvesting**: Mass collection of Microsoft Office tokens through router compromises
- **Cryptomining Botnet Deployment**: Targeting exposed ComfyUI instances for cryptocurrency mining
- **File Upload Exploitation**: Leveraging WordPress plugin vulnerabilities for arbitrary file uploads
- **Container Authorization Bypass**: Exploiting Docker Engine flaws to gain unauthorized host access

## Threat Actor Activities

- **APT28 (Forest Blizzard/Pawn Storm)**: Russian state-linked group deploying PRISMEX malware in campaigns targeting Ukraine and NATO allies; conducting global DNS hijacking through compromised SOHO routers
- **Iranian Threat Actors**: Targeting U.S. critical infrastructure through internet-exposed PLCs, causing operational disruption and financial losses across multiple sectors
- **Storm-1175**: Financially motivated cybercrime group rapidly deploying Medusa ransomware using both N-day and zero-day vulnerabilities
- **North Korean Hackers (Contagious Interview)**: Spreading 1,700 malicious packages across npm, PyPI, Go, Rust, and PHP ecosystems in persistent supply chain campaign
- **FrostArmada Campaign**: APT28-linked operation hijacking local traffic from MikroTik and TP-Link routers for Microsoft 365 credential theft