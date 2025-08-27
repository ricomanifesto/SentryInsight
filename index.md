# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise and government environments. Citrix NetScaler infrastructure faces active zero-day exploitation with CVE-2025-7775 being weaponized in the wild, while Git version control systems are under attack through an arbitrary code execution vulnerability. Threat actors are conducting sophisticated supply chain attacks, including the breach of Salesloft to steal OAuth tokens for downstream Salesforce data theft. Additionally, coordinated scanning campaigns against Microsoft Remote Desktop Services suggest potential preparation for exploiting an undisclosed vulnerability, while state-level cyberattacks have disrupted Nevada's government operations.

## Active Exploitation Details

### Citrix NetScaler Zero-Day Vulnerability
- **Description**: A critical security flaw affecting NetScaler ADC and NetScaler Gateway technologies that allows attackers to compromise enterprise network infrastructure
- **Impact**: Complete compromise of network gateway systems, potential for lateral movement and data exfiltration across enterprise networks
- **Status**: Actively exploited in the wild, patches have been released by Citrix
- **CVE ID**: CVE-2025-7775

### Git Arbitrary Code Execution Flaw
- **Description**: A vulnerability in the Git distributed version control system that enables arbitrary code execution on affected systems
- **Impact**: Attackers can execute malicious code on systems running vulnerable Git installations, potentially compromising development environments and source code repositories
- **Status**: Actively exploited according to CISA warning, exploitation confirmed in the wild

### Salesloft OAuth Token Theft
- **Description**: Breach of the Salesloft sales automation platform specifically targeting OAuth and refresh tokens from Drift chat agent integration with Salesforce
- **Impact**: Attackers can pivot to customer Salesforce environments and exfiltrate sensitive business data using stolen authentication tokens
- **Status**: Confirmed breach with active data theft operations targeting downstream customers

## Affected Systems and Products

- **Citrix NetScaler ADC**: Network application delivery controllers used for load balancing and application acceleration
- **Citrix NetScaler Gateway**: Secure remote access solutions for enterprise environments
- **Git Version Control System**: Distributed version control system used across development environments
- **Salesloft Platform**: Sales automation and customer relationship management platform
- **Salesforce Environments**: Customer relationship management systems accessed through compromised OAuth tokens
- **Microsoft Remote Desktop Services**: Remote access services experiencing coordinated scanning activity
- **Nevada State Government Systems**: Government IT infrastructure and online platforms affected by cyberattack

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Citrix NetScaler vulnerabilities to gain initial access
- **Supply Chain Compromise**: Targeting third-party platforms like Salesloft to access downstream customer environments
- **OAuth Token Theft**: Stealing authentication tokens to maintain persistent access to cloud-based services
- **Coordinated Network Scanning**: Large-scale reconnaissance operations against Remote Desktop Services infrastructure
- **Ransomware Deployment**: Hook Android Trojan evolution to include ransomware-style attacks on mobile devices

## Threat Actor Activities

- **Citrix-Targeting Groups**: Threat actors actively exploiting NetScaler zero-day vulnerabilities for enterprise network compromise
- **Supply Chain Attackers**: Sophisticated actors conducting multi-stage attacks through compromised service providers to reach high-value targets
- **RDP Scanning Campaigns**: Coordinated threat actors conducting massive scanning operations against Microsoft Remote Desktop Services, potentially preparing for exploitation of undisclosed vulnerabilities
- **State-Level Attackers**: Advanced persistent threat actors targeting government infrastructure, successfully disrupting Nevada state operations and forcing office closures
- **Mobile Malware Operators**: Cybercriminals distributing evolved Hook Android Trojan with ransomware capabilities through GitHub and other platforms