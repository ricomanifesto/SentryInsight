# Exploitation Report

Critical active exploitation is occurring across multiple fronts, with Microsoft Defender facing three zero-day vulnerabilities currently being exploited in the wild, two of which remain unpatched. The threat landscape is further complicated by the active exploitation of a newly disclosed Apache ActiveMQ vulnerability that CISA has added to its Known Exploited Vulnerabilities catalog. Additionally, threat actors are leveraging a Mirai variant called Nexcorium to exploit TBK DVR systems, while various ransomware groups and nation-state actors are deploying sophisticated new attack techniques including virtual machine-based evasion and device code phishing.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender are being actively exploited by threat actors to gain elevated privileges
- **Impact**: Attackers can achieve SYSTEM or elevated administrator permissions on compromised systems
- **Status**: Active exploitation confirmed; two vulnerabilities remain unpatched

### Microsoft Defender RedSun Zero-Day
- **Description**: A second Microsoft Defender zero-day vulnerability published as a proof-of-concept exploit within two weeks
- **Impact**: Grants SYSTEM privileges to attackers
- **Status**: Proof-of-concept available; actively exploited

### Apache ActiveMQ Classic Vulnerability
- **Description**: A high-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years before being patched
- **Impact**: Enables attackers to compromise Apache ActiveMQ systems
- **Status**: Actively exploited in attacks; patched earlier this month
- **CVE ID**: CVE-2026-34197

### TBK DVR Vulnerability
- **Description**: Security flaw in TBK DVR systems being exploited by the Mirai variant Nexcorium
- **Impact**: Allows hijacking of devices for DDoS botnet operations
- **Status**: Actively exploited by Nexcorium botnet
- **CVE ID**: CVE-2024-3721

### Protobuf.js Critical Remote Code Execution
- **Description**: Critical remote code execution flaw in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: Enables JavaScript code execution in affected applications
- **Status**: Proof-of-concept exploit code published

## Affected Systems and Products

- **Microsoft Defender**: All versions affected by three zero-day vulnerabilities
- **Apache ActiveMQ Classic**: Legacy versions affected by 13-year-old vulnerability
- **TBK DVR Systems**: All models vulnerable to Nexcorium botnet exploitation
- **End-of-Life TP-Link Wi-Fi Routers**: Targeted alongside TBK DVRs for botnet recruitment
- **Protobuf.js Library**: JavaScript applications using Protocol Buffers implementation
- **Windows Domain Controllers**: Some experiencing reboot loops after April 2026 security updates
- **Microsoft Teams Desktop Client**: Right-click paste functionality broken by Edge update
- **Water Treatment Systems**: Targeted by ZionSiphon operational technology malware
- **macOS Systems**: Targeted by North Korean ClickFix attacks

## Attack Vectors and Techniques

- **Virtual Machine Evasion**: Payouts King ransomware uses QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishers have adopted device code phishing techniques, tricking victims into granting account access through legitimate new-device login flows
- **Randomized Command and Control**: PowMix botnet uses randomized C2 traffic to evade detection while targeting Czech workforce
- **Fake Job Offers**: North Korean Sapphire Sleet group uses fraudulent job offers and phony Zoom updates to deliver ClickFix attacks
- **Scheduled Task Persistence**: Dragon Boss adware establishes persistence via scheduled tasks and configures Windows Defender exclusions
- **OT-Specific Targeting**: ZionSiphon malware specifically designed for operational technology environments in water treatment facilities

## Threat Actor Activities

- **Huntress Research**: Identified and reported the three actively exploited Microsoft Defender zero-days
- **Chaotic Eclipse**: Published proof-of-concept exploits for Microsoft Defender zero-days in protest of Microsoft's security research handling
- **Nexcorium Operators**: Deploying Mirai variant to exploit TBK DVRs and end-of-life TP-Link routers for DDoS operations
- **Payouts King Group**: Using sophisticated QEMU-based evasion techniques to deploy ransomware while bypassing endpoint security
- **Tycoon 2FA Phishers**: Evolved tactics to include device code phishing for bypassing multi-factor authentication
- **Sapphire Sleet (North Korea)**: Targeting macOS users with ClickFix attacks using fake job offers and Zoom updates
- **PowMix Operators**: Running active campaign against Czech workforce since December 2025 using randomized C2 infrastructure
- **ZionSiphon Developers**: Creating specialized malware for sabotaging water treatment and desalination systems
- **Operation PowerOFF Targets**: International law enforcement identified over 75,000 DDoS users across 21 countries and seized 53 domains