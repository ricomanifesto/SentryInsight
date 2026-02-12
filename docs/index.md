# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple platforms, with Microsoft addressing six actively exploited zero-day vulnerabilities in their February 2026 Patch Tuesday release. Concurrently, Apple has patched a zero-day flaw that was leveraged in highly sophisticated targeted attacks against specific individuals. The exploitation landscape is further complicated by supply chain attacks targeting Microsoft Outlook add-ins, sophisticated North Korean campaigns against cryptocurrency organizations using AI-generated content, and emerging botnet operations targeting Linux systems with legacy kernel exploits.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities across Microsoft products that have been actively exploited in the wild, including three security feature bypass flaws
- **Impact**: Attackers can bypass built-in security protections in multiple Microsoft products, potentially leading to unauthorized access and system compromise
- **Status**: Patched in Microsoft's February 2026 Patch Tuesday release addressing 58 total flaws

### Apple Zero-Day Vulnerability
- **Description**: A zero-day vulnerability exploited in extremely sophisticated attacks targeting specific individuals
- **Impact**: Enables attackers to compromise Apple devices through highly targeted exploitation
- **Status**: Patched by Apple with security updates released to address the vulnerability

### Windows 11 Notepad Remote Code Execution
- **Description**: A remote code execution vulnerability in Windows 11 Notepad that allows attackers to execute local or remote programs through specially crafted Markdown links
- **Impact**: Attackers can achieve code execution by tricking users into clicking malicious Markdown links
- **Status**: Fixed by Microsoft

### SSHStalker Botnet Kernel Exploits
- **Description**: New botnet operation targeting Linux systems using legacy kernel exploits for initial access
- **Impact**: Compromised Linux systems are incorporated into a botnet controlled via IRC protocol
- **Status**: Active exploitation ongoing against vulnerable Linux systems

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by zero-day vulnerabilities and Notepad flaw
- **Microsoft Outlook**: Outlook add-ins compromised in supply chain attacks affecting over 4,000 accounts
- **Apple Devices**: Unspecified Apple products targeted in sophisticated zero-day attacks
- **Linux Systems**: Various Linux distributions vulnerable to legacy kernel exploits used by SSHStalker botnet
- **SolarWinds Web Help Desk**: Instances exposed to public internet becoming prime targets for attacks
- **Cryptocurrency Platforms**: Windows and macOS systems in cryptocurrency organizations targeted by North Korean actors

## Attack Vectors and Techniques

- **ClickFix Technique**: Social engineering method used to deliver malware through fake error messages and prompts
- **Supply Chain Attacks**: Compromised legitimate software add-ins and installers to distribute malware
- **AI-Generated Content**: Use of deepfakes and AI-generated videos for social engineering in cryptocurrency targeting
- **Markdown Link Exploitation**: Crafted Markdown links in Notepad to achieve remote code execution
- **IRC Command and Control**: Traditional IRC protocol used for botnet communication and control
- **Phishing Automation**: Tools like JokerOTP used to intercept multi-factor authentication codes
- **Legitimate Tool Abuse**: Employee monitoring software and remote support tools used for persistence

## Threat Actor Activities

- **UNC1069 (North Korea-linked)**: Targeting cryptocurrency organizations with AI-generated lures, deepfakes, and custom malware for both Windows and macOS systems
- **APT36**: Cross-platform campaigns against Indian defense sector and government organizations using remote access trojans
- **SideCopy**: Coordinated attacks alongside APT36 targeting Indian entities with multi-platform malware
- **Crazy Ransomware Gang**: Abusing legitimate employee monitoring tools and SimpleHelp remote support software for persistence and evasion
- **SSHStalker Operators**: New botnet campaign targeting Linux systems with IRC-based command and control infrastructure
- **Microsoft Outlook Add-in Attackers**: Supply chain compromise of AgreeTo add-in resulting in theft of over 4,000 Microsoft account credentials
- **LummaStealer Campaigns**: Surge in infections driven by CastleLoader malware distribution using ClickFix social engineering techniques