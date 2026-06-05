# Exploitation Report

Critical vulnerability exploitation activity is currently affecting multiple platforms and systems. Most notably, Cisco has confirmed active exploitation of an unpatched zero-day vulnerability in SD-WAN Manager that enables attackers to gain root privileges. Additionally, threat actors are actively exploiting a critical flaw in the Everest Forms Pro WordPress plugin to achieve complete site compromise. Supply chain attacks are also prevalent, with IronWorm malware infiltrating 36 NPM packages and a compromised Hola Browser distributing cryptocurrency miners. These incidents represent significant security risks requiring immediate attention from organizations using affected technologies.

## Active Exploitation Details

### Cisco SD-WAN Manager Zero-Day
- **Description**: High-severity, unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager actively being exploited in the wild
- **Impact**: Attackers can escalate privileges to root level, potentially gaining complete control over SD-WAN infrastructure
- **Status**: Currently unpatched and under active exploitation
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Threat actors can execute arbitrary code leading to complete site compromise
- **Status**: Under active exploitation by threat actors

### Cisco Unified Communications Manager Vulnerability
- **Description**: Critical vulnerability allowing unauthenticated attackers on the network to write files and escalate to root privileges
- **Impact**: Complete system compromise with root access
- **Status**: Patched, but proof-of-concept exploit code has been made public
- **CVE ID**: CVE-2026-20230

### IronWorm NPM Supply Chain Attack
- **Description**: Rust-written infostealer malware targeting developers through compromised NPM packages
- **Impact**: Credential theft and propagation across software supply chain
- **Status**: 36 packages confirmed infected on npm index

### Hola Browser Supply Chain Compromise
- **Description**: Windows version of Hola Browser compromised to deliver undeclared cryptocurrency mining executable
- **Impact**: Unauthorized cryptocurrency mining on victim systems
- **Status**: Ongoing compromise affecting Windows users

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Unpatched systems vulnerable to root privilege escalation
- **Everest Forms Pro WordPress Plugin**: Approximately 4,000 active installations at risk of complete compromise
- **Cisco Unified Communications Manager**: Recently patched but exploit code publicly available
- **NPM Package Ecosystem**: 36 packages infected with IronWorm malware targeting developers
- **Hola Browser for Windows**: Compromised to deliver cryptocurrency miners
- **Cloud Infrastructure**: AWS, Google Cloud, and Azure servers hijacked by PCPJack for SMTP relay networks
- **macOS Systems**: Targeted by FlutterShell backdoor via malicious Google and YouTube advertisements
- **Anthropic's Claude Code GitHub Action**: Vulnerability allowing repository takeover through malicious issues

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Cisco SD-WAN Manager vulnerability
- **WordPress Plugin Exploitation**: Critical flaws in popular plugins leading to site takeover
- **Supply Chain Attacks**: Malicious packages in software repositories targeting developers
- **Malvertising Campaigns**: Fake Google and YouTube ads distributing FlutterShell backdoor on macOS
- **Traffic Distribution Systems**: Large-scale operations using fake sites mimicking open-source tools
- **Email Compromise**: Long-term access to stock exchange executive's Outlook mailbox
- **Cloud Server Hijacking**: PCPJack creating covert SMTP relay networks using compromised cloud infrastructure
- **Cryptocurrency Mining**: Unauthorized mining through compromised browser distributions

## Threat Actor Activities

- **PCPJack**: Hijacked 230 cloud servers across AWS, Google Cloud, and Azure to create covert SMTP email relay networks for malicious operations
- **TA4922 (China-linked)**: Expanded phishing attacks from East Asia to target organizations in the UK, Germany, Italy, and South Africa with diverse cybercrime activities
- **Operation FlutterBridge**: Sophisticated macOS malvertising campaign distributing FlutterShell backdoor through malicious Google and YouTube advertisements
- **IronWorm Operators**: Conducting supply chain attacks against NPM ecosystem, targeting developers to steal credentials and propagate across software supply chains
- **Magecart Campaign**: Abusing Stripe's API infrastructure to host credit card-stealing payloads and exfiltrate data from e-commerce checkout pages
- **Unknown Advanced Actors**: Conducting long-term surveillance of stock exchange executive's email communications over five-month period