# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple sectors and platforms. Microsoft's January 2026 Patch Tuesday addressed 114 vulnerabilities including three zero-day flaws, with one being actively exploited in the wild and two publicly disclosed. Critical exploitation activity includes a high-severity Gogs vulnerability enabling remote code execution that CISA has confirmed is being actively exploited in zero-day attacks. Additional concerning developments include sophisticated malware campaigns targeting Linux cloud environments, extensive web skimming operations affecting payment networks, and supply chain attacks targeting developer workflows.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Three zero-day vulnerabilities patched in Microsoft's January 2026 Patch Tuesday, including one that was actively exploited in the wild and two that were publicly disclosed
- **Impact**: One vulnerability was being actively exploited by threat actors before patches were available
- **Status**: Patches released in January 2026 through KB5073724 and other cumulative updates

### Gogs Remote Code Execution Vulnerability
- **Description**: High-severity security flaw in Gogs (Git service) enabling remote code execution
- **Impact**: Attackers can execute arbitrary code on affected systems without authentication
- **Status**: Being actively exploited in zero-day attacks; CISA has added to Known Exploited Vulnerabilities catalog and ordered federal agencies to patch

### ServiceNow AI Platform User Impersonation Flaw
- **Description**: Critical security vulnerability in ServiceNow's artificial intelligence platform allowing unauthenticated user impersonation
- **Impact**: Enables attackers to impersonate legitimate users without authentication credentials
- **Status**: Now patched by ServiceNow

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by zero-day vulnerabilities and Secure Boot certificate issues
- **Gogs Git Service**: Self-hosted Git service vulnerable to remote code execution attacks
- **ServiceNow AI Platform**: Enterprise AI platform affected by critical impersonation vulnerability
- **Linux Servers**: Over 50,000 Linux servers targeted by GoBruteforcer botnet
- **Payment Networks**: American Express, Diners Club, Discover payment systems affected by web skimming
- **MEXC Cryptocurrency Exchange**: API keys targeted through malicious Chrome extensions
- **n8n Workflow Platform**: OAuth tokens stolen through supply chain attack on community nodes

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Microsoft vulnerabilities before public disclosure
- **Remote Code Execution**: Exploitation of Gogs vulnerability to execute arbitrary commands
- **Web Skimming**: Long-running campaign since January 2022 targeting checkout pages to steal credit card data
- **Browser-in-Browser (BitB)**: Facebook credential theft using convincing fake browser windows
- **Supply Chain Attacks**: Malicious npm packages targeting n8n workflow automation platform
- **Malicious Chrome Extensions**: Cryptocurrency API key theft through fake trading tools
- **QR Code Phishing (Quishing)**: North Korean APT using QR codes in phishing campaigns
- **Multi-Stage Malware Delivery**: SHADOW#REACTOR campaign delivering Remcos RAT through evasive attack chains
- **Botnet Brute Force**: GoBruteforcer targeting Linux servers with weak credentials

## Threat Actor Activities

- **North Korean APT (Kimsuky)**: Conducting quishing attacks against US and foreign government agencies, NGOs, and academic institutions using QR code-filled phishing emails
- **Web Skimming Groups**: Operating sophisticated payment card theft campaign since January 2022 targeting major payment networks
- **Linux Malware Operators**: Deploying advanced VoidLink malware framework for long-term, stealthy access to cloud and container environments
- **Cryptocurrency Attackers**: Using malicious Chrome extensions and fake trading tools to steal MEXC exchange API keys
- **BreachForums Infiltrators**: Successfully breached the notorious cybercriminal forum, exposing 324,000 member details including real identities and administrator information
- **Supply Chain Attackers**: Uploading malicious npm packages masquerading as legitimate n8n workflow integrations to steal OAuth credentials