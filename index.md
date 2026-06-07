# Exploitation Report

Critical vulnerabilities are under active exploitation across multiple enterprise environments, with threat actors targeting WordPress plugins, network infrastructure, and supply chain components. The most severe incidents include zero-day exploitation of Cisco SD-WAN systems enabling privilege escalation, active attacks against WordPress sites through a critical Everest Forms Pro vulnerability, and widespread supply chain compromises affecting npm packages and GitHub repositories. Additionally, attackers are exploiting SolarWinds Serv-U systems to crash servers, while sophisticated threat groups deploy custom malware frameworks to maintain persistent access in compromised networks.

## Active Exploitation Details

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the Everest Forms Pro WordPress plugin with approximately 4,000 active installations
- **Impact**: Allows threat actors to execute arbitrary code and achieve complete site compromise
- **Status**: Currently under active exploitation by attackers
- **CVE ID**: CVE-2026-3300

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity unpatched vulnerability in Cisco Catalyst SD-WAN Manager systems
- **Impact**: Enables attackers to escalate privileges to root level access
- **Status**: Actively exploited with no patch currently available
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Denial of Service Flaw
- **Description**: High-severity vulnerability in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Attackers can crash servers and cause denial of service conditions
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: Critical vulnerability allowing unauthenticated attackers to write files to the system
- **Impact**: Enables file system access and privilege escalation to root
- **Status**: Patched by Cisco with exploit code now publicly available
- **CVE ID**: CVE-2026-20230

## Affected Systems and Products

- **WordPress Sites**: Approximately 4,000 installations using Everest Forms Pro plugin vulnerable to complete takeover
- **Cisco SD-WAN Manager**: Enterprise network management systems exposed to privilege escalation attacks
- **SolarWinds Serv-U**: File server deployments susceptible to denial of service attacks
- **npm Package Ecosystem**: Over 50 packages compromised including 36 packages infected with IronWorm malware
- **GitHub Repositories**: 73 Microsoft repositories affected by Miasma worm attacks
- **FFmpeg Implementations**: Media processing libraries containing 21 newly discovered zero-day vulnerabilities
- **Smart TV Platforms**: Consumer devices being converted into web-scraping proxy networks
- **Cloud Infrastructure**: 230+ AWS, Google Cloud, and Azure servers hijacked for covert SMTP relay networks

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages distributed through npm with information-stealing capabilities
- **Self-Replicating Worms**: Miasma worm spreading across GitHub repositories in coordinated campaigns
- **Plugin Exploitation**: Direct targeting of WordPress plugin vulnerabilities for site takeover
- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities in enterprise network equipment
- **Social Engineering**: FIFA World Cup 2026-themed scams targeting users with fake sites and banking malware
- **Credential Harvesting**: Suspicious login prompts appearing on legitimate websites like Toshiba and Muji
- **Browser-Based Attacks**: Increasing focus on phishing, malicious extensions, and credential theft within browsers
- **Mobile Malware Distribution**: Android spyware targeting Arabic-speaking users through fake applications

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor and new malware variants (Plenet, AgentPSD) to maintain access to Microsoft 365 environments
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack Group**: Hijacking cloud servers across major providers to create covert SMTP relay networks for malicious email operations
- **Miasma Campaign Operators**: Conducting large-scale supply chain attacks affecting both npm packages and GitHub repositories
- **Magecart Operators**: Abusing Stripe's API infrastructure to host credit card-stealing payloads and exfiltrated payment data
- **Asin Spyware Developers**: Targeting Arabic-speaking mobile users through fake news, PDF, and war map applications
- **FIFA Scammers**: Launching early World Cup 2026-themed fraud campaigns with banking malware and credential theft