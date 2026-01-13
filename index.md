# Exploitation Report

Critical security vulnerabilities are being actively exploited across multiple platforms and services, with attackers targeting everything from AI platforms to gaming infrastructure. The most concerning developments include zero-day attacks against the Gogs Git service leading to CISA emergency directives, a critical ServiceNow AI Platform flaw allowing unauthenticated user impersonation, a maximum-severity vulnerability affecting nearly 60,000 n8n workflow automation instances, and sophisticated botnet operations targeting Linux servers and cryptocurrency databases. Additionally, supply chain attacks through malicious npm packages and advanced social engineering campaigns demonstrate the evolving sophistication of modern threat actors.

## Active Exploitation Details

### Gogs Git Service Remote Code Execution
- **Description**: A high-severity security flaw in the Gogs Git service that enables remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable systems, potentially leading to full system compromise
- **Status**: Being actively exploited as zero-day attacks; CISA has added it to the Known Exploited Vulnerabilities catalog and ordered federal agencies to patch immediately

### ServiceNow AI Platform Authentication Bypass
- **Description**: Critical security flaw in ServiceNow's AI Platform allowing unauthenticated user impersonation
- **Impact**: Unauthenticated attackers can impersonate legitimate users and perform arbitrary actions within the platform
- **Status**: Now patched by ServiceNow after disclosure

### n8n Workflow Automation Vulnerability (Ni8mare)
- **Description**: Maximum-severity vulnerability affecting n8n workflow automation instances
- **Impact**: Critical system compromise potential affecting automation workflows
- **Status**: Nearly 60,000 instances remain unpatched despite the severity

### Telegram Proxy Link IP Address Exposure
- **Description**: Vulnerability in how Telegram handles proxy links that can expose users' real IP addresses
- **Impact**: Single-click attack can reveal user's actual IP address, compromising anonymity
- **Status**: Telegram acknowledges the issue and plans to add warnings

## Affected Systems and Products

- **ServiceNow AI Platform**: Critical authentication bypass vulnerability allowing user impersonation
- **Gogs Git Service**: High-severity remote code execution flaw under active exploitation
- **n8n Workflow Automation**: Maximum-severity "Ni8mare" vulnerability affecting ~60,000 instances
- **Linux Servers**: Over 50,000 servers targeted by GoBruteforcer botnet campaigns
- **npm Registry**: Eight malicious packages uploaded targeting n8n workflow platform
- **Telegram**: Proxy link handling vulnerability exposing user IP addresses
- **Apex Legends**: Character hijacking attacks during live gaming sessions
- **Facebook/Instagram**: Browser-in-browser attacks targeting login credentials
- **Cryptocurrency Databases**: Targeted by GoBruteforcer botnet for credential compromise

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Gogs vulnerability for remote code execution
- **Supply Chain Attacks**: Malicious npm packages masquerading as legitimate n8n integrations to steal OAuth tokens
- **Botnet Operations**: GoBruteforcer targeting Linux servers and crypto databases through weak credential exploitation
- **Browser-in-Browser (BitB)**: Sophisticated Facebook credential theft using fake browser windows
- **Spear-Phishing**: Multi-stage SHADOW#REACTOR campaign delivering Remcos RAT through evasive attack chains
- **QR Code Phishing (Quishing)**: North Korean APT Kimsuky using QR codes in phishing emails
- **Character Hijacking**: Real-time manipulation of gaming characters in live Apex Legends matches
- **Social Engineering**: Advanced techniques combining AI optimization with traditional attack methods

## Threat Actor Activities

- **CISA Response**: Emergency directive issued for federal agencies to patch Gogs vulnerability due to active exploitation
- **SHADOW#REACTOR Campaign**: Multi-stage attack chain deploying Remcos RAT through evasive techniques targeting Windows systems
- **GoBruteforcer Operators**: Enhanced botnet targeting 50,000+ Linux servers and cryptocurrency project databases
- **MuddyWater (Iranian APT)**: RustyWater RAT deployment via spear-phishing across Middle East diplomatic, maritime, financial, and telecom sectors
- **Kimsuky (North Korean APT)**: QR code-based phishing campaigns targeting US and foreign government agencies, NGOs, and academic institutions
- **n8n Supply Chain Attackers**: Eight malicious npm packages uploaded to steal developer OAuth credentials
- **BreachForums Breach**: Major cybercriminal forum compromised, exposing 324,000 member identities
- **Port Infrastructure Attackers**: Seven-year sentence handed down for Rotterdam and Antwerp port system breaches
- **Target Corporation**: Claims of internal source code theft with samples published publicly
- **University of Hawaii**: Ransomware attack on Cancer Center compromising participant data from 1990s
- **Endesa Energy**: Spanish energy giant breach affecting customer contract information