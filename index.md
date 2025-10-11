# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in the wild, with threat actors targeting enterprise file sharing systems and Oracle business applications. Most concerning is the active exploitation of CVE-2025-11371 in Gladinet CentreStack and TrioFox products, allowing local attackers to access system files without authentication. Additionally, CL0P-linked hackers have been exploiting an Oracle E-Business Suite zero-day since August 2025, potentially impacting dozens of organizations. Meanwhile, multiple threat groups are leveraging legitimate security tools like Velociraptor for persistent access in ransomware campaigns, and sophisticated botnet operations like RondoDox and Aisuru are compromising consumer edge devices and IoT infrastructure at scale.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Local file inclusion vulnerability that allows attackers to access system files without authentication, with demonstrated escalation to remote code execution
- **Impact**: Complete system compromise through unauthorized file access and potential RCE capabilities
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: Security flaw in Oracle's E-Business Suite software being exploited by CL0P-linked threat actors
- **Impact**: Data breach affecting dozens of organizations since exploitation began
- **Status**: Active exploitation ongoing since August 9, 2025

### GoAnywhere MFT Critical Flaw
- **Description**: Critical security vulnerability in Fortra's GoAnywhere Managed File Transfer platform
- **Impact**: Potential system compromise and data exfiltration through managed file transfer systems
- **Status**: Under active exploitation with full timeline investigation completed
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to local file inclusion attacks
- **Oracle E-Business Suite**: Enterprise resource planning software affected by zero-day exploitation
- **Fortra GoAnywhere MFT**: Managed file transfer solutions experiencing active attacks
- **Consumer Edge Devices**: Routers, IoT devices, and network equipment targeted by RondoDox botnet operations
- **IoT Infrastructure**: Internet-connected devices on major US ISPs including AT&T, Comcast, and Verizon compromised by Aisuru botnet
- **Node.js Applications**: Systems using Single Executable Application feature targeted by Stealit malware campaign
- **SonicWall Cloud Backup**: 100% of firewall configuration backups compromised in recent breach

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in enterprise software systems
- **Tool Abuse**: Legitimate DFIR tools like Velociraptor weaponized for persistent access and ransomware deployment
- **Supply Chain Compromise**: 175 malicious npm packages with 26,000 downloads used for credential phishing
- **Social Engineering**: Android spyware ClayRat disguised as popular applications like WhatsApp, TikTok, and YouTube
- **Botnet Operations**: Shotgun-style exploitation of consumer edge devices for DDoS and persistent access
- **AI Tool Manipulation**: CamoLeak attacks targeting GitHub Copilot for data exfiltration
- **Payroll Hijacking**: HR system compromise for salary payment diversion attacks

## Threat Actor Activities

- **CL0P Ransomware Group**: Actively exploiting Oracle E-Business Suite zero-day affecting dozens of organizations since August 2025
- **Storm-2603**: Chinese threat group using Velociraptor DFIR tools in LockBit and Babuk ransomware attacks for persistent network access
- **Storm-2657**: "Payroll Pirates" targeting university HR employees in the United States to hijack salary payments since March 2025
- **ShinyHunters Group**: Operating BreachForums portal for Salesforce extortion until FBI takedown of all domains
- **RondoDox Operators**: Running hit-and-run exploitation campaigns against consumer edge devices worldwide using shotgun approach
- **Aisuru Botnet**: Orchestrating record-breaking DDoS attacks primarily from compromised IoT devices on US ISPs
- **Stealit Campaign**: Distributing malware through game and VPN installers using Node.js Single Executable Application features