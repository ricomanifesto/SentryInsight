# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple enterprise platforms, with threat actors targeting Oracle E-Business Suite (CVE-2025-10035), Gladinet file sharing software (CVE-2025-11371), and SonicWall SSL VPN devices. CL0P-linked hackers have successfully breached dozens of organizations through Oracle software flaws since August 2025, while widespread SonicWall VPN compromises have impacted over 100 accounts. Additionally, sophisticated threat actors are weaponizing legitimate security tools like Velociraptor DFIR software for ransomware attacks and deploying new Android spyware campaigns alongside large-scale malicious npm package operations.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle's E-Business Suite software that allows unauthorized access to sensitive data without authentication
- **Impact**: Complete unauthorized access to enterprise data and systems; dozens of organizations have been breached since August 9, 2025
- **Status**: Under active exploitation by CL0P-linked threat actors; Oracle has issued security alerts
- **CVE ID**: CVE-2025-10035

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Local file inclusion vulnerability that can be escalated to remote code execution, allowing attackers to access system files without authentication
- **Impact**: Complete system compromise with ability to execute arbitrary code and access sensitive files
- **Status**: Active in-the-wild exploitation detected; currently unpatched zero-day vulnerability
- **CVE ID**: CVE-2025-11371

### SonicWall SSL VPN Mass Compromise
- **Description**: Widespread authentication bypass affecting SonicWall SSL VPN devices across multiple customer environments
- **Impact**: Unauthorized network access, lateral movement capabilities, and potential data exfiltration
- **Status**: Active exploitation with over 100 accounts compromised; threat actors authenticating into multiple customer environments

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software used by large organizations worldwide
- **Gladinet CentreStack and TrioFox**: File sharing and cloud storage solutions for enterprise environments
- **SonicWall SSL VPN devices**: Network security appliances providing remote access capabilities
- **Android mobile devices**: Targeted by ClayRat spyware masquerading as legitimate applications
- **Node.js applications**: Exploited through Single Executable Application feature for malware distribution
- **npm package ecosystem**: 175 malicious packages with 26,000 downloads used for credential harvesting
- **Consumer IoT devices**: Compromised for DDoS botnet operations on major US ISPs

## Attack Vectors and Techniques

- **Zero-day exploitation**: Direct targeting of unpatched vulnerabilities in enterprise software
- **Authentication bypass**: Circumventing login mechanisms in VPN and enterprise applications  
- **Local file inclusion to RCE escalation**: Converting file access vulnerabilities to full system compromise
- **Supply chain attacks**: Distribution of malicious npm packages and compromised software installers
- **Social engineering**: Fake mobile applications and phishing campaigns targeting credentials
- **Legitimate tool abuse**: Weaponizing Velociraptor DFIR tool for persistent network access
- **Botnet operations**: Large-scale DDoS attacks using compromised IoT devices

## Threat Actor Activities

- **CL0P-linked hackers**: Actively exploiting Oracle E-Business Suite zero-day to breach dozens of organizations since August 2025
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group abusing Velociraptor incident response tool in LockBit ransomware campaigns
- **Storm-2657**: "Payroll Pirates" hijacking HR SaaS accounts to divert employee salary payments to attacker-controlled accounts
- **GXC Team cybercrime syndicate**: Brazilian-led operation dismantled by Spanish authorities, with leader "GoogleXcoder" arrested
- **ShinyHunters group**: Operating BreachForums portal for data extortion before FBI takedown; continuing Salesforce extortion activities
- **Aisuru botnet operators**: Conducting record-breaking DDoS attacks against US ISPs using compromised IoT devices
- **RondoDox botnet**: Taking "shotgun approach" to exploiting vulnerabilities in consumer edge devices globally