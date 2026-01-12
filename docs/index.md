# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitations targeting critical infrastructure and enterprise systems. Most notably, Chinese-speaking threat actors are exploiting VMware ESXi zero-day vulnerabilities to escape virtual machines, while HPE OneView faces maximum severity exploitation in the wild. Nation-state actors including Russian APT28 and North Korean groups are conducting sophisticated campaigns using credential harvesting and malicious QR codes. Additionally, threat actors are systematically targeting misconfigured proxy servers to gain unauthorized access to commercial AI services, and fake AI Chrome extensions have compromised data from 900,000 users.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Chinese-speaking threat actors are exploiting zero-day vulnerabilities in VMware ESXi hypervisors to escape virtual machine environments
- **Impact**: Allows attackers to break out of virtualized environments and potentially access the underlying host system
- **Status**: Currently being exploited in the wild, with exploitation potentially dating back to earlier periods

### HPE OneView Critical Vulnerability
- **Description**: A maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities that can lead to devastating consequences for enterprise infrastructure management
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central RCE Vulnerability
- **Description**: Critical remote code execution vulnerability affecting on-premise Windows versions of Trend Micro Apex Central
- **Impact**: Arbitrary code execution on affected systems, potentially compromising endpoint security management infrastructure
- **Status**: Security updates have been released to address the vulnerability

### Instagram Password Reset Bug
- **Description**: A vulnerability that allowed threat actors to mass-request password reset emails
- **Impact**: Enabled large-scale data scraping operations affecting over 17 million Instagram accounts
- **Status**: Instagram reports the bug has been fixed

## Affected Systems and Products

- **VMware ESXi**: Hypervisor systems vulnerable to zero-day exploits enabling virtual machine escape
- **HPE OneView**: IT infrastructure management platform with maximum severity RCE vulnerability
- **Trend Micro Apex Central**: On-premise Windows versions affected by critical RCE flaw
- **Instagram**: Social media platform affected by password reset mass-request vulnerability
- **SonicWall VPN**: Appliances compromised as initial access vectors for ESXi exploits
- **Chrome Extensions**: Fake AI-powered extensions compromising user data
- **Misconfigured Proxy Servers**: Systems providing unauthorized access to commercial LLM services

## Attack Vectors and Techniques

- **Virtual Machine Escape**: Exploitation of VMware ESXi zero-days to break out of virtualized environments
- **Initial Access via VPN**: Compromised SonicWall VPN appliances used as entry points for advanced attacks
- **Spear-Phishing Campaigns**: Targeted email attacks using malicious attachments and social engineering
- **Malicious QR Codes**: North Korean threat actors embedding malicious QR codes in spear-phishing campaigns
- **Credential Harvesting**: Systematic collection of user credentials through phishing operations
- **Mass Password Reset Exploitation**: Automated requests to overwhelm password reset systems for data collection
- **Proxy Server Abuse**: Targeting misconfigured proxy servers to access paid AI services without authorization
- **Malicious Browser Extensions**: Fake AI Chrome extensions designed to steal user data and send it to command and control servers

## Threat Actor Activities

- **Chinese-Speaking Threat Actors**: Conducting sophisticated VMware ESXi zero-day exploitation campaigns with potential long-term access
- **Russian APT28 (Fancy Bear)**: Running credential-stealing campaigns targeting energy organizations and policy institutions in Turkey and strategic policy entities
- **North Korean State-Sponsored Groups**: Deploying malicious QR codes in spear-phishing operations targeting cryptocurrency and technology sectors
- **MuddyWater (Iranian APT)**: Launching RustyWater RAT via spear-phishing across Middle East diplomatic, maritime, financial, and telecom sectors
- **Black Axe Criminal Organization**: 34 members arrested in Spain for €5.9M fraud operations and organized cybercrime activities
- **Pig Butchering Service Providers**: Industrial-scale fraud operations supported by specialized service providers offering tools and infrastructure