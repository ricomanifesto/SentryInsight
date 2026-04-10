# Exploitation Report

Recent threat activity reveals a concerning landscape of active zero-day exploitations and sophisticated attack campaigns. Most notably, threat actors have been exploiting an Adobe Reader zero-day vulnerability using malicious PDF documents since December 2025, while multiple targeted campaigns leverage advanced malware including the new LucidRook malware targeting Taiwanese organizations and the emergence of sophisticated phishing-as-a-service platforms. Additionally, critical infrastructure vulnerabilities in Ivanti EPMM systems are being actively exploited, prompting emergency federal patching requirements, while threat groups like Russia's APT28 continue leveraging router compromises for persistent access.

## Active Exploitation Details

### Adobe Reader Zero-Day Vulnerability
- **Description**: An unknown zero-day vulnerability in Adobe Reader being exploited through maliciously crafted PDF documents
- **Impact**: Allows threat actors to compromise systems when users open malicious PDF files
- **Status**: Currently being exploited in the wild since at least December 2025; no patch information provided in source material

### Windows Zero-Day Vulnerability (BlueHammer)
- **Description**: A zero-day flaw in Windows systems that allows local privilege escalation for system takeover
- **Impact**: Enables local users to gain system-level access and control
- **Status**: Proof-of-concept exploit released by researcher "Chaotic Eclipse" citing disclosure issues with Microsoft

### Ivanti EPMM Critical Vulnerability
- **Description**: A critical-severity vulnerability in Ivanti Endpoint Manager Mobile (EPMM) systems
- **Impact**: System compromise and unauthorized access to enterprise mobile management infrastructure
- **Status**: Actively exploited since January; CISA has mandated federal agencies patch by Sunday

### EngageLab SDK Vulnerability
- **Description**: Security flaw in the widely-used EngageLab SDK for Android applications
- **Impact**: Exposed 50 million Android users including 30 million cryptocurrency wallet users to potential data theft
- **Status**: Now patched but previously affected millions of users

## Affected Systems and Products

- **Adobe Reader**: All versions affected by zero-day vulnerability with malicious PDF exploitation vector
- **Windows Systems**: Affected by BlueHammer zero-day allowing local privilege escalation
- **Ivanti EPMM**: Enterprise mobile management systems with critical vulnerability under active exploitation
- **Android Applications**: Apps using EngageLab SDK exposed millions of users including crypto wallet applications
- **WordPress/Joomla Sites**: Smart Slider 3 Pro plugin compromised through hijacked update mechanism
- **SOHO Routers**: Small office/home office routers targeted by Russia's APT28 for DNS manipulation attacks
- **Magento E-commerce**: Nearly 100 online stores affected by credit card skimmer hidden in pixel-sized SVG images

## Attack Vectors and Techniques

- **Malicious PDF Documents**: Zero-day exploitation through crafted PDF files targeting Adobe Reader users
- **Spear-Phishing Campaigns**: LucidRook malware delivered via targeted emails to NGOs and universities in Taiwan
- **Phishing-as-a-Service**: VENOM platform targeting C-suite executives' Microsoft credentials across industries
- **Supply Chain Attacks**: Smart Slider plugin update system compromised to deliver backdoored versions
- **DNS Manipulation**: APT28 modifying router DNS settings for malwareless espionage operations
- **ClickFix Attacks**: macOS campaigns using Script Editor to trick users into executing malicious commands
- **SVG Image Concealment**: Credit card stealers hidden in pixel-sized scalable vector graphics on e-commerce sites
- **Session Cookie Theft**: Info-stealing malware targeting browser session credentials

## Threat Actor Activities

- **APT28 (Fancy Bear)**: Russian state-sponsored group continuing global operations through SOHO router compromises and DNS manipulation for credential harvesting
- **UAT-10362**: Previously undocumented threat cluster conducting spear-phishing campaigns against Taiwanese NGOs and universities using LucidRook malware
- **UNC6783**: New threat actor compromising business process outsourcing providers to access high-value corporate targets and steal Zendesk support tickets
- **Forest Blizzard**: Russian APT group conducting fileless espionage operations by modifying DNS settings in compromised routers
- **VENOM Operators**: Threat actors using phishing-as-a-service platform to target senior executives across multiple industries
- **Bitter-Linked Campaign**: Hack-for-hire operations with suspected Indian government ties targeting journalists and activists across MENA region
- **Chaos Botnet Operators**: Expanding operations to target misconfigured cloud deployments with new SOCKS proxy capabilities
- **Masjesu Botnet**: DDoS-for-hire service operators targeting global IoT devices through Telegram-advertised services