# Exploitation Report

Critical vulnerabilities are currently being exploited across enterprise platforms, with the most severe being a maximum severity SCIM flaw in Grafana Enterprise (CVE-2025-41115) that enables admin impersonation and privilege escalation. Threat actors are actively exploiting unpatched vulnerabilities in Ray AI frameworks for GPU cryptomining operations, conducting sophisticated espionage campaigns using custom malware, and targeting enterprise VPN infrastructure through massive scanning operations. Additionally, attackers are leveraging OAuth abuse vectors against Salesforce customers and deploying novel command-and-control techniques through browser notifications and Ethereum-based infrastructure.

## Active Exploitation Details

### Grafana Enterprise SCIM Vulnerability
- **Description**: Maximum severity security flaw in Grafana's System for Cross-domain Identity Management (SCIM) implementation that allows attackers to treat new users as administrators
- **Impact**: Complete privilege escalation, user impersonation, and unauthorized administrative access to Grafana Enterprise installations
- **Status**: Security updates have been released by Grafana Labs
- **CVE ID**: CVE-2025-41115

### Ray AI Framework Vulnerability
- **Description**: Two-year-old unpatched security flaw in the Ray open-source artificial intelligence framework being exploited by ShadowRay 2.0 botnet
- **Impact**: Complete compromise of AI clusters with NVIDIA GPUs, conversion into self-spreading cryptocurrency mining botnet
- **Status**: Actively exploited despite being known for two years, patches available but not widely applied

### SonicWall SonicOS SSLVPN Vulnerability
- **Description**: High-severity security flaw in SonicWall's SonicOS SSLVPN implementation that allows denial-of-service attacks
- **Impact**: Attackers can crash vulnerable SonicWall firewalls, disrupting network security and connectivity
- **Status**: Patch released by SonicWall, customers urged to update immediately

## Affected Systems and Products

- **Grafana Enterprise**: All versions with SCIM implementation prior to security update
- **Ray AI Framework**: Open-source AI framework installations with NVIDIA GPU clusters
- **SonicWall SonicOS**: SSLVPN-enabled firewall appliances running vulnerable firmware
- **Palo Alto GlobalProtect**: VPN portals experiencing massive reconnaissance scanning
- **Salesforce Platform**: Customer instances connected to compromised Gainsight applications
- **Windows Systems**: Targets of Tsundere botnet using game-themed social engineering lures
- **Italian Rail Infrastructure**: FS Italiane Group systems compromised via Almaviva IT services provider
- **Chinese Organizations**: Primary targets of PlushDaemon router infections for software update hijacking

## Attack Vectors and Techniques

- **SCIM Protocol Abuse**: Exploitation of identity management protocols to escalate privileges in enterprise environments
- **AI Framework Exploitation**: Targeting distributed computing frameworks to build GPU-powered cryptocurrency mining operations
- **VPN Portal Reconnaissance**: Mass scanning campaigns with 2.3 million sessions targeting GlobalProtect infrastructure
- **OAuth Token Abuse**: Unauthorized access to customer data through compromised third-party application integrations
- **Router-Based Software Hijacking**: Infection of networking equipment to intercept and modify legitimate software updates
- **Browser Notification Hijacking**: Novel command-and-control technique using Matrix Push tool to abuse browser notification systems
- **Game-Themed Social Engineering**: Distribution of malware through gaming-related lures targeting Windows users
- **Ethereum-Based C2**: Use of blockchain infrastructure for command-and-control communications

## Threat Actor Activities

- **APT24**: China-linked espionage group conducting three-year campaign using previously undocumented BADAUDIO malware, targeting Taiwan and over 1,000 domains with sophisticated persistence mechanisms
- **PlushDaemon Operators**: Chinese state-sponsored APT group infecting routers to hijack software updates, primarily targeting domestic Chinese organizations while evading international attention
- **ShadowRay 2.0 Botnet**: Cryptocurrency mining operation exploiting Ray AI framework vulnerabilities to build self-spreading GPU botnets
- **Tsundere Botnet**: Active since mid-2025, targeting Windows users with JavaScript-based malware distributed through gaming lures and utilizing Ethereum blockchain for command-and-control
- **Scattered Spider**: British teenagers involved in Transport for London breach pleading not guilty to charges related to August 2024 attack causing millions in damages
- **Italian Rail Attacker**: Threat actor claiming to steal 2.3TB of data from FS Italiane Group through Almaviva IT services provider compromise
- **Gainsight-Linked Attackers**: Unauthorized actors exploiting OAuth applications to access Salesforce customer data through compromised Gainsight integrations