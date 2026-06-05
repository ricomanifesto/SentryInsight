# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities being actively exploited, with Chinese APT groups leading sophisticated campaigns against enterprise infrastructure. Most concerning is the active exploitation of CVE-2026-20245, an unpatched zero-day in Cisco Catalyst SD-WAN Manager enabling root privilege escalation. Additionally, threat actors are exploiting a critical WordPress plugin flaw and launching supply chain attacks through compromised NPM packages and browser distributions. Chinese espionage groups continue to deploy advanced persistent malware including previously undocumented tools, while cybercriminals are leveraging legitimate services like Stripe for payment card theft operations.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity zero-day vulnerability in Cisco Catalyst SD-WAN Manager systems
- **Impact**: Enables attackers to achieve root privilege escalation on affected systems
- **Status**: Currently unpatched and being actively exploited in attacks
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Allows threat actors to execute arbitrary code, leading to complete site compromise
- **Status**: Being actively exploited by threat actors to take over WordPress sites

### Cisco Unified Communications Manager Vulnerability
- **Description**: Network-accessible vulnerability allowing unauthenticated file writing with privilege escalation to root
- **Impact**: Enables attackers to write arbitrary files and escalate privileges to root access
- **Status**: Patched by Cisco, but exploit code has been made publicly available
- **CVE ID**: CVE-2026-20230

### Hola Browser Supply Chain Compromise
- **Description**: Windows version of Hola Browser compromised to deliver undeclared executable payloads
- **Impact**: Delivers cryptocurrency mining malware to users through legitimate software distribution
- **Status**: Active supply chain attack affecting Windows users

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Unpatched systems vulnerable to root privilege escalation
- **WordPress Sites**: Installations using Everest Forms Pro plugin (approximately 4,000 active sites)
- **Cisco Unified Communications Manager**: Systems patched but exploit code publicly available
- **Microsoft IIS Servers**: Targeted by OP-512 threat cluster using custom web shell frameworks
- **NPM Ecosystem**: 36 packages infected with IronWorm malware in supply chain attack
- **Cloud Infrastructure**: Over 230 AWS, Google Cloud, and Azure servers compromised by PCPJack
- **Gas Station Tank Gauge Systems**: Over 900 automatic tank gauge systems exposed online across US critical infrastructure
- **Android Devices**: Arabic-speaking users targeted by Asin spyware through fake applications
- **Hola Browser for Windows**: Compromised distribution delivering cryptocurrency miners

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Cisco SD-WAN vulnerability for privilege escalation
- **Supply Chain Attacks**: Compromise of legitimate software distributions including NPM packages and browser applications
- **Web Shell Deployment**: Custom web shell frameworks targeting Microsoft IIS servers
- **Mobile Malware Distribution**: Fake news, PDF, and war map applications delivering Android spyware
- **Cloud Server Hijacking**: Compromise of cloud infrastructure to create covert SMTP relay networks
- **WordPress Plugin Exploitation**: Arbitrary code execution through vulnerable form processing plugins
- **Magecart Campaigns**: Abuse of Stripe API infrastructure to host credit card stealing payloads
- **Social Engineering**: FIFA World Cup 2026-themed scams using fake websites and banking malware

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Maintaining persistent access to Microsoft 365 environments using Brickstorm backdoor and deploying new malware variants Plenet and AgentPSD
- **OP-512**: Previously unreported threat cluster targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack**: Hijacking cloud servers across AWS, Google Cloud, and Azure to establish covert SMTP email relay networks
- **TA4922 (Chinese)**: Expanding cybercrime operations globally beyond traditional East Asian targets with diverse attack methodologies
- **IronWorm Operators**: Conducting supply chain attacks against NPM ecosystem, compromising 36 packages with credential-stealing malware
- **Asin Operators**: Targeting Arabic-speaking users with sophisticated Android spyware through culturally relevant fake applications
- **Various Magecart Groups**: Leveraging Stripe's legitimate payment infrastructure to host stolen credit card data and exfiltration tools