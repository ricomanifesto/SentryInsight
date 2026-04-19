# Exploitation Report

The current threat landscape shows active exploitation of critical zero-day vulnerabilities alongside established attack vectors. Most concerning is the active exploitation of three Microsoft Defender zero-day vulnerabilities, with two remaining unpatched, allowing attackers to gain SYSTEM privileges. Additional active exploitation includes a high-severity Apache ActiveMQ vulnerability (CVE-2026-34197) that CISA has flagged for immediate patching, and a Mirai botnet variant exploiting DVR systems (CVE-2024-3721). Threat actors are also leveraging recently leaked Windows zero-days and deploying sophisticated ransomware operations using virtual machine techniques to bypass endpoint security.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender allowing privilege escalation
- **Impact**: Attackers can gain elevated SYSTEM privileges in compromised systems
- **Status**: One patched, two remain unpatched and actively exploited

### Microsoft Defender "RedSun" Zero-Day
- **Description**: Second zero-day vulnerability in Microsoft Defender with published proof-of-concept exploit
- **Impact**: Grants SYSTEM privileges to attackers
- **Status**: Actively exploited with public PoC available

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw that remained undetected for 13 years before recent discovery
- **Impact**: Enables remote code execution and system compromise
- **Status**: Actively exploited in the wild, patch available
- **CVE ID**: CVE-2026-34197

### TBK DVR Security Flaw
- **Description**: Vulnerability in TBK DVR systems being exploited by Mirai botnet variant Nexcorium
- **Impact**: Device hijacking for DDoS botnet recruitment
- **Status**: Active exploitation ongoing
- **CVE ID**: CVE-2024-3721

### Protobuf.js Critical Flaw
- **Description**: Critical remote code execution vulnerability in protobuf.js JavaScript implementation
- **Impact**: JavaScript code execution in affected applications
- **Status**: Proof-of-concept exploit code published

### Windows Zero-Days
- **Description**: Recently leaked Windows security vulnerabilities targeting privilege escalation
- **Impact**: SYSTEM or elevated administrator permissions
- **Status**: Active exploitation in attacks

## Affected Systems and Products

- **Microsoft Defender**: All versions affected by three zero-day vulnerabilities
- **Apache ActiveMQ Classic**: All versions prior to latest security update
- **TBK DVR Systems**: Digital video recorders vulnerable to botnet recruitment
- **End-of-Life TP-Link Routers**: Legacy Wi-Fi routers targeted by Mirai variants
- **Protobuf.js Library**: JavaScript applications using Google's Protocol Buffers implementation
- **Windows Systems**: Multiple versions affected by recently disclosed zero-days
- **Microsoft Teams Desktop Client**: Right-click paste functionality broken by Edge browser updates

## Attack Vectors and Techniques

- **Privilege Escalation**: Exploitation of Microsoft Defender zero-days for SYSTEM access
- **Remote Code Execution**: ActiveMQ and Protobuf vulnerabilities enabling code execution
- **Botnet Recruitment**: Mirai variants targeting IoT devices and DVR systems
- **Virtual Machine Evasion**: Payouts King ransomware using QEMU emulator to bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishing groups adopting legitimate device login flows
- **ClickFix Attacks**: North Korean groups targeting macOS users with fake job offers and Zoom updates
- **Scheduled Task Persistence**: Dragon Boss adware establishing persistence and excluding payloads from Windows Defender

## Threat Actor Activities

- **Huntress Research**: Identified active exploitation of Microsoft Defender zero-days
- **Nexcorium Botnet**: Mirai variant exploiting DVR and router vulnerabilities for DDoS operations
- **Payouts King Ransomware**: Using QEMU virtual machines as reverse SSH backdoors
- **Tycoon 2FA Phishing Groups**: Scattered operations adopting device code phishing techniques
- **North Korean Sapphire Sleet**: Targeting macOS users with ClickFix attacks and credential theft
- **Dragon Boss Operators**: Transforming adware into antivirus-killing malware
- **PowMix Botnet**: Targeting Czech Republic workforce with randomized command-and-control traffic
- **Operation PowerOFF**: Law enforcement operation seizing 53 DDoS domains and exposing 3 million criminal accounts