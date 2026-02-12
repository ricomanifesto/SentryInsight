# Exploitation Report

Microsoft has addressed a significant wave of active exploitation with its February 2026 Patch Tuesday, releasing fixes for 59 vulnerabilities including six actively exploited zero-day vulnerabilities. Three of these zero-days are security feature bypass flaws that enable attackers to circumvent built-in protections across multiple Microsoft products. Concurrently, multiple threat actors are leveraging sophisticated social engineering campaigns, with North Korean groups targeting cryptocurrency organizations through AI-generated lures and the ClickFix technique, while ransomware groups abuse legitimate remote monitoring tools to maintain persistent access in corporate networks.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities in Microsoft Windows and other software products that have been actively exploited in the wild
- **Impact**: Three are security feature bypass flaws allowing attackers to circumvent built-in security protections, with additional vulnerabilities providing various attack capabilities
- **Status**: Patches released in February 2026 Patch Tuesday update

### SSHStalker Linux Botnet Exploits
- **Description**: A new botnet operation targeting Linux systems using legacy kernel exploits to gain unauthorized access
- **Impact**: Complete system compromise allowing remote control through IRC command-and-control infrastructure
- **Status**: Active exploitation ongoing, using old-school IRC protocols for stealth

### JokerOTP MFA Bypass Tool
- **Description**: Phishing automation tool designed to intercept one-time passwords and bypass multi-factor authentication
- **Impact**: Account takeover through MFA circumvention, enabling unauthorized access to protected accounts
- **Status**: Tool seller arrested by Netherlands Police, but tool may still be in circulation

## Affected Systems and Products

- **Microsoft Windows**: All supported versions affected by six zero-day vulnerabilities
- **Microsoft Software Suite**: Various Microsoft products impacted by security feature bypass vulnerabilities
- **Linux Systems**: Targeted by SSHStalker botnet through legacy kernel exploits
- **macOS Systems**: Targeted by North Korean threat actors with new malware variants
- **Employee Monitoring Software**: Abused by Crazy ransomware gang for persistence
- **SimpleHelp Remote Support Tool**: Leveraged by ransomware operators for network access
- **Cryptocurrency Platforms**: Primary targets for North Korean UNC1069 operations
- **I2P Anonymity Network**: Disrupted by Kimwolf IoT botnet operations
- **7-Zip Distribution**: Fake websites distributing trojanized installers
- **SolarWinds Web Help Desk**: Exposed instances targeted by attackers

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Used to deliver CastleLoader malware leading to LummaStealer infections
- **AI-Generated Video Lures**: North Korean actors using sophisticated deepfake content to target cryptocurrency sector
- **LinkedIn Impersonation**: DPRK operatives using real LinkedIn profiles to infiltrate companies for remote IT positions
- **IRC Command-and-Control**: SSHStalker botnet using traditional IRC protocols to evade modern detection systems
- **Legitimate Tool Abuse**: Ransomware groups leveraging employee monitoring and remote support tools for stealth
- **Fake Software Distribution**: Malicious websites distributing trojanized versions of popular software like 7-Zip
- **MFA Bypass Automation**: JokerOTP tool automating the interception of one-time passwords
- **Cross-Platform RAT Deployment**: APT36 and SideCopy targeting both Windows and Linux environments simultaneously

## Threat Actor Activities

- **Crazy Ransomware Gang**: Abusing legitimate employee monitoring software and SimpleHelp tools to maintain persistence in corporate networks while evading detection
- **North Korean UNC1069**: Conducting sophisticated campaigns against cryptocurrency organizations using AI-generated video content and targeting both Windows and macOS systems for data theft
- **SSHStalker Operators**: Managing a new Linux-focused botnet using IRC communication protocols to control compromised systems
- **APT36 and SideCopy**: Launching coordinated cross-platform remote access trojan campaigns specifically targeting Indian defense sector and government-aligned organizations
- **Kimwolf Botnet Controllers**: Operating a massive IoT botnet that has been disrupting the I2P anonymity network infrastructure
- **JokerOTP Distributor**: Selling access to MFA bypass tools before arrest by Netherlands authorities
- **DPRK IT Worker Network**: Using impersonated LinkedIn profiles of real professionals to gain remote employment and infiltrate target organizations