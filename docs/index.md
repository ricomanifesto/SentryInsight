# Exploitation Report

Critical security threats are actively targeting organizations through multiple attack vectors, with CISA highlighting the active exploitation of a high-severity Gogs vulnerability that enables remote code execution. Concurrent threats include the SHADOW#REACTOR campaign delivering Remcos RAT through sophisticated multi-stage attacks, the GoBruteforcer botnet compromising over 50,000 Linux servers through credential attacks, and supply chain compromises targeting the n8n workflow automation platform. A ServiceNow AI Platform vulnerability has been patched that allowed unauthenticated user impersonation, while threat actors continue leveraging social engineering techniques including browser-in-browser attacks for credential theft and QR code phishing campaigns attributed to North Korean APT groups.

## Active Exploitation Details

### Gogs Vulnerability
- **Description**: High-severity security flaw in Gogs (Go Git Service) that enables remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable systems, potentially leading to full system compromise
- **Status**: Currently being exploited in zero-day attacks; CISA has ordered federal agencies to patch systems

### ServiceNow AI Platform User Impersonation
- **Description**: Critical security flaw in ServiceNow's AI Platform allowing unauthenticated attackers to impersonate legitimate users
- **Impact**: Unauthorized users can perform arbitrary actions by impersonating other users, potentially accessing sensitive data and system functions
- **Status**: Patched by ServiceNow; organizations advised to update immediately

### n8n Workflow Automation Platform Supply Chain Attack
- **Description**: Eight malicious packages uploaded to npm registry masquerading as legitimate n8n integrations
- **Impact**: Theft of developers' OAuth credentials and potential compromise of workflow automation systems
- **Status**: Ongoing threat targeting the n8n ecosystem through compromised community nodes

### Ni8mare n8n Vulnerability
- **Description**: Maximum-severity vulnerability affecting n8n workflow automation instances
- **Impact**: Complete system compromise possible on vulnerable instances
- **Status**: Nearly 60,000 n8n instances remain unpatched and exposed online

## Affected Systems and Products

- **Gogs Git Service**: Self-hosted Git service installations vulnerable to remote code execution
- **ServiceNow AI Platform**: ServiceNow's artificial intelligence platform components
- **n8n Workflow Automation**: Approximately 60,000 exposed instances globally
- **Linux Servers**: Over 50,000 servers targeted by GoBruteforcer botnet
- **Windows Systems**: Targeted by SHADOW#REACTOR campaign delivering Remcos RAT
- **Cryptocurrency and Blockchain Databases**: Specifically targeted by GoBruteforcer attacks
- **Facebook/Meta Platforms**: Targeted by browser-in-browser credential theft campaigns
- **Telegram Users**: Affected by proxy link IP address exposure vulnerability
- **Apex Legends Gaming Platform**: Character hijacking during live matches

## Attack Vectors and Techniques

- **Remote Code Execution**: Direct exploitation of Gogs vulnerability for system compromise
- **Multi-Stage Attack Chains**: SHADOW#REACTOR campaign employs evasive techniques to deliver RATs
- **Credential Brute-Forcing**: GoBruteforcer botnet targeting weak SSH and database credentials
- **Supply Chain Compromise**: Malicious npm packages targeting developer workflows
- **Browser-in-Browser (BitB)**: Advanced phishing technique mimicking legitimate login interfaces
- **QR Code Phishing (Quishing)**: North Korean APT using QR codes in phishing emails
- **Social Engineering**: Spear-phishing campaigns targeting specific sectors and organizations
- **User Impersonation**: Exploiting authentication flaws to bypass access controls

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Conducting spear-phishing campaigns with RustyWater RAT targeting Middle East diplomatic, maritime, financial, and telecom sectors
- **Kimsuky (North Korean APT)**: Deploying QR code phishing attacks against US and foreign government agencies, NGOs, and academic institutions
- **SHADOW#REACTOR Campaign**: Sophisticated multi-stage attack delivering Remcos RAT through evasive techniques
- **GoBruteforcer Operators**: Targeting cryptocurrency project databases and Linux servers for botnet recruitment
- **n8n Supply Chain Attackers**: Uploading malicious packages to npm registry to steal OAuth credentials
- **BreachForums Attackers**: Successfully breached the notorious cybercriminal forum, exposing 324,000 user records
- **Port Infrastructure Hackers**: Dutch national sentenced for breaching Rotterdam and Antwerp ports
- **Gaming Platform Attackers**: Hijacking Apex Legends characters during live gameplay sessions