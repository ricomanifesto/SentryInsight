# Exploitation Report

Current threat landscapes reveal severe active exploitation across multiple critical systems, with several zero-day vulnerabilities being weaponized in the wild. The most concerning activity includes three Microsoft Defender zero-day exploits with two remaining unpatched, active exploitation of a 13-year-old Apache ActiveMQ vulnerability now flagged by CISA, and sophisticated ransomware operations using virtualization techniques to evade security controls. Additionally, IoT botnets are leveraging known vulnerabilities in DVR systems, while nation-state actors are deploying advanced phishing techniques and infrastructure-targeting malware designed specifically for operational technology environments.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender are being actively exploited by threat actors to gain elevated privileges in compromised systems
- **Impact**: Attackers can obtain SYSTEM or elevated administrator permissions on compromised systems
- **Status**: One vulnerability has been patched, but two remain unpatched and actively exploited

### Microsoft Defender "RedSun" Zero-Day
- **Description**: A second Microsoft Defender zero-day vulnerability with published proof-of-concept exploit code
- **Impact**: Grants SYSTEM privileges to attackers on compromised Windows systems
- **Status**: Actively exploited with public PoC available, patch status unclear

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years before being patched earlier this month
- **Impact**: Allows attackers to compromise message broker systems and potentially gain unauthorized access to enterprise messaging infrastructure
- **Status**: Actively exploited in the wild, patched but exploitation continuing
- **CVE ID**: CVE-2026-34197

### TBK DVR Vulnerability
- **Description**: Security flaw in TBK DVR systems being exploited by Mirai botnet variants
- **Impact**: Allows threat actors to hijack DVR devices for use in DDoS botnets and other malicious activities
- **Status**: Actively exploited by Nexcorium Mirai variant
- **CVE ID**: CVE-2024-3721

### Protobuf.js Critical Vulnerability
- **Description**: Critical remote code execution flaw in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: Enables JavaScript code execution in applications using the vulnerable library
- **Status**: Proof-of-concept exploit code has been published

## Affected Systems and Products

- **Microsoft Defender**: Windows endpoint security solution affected by multiple zero-day vulnerabilities
- **Apache ActiveMQ Classic**: Enterprise message broker systems vulnerable to 13-year-old undetected flaw
- **TBK DVR Systems**: Digital video recorders being compromised for botnet recruitment
- **TP-Link Wi-Fi Routers**: End-of-life devices targeted by Mirai variants
- **protobuf.js Library**: JavaScript applications using Google's Protocol Buffers implementation
- **Windows Domain Controllers**: Some servers experiencing reboot loops after April 2026 security updates
- **macOS Systems**: Targeted by North Korean threat actors using ClickFix techniques
- **Czech Republic Workforce Systems**: Targeted by PowMix botnet campaign

## Attack Vectors and Techniques

- **Privilege Escalation**: Microsoft Defender vulnerabilities exploited to gain SYSTEM privileges
- **IoT Botnet Recruitment**: DVR and router vulnerabilities used to build DDoS botnets
- **QEMU VM Evasion**: Payouts King ransomware using QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **ClickFix Phishing**: North Korean Sapphire Sleet group using fake job offers and phony Zoom updates to steal credentials and data from macOS users
- **Device Code Phishing**: Tycoon 2FA phishers adopting legitimate new-device login flows to trick victims into granting account access
- **Adware-to-Malware Evolution**: Dragon Boss adware transforming into antivirus killer through scheduled tasks and Windows Defender exclusions

## Threat Actor Activities

- **Microsoft Defender Exploiters**: Unknown threat actors actively exploiting three zero-day vulnerabilities for privilege escalation
- **Nexcorium Operators**: Mirai variant operators exploiting TBK DVR and TP-Link router vulnerabilities for botnet expansion
- **Payouts King Group**: Ransomware operators using sophisticated QEMU virtualization techniques to evade endpoint security
- **Sapphire Sleet (North Korea)**: Nation-state group targeting macOS users with ClickFix attacks using fake job offers and Zoom updates
- **Tycoon 2FA Group**: Phishing operators adapting to use device code phishing techniques against 2FA-protected accounts
- **PowMix Operators**: New botnet campaign specifically targeting Czech Republic workforce with randomized C2 traffic
- **ZionSiphon Attackers**: Advanced threat actors deploying operational technology-specific malware designed to sabotage water treatment and desalination systems