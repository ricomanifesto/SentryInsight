# Exploitation Report

Critical zero-day vulnerabilities are dominating the threat landscape with Microsoft addressing six zero-day vulnerabilities in their October 2025 Patch Tuesday, including active exploitation of Internet Explorer mode in Edge browsers. Oracle has silently patched CVE-2025-61884, an actively exploited vulnerability in Oracle E-Business Suite that was publicly leaked by ShinyHunters. Chinese state-sponsored actors are demonstrating sophisticated persistence techniques by weaponizing ArcGIS Server components as backdoors for over a year. Additionally, the RondoDox botnet has expanded its capabilities to exploit over 50 vulnerabilities across 30+ vendors, while threat actors are leveraging zero-day exploits in the Chakra JavaScript engine to compromise systems through Edge's Internet Explorer compatibility mode.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities patched in Microsoft's October 2025 Patch Tuesday update, part of 172 total security fixes
- **Impact**: Active exploitation allows attackers to compromise Windows systems and applications
- **Status**: Patches available in October 2025 security updates

### Oracle E-Business Suite Zero-Day
- **Description**: Critical vulnerability in Oracle E-Business Suite that was actively exploited by threat actors
- **Impact**: Attackers can breach Oracle servers and gain unauthorized access to business systems
- **Status**: Silently patched by Oracle after public exploit leak by ShinyHunters
- **CVE ID**: CVE-2025-61884

### Internet Explorer Mode Zero-Day Exploits
- **Description**: Zero-day exploits targeting the Chakra JavaScript engine in Edge's Internet Explorer compatibility mode
- **Impact**: Attackers can gain access to target devices through legacy browser functionality
- **Status**: Microsoft has restricted access to IE mode after receiving credible reports in August 2025

### ArcGIS Server Backdoor Exploitation
- **Description**: Chinese hackers compromised ArcGIS geo-mapping systems and converted components into persistent web shells
- **Impact**: Long-term persistence in target environments, allowing sustained access to critical infrastructure
- **Status**: Active campaign lasting over one year with undetected presence

### RondoDox Botnet Multi-Vendor Exploitation
- **Description**: Botnet campaign exploiting over 50 vulnerabilities across 30+ different vendors
- **Impact**: Mass compromise of systems through diverse attack vectors, described as an "exploit shop"
- **Status**: Active and expanding targeting capabilities

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 (end of support), Windows 11 versions 25H2/24H2 and 23H2
- **Microsoft Edge**: Internet Explorer mode functionality specifically targeted
- **Oracle E-Business Suite**: Servers running vulnerable versions prior to silent patch
- **ArcGIS Server**: Geo-mapping and GIS systems used by organizations
- **Framework Laptops**: Nearly 200,000 Linux Framework systems with Secure Boot bypass risk
- **Android Devices**: Google and Samsung devices vulnerable to Pixnapping attack
- **SonicWall SSLVPN**: Over 100 compromised accounts using stolen credentials
- **Remote Desktop Protocol**: RDP services across the United States targeted by massive botnet
- **Package Repositories**: npm, PyPI, and RubyGems ecosystems with malicious packages

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities in Microsoft products and Oracle systems
- **Web Shell Deployment**: Converting legitimate ArcGIS components into persistent backdoors
- **Credential Stuffing**: Large-scale attacks against SonicWall VPN using stolen valid credentials
- **Supply Chain Attacks**: Malicious packages in software repositories using Discord for command and control
- **Side-Channel Attacks**: Pixnapping technique to steal 2FA codes without requiring permissions
- **Botnet Operations**: Multi-country coordination targeting RDP services from 100,000+ IP addresses
- **Legacy System Abuse**: Exploiting Internet Explorer mode compatibility features in modern browsers
- **Secure Boot Bypass**: Exploitation of signed UEFI shell components on Framework laptops

## Threat Actor Activities

- **Chinese State-Sponsored Groups**: Long-term persistence campaigns using ArcGIS servers as backdoors, maintaining access for over one year in target environments
- **ShinyHunters**: Public leak of Oracle E-Business Suite zero-day exploit, forcing vendor to issue silent patch
- **TA585**: Previously undocumented threat actor delivering MonsterV2 malware through phishing campaigns
- **RondoDox Operators**: Botnet campaign expanding to weaponize vulnerabilities across multiple vendor ecosystems
- **Multi-Country Botnet**: Large-scale RDP targeting operation coordinating attacks from over 100,000 IP addresses globally
- **Package Repository Attackers**: Cybercriminals distributing malicious packages across npm, Python, and Ruby ecosystems using Discord for data exfiltration
- **Astaroth Banking Trojan Groups**: Leveraging GitHub infrastructure to maintain operational resilience after takedowns