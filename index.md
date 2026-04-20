# Exploitation Report

Current threat activity shows several critical zero-day vulnerabilities under active exploitation, with threat actors leveraging both newly disclosed flaws and sophisticated evasion techniques. Most concerning are three Microsoft Defender zero-days being actively exploited for privilege escalation, with two remaining unpatched. Additionally, attackers are exploiting CVE-2026-34197 in Apache ActiveMQ and CVE-2024-3721 in TBK DVRs for botnet operations. Recent Windows zero-days leaked to the public are now being weaponized in the wild, while ransomware operators are employing virtual machine-based evasion tactics to bypass endpoint security solutions.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that enable privilege escalation
- **Impact**: Attackers can gain elevated privileges and SYSTEM-level access in compromised systems
- **Status**: One vulnerability has been patched, two remain unpatched and under active exploitation

### Apache ActiveMQ Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years
- **Impact**: Enables unauthorized access and potential system compromise
- **Status**: Actively exploited in attacks, patched in April 2026
- **CVE ID**: CVE-2026-34197

### TBK DVR Vulnerability in Mirai Botnet Campaign
- **Description**: Security flaw in TBK DVR systems being exploited by Nexcorium Mirai variant
- **Impact**: Hijacking of DVR devices for DDoS botnet operations
- **Status**: Under active exploitation for botnet recruitment
- **CVE ID**: CVE-2024-3721

### Windows Zero-Day Vulnerabilities
- **Description**: Recently leaked Windows security vulnerabilities targeting privilege escalation
- **Impact**: Attackers achieve SYSTEM or elevated administrator permissions
- **Status**: Under active exploitation following public disclosure

### Protobuf.js Remote Code Execution
- **Description**: Critical flaw in protobuf.js JavaScript implementation of Google's Protocol Buffers
- **Impact**: Remote code execution in JavaScript environments
- **Status**: Proof-of-concept exploit code published, increasing exploitation risk

## Affected Systems and Products

- **Microsoft Defender**: Multiple versions affected by three zero-day vulnerabilities
- **Apache ActiveMQ Classic**: All versions prior to April 2026 patch vulnerable to CVE-2026-34197
- **TBK DVR Systems**: DVR devices compromised for botnet operations via CVE-2024-3721
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy routers targeted in Mirai botnet campaigns
- **Windows Systems**: Various Windows versions affected by recently leaked zero-days
- **JavaScript Applications**: Systems using protobuf.js library vulnerable to RCE attacks
- **Apple Accounts**: Account change notification system being abused for phishing campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being weaponized for privilege escalation
- **Virtual Machine Evasion**: Payouts King ransomware using QEMU VMs with reverse SSH backdoors to bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA attackers adopting legitimate new-device login flows to steal account access
- **Botnet Recruitment**: Mirai variants targeting IoT devices through known vulnerabilities
- **Phishing via Legitimate Channels**: Apple account notifications being manipulated to send fake purchase alerts
- **Adware Transformation**: Dragon Boss adware evolving to disable antivirus protection via scheduled tasks

## Threat Actor Activities

- **Huntress-Identified Actors**: Actively exploiting three Microsoft Defender zero-days for privilege escalation in enterprise environments
- **Nexcorium Mirai Operators**: Deploying botnet variants targeting TBK DVRs and TP-Link routers for DDoS operations
- **Payouts King Ransomware Group**: Using QEMU emulator technology to create hidden virtual machines and evade detection
- **Tycoon 2FA Phishing Group**: Transitioning to device code phishing techniques targeting multi-factor authentication systems
- **Sapphire Sleet (North Korea)**: Using ClickFix attacks with fake job offers and Zoom updates to target macOS users
- **Dragon Boss Operators**: Transforming benign adware into antivirus-killing malware through scheduled task persistence
- **DraftKings Account Sellers**: Criminal marketplace operations selling access to compromised gaming accounts