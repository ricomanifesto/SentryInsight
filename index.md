# Exploitation Report

Microsoft's February 2026 Patch Tuesday reveals a critical security landscape with six actively exploited zero-day vulnerabilities being leveraged by attackers in the wild. Concurrently, threat actors are deploying sophisticated attack campaigns including the SSHStalker botnet targeting Linux systems through legacy kernel exploits, North Korean groups using AI-generated lures for cryptocurrency theft, and the emergence of Reynolds ransomware employing BYOVD techniques to disable security tools. The exploitation activity spans multiple platforms and demonstrates an escalation in both sophistication and targeting precision across Windows, Linux, and macOS environments.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities across Microsoft's software ecosystem, with three specifically identified as security feature bypass flaws
- **Impact**: Attackers can circumvent built-in security protections in multiple Microsoft products, enabling unauthorized access and privilege escalation
- **Status**: Actively exploited in the wild; patches released in February 2026 Patch Tuesday update

### SSHStalker Botnet Linux Exploits
- **Description**: Linux botnet operation exploiting legacy kernel vulnerabilities to compromise systems
- **Impact**: Complete system compromise allowing attackers to establish persistence and use IRC-based command-and-control infrastructure
- **Status**: Active exploitation targeting Linux systems with outdated kernels

### Fortinet FortiClientEMS SQL Injection
- **Description**: Critical SQL injection vulnerability enabling unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Recently patched by Fortinet; exploitation potential remains high for unpatched systems
- **CVE ID**: CVE-2026 (specific number referenced but not fully disclosed in articles)

## Affected Systems and Products

- **Microsoft Windows**: All versions affected by six zero-day vulnerabilities, including Windows 10 and Windows 11 systems
- **Microsoft 365**: Various components affected by security feature bypass vulnerabilities
- **Linux Systems**: Legacy kernel versions targeted by SSHStalker botnet operations
- **Fortinet FortiClientEMS**: Enterprise endpoint management systems vulnerable to SQL injection attacks
- **macOS and Windows**: Cryptocurrency sector targets of North Korean UNC1069 operations
- **SolarWinds Web Help Desk**: Publicly exposed instances becoming prime attack targets

## Attack Vectors and Techniques

- **IRC-Based Command and Control**: SSHStalker botnet uses Internet Relay Chat protocol for C2 communications, representing a return to legacy protocols
- **AI-Generated Social Engineering**: North Korean threat actors creating deepfake videos and AI-generated content to enhance phishing campaigns
- **ClickFix Technique**: Social engineering method used to trick users into executing malicious code
- **BYOVD (Bring Your Own Vulnerable Driver)**: Reynolds ransomware embeds vulnerable drivers to disable EDR security tools
- **Security Feature Bypass**: Three zero-days specifically designed to circumvent Microsoft's built-in security protections
- **Unauthenticated Remote Code Execution**: Critical Fortinet vulnerability allowing code execution without authentication

## Threat Actor Activities

- **UNC1069 (North Korean)**: Conducting sophisticated campaigns against cryptocurrency organizations using AI-generated lures and targeting both Windows and macOS systems
- **DPRK IT Workers**: Impersonating professionals on LinkedIn using real accounts to infiltrate companies and secure remote positions
- **SSHStalker Operators**: Deploying Linux botnet infrastructure targeting systems with legacy kernel vulnerabilities through SSH-based attacks
- **Reynolds Ransomware Group**: Emerging ransomware family incorporating advanced evasion techniques including BYOVD drivers for EDR bypass
- **Cryptocurrency-Focused Attackers**: Multiple threat groups specifically targeting the cryptocurrency sector with tailored malware and social engineering campaigns