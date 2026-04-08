# Exploitation Report

Critical vulnerability exploitation activity is actively targeting multiple platforms with devastating impact. Attackers are exploiting maximum-severity vulnerabilities in AI platforms, WordPress plugins, and enterprise infrastructure systems. The most concerning developments include the exploitation of CVE-2025-59528 in Flowise AI platforms with a CVSS 10.0 severity rating, widespread attacks on WordPress sites through Ninja Forms vulnerabilities, and sophisticated campaigns by state-linked groups targeting network infrastructure. Zero-day exploits are being weaponized by threat groups like Storm-1175 for rapid ransomware deployment, while Russian APT28 operations have compromised thousands of routers for credential theft. Additionally, researchers have disclosed new attack techniques including GPU-based privilege escalation methods and Windows zero-day exploits that remain unpatched.

## Active Exploitation Details

### Flowise Remote Code Execution Vulnerability
- **Description**: A maximum-severity vulnerability in the Flowise open-source platform for building custom LLM apps and agentic systems that allows remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable systems, leading to complete system compromise
- **Status**: Currently being exploited in active attacks with over 12,000 instances exposed
- **CVE ID**: CVE-2025-59528

### Ninja Forms WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress that allows uploading arbitrary files without authentication
- **Impact**: Remote code execution through unrestricted file upload, enabling complete website takeover
- **Status**: Actively exploited by hackers in ongoing campaigns

### Docker Engine Authorization Bypass
- **Description**: High-severity security vulnerability that permits attackers to bypass authorization plugins (AuthZ) under specific circumstances
- **Impact**: Unauthorized access to Docker host systems and container environments
- **Status**: Recently disclosed vulnerability requiring immediate patching
- **CVE ID**: CVE-2026-34040

### FortiClient Zero-Day Authentication Bypass
- **Description**: Authentication bypass flaw in Fortinet's FortiClient that allows unauthorized access
- **Impact**: Complete bypass of authentication mechanisms, enabling unauthorized system access
- **Status**: Zero-day vulnerability exploited in the wild, emergency patch issued
- **CVE ID**: CVE-2026-35616

### Windows "BlueHammer" Privilege Escalation Zero-Day
- **Description**: Unpatched Windows privilege escalation flaw that was privately reported to Microsoft
- **Impact**: Attackers can gain SYSTEM or elevated administrator permissions
- **Status**: Exploit code publicly released, currently unpatched by Microsoft

## Affected Systems and Products

- **Flowise AI Platform**: Open-source platform for building custom LLM applications with over 12,000 exposed instances
- **WordPress Sites**: Sites using Ninja Forms File Uploads premium add-on vulnerable to file upload attacks
- **Docker Engine**: Container platforms running vulnerable Docker Engine versions
- **MikroTik and TP-Link Routers**: Small office/home office routers compromised in DNS hijacking campaigns
- **FortiClient**: Fortinet's endpoint security client software
- **Microsoft Office 365**: Authentication tokens targeted through router compromises
- **Windows Systems**: All Windows versions affected by the BlueHammer privilege escalation flaw
- **Snowflake Customers**: Multiple organizations affected through SaaS integrator breach
- **ComfyUI Instances**: Over 1,000 exposed ComfyUI stable diffusion platforms targeted for cryptomining
- **Rockwell/Allen-Bradley PLCs**: Programmable logic controllers in U.S. critical infrastructure

## Attack Vectors and Techniques

- **Remote Code Execution**: Direct exploitation of web application vulnerabilities for code execution
- **File Upload Attacks**: Bypassing authentication to upload malicious files leading to RCE
- **DNS Hijacking**: Compromising routers to redirect traffic and steal authentication credentials
- **Authorization Bypass**: Exploiting container platform vulnerabilities to bypass security controls
- **Zero-Day Exploitation**: Leveraging unknown vulnerabilities for initial access and privilege escalation
- **Supply Chain Attacks**: Targeting SaaS integrators to access downstream customer data
- **GPU RowHammer**: Novel GPUBreach attack technique using GDDR6 bit-flips for privilege escalation
- **Social Engineering**: AI-assisted campaigns targeting GitHub maintainers and software supply chains
- **Credential Theft**: Mass harvesting of Microsoft Office authentication tokens through router compromises
- **Cryptomining Botnet**: Automated targeting of exposed AI platform instances for cryptocurrency mining

## Threat Actor Activities

- **Storm-1175**: China-linked financially motivated group deploying Medusa ransomware using zero-day and N-day vulnerabilities in high-velocity attacks
- **APT28 (Forest Blizzard)**: Russian state-linked group conducting FrostArmada campaign, compromising MikroTik and TP-Link routers for DNS hijacking and Microsoft 365 credential theft
- **Russian Military Intelligence**: Linked hackers exploiting router vulnerabilities to steal Microsoft Office authentication tokens
- **Iranian-Linked Groups**: Targeting U.S. critical infrastructure organizations through Internet-exposed Rockwell/Allen-Bradley programmable logic controllers
- **Cybercrime Groups**: Multiple threat actors exploiting WordPress, Docker, and AI platform vulnerabilities for various malicious purposes including ransomware deployment and data theft
- **REvil and GandCrab Operators**: German authorities identified Russian nationals as leaders of major ransomware operations between 2019 and 2021