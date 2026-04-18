# Exploitation Report

Critical zero-day vulnerabilities in Microsoft Defender are under active exploitation by threat actors seeking to gain elevated privileges on compromised systems. Three recently disclosed Microsoft Defender security flaws are being exploited, with two remaining unpatched despite active exploitation warnings from security researchers. Additionally, the Apache ActiveMQ vulnerability CVE-2026-34197 has been flagged by CISA as actively exploited after remaining undetected for 13 years. Threat actors are also exploiting recently leaked Windows zero-days targeting SYSTEM and administrator privileges, while sophisticated ransomware operations like Payouts King are using virtual machine techniques to bypass endpoint security solutions.

## Active Exploitation Details

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Three recently disclosed security flaws in Microsoft Defender allowing threat actors to gain elevated privileges in compromised systems
- **Impact**: Attackers can escalate privileges to SYSTEM level or elevated administrator permissions
- **Status**: Two vulnerabilities remain unpatched despite active exploitation warnings

### RedSun Microsoft Defender Zero-Day
- **Description**: A proof-of-concept exploit published by researcher "Chaotic Eclipse" targeting Microsoft Defender
- **Impact**: Grants SYSTEM privileges to attackers
- **Status**: Actively exploited with public proof-of-concept available

### Apache ActiveMQ Classic Vulnerability
- **Description**: High-severity security flaw in Apache ActiveMQ Classic that went undetected for 13 years
- **Impact**: Allows unauthorized access and potential system compromise
- **Status**: Actively exploited in the wild, patched earlier this month
- **CVE ID**: CVE-2026-34197

### Windows Zero-Day Vulnerabilities
- **Description**: Recently leaked Windows security vulnerabilities targeting privilege escalation
- **Impact**: Attackers can gain SYSTEM or elevated administrator permissions
- **Status**: Actively exploited following recent disclosure

### Marimo Reactive Python Notebook Vulnerability
- **Description**: Critical vulnerability in Marimo reactive Python notebook platform
- **Impact**: Used to deploy NKAbuse malware hosted on Hugging Face Spaces
- **Status**: Actively exploited to distribute malware

## Affected Systems and Products

- **Microsoft Defender**: All versions affected by three zero-day vulnerabilities
- **Windows Systems**: Domain controllers and servers experiencing issues with April 2026 security updates
- **Apache ActiveMQ Classic**: All versions prior to recent patch affected by 13-year-old vulnerability
- **Marimo Reactive Python Notebook**: Critical vulnerability enabling malware deployment
- **DraftKings Platform**: Thousands of accounts compromised and sold on underground markets
- **Water Treatment Systems**: Targeted by ZionSiphon malware for operational disruption

## Attack Vectors and Techniques

- **Virtual Machine Evasion**: Payouts King ransomware uses QEMU emulator as reverse SSH backdoor to run hidden virtual machines and bypass endpoint security
- **Device Code Phishing**: Tycoon 2FA phishers adopting device code phishing techniques to trick victims into granting account access
- **ClickFix Attacks**: North Korean actors using fake job offers and phony Zoom updates to deliver credential-stealing attacks on macOS systems
- **AI-Powered Vishing**: ATHR platform uses AI voice agents for automated voice phishing attacks with human operator assistance
- **Privilege Escalation**: Multiple zero-day exploits targeting SYSTEM and administrator privilege escalation

## Threat Actor Activities

- **Payouts King**: Ransomware group using sophisticated QEMU virtual machine techniques to evade detection and maintain persistence
- **Tycoon 2FA Phishers**: Adapting to device code phishing methods to bypass two-factor authentication protections
- **Sapphire Sleet (North Korea)**: Targeting macOS users with ClickFix attacks using fake job offers and software updates
- **PowMix Botnet Operators**: Targeting Czech Republic workforce with randomized command-and-control traffic since December
- **Underground Carding Networks**: Sophisticated evaluation systems for stolen credit card shops with quality and reputation verification
- **DDoS-for-Hire Services**: Operation PowerOFF identified 75,000 users across 53 domains providing commercial DDoS services