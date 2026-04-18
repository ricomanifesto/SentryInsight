# Exploitation Report

Critical exploitation activities are currently affecting multiple high-profile systems across various sectors. Most notably, three Microsoft Defender zero-day vulnerabilities are being actively exploited by threat actors to gain elevated privileges, with two remaining unpatched. Additionally, threat actors are leveraging CVE-2024-3721 to compromise TBK DVR systems for botnet operations, while CVE-2026-34197 in Apache ActiveMQ has been added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation. A critical flaw in the widely-used protobuf.js library has also been disclosed with proof-of-concept exploit code publicly available, enabling remote code execution. The threat landscape is further complicated by sophisticated attack techniques including ransomware operations using virtual machines to bypass security controls and advanced phishing campaigns targeting multi-factor authentication protections.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that allow privilege escalation
- **Impact**: Threat actors can gain SYSTEM or elevated administrator permissions on compromised systems
- **Status**: Actively exploited in the wild; two vulnerabilities remain unpatched

### Microsoft Defender RedSun Zero-Day
- **Description**: A second Microsoft Defender zero-day vulnerability with published proof-of-concept exploit code
- **Impact**: Grants SYSTEM privileges to attackers
- **Status**: Actively exploited with public PoC available

### TBK DVR Security Vulnerability
- **Description**: Security flaw in TBK DVR systems being exploited by Mirai botnet variants
- **Impact**: Allows hijacking of DVR systems for DDoS botnet operations
- **Status**: Actively exploited by Nexcorium Mirai variant
- **CVE ID**: CVE-2024-3721

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years
- **Impact**: Enables remote code execution and system compromise
- **Status**: Actively exploited in attacks; added to CISA Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-34197

### Protobuf.js Remote Code Execution Flaw
- **Description**: Critical vulnerability in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: Enables JavaScript code execution on affected systems
- **Status**: Critical severity with proof-of-concept exploit code published

## Affected Systems and Products

- **Microsoft Defender**: Multiple zero-day vulnerabilities affecting privilege escalation controls
- **TBK DVR Systems**: DVR devices compromised for botnet recruitment via Mirai variant
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy routers targeted alongside DVR systems for botnet operations
- **Apache ActiveMQ Classic**: Message broker systems vulnerable to remote code execution
- **Protobuf.js Library**: JavaScript applications using the Protocol Buffers implementation
- **Windows Domain Controllers**: Systems experiencing restart loops after April 2026 security updates
- **macOS Systems**: Targeted by North Korean ClickFix attacks through fake job offers and Zoom updates

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities in Microsoft Defender being exploited for privilege escalation
- **Botnet Recruitment**: Exploitation of IoT devices including DVRs and routers for DDoS operations
- **Virtual Machine Evasion**: Payouts King ransomware using QEMU emulator as reverse SSH backdoor to bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA attackers adopting legitimate new-device login flows to bypass multi-factor authentication
- **ClickFix Attacks**: North Korean actors using fake job offers and phony Zoom updates to deliver credential theft malware
- **Adware Transformation**: Dragon Boss adware evolving into antivirus-killing malware through scheduled task persistence
- **Randomized C2 Communications**: PowMix botnet using randomized command-and-control traffic patterns

## Threat Actor Activities

- **Nexcorium Mirai Operators**: Exploiting CVE-2024-3721 to build DDoS botnets from compromised TBK DVR systems
- **Payouts King Ransomware Group**: Using innovative QEMU-based techniques to hide malicious activities in virtual machines
- **Tycoon 2FA Phishing Group**: Adapting to use device code phishing techniques to circumvent multi-factor authentication
- **Sapphire Sleet (North Korea)**: Conducting ClickFix campaigns targeting macOS users with fake job offers and software updates
- **PowMix Botnet Operators**: Targeting Czech Republic workforce with previously undocumented botnet since December 2025
- **Dragon Boss Operators**: Transforming benign adware into sophisticated antivirus evasion malware
- **ZionSiphon Operators**: Deploying specialized malware designed to sabotage water treatment and desalination systems