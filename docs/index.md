# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and infrastructure systems across various sectors. The most significant threats include active zero-day exploitation of Cisco SD-WAN systems, widespread supply chain attacks targeting npm packages with IronWorm malware, and sophisticated campaigns against WordPress plugins and industrial control systems. Threat actors are leveraging compromised browser extensions, exploiting exposed fuel tank gauge systems, and conducting targeted spyware campaigns against Arabic-speaking users. Additionally, Chinese APT groups are deploying new persistent malware to maintain access to Microsoft 365 environments while cybercriminals are hijacking cloud infrastructure for covert operations.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity zero-day vulnerability allowing unauthenticated attackers to escalate privileges to root level
- **Impact**: Complete system compromise with root-level access to SD-WAN infrastructure
- **Status**: Currently unpatched and actively exploited in the wild
- **CVE ID**: CVE-2026-20245

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: Authentication bypass vulnerability allowing unauthenticated network attackers to write files and escalate to root privileges
- **Impact**: Complete system compromise through arbitrary file write leading to privilege escalation
- **Status**: Patched by Cisco with public exploit code now available
- **CVE ID**: CVE-2026-20230

### SolarWinds Serv-U Server Crash Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U that allows attackers to crash servers
- **Impact**: Denial of service attacks causing server crashes and service disruption
- **Status**: Recently patched but now actively exploited by hackers

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in WordPress plugin with approximately 4,000 active installations
- **Impact**: Arbitrary code execution leading to complete site compromise
- **Status**: Actively exploited by threat actors for site takeovers

### Polyfill Supply Chain Compromise
- **Description**: Malicious JavaScript injection through compromised polyfill services affecting major websites
- **Impact**: Credential theft through suspicious login prompts on legitimate websites
- **Status**: Active compromise affecting Toshiba and Muji websites

### IronWorm npm Supply Chain Attack
- **Description**: Rust-based information stealer targeting npm ecosystem through malicious and poisoned packages
- **Impact**: Developer credential theft and supply chain propagation
- **Status**: Active campaign affecting over 50 legitimate packages and 36 infected npm packages

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Zero-day vulnerability with active exploitation
- **Cisco Unified Communications Manager**: File write vulnerability with public exploits
- **SolarWinds Serv-U**: Server crash vulnerability under active attack
- **WordPress Everest Forms Pro Plugin**: Critical flaw in 4,000+ installations
- **npm Package Ecosystem**: Over 50 packages compromised with IronWorm malware
- **Microsoft Internet Information Services (IIS)**: Targeted by OP-512 threat cluster
- **Microsoft 365 Environments**: Compromised by Chinese APT UNC5221
- **Automatic Tank Gauge Systems**: Over 900 US systems exposed to attacks
- **Android Devices**: Arabic users targeted by Asin spyware
- **Hola Browser for Windows**: Supply chain compromise delivering cryptocurrency miners
- **AWS, Google Cloud, Azure**: 230 servers hijacked for SMTP relay network

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN systems
- **Supply Chain Poisoning**: Compromised npm packages and browser extensions
- **Web Shell Deployment**: Custom framework targeting Microsoft IIS servers
- **Credential Harvesting**: Polyfill-based attacks injecting malicious login forms
- **Mobile Spyware Distribution**: Fake news, PDF, and war map applications on Android
- **Industrial System Exploitation**: Direct attacks on exposed fuel tank gauge systems
- **Cloud Infrastructure Hijacking**: Unauthorized access to cloud servers for email relay networks
- **Social Engineering**: FIFA World Cup 2026-themed scams and fake websites

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor and new malware (Plenet, AgentPSD) in Microsoft 365 environments for persistent access
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for sustained access
- **PCPJack**: Hijacking 230 AWS, Google Cloud, and Azure servers to create covert SMTP email relay networks
- **TA4922 (Chinese Group)**: Expanding cybercrime operations globally beyond traditional East Asian targets
- **IronWorm Campaign**: Sophisticated supply chain attacks targeting npm ecosystem with Rust-based malware
- **Asin Spyware Operators**: Targeting Arabic-speaking users through fake applications and social engineering
- **Magecart Groups**: New campaign abusing Stripe's API infrastructure to host stolen payment card data