# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by several high-severity flaws across enterprise infrastructure and software supply chains. The most severe threats include a zero-day vulnerability in Cisco's SD-WAN infrastructure that is being actively exploited in the wild, enabling attackers to achieve root privilege escalation. Additionally, threat actors are exploiting a critical WordPress plugin vulnerability to completely compromise websites, while sophisticated supply chain attacks are targeting developer ecosystems through malicious npm packages and compromised browser software. These exploitation campaigns demonstrate the continued focus on enterprise networking equipment, content management systems, and software distribution channels as primary attack vectors.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: A high-severity, unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager that allows privilege escalation
- **Impact**: Attackers can achieve root privilege escalation on affected systems
- **Status**: Currently unpatched and actively exploited in the wild
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: A critical security vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution
- **Status**: Actively exploited by threat actors to take over WordPress websites

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: A vulnerability that allows unauthenticated attackers on the network to write files to the system and escalate to root privileges
- **Impact**: Complete system compromise with root access from network-based attacks
- **Status**: Patched by Cisco, but exploit code has gone public
- **CVE ID**: CVE-2026-20230

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Enterprise SD-WAN infrastructure vulnerable to zero-day exploitation
- **WordPress Everest Forms Pro Plugin**: Approximately 4,000 websites using this plugin are at risk
- **Cisco Unified Communications Manager**: Enterprise communication systems affected by file write vulnerability
- **npm Package Repository**: 36 packages infected with IronWorm malware targeting developers
- **Hola Browser for Windows**: Compromised in supply chain attack delivering cryptocurrency miners
- **Cloud Infrastructure**: AWS, Google Cloud, and Azure servers hijacked by PCPJack threat actor
- **Anthropic Claude Code GitHub Action**: Vulnerable to repository hijacking attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN vulnerabilities for privilege escalation
- **WordPress Plugin Exploitation**: Targeting critical vulnerabilities in popular plugins for website takeover
- **Supply Chain Attacks**: Compromising legitimate software packages and browsers to deliver malware
- **Cloud Server Hijacking**: Compromising cloud infrastructure to create covert SMTP relay networks
- **Malvertising Campaigns**: Using malicious Google and YouTube ads to distribute FlutterShell backdoor to macOS users
- **GitHub Repository Hijacking**: Exploiting GitHub Actions to take control of public repositories
- **Traffic Distribution Systems (TDS)**: Using fake websites mimicking open-source tools to funnel users to malware

## Threat Actor Activities

- **PCPJack**: Hijacked 230 cloud servers across AWS, Google Cloud, and Azure to create a covert SMTP email relay network for malicious activities
- **TA4922 (China-linked)**: Expanded phishing operations globally, now targeting organizations in the U.K., Germany, Italy, and South Africa with diverse cybercrime activities
- **IronWorm Campaign**: Conducted sophisticated supply chain attack against npm ecosystem, compromising 36 packages with credential-stealing malware written in Rust
- **FlutterBridge Operation**: Executed macOS malvertising campaign distributing FlutterShell backdoor through malicious Google and YouTube advertisements
- **Magecart Groups**: Abusing Stripe's API infrastructure to host credit card-stealing payloads and exfiltrate data from compromised checkout pages
- **FIFA-themed Scammers**: Launching fraudulent campaigns targeting World Cup 2026 fans with fake websites, banking malware, and credential theft operations