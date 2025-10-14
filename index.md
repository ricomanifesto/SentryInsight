# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting enterprise systems and infrastructure. Zero-day vulnerabilities in Microsoft Edge's Internet Explorer mode and Oracle E-Business Suite are being actively exploited by threat actors to gain unauthorized system access. The Chakra JavaScript engine exploitation in Edge browsers has prompted Microsoft to implement emergency security restrictions. Additionally, widespread botnet operations are leveraging over 50 vulnerabilities across 30+ vendors, while credential-based attacks against VPN infrastructure and RDP services continue to pose significant risks to organizational security.

## Active Exploitation Details

### Microsoft Edge Internet Explorer Mode Zero-Day
- **Description**: Zero-day vulnerability in the Chakra JavaScript engine within Microsoft Edge's Internet Explorer mode
- **Impact**: Allows attackers to gain unauthorized access to target devices and establish persistent backdoors
- **Status**: Microsoft has implemented emergency security restrictions on IE mode access in Edge browser

### Oracle E-Business Suite Vulnerability
- **Description**: Critical security flaw in Oracle E-Business Suite allowing remote exploitation by unauthenticated attackers
- **Impact**: Enables unauthorized access to sensitive data and system compromise without authentication
- **Status**: Oracle issued emergency security patch over the weekend

### RondoDox Botnet Exploitation Campaign
- **Description**: Large-scale botnet operation exploiting over 50 vulnerabilities across more than 30 vendors
- **Impact**: Mass compromise of edge devices and consumer infrastructure through "exploit shotgun" approach
- **Status**: Active ongoing campaign targeting multiple vendor products simultaneously

## Affected Systems and Products

- **Microsoft Edge**: Internet Explorer mode functionality compromised through Chakra JavaScript engine exploitation
- **Oracle E-Business Suite**: Critical vulnerability allowing unauthenticated remote access to sensitive data
- **SonicWall SSL VPN**: Over 100 accounts compromised using stolen valid credentials
- **Remote Desktop Protocol (RDP) Services**: Targeted by massive multi-country botnet from 100,000+ IP addresses
- **Consumer Edge Devices**: Over 30 vendors affected by RondoDox botnet exploitation campaign
- **IoT Devices**: Compromised devices on major US ISPs including AT&T, Comcast, and Verizon powering DDoS attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in widely-used enterprise software
- **Credential-Based Attacks**: Use of stolen valid credentials to compromise VPN and remote access infrastructure
- **Mass Vulnerability Exploitation**: Shotgun approach targeting multiple vulnerabilities across diverse vendor ecosystems
- **Legitimate Tool Abuse**: Weaponization of Velociraptor DFIR tool for persistence in ransomware attacks
- **GitHub Infrastructure Abuse**: Astaroth banking trojan using GitHub repositories for command and control resilience
- **Discord C2 Communications**: ChaosBot malware leveraging Discord channels for victim control

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group abusing Velociraptor DFIR tools in LockBit ransomware campaigns
- **Clop Ransomware Gang**: Exploiting Oracle zero-day vulnerabilities, with Harvard University among recent victims
- **RondoDox Operators**: Conducting widespread botnet operations targeting edge devices across multiple vendors
- **GXC Team Syndicate**: Spanish authorities dismantled this cybercrime group and arrested its Brazilian leader "GoogleXcoder"
- **ShinyHunters**: Federal authorities shut down their Salesforce extortion site, though threats against victims remain active
- **Astaroth Banking Trojan Operators**: Leveraging GitHub infrastructure for resilient command and control operations