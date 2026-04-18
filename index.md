# Exploitation Report

The current threat landscape is dominated by several critical zero-day vulnerabilities and active exploitation campaigns. Most concerning are three Microsoft Defender zero-day vulnerabilities being actively exploited to gain elevated privileges, with two remaining unpatched. Additionally, CISA has flagged an Apache ActiveMQ vulnerability (CVE-2026-34197) as actively exploited after remaining undetected for 13 years. Recently leaked Windows zero-days are also being weaponized in attacks targeting SYSTEM-level permissions. Threat actors are employing sophisticated techniques including QEMU virtual machine evasion, device code phishing, and AI-powered voice phishing platforms to bypass modern security controls.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender that allow attackers to gain elevated privileges in compromised systems
- **Impact**: Privilege escalation to SYSTEM or elevated administrator permissions
- **Status**: Actively exploited in the wild; two vulnerabilities remain unpatched

### RedSun Microsoft Defender Zero-Day
- **Description**: A newly disclosed proof-of-concept exploit for Microsoft Defender discovered by researcher "Chaotic Eclipse"
- **Impact**: Grants SYSTEM-level privileges to attackers
- **Status**: Proof-of-concept published; exploitation status unclear

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years before being patched
- **Impact**: Allows attackers to compromise message broker systems
- **Status**: Actively exploited in attacks; patch available
- **CVE ID**: CVE-2026-34197

### Recently Leaked Windows Zero-Days
- **Description**: Three recently disclosed Windows security vulnerabilities that were leaked and are now being exploited
- **Impact**: Allows attackers to gain SYSTEM or elevated administrator permissions
- **Status**: Actively exploited in attacks following disclosure

### Marimo Python Notebook Vulnerability
- **Description**: Critical vulnerability in Marimo reactive Python notebook platform
- **Impact**: Allows deployment of NKAbuse malware hosted on Hugging Face Spaces
- **Status**: Actively exploited to deploy malware

## Affected Systems and Products

- **Microsoft Defender**: All versions affected by three zero-day vulnerabilities
- **Windows Systems**: Domain controllers experiencing reboot loops after April 2026 security updates; general Windows systems affected by leaked zero-days
- **Apache ActiveMQ Classic**: All versions prior to recent patch containing 13-year-old vulnerability
- **Marimo Python Notebooks**: Reactive Python notebook platforms vulnerable to critical flaw
- **macOS Systems**: Targeted by North Korean threat actors using ClickFix attacks
- **Water Treatment Systems**: Targeted by ZionSiphon malware designed for operational technology sabotage

## Attack Vectors and Techniques

- **QEMU Virtual Machine Evasion**: Payouts King ransomware uses QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA attackers use legitimate new-device login flows to trick victims into granting account access
- **ClickFix Attacks**: North Korean Sapphire Sleet group uses fake job offers and phony Zoom updates to deliver credential-stealing attacks on macOS
- **AI Voice Phishing**: ATHR platform employs AI voice agents for fully automated vishing attacks with human operator backup
- **Malware Hosting on AI Platforms**: Attackers leverage Hugging Face Spaces to host and distribute NKAbuse malware
- **Scheduled Task Persistence**: Dragon Boss adware establishes persistence via scheduled tasks and excludes payloads from Windows Defender

## Threat Actor Activities

- **Payouts King**: Ransomware group using QEMU virtual machines to evade detection and maintain persistence on compromised systems
- **Tycoon 2FA Group**: Phishing operation that has scattered and adopted device code phishing techniques to bypass two-factor authentication
- **Sapphire Sleet (North Korea)**: Targeting macOS users with ClickFix attacks using fake job offers and software updates to steal credentials and sensitive data
- **PowMix Botnet Operators**: Targeting Czech Republic workforce since December with randomized command-and-control traffic
- **DraftKings Account Sellers**: Criminal operation selling access to tens of thousands of compromised gambling accounts
- **DDoS-for-Hire Services**: Operation PowerOFF identified 75,000 users and seized 53 domains across 21 countries in latest crackdown
- **Water Infrastructure Attackers**: ZionSiphon malware operators specifically targeting water treatment and desalination facilities for sabotage operations