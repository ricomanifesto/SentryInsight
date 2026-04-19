# Exploitation Report

Critical exploitation activity is surging across multiple fronts, with threat actors actively exploiting recently disclosed zero-day vulnerabilities and leveraging sophisticated techniques to bypass security controls. Microsoft Defender faces unprecedented threats with three zero-day vulnerabilities under active exploitation, two of which remain unpatched. Meanwhile, infrastructure-critical systems including Apache ActiveMQ (CVE-2026-34197), TBK DVR devices (CVE-2024-3721), and Protocol Buffers implementations are being targeted by attackers seeking remote code execution capabilities. Specialized malware campaigns are emerging with ZionSiphon targeting water treatment facilities and Payouts King ransomware employing QEMU virtual machines to evade endpoint detection.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that allow threat actors to gain elevated privileges in compromised systems
- **Impact**: Attackers can escalate privileges to SYSTEM level or elevated administrator permissions on Windows systems
- **Status**: Actively exploited; two vulnerabilities remain unpatched

### RedSun Microsoft Defender Zero-Day
- **Description**: A privilege escalation vulnerability in Microsoft Defender with published proof-of-concept exploit code
- **Impact**: Grants SYSTEM-level privileges to attackers
- **Status**: Zero-day with public PoC available; exploitation status indicates active use

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years before being patched
- **Impact**: Enables remote code execution on affected message broker systems
- **Status**: Actively exploited in the wild; added to CISA Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-34197

### TBK DVR Security Flaws
- **Description**: Vulnerabilities in TBK Digital Video Recorder systems being exploited by Mirai botnet variants
- **Impact**: Device hijacking for DDoS botnet recruitment and remote control
- **Status**: Actively exploited by Nexcorium Mirai variant
- **CVE ID**: CVE-2024-3721

### Protocol Buffers JavaScript Implementation Flaw
- **Description**: Critical remote code execution vulnerability in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: Enables JavaScript code execution in applications using the vulnerable library
- **Status**: Critical vulnerability with published proof-of-concept exploit code

## Affected Systems and Products

- **Microsoft Defender**: Windows endpoint protection systems vulnerable to privilege escalation attacks
- **Apache ActiveMQ Classic**: Message broker systems in enterprise environments
- **TBK DVR Systems**: Digital video recording devices used in surveillance infrastructure
- **TP-Link Wi-Fi Routers**: End-of-life router models targeted for botnet recruitment
- **Protocol Buffers (protobuf.js)**: JavaScript applications using Google's Protocol Buffers implementation
- **Windows Domain Controllers**: Some systems experiencing reboot loops after April 2026 security updates
- **Water Treatment Systems**: Operational technology environments targeted by ZionSiphon malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in security software and system components
- **QEMU VM Evasion**: Payouts King ransomware uses QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **Mirai Botnet Variants**: Nexcorium variant exploiting IoT device vulnerabilities for DDoS botnet expansion
- **ClickFix Attacks**: North Korean threat actors using fake job offers and Zoom updates to deliver credential-stealing payloads targeting macOS users
- **Device Code Phishing**: Tycoon 2FA phishing groups adopting legitimate new-device login flows to bypass multi-factor authentication
- **OT-Specific Malware**: ZionSiphon designed specifically for operational technology environments in water treatment facilities

## Threat Actor Activities

- **Huntress Research**: Identified and reported active exploitation of Microsoft Defender zero-day vulnerabilities by multiple threat actors
- **Chaotic Eclipse**: Security researcher published proof-of-concept exploits for Microsoft Defender vulnerabilities in protest of disclosure handling
- **Nexcorium Operators**: Mirai variant operators targeting TBK DVR and TP-Link router vulnerabilities for botnet recruitment
- **Sapphire Sleet (North Korea)**: Using ClickFix techniques to target macOS users with fake job offers and software updates
- **Payouts King Ransomware Group**: Employing sophisticated VM-based evasion techniques using QEMU emulators
- **ZionSiphon Operators**: Targeting critical infrastructure with specialized malware designed for water treatment sabotage
- **Dragon Boss Adware Network**: Transformed from benign adware to antivirus-killing malware through malicious updates
- **PowMix Botnet Controllers**: Active campaign targeting Czech workforce using randomized command-and-control traffic
- **Operation PowerOFF Targets**: International law enforcement identified over 75,000 users of commercial DDoS services across 21 countries