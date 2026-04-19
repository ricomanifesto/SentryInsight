# Exploitation Report

The current threat landscape shows significant zero-day exploitation activity targeting Microsoft Windows and enterprise infrastructure. Three Microsoft Defender zero-day vulnerabilities are under active exploitation with two remaining unpatched, enabling privilege escalation attacks. Concurrently, threat actors are exploiting recently disclosed vulnerabilities in Apache ActiveMQ Classic and TBK DVR systems to compromise enterprise messaging infrastructure and deploy DDoS botnets. The Mirai-variant Nexcorium botnet is leveraging these flaws alongside attacks on end-of-life TP-Link routers, while sophisticated ransomware operations like Payouts King are implementing advanced evasion techniques using QEMU virtual machines to bypass endpoint security solutions.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender enabling privilege escalation
- **Impact**: Threat actors can gain elevated privileges and SYSTEM-level access in compromised systems
- **Status**: Active exploitation confirmed; two vulnerabilities remain unpatched

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic message broker that remained undetected for 13 years
- **Impact**: Enables remote code execution and system compromise
- **Status**: Actively exploited in the wild; patched earlier this month
- **CVE ID**: CVE-2026-34197

### TBK DVR Security Flaws
- **Description**: Security vulnerabilities in TBK Digital Video Recorder systems being exploited by Mirai variants
- **Impact**: Device hijacking for DDoS botnet recruitment and remote control capabilities
- **Status**: Active exploitation by Nexcorium variant
- **CVE ID**: CVE-2024-3721

### Protobuf.js Critical Vulnerability
- **Description**: Critical remote code execution flaw in protobuf.js, the JavaScript implementation of Google's Protocol Buffers
- **Impact**: JavaScript code execution and potential system compromise
- **Status**: Proof-of-concept exploit code published; critical severity

## Affected Systems and Products

- **Microsoft Defender**: Security solution experiencing zero-day exploitation enabling privilege escalation
- **Apache ActiveMQ Classic**: Enterprise message broker systems vulnerable to remote code execution
- **TBK DVR Systems**: Digital video recorders being compromised for botnet operations
- **End-of-life TP-Link Wi-Fi Routers**: Legacy networking equipment targeted by Mirai variants
- **Protobuf.js Library**: Widely-used JavaScript Protocol Buffer implementation
- **Windows Domain Controllers**: Servers experiencing reboot loops after April 2026 security updates
- **Microsoft Teams Desktop Client**: Application functionality broken by Edge browser updates

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Microsoft Defender vulnerabilities for privilege escalation
- **Botnet Deployment**: Mirai variant Nexcorium exploiting IoT devices for DDoS infrastructure
- **Virtual Machine Evasion**: Payouts King ransomware using QEMU emulator to create hidden VMs and bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishing groups adopting legitimate new-device login flows to trick victims
- **Apple Account Abuse**: Legitimate Apple notification system exploited to send convincing phishing emails
- **QEMU Reverse SSH Backdoor**: Advanced persistence mechanism creating hidden virtual environments
- **Cryptocurrency Exchange Compromise**: Multi-million dollar attacks on financial platforms

## Threat Actor Activities

- **Huntress Research**: Identified active exploitation of three Microsoft Defender zero-days with ongoing privilege escalation campaigns
- **Nexcorium Operators**: Mirai variant group targeting TBK DVRs and TP-Link routers for DDoS botnet expansion
- **Payouts King Ransomware Group**: Sophisticated operators using QEMU virtualization for endpoint security evasion
- **Tycoon 2FA Phishing Network**: Evolved phishing operation adopting device code authentication bypass techniques
- **Apple Phishing Campaign**: Threat actors leveraging legitimate Apple infrastructure for convincing iPhone purchase scams
- **Grinex Exchange Attackers**: Unidentified actors responsible for $13.7 million cryptocurrency theft from sanctioned exchange