# Exploitation Report

Several critical zero-day and recently disclosed vulnerabilities are being actively exploited in the wild, posing significant risks to enterprise networks and government entities. The most concerning developments include a zero-day vulnerability in Trend Micro Apex One security software being exploited against Windows systems, a highly critical SQL injection flaw in Drupal now under active attack, and three maximum severity vulnerabilities in Ubiquiti UniFi OS that allow remote attackers to gain unauthorized access. Additionally, threat actors are leveraging sophisticated malware campaigns, including Chinese APT groups deploying new Linux and Windows backdoors against telecommunications providers, and the Belarus-aligned Ghostwriter group targeting Ukrainian government entities with phishing attacks.

## Active Exploitation Details

### Trend Micro Apex One Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Trend Micro's Apex One cybersecurity software affecting Windows systems
- **Impact**: Allows attackers to compromise security software designed to protect enterprise networks
- **Status**: Currently being exploited in the wild; security updates have been released by Trend Micro

### Drupal SQL Injection Vulnerability
- **Description**: A highly critical SQL injection flaw in the popular content management system Drupal
- **Impact**: Enables attackers to execute malicious database queries and potentially gain unauthorized access to website data
- **Status**: Actively being targeted by hackers following public disclosure earlier this week

### Ubiquiti UniFi OS Vulnerabilities
- **Description**: Three maximum severity security flaws in UniFi OS networking equipment
- **Impact**: Allow remote attackers without privileges to gain unauthorized access to network infrastructure
- **Status**: Security patches have been released by Ubiquiti

### Cisco Secure Workload REST API Vulnerability
- **Description**: Maximum-severity security flaw in Cisco Secure Workload REST API
- **Impact**: Allows unauthenticated remote attackers to access sensitive data and gain Site Admin privileges
- **Status**: Security updates have been released by Cisco
- **CVE ID**: CVE-2026-20223

### Langflow Vulnerability
- **Description**: Security flaw in the Langflow platform that has been exploited in attacks
- **Impact**: Enables unauthorized access to systems running the affected software
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation

## Affected Systems and Products

- **Trend Micro Apex One**: Windows-based cybersecurity software installations
- **Drupal**: Content management systems running vulnerable versions
- **Ubiquiti UniFi OS**: Network infrastructure equipment including access points and controllers
- **Cisco Secure Workload**: Application security platform installations
- **Langflow**: Machine learning workflow platforms
- **Linux Systems**: Telecommunications infrastructure targeted by Showboat malware
- **Windows Systems**: Enterprise networks targeted by JFMBackdoor malware
- **GitHub Repositories**: Over 5,561 repositories compromised in Megalodon campaign
- **Ukrainian Government Systems**: Entities targeted by Ghostwriter phishing campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in security software
- **SQL Injection**: Database manipulation attacks against web applications
- **Phishing Campaigns**: Email-based attacks using lures related to Ukrainian defense systems
- **Supply Chain Attacks**: Malicious CI/CD workflows injected into GitHub repositories
- **SOCKS5 Proxy Backdoors**: Network tunneling for persistent access to compromised systems
- **Social Engineering**: Increased targeting of healthcare sector with evolved tactics
- **Botnet Operations**: DDoS-for-hire services using infected IoT devices
- **Legitimate Service Abuse**: Using Discord and Microsoft Graph APIs for command and control

## Threat Actor Activities

- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned group targeting Ukrainian government entities with Prometheus-themed phishing attacks using malware designed to harvest credentials
- **Chinese APT Groups**: Conducting cyber-espionage campaigns against telecommunications providers in Central Asia and the Middle East using Showboat Linux malware and JFMBackdoor Windows malware for persistent access
- **Webworm**: Chinese advanced persistent threat group targeting European Union governments using Discord and Microsoft Graph APIs for command and control operations
- **Kimwolf Botnet Operator**: Canadian individual arrested for operating a DDoS botnet that infected nearly two million devices worldwide for denial-of-service attacks
- **Megalodon Campaign**: Automated attack targeting thousands of GitHub repositories with malicious CI/CD workflows within a six-hour timeframe
- **Ransomware Groups**: 25 different ransomware organizations using dismantled First VPN service to obscure attack origins and evade law enforcement detection