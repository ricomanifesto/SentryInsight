# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with threat actors targeting everything from enterprise cloud infrastructure to consumer IoT devices. The most concerning activities include Iranian hackers disrupting U.S. critical infrastructure through exposed programmable logic controllers, Russian military intelligence units harvesting Microsoft Office tokens via compromised routers, and a maximum-severity remote code execution vulnerability in Flowise being exploited in active attacks. Additional exploitation includes a 13-year-old Apache ActiveMQ vulnerability enabling remote command execution, critical flaws in WordPress plugins and Ivanti endpoint management systems, and sophisticated malware campaigns targeting macOS users and Magento e-commerce platforms.

## Active Exploitation Details

### Flowise Remote Code Execution Vulnerability
- **Description**: Maximum-severity vulnerability in the open-source Flowise platform for building custom LLM applications and agentic systems
- **Impact**: Allows attackers to execute arbitrary code on affected systems
- **Status**: Currently being exploited in active attacks
- **CVE ID**: CVE-2025-59528

### Apache ActiveMQ Classic Remote Code Execution
- **Description**: A 13-year-old undetected vulnerability in Apache ActiveMQ Classic message broker
- **Impact**: Enables attackers to remotely execute arbitrary commands on affected systems
- **Status**: Recently discovered and disclosed, exploitation potential confirmed

### Ninja Forms WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on for WordPress
- **Impact**: Allows uploading arbitrary files without authentication, leading to remote code execution
- **Status**: Actively being exploited by hackers

### Ivanti Endpoint Manager Mobile Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti EPMM that has been exploited since January
- **Impact**: Allows attackers to compromise endpoint management systems
- **Status**: CISA has mandated federal agencies patch by Sunday due to active exploitation

### Microsoft Office Token Theft via Router Compromise
- **Description**: Russian hackers exploiting known flaws in older Internet routers to harvest authentication tokens
- **Impact**: Mass collection of Microsoft Office user credentials and authentication tokens
- **Status**: Active campaign linked to Russian military intelligence units

### Internet-Facing PLC Exploitation
- **Description**: Iranian-linked hackers targeting exposed Rockwell/Allen-Bradley programmable logic controllers
- **Impact**: Disruption of critical infrastructure operations, file manipulation, operational disruption, and financial losses
- **Status**: Ongoing attacks against U.S. critical infrastructure

## Affected Systems and Products

- **Flowise Platform**: Open-source LLM application building platform
- **Apache ActiveMQ Classic**: Message broker software with 13-year-old vulnerability
- **Ninja Forms WordPress Plugin**: File Uploads premium add-on
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management solution
- **Microsoft Office**: Authentication token harvesting via router compromise
- **Rockwell/Allen-Bradley PLCs**: Industrial control systems in critical infrastructure
- **Magento E-commerce Platforms**: Nearly 100 online stores affected by credit card skimming
- **Zendesk Support Systems**: Corporate support ticket systems targeted by UNC6783
- **macOS Systems**: Script Editor exploitation in ClickFix attacks
- **IoT Devices**: Global targeting by Masjesu botnet for DDoS attacks
- **npm, PyPI, Go, Rust Package Repositories**: 1,700 malicious packages deployed

## Attack Vectors and Techniques

- **Pixel-Sized SVG Image Hiding**: Credit card stealer code hidden in 1-pixel SVG images on Magento stores
- **ClickFix Attack Variation**: macOS users tricked into executing malicious commands via Script Editor
- **Business Process Outsourcing Compromise**: Targeting BPO providers to access high-value companies
- **Spear-Phishing with PRISMEX Malware**: APT28 targeting Ukraine and NATO allies
- **Malicious Package Distribution**: North Korean hackers spreading 1,700 malicious packages across development ecosystems
- **Router Vulnerability Exploitation**: Mass harvesting of Microsoft Office authentication tokens
- **Internet-Exposed OT Device Targeting**: Direct attacks on programmable logic controllers
- **Supply Chain Attacks**: SaaS integrator breach leading to Snowflake customer data theft
- **Emoji-Based Communications**: Threat actors using emojis to evade detection filters

## Threat Actor Activities

- **UNC6783**: Compromising business process outsourcing providers to steal corporate Zendesk support tickets and access high-value companies
- **APT28 (Forest Blizzard/Pawn Storm)**: Russian threat actor deploying PRISMEX malware in spear-phishing campaigns targeting Ukraine and NATO allies
- **Iranian Threat Actors**: Disrupting U.S. critical infrastructure through attacks on Internet-facing programmable logic controllers
- **Russian Military Intelligence**: Mass harvesting Microsoft Office authentication tokens through router compromise campaigns
- **Storm-1175**: Microsoft-tracked financially motivated group deploying Medusa ransomware at high velocity, exploiting both N-day and zero-day vulnerabilities
- **North Korean Hackers (Contagious Interview)**: Spreading 1,700 malicious packages across npm, PyPI, Go, and Rust ecosystems
- **Masjesu Botnet Operators**: Operating DDoS-for-hire service targeting global IoT devices, advertised via Telegram
- **Chaos Botnet Operators**: New variant targeting misconfigured cloud deployments with SOCKS proxy capabilities