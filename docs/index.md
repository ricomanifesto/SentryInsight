# Exploitation Report

Critical exploitation activity is currently affecting enterprise environments across multiple attack vectors. Notable incidents include the UNC6426 threat group leveraging supply chain compromises to gain AWS administrative access within 72 hours, while CISA has flagged several actively exploited vulnerabilities in enterprise software including SolarWinds, Ivanti, and VMware Workspace One products. Microsoft has addressed two zero-day vulnerabilities in their March 2026 Patch Tuesday release, and threat actors are increasingly targeting edge devices, cloud configurations, and development environments through sophisticated campaigns including malicious package repositories, EDR evasion techniques, and social engineering attacks.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities in Windows operating systems
- **Impact**: Attackers can exploit these flaws for privilege escalation and system compromise
- **Status**: Patched in Microsoft's March 2026 Patch Tuesday update, but previously exploited in the wild

### Ivanti Endpoint Manager Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager (EPM) software
- **Impact**: Allows attackers to compromise endpoint management infrastructure
- **Status**: Recently patched but now actively exploited according to CISA

### SolarWinds Vulnerability
- **Description**: Security flaw in SolarWinds software products
- **Impact**: Enables unauthorized access and potential network compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### VMware Workspace One Vulnerability
- **Description**: Security vulnerability affecting VMware Workspace One platform
- **Impact**: Allows attackers to compromise virtual desktop infrastructure
- **Status**: Actively exploited and flagged by CISA for immediate patching

### HPE AOS-CX Authentication Bypass
- **Description**: Critical vulnerability in HPE Aruba Networking AOS-CX operating system allowing admin password resets
- **Impact**: Complete administrative takeover of network infrastructure devices
- **Status**: Recently patched by HPE, multiple authentication and code execution issues addressed

### Google Looker Studio Cross-Tenant Vulnerabilities
- **Description**: Nine cross-tenant vulnerabilities dubbed "LeakyLooker" flaws in Google Looker Studio
- **Impact**: Enables attackers to run arbitrary SQL queries on victims' databases and exfiltrate sensitive data
- **Status**: Disclosed vulnerabilities that could allow cross-tenant data access

## Affected Systems and Products

- **Microsoft Windows**: Multiple versions affected by zero-day vulnerabilities and 79 total flaws in March 2026 updates
- **Ivanti Endpoint Manager**: EPM software actively targeted by threat actors
- **SolarWinds Products**: Various SolarWinds software solutions under active exploitation
- **VMware Workspace One**: Virtual desktop infrastructure platform compromised
- **HPE Aruba AOS-CX**: Network operating system with critical authentication bypass flaws
- **Google Looker Studio**: Business intelligence platform vulnerable to cross-tenant attacks
- **FortiGate NGFW**: Next-Generation Firewall appliances used as network entry points
- **ASUS Routers**: Edge networking devices infected by KadNap malware botnet
- **Salesforce Experience Cloud**: Misconfigured public sites targeted for data exposure
- **npm Package Repository**: Supply chain attacks targeting nx npm packages
- **Rust Crates Repository**: Five malicious Rust packages targeting CI/CD pipelines

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Exploitation of compromised nx npm packages to steal AWS credentials and achieve administrative access
- **Malicious Package Distribution**: Five malicious Rust crates masquerading as time utilities to steal .env file data from CI/CD pipelines
- **Edge Device Compromise**: KadNap malware targeting over 14,000 ASUS routers to create proxy botnets for malicious traffic
- **EDR Evasion**: BlackSanta malware specifically designed to disable endpoint detection and response solutions
- **Social Engineering**: Microsoft Teams phishing campaigns delivering A0Backdoor malware through Quick Assist remote access
- **Zombie ZIP Technique**: New compression-based evasion method to bypass security tools and deliver malware payloads
- **Configuration Exploitation**: Targeting overly permissive Salesforce cloud configurations and guest user access controls
- **Cross-Tenant Attacks**: Exploiting multi-tenant cloud services to access unauthorized data across different organizations

## Threat Actor Activities

- **UNC6426**: Advanced threat group executed complete cloud environment breach within 72 hours using stolen supply chain credentials to gain AWS administrative access
- **APT28 (Russian State-Sponsored)**: Deployed customized BEARDSHELL and COVENANT malware variants for long-term surveillance operations against Ukrainian military personnel
- **Sednit (Russian-Affiliated)**: Resurfaced with sophisticated new toolkit after years of using simple implants, demonstrating evolved capabilities
- **Russian-Speaking Actors**: Conducted year-long campaign targeting HR departments with BlackSanta EDR killer malware to hijack organizational workflows
- **Anonymous Threat Actors**: Exploited FortiGate devices as network entry points to breach victim networks and steal service account credentials
- **Cybercriminals**: Created fake Android applications posing as Starlink apps to distribute BeatBanker malware and hijack mobile devices
- **Package Repository Attackers**: Published malicious Rust crates and deployed AI bots to exploit CI/CD pipelines for developer secret theft