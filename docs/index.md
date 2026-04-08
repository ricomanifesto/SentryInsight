# Exploitation Report

Critical exploitation activity is currently dominated by multiple zero-day vulnerabilities and sophisticated campaigns targeting infrastructure components. Most concerning are the active exploitations of CVE-2025-59528 in Flowise AI platforms, CVE-2026-35616 in FortiClient, and CVE-2026-34040 in Docker Engine. The Storm-1175 threat group is conducting high-velocity ransomware deployments using both zero-day and N-day vulnerabilities, while Russian state-linked APT28 has compromised thousands of routers for DNS hijacking operations targeting Microsoft 365 credentials. Additionally, a leaked Windows zero-day exploit called "BlueHammer" poses immediate risks for privilege escalation attacks across Windows environments.

## Active Exploitation Details

### Flowise AI Platform Remote Code Execution
- **Description**: A maximum-severity vulnerability in the open-source Flowise platform for building custom LLM applications and agentic systems
- **Impact**: Allows attackers to execute arbitrary code on affected systems with over 12,000+ exposed instances identified
- **Status**: Currently being actively exploited in the wild
- **CVE ID**: CVE-2025-59528

### FortiClient Authentication Bypass Zero-Day
- **Description**: An authentication bypass vulnerability in Fortinet's FortiClient application
- **Impact**: Allows attackers to bypass authentication mechanisms
- **Status**: Zero-day vulnerability with emergency patch issued by Fortinet
- **CVE ID**: CVE-2026-35616

### Docker Engine Authorization Bypass
- **Description**: High-severity vulnerability in Docker Engine that allows bypassing authorization plugins (AuthZ) under specific circumstances
- **Impact**: Attackers can bypass authorization and gain host access
- **Status**: Vulnerability disclosed with patches available
- **CVE ID**: CVE-2026-34040

### Windows BlueHammer Zero-Day Privilege Escalation
- **Description**: Unpatched Windows privilege escalation vulnerability with publicly leaked exploit code
- **Impact**: Allows attackers to gain SYSTEM or elevated administrator permissions
- **Status**: Zero-day with exploit code publicly available; reported privately to Microsoft but currently unpatched

### Ninja Forms WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress
- **Impact**: Allows uploading arbitrary files without authentication, leading to remote code execution
- **Status**: Actively exploited in attacks targeting WordPress installations

## Affected Systems and Products

- **Flowise AI Platform**: Over 12,000+ internet-exposed instances vulnerable to remote code execution
- **FortiClient**: Fortinet's client software affected by authentication bypass vulnerability
- **Docker Engine**: Container platform vulnerable to authorization bypass attacks
- **Windows Operating Systems**: All versions affected by the BlueHammer privilege escalation zero-day
- **WordPress Ninja Forms Plugin**: Premium File Uploads add-on vulnerable to arbitrary file upload
- **MikroTik and TP-Link Routers**: Consumer and small office routers compromised in DNS hijacking campaigns
- **ComfyUI Instances**: Over 1,000 exposed stable diffusion platforms targeted for cryptocurrency mining
- **Microsoft Office 365**: Users targeted through router-based token theft operations
- **Snowflake SaaS Platform**: Multiple customer organizations affected through SaaS integrator breach
- **Grafana AI Components**: AI functionality vulnerable to data leakage through malicious instructions

## Attack Vectors and Techniques

- **Router DNS Hijacking**: APT28 modifying router DNS settings to redirect traffic and steal Microsoft 365 authentication tokens
- **Supply Chain Attacks**: AI-assisted targeting of GitHub repositories and NPM package maintainers
- **Zero-Day Exploitation**: Coordinated use of multiple zero-day vulnerabilities for rapid deployment
- **Cryptocurrency Mining Botnets**: Targeting exposed AI platform instances for mining operations
- **Authentication Token Theft**: Mass harvesting of Microsoft Office tokens through compromised infrastructure
- **Privilege Escalation**: GPU-based RowHammer attacks enabling system takeover through GDDR6 bit-flips
- **Social Engineering**: Industrialized campaigns targeting software maintainers and developers
- **File Upload Exploitation**: Bypassing authentication to upload malicious files for remote code execution

## Threat Actor Activities

- **Storm-1175**: China-linked group deploying Medusa ransomware using zero-day and N-day vulnerabilities in high-velocity attacks
- **APT28 (Forest Blizzard)**: Russian state-linked actor conducting global DNS hijacking campaign through compromised routers
- **FrostArmada**: APT28 campaign specifically targeting Microsoft 365 credentials through router compromises
- **Iranian Threat Actors**: Targeting critical infrastructure by exploiting Internet-exposed Rockwell/Allen-Bradley programmable logic controllers
- **Cryptocurrency Mining Groups**: Orchestrating botnet campaigns against exposed ComfyUI and AI platform instances
- **REvil and GandCrab Operators**: Two Russian nationals identified by German authorities as leaders of major ransomware operations (2019-2021)
- **GitHub Supply Chain Attackers**: AI-assisted campaigns targeting software repositories and package maintainers
- **SaaS Integration Breach Actors**: Compromising integration providers to steal authentication tokens for downstream attacks