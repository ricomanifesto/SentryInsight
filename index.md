# Exploitation Report

Current threat landscapes reveal several critical exploitation campaigns targeting enterprise infrastructure and applications. Notable activities include widespread attacks against RDP services by a massive botnet spanning over 100,000 IP addresses, active exploitation of Oracle E-Business Suite vulnerabilities requiring emergency patches, and a zero-day attack against Gladinet file sharing software. The RondoDox botnet has significantly expanded its operations to weaponize over 50 vulnerabilities across more than 30 vendors, while threat actors continue to compromise SonicWall VPN accounts using stolen credentials in large-scale campaigns. Additionally, sophisticated ransomware groups are leveraging legitimate incident response tools like Velociraptor as backdoors, and attackers are exploiting Microsoft Edge's Internet Explorer mode as an unauthorized access vector.

## Active Exploitation Details

### Oracle E-Business Suite Vulnerability
- **Description**: A critical vulnerability in Oracle E-Business Suite that allows unauthorized access to sensitive data without authentication
- **Impact**: Remote unauthenticated attackers can exploit this flaw to access sensitive business data
- **Status**: Oracle issued an emergency security update over the weekend to address this vulnerability
- **CVE ID**: CVE-2025-11371

### Gladinet Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Gladinet CentreStack and Triofox file sharing products
- **Impact**: Local attackers can access system files without authentication
- **Status**: Currently being actively exploited in the wild
- **CVE ID**: CVE-2025-11371

### Microsoft Edge Internet Explorer Mode Abuse
- **Description**: Threat actors are exploiting the backward compatibility feature in Microsoft Edge's IE mode
- **Impact**: Attackers can use this legacy feature as an unauthorized backdoor
- **Status**: Microsoft has revamped IE mode after receiving credible reports of abuse in August 2025

### RondoDox Botnet Multi-Vendor Exploits
- **Description**: Malware campaigns distributing RondoDox botnet targeting vulnerabilities across multiple vendors
- **Impact**: Mass exploitation of over 50 flaws across 30+ vendors in consumer edge devices
- **Status**: Actively exploiting vulnerabilities in a "shotgun" approach for maximum impact

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise business applications vulnerable to remote unauthenticated attacks
- **Gladinet CentreStack and Triofox**: File sharing software products with active zero-day exploitation
- **SonicWall SSL VPN**: Over 100 accounts compromised through credential-based attacks
- **Microsoft Edge**: Internet Explorer mode feature being abused as backdoor access
- **Remote Desktop Protocol (RDP)**: Services across the United States targeted by massive botnet
- **Consumer Edge Devices**: Multiple vendors affected by RondoDox botnet exploitation campaigns
- **Velociraptor DFIR Tool**: Open-source incident response tool weaponized for ransomware attacks

## Attack Vectors and Techniques

- **Credential-Based Attacks**: Threat actors using stolen, valid credentials to compromise SonicWall VPN accounts
- **Botnet Operations**: Massive multi-country botnet leveraging over 100,000 IP addresses for RDP targeting
- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in file sharing software
- **Tool Weaponization**: Legitimate DFIR tools like Velociraptor repurposed as persistent backdoors
- **Legacy Feature Abuse**: Exploitation of backward compatibility features in modern browsers
- **Mass Vulnerability Scanning**: RondoDox employing "exploit shotgun" approach across multiple vendors

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group abusing Velociraptor DFIR tool in LockBit ransomware attacks for persistent network access
- **Clop Ransomware Gang**: Listed Harvard University on data leak site following alleged Oracle zero-day exploitation
- **GXC Team**: Cybercrime syndicate dismantled by Spanish authorities, with leader "GoogleXcoder" arrested
- **ShinyHunters**: Extortion site shut down by federal authorities, though threats against Salesforce victims remain active
- **RondoDox Operators**: Conducting widespread campaigns across consumer edge devices using automated exploitation techniques
- **Multi-Country Botnet**: Coordinated RDP targeting campaign spanning international infrastructure