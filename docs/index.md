# Exploitation Report

Critical exploitation activity is currently targeting multiple high-profile vulnerabilities across diverse platforms. The most concerning developments include three Microsoft Defender zero-day vulnerabilities being actively exploited by threat actors, with two remaining unpatched. Simultaneously, attackers are leveraging CVE-2024-3721 in TBK DVRs to deploy Mirai botnet variants, while CVE-2026-34197 in Apache ActiveMQ has been added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation. Additional threats include a critical remote code execution flaw in the widely-used protobuf.js library and sophisticated ransomware operations using QEMU virtualization to bypass security controls.

## Active Exploitation Details

### Microsoft Defender Zero-Days
- **Description**: Three recently disclosed security flaws in Microsoft Defender allowing threat actors to gain elevated privileges in compromised systems
- **Impact**: Attackers can achieve SYSTEM or elevated administrator permissions on compromised Windows systems
- **Status**: One vulnerability has been patched, two remain unpatched and actively exploited

### TBK DVR Vulnerability
- **Description**: Security flaw in TBK Digital Video Recorders being exploited by Mirai botnet variants
- **Impact**: Complete device compromise enabling DDoS botnet recruitment and remote control
- **Status**: Actively exploited in the wild by threat actors deploying Nexcorium Mirai variant
- **CVE ID**: CVE-2024-3721

### Apache ActiveMQ Vulnerability
- **Description**: High-severity flaw in Apache ActiveMQ Classic that went undetected for 13 years
- **Impact**: Remote code execution and system compromise capabilities
- **Status**: Patched earlier this month but now actively exploited; added to CISA KEV catalog
- **CVE ID**: CVE-2026-34197

### Protobuf.js Critical Flaw
- **Description**: Critical remote code execution vulnerability in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: JavaScript code execution in affected applications
- **Status**: Proof-of-concept exploit code has been published

### Windows Zero-Day Vulnerabilities
- **Description**: Recently leaked Windows security vulnerabilities being exploited for privilege escalation
- **Impact**: SYSTEM or elevated administrator permissions on Windows systems
- **Status**: Recently disclosed and now actively exploited in attacks

## Affected Systems and Products

- **Microsoft Defender**: Windows endpoint security solution affected by multiple zero-day vulnerabilities
- **TBK Digital Video Recorders**: DVR systems compromised for botnet recruitment
- **Apache ActiveMQ Classic**: Message broker software vulnerable to remote exploitation
- **Protobuf.js Library**: JavaScript Protocol Buffers implementation used across web applications
- **Windows Operating Systems**: Multiple versions affected by recently leaked zero-day vulnerabilities
- **TP-Link Wi-Fi Routers**: End-of-life devices targeted alongside TBK DVRs for botnet operations

## Attack Vectors and Techniques

- **QEMU Virtualization Evasion**: Payouts King ransomware uses QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishing group adopting device code phishing techniques to trick victims into granting account access through legitimate new-device login flows
- **Botnet Recruitment**: Mirai variant Nexcorium exploiting IoT devices to build DDoS botnets
- **Privilege Escalation**: Multiple Windows and Defender vulnerabilities being chained for system-level access
- **ClickFix Attacks**: North Korean Sapphire Sleet group using fake job offers and phony Zoom updates to deliver credential-stealing attacks against macOS users

## Threat Actor Activities

- **Huntress Research**: Identified and reported active exploitation of three Microsoft Defender zero-days
- **Nexcorium Botnet Operators**: Deploying Mirai variants through CVE-2024-3721 exploitation in TBK DVRs
- **Payouts King Ransomware Group**: Utilizing QEMU virtualization techniques to evade detection while deploying ransomware
- **Tycoon 2FA Phishing Group**: Transitioning to device code phishing techniques for enhanced credential theft
- **Sapphire Sleet (North Korea)**: Targeting macOS users with ClickFix attacks through fake job offers and software updates
- **PowMix Botnet Operators**: Conducting targeted campaigns against Czech Republic workforce using randomized command-and-control traffic
- **Chaotic Eclipse Researcher**: Published proof-of-concept for "RedSun" Microsoft Defender zero-day, protesting Microsoft's vulnerability disclosure practices