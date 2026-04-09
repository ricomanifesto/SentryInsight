# Exploitation Report

Current exploitation activity reveals several critical zero-day vulnerabilities and active attack campaigns targeting enterprise systems and global infrastructure. The most significant threats include an Adobe Reader zero-day being actively exploited through malicious PDF documents since December 2025, a critical Ivanti EPMM vulnerability under active attack, and sophisticated campaigns by Russian APT28 and other nation-state actors. Additional concerns include supply chain attacks through malicious packages across multiple programming ecosystems, IoT botnet operations, and advanced persistent threats targeting critical infrastructure through exposed industrial control systems.

## Active Exploitation Details

### Adobe Reader Zero-Day Vulnerability
- **Description**: Previously unknown zero-day vulnerability in Adobe Reader being exploited through maliciously crafted PDF documents
- **Impact**: Remote code execution when victims open weaponized PDF files
- **Status**: Active exploitation ongoing since at least December 2025, patch status unknown

### Ivanti EPMM Critical Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti Endpoint Manager Mobile (EPMM) systems
- **Impact**: System compromise allowing unauthorized access to mobile device management infrastructure
- **Status**: Active exploitation in the wild since January, CISA has ordered federal agencies to patch by Sunday

### 13-Year-Old Apache ActiveMQ Classic Vulnerability
- **Description**: Remote code execution vulnerability in Apache ActiveMQ Classic that remained undetected for 13 years
- **Impact**: Allows attackers to execute arbitrary commands on affected systems
- **Status**: Recently discovered, exploitation potential confirmed

## Affected Systems and Products

- **Adobe Reader**: All versions affected by the zero-day vulnerability
- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical infrastructure management systems
- **Apache ActiveMQ Classic**: Message broker systems with 13-year-old RCE flaw
- **SOHO Routers**: Small office/home office routers targeted by APT28 for DNS manipulation
- **Magento E-commerce Platforms**: Nearly 100 online stores compromised with credit card stealers
- **IoT Devices**: Global IoT infrastructure targeted by Masjesu botnet
- **Industrial Control Systems**: Exposed PLCs in US critical infrastructure
- **Package Repositories**: npm, PyPI, Go, and Rust ecosystems with 1,700 malicious packages

## Attack Vectors and Techniques

- **Malicious PDF Documents**: Zero-day exploitation through weaponized Adobe Reader files
- **DNS Manipulation**: APT28 modifying single DNS settings in compromised routers for espionage
- **Supply Chain Attacks**: North Korean actors distributing malicious packages across multiple programming ecosystems
- **Pixel-Sized SVG Hiding**: Credit card stealers concealed in microscopic SVG images on e-commerce sites
- **ClickFix Attacks**: macOS stealer campaigns abusing Script Editor to trick users into executing malicious commands
- **BPO Provider Compromise**: Targeting business process outsourcing providers to access high-value clients
- **Exposed PLC Exploitation**: Direct attacks on Internet-facing operational technology devices

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Deploying PRISMEX malware in spear-phishing campaigns targeting Ukraine and NATO allies, conducting malwareless espionage through router DNS manipulation
- **UNC6783**: Compromising business process outsourcing providers to steal corporate Zendesk support tickets and access multiple high-value sectors
- **Bitter-Linked Group**: Orchestrating hack-for-hire campaigns targeting journalists, activists, and government officials across the Middle East and North Africa region
- **North Korean Contagious Interview Campaign**: Distributing 1,700 malicious packages across Go, Rust, and PHP ecosystems in addition to existing npm and PyPI operations
- **Iranian Threat Actors**: Disrupting US critical infrastructure through attacks on exposed programmable logic controllers, causing operational disruption and financial losses
- **Masjesu Botnet Operators**: Running DDoS-for-hire services through Telegram, targeting global IoT devices for distributed denial-of-service attacks