# Exploitation Report

Critical exploitation activity is currently targeting multiple high-impact vulnerabilities across enterprise infrastructure and AI platforms. Most concerning is the active exploitation of CVE-2025-59528, a maximum severity RCE vulnerability in Flowise AI platform with over 12,000 exposed instances globally. Russian state-linked APT28 continues sophisticated operations targeting SOHO routers for DNS hijacking to steal Microsoft 365 credentials, while Storm-1175 deploys Medusa ransomware at unprecedented speed using zero-day vulnerabilities. Additional threats include a newly leaked Windows privilege escalation zero-day called "BlueHammer" and CVE-2026-35616, an authentication bypass flaw in FortiClient requiring emergency patching.

## Active Exploitation Details

### Flowise RCE Vulnerability
- **Description**: Maximum severity remote code execution vulnerability in the open-source Flowise platform for building custom LLM applications and agentic systems
- **Impact**: Attackers can execute arbitrary code on vulnerable instances, potentially leading to complete system compromise
- **Status**: Actively exploited in the wild with over 12,000 instances exposed globally
- **CVE ID**: CVE-2025-59528

### FortiClient Authentication Bypass
- **Description**: Authentication bypass vulnerability in Fortinet's FortiClient requiring emergency patching
- **Impact**: Allows attackers to bypass authentication mechanisms in FortiClient deployments
- **Status**: Zero-day vulnerability with active exploitation prompting emergency patch release
- **CVE ID**: CVE-2026-35616

### BlueHammer Windows Privilege Escalation
- **Description**: Unpatched Windows privilege escalation vulnerability leaked by disgruntled researcher
- **Impact**: Allows attackers to gain SYSTEM or elevated administrator permissions on Windows systems
- **Status**: Zero-day with public exploit code available, reported privately to Microsoft but remains unpatched

### Docker Authorization Bypass
- **Description**: High-severity vulnerability allowing attackers to bypass authorization plugins (AuthZ) under specific circumstances
- **Impact**: Permits unauthorized access to Docker environments and potential host system compromise
- **Status**: Recently disclosed vulnerability requiring immediate patching
- **CVE ID**: CVE-2026-34040

### SOHO Router Vulnerabilities
- **Description**: Known flaws in older Internet routers being exploited for mass harvesting of authentication tokens
- **Impact**: Enables theft of Microsoft Office/365 authentication tokens and DNS hijacking capabilities
- **Status**: Actively exploited by Russian military intelligence units and APT28 in global campaigns

## Affected Systems and Products

- **Flowise AI Platform**: Open-source platform for building custom LLM applications with 12,000+ exposed instances
- **FortiClient**: Fortinet's client security software affected by authentication bypass vulnerability
- **Windows Systems**: All Windows versions vulnerable to BlueHammer privilege escalation exploit
- **Docker Engine**: Container platform affected by authorization bypass vulnerability
- **MikroTik Routers**: SOHO routers compromised in DNS hijacking campaigns
- **TP-Link Routers**: Consumer routers targeted for DNS settings manipulation
- **Rockwell/Allen-Bradley PLCs**: Programmable logic controllers on critical infrastructure networks
- **ComfyUI Platform**: Over 1,000 exposed instances targeted for cryptomining botnet recruitment
- **Microsoft 365 Environments**: Enterprise email and productivity platforms targeted in credential theft
- **Grafana**: AI feature vulnerabilities patched to prevent data leakage

## Attack Vectors and Techniques

- **DNS Hijacking**: Modification of router DNS settings to redirect traffic to attacker-controlled servers
- **Remote Code Execution**: Direct exploitation of RCE vulnerabilities for immediate system access
- **Authentication Token Theft**: Mass harvesting of Microsoft 365 tokens through compromised routers
- **Privilege Escalation**: Exploitation of Windows vulnerabilities to gain SYSTEM-level access
- **Social Engineering**: Sophisticated, AI-assisted campaigns targeting GitHub maintainers and developers
- **Password Spraying**: Automated credential attacks against Microsoft 365 organizations
- **Cryptomining Botnet**: Recruitment of exposed AI platform instances for cryptocurrency mining
- **Supply Chain Attacks**: AI-assisted targeting of GitHub repositories and NPM packages
- **GPU RowHammer**: GPUBreach attack technique enabling privilege escalation via GDDR6 bit-flips

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Russian state-linked group conducting global DNS hijacking campaigns targeting MikroTik and TP-Link routers to steal Microsoft 365 credentials
- **Storm-1175**: Financially motivated cybercrime group deploying Medusa ransomware at high velocity using zero-day and N-day vulnerability combinations
- **Iranian Threat Actors**: Targeting Internet-exposed Rockwell/Allen-Bradley PLCs on U.S. critical infrastructure networks and conducting password spraying against 300+ Israeli Microsoft 365 organizations
- **Chinese-linked Groups**: Storm-1175 attributed to China-based actors exploiting zero-day vulnerabilities for rapid ransomware deployment
- **Cryptomining Groups**: Targeting over 1,000 exposed ComfyUI instances for botnet recruitment and cryptocurrency mining operations
- **Russian Military Intelligence**: Exploiting router vulnerabilities for authentication token harvesting operations against Microsoft Office users