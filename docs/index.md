# Exploitation Report

Several critical vulnerabilities are being actively exploited or have public proof-of-concept code available, posing significant risks to organizations worldwide. The most concerning developments include a critical Cisco Unified Communications Manager flaw (CVE-2026-20230) that allows unauthenticated attackers to achieve root privileges with public exploit code, a Redis remote code execution vulnerability (CVE-2026-23479) discovered by autonomous AI tools, and various supply chain attacks targeting npm packages and GitHub repositories. Additionally, new malware campaigns including IronWorm infostealer and FlutterShell backdoor are actively targeting organizations through sophisticated distribution methods.

## Active Exploitation Details

### Cisco Unified Communications Manager Vulnerability
- **Description**: Critical vulnerability in Cisco Unified Communications Manager that allows unauthenticated attackers to write files to the system and escalate privileges to root
- **Impact**: Complete system compromise, allowing attackers to gain root access on affected Cisco Unified CM systems
- **Status**: Patched by Cisco with public exploit code available
- **CVE ID**: CVE-2026-20230

### Redis Remote Code Execution Vulnerability
- **Description**: Use-after-free vulnerability in Redis blocking-client code discovered by autonomous AI tools
- **Impact**: Authenticated users can execute arbitrary OS commands on the machine hosting the Redis database
- **Status**: Patched by Redis developers
- **CVE ID**: CVE-2026-23479

### Claude Code GitHub Action Repository Hijacking
- **Description**: Flaw in Anthropic's Claude Code GitHub Action that allows attackers to take over vulnerable public repositories
- **Impact**: Repository takeover through malicious GitHub issues, potentially compromising CI/CD pipelines and code integrity
- **Status**: Actively exploitable with minimal attack requirements

### HTTP/2 Bomb Denial of Service Attack
- **Description**: New denial-of-service attack method targeting web servers using HTTP/2 protocol
- **Impact**: Can crash web servers within seconds to under a minute from a single attacking machine
- **Status**: Newly disclosed attack technique affecting HTTP/2-enabled web servers

## Affected Systems and Products

- **Cisco Unified Communications Manager**: All versions prior to security update, allowing unauthenticated file write and privilege escalation
- **Redis Database**: Versions containing the use-after-free vulnerability in blocking-client code
- **GitHub Repositories**: Public repositories using Anthropic's Claude Code GitHub Action
- **npm Package Ecosystem**: 36 infected packages containing IronWorm malware in supply chain attack
- **macOS Systems**: Targeted by FlutterShell backdoor through malicious Google and YouTube advertisements
- **Microsoft 365 Android Apps**: Word, PowerPoint, and Excel apps with disabled authentication security settings
- **Visual Studio Code**: Users vulnerable to GitHub OAuth token theft through malicious links
- **Google Gemini on Android**: Voice assistant vulnerable to hijacking through poisoned notifications
- **Fuel Tank Monitoring Systems**: Automatic tank gauge (ATG) systems exposed to internet-based attacks
- **Web Servers**: HTTP/2-enabled servers vulnerable to new DoS attack methods

## Attack Vectors and Techniques

- **Supply Chain Attacks**: IronWorm malware distributed through 36 compromised npm packages targeting Node.js developers
- **Malvertising Campaigns**: FlutterShell backdoor spread through malicious advertisements on Google and YouTube platforms
- **Social Engineering**: Traffic Distribution System (TDS) operations using fake websites mimicking open-source tools
- **Repository Hijacking**: Single malicious GitHub issue exploitation to compromise repositories using vulnerable GitHub Actions
- **Notification Hijacking**: Poisoned notifications from WhatsApp, Slack, SMS, Signal, Instagram, or Messenger to hijack Google Gemini
- **OAuth Token Theft**: One-click attacks through Visual Studio Code to steal GitHub authentication tokens
- **Protocol Exploitation**: HTTP/2 Bomb attacks leveraging protocol-specific vulnerabilities for rapid DoS
- **AI-Assisted EDR Evasion**: Python scripts used to automate testing against endpoint detection systems

## Threat Actor Activities

- **China-Linked TA4922**: Expanded phishing operations targeting organizations in U.K., Germany, Italy, and South Africa with new attack methodologies
- **Chinese Cybercrime Groups**: Deployment of Atlas RAT malware and other previously undocumented tools in European cyberattacks
- **Pakistani Intelligence Operations**: Use of Xeno RAT malware for espionage against Afghan Finance Ministry systems
- **Iranian Ransomware Actors**: Continued use of Nobitex cryptocurrency exchange for payment processing despite U.S. sanctions
- **Southeast Asia Fraud Networks**: Multi-million dollar cryptocurrency fraud operations disrupted by U.S. Department of Justice
- **Stock Exchange Attackers**: Unknown threat actors maintained persistent access to executive Outlook mailbox for five months
- **Critical Infrastructure Targeting**: Coordinated attacks against fuel tank monitoring systems and automatic tank gauge systems