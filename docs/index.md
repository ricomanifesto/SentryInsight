# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited in the wild, with the most significant being an Adobe Reader zero-day that has been exploited via malicious PDF documents since December 2025. Additionally, CISA has issued emergency directives for federal agencies to patch a critical Ivanti EPMM vulnerability that is under active exploitation. Threat actors are also leveraging compromised SOHO routers for credential harvesting, targeting cloud deployments with new malware variants, and conducting sophisticated supply chain attacks through malicious packages across multiple programming ecosystems. Iranian threat actors have demonstrated the ability to disrupt critical infrastructure through exposed industrial control systems.

## Active Exploitation Details

### Adobe Reader Zero-Day Vulnerability
- **Description**: A previously unknown zero-day vulnerability in Adobe Reader that allows exploitation through maliciously crafted PDF documents
- **Impact**: Attackers can execute arbitrary code and compromise systems when victims open specially crafted PDF files
- **Status**: Currently being exploited in the wild since December 2025, no patch information provided in the articles

### Ivanti EPMM Critical Vulnerability
- **Description**: A critical-severity vulnerability in Ivanti Endpoint Manager Mobile (EPMM) affecting enterprise mobile device management systems
- **Impact**: Allows attackers to compromise enterprise mobile management infrastructure
- **Status**: Actively exploited since January, CISA has ordered federal agencies to patch by Sunday deadline

### Apache ActiveMQ Remote Code Execution
- **Description**: A 13-year-old remote code execution vulnerability in Apache ActiveMQ Classic message broker that went undetected
- **Impact**: Enables attackers to execute arbitrary commands on vulnerable systems
- **Status**: Recently discovered vulnerability with potential for exploitation

## Affected Systems and Products

- **Adobe Reader**: All versions susceptible to zero-day PDF-based attacks
- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems under active attack
- **Apache ActiveMQ Classic**: Message broker systems vulnerable to 13-year-old RCE flaw
- **SOHO Routers**: Small office/home office routers being compromised for credential harvesting
- **Magento E-commerce Platforms**: Nearly 100 online stores affected by credit card stealing campaigns
- **Industrial Control Systems**: Internet-facing PLCs and OT devices in critical infrastructure sectors
- **Cloud Deployments**: Misconfigured cloud infrastructure targeted by Chaos malware variant
- **Package Repositories**: npm, PyPI, Go, Rust ecosystems infiltrated with 1,700+ malicious packages

## Attack Vectors and Techniques

- **Malicious PDF Documents**: Zero-day exploitation through crafted PDF files in Adobe Reader
- **DNS Modification**: APT28 modifying DNS settings in compromised routers for credential harvesting
- **ClickFix Attacks**: macOS campaigns using Script Editor to deliver Atomic Stealer malware
- **SVG Image Hiding**: Credit card stealers concealed in pixel-sized Scalable Vector Graphics images
- **Supply Chain Poisoning**: Malicious packages distributed across multiple programming language ecosystems
- **Cloud Misconfiguration Exploitation**: Targeting improperly configured cloud deployments
- **Spear-Phishing Campaigns**: Targeted email attacks deploying PRISMEX malware
- **Industrial Control System Compromise**: Direct attacks on Internet-exposed PLCs and OT devices

## Threat Actor Activities

- **APT28 (Forest Blizzard)**: Russian group conducting credential harvesting via compromised SOHO routers and deploying PRISMEX malware against Ukraine and NATO allies
- **UNC6783**: New threat actor compromising business process outsourcing providers to access high-value corporate targets and steal Zendesk support tickets
- **Bitter-Linked Group**: Suspected Indian government-affiliated actors running hack-for-hire campaigns targeting journalists and activists across the MENA region
- **North Korean Contagious Interview Campaign**: Spreading 1,700+ malicious packages across Go, Rust, PHP, npm, and PyPI ecosystems
- **Iranian Threat Actors**: Disrupting US critical infrastructure through compromise of exposed industrial control systems
- **Masjesu Botnet Operators**: Running DDoS-for-hire services targeting global IoT devices via Telegram advertising