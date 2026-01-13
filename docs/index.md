# Exploitation Report

CISA has issued critical warnings about active exploitation of a high-severity Gogs vulnerability that enables remote code execution through zero-day attacks. The agency has added this flaw to its Known Exploited Vulnerabilities catalog and mandated federal agencies to apply patches immediately. Meanwhile, threat actors are deploying sophisticated attack vectors including Chinese-linked hackers exploiting VMware ESXi zero-day vulnerabilities to escape virtual machines, the GoBruteforcer botnet targeting over 50,000 Linux servers with weak credentials, and supply chain attacks against n8n workflow automation platforms. Additional concerns include North Korean APT groups conducting quishing attacks and a maximum-severity vulnerability dubbed "Ni8mare" affecting nearly 60,000 n8n instances worldwide.

## Active Exploitation Details

### Gogs Remote Code Execution Vulnerability
- **Description**: High-severity security flaw in the Gogs Git service that allows attackers to execute arbitrary code remotely
- **Impact**: Complete system compromise and unauthorized code execution on affected servers
- **Status**: Actively exploited in zero-day attacks; patches available and mandated by CISA for federal agencies

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in VMware ESXi hypervisor that enable virtual machine escape
- **Impact**: Attackers can break out of virtual machine containment and access the underlying hypervisor infrastructure
- **Status**: Actively exploited by Chinese-linked threat actors; may have been developed years prior to discovery

### n8n Ni8mare Vulnerability
- **Description**: Maximum-severity vulnerability affecting the n8n workflow automation platform
- **Impact**: Complete system compromise of n8n instances
- **Status**: Nearly 60,000 instances remain unpatched and vulnerable to exploitation

### Instagram Password Reset Bug
- **Description**: Vulnerability allowing mass-requesting of password reset emails leading to data scraping
- **Impact**: Potential exposure of account data from over 17 million Instagram accounts
- **Status**: Fixed by Instagram, but data may have been compromised and leaked

## Affected Systems and Products

- **Gogs Git Service**: Self-hosted Git service installations vulnerable to remote code execution
- **VMware ESXi**: Hypervisor platforms susceptible to virtual machine escape attacks
- **n8n Workflow Automation**: Nearly 60,000 publicly exposed instances affected by Ni8mare vulnerability
- **Linux Servers**: Over 50,000 servers targeted by GoBruteforcer botnet through weak credential exploitation
- **npm Registry**: Eight malicious packages targeting n8n platform integrations
- **SonicWall VPN**: Compromised appliances used as initial access vectors
- **Instagram Platform**: Password reset functionality exploited for mass data scraping
- **Telegram**: Proxy link handling vulnerability exposing user IP addresses

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities exploited before patches were available
- **Credential Brute-Forcing**: GoBruteforcer botnet targeting servers with weak authentication
- **Supply Chain Attacks**: Malicious npm packages masquerading as legitimate n8n integrations
- **Virtual Machine Escape**: Sophisticated techniques to break out of VM containment
- **Spear-Phishing**: Targeted email campaigns delivering malicious payloads
- **Quishing Attacks**: QR code-based phishing techniques deployed via email
- **Browser-in-Browser**: Deceptive technique mimicking legitimate login interfaces
- **Mass Data Scraping**: Automated exploitation of password reset functionalities

## Threat Actor Activities

- **Chinese-Linked Groups**: Exploiting VMware ESXi zero-days through compromised SonicWall VPN appliances for virtual machine escape attacks
- **MuddyWater (Iranian APT)**: Conducting spear-phishing campaigns across Middle East diplomatic, maritime, financial, and telecom sectors using RustyWater RAT
- **Kimsuky (North Korean APT)**: Deploying quishing attacks against US and foreign government agencies, NGOs, and academic institutions
- **GoBruteforcer Operators**: Targeting cryptocurrency and blockchain project databases with enhanced botnet capabilities
- **Supply Chain Attackers**: Uploading malicious npm packages to steal OAuth credentials from n8n developers
- **BreachForums**: Criminal marketplace compromised, exposing data of 324,000 cybercriminals and administrators
- **Black Axe Organization**: International criminal group with 34 members arrested in Spain for €5.9M fraud operations