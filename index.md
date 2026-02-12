# Exploitation Report

Microsoft's February 2026 Patch Tuesday revealed critical security concerns with six actively exploited zero-day vulnerabilities being patched, representing one of the most significant exploitation events in recent memory. Simultaneously, threat actors continue to leverage sophisticated techniques including AI-generated content, supply chain attacks, and malicious browser add-ins to compromise systems. Notable activities include North Korean UNC1069 targeting cryptocurrency firms with AI-powered lures, the discovery of the first known malicious Microsoft Outlook add-in stealing over 4,000 credentials, and multiple botnet operations including SSHStalker targeting Linux systems and Kimwolf disrupting the I2P network.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities (February 2026 Patch Tuesday)
- **Description**: Six zero-day vulnerabilities were actively exploited in the wild before Microsoft's February 2026 security updates
- **Impact**: Three are security feature bypass flaws allowing attackers to circumvent built-in protections in multiple Microsoft products
- **Status**: Patches released as part of 59 total security fixes in February 2026 Patch Tuesday

### Windows 11 Notepad Remote Code Execution Vulnerability
- **Description**: Vulnerability in Windows 11 Notepad allowing remote code execution through specially crafted Markdown links
- **Impact**: Attackers can execute local or remote programs by tricking users into clicking malicious Markdown links
- **Status**: Fixed by Microsoft

### Legacy Linux Kernel Exploits
- **Description**: Older kernel vulnerabilities being exploited by the SSHStalker botnet
- **Impact**: Complete system compromise and botnet enrollment of Linux systems
- **Status**: Actively exploited by cybercriminals

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by zero-days and Notepad vulnerability
- **Microsoft Outlook**: AgreeTo add-in compromised to steal credentials from 4,000+ accounts
- **Linux Systems**: Various distributions vulnerable to legacy kernel exploits used by SSHStalker botnet
- **macOS**: Targeted by North Korean threat actors with new malware variants
- **7-Zip**: Fake distribution sites serving trojanized installers
- **SolarWinds Web Help Desk**: Public-facing instances targeted for compromise
- **I2P Network**: Anonymity network disrupted by Kimwolf botnet activities

## Attack Vectors and Techniques

- **ClickFix Technique**: Social engineering method used by multiple threat actors to deliver malware through fake browser error messages
- **AI-Generated Content**: UNC1069 using large language models and deepfakes to create convincing social engineering lures
- **Supply Chain Attacks**: Hijacking legitimate software distribution channels and browser add-ins
- **Markdown Link Exploitation**: Leveraging Windows 11 Notepad vulnerability through crafted Markdown files
- **IRC Command-and-Control**: SSHStalker botnet using old-school IRC protocols for C2 communications
- **Employee Monitoring Software Abuse**: Crazy ransomware gang leveraging legitimate remote monitoring tools
- **Residential Proxy Networks**: Converting compromised systems into proxy nodes for malicious activities

## Threat Actor Activities

- **UNC1069 (North Korea)**: Targeting cryptocurrency organizations with AI-powered social engineering campaigns, deploying malware for both Windows and macOS systems
- **APT36 and SideCopy**: Launching cross-platform RAT campaigns against Indian defense and government entities
- **Crazy Ransomware Gang**: Abusing SimpleHelp remote support tools and employee monitoring software for persistence and evasion
- **SSHStalker Operators**: Operating Linux botnet using IRC for command-and-control communications
- **Kimwolf Botnet**: Massive IoT botnet disrupting I2P anonymity network infrastructure
- **JokerOTP Operators**: Providing MFA bypass services through phishing automation tools (operator arrested)
- **CastleLoader Campaigns**: Driving surge in LummaStealer infections through social engineering