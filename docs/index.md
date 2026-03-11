# Exploitation Report

The current threat landscape reveals multiple critical exploitation campaigns targeting enterprise infrastructure and supply chain components. The most significant activity includes active exploitation of n8n workflow automation vulnerabilities, with CISA mandating immediate federal remediation due to confirmed attacks in the wild. Parallel campaigns show sophisticated threat actors leveraging supply chain compromises through malicious npm packages and exploiting FortiGate network appliances for credential theft and lateral movement. Additional concerns include Iranian-linked wiper attacks against critical infrastructure, advanced EDR evasion techniques, and compromised edge devices being enrolled into proxy botnets for malicious traffic routing.

## Active Exploitation Details

### n8n Remote Code Execution Vulnerability
- **Description**: Critical vulnerability in the n8n workflow automation platform allowing arbitrary command execution
- **Impact**: Attackers can achieve complete system compromise and execute malicious code remotely
- **Status**: Actively exploited in the wild, patches available, CISA mandates federal agency remediation

### FortiGate Network Appliance Compromise
- **Description**: Threat actors exploiting FortiGate Next-Generation Firewall devices as network entry points
- **Impact**: Complete network breach capabilities with service account credential theft and lateral movement
- **Status**: Active campaign targeting enterprise networks through compromised firewall appliances

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities in Microsoft products
- **Impact**: Various exploitation capabilities depending on specific vulnerabilities
- **Status**: Patched in March 2026 Patch Tuesday, previously exploited in the wild

### nx npm Supply Chain Compromise
- **Description**: Supply chain attack targeting the nx npm package with stolen authentication keys
- **Impact**: Complete cloud environment compromise within 72 hours, AWS administrative access
- **Status**: Historical compromise being leveraged for ongoing attacks by UNC6426 threat group

## Affected Systems and Products

- **n8n Workflow Platform**: Workflow automation systems requiring immediate patching
- **FortiGate NGFW Appliances**: Network security devices being exploited as attack vectors
- **Microsoft Windows Systems**: Various Windows components affected by 79 vulnerabilities including 2 zero-days
- **HPE Aruba AOS-CX**: Network operating system with critical authentication bypass vulnerabilities
- **Asus Routers**: Edge devices infected by KadNap malware for botnet operations
- **npm Package Registry**: JavaScript development environments targeted through malicious packages
- **Rust Crates Repository**: Development pipelines compromised through malicious time utility packages
- **Stryker Medical Systems**: Healthcare technology infrastructure targeted by wiper malware
- **Android Devices**: Mobile platforms targeted by BeatBanker malware disguised as Starlink applications

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages deployed through npm registry and Rust crates targeting developer environments
- **Wiper Malware Deployment**: Destructive attacks against critical infrastructure using data-wiping capabilities
- **EDR Evasion**: BlackSanta malware specifically designed to disable endpoint detection and response systems
- **Zombie ZIP Technique**: Novel compression-based evasion method to bypass security scanning solutions
- **AI Browser Manipulation**: Social engineering attacks targeting AI-powered autonomous browsing systems
- **Firewall Exploitation**: Network appliances compromised to facilitate credential theft and network traversal
- **Mobile Application Impersonation**: Malware distribution through fake application stores and brand impersonation

## Threat Actor Activities

- **UNC6426**: Leveraging historical npm supply chain compromise to achieve rapid cloud environment takeover within 72 hours
- **Handala Group**: Iranian-linked hacktivist organization conducting wiper attacks against medical technology companies
- **PhantomRaven Campaign**: Ongoing supply chain attacks through 88+ malicious npm packages targeting developer credentials
- **Russian-Speaking Actors**: Targeting HR departments with BlackSanta EDR killer malware for over one year
- **Sednit (APT28)**: Russian state-affiliated group returning with sophisticated new malware toolkit after period of reduced activity
- **Chinese Nexus Actors**: Pivoting targeting focus to Qatar amid regional geopolitical tensions
- **Southeast Asian Scam Centers**: Operating 150,000+ fraudulent accounts across Meta platforms for financial crimes