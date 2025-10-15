# Exploitation Report

Critical exploitation activity continues to surge with Microsoft's October 2025 Patch Tuesday addressing six zero-day vulnerabilities, including two Windows zero-days that have been actively exploited in the wild. One of these affects every Windows version ever shipped. Concurrent threats include active exploitation of ICTBroadcast servers through cookie-based attacks, F5 BIG-IP vulnerabilities stolen by nation-state actors, and Oracle E-Business Suite systems compromised through a zero-day exploit publicly leaked by ShinyHunters. The threat landscape is further complicated by new attack techniques like Pixnapping against Android devices and Chinese APT groups maintaining persistent backdoors in ArcGIS servers for over a year.

## Active Exploitation Details

### Windows Zero-Day Vulnerabilities
- **Description**: Two critical zero-day vulnerabilities affecting Windows systems, with one impacting every version of Windows ever released
- **Impact**: Attackers can achieve code execution and system compromise across all Windows environments
- **Status**: Actively exploited in the wild; patches released in October 2025 Patch Tuesday update

### ICTBroadcast Cookie Exploitation
- **Description**: Critical security flaw in ICTBroadcast autodialer software from ICT Innovations being actively exploited through cookie manipulation
- **Impact**: Attackers gain remote shell access to compromised servers
- **Status**: Under active exploitation in the wild

### Oracle E-Business Suite Zero-Day
- **Description**: Zero-day vulnerability in Oracle E-Business Suite systems that was silently patched after public exploit disclosure
- **Impact**: Server compromise and unauthorized system access
- **Status**: Previously exploited; exploit was publicly leaked by ShinyHunters group
- **CVE ID**: CVE-2025-61884

### F5 BIG-IP Vulnerabilities
- **Description**: Multiple undisclosed security vulnerabilities in F5 BIG-IP systems stolen by nation-state hackers during breach
- **Impact**: Potential for widespread exploitation of BIG-IP infrastructure once vulnerabilities are reverse-engineered
- **Status**: Vulnerabilities and source code stolen; disclosure timeline unknown

## Affected Systems and Products

- **Microsoft Windows**: All versions ever shipped affected by one zero-day; widespread impact across enterprise environments
- **ICTBroadcast**: Autodialer software servers vulnerable to cookie-based remote access attacks
- **Oracle E-Business Suite**: Enterprise applications vulnerable to authenticated exploitation
- **F5 BIG-IP**: Network infrastructure devices with stolen vulnerability details and source code
- **Red Lion Sixnet RTUs**: Industrial control systems with two CVSS 10.0 vulnerabilities enabling full system takeover
- **SAP NetWeaver AS Java**: Enterprise systems vulnerable to unauthenticated command execution
- **Android Devices**: Google and Samsung devices vulnerable to Pixnapping side-channel attacks
- **ArcGIS Servers**: Geospatial mapping systems compromised and used as persistent backdoors

## Attack Vectors and Techniques

- **Cookie Manipulation**: Exploitation of ICTBroadcast systems through malicious cookie injection for remote shell access
- **Zero-Day Exploitation**: Direct targeting of unpatched Windows and Oracle systems using publicly available exploits
- **Supply Chain Attacks**: Malicious VSCode extensions targeting developers through cryptocurrency theft capabilities
- **Pixnapping Attack**: Novel side-channel technique stealing 2FA codes and sensitive data pixel-by-pixel from Android applications
- **Backdoor Implantation**: Long-term persistence achieved through modification of legitimate ArcGIS server software
- **Phishing Campaigns**: TA585 threat actor delivering MonsterV2 malware through targeted email attacks
- **Package Repository Poisoning**: Malicious packages in npm, PyPI, and RubyGems ecosystems using Discord for command and control

## Threat Actor Activities

- **Nation-State Hackers**: Successfully breached F5 systems to steal undisclosed BIG-IP vulnerabilities and proprietary source code
- **Flax Typhoon (Chinese APT)**: Maintained persistent access to ArcGIS servers for over one year, using geospatial mapping software as backdoor infrastructure
- **ShinyHunters**: Publicly leaked Oracle E-Business Suite zero-day exploit, forcing emergency patching response
- **TigerJack**: Continuously targeting software developers through malicious VSCode extensions designed to steal cryptocurrency assets
- **TA585**: Previously undocumented threat actor conducting phishing campaigns to distribute MonsterV2 off-the-shelf malware
- **Prince Group**: Criminal organization responsible for multi-billion dollar cryptocurrency theft through "pig butchering" scams, with $15 billion in bitcoin seized by U.S. authorities