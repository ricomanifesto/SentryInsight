# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple attack vectors, with zero-day vulnerabilities in critical enterprise systems being actively targeted. Microsoft has taken emergency measures to restrict Internet Explorer mode access in Edge browser following credible reports of attackers leveraging zero-day exploits in the Chakra JavaScript engine. Simultaneously, Oracle has issued emergency patches for a newly disclosed E-Business Suite vulnerability that allows unauthenticated remote attackers to access sensitive data. Large-scale campaigns are compromising SonicWall VPN accounts using stolen credentials, while sophisticated botnets like RondoDox are weaponizing over 50 vulnerabilities across 30+ vendors in widespread exploitation campaigns.

## Active Exploitation Details

### Internet Explorer Mode Zero-Day Vulnerability
- **Description**: Zero-day exploits targeting the Chakra JavaScript engine in Internet Explorer mode within Microsoft Edge browser
- **Impact**: Attackers can gain unauthorized access to target devices through malicious JavaScript execution
- **Status**: Microsoft has restricted access to IE mode after receiving credible reports in August 2025 and implemented security enhancements

### Oracle E-Business Suite Critical Vulnerability
- **Description**: Remote code execution vulnerability in Oracle E-Business Suite allowing unauthorized data access
- **Impact**: Unauthenticated attackers can remotely exploit the flaw to access sensitive business data
- **Status**: Oracle released emergency security patch over the weekend; actively being exploited

### RondoDox Botnet Multi-Vendor Exploitation
- **Description**: Widespread exploitation campaign targeting over 50 vulnerabilities across 30+ vendors using "exploit shotgun" approach
- **Impact**: Mass compromise of edge devices and consumer systems for botnet recruitment
- **Status**: Active ongoing campaign with expanding target scope

## Affected Systems and Products

- **Microsoft Edge Browser**: Internet Explorer mode functionality compromised through Chakra JavaScript engine exploits
- **Oracle E-Business Suite**: All versions vulnerable to unauthenticated remote access attacks
- **SonicWall SSL VPN Devices**: Over 100 accounts compromised through credential-based attacks
- **Consumer Edge Devices**: Wide range of IoT and networking equipment targeted by RondoDox botnet
- **Remote Desktop Protocol Services**: Large-scale targeting from 100,000+ IP addresses in botnet attacks
- **Harvard University Systems**: Compromised through Oracle zero-day exploitation linked to Clop ransomware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Targeting unpatched vulnerabilities in Chakra JavaScript engine and Oracle systems
- **Credential-Based Attacks**: Using stolen valid credentials to compromise SonicWall VPN accounts
- **Botnet Operations**: Large-scale coordinated attacks using compromised IoT devices and consumer equipment
- **Ransomware Integration**: Velociraptor DFIR tool weaponized by Storm-2603 group for LockBit ransomware deployment
- **GitHub Abuse**: Astaroth banking trojan using GitHub infrastructure for command and control resilience
- **Discord C2 Communications**: ChaosBot malware leveraging Discord channels for backdoor operations

## Threat Actor Activities

- **Unknown Threat Actors**: Actively exploiting Internet Explorer mode zero-days and Oracle E-Business Suite vulnerabilities
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing Velociraptor DFIR tool in ransomware attacks and using legitimate incident response tools for persistent access
- **Clop Ransomware Gang**: Exploiting Oracle zero-day vulnerabilities to breach high-profile targets like Harvard University
- **RondoDox Botnet Operators**: Conducting mass exploitation campaigns across multiple vendor ecosystems using automated vulnerability scanning
- **GXC Team Cybercrime Syndicate**: Brazilian-led group dismantled by Spanish authorities, with leader "GoogleXcoder" arrested
- **ShinyHunters Group**: Extortion operations against Salesforce customers disrupted by federal law enforcement takedown