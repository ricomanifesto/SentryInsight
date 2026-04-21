# Exploitation Report

Current threat landscape reveals multiple critical exploitation activities targeting both enterprise infrastructure and operational technology systems. Notable active exploitations include three Microsoft Defender zero-day vulnerabilities being leveraged for privilege escalation, with two remaining unpatched. The SGLang vulnerability CVE-2026-5760 poses severe risks with remote code execution capabilities through malicious GGUF model files. Industrial systems face significant threats from the Nexcorium Mirai variant exploiting CVE-2024-3721 to compromise TBK DVR systems for botnet operations, while ZionSiphon malware specifically targets Israeli water treatment and desalination infrastructure. Additionally, serial-to-IP devices used in operational technology environments harbor thousands of vulnerabilities, creating widespread attack surfaces for threat actors.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender are being actively exploited by threat actors
- **Impact**: Attackers can gain elevated privileges in compromised systems
- **Status**: Active exploitation confirmed; two of the three vulnerabilities remain unpatched

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in SGLang that enables remote code execution through malicious GGUF model files
- **Impact**: Complete system compromise through remote code execution on susceptible systems
- **Status**: Critical vulnerability with CVSS score of 9.8
- **CVE ID**: CVE-2026-5760

### TBK DVR Exploitation for Botnet Operations
- **Description**: Security flaws in TBK DVR systems and end-of-life TP-Link Wi-Fi routers being exploited to deploy Mirai botnet variants
- **Impact**: Device compromise for DDoS botnet operations
- **Status**: Active exploitation by Nexcorium Mirai variant
- **CVE ID**: CVE-2024-3721

### Protobuf.js Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: JavaScript code execution on affected systems
- **Status**: Proof-of-concept exploit code published

## Affected Systems and Products

- **Microsoft Defender**: Multiple versions affected by three zero-day vulnerabilities
- **SGLang**: Systems processing GGUF model files vulnerable to remote code execution
- **TBK DVR Systems**: Digital video recorders compromised for botnet operations
- **TP-Link Wi-Fi Routers**: End-of-life devices targeted for Mirai variant deployment
- **Serial-to-IP Devices**: OT devices with thousands of old and new vulnerabilities
- **Protobuf.js Library**: JavaScript implementation of Google's Protocol Buffers
- **Israeli Water Treatment Systems**: Targeted by ZionSiphon malware
- **Desalination Systems**: Specifically targeted operational technology infrastructure

## Attack Vectors and Techniques

- **Malicious GGUF Model Files**: Remote code execution through specially crafted model files in SGLang
- **Privilege Escalation**: Microsoft Defender vulnerabilities exploited for elevated system access
- **Botnet Recruitment**: TBK DVR and router exploitation for DDoS botnet expansion
- **OT System Targeting**: Direct attacks on water treatment and desalination infrastructure
- **QEMU VM Evasion**: Payouts King ransomware using QEMU emulator as reverse SSH backdoor
- **Device Code Phishing**: Tycoon 2FA phishing groups adopting legitimate device login flows
- **SystemBC Proxy Botnet**: Network of over 1,570 compromised hosts used by Gentlemen ransomware
- **Microsoft Teams Abuse**: Helpdesk impersonation attacks leveraging external collaboration features

## Threat Actor Activities

- **Nexcorium Operators**: Deploying Mirai variant to compromise IoT devices for botnet operations
- **ZionSiphon Attackers**: Targeting Israeli critical infrastructure with specialized malware
- **Gentlemen Ransomware Group**: Utilizing SystemBC proxy malware botnet for enhanced attack capabilities
- **Scattered Spider**: British leader pleaded guilty to cryptocurrency theft and identity fraud charges
- **Payouts King Operators**: Using QEMU virtualization to evade endpoint security solutions
- **Tycoon 2FA Phishing Groups**: Adapting techniques to use device code phishing for account compromise
- **Microsoft Defender Exploiters**: Actively leveraging three zero-day vulnerabilities for privilege escalation
- **Seiko USA Attackers**: Website defacement and claimed customer database theft with ransom demands