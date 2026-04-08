# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems across various sectors. Iran-linked hackers are actively disrupting U.S. critical infrastructure by targeting internet-exposed programmable logic controllers (PLCs), while Russian APT28 actors are conducting global DNS hijacking campaigns through compromised routers. Multiple maximum-severity vulnerabilities are under active exploitation, including CVE-2025-59528 in Flowise AI platforms and CVE-2026-34040 in Docker Engine. The threat landscape also includes zero-day exploitation by China-linked Storm-1175 group deploying Medusa ransomware, authentication bypass vulnerabilities in Fortinet products, and critical flaws in WordPress plugins enabling remote code execution.

## Active Exploitation Details

### Flowise Remote Code Execution Vulnerability
- **Description**: Maximum-severity vulnerability in the open-source Flowise AI platform for building custom LLM apps and agentic systems
- **Impact**: Allows execution of arbitrary code on affected systems
- **Status**: Actively exploited in attacks with over 12,000 instances exposed
- **CVE ID**: CVE-2025-59528

### Docker Engine Authorization Bypass
- **Description**: High-severity vulnerability in Docker Engine that permits bypassing authorization plugins (AuthZ)
- **Impact**: Attackers can gain unauthorized host access under specific circumstances
- **Status**: Recently disclosed vulnerability with bypass capabilities
- **CVE ID**: CVE-2026-34040

### Ninja Forms WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress
- **Impact**: Allows uploading arbitrary files without authentication, leading to remote code execution
- **Status**: Currently being exploited by hackers

### FortiClient Zero-Day Authentication Bypass
- **Description**: Authentication bypass vulnerability in Fortinet's FortiClient product
- **Impact**: Allows bypassing authentication mechanisms
- **Status**: Emergency patch issued by Fortinet for active exploitation
- **CVE ID**: CVE-2026-35616

### BlueHammer Windows Zero-Day
- **Description**: Unpatched Windows privilege escalation vulnerability
- **Impact**: Enables attackers to gain SYSTEM or elevated administrator permissions
- **Status**: Exploit code publicly released by disgruntled researcher

### Grafana AI Information Disclosure
- **Description**: Vulnerability in Grafana's AI functionality that could leak user data
- **Impact**: AI systems could ingest malicious instructions and return sensitive data to attacker servers
- **Status**: Recently patched by Grafana

## Affected Systems and Products

- **Programmable Logic Controllers (PLCs)**: Rockwell/Allen-Bradley controllers in U.S. critical infrastructure
- **Routers**: MikroTik and TP-Link routers compromised for DNS hijacking campaigns
- **Flowise AI Platform**: Over 12,000 exposed instances vulnerable to remote code execution
- **Docker Engine**: Container systems vulnerable to authorization bypass
- **WordPress Sites**: Sites using Ninja Forms File Uploads premium add-on
- **FortiClient**: Fortinet's endpoint protection software
- **Windows Systems**: Systems vulnerable to privilege escalation via BlueHammer exploit
- **ComfyUI Instances**: Over 1,000 exposed instances targeted for cryptomining botnet
- **Grafana Deployments**: AI-enabled Grafana installations
- **Snowflake Customers**: Multiple companies affected through SaaS integrator breach

## Attack Vectors and Techniques

- **Internet-Exposed Device Targeting**: Direct exploitation of PLCs and routers accessible from the internet
- **DNS Hijacking**: Modification of router DNS settings to redirect traffic and steal authentication tokens
- **Remote Code Execution**: Exploitation of file upload vulnerabilities to execute malicious code
- **Authorization Bypass**: Circumventing security controls in containerized environments
- **Privilege Escalation**: Exploiting Windows vulnerabilities to gain elevated system access
- **Social Engineering**: Sophisticated campaigns targeting software maintainers and developers
- **Supply Chain Attacks**: AI-assisted targeting of GitHub repositories and package maintainers
- **Cryptomining Botnet**: Compromising AI platforms for cryptocurrency mining operations
- **Token Theft**: Harvesting Microsoft Office authentication tokens through router compromises

## Threat Actor Activities

- **Iran-Linked Hackers**: Actively targeting U.S. critical infrastructure through internet-exposed OT devices and PLCs
- **APT28 (Forest Blizzard)**: Russian state-linked group conducting global DNS hijacking campaigns using compromised routers
- **Storm-1175**: China-linked financially motivated group deploying Medusa ransomware at high velocity using zero-day and N-day vulnerabilities
- **Russian Military Intelligence**: Exploiting router vulnerabilities to mass harvest Microsoft Office authentication tokens
- **Unknown Threat Actors**: Exploiting Flowise vulnerabilities for remote code execution and targeting ComfyUI instances for cryptomining operations
- **Disgruntled Researcher**: Released Windows zero-day exploit publicly after private disclosure issues
- **Supply Chain Attackers**: Using AI-assisted techniques to target GitHub repositories and NPM packages