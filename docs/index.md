# Exploitation Report

Current threat activity reveals sophisticated exploitation campaigns targeting critical infrastructure and enterprise systems. Chinese-speaking threat actors are exploiting VMware ESXi zero-day vulnerabilities developed over a year ago to escape virtual machines after initial access through compromised SonicWall VPN appliances. Simultaneously, a maximum severity HPE OneView vulnerability (CVE-2025-37164) is being actively exploited in the wild, enabling remote code execution on IT infrastructure management platforms. State-sponsored groups including Russian APT28 and North Korean Kimsuky are conducting credential harvesting campaigns using novel techniques like malicious QR codes in spear-phishing operations. Additionally, threat actors are exploiting misconfigured proxy servers to gain unauthorized access to commercial large language model services, while fake AI Chrome extensions have compromised data from approximately 900,000 users.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in VMware ESXi being exploited by Chinese-speaking threat actors to escape virtual machines
- **Impact**: Virtual machine escape, potential lateral movement across virtualized infrastructure
- **Status**: Vulnerabilities were developed and exploited approximately one year before disclosure, indicating sophisticated long-term exploitation

### HPE OneView Critical Remote Code Execution
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central Critical RCE Vulnerability
- **Description**: Critical security flaw in on-premise Windows versions of Apex Central allowing arbitrary code execution
- **Impact**: Attackers can execute arbitrary code with SYSTEM privileges
- **Status**: Patched by Trend Micro, scored 9.8 CVSS

### Misconfigured Proxy Server Exploitation
- **Description**: Systematic targeting of misconfigured proxy servers to access commercial LLM services
- **Impact**: Unauthorized access to paid AI services, potential data exposure
- **Status**: Ongoing campaign targeting proxy misconfigurations

## Affected Systems and Products

- **VMware ESXi**: Virtual machine hypervisor platforms vulnerable to escape attacks
- **HPE OneView**: IT infrastructure management platform (on-premise deployments)
- **Trend Micro Apex Central**: On-premise Windows versions of security management console
- **SonicWall VPN Appliances**: Used as initial access vector for ESXi exploitation
- **Chrome Browser Extensions**: Fake AI extensions affecting approximately 900,000 users
- **Proxy Servers**: Misconfigured instances providing unauthorized LLM access
- **Telecommunications Infrastructure**: Edge devices targeted by China-linked actors
- **WhatsApp Messaging Platform**: Used for Astaroth banking trojan distribution in Brazil

## Attack Vectors and Techniques

- **Virtual Machine Escape**: Exploitation of ESXi hypervisor vulnerabilities to break containment
- **VPN Appliance Compromise**: Initial access through compromised SonicWall devices
- **QR Code Phishing**: Malicious QR codes embedded in spear-phishing campaigns
- **Credential Harvesting**: Targeting energy and policy organizations for credential theft
- **Proxy Misconfiguration Abuse**: Systematic scanning for improperly configured proxy servers
- **Chrome Extension Impersonation**: Fake AI extensions mimicking legitimate tools
- **WhatsApp Worm Distribution**: Auto-messaging contacts to spread banking trojans
- **Edge Device Exploitation**: Targeting telecommunications provider edge infrastructure

## Threat Actor Activities

- **Chinese-Speaking APT Groups**: Conducting sophisticated ESXi exploitation campaigns and telecommunications targeting in Southeastern Europe
- **Russian APT28 (Fancy Bear)**: Running credential-stealing campaigns against Turkish energy agencies and policy organizations using basic but effective techniques
- **North Korean Kimsuky**: Deploying malicious QR codes in spear-phishing operations targeting U.S. organizations
- **Brazilian Cybercriminals**: Distributing Astaroth banking trojan through WhatsApp worm campaigns with contact auto-messaging
- **Unknown Threat Actors**: Operating fake AI Chrome extensions and systematically exploiting proxy misconfigurations for LLM access