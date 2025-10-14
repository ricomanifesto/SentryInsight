# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and organizations through sophisticated attack campaigns. Zero-day vulnerabilities in Microsoft's Internet Explorer mode within Edge browser are being actively exploited by threat actors to gain unauthorized access to target systems. Oracle E-Business Suite has been compromised through a critical vulnerability that allows unauthenticated remote attackers to access sensitive data. The RondoDox botnet has emerged as a significant threat, weaponizing over 50 vulnerabilities across more than 30 vendors in a shotgun-style exploitation approach. Additionally, widespread credential-based attacks against SonicWall VPN services have compromised over 100 accounts, while threat actors are increasingly abusing legitimate security tools like Velociraptor for ransomware operations. A massive botnet campaign is also targeting Remote Desktop Protocol services across the United States from over 100,000 IP addresses.

## Active Exploitation Details

### Internet Explorer Mode Zero-Day Vulnerability
- **Description**: Zero-day exploits targeting the Chakra JavaScript engine within Microsoft Edge's Internet Explorer mode
- **Impact**: Allows attackers to gain unauthorized access to target devices and potentially execute arbitrary code
- **Status**: Microsoft has restricted access to IE mode in Edge browser and implemented security measures

### Oracle E-Business Suite Critical Vulnerability
- **Description**: Remote code execution vulnerability in Oracle E-Business Suite that can be exploited by unauthenticated attackers
- **Impact**: Unauthorized access to sensitive data and potential system compromise
- **Status**: Oracle has issued emergency security patches over the weekend

### RondoDox Botnet Multi-Vendor Exploitation
- **Description**: Sophisticated botnet campaign exploiting over 50 vulnerabilities across 30+ vendors using a "shotgun approach"
- **Impact**: Widespread compromise of edge devices and systems globally
- **Status**: Active exploitation targeting consumer edge devices with hit-and-run tactics

### SonicWall VPN Credential-Based Attacks
- **Description**: Large-scale campaign compromising SonicWall SSL VPN accounts using stolen valid credentials
- **Impact**: Unauthorized access to corporate networks and potential data exfiltration
- **Status**: Over 100 accounts confirmed compromised across multiple customer environments

## Affected Systems and Products

- **Microsoft Edge Browser**: Internet Explorer mode functionality compromised through Chakra JavaScript engine exploits
- **Oracle E-Business Suite**: All versions vulnerable to unauthenticated remote attacks until emergency patch applied
- **SonicWall SSL VPN Devices**: Multiple customer environments compromised through credential theft
- **Consumer Edge Devices**: Over 30 vendor products targeted by RondoDox botnet exploitation
- **Remote Desktop Protocol Services**: US-based RDP services under attack from 100,000+ IP addresses
- **Internet-of-Things Devices**: IoT devices on major US ISPs including AT&T, Comcast, and Verizon compromised for DDoS operations

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in browser engines and enterprise software
- **Credential Stuffing**: Use of stolen valid credentials to access VPN services and corporate networks
- **Botnet Operations**: Coordinated attacks from distributed networks spanning multiple countries
- **Legitimate Tool Abuse**: Weaponization of Velociraptor DFIR tool for persistent access in ransomware campaigns
- **Multi-Vector Campaigns**: Simultaneous exploitation of dozens of vulnerabilities across different vendors and platforms

## Threat Actor Activities

- **Unknown Threat Actors**: Actively exploiting Microsoft Edge IE mode zero-days for targeted access campaigns
- **Clop Ransomware Gang**: Leveraging Oracle zero-day exploits to breach high-profile targets including Harvard University
- **RondoDox Operators**: Conducting widespread exploitation campaigns targeting consumer and enterprise edge devices globally
- **Storm-2603 Group**: Chinese-linked threat actors abusing Velociraptor tool in LockBit ransomware operations for persistent network access
- **Multi-Country Botnet Operators**: Coordinating large-scale DDoS and RDP targeting campaigns from over 100,000 compromised IP addresses
- **GXC Team Cybercrime Syndicate**: Brazilian-led operation dismantled by Spanish authorities after conducting widespread cybercrime activities