# Exploitation Report

Critical exploitation activity is dominating the current threat landscape with multiple zero-day vulnerabilities and high-impact flaws being actively exploited by threat actors. The most concerning developments include three Microsoft Defender zero-day vulnerabilities currently being exploited to gain elevated privileges, with two remaining unpatched. Additionally, a recently discovered Apache ActiveMQ vulnerability that went undetected for 13 years is now under active exploitation, prompting CISA to add it to their Known Exploited Vulnerabilities catalog. The Mirai botnet variant Nexcorium is actively exploiting TBK DVR vulnerabilities to build DDoS botnets, while new sophisticated attack techniques emerge including the use of virtual machines to bypass endpoint security and specialized malware targeting critical infrastructure systems.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that allow threat actors to gain elevated privileges in compromised systems
- **Impact**: Attackers can achieve SYSTEM or elevated administrator permissions on compromised systems
- **Status**: Currently being actively exploited; two vulnerabilities remain unpatched

### RedSun Microsoft Defender Zero-Day
- **Description**: A newly published proof-of-concept exploit for Microsoft Defender that grants SYSTEM-level privileges
- **Impact**: Complete system compromise with highest level administrative access
- **Status**: PoC exploit code publicly available, actively being exploited

### Apache ActiveMQ Vulnerability
- **Description**: A high-severity security flaw in Apache ActiveMQ Classic that remained undetected for 13 years before recent discovery and patching
- **Impact**: Remote code execution and system compromise
- **Status**: Active exploitation detected; added to CISA KEV catalog
- **CVE ID**: CVE-2026-34197

### TBK DVR Vulnerability in Mirai Botnet Campaign
- **Description**: Security flaws in TBK DVR systems being exploited by the Mirai variant Nexcorium to build DDoS botnets
- **Impact**: Device hijacking for distributed denial-of-service attacks
- **Status**: Active exploitation by botnet operators
- **CVE ID**: CVE-2024-3721

### Protobuf.js Critical Remote Code Execution
- **Description**: Critical vulnerability in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: Remote JavaScript code execution in applications using the library
- **Status**: Proof-of-concept exploit code published

## Affected Systems and Products

- **Microsoft Defender**: Multiple versions affected by zero-day vulnerabilities allowing privilege escalation
- **Apache ActiveMQ Classic**: All versions prior to recent security patch vulnerable to 13-year-old flaw
- **TBK DVR Systems**: Digital video recorders being hijacked for botnet operations
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy devices targeted in Mirai botnet campaigns
- **Protobuf.js Library**: JavaScript applications utilizing Google Protocol Buffers implementation
- **Windows Systems**: Domain controllers experiencing reboot loops after April 2026 security updates
- **Water Treatment Systems**: Critical infrastructure targeted by ZionSiphon malware
- **macOS Systems**: Apple devices targeted by North Korean ClickFix campaigns

## Attack Vectors and Techniques

- **Virtual Machine Evasion**: Payouts King ransomware using QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA attackers adopting device code phishing techniques to trick victims into granting account access through legitimate new-device login flows
- **ClickFix Social Engineering**: North Korean Sapphire Sleet group using fake job offers and phony Zoom updates to deliver credential-stealing attacks on macOS
- **Scheduled Task Persistence**: Dragon Boss adware establishing persistence through scheduled tasks while excluding future payloads from Windows Defender
- **DDoS Botnet Recruitment**: Mirai variant Nexcorium exploiting IoT device vulnerabilities to build distributed attack infrastructure
- **Critical Infrastructure Targeting**: ZionSiphon malware specifically designed to sabotage operational technology in water treatment and desalination facilities

## Threat Actor Activities

- **Huntress Research**: Identified and reported active exploitation of three Microsoft Defender zero-days with ongoing monitoring of attack campaigns
- **Chaotic Eclipse**: Security researcher publishing proof-of-concept exploits for Microsoft Defender zero-days in protest of company disclosure practices
- **Mirai Botnet Operators**: Deploying Nexcorium variant to compromise TBK DVRs and end-of-life TP-Link routers for DDoS infrastructure
- **Sapphire Sleet (North Korea)**: Conducting ClickFix campaigns against macOS users using social engineering and fake software updates to steal credentials and sensitive data
- **Payouts King Ransomware Group**: Utilizing sophisticated QEMU-based virtual machine techniques to evade endpoint detection and maintain persistence
- **Tycoon 2FA Phishing Group**: Evolving tactics to include device code phishing attacks that abuse legitimate authentication flows
- **ZionSiphon Operators**: Targeting water treatment and desalination facilities with specialized operational technology malware designed for infrastructure sabotage