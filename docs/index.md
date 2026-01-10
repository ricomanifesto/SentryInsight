# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple critical infrastructure components and enterprise systems. Chinese-speaking threat actors are actively exploiting VMware ESXi zero-day vulnerabilities through compromised SonicWall VPN appliances, potentially having developed these exploits over a year before disclosure. HPE OneView is experiencing active exploitation of a maximum severity vulnerability enabling remote code execution on IT infrastructure management platforms. Meanwhile, Russian state-sponsored APT28 (Fancy Bear) continues credential harvesting campaigns targeting energy and policy organizations, while North Korean Kimsuky hackers have adopted QR code-based spear-phishing techniques against U.S. organizations. Additionally, a new China-linked threat group is exploiting edge device vulnerabilities to breach telecommunications providers, and threat actors are systematically hunting for misconfigured proxy servers to access commercial large language model services.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Critical zero-day vulnerabilities in VMware ESXi that allow virtual machine escape and host system compromise
- **Impact**: Attackers can escape virtual machine constraints and gain control of the underlying ESXi host infrastructure
- **Status**: Zero-day vulnerabilities actively exploited, exploit toolkit appears to have been developed over a year before disclosure

### HPE OneView Remote Code Execution Vulnerability
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities on IT infrastructure management systems, leading to potentially devastating consequences
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central Remote Code Execution Vulnerability
- **Description**: Critical security flaw in Trend Micro Apex Central on-premise Windows versions
- **Impact**: Allows attackers to execute arbitrary code with SYSTEM privileges
- **Status**: Recently patched after discovery, CVSS score of 9.8

### Edge Device Vulnerabilities in Telecommunications
- **Description**: Multiple vulnerabilities in edge devices used by telecommunications providers
- **Impact**: Enables breach of telecom infrastructure and expansion into Southeastern European organizations
- **Status**: Currently being exploited by sophisticated China-linked threat actors

## Affected Systems and Products

- **VMware ESXi**: Hypervisor infrastructure affected by zero-day exploits enabling virtual machine escape
- **HPE OneView**: IT infrastructure management platform experiencing active exploitation
- **Trend Micro Apex Central**: On-premise Windows versions vulnerable to remote code execution
- **SonicWall VPN Appliances**: Used as initial access vector for VMware ESXi attacks
- **Telecommunications Edge Devices**: Multiple vendors affected by China-linked exploitation campaigns
- **Misconfigured Proxy Servers**: Providing unauthorized access to commercial LLM services
- **Chrome Browser Extensions**: Fake AI extensions stealing data from 900,000 users
- **WhatsApp Messaging Platform**: Used as distribution vector for Astaroth banking trojan in Brazil

## Attack Vectors and Techniques

- **Virtual Machine Escape**: Exploitation of VMware ESXi zero-days to break out of virtual machine constraints
- **VPN Appliance Compromise**: Initial access through compromised SonicWall VPN devices
- **QR Code Spear-Phishing**: North Korean Kimsuky group using malicious QR codes in targeted campaigns
- **Credential Harvesting**: Russian APT28 conducting systematic credential theft operations
- **Proxy Server Hunting**: Systematic reconnaissance for misconfigured proxy servers providing LLM access
- **Malicious Browser Extensions**: Fake AI-powered Chrome extensions for data harvesting
- **WhatsApp Auto-Messaging**: Worm-based distribution of banking trojans through contact lists
- **Edge Device Exploitation**: Targeting telecommunications infrastructure through edge device vulnerabilities

## Threat Actor Activities

- **Chinese-Speaking Threat Actors**: Deploying VMware ESXi exploits through compromised VPN infrastructure, potentially maintaining access for over a year
- **APT28 (Fancy Bear)**: Russian state-sponsored group conducting credential harvesting against energy and policy organizations globally
- **Kimsuky (North Korean)**: Adopting QR code techniques in spear-phishing campaigns targeting U.S. organizations
- **China-Linked Telecommunications Group**: Sophisticated actor using Linux-based malware to target telecom providers, expanding operations into Southeastern Europe
- **Brazil-Focused Banking Trojan Operators**: Distributing Astaroth banking trojan through WhatsApp worm campaigns
- **LLM Access Abuse Groups**: Systematically hunting misconfigured proxies for unauthorized access to commercial AI services
- **Chrome Extension Fraudsters**: Creating fake AI extensions to harvest ChatGPT and DeepSeek user data from 900,000 victims