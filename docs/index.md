# Exploitation Report

Critical exploitation activity is currently targeting multiple sectors with significant impact across enterprise environments. Active zero-day exploitation has been confirmed against Cisco SD-WAN infrastructure, enabling root privilege escalation on network management systems. Supply chain attacks are proliferating through the npm ecosystem with new Rust-based malware variants, while WordPress sites face widespread compromise through plugin vulnerabilities. Infrastructure systems including fuel tank monitoring networks and Microsoft IIS servers are under targeted attack, demonstrating threat actors' focus on operational technology and web infrastructure. These coordinated campaigns leverage both known vulnerabilities and sophisticated new malware frameworks to establish persistent access across diverse environments.

## Active Exploitation Details

### Cisco SD-WAN Manager Zero-Day
- **Description**: High-severity vulnerability in Cisco Catalyst SD-WAN Manager allowing unauthorized privilege escalation
- **Impact**: Attackers can achieve root-level access to network management infrastructure
- **Status**: Currently being exploited in active attacks, unpatched at time of disclosure
- **CVE ID**: CVE-2026-20245

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: Vulnerability allowing unauthenticated network attackers to write arbitrary files to the system and escalate to root privileges
- **Impact**: Complete system compromise with root access
- **Status**: Patched by Cisco, but exploit code has been made publicly available
- **CVE ID**: CVE-2026-20230

### SolarWinds Serv-U Server Crash Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U that allows attackers to crash servers
- **Impact**: Service disruption and potential denial of service attacks
- **Status**: Recently patched, but now actively exploited by threat actors

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in WordPress plugin with approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution
- **Status**: Actively exploited by threat actors for website takeovers

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management infrastructure vulnerable to privilege escalation
- **Cisco Unified Communications Manager**: Enterprise communication systems at risk of file write attacks
- **SolarWinds Serv-U**: File transfer servers susceptible to crash attacks
- **WordPress Sites**: Installations using Everest Forms Pro plugin facing critical compromise risk
- **Microsoft IIS Servers**: Web servers targeted by custom web shell frameworks
- **npm Ecosystem**: Node.js package repositories compromised with malicious packages
- **Automatic Tank Gauge Systems**: Over 900 fuel monitoring systems across US critical infrastructure exposed online
- **Cloud Infrastructure**: AWS, Google Cloud, and Microsoft Azure servers hijacked for covert operations
- **Hola Browser**: Windows version compromised in supply chain attack
- **Polyfill Services**: Websites using compromised JavaScript libraries showing malicious login prompts

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in network infrastructure
- **Supply Chain Poisoning**: Malicious packages injected into legitimate software repositories
- **Web Shell Deployment**: Custom frameworks for maintaining persistent access to web servers
- **Credential Harvesting**: Malicious login prompts deployed through compromised web services
- **Cryptocurrency Mining**: Unauthorized deployment of mining software through compromised applications
- **Email Relay Networks**: Hijacked cloud servers repurposed for covert SMTP operations
- **Plugin Exploitation**: WordPress plugin vulnerabilities leveraged for complete site compromise
- **Infrastructure Targeting**: Direct attacks against exposed industrial control systems

## Threat Actor Activities

- **UNC5221**: Chinese espionage group deploying Brickstorm backdoor and new malware variants including Plenet and AgentPSD for persistent Microsoft 365 access
- **OP-512**: Previously unreported threat cluster targeting Microsoft IIS servers with sophisticated web shell frameworks
- **PCPJack**: Threat actor hijacking cloud infrastructure across AWS, Google Cloud, and Azure to create covert SMTP relay networks
- **TA4922**: Chinese cybercrime group expanding global operations beyond East Asia with diverse attack methodologies
- **IronWorm Operators**: Supply chain attackers deploying Rust-based information stealers through npm package ecosystem
- **Magecart Campaigns**: Credit card theft operations abusing Stripe API infrastructure to host stolen payment data
- **Asin Spyware Group**: Targeting Arabic-speaking users through fake news applications and PDF readers on Android platforms