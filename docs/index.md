# Exploitation Report

The current threat landscape reveals a surge in sophisticated zero-day exploitation and advanced persistent threat activities. Most critically, Microsoft has addressed six actively exploited zero-day vulnerabilities in their February 2026 Patch Tuesday release, while Apple has patched a zero-day flaw being exploited in "extremely sophisticated attacks" targeting specific individuals. The exploitation activity spans multiple platforms including enterprise mobile management systems, with 83% of Ivanti EPMM exploits traced to a single IP address on bulletproof hosting infrastructure. Additionally, several advanced threat actors are leveraging AI technologies and novel attack vectors, including North Korean groups targeting cryptocurrency organizations and ransomware operators abusing legitimate employee monitoring tools.

## Active Exploitation Details

### Apple Zero-Day Vulnerability
- **Description**: A zero-day vulnerability affecting iOS, iPadOS, macOS Tahoe, tvOS, watchOS, and visionOS systems
- **Impact**: Enables sophisticated cyber attacks targeting specific individuals
- **Status**: Actively exploited in the wild; patches released by Apple across all affected platforms

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities across Microsoft's software ecosystem
- **Impact**: Various attack vectors enabling system compromise and unauthorized access
- **Status**: Actively exploited in the wild; patches released in February 2026 Patch Tuesday update

### Ivanti EPMM Security Flaw
- **Description**: Newly disclosed security vulnerability in Ivanti Endpoint Manager Mobile (EPMM)
- **Impact**: Enables remote exploitation and system compromise
- **Status**: Active exploitation with 83% of attacks originating from single IP address on bulletproof hosting infrastructure

### Windows 11 Notepad Remote Code Execution
- **Description**: Vulnerability in Windows 11 Notepad allowing remote code execution via specially crafted Markdown links
- **Impact**: Attackers can execute local or remote programs by tricking users into clicking malicious Markdown links
- **Status**: Fixed by Microsoft in recent updates

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, macOS Tahoe, tvOS, watchOS, and visionOS across all supported versions
- **Microsoft Windows**: Windows 11 systems running Notepad with Markdown support
- **Ivanti EPMM**: Endpoint Manager Mobile installations exposed to internet
- **Microsoft Software**: 59 vulnerabilities across Microsoft's software portfolio including operating systems
- **Linux Systems**: Legacy kernel versions targeted by SSHStalker botnet operations
- **Cryptocurrency Organizations**: Windows and macOS systems in cryptocurrency sector

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unknown vulnerabilities in Apple and Microsoft systems
- **Bulletproof Hosting**: Centralized exploitation infrastructure for Ivanti EPMM attacks
- **Social Engineering with AI**: Use of AI-generated content and deepfakes for credential theft
- **ClickFix Technique**: Social engineering method used for malware delivery and MFA bypass
- **Supply Chain Attacks**: Hijacking of legitimate Microsoft Store Outlook add-ins
- **Markdown Link Exploitation**: Crafted Markdown links in Windows 11 Notepad for code execution
- **IRC Command and Control**: Legacy IRC protocol used by SSHStalker botnet for C2 communications
- **Employee Monitoring Tool Abuse**: Legitimate tools repurposed for persistence and evasion

## Threat Actor Activities

- **UNC1069 (North Korea)**: Targeting cryptocurrency organizations with AI-enhanced social engineering campaigns using deepfakes and legitimate platforms to steal sensitive data from Windows and macOS systems
- **APT36 and SideCopy**: Cross-platform RAT campaigns against Indian defense sector and government organizations, compromising both Windows and Linux environments
- **Crazy Ransomware Gang**: Abusing legitimate employee monitoring software and SimpleHelp remote support tools for network persistence and detection evasion
- **Green Blood Group**: Breached Senegal's national biometric database, stealing personal records and biometric data of nearly 20 million residents
- **SSHStalker Botnet Operators**: Deploying Linux botnet using IRC for command-and-control operations, targeting systems with legacy kernel exploits
- **Kimwolf Botnet**: Massive IoT botnet disrupting the I2P anonymity network infrastructure
- **Microsoft Store Supply Chain Attackers**: Compromised AgreeTo Outlook add-in to steal over 4,000 Microsoft account credentials