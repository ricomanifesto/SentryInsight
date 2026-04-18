# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by multiple Microsoft Defender zero-day vulnerabilities being actively exploited for privilege escalation, alongside a TBK DVR vulnerability (CVE-2024-3721) being leveraged for botnet operations and a recently disclosed Apache ActiveMQ flaw (CVE-2026-34197) that has come under active attack. Three Microsoft Defender zero-days are particularly concerning as two remain unpatched despite active exploitation, while threat actors are also exploiting recently leaked Windows zero-days to gain SYSTEM privileges. Additionally, attackers are targeting IoT devices through CVE-2024-3721 to build DDoS botnets and exploiting a critical Marimo vulnerability to deploy NKAbuse malware.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender allowing privilege escalation
- **Impact**: Attackers can gain elevated privileges and SYSTEM-level access in compromised systems
- **Status**: One patched, two remain unpatched despite active exploitation

### Microsoft Defender "RedSun" Zero-Day
- **Description**: Second zero-day vulnerability in Microsoft Defender published as proof-of-concept
- **Impact**: Grants SYSTEM privileges to attackers
- **Status**: Proof-of-concept publicly available, exploitation status ongoing

### TBK DVR Vulnerability
- **Description**: Security flaw in TBK DVR systems being exploited by Mirai botnet variants
- **Impact**: Device hijacking for DDoS botnet operations
- **Status**: Actively exploited by Nexcorium variant
- **CVE ID**: CVE-2024-3721

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw that remained undetected for 13 years
- **Impact**: Remote code execution and system compromise
- **Status**: Actively exploited, patched earlier this month, added to CISA KEV
- **CVE ID**: CVE-2026-34197

### Recently Leaked Windows Zero-Days
- **Description**: Three recently disclosed Windows security vulnerabilities
- **Impact**: SYSTEM or elevated administrator permissions
- **Status**: Now being exploited in active attacks

### Marimo Critical Vulnerability
- **Description**: Critical vulnerability in Marimo reactive Python notebook
- **Impact**: Deployment of NKAbuse malware from Hugging Face platforms
- **Status**: Actively exploited

## Affected Systems and Products

- **Microsoft Defender**: Microsoft's endpoint protection platform affected by multiple zero-day vulnerabilities
- **TBK DVR Systems**: Digital video recorder systems vulnerable to botnet hijacking
- **End-of-Life TP-Link Wi-Fi Routers**: Legacy networking equipment targeted for botnet expansion
- **Apache ActiveMQ Classic**: Message broker software with 13-year-old vulnerability
- **Windows Systems**: Multiple Windows versions affected by recently leaked zero-days
- **Marimo Notebooks**: Python reactive notebook environment vulnerable to malware deployment

## Attack Vectors and Techniques

- **Privilege Escalation**: Exploitation of Microsoft Defender flaws to gain elevated system privileges
- **IoT Device Hijacking**: Targeting DVR and router vulnerabilities for botnet recruitment
- **DDoS Botnet Operations**: Using compromised devices for distributed denial-of-service attacks
- **Malware Deployment**: Leveraging Marimo vulnerabilities to host and distribute NKAbuse malware
- **Supply Chain Abuse**: Using legitimate platforms like Hugging Face Spaces for malware hosting
- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities for system compromise

## Threat Actor Activities

- **Nexcorium Operators**: Deploying Mirai variant to exploit TBK DVR and TP-Link router vulnerabilities for DDoS operations
- **Microsoft Defender Exploiters**: Multiple threat actors leveraging three different zero-day vulnerabilities for privilege escalation
- **NKAbuse Campaign**: Attackers exploiting Marimo vulnerability to deploy malware from Hugging Face infrastructure
- **Windows Zero-Day Exploiters**: Threat actors capitalizing on recently leaked Windows vulnerabilities for system compromise
- **Apache ActiveMQ Attackers**: Exploitation of the 13-year-old vulnerability following public disclosure and patch release