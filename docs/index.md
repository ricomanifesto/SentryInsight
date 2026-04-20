# Exploitation Report

Critical exploitation activity is currently underway across multiple platforms, with threat actors actively targeting Microsoft Defender zero-day vulnerabilities, Apache ActiveMQ systems, and IoT devices. Three Microsoft Defender zero-days are being exploited for privilege escalation with two remaining unpatched, while CVE-2026-34197 in Apache ActiveMQ and CVE-2024-3721 in TBK DVRs are being leveraged for remote code execution and botnet recruitment. Additionally, sophisticated attackers are deploying novel evasion techniques including QEMU virtualization for ransomware deployment and ClickFix attacks targeting macOS users.

## Active Exploitation Details

### Microsoft Defender Zero-Days
- **Description**: Three recently disclosed security vulnerabilities in Microsoft Defender are being actively exploited by threat actors
- **Impact**: Attackers can gain elevated privileges and SYSTEM-level access in compromised systems
- **Status**: Active exploitation confirmed; two vulnerabilities remain unpatched

### Apache ActiveMQ Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years before being patched earlier this month
- **Impact**: Remote code execution capabilities allowing attackers to compromise ActiveMQ systems
- **Status**: Active exploitation confirmed by CISA; vulnerability patched
- **CVE ID**: CVE-2026-34197

### TBK DVR Remote Code Execution
- **Description**: Security flaw in TBK DVR systems being exploited to deploy Mirai botnet variants
- **Impact**: Device hijacking for distributed denial-of-service (DDoS) attacks and botnet recruitment
- **Status**: Active exploitation by Nexcorium Mirai variant
- **CVE ID**: CVE-2024-3721

### Protobuf.js Critical Vulnerability
- **Description**: Critical remote code execution flaw in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: JavaScript code execution in applications using the vulnerable library
- **Status**: Proof-of-concept exploit code published; critical severity rating

### Recently Leaked Windows Zero-Days
- **Description**: Three recently disclosed Windows security vulnerabilities are being exploited in active attacks
- **Impact**: Attackers can gain SYSTEM or elevated administrator permissions
- **Status**: Active exploitation confirmed following recent disclosure

## Affected Systems and Products

- **Microsoft Defender**: Security software experiencing active zero-day exploitation
- **Apache ActiveMQ Classic**: Message broker systems vulnerable to remote code execution
- **TBK DVR Systems**: Digital video recorders being hijacked for botnet operations
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy networking equipment targeted by Mirai variants
- **Protobuf.js Library**: JavaScript applications implementing Google's Protocol Buffers
- **Windows Systems**: Domain controllers and servers affected by various zero-day vulnerabilities
- **macOS Systems**: Apple devices targeted by ClickFix attacks through fake applications

## Attack Vectors and Techniques

- **Privilege Escalation**: Exploitation of Microsoft Defender vulnerabilities to gain elevated system access
- **Remote Code Execution**: ActiveMQ and protobuf.js vulnerabilities allowing arbitrary code execution
- **Botnet Recruitment**: IoT device compromise through DVR and router vulnerabilities for DDoS operations
- **QEMU Virtualization Evasion**: Payouts King ransomware using QEMU emulator to bypass endpoint security detection
- **ClickFix Social Engineering**: North Korean actors using fake job offers and Zoom updates to deliver credential theft malware
- **Device Code Phishing**: Tycoon 2FA attackers leveraging legitimate new-device login flows to bypass authentication
- **Adware Evolution**: Dragon Boss adware transforming into antivirus-killing malware through scheduled task persistence

## Threat Actor Activities

- **Nexcorium Group**: Deploying Mirai variant to exploit TBK DVR systems and TP-Link routers for DDoS botnet operations
- **Payouts King Ransomware Operators**: Using QEMU virtual machines as reverse SSH backdoors to evade endpoint security
- **Sapphire Sleet (North Korea)**: Targeting macOS users with ClickFix attacks through fraudulent job postings and software updates
- **Tycoon 2FA Phishing Group**: Adopting device code phishing techniques to circumvent multi-factor authentication protections
- **Dragon Boss Operators**: Transforming benign adware into sophisticated antivirus evasion tools with persistence mechanisms
- **Microsoft Defender Exploiters**: Actively leveraging three zero-day vulnerabilities for system compromise and privilege escalation