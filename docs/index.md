# Exploitation Report

Critical exploitation activity continues to surge across multiple platforms and products, with several high-severity vulnerabilities being actively weaponized by threat actors. CISA has confirmed that ransomware gangs are now exploiting a VMware ESXi sandbox escape vulnerability that was previously used in zero-day attacks, while a five-year-old GitLab vulnerability remains under active exploitation despite its age. The Chinese-linked Amaranth Dragon threat group has been exploiting CVE-2025-8088 in WinRAR for espionage campaigns targeting Southeast Asian government agencies. Additionally, CISA has flagged a critical SolarWinds Web Help Desk remote code execution vulnerability as actively exploited, ordering federal agencies to patch within three days. Russian APT28 actors have demonstrated remarkable speed in weaponizing a Microsoft Office vulnerability, deploying exploits within just three days of disclosure.

## Active Exploitation Details

### VMware ESXi Sandbox Escape Vulnerability
- **Description**: A high-severity sandbox escape vulnerability in VMware ESXi that allows attackers to break out of virtualized environments
- **Impact**: Ransomware gangs can compromise ESXi hosts and encrypt virtual machines, leading to widespread system disruption
- **Status**: Previously exploited as a zero-day, now confirmed to be exploited by ransomware groups

### GitLab Five-Year-Old Vulnerability
- **Description**: A legacy vulnerability in GitLab that has persisted for five years
- **Impact**: Allows attackers to compromise GitLab instances and potentially access source code repositories and development infrastructure
- **Status**: Actively exploited in attacks, CISA has ordered government agencies to patch

### WinRAR Archive Processing Vulnerability
- **Description**: A vulnerability in WinRAR's archive processing functionality that can be exploited through malicious archive files
- **Impact**: Enables remote code execution and system compromise when victims open specially crafted archive files
- **Status**: Actively exploited by Amaranth Dragon APT group in espionage campaigns
- **CVE ID**: CVE-2025-8088

### SolarWinds Web Help Desk RCE Vulnerability
- **Description**: A critical remote code execution vulnerability in SolarWinds Web Help Desk (WHD) software
- **Impact**: Attackers can achieve complete system compromise and execute arbitrary code on affected systems
- **Status**: Added to CISA's KEV catalog due to active exploitation, federal agencies ordered to patch within three days

### Microsoft Office Rich Text Format Vulnerability
- **Description**: A vulnerability in Microsoft Office's handling of Rich Text Format (RTF) documents
- **Impact**: Enables multistage infection chains through specially crafted RTF documents
- **Status**: Weaponized by Russian APT28 within three days of disclosure

## Affected Systems and Products

- **VMware ESXi**: Hypervisor environments running vulnerable ESXi versions
- **GitLab**: GitLab instances running legacy versions with the five-year-old vulnerability
- **WinRAR**: Archive processing software vulnerable to CVE-2025-8088
- **SolarWinds Web Help Desk**: IT service management platform with critical RCE vulnerability
- **Microsoft Office**: Applications processing RTF documents vulnerable to APT28 attacks
- **Citrix NetScaler**: Infrastructure being targeted in coordinated reconnaissance campaigns
- **Docker Desktop**: Ask Gordon AI assistant with code execution vulnerability
- **Google Looker**: Business intelligence platform with cross-tenant RCE and data exfiltration vulnerabilities

## Attack Vectors and Techniques

- **Malicious Archive Files**: WinRAR exploitation through specially crafted archive files in email attachments
- **RTF Document Exploitation**: Microsoft Office attacks using weaponized Rich Text Format documents
- **Sandbox Escape**: VMware ESXi exploitation allowing breakout from virtualized environments
- **Web Application Exploitation**: Direct attacks against GitLab and SolarWinds web interfaces
- **Residential Proxy Networks**: Citrix NetScaler reconnaissance using tens of thousands of residential proxies
- **IPFS-Hosted Phishing**: DEAD#VAX campaign using InterPlanetary File System to host VHD phishing files
- **Signed Kernel Driver Abuse**: EDR evasion using legitimate but revoked EnCase forensic software drivers
- **AI Assistant Exploitation**: Docker Ask Gordon vulnerability through malicious image metadata

## Threat Actor Activities

- **Amaranth Dragon (APT41-linked)**: Chinese espionage group targeting Southeast Asian government and law enforcement agencies using CVE-2025-8088 WinRAR exploitation
- **APT28 (Russian)**: Rapid weaponization of Microsoft Office vulnerability within three days, deploying RTF-based attack chains
- **Ransomware Groups**: Multiple ransomware gangs exploiting VMware ESXi vulnerability for virtual machine encryption
- **DEAD#VAX Campaign**: Sophisticated malware operation deploying AsyncRAT through IPFS-hosted VHD files with advanced evasion techniques
- **Unknown Attackers**: Active exploitation of SolarWinds Web Help Desk and GitLab vulnerabilities by unidentified threat actors
- **GlassWorm Operators**: Self-replicating malware campaign targeting Open VSX developer ecosystems with infostealer infections