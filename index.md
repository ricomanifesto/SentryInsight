# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact campaigns targeting diverse infrastructure components. Russia's APT28 (Forest Blizzard) is conducting sophisticated espionage operations by compromising vulnerable SOHO routers to harvest Microsoft Office authentication tokens without deploying traditional malware. Meanwhile, Iranian threat actors are actively disrupting U.S. critical infrastructure by targeting Internet-exposed programmable logic controllers (PLCs), causing operational disruptions and financial losses. Additional concerning activity includes a massive credit card skimming campaign affecting nearly 100 Magento e-commerce stores, active exploitation of vulnerabilities in Ivanti Endpoint Manager Mobile, Apache ActiveMQ Classic, and WordPress plugins, alongside emerging threats from North Korean supply chain attacks and new botnet operations.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti EPMM that allows unauthorized access to mobile device management systems
- **Impact**: Complete compromise of mobile device management infrastructure, potential access to corporate mobile devices and data
- **Status**: Actively exploited since January, CISA has mandated federal agencies patch by Sunday

### Apache ActiveMQ Classic Remote Code Execution
- **Description**: 13-year-old remote code execution vulnerability in Apache ActiveMQ Classic message broker that went undetected
- **Impact**: Attackers can execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Recently discovered vulnerability with proof-of-concept available, high risk of active exploitation

### Ninja Forms WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in the Ninja Forms File Uploads premium add-on allowing arbitrary file uploads without authentication
- **Impact**: Remote code execution on WordPress sites, complete website compromise
- **Status**: Currently being exploited in the wild

### SOHO Router Authentication Token Harvesting
- **Description**: APT28 exploiting known vulnerabilities in older Internet routers to modify DNS settings and harvest Microsoft Office authentication tokens
- **Impact**: Mass credential theft enabling persistent access to corporate email and cloud services
- **Status**: Ongoing espionage campaign targeting global organizations

### Internet-Exposed PLC Compromise
- **Description**: Iranian threat actors targeting vulnerabilities in Rockwell/Allen-Bradley programmable logic controllers accessible from the Internet
- **Impact**: Critical infrastructure disruption, operational manipulation, financial losses
- **Status**: Active targeting of U.S. critical infrastructure sectors

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management platforms in federal and enterprise environments
- **Apache ActiveMQ Classic**: Message broker systems across enterprise infrastructure
- **WordPress Sites**: Websites using Ninja Forms File Uploads premium add-on
- **SOHO Routers**: Older consumer and small office routers with known vulnerabilities
- **Rockwell/Allen-Bradley PLCs**: Internet-exposed programmable logic controllers in critical infrastructure
- **Magento E-commerce Platforms**: Nearly 100 online stores affected by credit card skimming campaign
- **Zendesk Systems**: Business process outsourcing providers using Zendesk for customer support
- **macOS Systems**: Targeted by Atomic Stealer malware via Script Editor abuse
- **Cloud Deployments**: Misconfigured cloud infrastructure targeted by Chaos botnet variant
- **IoT Devices**: Global IoT infrastructure targeted by Masjesu DDoS-for-hire botnet

## Attack Vectors and Techniques

- **DNS Manipulation**: Modifying single DNS settings in compromised routers to redirect traffic and harvest tokens
- **Malwareless Espionage**: Credential theft without traditional malware deployment through infrastructure compromise
- **SVG Image Hiding**: Concealing credit card stealing code in pixel-sized Scalable Vector Graphics images
- **ClickFix Social Engineering**: Tricking macOS users into executing malicious commands via Script Editor
- **Supply Chain Poisoning**: Distributing 1,700+ malicious packages across npm, PyPI, Go, and Rust ecosystems
- **Business Email Compromise**: Targeting BPO providers to gain access to high-value corporate customers
- **Spear Phishing**: PRISMEX malware deployment against Ukraine and NATO allies
- **File Upload Exploitation**: Bypassing authentication to upload arbitrary files on WordPress sites
- **OT Device Targeting**: Direct attacks on Internet-facing operational technology systems

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Conducting router-based credential harvesting campaigns targeting global organizations for espionage purposes
- **Iranian Threat Actors**: Systematically targeting U.S. critical infrastructure PLCs causing operational disruption across multiple sectors
- **UNC6783**: Compromising business process outsourcing providers to access high-value companies and steal Zendesk support tickets
- **Storm-1175**: Deploying Medusa ransomware at high velocity, exploiting both N-day and zero-day vulnerabilities
- **North Korean Actors**: Operating Contagious Interview campaign distributing malicious packages across multiple programming language ecosystems
- **Magento Skimmers**: Large-scale credit card theft operation targeting e-commerce platforms with sophisticated concealment techniques
- **Chaos Botnet Operators**: Expanding targeting to include misconfigured cloud deployments with enhanced SOCKS proxy capabilities
- **Masjesu Botnet**: Emerging DDoS-for-hire service advertised via Telegram targeting global IoT devices