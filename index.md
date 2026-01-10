# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited by sophisticated threat actors, with Chinese-linked hackers leveraging VMware ESXi zero-days for virtual machine escape and a maximum severity flaw in HPE OneView (CVE-2025-37164) enabling remote code execution. State-sponsored groups are intensifying campaigns, with Russian APT28 conducting credential harvesting operations, Iranian MuddyWater deploying Rust-based RATs, and North Korean actors using malicious QR codes in spear-phishing. Additionally, cybercriminals are exploiting misconfigured proxy servers to access premium AI services, while botnets like Kimwolf have compromised over two million Android TV devices. The threat landscape also includes a critical remote code execution vulnerability in Trend Micro's Apex Central platform and widespread fraud operations by the Black Axe criminal organization.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Zero-day vulnerabilities in VMware ESXi platform being exploited by Chinese-speaking threat actors to escape virtual machines
- **Impact**: Enables attackers to break out of virtual machine isolation and gain access to underlying hypervisor infrastructure
- **Status**: Actively exploited in the wild, exploit may have been developed as far back as previous years

### HPE OneView Remote Code Execution Flaw
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Enables remote code execution, leading to devastating consequences for enterprise infrastructure
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central RCE Vulnerability
- **Description**: Critical security flaw in on-premise Apex Central for Windows that allows arbitrary code execution
- **Impact**: Attackers can execute arbitrary code with SYSTEM privileges on affected systems
- **Status**: Recently patched by Trend Micro with 9.8 CVSS score

### Misconfigured Proxy Server Exploitation
- **Description**: Systematic targeting of misconfigured proxy servers to gain unauthorized access to commercial LLM services
- **Impact**: Unauthorized access to paid AI services, potential data exposure and financial losses
- **Status**: Ongoing exploitation campaign

## Affected Systems and Products

- **VMware ESXi**: Hypervisor infrastructure vulnerable to virtual machine escape exploits
- **HPE OneView**: IT infrastructure management platform with maximum severity RCE vulnerability
- **Trend Micro Apex Central**: On-premise Windows versions affected by critical RCE flaw
- **SonicWall VPN Appliances**: Used as initial access vector in VMware ESXi exploitation campaigns
- **Proxy Servers**: Misconfigured servers providing unauthorized access to LLM services
- **Android TV Devices**: Over 2 million devices compromised by Kimwolf botnet
- **WhatsApp Platform**: Used as distribution vector for Astaroth banking trojan in Brazil
- **Chrome Browser**: Fake AI extensions compromising 900,000 users' data

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Chinese threat actors leveraging previously unknown VMware ESXi vulnerabilities
- **Spear-Phishing**: Multiple campaigns using targeted emails with malicious attachments and QR codes
- **VPN Compromise**: Initial access through compromised SonicWall VPN appliances
- **Rust-Based Malware**: RustyWater RAT deployment by Iranian MuddyWater group
- **Social Engineering**: WhatsApp worm spreading banking trojans through contact auto-messaging
- **Malicious Browser Extensions**: Fake AI Chrome extensions harvesting user credentials and data
- **Proxy Misconfiguration Abuse**: Systematic scanning for vulnerable proxy configurations
- **QR Code Phishing**: North Korean actors using malicious QR codes in targeted campaigns

## Threat Actor Activities

- **Chinese-Linked Hackers**: Exploiting VMware ESXi zero-days and targeting telecommunications providers with Linux-based malware in Southeastern Europe
- **MuddyWater (Iranian APT)**: Conducting spear-phishing campaigns with RustyWater RAT targeting diplomatic, maritime, financial, and telecom entities in Middle East
- **APT28 (Fancy Bear/Russian)**: Running credential-stealing campaigns targeting energy organizations, nuclear research agencies, and policy organizations in Turkey
- **North Korean State Actors**: Using malicious QR codes in spear-phishing campaigns as warned by FBI
- **Black Axe Criminal Organization**: 34 members arrested in Spain for €5.9M fraud operations and organized crime activities
- **Brazilian Cybercriminals**: Deploying Astaroth banking trojan via WhatsApp worm targeting Brazilian users
- **Botnet Operators**: Managing Kimwolf and Aisuru botnets affecting millions of Android TV streaming devices