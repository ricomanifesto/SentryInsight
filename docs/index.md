# Exploitation Report

Critical zero-day vulnerabilities in Microsoft Defender are being actively exploited to gain elevated privileges, while threat actors continue to exploit recently patched Apache ActiveMQ vulnerabilities and newly disclosed Marimo flaws. The current threat landscape shows sophisticated attackers leveraging both unpatched zero-days and recently discovered vulnerabilities across enterprise security tools, message brokers, and development platforms. Of particular concern are the three Microsoft Defender zero-days, two of which remain unpatched, alongside the ongoing exploitation of CVE-2026-34197 in Apache ActiveMQ Classic and attacks targeting TBK DVR systems using CVE-2024-3721.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that allow threat actors to gain elevated privileges and SYSTEM-level access on compromised systems
- **Impact**: Attackers can escalate privileges to gain SYSTEM or elevated administrator permissions, completely compromising affected systems
- **Status**: Active exploitation confirmed; two vulnerabilities remain unpatched while one has received a security update

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years before being patched
- **Impact**: Allows attackers to compromise message broker systems and potentially gain unauthorized access to enterprise messaging infrastructure
- **Status**: Actively exploited in the wild; patch available but exploitation continues
- **CVE ID**: CVE-2026-34197

### TBK DVR Security Flaw
- **Description**: Vulnerability in TBK Digital Video Recorder systems being exploited by the Nexcorium Mirai botnet variant
- **Impact**: Compromised DVR devices are recruited into DDoS botnets for large-scale distributed attacks
- **Status**: Active exploitation for botnet recruitment and DDoS operations
- **CVE ID**: CVE-2024-3721

### Marimo Critical Vulnerability
- **Description**: Critical security flaw in Marimo reactive Python notebook application
- **Impact**: Enables deployment of NKAbuse malware variants hosted on Hugging Face Spaces
- **Status**: Active exploitation to deploy malware from machine learning platforms

## Affected Systems and Products

- **Microsoft Defender**: All versions affected by the three zero-day vulnerabilities
- **Apache ActiveMQ Classic**: Versions containing the 13-year-old vulnerability
- **TBK DVR Systems**: Digital video recorder devices vulnerable to botnet recruitment
- **TP-Link Wi-Fi Routers**: End-of-life devices targeted for botnet incorporation
- **Marimo Python Notebooks**: Reactive notebook applications vulnerable to malware deployment
- **Windows Domain Controllers**: Some systems experiencing reboot loops after April 2026 security updates
- **Hugging Face Spaces**: Platform being abused to host NKAbuse malware variants

## Attack Vectors and Techniques

- **Privilege Escalation**: Exploitation of Microsoft Defender vulnerabilities to gain SYSTEM privileges
- **Botnet Recruitment**: Mirai variant attacks targeting IoT devices for DDoS operations
- **Supply Chain Abuse**: Using legitimate platforms like Hugging Face to host and distribute malware
- **Device Code Phishing**: Tycoon group adopting new techniques to bypass two-factor authentication
- **Virtual Machine Evasion**: Payouts King ransomware using QEMU emulators to bypass endpoint security
- **ClickFix Attacks**: North Korean threat actors using fake job offers and Zoom updates targeting macOS users

## Threat Actor Activities

- **Nexcorium Group**: Deploying Mirai botnet variants targeting TBK DVRs and TP-Link routers for DDoS operations
- **Tycoon 2FA Phishers**: Transitioning to device code phishing techniques to circumvent multi-factor authentication
- **Payouts King Ransomware**: Implementing QEMU virtual machines as reverse SSH backdoors to evade detection
- **Sapphire Sleet (North Korea)**: Conducting ClickFix campaigns against macOS users using social engineering
- **PowMix Botnet Operators**: Targeting Czech workforce with randomized command-and-control traffic
- **ZionSiphon Operators**: Developing specialized malware to sabotage water treatment and desalination systems
- **NKAbuse Distributors**: Leveraging Marimo vulnerabilities to deploy malware from AI/ML platforms