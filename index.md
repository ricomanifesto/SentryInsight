# Exploitation Report

Critical zero-day vulnerabilities and supply chain attacks dominate the current threat landscape. Cisco's Catalyst SD-WAN Manager faces active zero-day exploitation with no available patches, while SolarWinds Serv-U systems are being targeted to cause denial-of-service attacks. Simultaneously, sophisticated supply chain campaigns including the Miasma worm have compromised major repositories, and WordPress plugins are under active attack. The exploitation activity spans from enterprise infrastructure to consumer applications, with threat actors leveraging everything from unpatched zero-days to compromised browser applications.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity privilege escalation vulnerability in Cisco Catalyst SD-WAN Manager
- **Impact**: Attackers can gain root privileges and full system control
- **Status**: Actively exploited with no patch available
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Attackers can crash servers and cause denial of service
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog
- **CVE ID**: Not specified in articles

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in Everest Forms Pro WordPress plugin
- **Impact**: Complete site compromise through arbitrary code execution
- **Status**: Actively exploited against approximately 4,000 active installations
- **CVE ID**: Not specified in articles

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library
- **Impact**: Potential code execution and system compromise across video processing applications
- **Status**: Recently discovered through AI analysis, disclosure status unclear
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management platform vulnerable to privilege escalation
- **SolarWinds Serv-U**: Multi-protocol file server software experiencing DoS attacks
- **WordPress Sites**: Approximately 4,000 installations using Everest Forms Pro plugin
- **FFmpeg-based Applications**: Nearly all video processing software using FFmpeg library
- **Smart TVs and Consumer Devices**: IoT devices compromised through malicious apps for proxy networks
- **Gas Station Tank Gauges**: Over 900 automatic tank gauge systems exposed online across US critical infrastructure
- **Microsoft GitHub Repositories**: 73 repositories compromised by Miasma worm campaign
- **npm Ecosystem**: Supply chain attacks targeting over 50 legitimate packages
- **Hola Browser for Windows**: Compromised to deliver cryptocurrency miners
- **Microsoft IIS Servers**: Targeted by OP-512 threat cluster with custom web shells
- **Cloud Infrastructure**: 230 AWS, Google Cloud, and Azure servers hijacked by PCPJack

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities for privilege escalation and system compromise
- **Supply Chain Poisoning**: Miasma and IronWorm campaigns targeting software repositories and package managers
- **Web Shell Deployment**: Custom frameworks targeting Microsoft IIS servers for persistent access
- **Proxy Network Creation**: Smart TV compromise to create covert web-scraping infrastructure
- **Browser Compromise**: Supply chain attacks against browser applications to deliver malicious payloads
- **Critical Infrastructure Targeting**: Direct attacks on exposed industrial control systems
- **Cloud Server Hijacking**: Unauthorized access to cloud resources for SMTP relay networks
- **WordPress Plugin Exploitation**: Direct targeting of vulnerable plugins for site takeover

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm, Plenet, and AgentPSD malware to maintain persistent access to Microsoft 365 environments
- **TA4922 (Chinese Cybercrime Group)**: Expanding global operations beyond East Asia with diverse attack methods
- **OP-512 Threat Cluster**: Newly identified group targeting Microsoft IIS servers with custom web shell frameworks
- **PCPJack**: Cloud infrastructure hijacking to create covert SMTP email relay networks across major cloud providers
- **Miasma Campaign Operators**: Large-scale supply chain attacks targeting Microsoft GitHub repositories and npm packages
- **IronWorm Campaign**: Rust-based information stealing malware distributed through poisoned npm packages
- **Bright Data Operations**: Controversial use of consumer applications to create proxy networks through smart TV compromise
- **Asin Spyware Operators**: Targeting Arabic-speaking users through fake applications distributed via social media