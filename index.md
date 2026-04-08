# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure through multiple vectors, with threat actors exploiting vulnerabilities in mobile device management platforms, cloud deployments, enterprise messaging systems, and network infrastructure. The most concerning developments include active attacks against Ivanti Endpoint Manager Mobile systems requiring immediate federal agency patching, exploitation of a 13-year-old Apache ActiveMQ vulnerability enabling remote code execution, and sophisticated campaigns by state-sponsored groups targeting routers and critical infrastructure. Iranian threat actors are actively compromising internet-exposed programmable logic controllers across U.S. critical infrastructure, while Russian APT28 operators are conducting large-scale DNS hijacking campaigns through compromised routers to steal Microsoft Office authentication tokens.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Critical Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti Endpoint Manager Mobile that has been actively exploited since January
- **Impact**: CISA has mandated federal agencies patch within four days due to active exploitation
- **Status**: Actively exploited, patch available, federal compliance deadline set
- **CVE ID**: Not specified in source articles

### Apache ActiveMQ Classic Remote Code Execution
- **Description**: 13-year-old remote code execution vulnerability in Apache ActiveMQ Classic that has gone undetected for over a decade
- **Impact**: Allows attackers to execute arbitrary commands on affected systems
- **Status**: Recently discovered, exploitation possible
- **CVE ID**: Not specified in source articles

### Flowise Platform Maximum Severity Vulnerability
- **Description**: Maximum-severity vulnerability in the open-source Flowise platform used for building custom LLM apps and agentic systems
- **Impact**: Enables arbitrary code execution on affected systems
- **Status**: Currently being exploited in active attacks
- **CVE ID**: CVE-2025-59528

### Ninja Forms WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress allowing arbitrary file uploads without authentication
- **Impact**: Can lead to remote code execution through malicious file uploads
- **Status**: Currently being exploited by attackers
- **CVE ID**: Not specified in source articles

### Docker Engine Authorization Bypass
- **Description**: High-severity vulnerability in Docker Engine allowing attackers to bypass authorization plugins under specific circumstances
- **Impact**: Permits unauthorized access to Docker host systems by circumventing AuthZ controls
- **Status**: Recently disclosed, patch available
- **CVE ID**: CVE-2026-34040

### Grafana AI Data Leakage Vulnerability
- **Description**: Vulnerability in Grafana's AI functionality that could be exploited to leak user data through malicious instructions
- **Impact**: Attackers could extract sensitive data by embedding malicious instructions on controlled web pages
- **Status**: Recently patched by Grafana
- **CVE ID**: Not specified in source articles

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: All versions prior to latest security update, affecting federal agency mobile device management
- **Apache ActiveMQ Classic**: All versions containing the 13-year-old vulnerability, widespread enterprise messaging infrastructure
- **Flowise Platform**: Open-source LLM application building platform installations
- **Ninja Forms WordPress Plugin**: Premium File Uploads add-on affecting WordPress websites
- **Docker Engine**: Container platform installations vulnerable to authorization bypass
- **Grafana**: Business intelligence and monitoring platform with AI features
- **MikroTik and TP-Link Routers**: Small office/home office routers targeted in DNS hijacking campaigns
- **Rockwell/Allen-Bradley PLCs**: Internet-exposed programmable logic controllers in U.S. critical infrastructure
- **Microsoft Office 365**: Authentication tokens targeted through compromised router infrastructure

## Attack Vectors and Techniques

- **Mobile Device Management Exploitation**: Direct attacks against enterprise mobile management platforms to gain network access
- **Legacy Vulnerability Exploitation**: Targeting decades-old unpatched vulnerabilities in enterprise messaging systems
- **Supply Chain Contamination**: Distribution of 1,700+ malicious packages across npm, PyPI, Go, and Rust ecosystems by North Korean actors
- **Router DNS Hijacking**: Compromising SOHO routers to redirect DNS queries and steal authentication credentials
- **Cloud Misconfiguration Attacks**: Targeting improperly configured cloud deployments with enhanced Chaos botnet variants
- **Critical Infrastructure Targeting**: Direct attacks against internet-exposed operational technology devices including PLCs
- **Container Authorization Bypass**: Exploiting Docker Engine vulnerabilities to gain unauthorized host system access
- **AI-Assisted Data Extraction**: Using malicious prompts embedded in web pages to extract sensitive information through AI systems

## Threat Actor Activities

- **APT28 (Forest Blizzard/Pawn Storm)**: Conducting large-scale DNS hijacking campaigns through compromised MikroTik and TP-Link routers to steal Microsoft Office 365 authentication tokens; deploying PRISMEX malware in spear-phishing campaigns targeting Ukraine and NATO allies
- **Iranian Threat Actors**: Systematically targeting U.S. critical infrastructure by compromising internet-exposed programmable logic controllers, causing operational disruption and financial losses across multiple sectors
- **Storm-1175**: Deploying Medusa ransomware at "high velocity" by exploiting both N-day and zero-day vulnerabilities in rapid attack campaigns
- **North Korean Contagious Interview Campaign**: Spreading 1,700+ malicious packages across major development ecosystems (npm, PyPI, Go, Rust, PHP) to target software developers and supply chains
- **Masjesu Botnet Operators**: Operating DDoS-for-hire service through Telegram, targeting global IoT devices for distributed denial-of-service attacks
- **Chaos Botnet Variant Developers**: Enhancing malware capabilities to target misconfigured cloud deployments while adding SOCKS proxy functionality for improved persistence