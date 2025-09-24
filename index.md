# Exploitation Report

Critical vulnerabilities are currently being exploited in the wild across multiple platforms and systems. The most significant threats include active exploitation of Pandoc CVE-2025-51591 targeting AWS EC2 instances to steal IAM credentials, state-sponsored attacks against Libraesva Email Security Gateway systems, and federal agencies being compromised through unpatched GeoServer instances. Additional concerning activity includes the emergence of the ShadowV2 botnet exploiting misconfigured Docker containers, ransomware attacks disrupting European airports, and multiple supply chain attacks targeting the npm ecosystem. Critical vulnerabilities in SolarWinds Web Help Desk (CVE-2025-26399) and Supermicro BMC firmware are also creating significant security risks for enterprise environments.

## Active Exploitation Details

### Pandoc Vulnerability
- **Description**: A security flaw in the Linux utility Pandoc that enables server-side request forgery attacks
- **Impact**: Attackers can infiltrate Amazon Web Services environments and steal EC2 IAM credentials by targeting AWS Instance Metadata Service (IMDS)
- **Status**: Actively exploited in the wild, cloud security researchers have confirmed exploitation
- **CVE ID**: CVE-2025-51591

### Libraesva Email Security Gateway Vulnerability
- **Description**: A security flaw in Libraesva's Email Security Gateway (ESG) solution affecting email security infrastructure
- **Impact**: Enables unauthorized access to email security systems and potential compromise of email communications
- **Status**: Actively exploited by state-sponsored threat actors, emergency security update released

### SolarWinds Web Help Desk RCE
- **Description**: A critical remote code execution vulnerability in SolarWinds Web Help Desk software
- **Impact**: Allows attackers to execute arbitrary commands on susceptible systems without authentication
- **Status**: Critical severity, hotfix released after third patching attempt
- **CVE ID**: CVE-2025-26399

### GeoServer Exploitation
- **Description**: Unpatched vulnerability in GeoServer instances used to breach federal networks
- **Impact**: Complete network compromise of U.S. federal civilian executive branch agency systems
- **Status**: Successfully exploited to breach federal agency, CISA confirmed incident

## Affected Systems and Products

- **Pandoc Utility**: Linux-based systems using the Pandoc document conversion tool, particularly in AWS cloud environments
- **Libraesva Email Security Gateway**: Email security infrastructure using ESG solutions
- **SolarWinds Web Help Desk**: Enterprise help desk and IT service management platforms
- **GeoServer**: Federal agency geographic information systems and mapping services
- **Supermicro BMC**: Baseboard Management Controller firmware on Supermicro hardware systems
- **Docker Containers**: Misconfigured AWS Docker daemon implementations
- **npm Ecosystem**: Node.js package management systems and JavaScript development environments
- **European Airport Systems**: Check-in and boarding system infrastructure across multiple European airports

## Attack Vectors and Techniques

- **Server-Side Request Forgery (SSRF)**: Exploitation of Pandoc vulnerability to access AWS IMDS endpoints
- **Supply Chain Attacks**: Malicious npm packages using QR codes and SEO poisoning techniques
- **SEO Poisoning**: BadIIS malware campaign using search engine manipulation to redirect traffic and plant web shells
- **Container Exploitation**: ShadowV2 botnet targeting exposed Docker daemons for DDoS-for-hire services
- **Rootkit Deployment**: Advanced persistent threats targeting SonicWall SMA100 series devices
- **Ransomware Operations**: Coordinated attacks disrupting critical transportation infrastructure
- **Social Engineering**: Scattered Spider group using sophisticated phishing and identity theft techniques

## Threat Actor Activities

- **State-Sponsored Groups**: Actively exploiting Libraesva ESG vulnerabilities for intelligence gathering and persistent access
- **Scattered Spider**: Cybercrime syndicate responsible for $115 million in ransomware payments, targeting major corporations and cloud services
- **Chinese-Speaking Actors**: Conducting Operation Rewrite SEO poisoning campaign using BadIIS malware for traffic redirection and web shell installation
- **ShadowV2 Operators**: Running DDoS-for-hire botnet services by exploiting misconfigured cloud infrastructure
- **European Cryptocurrency Fraud Ring**: €100 million investment fraud scheme spanning 23 countries with five arrests made
- **Federal Agency Attackers**: Unknown threat actors successfully compromising U.S. government systems through GeoServer exploitation