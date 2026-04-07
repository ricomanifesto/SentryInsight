# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems, with threat actors leveraging both zero-day vulnerabilities and known flaws to conduct high-impact attacks. The most concerning activities include Russian military intelligence units exploiting router vulnerabilities to steal Microsoft Office authentication tokens, Chinese threat actors deploying Medusa ransomware through zero-day exploits, and active exploitation of maximum-severity vulnerabilities in AI platforms. Iranian hackers are simultaneously targeting critical infrastructure through programmable logic controllers, while widespread DNS hijacking campaigns compromise thousands of SOHO routers globally.

## Active Exploitation Details

### Flowise RCE Vulnerability
- **Description**: Maximum-severity remote code execution vulnerability in the open-source Flowise platform for building custom LLM applications and agentic systems
- **Impact**: Allows attackers to execute arbitrary code on affected systems
- **Status**: Currently under active exploitation with over 12,000 exposed instances identified
- **CVE ID**: CVE-2025-59528

### FortiClient Authentication Bypass
- **Description**: Zero-day authentication bypass vulnerability in Fortinet's FortiClient software
- **Impact**: Enables attackers to bypass authentication mechanisms
- **Status**: Emergency patch issued by Fortinet following active exploitation
- **CVE ID**: CVE-2026-35616

### Docker Engine Authorization Bypass
- **Description**: High-severity vulnerability allowing attackers to bypass authorization plugins (AuthZ) under specific circumstances
- **Impact**: Permits unauthorized access to Docker host systems
- **Status**: Vulnerability disclosed with potential for host system compromise
- **CVE ID**: CVE-2026-34040

### BlueHammer Windows Privilege Escalation
- **Description**: Unpatched Windows privilege escalation vulnerability leaked by a disgruntled researcher
- **Impact**: Allows attackers to gain SYSTEM or elevated administrator permissions
- **Status**: Exploit code publicly released, no patch available from Microsoft

### Storm-1175 Zero-Day Exploits
- **Description**: Combination of zero-day and N-day vulnerabilities weaponized by China-based threat actors
- **Impact**: Enables rapid deployment of Medusa ransomware in high-velocity attacks
- **Status**: Active exploitation observed in targeted ransomware campaigns

## Affected Systems and Products

- **Flowise AI Platform**: Open-source LLM application builder with 12,000+ exposed instances
- **MikroTik Routers**: SOHO routers compromised for DNS hijacking operations
- **TP-Link Routers**: Consumer routers exploited in APT28 campaigns
- **Rockwell/Allen-Bradley PLCs**: Programmable logic controllers targeted in Iranian attacks
- **FortiClient Software**: Fortinet's client security solution affected by zero-day
- **Docker Engine**: Containerization platform vulnerable to authorization bypass
- **ComfyUI Instances**: Over 1,000 exposed stable diffusion platform instances targeted
- **Microsoft 365 Environments**: 300+ Israeli organizations targeted in password spraying
- **GitHub Repositories**: Used as command-and-control infrastructure in DPRK attacks

## Attack Vectors and Techniques

- **DNS Hijacking**: Modification of router DNS settings to redirect traffic to malicious servers
- **Authentication Token Theft**: Harvesting Microsoft Office tokens through compromised routers
- **Password Spraying**: Automated credential attacks against Microsoft 365 accounts
- **Remote Code Execution**: Exploitation of maximum-severity RCE vulnerabilities
- **Privilege Escalation**: Windows system compromise through leaked zero-day exploits
- **Cryptocurrency Mining**: Botnet deployment for cryptomining operations
- **Supply Chain Attacks**: AI-assisted targeting of GitHub misconfigurations
- **GPU Memory Exploitation**: GPUBreach attacks using GDDR6 bit-flips for system compromise
- **Social Engineering**: Industrialized campaigns targeting software maintainers

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Russian military intelligence group conducting global DNS hijacking through compromised SOHO routers, specifically targeting MikroTik and TP-Link devices
- **Storm-1175**: China-based financially motivated group deploying Medusa ransomware using zero-day and N-day exploits in high-velocity attacks
- **Iranian Threat Actors**: Targeting U.S. critical infrastructure through Internet-exposed Rockwell/Allen-Bradley programmable logic controllers
- **FrostArmada Campaign**: APT28 operation hijacking local traffic from routers to steal Microsoft 365 credentials, disrupted by international law enforcement
- **DPRK-Linked Groups**: North Korean threat actors using GitHub as command-and-control infrastructure in multi-stage attacks targeting South Korean organizations
- **Iranian Password Spraying Campaign**: Targeting 300+ Israeli Microsoft 365 organizations amid ongoing Middle East conflict
- **Cryptomining Botnet Operators**: Targeting over 1,000 exposed ComfyUI instances for cryptocurrency mining operations