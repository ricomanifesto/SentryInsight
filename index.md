# Exploitation Report

Current threat landscape shows several critical zero-day vulnerabilities under active exploitation, with threat actors leveraging both known and unknown security flaws across enterprise software platforms. Most concerning is the active exploitation of CVE-2025-10035 in Fortra's GoAnywhere Managed File Transfer solution and an unpatched zero-day vulnerability affecting Gladinet CentreStack and TrioFox products. Additionally, CL0P-linked threat actors have been exploiting a zero-day flaw in Oracle's E-Business Suite since August 2025, impacting dozens of organizations worldwide. The RondoDox botnet is conducting widespread attacks targeting 56 n-day vulnerabilities across more than 30 device types, while various malware campaigns including Stealit, ClayRat spyware, and credential harvesting operations through npm packages continue to pose significant threats to organizations globally.

## Active Exploitation Details

### GoAnywhere Managed File Transfer Vulnerability
- **Description**: Critical security flaw in Fortra's GoAnywhere Managed File Transfer solution that has been actively exploited in the wild
- **Impact**: Attackers can compromise file transfer systems, potentially gaining access to sensitive data transfers and file repositories
- **Status**: Under active exploitation with full timeline investigation completed by Fortra
- **CVE ID**: CVE-2025-10035

### Gladinet and TrioFox Zero-Day Vulnerability
- **Description**: Unpatched zero-day vulnerability affecting Gladinet CentreStack and TrioFox products that allows progression from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Attackers can achieve full remote code execution on affected systems, potentially compromising entire network infrastructures
- **Status**: Currently unpatched with active in-the-wild exploitation detected by Huntress

### Oracle E-Business Suite Zero-Day
- **Description**: Zero-day security flaw in Oracle's E-Business Suite (EBS) software that has been exploited by CL0P-linked hackers
- **Impact**: Allows threat actors to breach organizations and potentially deploy ransomware or steal sensitive corporate data
- **Status**: Active exploitation ongoing since August 9, 2025, with dozens of organizations confirmed impacted

### RondoDox Botnet N-Day Exploitation
- **Description**: Large-scale botnet targeting 56 known vulnerabilities across more than 30 distinct device types, including flaws first disclosed at Pwn2Own competitions
- **Impact**: Widespread device compromise enabling botnet expansion and potential secondary attack deployment
- **Status**: Active worldwide attacks targeting previously disclosed but unpatched vulnerabilities

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed file transfer solutions used by enterprises for secure data exchange
- **Gladinet CentreStack**: Cloud file server and sync solutions for enterprises
- **TrioFox**: File access and sharing platforms
- **Oracle E-Business Suite**: Enterprise resource planning software used by large organizations
- **Various IoT Devices**: Internet-of-Things devices targeted by RondoDox botnet across multiple manufacturers
- **Android Devices**: Mobile devices targeted by ClayRat spyware through fake application installations
- **npm Registry**: Developer package repository affected by 175 malicious packages
- **Node.js Applications**: Applications using Node.js Single Executable feature targeted by Stealit malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software platforms
- **Social Engineering**: Fake application distribution through Telegram channels and phishing websites
- **Supply Chain Attacks**: Malicious npm packages designed to harvest credentials from developer environments
- **Legitimate Tool Abuse**: Misuse of Velociraptor DFIR tool by Storm-2603 for persistent network access and ransomware deployment
- **N-Day Vulnerability Targeting**: Systematic exploitation of known but unpatched vulnerabilities across diverse device ecosystems
- **Application Impersonation**: ClayRat spyware disguising as popular apps like WhatsApp, TikTok, and YouTube

## Threat Actor Activities

- **CL0P-Linked Hackers**: Conducting large-scale breaches through Oracle EBS zero-day exploitation targeting multiple organizations since August 2025
- **Storm-2603**: Chinese threat group abusing Velociraptor incident response tool to maintain persistent access and deploy LockBit and Babuk ransomware
- **Storm-2657**: "Payroll Pirates" targeting university HR employees and SaaS accounts to redirect salary payments to attacker-controlled accounts
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaks and Salesforce extortion activities before FBI takedown
- **UTA0388**: China-aligned espionage group conducting spear-phishing campaigns across North America, Asia, and Europe using GOVERSHELL malware
- **Aisuru Botnet Operators**: Managing the world's largest DDoS botnet primarily composed of compromised IoT devices from major US ISPs including AT&T, Comcast, and Verizon