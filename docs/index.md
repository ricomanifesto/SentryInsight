# Exploitation Report

Current exploitation activity shows several critical security incidents, with the most concerning being an Adobe Reader zero-day vulnerability that has been actively exploited since December 2025 through maliciously crafted PDF documents. Other significant exploitation includes attacks targeting Ivanti Endpoint Manager Mobile systems, a 13-year-old Apache ActiveMQ Classic vulnerability, and sophisticated supply chain attacks against the Smart Slider 3 Pro plugin affecting WordPress and Joomla installations. State-sponsored actors continue to leverage infrastructure compromises, with APT28 deploying new malware variants and conducting DNS manipulation attacks through compromised SOHO routers.

## Active Exploitation Details

### Adobe Reader Zero-Day Vulnerability
- **Description**: A previously unknown vulnerability in Adobe Reader being exploited through maliciously crafted PDF documents
- **Impact**: Allows threat actors to compromise systems when users open malicious PDF files
- **Status**: Active exploitation detected since December 2025, currently unpatched

### Ivanti Endpoint Manager Mobile (EPMM) Critical Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti EPMM that has been exploited in the wild
- **Impact**: Allows attackers to compromise enterprise mobile device management systems
- **Status**: CISA has ordered federal agencies to patch by Sunday, indicating active exploitation

### Apache ActiveMQ Classic Remote Code Execution
- **Description**: A 13-year-old undetected vulnerability in Apache ActiveMQ Classic that enables remote code execution
- **Impact**: Attackers can execute arbitrary commands on affected systems
- **Status**: Recently discovered after 13 years, potential for widespread exploitation

### Smart Slider 3 Pro Plugin Supply Chain Attack
- **Description**: Hackers compromised the update system for Smart Slider 3 Pro plugin for WordPress and Joomla
- **Impact**: Malicious plugin versions containing multiple backdoors were distributed to legitimate users
- **Status**: Active supply chain compromise affecting plugin update mechanisms

## Affected Systems and Products

- **Adobe Reader**: All versions vulnerable to zero-day PDF exploitation
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems
- **Apache ActiveMQ Classic**: Message broker software with 13-year-old RCE vulnerability
- **Smart Slider 3 Pro Plugin**: WordPress and Joomla plugin users receiving malicious updates
- **SOHO Routers**: Small office/home office routers compromised for DNS manipulation
- **Magento E-commerce Platforms**: Nearly 100 online stores affected by credit card stealing campaign
- **Zendesk Support Systems**: Corporate support ticket systems targeted by UNC6783
- **macOS Systems**: Targeted by Atomic Stealer malware via ClickFix attacks
- **Cloud Deployments**: Misconfigured cloud infrastructure targeted by Chaos malware variant

## Attack Vectors and Techniques

- **Malicious PDF Documents**: Zero-day exploitation through crafted PDF files targeting Adobe Reader
- **Supply Chain Compromise**: Hijacking legitimate software update mechanisms to distribute backdoors
- **DNS Manipulation**: Modifying single DNS settings in compromised routers for espionage
- **Spear-Phishing Campaigns**: Targeted email attacks deploying LucidRook malware and PRISMEX malware
- **ClickFix Social Engineering**: Tricking macOS users into executing malicious commands via Script Editor
- **Pixel-Sized SVG Injection**: Hiding credit card stealing code in microscopic SVG images on e-commerce sites
- **BPO Provider Compromise**: Targeting business process outsourcing companies to access high-value clients
- **IoT Device Exploitation**: Masjesu botnet targeting global IoT devices for DDoS-for-hire services

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Conducting "malwareless" cyber espionage through SOHO router DNS manipulation and deploying PRISMEX malware against Ukraine and NATO allies
- **UAT-10362**: Targeting Taiwanese NGOs and universities with LucidRook malware through spear-phishing
- **UNC6783**: Compromising business process outsourcing providers to steal corporate Zendesk support tickets
- **Bitter-Linked Group**: Orchestrating hack-for-hire campaigns targeting journalists and activists across the MENA region
- **Chaos Malware Operators**: Expanding botnet capabilities to target misconfigured cloud deployments with SOCKS proxy functionality
- **Masjesu Botnet**: Operating DDoS-for-hire services advertised via Telegram, targeting global IoT devices
- **Atomic Stealer Campaign**: Targeting macOS users with stealer malware through innovative ClickFix techniques
- **Credit Card Skimming Groups**: Conducting massive campaigns against Magento e-commerce platforms using steganographic techniques