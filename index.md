# Exploitation Report

Critical zero-day exploitation activity is currently targeting multiple platforms, with attackers leveraging vulnerabilities in Microsoft Edge's Internet Explorer mode through the Chakra JavaScript engine, Oracle E-Business Suite systems, and widespread compromises of SonicWall VPN infrastructure. The threat landscape shows sophisticated campaigns including the RondoDox botnet exploiting over 50 vulnerabilities across 30+ vendors, while threat actors abuse legitimate security tools like Velociraptor for ransomware operations. Notable incidents include Harvard University's breach through Oracle zero-day exploitation and large-scale credential-based attacks against enterprise VPN solutions.

## Active Exploitation Details

### **Chakra JavaScript Engine Zero-Day**
- **Description**: Zero-day vulnerabilities in Microsoft Edge's Internet Explorer mode targeting the Chakra JavaScript engine
- **Impact**: Allows attackers to gain unauthorized access to target devices through browser exploitation
- **Status**: Microsoft has restricted access to IE mode in Edge browser as a mitigation measure following credible reports of active exploitation in August 2025

### **Oracle E-Business Suite Vulnerability**
- **Description**: Security flaw in Oracle E-Business Suite that allows unauthorized access without authentication
- **Impact**: Enables attackers to access sensitive data remotely without requiring login credentials
- **Status**: Oracle issued an emergency security patch over the weekend to address this actively exploited vulnerability

### **RondoDox Botnet Multi-Vendor Exploitation**
- **Description**: Sophisticated botnet campaign targeting over 50 vulnerabilities across more than 30 different vendors
- **Impact**: Enables widespread compromise of edge devices and consumer systems globally
- **Status**: Actively exploiting vulnerabilities in a "shotgun" approach targeting edge devices worldwide

## Affected Systems and Products

- **Microsoft Edge Browser**: Internet Explorer mode functionality compromised through Chakra JavaScript engine vulnerabilities
- **Oracle E-Business Suite**: Multiple versions affected by remote authentication bypass vulnerability
- **SonicWall SSL VPN**: Over 100 accounts compromised through credential-based attacks
- **Consumer Edge Devices**: More than 30 vendors affected by RondoDox botnet exploitation campaigns
- **Harvard University Systems**: Breached through Oracle zero-day exploitation, claimed by Clop ransomware gang
- **IoT Devices on US ISPs**: Compromised devices on AT&T, Comcast, and Verizon networks contributing to Aisuru DDoS botnet

## Attack Vectors and Techniques

- **Browser-Based Exploitation**: Zero-day attacks through Internet Explorer mode in Microsoft Edge targeting JavaScript engine vulnerabilities
- **Remote Authentication Bypass**: Unauthenticated remote exploitation of Oracle E-Business Suite systems
- **Credential-Based VPN Compromise**: Large-scale attacks using stolen valid credentials against SonicWall SSL VPN accounts
- **Multi-Vector Botnet Operations**: RondoDox employing "exploit shotgun" methodology across diverse vendor platforms
- **DFIR Tool Abuse**: Threat actors weaponizing Velociraptor digital forensics tool for persistent access and ransomware deployment
- **GitHub Infrastructure Abuse**: Astaroth banking trojan using GitHub as operational backbone for resilience

## Threat Actor Activities

- **Unknown Threat Actors**: Conducting zero-day attacks against Microsoft Edge IE mode since August 2025
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group abusing Velociraptor DFIR tool in LockBit ransomware operations
- **Clop Ransomware Gang**: Exploiting Oracle zero-day vulnerabilities, claiming breach of Harvard University systems
- **RondoDox Operators**: Managing large-scale botnet operations targeting consumer edge devices across 30+ vendors
- **Astaroth Banking Trojan Group**: Leveraging GitHub infrastructure for command and control operations
- **SonicWall VPN Attackers**: Conducting widespread compromise campaigns affecting over 100 enterprise VPN accounts
- **Aisuru Botnet Operators**: Operating record-breaking DDoS botnet primarily from compromised US ISP-hosted IoT devices
- **GXC Team Cybercrime Syndicate**: Dismantled by Spanish authorities with leader "GoogleXcoder" arrested