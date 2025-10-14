# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity, with multiple critical vulnerabilities being actively targeted by threat actors. Zero-day exploits in Microsoft Edge's Internet Explorer mode through the Chakra JavaScript engine have prompted Microsoft to implement access restrictions. Oracle E-Business Suite faces active exploitation with a newly disclosed vulnerability allowing unauthorized remote access by unauthenticated attackers. The RondoDox botnet is conducting widespread exploitation campaigns targeting over 50 vulnerabilities across 30+ vendors in an "exploit shotgun" approach. Additionally, threat actors are compromising SonicWall SSL VPN accounts using stolen credentials, affecting over 100 accounts in widespread attacks. Harvard University has been breached through an Oracle zero-day exploit, with the Clop ransomware gang claiming responsibility for the attack.

## Active Exploitation Details

### Internet Explorer Mode Zero-Day in Microsoft Edge
- **Description**: Zero-day vulnerabilities in the Chakra JavaScript engine within Internet Explorer mode in Microsoft Edge browser
- **Impact**: Attackers can gain access to target devices and use the legacy feature as a backdoor
- **Status**: Microsoft has implemented access restrictions to IE mode after receiving credible reports of exploitation in August 2025

### Oracle E-Business Suite Vulnerability
- **Description**: A critical security flaw in Oracle E-Business Suite that allows remote exploitation without authentication
- **Impact**: Unauthorized access to sensitive data and systems without requiring valid credentials
- **Status**: Oracle issued an emergency security update over the weekend to patch this vulnerability

### RondoDox Botnet Exploitation Campaign
- **Description**: Malware campaign exploiting over 50 vulnerabilities across more than 30 vendors
- **Impact**: Widespread compromise of edge devices and systems through automated exploitation
- **Status**: Active exploitation described as an "exploit shotgun" approach with hit-and-run tactics

## Affected Systems and Products

- **Microsoft Edge Browser**: Internet Explorer mode functionality compromised through Chakra JavaScript engine exploits
- **Oracle E-Business Suite**: Multiple versions affected by critical remote access vulnerability requiring emergency patching
- **SonicWall SSL VPN Devices**: Over 100 accounts compromised through credential-based attacks
- **Consumer Edge Devices**: Various manufacturers targeted by RondoDox botnet across 30+ vendors
- **Package Repositories**: npm, PyPI, and RubyGems ecosystems containing malicious packages

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in Chakra JavaScript engine and Oracle systems
- **Credential Stuffing**: Threat actors using stolen valid credentials to compromise SonicWall VPN accounts
- **Package Repository Poisoning**: Malicious packages distributed through npm, PyPI, and RubyGems sending data to Discord channels
- **DFIR Tool Abuse**: Velociraptor digital forensics tool weaponized in LockBit ransomware attacks
- **Remote Desktop Protocol Attacks**: Large-scale botnet targeting RDP services from over 100,000 IP addresses

## Threat Actor Activities

- **TA585**: Previously undocumented threat actor delivering MonsterV2 malware through phishing campaigns
- **Clop Ransomware Gang**: Claimed responsibility for Harvard University breach leveraging Oracle zero-day exploit
- **Storm-2603 (CL-CRI-1040)**: Likely orchestrating LockBit ransomware attacks using weaponized Velociraptor DFIR tool
- **RondoDox Operators**: Conducting widespread exploitation campaigns with automated "shotgun" approach across multiple vendors
- **SonicWall Attackers**: Unknown threat actors compromising SSL VPN accounts for widespread customer environment access
- **GXC Team Cybercrime Syndicate**: Dismantled by Spanish authorities with leader "GoogleXcoder" arrested