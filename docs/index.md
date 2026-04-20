# Exploitation Report

Critical security vulnerabilities are currently being exploited in the wild across multiple platforms and systems. The most concerning activities include the exploitation of three zero-day vulnerabilities in Microsoft Defender, with two remaining unpatched, allowing threat actors to gain elevated privileges on compromised systems. Additionally, CISA has flagged an Apache ActiveMQ vulnerability (CVE-2024-34197) as actively exploited after remaining undetected for 13 years. Threat actors are also leveraging recently leaked Windows zero-day vulnerabilities to achieve SYSTEM-level access. The Mirai botnet variant Nexcorium is actively exploiting CVE-2024-3721 to compromise TBK DVRs for DDoS operations, while a critical flaw in the widely-used protobuf.js library has proof-of-concept exploit code available for remote code execution attacks.

## Active Exploitation Details

### **Microsoft Defender Zero-Day Vulnerabilities**
- **Description**: Three recently disclosed security flaws in Microsoft Defender allowing privilege escalation
- **Impact**: Attackers can gain elevated privileges on compromised systems
- **Status**: Actively exploited; two vulnerabilities remain unpatched

### **Apache ActiveMQ Classic Vulnerability**
- **Description**: High-severity security flaw that remained undetected for 13 years
- **Impact**: Remote exploitation allowing unauthorized access to messaging systems
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2024-34197

### **Windows Zero-Day Vulnerabilities**
- **Description**: Recently leaked Windows security vulnerabilities targeting privilege escalation
- **Impact**: Threat actors can achieve SYSTEM or elevated administrator permissions
- **Status**: Actively exploited following public disclosure

### **TBK DVR Remote Code Execution**
- **Description**: Security flaw in TBK DVR systems being exploited by Mirai botnet variants
- **Impact**: Device hijacking for DDoS botnet operations
- **Status**: Active exploitation by Nexcorium variant
- **CVE ID**: CVE-2024-3721

### **Protobuf.js Remote Code Execution**
- **Description**: Critical flaw in protobuf.js JavaScript implementation of Google's Protocol Buffers
- **Impact**: Remote code execution in JavaScript environments
- **Status**: Proof-of-concept exploit code published

## Affected Systems and Products

- **Microsoft Defender**: Security software with multiple privilege escalation vulnerabilities
- **Apache ActiveMQ Classic**: Message broker systems vulnerable to remote exploitation
- **Windows Operating Systems**: Multiple versions affected by recently disclosed zero-days
- **TBK DVR Systems**: Digital video recorders being compromised for botnet operations
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy devices targeted by Mirai variants
- **protobuf.js Library**: Widely-used JavaScript Protocol Buffers implementation
- **Vercel Platform**: Cloud development platform experiencing confirmed security breach
- **Apple Account Systems**: Legitimate notification system being abused for phishing

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being exploited before patches are available
- **Privilege Escalation**: Attackers using Microsoft Defender flaws to gain elevated system access
- **Botnet Recruitment**: Mirai variants targeting IoT devices and DVR systems for DDoS operations
- **Supply Chain Targeting**: Critical vulnerabilities in widely-used development libraries
- **QEMU VM Evasion**: Payouts King ransomware using QEMU emulator as reverse SSH backdoor to bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishers adopting device code phishing techniques
- **Apple Service Abuse**: Legitimate Apple account notification system being exploited for phishing campaigns
- **ClickFix Attacks**: North Korean threat actors targeting macOS users with fake job offers and Zoom updates

## Threat Actor Activities

- **Huntress Research Team**: Identified active exploitation of Microsoft Defender zero-days
- **Nexcorium Operators**: Deploying Mirai botnet variants targeting TBK DVRs and TP-Link routers
- **Payouts King Ransomware Group**: Using sophisticated VM-based evasion techniques with QEMU emulator
- **Tycoon 2FA Phishers**: Transitioning to device code phishing techniques for account takeover
- **Sapphire Sleet (North Korea)**: Targeting macOS users with ClickFix attacks via fake job offers
- **Dragon Boss Adware Network**: Transforming benign adware into antivirus-killing malware through scheduled updates
- **Grinex Exchange Attackers**: $13.7 million cryptocurrency theft attributed to state-level actors
- **DDoS-for-Hire Operations**: Commercial DDoS services with over 75,000 users identified in law enforcement takedown