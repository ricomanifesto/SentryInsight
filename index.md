# Exploitation Report

Critical exploitation activity continues to emerge across multiple platforms, with several significant zero-day vulnerabilities being actively exploited in the wild. Microsoft addressed six zero-day vulnerabilities in their October 2025 Patch Tuesday update, while Oracle silently patched a zero-day exploit (CVE-2025-61884) that was actively used to breach servers and had its proof-of-concept publicly leaked by the ShinyHunters group. Chinese state-sponsored hackers have demonstrated sophisticated persistence techniques by weaponizing ArcGIS geo-mapping tools as backdoors for over a year, while a new Android side-channel attack called "Pixnapping" enables malicious apps to steal sensitive data including 2FA codes without requiring any permissions. Microsoft has also restricted Internet Explorer mode in Edge browser after receiving credible reports of hackers exploiting zero-day vulnerabilities in the Chakra JavaScript engine.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities identified and patched in Microsoft's October 2025 Patch Tuesday update
- **Impact**: Active exploitation allowing attackers to compromise systems before patches were available
- **Status**: Patches available as of October 2025 Patch Tuesday release

### Oracle E-Business Suite Zero-Day
- **Description**: Vulnerability in Oracle E-Business Suite that was actively exploited to breach servers
- **Impact**: Server compromise and unauthorized access to Oracle E-Business Suite systems
- **Status**: Silently patched by Oracle after active exploitation was discovered
- **CVE ID**: CVE-2025-61884

### Internet Explorer Mode Zero-Days
- **Description**: Zero-day exploits targeting the Chakra JavaScript engine in Internet Explorer mode within Microsoft Edge browser
- **Impact**: Remote code execution and system compromise through legacy browser functionality
- **Status**: Microsoft has restricted access to IE mode after receiving credible exploitation reports

### ArcGIS Server Backdoor Exploitation
- **Description**: Chinese threat actors exploited ArcGIS geo-mapping systems to establish persistent backdoors
- **Impact**: Long-term persistence and continued access to compromised infrastructure for over a year
- **Status**: Ongoing campaign with established backdoors in target environments

### Pixnapping Side-Channel Attack
- **Description**: Novel Android side-channel attack that steals sensitive data by capturing pixels from other applications
- **Impact**: Theft of 2FA codes, Google Maps data, and sensitive information from Gmail, Google Authenticator, Signal, and Venmo without requiring app permissions
- **Status**: Proof-of-concept demonstrated; affects Android devices from Google and Samsung

### RMPocalypse AMD Vulnerability
- **Description**: Security flaw affecting AMD's SEV-SNP confidential computing that can be exploited with a single 8-byte write
- **Impact**: Undermines confidential computing guarantees and security protections
- **Status**: Patches released by AMD to address the vulnerability

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 (final patch released), Windows 11, and Microsoft Edge IE mode functionality
- **Oracle E-Business Suite**: Systems vulnerable to server compromise through the patched zero-day
- **Android Devices**: Google and Samsung Android devices vulnerable to Pixnapping attacks
- **ArcGIS Server**: Geo-mapping systems used as backdoors by Chinese threat actors
- **AMD Processors**: Systems using AMD SEV-SNP confidential computing affected by RMPocalypse
- **Framework Laptops**: Nearly 200,000 Linux Framework systems with Secure Boot bypass risks
- **Package Repositories**: npm, PyPI, and RubyGems ecosystems containing malicious packages

## Attack Vectors and Techniques

- **Side-Channel Attacks**: Pixnapping technique steals data by capturing screen pixels without requiring permissions
- **Web Shell Deployment**: Chinese actors converted ArcGIS components into persistent web shells for backdoor access
- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Microsoft and Oracle products
- **Supply Chain Attacks**: Malicious packages in software repositories using Discord as command-and-control infrastructure
- **Legacy System Abuse**: Exploitation of Internet Explorer mode functionality as an attack vector
- **Social Engineering**: TA585 threat actor using phishing campaigns to deliver MonsterV2 malware
- **Infrastructure Abuse**: GitHub and Discord platforms used for malware command-and-control operations

## Threat Actor Activities

- **Chinese State Actors**: Demonstrated year-long persistence through ArcGIS server compromise, establishing sophisticated backdoor access to target infrastructure
- **ShinyHunters Group**: Publicly leaked proof-of-concept exploit for Oracle E-Business Suite zero-day vulnerability
- **TA585 Threat Actor**: Conducting phishing campaigns to deliver MonsterV2 off-the-shelf malware to targets
- **RondoDox Botnet Operators**: Expanded targeting to exploit over 50 vulnerabilities across more than 30 vendors in an "exploit shop" approach
- **Prince Group**: Cryptocurrency fraud operation that stole billions through "pig butchering" schemes, resulting in $15 billion seizure by U.S. authorities
- **Astaroth Banking Trojan**: Operators using GitHub as infrastructure backbone to maintain resilience after takedowns
- **ChaosBot Operators**: Deploying new Rust-based backdoor using Discord channels for command and control