# Exploitation Report

Several critical vulnerabilities are currently under active exploitation, with Microsoft addressing two publicly known zero-day vulnerabilities in their March 2026 Patch Tuesday release alongside 77 other security flaws. CISA has flagged a recently patched Ivanti Endpoint Manager vulnerability as actively exploited in attacks, requiring immediate attention from federal agencies. Additionally, threat actors are leveraging FortiGate Next-Generation Firewall appliances as entry points to breach networks and steal service account credentials, while Chinese-nexus actors have shifted focus to Qatari entities amid geopolitical tensions. The exploitation landscape also includes supply chain attacks through compromised npm packages and sophisticated malware campaigns targeting enterprise environments.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities affecting Microsoft Windows operating systems and software components
- **Impact**: Potential for arbitrary code execution and system compromise depending on the specific vulnerabilities
- **Status**: Patched in March 2026 Patch Tuesday release, but previously exploited in the wild

### Ivanti Endpoint Manager Vulnerability
- **Description**: High-severity vulnerability in Ivanti Endpoint Manager (EPM) that was recently patched
- **Impact**: Allows attackers to compromise endpoint management systems
- **Status**: Currently being actively exploited in attacks according to CISA, patches available

### FortiGate NGFW Exploitation
- **Description**: Vulnerabilities in FortiGate Next-Generation Firewall appliances being used as network entry points
- **Impact**: Network breach and service account credential theft
- **Status**: Active exploitation campaign targeting FortiGate devices

### n8n Workflow Automation Platform
- **Description**: Two critical security flaws in the n8n workflow automation platform
- **Impact**: Arbitrary command execution and exposure of stored credentials
- **Status**: Now patched, but previously vulnerable to remote code execution

### nx npm Package Supply Chain Attack
- **Description**: Supply chain compromise of the nx npm package with stolen keys
- **Impact**: Complete cloud environment breach within 72 hours, AWS admin access compromise
- **Status**: Keys from previous supply chain attack being actively leveraged by UNC6426

## Affected Systems and Products

- **Microsoft Windows**: Operating systems affected by two zero-day vulnerabilities in March 2026 Patch Tuesday
- **Ivanti Endpoint Manager (EPM)**: High-severity vulnerability requiring immediate patching per CISA directive
- **FortiGate NGFW Appliances**: Next-Generation Firewall devices being exploited for network infiltration
- **n8n Workflow Platform**: Automation platform with critical RCE vulnerabilities
- **ASUS Routers**: Over 14,000 edge devices infected by KadNap malware for proxy botnet operations
- **SAP Enterprise Software**: Critical vulnerabilities allowing arbitrary code execution
- **HPE Aruba AOS-CX**: Multiple authentication and code execution vulnerabilities patched
- **Google Looker Studio**: Nine cross-tenant vulnerabilities enabling SQL injection attacks

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious Rust crates masquerading as time utilities to steal developer secrets from CI/CD pipelines
- **Zero-Day Exploitation**: Active exploitation of publicly disclosed Microsoft vulnerabilities before patches were applied
- **Network Device Compromise**: FortiGate firewall exploitation for lateral movement and credential theft
- **Botnet Operations**: KadNap malware targeting ASUS routers to create stealth proxy networks
- **EDR Evasion**: BlackSanta malware specifically designed to bypass endpoint detection and response systems
- **Mobile Malware**: BeatBanker Android malware posing as Starlink applications to hijack devices
- **Evasion Techniques**: Zombie ZIP method to conceal payloads in compressed files and avoid security detection

## Threat Actor Activities

- **UNC6426**: Leveraging stolen nx npm package keys to achieve complete AWS cloud environment compromise within 72 hours
- **Chinese-Nexus Actors**: Shifting operational focus to Qatari entities in response to Iranian conflict and geopolitical events
- **Russian-Speaking Actors**: Deploying BlackSanta EDR killer malware targeting HR departments for over a year
- **Sednit Group**: Russian-affiliated threat actor returning with sophisticated new malware toolkit after years of using simple implants
- **Southeast Asia Scam Operations**: Large-scale coordinated efforts with over 150,000 accounts disabled by Meta in partnership with international authorities