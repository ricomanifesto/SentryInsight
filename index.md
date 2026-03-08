# Exploitation Report

The cybersecurity landscape is experiencing a significant surge in sophisticated exploitation activity across multiple domains. Key developments include the active exploitation of iOS security flaws through the Coruna exploit kit for cyberespionage and crypto-theft attacks, prompting CISA to issue urgent patching orders for federal agencies. Google's Threat Intelligence Group has tracked 90 zero-day vulnerabilities exploited in attacks during 2025, with nearly half targeting enterprise software and appliances. Critical vulnerabilities in VMware Aria Operations are being actively exploited through command injection attacks, potentially granting attackers broad access to cloud environments. Additionally, a critical WordPress membership plugin vulnerability affecting over 60,000 sites is being exploited to create unauthorized admin accounts, while Cisco has patched 48 new firewall vulnerabilities, including two critical flaws with perfect 10.0 CVSS scores.

## Active Exploitation Details

### iOS Security Flaws via Coruna Exploit Kit
- **Description**: Three iOS security vulnerabilities being exploited through the Coruna exploit kit
- **Impact**: Cyberespionage operations and cryptocurrency theft attacks
- **Status**: CISA has ordered federal agencies to patch these actively exploited flaws

### VMware Aria Operations Command Injection Vulnerability
- **Description**: Command injection flaw in VMware Aria Operations cloud management platform
- **Impact**: Attackers can gain broad access to victims' cloud environments and resources
- **Status**: Currently being exploited in active attacks

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in WordPress membership plugin installed on over 60,000 sites
- **Impact**: Allows hackers to create unauthorized administrator accounts
- **Status**: Actively being exploited by attackers

### Zero-Day Vulnerabilities Tracked by Google
- **Description**: 90 zero-day vulnerabilities identified as actively exploited throughout 2025
- **Impact**: Nearly half target enterprise software and appliances, enabling various attack scenarios
- **Status**: Ongoing exploitation across multiple platforms and vendors

## Affected Systems and Products

- **Apple iOS Devices**: Multiple iOS versions affected by three security flaws exploited via Coruna kit
- **VMware Aria Operations**: Cloud management platform vulnerable to command injection attacks
- **WordPress Sites**: Over 60,000 sites using User Registration & Membership plugin at risk
- **Cisco Firewall Products**: 48 vulnerabilities patched, including two critical flaws with CVSS 10.0 scores
- **Enterprise Software**: Broad category representing nearly half of the 90 zero-days tracked by Google
- **Network Appliances**: Infrastructure devices targeted in zero-day exploitation campaigns

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Velvet Tempest ransomware group using ClickFix technique with legitimate Windows utilities
- **InstallFix Attacks**: New variation of ClickFix targeting fake Claude Code installations to deploy infostealers
- **Command Injection**: Direct exploitation of VMware Aria Operations for cloud environment access
- **Plugin Exploitation**: Direct attacks on WordPress membership plugin to escalate privileges
- **AI-Enhanced Attacks**: Threat actors leveraging artificial intelligence across all stages of cyberattacks
- **Phishing Campaigns**: Traditional social engineering enhanced with AI tools for improved effectiveness

## Threat Actor Activities

- **Velvet Tempest**: Deploying Termite ransomware through ClickFix techniques and CastleRAT backdoor operations
- **Chinese APT UAT-9244**: Targeting South American telecommunications providers with new malware toolkit since 2024
- **China's Silver Dragon**: APT41-nexus group conducting cyber espionage against EU and Southeast Asian governments
- **Pakistani APT36**: Using AI-powered "vibe-coding" to mass-produce malware at unprecedented scale
- **Indian APT Sloppy Lemming**: Targeting defense and critical infrastructure with custom Rust-based tools
- **North Korean APTs**: Enhancing IT worker scams with AI tools including face swapping and automated communications
- **Nation-State Actors**: Broadly leveraging AI for malware development and attack acceleration across multiple campaigns