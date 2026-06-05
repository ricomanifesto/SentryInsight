# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise and cloud environments. Active threats include zero-day exploitation of Cisco SD-WAN infrastructure enabling root privilege escalation, widespread compromise of WordPress sites through a plugin vulnerability, and sophisticated supply chain attacks targeting both npm packages and browser applications. Additionally, threat actors are leveraging cloud infrastructure for covert operations while exploiting recently patched Cisco Unified Communications systems where proof-of-concept code has become publicly available.

## Active Exploitation Details

### **Cisco Catalyst SD-WAN Manager Zero-Day**
- **Description**: High-severity unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager
- **Impact**: Enables root privilege escalation on compromised systems
- **Status**: Currently unpatched and actively exploited in the wild
- **CVE ID**: CVE-2026-20245

### **Everest Forms Pro WordPress Plugin Critical Flaw**
- **Description**: Critical security vulnerability in Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Allows threat actors to execute arbitrary code leading to complete site compromise
- **Status**: Actively exploited by threat actors

### **Cisco Unified Communications Manager Vulnerability**
- **Description**: Critical flaw allowing unauthenticated network attackers to write files to the system and escalate to root privileges
- **Impact**: Complete system compromise with root access
- **Status**: Recently patched but proof-of-concept exploit code is now publicly available
- **CVE ID**: CVE-2026-20230

### **Redis Use-After-Free Vulnerability**
- **Description**: Two-year-old use-after-free vulnerability in Redis blocking-client code discovered by autonomous AI tool
- **Impact**: Allows authenticated users to execute arbitrary OS commands on the hosting machine
- **Status**: Recently patched after discovery
- **CVE ID**: CVE-2026-23479

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Zero-day vulnerability with active exploitation
- **Everest Forms Pro WordPress Plugin**: Approximately 4,000 active installations at risk
- **Cisco Unified Communications Manager**: Systems vulnerable to file write and privilege escalation
- **Redis Database**: Use-after-free vulnerability in blocking-client functionality
- **AWS, Google Cloud, and Azure Servers**: 230 cloud servers compromised by PCPJack threat actor
- **Hola Browser for Windows**: Compromised in supply chain attack delivering cryptocurrency miners
- **npm Packages**: 36 packages infected with IronWorm malware
- **GitHub Repositories**: Vulnerable to hijacking via Claude Code GitHub Action flaw
- **macOS Systems**: Targeted by FlutterShell backdoor via malicious Google and YouTube ads
- **Automatic Tank Gauge (ATG) Systems**: Internet-exposed fuel monitoring systems under attack

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Cisco SD-WAN vulnerability for privilege escalation
- **Supply Chain Attacks**: Compromise of npm packages with IronWorm malware and Hola Browser with cryptocurrency miners
- **Malvertising Campaigns**: FlutterShell backdoor distribution via malicious Google and YouTube advertisements
- **Cloud Infrastructure Hijacking**: PCPJack actor compromising cloud servers for SMTP relay networks
- **Social Engineering**: FIFA World Cup 2026-themed scams targeting fans with fake websites and banking malware
- **GitHub Repository Hijacking**: Single malicious GitHub issues exploiting Claude Code Action vulnerabilities
- **Traffic Distribution Systems**: Fake websites impersonating open-source tools to deliver malware
- **One-Click Attacks**: VS Code-based attacks to steal GitHub OAuth tokens
- **HTTP/2 Bomb DoS**: New denial-of-service technique capable of crashing web servers within minutes
- **Magecart Campaigns**: Credit card theft using Stripe API infrastructure to host stolen payment data

## Threat Actor Activities

- **PCPJack**: Hijacked 230 cloud servers across AWS, Google Cloud, and Azure to create covert SMTP email relay network for malicious activities
- **TA4922 (China-linked)**: Expanded phishing operations targeting organizations in the U.K., Germany, Italy, and South Africa
- **Chinese-speaking Cybercrime Groups**: Deploying Atlas RAT malware and previously undocumented tools in European cyberattacks
- **Operation FlutterBridge**: macOS malvertising campaign distributing FlutterShell backdoor through compromised advertisements
- **IronWorm Operators**: Conducted supply chain attack against 36 npm packages with infostealer malware
- **Southeast Asia Crypto Fraud Networks**: Multi-million dollar cryptocurrency fraud operations disrupted by DoJ with $3.8 million in assets frozen
- **Stock Exchange Infiltrators**: Unknown attackers maintained five-month persistence in major stock exchange executive's Outlook mailbox