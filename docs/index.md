# Exploitation Report

Critical zero-day vulnerabilities are currently being actively exploited across multiple enterprise platforms, with threat actors targeting Microsoft Exchange Server, Cisco SD-WAN controllers, and WordPress plugins. The most severe active exploits include CVE-2026-42897 affecting on-premise Exchange Server installations and CVE-2026-20182 in Cisco Catalyst SD-WAN Controller, both achieving maximum CVSS 10.0 severity ratings. Supply chain attacks continue to pose significant risks, with the TanStack Mini Shai-Hulud campaign compromising OpenAI employee devices and malicious backdoors discovered in Node-IPC packages. Additionally, threat actors are rapidly exploiting newly disclosed vulnerabilities, with authentication bypass flaws in PraisonAI being targeted within hours of public disclosure.

## Active Exploitation Details

### Microsoft Exchange Server XSS Vulnerability
- **Description**: High-severity vulnerability in on-premise Exchange Server allowing arbitrary code execution through cross-site scripting (XSS) attacks
- **Impact**: Threat actors can execute arbitrary code on compromised Exchange servers
- **Status**: Actively exploited in the wild, mitigations provided by Microsoft
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: Maximum-severity authentication bypass flaw in Cisco's SD-WAN network control system
- **Impact**: Attackers can gain administrative access to SD-WAN controllers without authentication
- **Status**: Actively exploited in zero-day attacks, patches now available
- **CVE ID**: CVE-2026-20182

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the popular WordPress statistics plugin
- **Impact**: Hackers can obtain admin-level access to WordPress websites
- **Status**: Currently being exploited by threat actors to compromise websites

### PraisonAI Authentication Bypass
- **Description**: Authentication bypass vulnerability in the open-source multi-agent orchestration framework
- **Impact**: Unauthorized access to AI framework installations
- **Status**: Actively targeted within four hours of public disclosure
- **CVE ID**: CVE-2026-44338

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise installations vulnerable to XSS-based code execution
- **Cisco Catalyst SD-WAN Controller**: Network control systems susceptible to authentication bypass
- **WordPress Sites**: Installations using the Burst Statistics plugin face admin access compromise
- **PraisonAI Framework**: Open-source AI orchestration systems at risk of unauthorized access
- **Node-IPC Package**: Three versions containing stealer backdoors targeting developer secrets
- **OpenAI Corporate Environment**: Two employee devices compromised via TanStack supply chain attack
- **Windows 11 and Microsoft Edge**: Multiple zero-day exploits demonstrated at Pwn2Own Berlin 2026

## Attack Vectors and Techniques

- **Crafted Email Exploitation**: CVE-2026-42897 exploited through specially crafted emails to Exchange servers
- **Authentication Bypass**: Direct exploitation of authentication mechanisms in SD-WAN controllers and WordPress plugins
- **Supply Chain Compromise**: TanStack Mini Shai-Hulud attack targeting npm and PyPI packages
- **Backdoored Dependencies**: Malicious code injected into legitimate Node-IPC package versions
- **Rapid Vulnerability Exploitation**: Automated scanning and exploitation within hours of disclosure
- **Session Theft**: REMUS infostealer focusing on browser sessions and authentication tokens rather than passwords
- **Social Engineering via Teams**: KongTuke threat actors using Microsoft Teams for corporate network infiltration

## Threat Actor Activities

- **TanStack Supply Chain Attackers**: Compromised hundreds of npm and PyPI packages, affected OpenAI employee devices
- **Exchange Server Exploiters**: Unknown threat actors actively exploiting CVE-2026-42897 in targeted attacks
- **Cisco SD-WAN Attackers**: Limited but active exploitation of maximum-severity authentication bypass
- **REMUS Infostealer Operators**: Evolution toward Malware-as-a-Service model focusing on session theft
- **TeamPCP Group**: Threatening to leak Mistral AI source code repositories
- **KongTuke Initial Access Broker**: Shifted to Microsoft Teams for social engineering, achieving persistent access in five minutes
- **FrostyNeighbor APT**: Belarussian nation-state group targeting government organizations in Poland and Ukraine
- **Ghostwriter Group**: Belarus-aligned threat actor targeting Ukrainian government with geofenced PDF phishing and Cobalt Strike
- **WordPress Plugin Exploiters**: Mass exploitation campaigns targeting Burst Statistics plugin vulnerabilities
- **Pwn2Own Researchers**: Demonstrated 24 unique zero-days in Windows 11 and Microsoft Edge, earning $523,000 in awards