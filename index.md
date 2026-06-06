# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value infrastructure systems and software platforms. Active zero-day exploitation includes a Cisco SD-WAN vulnerability enabling root privilege escalation, while recently patched SolarWinds Serv-U flaws are being weaponized to crash servers. Supply chain attacks are proliferating across the npm ecosystem through malicious packages, and WordPress plugin vulnerabilities are enabling complete site takeovers. Additional threats include exposed fuel tank gauge systems being actively targeted, Android spyware campaigns, and sophisticated APT activities leveraging new malware frameworks.

## Active Exploitation Details

### Cisco SD-WAN Manager Zero-Day
- **Description**: High-severity unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager
- **Impact**: Enables attackers to achieve root privilege escalation
- **Status**: Currently unpatched and actively exploited in attacks
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Server Crash Vulnerability
- **Description**: Recently patched high-severity flaw in SolarWinds Serv-U file transfer solution
- **Impact**: Allows attackers to crash servers and disrupt operations
- **Status**: Actively exploited despite patch availability

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in WordPress plugin with approximately 4,000 active installations
- **Impact**: Enables arbitrary code execution leading to complete site compromise
- **Status**: Currently being actively exploited for site takeovers

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: Vulnerability allowing unauthenticated network attackers to write files and escalate to root privileges
- **Impact**: Complete system compromise with root access
- **Status**: Patched but exploit code has gone public
- **CVE ID**: CVE-2026-20230

### Hola Browser Supply Chain Compromise
- **Description**: Windows version of Hola Browser compromised to deliver cryptocurrency miners
- **Impact**: Installation of undeclared cryptocurrency mining malware
- **Status**: Active supply chain attack affecting browser users

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Unpatched systems vulnerable to root privilege escalation
- **SolarWinds Serv-U**: File transfer servers experiencing denial-of-service attacks
- **WordPress Sites**: Installations using Everest Forms Pro plugin (4,000+ active sites)
- **Cisco Unified Communications Manager**: Network communication systems
- **npm Package Ecosystem**: 36+ packages infected with IronWorm malware
- **Automatic Tank Gauge Systems**: Over 900 exposed ATG systems across US gas stations
- **Android Devices**: Arabic-speaking users targeted by Asin spyware
- **Cloud Infrastructure**: AWS, Google Cloud, and Azure servers hijacked by PCPJack
- **Hola Browser**: Windows version compromised with cryptomining payload

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN vulnerability
- **Supply Chain Poisoning**: Malicious npm packages distributing IronWorm Rust-based infostealer
- **WordPress Plugin Exploitation**: Critical vulnerabilities in form processing plugins
- **Mobile Spyware Distribution**: Fake news, PDF, and war map applications on Android
- **Internet-Exposed System Targeting**: Direct attacks on publicly accessible tank gauge systems
- **Cloud Server Hijacking**: Compromise of cloud infrastructure for SMTP relay networks
- **Browser Supply Chain Attacks**: Compromised browser distributions delivering cryptominers
- **Magecart Payment Skimming**: Credit card theft campaigns abusing Stripe API infrastructure

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor, Plenet, and AgentPSD malware to maintain persistence in Microsoft 365 environments
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks
- **TA4922 (Chinese Group)**: Expanding cybercrime operations globally beyond East Asia
- **PCPJack**: Hijacking cloud servers across AWS, Google Cloud, and Azure for covert SMTP relay networks
- **IronWorm Campaign**: Conducting supply chain attacks against npm ecosystem with Rust-based malware
- **Asin Spyware Operators**: Targeting Arabic-speaking users through malicious Android applications
- **Magecart Groups**: Exploiting Stripe infrastructure to host stolen payment information