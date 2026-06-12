# Exploitation Report

Critical zero-day and recently patched vulnerabilities are under active exploitation across multiple platforms, with threat actors targeting enterprise systems, AI platforms, and network infrastructure. The most severe activity involves the ShinyHunters group exploiting a critical Oracle PeopleSoft zero-day (CVE-2026-35273) that allows unauthenticated remote code execution, successfully breaching over 100 organizations including multiple universities. Concurrent exploitation campaigns are targeting Ivanti Sentry gateways, AI development platforms, and Chrome browsers, while sophisticated threat actors continue to expand botnet operations for cyber reconnaissance activities.

## Active Exploitation Details

### Oracle PeopleSoft Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Oracle PeopleSoft Suite allowing unauthenticated remote code execution
- **Impact**: Complete system compromise, data theft, and extortion attacks targeting enterprise systems
- **Status**: Actively exploited by ShinyHunters group across 100+ organizations, Oracle has issued mitigation guidance
- **CVE ID**: CVE-2026-35273

### Ivanti Sentry Maximum Severity Flaw
- **Description**: Maximum severity vulnerability in Ivanti Sentry secure mobile gateways
- **Impact**: Attackers can execute code with root privileges on Internet-exposed gateways
- **Status**: Recently patched but now under active exploitation

### Langflow Path Traversal Vulnerability
- **Description**: High-severity path traversal flaw in the AI development platform Langflow
- **Impact**: Allows attackers to write arbitrary files on exposed servers, leading to potential remote code execution
- **Status**: Actively exploited for unauthenticated RCE attacks
- **CVE ID**: CVE-2026-5027

### Microsoft Exchange Server Zero-Day
- **Description**: Zero-day vulnerability in Microsoft Exchange Server enabling cross-site scripting attacks
- **Impact**: Allows threat actors to execute arbitrary JavaScript code targeting Outlook Web Access users
- **Status**: Actively exploited in attacks, recently patched by Microsoft

### Chrome, Cisco, and Arista Network Vulnerabilities
- **Description**: Multiple critical vulnerabilities across Chrome browsers, Cisco systems, and Arista network equipment
- **Impact**: Various impacts including remote code execution and system compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

## Affected Systems and Products

- **Oracle PeopleSoft Suite**: Enterprise resource planning systems across universities and organizations
- **Ivanti Sentry**: Internet-exposed secure mobile gateways with maximum severity vulnerabilities
- **Langflow Platform**: Open-source AI development platforms with path traversal exposures
- **Microsoft Exchange Server**: Email servers vulnerable to cross-site scripting attacks via Outlook Web Access
- **Chrome Browsers**: Web browsers with actively exploited security flaws
- **Cisco Systems**: Network infrastructure equipment with critical vulnerabilities
- **Arista Networks**: Network devices added to federal exploitation watchlist
- **Windows BitLocker**: Encryption bypass vulnerabilities affecting Windows systems
- **OpenClaw AI Agent**: Self-hosted AI agents vulnerable to code execution and data leakage

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Threat actors leveraging unpatched vulnerabilities for immediate system access
- **Unauthenticated Remote Code Execution**: Direct system compromise without authentication requirements
- **Path Traversal Attacks**: File system manipulation leading to arbitrary file writes and code execution
- **Cross-Site Scripting**: JavaScript injection targeting web application users
- **BitLocker Bypass**: GreatXML exploit technique using recovery partition XML files
- **AI Agent Manipulation**: Tricking AI systems into executing malicious code and leaking sensitive data
- **Supply Chain Targeting**: Miasma worm framework briefly exposed for credential theft operations
- **Botnet Reconnaissance**: Expanded targeting of military and critical infrastructure networks

## Threat Actor Activities

- **ShinyHunters Group**: Conducting large-scale data theft and extortion campaigns using Oracle PeopleSoft zero-day, targeting over 100 organizations with focus on universities
- **The Gentlemen Ransomware**: Operating as second most active ransomware group with 478 claimed victims, employing worm-like spreading capabilities and aggressive recruitment strategies
- **OceanLotus (APT32)**: Vietnam-aligned threat actor conducting FireAnt campaigns targeting domestic investors using SPECTRALVIPER backdoor
- **China-Linked JDY Botnet**: Expanding operations to over 1,500 compromised SOHO devices for cyber reconnaissance against U.S. military networks
- **AudiA6 Cryptocurrency Service**: Dismantled money laundering operation that processed over $380 million for ransomware groups and cybercriminals