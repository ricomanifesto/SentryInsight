# Exploitation Report

Critical exploitation activity is currently focused on several high-impact vulnerabilities affecting widely-used systems. Most concerning are three Microsoft Defender zero-day vulnerabilities being actively exploited for privilege escalation, with two remaining unpatched. Additionally, threat actors are leveraging CVE-2024-3721 in TBK DVRs and CVE-2026-34197 in Apache ActiveMQ Classic for widespread attacks. The security landscape is further complicated by sophisticated attack techniques including QEMU-based virtual machine evasion by ransomware groups and the emergence of device code phishing campaigns targeting multi-factor authentication systems.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that allow threat actors to gain elevated privileges in compromised systems
- **Impact**: Attackers can escalate privileges to SYSTEM or elevated administrator permissions
- **Status**: One vulnerability has been patched, two remain unpatched and actively exploited

### TBK DVR Vulnerability
- **Description**: Security flaw in TBK DVR systems being exploited by the Mirai botnet variant Nexcorium
- **Impact**: Complete device compromise for DDoS botnet recruitment
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2024-3721

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years before being patched
- **Impact**: Remote code execution and system compromise
- **Status**: Added to CISA KEV catalog due to active exploitation
- **CVE ID**: CVE-2026-34197

### Protobuf.js Critical Vulnerability
- **Description**: Critical remote code execution flaw in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: JavaScript code execution in affected applications
- **Status**: Proof-of-concept exploit code has been published

## Affected Systems and Products

- **TBK DVR Systems**: Digital video recording devices compromised for botnet operations
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy networking equipment targeted by Mirai variants
- **Microsoft Defender**: Enterprise endpoint security solution with multiple zero-day vulnerabilities
- **Apache ActiveMQ Classic**: Message broker software used in enterprise environments
- **Vercel Cloud Platform**: Development platform experiencing confirmed security breach
- **Windows Domain Controllers**: Servers experiencing reboot loops after April 2026 security updates
- **DraftKings Gaming Platform**: Thousands of user accounts compromised and sold on underground markets
- **Protobuf.js Library**: JavaScript applications using Protocol Buffers implementation

## Attack Vectors and Techniques

- **QEMU Virtual Machine Evasion**: Payouts King ransomware uses QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishing group adopting legitimate new-device login flows to trick victims into granting account access
- **Apple Account Notification Abuse**: Threat actors manipulating Apple's legitimate account change notification system to send phishing emails
- **ClickFix Attacks**: North Korean Sapphire Sleet group using fake job offers and phony Zoom updates to deliver credential-stealing attacks targeting macOS users
- **Scheduled Task Persistence**: Dragon Boss adware establishing persistence through Windows scheduled tasks while excluding payloads from Windows Defender

## Threat Actor Activities

- **Mirai Botnet Operators**: Deploying Nexcorium variant to exploit DVR and router vulnerabilities for DDoS infrastructure expansion
- **Payouts King Ransomware Group**: Implementing sophisticated VM-based evasion techniques to bypass modern endpoint detection
- **Tycoon 2FA Phishing Group**: Transitioning to device code phishing techniques to overcome traditional 2FA protections
- **Sapphire Sleet (North Korea)**: Targeting macOS users through fake employment opportunities and software update schemes
- **Dragon Boss Campaign**: Transforming from benign adware into antivirus-killing malware with advanced persistence mechanisms
- **Vercel Breach Actors**: Unknown threat actors claiming to possess and sell stolen data from the cloud development platform
- **DraftKings Account Sellers**: Criminal operation involving tens of thousands of compromised gaming accounts sold through underground markets