# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple platforms, with threat actors targeting Adobe Reader through malicious PDF campaigns since December 2025. Several sophisticated attack campaigns are underway, including the deployment of LucidRook malware against Taiwanese organizations, exploitation of misconfigured cloud deployments by Chaos botnet variants, and active compromise of Ivanti Endpoint Manager Mobile systems. Additionally, threat actors are leveraging compromised update mechanisms, stolen credentials, and advanced phishing techniques to maintain persistent access to corporate environments and steal sensitive data.

## Active Exploitation Details

### Adobe Reader Zero-Day Vulnerability
- **Description**: A previously unknown zero-day vulnerability in Adobe Reader being exploited through maliciously crafted PDF documents
- **Impact**: Attackers can execute arbitrary code and potentially achieve system compromise when victims open malicious PDF files
- **Status**: Active exploitation confirmed since at least December 2025, patch status not specified

### BlueHammer Windows Zero-Day
- **Description**: A zero-day vulnerability in Windows systems that allows local privilege escalation for system takeover
- **Impact**: Local users can escalate privileges to gain complete control of affected Windows systems
- **Status**: Proof-of-concept exploit released by researcher "Chaotic Eclipse", indicating active threat potential

### Ivanti Endpoint Manager Mobile (EPMM) Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti EPMM being actively exploited in targeted attacks
- **Impact**: Unauthorized access to mobile device management infrastructure and potential data exfiltration
- **Status**: Active exploitation confirmed since January, CISA emergency directive issued requiring federal agencies to patch by Sunday

### EngageLab SDK Vulnerability
- **Description**: Security flaw in widely-used Android SDK affecting millions of users including cryptocurrency wallet applications
- **Impact**: Potential exposure of sensitive user data and compromise of cryptocurrency wallet security
- **Status**: Now patched, but previously exposed 50 million Android users including 30 million crypto wallet users

## Affected Systems and Products

- **Adobe Reader**: All versions affected by zero-day vulnerability exploited via malicious PDFs
- **Windows Systems**: Affected by BlueHammer zero-day allowing local privilege escalation
- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical vulnerability under active exploitation
- **Android Applications**: 50+ million users affected through EngageLab SDK vulnerability
- **Smart Slider 3 Pro**: WordPress and Joomla plugin update system compromised with backdoored versions
- **Magento E-commerce Platforms**: Nearly 100 online stores affected by credit card skimming campaign
- **Small Office/Home Office (SOHO) Routers**: Targeted by Forest Blizzard for DNS manipulation attacks
- **Cloud Deployments**: Misconfigured instances targeted by Chaos botnet variants
- **IoT Devices**: Global targeting by Masjesu botnet for DDoS operations

## Attack Vectors and Techniques

- **Malicious PDF Documents**: Adobe Reader zero-day exploitation through crafted PDF files
- **Spear-phishing Campaigns**: LucidRook malware delivery targeting NGOs and universities in Taiwan
- **Phishing-as-a-Service (PhaaS)**: VENOM platform targeting C-suite executives' Microsoft credentials
- **Supply Chain Compromise**: Smart Slider plugin update system hijacked to distribute backdoors
- **DNS Manipulation**: Forest Blizzard modifying DNS settings in vulnerable SOHO routers for credential theft
- **ClickFix Attacks**: macOS campaigns using Script Editor to deliver Atomic Stealer malware
- **Credit Card Skimming**: Pixel-sized SVG images hiding malicious code on e-commerce sites
- **BPO Provider Compromise**: UNC6783 targeting business process outsourcing providers for lateral movement

## Threat Actor Activities

- **UAT-10362**: Conducting spear-phishing campaigns with LucidRook malware against Taiwanese NGOs and universities
- **Forest Blizzard (APT28)**: Russian group performing malwareless espionage through SOHO router DNS manipulation
- **Fancy Bear (APT28)**: Continuing global cyberattack campaigns with emphasis on credential harvesting
- **UNC6783**: Compromising business process outsourcing providers to access high-value corporate targets across multiple sectors
- **Bitter-Linked Groups**: Suspected Indian government-tied actors targeting journalists and activists across MENA region through hack-for-hire operations
- **VENOM Operators**: Running phishing-as-a-service platform specifically targeting senior executives' Microsoft accounts
- **Chaos Botnet Operators**: Expanding targeting to include misconfigured cloud deployments with new SOCKS proxy capabilities
- **Masjesu Botnet**: Operating DDoS-for-hire service through Telegram, targeting global IoT infrastructure