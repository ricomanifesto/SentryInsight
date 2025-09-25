# Exploitation Report

Critical exploitation activity is currently targeting multiple sectors through diverse attack vectors. Most notably, Cisco has disclosed active exploitation of a zero-day SNMP vulnerability (CVE-2024-20567) in IOS and IOS XE Software that allows remote code execution or denial-of-service attacks. Additionally, CISA reports that attackers successfully breached a federal agency by exploiting a critical GeoServer vulnerability (CVE-2024-36401) within two weeks of its disclosure. Threat actors are also leveraging sophisticated malware campaigns including financially motivated groups distributing fake browser updates, North Korean hackers deploying new backdoors targeting cryptocurrency developers, and Chinese espionage groups conducting long-term persistence operations against U.S. organizations.

## Active Exploitation Details

### Cisco IOS SNMP Vulnerability
- **Description**: High-severity vulnerability in Simple Network Management Protocol (SNMP) implementation affecting Cisco IOS Software and IOS XE Software
- **Impact**: Allows remote attackers to execute arbitrary code or trigger denial-of-service conditions on affected network devices
- **Status**: Actively exploited zero-day vulnerability; Cisco has released security updates
- **CVE ID**: CVE-2024-20567

### GeoServer Critical Vulnerability
- **Description**: Critical vulnerability in GeoServer geospatial software platform
- **Impact**: Enabled attackers to breach a large federal civilian executive branch (FCEB) agency
- **Status**: Exploited less than two weeks after initial disclosure; used in successful federal agency compromise
- **CVE ID**: CVE-2024-36401

## Affected Systems and Products

- **Cisco IOS Software**: Network devices running affected versions of IOS and IOS XE Software with SNMP enabled
- **GeoServer**: Geospatial data servers used by federal agencies and organizations
- **Supermicro Hardware**: Baseboard Management Controller (BMC) firmware vulnerabilities allowing persistent backdoor creation
- **OnePlus Devices**: Multiple OxygenOS versions allowing unauthorized SMS data access
- **Wondershare RepairIt**: Software vulnerabilities exposing user data and AI models
- **Rust Development Environment**: Malicious crates targeting Solana and Ethereum wallet keys
- **Windows 10 Systems**: End-of-life systems requiring extended security updates

## Attack Vectors and Techniques

- **Drive-by Downloads**: UNC2165 and UNC5518 groups using FAKEUPDATES and FAKETREFF campaigns with SEO poisoning
- **Social Engineering**: FIN6 using legitimate job postings on LinkedIn and Indeed to distribute BULLZLINK and SQUIDSLEEP payloads
- **ClickFix Technique**: UNC5518 employing fake error messages to trick users into downloading malicious JavaScript
- **Supply Chain Attacks**: Malicious Rust crates impersonating legitimate fast_log library to steal cryptocurrency keys
- **BMC Exploitation**: Attackers using firmware vulnerabilities to create persistent backdoors in server hardware
- **Phishing Campaigns**: Fake PyPI websites targeting Python developers' credentials

## Threat Actor Activities

- **UNC2165**: Financially motivated group resuming operations after dormancy, leveraging UNC1543 distribution channels with COLORFAKE.V2 dropper and MYTHIC payloads
- **UNC5518**: Distributing FAKETREFF JavaScript downloader since April 2024, evolving techniques with obfuscation and multi-stage scripts
- **FIN6**: Targeting corporate recruiters through spoofed personal websites since December 2022, distributing BULLZLINK and SQUIDSLEEP payloads
- **North Korean Groups**: Using new AkdoorTea backdoor in Contagious Interview campaign targeting global cryptocurrency developers with TsunamiKit tools
- **RedNovember (Chinese APT)**: Conducting espionage operations against global governments using Pantegana and Cobalt Strike tools
- **UNC5221 (Chinese-nexus)**: Using BRICKSTORM backdoor for over a year targeting U.S. legal services, SaaS providers, and technology sectors
- **RTX Ransomware Group**: Causing widespread European airport disruptions leading to UK arrest of suspect
- **Scattered Spider**: Teen member surrenders amid group's claimed shutdown following 2023 Vegas casino attacks