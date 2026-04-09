# Exploitation Report

Critical active exploitation is currently underway across multiple attack vectors, with the most significant being a zero-day vulnerability in Adobe Reader that threat actors have been exploiting since December 2025 through maliciously crafted PDF documents. Additionally, CISA has issued urgent patching orders for an Ivanti EPMM vulnerability being actively exploited since January, while Russian APT28 operations are targeting global organizations through compromised SOHO routers and deploying new malware variants. The threat landscape also includes a 13-year-old Apache ActiveMQ vulnerability enabling remote code execution, targeted campaigns against journalists and activists, and sophisticated attacks on cloud infrastructure and e-commerce platforms.

## Active Exploitation Details

### Adobe Reader Zero-Day Vulnerability
- **Description**: Previously unknown zero-day vulnerability in Adobe Reader being exploited through maliciously crafted PDF documents
- **Impact**: Allows threat actors to compromise systems when users open malicious PDF files
- **Status**: Active exploitation since at least December 2025, zero-day status indicates no patch currently available

### Ivanti EPMM Critical Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti Endpoint Manager Mobile (EPMM) 
- **Impact**: System compromise allowing attackers to gain unauthorized access to mobile device management infrastructure
- **Status**: Active exploitation since January 2026, CISA has ordered federal agencies to patch by Sunday

### Apache ActiveMQ RCE Vulnerability
- **Description**: 13-year-old remote code execution vulnerability in Apache ActiveMQ Classic that remained undetected
- **Impact**: Enables attackers to execute arbitrary commands remotely on affected systems
- **Status**: Recently discovered after 13 years, exploitation potential confirmed

### SOHO Router DNS Manipulation
- **Description**: Vulnerability allowing modification of DNS settings in small office/home office routers
- **Impact**: Enables malwareless cyber espionage through DNS redirection and traffic manipulation
- **Status**: Actively exploited by Russian APT28 (Forest Blizzard) for credential harvesting

## Affected Systems and Products

- **Adobe Reader**: All versions affected by zero-day vulnerability, targeted via PDF documents
- **Ivanti EPMM**: Endpoint Manager Mobile platform with critical vulnerability requiring immediate patching
- **Apache ActiveMQ Classic**: 13-year-old vulnerability affecting remote code execution capabilities
- **SOHO Routers**: Small office/home office routers vulnerable to DNS setting manipulation
- **Magento E-commerce**: Nearly 100 online stores compromised with credit card stealing code
- **macOS Systems**: Targeted by Atomic Stealer malware through Script Editor abuse
- **Zendesk Platforms**: Corporate support ticket systems compromised by UNC6783 threat actor
- **Cloud Deployments**: Misconfigured cloud infrastructure targeted by Chaos botnet variants
- **IoT Devices**: Global IoT devices recruited into Masjesu botnet for DDoS attacks

## Attack Vectors and Techniques

- **Malicious PDF Documents**: Zero-day exploitation through crafted PDF files targeting Adobe Reader users
- **DNS Manipulation**: Router compromise enabling traffic redirection without deploying traditional malware
- **ClickFix Attacks**: Social engineering technique abusing macOS Script Editor for malware deployment
- **SVG Image Hiding**: Credit card stealing code concealed in pixel-sized Scalable Vector Graphics images
- **BPO Provider Compromise**: Targeting business process outsourcing companies to access high-value clients
- **Spear-Phishing Campaigns**: Targeted email attacks deploying PRISMEX malware against Ukraine and NATO allies
- **Cloud Misconfigurations**: Exploiting improperly configured cloud deployments for botnet expansion
- **PLC Exploitation**: Compromising Internet-facing operational technology devices in critical infrastructure

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Russian state-sponsored group conducting malwareless espionage through router compromise and deploying PRISMEX malware against Ukraine and NATO allies
- **UNC6783**: New threat actor compromising business process outsourcing providers to gain access to high-value corporate targets across multiple sectors
- **Bitter-Linked Campaign**: Hack-for-hire operation with suspected Indian government ties targeting journalists, activists, and government officials across MENA region
- **Iranian Threat Actors**: Disrupting US critical infrastructure through exposed programmable logic controller (PLC) compromise
- **Masjesu Botnet Operators**: Advertising DDoS-for-hire services via Telegram while recruiting global IoT devices
- **Chaos Botnet Operators**: Expanding targeting to include misconfigured cloud deployments with enhanced SOCKS proxy capabilities
- **Credit Card Skimming Groups**: Operating massive campaigns against e-commerce platforms using sophisticated SVG hiding techniques