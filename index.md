# Exploitation Report

Critical exploitation activity is currently centered around Microsoft Defender vulnerabilities and Apache ActiveMQ systems. Three Microsoft Defender zero-day vulnerabilities are being actively exploited by threat actors to gain elevated privileges, with two remaining unpatched. Additionally, a high-severity Apache ActiveMQ vulnerability (CVE-2026-34197) that went undetected for 13 years is now under active exploitation, prompting CISA to add it to their Known Exploited Vulnerabilities catalog. Recent leaked Windows security vulnerabilities are also being exploited in the wild to gain SYSTEM or elevated administrator permissions. Meanwhile, sophisticated attack campaigns are leveraging novel techniques including QEMU virtual machines to bypass endpoint security and AI-powered voice phishing platforms for automated credential harvesting.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that allow threat actors to gain elevated privileges in compromised systems
- **Impact**: Attackers can escalate privileges to SYSTEM level or elevated administrator permissions
- **Status**: One vulnerability has been patched, two remain unpatched and actively exploited

### RedSun Microsoft Defender Zero-Day
- **Description**: A second Microsoft Defender zero-day vulnerability with published proof-of-concept exploit code
- **Impact**: Grants attackers SYSTEM privileges on compromised systems
- **Status**: Actively exploited with public PoC available

### Apache ActiveMQ Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years
- **Impact**: Allows remote code execution and system compromise
- **Status**: Actively exploited in the wild, patch available
- **CVE ID**: CVE-2026-34197

### Recently Leaked Windows Zero-Days
- **Description**: Three recently disclosed Windows security vulnerabilities that have been leaked
- **Impact**: Enable attackers to gain SYSTEM or elevated administrator permissions
- **Status**: Actively exploited in attacks following public disclosure

### Marimo Vulnerability
- **Description**: Critical vulnerability in Marimo reactive Python notebook platform
- **Impact**: Used to deploy NKAbuse malware from Hugging Face Spaces
- **Status**: Actively exploited for malware deployment

## Affected Systems and Products

- **Microsoft Defender**: All versions affected by multiple zero-day vulnerabilities
- **Windows Systems**: Domain controllers and servers affected by security update issues and zero-day exploits
- **Apache ActiveMQ Classic**: All versions prior to recent patch affected by 13-year-old vulnerability
- **Marimo Platform**: Python notebook environments vulnerable to malware deployment
- **Water Treatment Systems**: Targeted by ZionSiphon malware for operational technology sabotage
- **macOS Systems**: Targeted by North Korean threat actors using ClickFix attacks
- **QEMU Virtual Machines**: Used by Payouts King ransomware to bypass endpoint security

## Attack Vectors and Techniques

- **QEMU VM Bypass**: Payouts King ransomware uses QEMU emulator as reverse SSH backdoor to run hidden virtual machines and evade detection
- **Device Code Phishing**: Tycoon 2FA threat actors exploit legitimate new-device login flows to steal account access
- **ClickFix Social Engineering**: North Korean Sapphire Sleet group uses fake job offers and phony Zoom updates to deliver credential-stealing attacks
- **AI Voice Phishing**: ATHR platform deploys fully automated voice phishing using AI agents and human operators
- **Malware Hosting**: Threat actors abuse Hugging Face Spaces to host NKAbuse malware variants
- **Privilege Escalation**: Multiple Windows and Defender vulnerabilities exploited for SYSTEM-level access
- **Scheduled Task Persistence**: Dragon Boss adware establishes persistence and excludes payloads from Windows Defender

## Threat Actor Activities

- **Payouts King**: Ransomware operators using novel QEMU virtualization techniques to bypass endpoint security solutions
- **Tycoon 2FA Group**: Phishing operators adapting to device code phishing techniques after dispersing from traditional methods
- **Sapphire Sleet (North Korea)**: Targeting macOS users with ClickFix attacks using fake job offers and software updates
- **PowMix Botnet Operators**: Targeting Czech Republic workforce with randomized command and control traffic
- **Criminal DDoS Networks**: Over 75,000 users identified in Operation PowerOFF targeting distributed denial-of-service ecosystems
- **Grinex Hackers**: Attributed $13.7 million cryptocurrency exchange hack to Western intelligence agencies
- **Dragon Boss Operators**: Transforming benign adware into antivirus-killing malware through March 2025 updates