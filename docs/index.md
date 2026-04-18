# Exploitation Report

Critical active exploitation activity is currently targeting multiple Microsoft Defender zero-day vulnerabilities, with three distinct flaws being exploited to gain elevated privileges on compromised systems. Two of these vulnerabilities remain unpatched, presenting immediate risks to organizations. Additionally, threat actors are actively exploiting a high-severity Apache ActiveMQ vulnerability (CVE-2026-34197) and a critical Protobuf.js remote code execution flaw. The Mirai botnet variant Nexcorium is exploiting CVE-2024-3721 in TBK DVRs to build DDoS capabilities, while the Payouts King ransomware is implementing innovative evasion techniques using QEMU virtual machines to bypass endpoint security.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender allowing attackers to gain elevated privileges
- **Impact**: Threat actors can escalate privileges to SYSTEM level or elevated administrator permissions on compromised systems
- **Status**: Currently being actively exploited; two vulnerabilities remain unpatched

### RedSun Microsoft Defender Zero-Day
- **Description**: A privilege escalation vulnerability in Microsoft Defender with published proof-of-concept exploit code
- **Impact**: Grants SYSTEM-level privileges to attackers
- **Status**: Zero-day with public PoC available; actively exploited

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw that remained undetected for 13 years before being patched
- **Impact**: Allows unauthorized access and potential system compromise
- **Status**: Actively exploited in the wild; patch available
- **CVE ID**: CVE-2026-34197

### Protobuf.js Remote Code Execution Flaw
- **Description**: Critical vulnerability in the widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: Enables remote JavaScript code execution on affected systems
- **Status**: Critical severity with proof-of-concept exploit code published

### TBK DVR Security Flaw
- **Description**: Security vulnerability in TBK Digital Video Recorders being exploited by Mirai botnet variants
- **Impact**: Compromised devices are recruited into DDoS botnets
- **Status**: Actively exploited by Nexcorium Mirai variant
- **CVE ID**: CVE-2024-3721

## Affected Systems and Products

- **Microsoft Defender**: All versions affected by multiple zero-day vulnerabilities
- **Apache ActiveMQ Classic**: Legacy versions containing 13-year-old vulnerability
- **Protobuf.js Library**: JavaScript implementations of Google's Protocol Buffers
- **TBK Digital Video Recorders**: IoT devices targeted for botnet recruitment
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy devices exploited alongside DVRs
- **Windows Domain Controllers**: Experiencing restart loops after April 2026 security updates
- **Water Treatment Systems**: Targeted by ZionSiphon operational technology malware
- **macOS Systems**: Targeted by North Korean ClickFix campaigns

## Attack Vectors and Techniques

- **Privilege Escalation**: Microsoft Defender zero-days used to gain SYSTEM privileges
- **Remote Code Execution**: Protobuf.js vulnerability enabling JavaScript execution
- **Botnet Recruitment**: IoT device exploitation for DDoS infrastructure
- **VM-Based Evasion**: QEMU virtual machines used by Payouts King ransomware to bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishers adopting legitimate device login flows for credential theft
- **ClickFix Social Engineering**: North Korean actors using fake job offers and Zoom updates
- **Operational Technology Targeting**: ZionSiphon malware specifically designed for water treatment sabotage

## Threat Actor Activities

- **Nexcorium Operators**: Deploying Mirai botnet variants targeting TBK DVRs and TP-Link routers for DDoS operations
- **Payouts King Ransomware Group**: Using QEMU emulators as reverse SSH backdoors to run hidden virtual machines and evade detection
- **Tycoon 2FA Phishing Group**: Shifting tactics to device code phishing techniques targeting account access
- **North Korean Sapphire Sleet**: Conducting ClickFix campaigns against macOS users with fake job offers and software updates
- **PowMix Botnet Operators**: Targeting Czech Republic workforce with randomized command-and-control traffic since December
- **Dragon Boss Adware Network**: Transforming benign adware into antivirus-killing malware with persistence mechanisms
- **ZionSiphon Developers**: Creating specialized operational technology malware for water treatment system sabotage
- **Microsoft Defender Exploit Developers**: Publishing zero-day proof-of-concept code and actively exploiting multiple vulnerabilities