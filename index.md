# Exploitation Report

Critical exploitation activity is dominated by state-sponsored threat actors and sophisticated campaigns targeting infrastructure at scale. Russian APT28 (Forest Blizzard) has been conducting large-scale espionage operations by compromising vulnerable SOHO routers to harvest Microsoft Office authentication tokens without deploying traditional malware. Iranian threat actors are actively disrupting U.S. critical infrastructure by targeting Internet-exposed programmable logic controllers (PLCs), causing operational disruption and financial losses across multiple sectors. Additionally, CISA has issued emergency directives for federal agencies to patch a critical Ivanti Endpoint Manager Mobile vulnerability that has been exploited in attacks since January. The threat landscape also shows significant activity from financially motivated groups, with Storm-1175 deploying Medusa ransomware at high velocity using both N-day and zero-day vulnerabilities, while North Korean actors have distributed over 1,700 malicious packages across major software repositories.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Critical Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti EPMM that allows attackers to compromise endpoint management systems
- **Impact**: Complete system compromise of mobile device management infrastructure
- **Status**: Actively exploited since January 2025, CISA has ordered federal agencies to patch by Sunday

### SOHO Router Authentication Token Harvesting
- **Description**: Russian APT28 exploiting known flaws in older Internet routers to mass harvest Microsoft Office authentication tokens
- **Impact**: Large-scale credential theft and unauthorized access to corporate Microsoft Office environments
- **Status**: Ongoing active exploitation using "malwareless" techniques that modify DNS settings

### Internet-Exposed Programmable Logic Controllers
- **Description**: Iranian threat actors targeting Internet-facing operational technology devices, specifically Rockwell/Allen-Bradley PLCs
- **Impact**: Operational disruption, file and display manipulation, and financial losses across critical infrastructure sectors
- **Status**: Active ongoing campaign targeting U.S. critical infrastructure

### Ninja Forms WordPress Plugin File Upload Vulnerability
- **Description**: Critical vulnerability in Ninja Forms File Uploads premium add-on allowing arbitrary file upload without authentication
- **Impact**: Remote code execution on WordPress websites
- **Status**: Currently being exploited in the wild

### 13-Year-Old Apache ActiveMQ Classic RCE Vulnerability
- **Description**: Remote code execution vulnerability in Apache ActiveMQ Classic that remained undetected for 13 years
- **Impact**: Arbitrary command execution on affected message broker systems
- **Status**: Recently discovered but potentially exploitable since 2012

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical vulnerability requiring immediate patching by federal agencies
- **SOHO Routers**: Older Internet routers with known vulnerabilities being mass-exploited by Russian APT28
- **Rockwell/Allen-Bradley PLCs**: Internet-exposed programmable logic controllers in critical infrastructure
- **WordPress Sites**: Websites using Ninja Forms File Uploads premium add-on vulnerable to file upload attacks
- **Apache ActiveMQ Classic**: Message broker systems with 13-year-old RCE vulnerability
- **Magento E-commerce Platforms**: Nearly 100 online stores compromised with credit card stealing code
- **macOS Systems**: Targeted by Atomic Stealer malware through ClickFix attacks using Script Editor
- **Software Repositories**: npm, PyPI, Go, Rust, and PHP ecosystems contaminated with 1,700+ malicious packages

## Attack Vectors and Techniques

- **DNS Modification**: APT28 modifying single DNS settings in compromised routers for credential harvesting
- **Pixel-Sized SVG Injection**: Credit card stealers hidden in 1-pixel SVG images on Magento sites
- **ClickFix Social Engineering**: macOS users tricked into executing malicious commands via Script Editor
- **Supply Chain Poisoning**: North Korean actors distributing malicious packages across multiple programming language ecosystems
- **Internet-Exposed OT Targeting**: Direct attacks on publicly accessible operational technology devices
- **Business Process Outsourcing Compromise**: UNC6783 targeting BPO providers to access high-value corporate clients
- **Spear-Phishing Campaigns**: APT28 using targeted email attacks to deploy PRISMEX malware

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Conducting large-scale router compromise campaigns for authentication token theft and deploying PRISMEX malware against Ukraine and NATO allies
- **Iranian Threat Actors**: Systematically targeting U.S. critical infrastructure through Internet-exposed PLCs causing operational disruptions
- **Storm-1175**: Deploying Medusa ransomware at high velocity using both N-day and zero-day vulnerabilities
- **UNC6783**: Compromising business process outsourcing providers to gain access to high-value companies across multiple sectors
- **North Korean Contagious Interview Campaign**: Distributing over 1,700 malicious packages across npm, PyPI, Go, Rust, and PHP ecosystems
- **Masjesu Botnet Operators**: Running DDoS-for-hire service targeting global IoT devices through Telegram advertisements