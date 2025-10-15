# Exploitation Report

October 2025 has witnessed an unprecedented surge in exploitation activity, marked by Microsoft's largest Patch Tuesday release addressing 172 security vulnerabilities, including six zero-day exploits that are actively being leveraged by threat actors. The most significant developments include the Oracle E-Business Suite vulnerability CVE-2025-61884 being actively exploited with proof-of-concept code leaked by the ShinyHunters group, and Chinese state-sponsored actors from Flax Typhoon successfully weaponizing ArcGIS geo-mapping servers as persistent backdoors for over a year. Additionally, a new Android side-channel attack called Pixnapping demonstrates how malicious applications can steal two-factor authentication codes without requiring any permissions, while the RondoDox botnet has expanded its arsenal to exploit over 50 vulnerabilities across 30+ vendors.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities in Microsoft Windows operating systems that were unknown to Microsoft when they were being exploited
- **Impact**: Attackers can achieve various levels of system compromise depending on the specific vulnerability, including privilege escalation and remote code execution
- **Status**: Actively exploited in the wild; patches released in October 2025 Patch Tuesday update

### Oracle E-Business Suite Vulnerability
- **Description**: A critical vulnerability in Oracle E-Business Suite that was being actively exploited to breach servers before Oracle silently patched it
- **Impact**: Allows attackers to compromise Oracle E-Business Suite servers and gain unauthorized access
- **Status**: Actively exploited; proof-of-concept exploit publicly leaked by ShinyHunters; Oracle has released a silent fix
- **CVE ID**: CVE-2025-61884

### ArcGIS Server Backdoor Exploitation
- **Description**: Chinese threat actors compromised ArcGIS geo-mapping servers and modified the widely used geospatial mapping software to create persistent backdoor access
- **Impact**: Long-term persistent access to target networks for espionage and data exfiltration activities
- **Status**: Active campaign running for over a year; used by Chinese state-sponsored Flax Typhoon group

## Affected Systems and Products

- **Microsoft Windows Operating Systems**: All supported versions affected by 172 security vulnerabilities including 6 zero-days
- **Oracle E-Business Suite**: Servers vulnerable to active exploitation before silent patching
- **ArcGIS Server**: Geo-mapping software compromised and weaponized as backdoor by Chinese actors
- **Android Devices**: Google and Samsung devices vulnerable to Pixnapping side-channel attacks
- **VSCode Extensions**: Malicious extensions targeting developers on Microsoft VSCode marketplace and OpenVSX registry
- **Framework Linux Laptops**: Nearly 200,000 systems with Secure Boot bypass vulnerability
- **Windows 10**: End-of-life systems no longer receiving security updates
- **Exchange Server 2016 and 2019**: End-of-support systems vulnerable to unpatched exploits
- **Developer Package Repositories**: npm, PyPI, and RubyGems packages containing malicious code

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Six Microsoft zero-days actively exploited before patches were available
- **Supply Chain Attacks**: Malicious packages distributed through npm, PyPI, and RubyGems repositories
- **Side-Channel Attacks**: Pixnapping technique stealing sensitive data pixel-by-pixel from Android applications
- **Web Shell Deployment**: Chinese actors using ArcGIS components as persistent backdoors
- **Extension Marketplace Abuse**: TigerJack threat actor distributing crypto-stealing VSCode extensions
- **Botnet Operations**: RondoDox botnet weaponizing 50+ vulnerabilities across 30+ vendors
- **Social Engineering**: TA585 group using phishing campaigns to deliver MonsterV2 malware
- **Discord C2 Channels**: Malicious packages using Discord as command-and-control infrastructure

## Threat Actor Activities

- **Flax Typhoon (Chinese APT)**: Compromised ArcGIS servers for year-long persistent access campaigns targeting geospatial intelligence
- **ShinyHunters**: Leaked proof-of-concept exploit for Oracle E-Business Suite vulnerability, forcing Oracle to silently patch
- **TigerJack**: Continuously targeting developers with malicious VSCode extensions designed to steal cryptocurrency wallets
- **TA585**: Previously undocumented threat actor delivering MonsterV2 malware through sophisticated phishing campaigns
- **RondoDox Operators**: Botnet operators expanding targeting to exploit over 50 vulnerabilities across multiple vendor products
- **Package Repository Attackers**: Multiple threat actors distributing malicious packages across npm, PyPI, and RubyGems ecosystems
- **Prince Group**: Criminal organization behind $15 billion cryptocurrency "pig butchering" schemes before U.S. seizure