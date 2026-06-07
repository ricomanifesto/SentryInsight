# Exploitation Report

Critical vulnerability exploitation is currently dominated by several high-severity flaws being actively targeted by threat actors. The most concerning incidents include a zero-day vulnerability in Cisco Catalyst SD-WAN Manager (CVE-2026-20245) being exploited in the wild with no patch available, allowing attackers to gain root-level privileges. Additionally, hackers are actively exploiting a critical flaw in the Everest Forms Pro WordPress plugin (CVE-2026-3300) to achieve complete site takeover capabilities. CISA has also added a SolarWinds Serv-U vulnerability to its Known Exploited Vulnerabilities catalog due to active exploitation for denial-of-service attacks. These incidents highlight a concerning trend of attackers targeting infrastructure and web platforms with immediate, high-impact exploitation capabilities.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager software that allows unauthorized privilege escalation
- **Impact**: Attackers can gain root-level access to compromised systems, enabling complete system control
- **Status**: Currently being actively exploited with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Allows threat actors to execute arbitrary code and achieve complete site compromise
- **Status**: Under active exploitation by threat actors
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Enables attackers to crash servers and disrupt file transfer services
- **Status**: Recently patched but actively exploited, added to CISA's KEV catalog

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library
- **Impact**: Potential arbitrary code execution and system compromise across multimedia applications
- **Status**: Recently disclosed by AI security research, patch status varies

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management platform vulnerable to privilege escalation
- **Everest Forms Pro WordPress Plugin**: Form management plugin with approximately 4,000 active installations
- **SolarWinds Serv-U**: Multi-protocol file transfer server software across enterprise environments
- **FFmpeg Media Library**: Core multimedia processing component embedded in numerous applications and systems
- **WordPress Websites**: Sites using vulnerable Everest Forms Pro plugin at risk of complete takeover
- **Fuel Tank Gauge Systems**: Over 900 automatic tank gauge systems across US gas stations exposed to internet attacks
- **Microsoft GitHub Repositories**: 73 repositories affected by Miasma worm supply chain attacks
- **npm Ecosystem**: Multiple packages compromised by IronWorm and Miasma worm variants
- **Hola Browser for Windows**: Compromised in supply chain attack delivering cryptocurrency miners

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN Manager vulnerability for privilege escalation
- **WordPress Plugin Exploitation**: Targeting vulnerable Everest Forms Pro installations for arbitrary code execution
- **Supply Chain Attacks**: Miasma and IronWorm worms targeting software repositories and package managers
- **Web Shell Deployment**: OP-512 threat cluster using custom web shell frameworks against Microsoft IIS servers
- **Internet-Exposed Systems**: Exploitation of publicly accessible fuel tank gauge systems across critical infrastructure
- **Polyfill Library Attacks**: Suspicious login prompts appearing on major websites including Toshiba and Muji
- **Credential Harvesting**: FIFA World Cup 2026-themed scams using fake sites and banking malware
- **Smart TV Proxy Networks**: Free apps converting smart TVs into web-scraping proxies without user knowledge

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying new malware including Brickstorm backdoor, Plenet, and AgentPSD to maintain access to Microsoft 365 environments
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack**: Hijacking 230+ cloud servers across AWS, Google Cloud, and Azure to create covert SMTP relay networks
- **TA4922 (Chinese Group)**: Expanding cybercrime operations globally beyond traditional East Asian targets
- **Miasma Worm Operators**: Conducting self-replicating supply chain attacks affecting major repositories including Microsoft GitHub
- **IronWorm Campaign**: Targeting npm ecosystem with Rust-based information stealers through malicious and poisoned packages
- **Fuel Infrastructure Attackers**: Exploiting exposed automatic tank gauge systems across US gas stations and critical infrastructure
- **Asin Spyware Operators**: Targeting Arabic-speaking users through fake news, PDF, and war map applications on Android platforms