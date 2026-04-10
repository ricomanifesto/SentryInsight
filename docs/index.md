# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation, with threat actors targeting Adobe Reader through malicious PDF documents since December 2025, and Windows systems through the BlueHammer exploit. Additional exploitation activity includes attacks on Ivanti Endpoint Manager Mobile systems, compromised Smart Slider 3 Pro plugin updates for WordPress and Joomla platforms, and sophisticated campaigns targeting corporate credentials through VENOM phishing-as-a-service operations. State-sponsored groups continue aggressive exploitation campaigns, with Russia's APT28/Fancy Bear and Forest Blizzard groups conducting global operations, while the UAT-10362 cluster targets Taiwanese organizations using the new LucidRook malware.

## Active Exploitation Details

### Adobe Reader Zero-Day Vulnerability
- **Description**: Previously unknown vulnerability in Adobe Reader being exploited through maliciously crafted PDF documents
- **Impact**: Allows attackers to compromise systems when users open malicious PDF files
- **Status**: Active exploitation confirmed since December 2025, vulnerability remains unpatched

### BlueHammer Windows Zero-Day Exploit
- **Description**: Zero-day flaw in Windows systems that allows for complete system takeover by a local user
- **Impact**: Enables privilege escalation and full system compromise
- **Status**: Proof-of-concept exploit released publicly under alias 'Chaotic Eclipse'

### Ivanti Endpoint Manager Mobile Critical Vulnerability
- **Description**: Critical-severity vulnerability in Ivanti EPMM systems
- **Impact**: Allows unauthorized access to mobile device management infrastructure
- **Status**: Actively exploited in attacks since January, CISA has mandated federal agencies patch by Sunday

### Smart Slider 3 Pro Update System Compromise
- **Description**: Hijacked update mechanism for WordPress and Joomla Smart Slider 3 Pro plugin
- **Impact**: Delivers malicious plugin versions containing multiple backdoors to websites
- **Status**: Update system compromised, malicious versions distributed to users

## Affected Systems and Products

- **Adobe Reader**: All versions vulnerable to zero-day PDF exploitation
- **Windows Systems**: Affected by BlueHammer local privilege escalation vulnerability
- **Ivanti Endpoint Manager Mobile (EPMM)**: Critical vulnerability under active exploitation
- **WordPress/Joomla Platforms**: Sites using Smart Slider 3 Pro plugin affected by malicious updates
- **EngageLab SDK**: Android applications using the SDK exposed 50M users including 30M crypto wallets
- **ChipSoft Healthcare Solutions**: Dutch healthcare software vendor hit by ransomware
- **Bitcoin Depot**: Crypto ATM network suffered $3.6 million theft from wallets

## Attack Vectors and Techniques

- **Malicious PDF Documents**: Zero-day Adobe Reader exploitation through crafted PDF files
- **Spear-Phishing Campaigns**: LucidRook malware delivery targeting NGOs and universities in Taiwan
- **Phishing-as-a-Service**: VENOM platform targeting C-suite executives' Microsoft credentials
- **Supply Chain Attacks**: Compromised plugin update mechanisms for web platforms
- **Router DNS Modification**: APT28 modifying single DNS settings in vulnerable SOHO routers
- **ClickFix Attacks**: Atomic Stealer malware using Script Editor on macOS systems
- **Pixel-Sized SVG Hiding**: Credit card stealer code hidden in 1-pixel SVG images on Magento stores

## Threat Actor Activities

- **APT28/Fancy Bear**: Continuing global onslaught with sophisticated techniques and router compromise campaigns
- **Forest Blizzard (APT28)**: Conducting malwareless cyber espionage through DNS modification in SOHO routers
- **UAT-10362**: Previously undocumented threat cluster targeting Taiwanese NGOs with LucidRook malware
- **UNC6783**: Compromising business process outsourcing providers to access high-value companies
- **Bitter-Linked Groups**: Hack-for-hire campaigns targeting journalists across MENA region
- **Chaotic Eclipse**: Researcher releasing Windows zero-day exploit citing issues with Microsoft
- **Masjesu Botnet**: DDoS-for-hire service targeting global IoT devices advertised via Telegram
- **Chaos Malware Variant**: Targeting misconfigured cloud deployments with added SOCKS proxy capabilities