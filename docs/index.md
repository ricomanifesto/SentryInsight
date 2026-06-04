# Exploitation Report

The current threat landscape reveals multiple active exploitation campaigns targeting critical vulnerabilities across diverse platforms. CISA has issued urgent warnings about active exploitation of Linux kernel and Android vulnerabilities, while zero-day attacks are affecting infrastructure ranging from Acer Wave 7 routers to Microsoft Visual Studio Code. Notable incidents include Chinese threat actors deploying new Atlas RAT malware in European cyberattacks, Pakistan-based espionage operations targeting Afghanistan's finance ministry with Xeno RAT, and sophisticated attacks on fuel tank monitoring systems. Authentication bypass vulnerabilities in Microsoft 365 Android applications and Google Gemini voice assistant are also under active exploitation, demonstrating the broad scope of current threat activity.

## Active Exploitation Details

### Linux Kernel and Android Vulnerabilities
- **Description**: Multiple vulnerabilities in the Linux kernel and Android operating system are being actively exploited by threat actors
- **Impact**: Attackers can gain elevated privileges and compromise affected systems
- **Status**: CISA has added these vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog, requiring immediate patching

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer Wave 7 mesh routers
- **Impact**: Complete compromise of router functionality and network security
- **Status**: Acer is actively working on patches, but vulnerabilities remain unpatched and exploitable

### Microsoft Visual Studio Code Zero-Day
- **Description**: A zero-day vulnerability in VS Code that allows token theft through social engineering
- **Impact**: Attackers can steal GitHub OAuth tokens with a single click from targeted developers
- **Status**: Exploit code has been publicly released, vulnerability remains unpatched

### Microsoft 365 Android Apps Authentication Bypass
- **Description**: A development debug flag left enabled in production builds disabled security checks for account token sharing
- **Impact**: Any Android app can steal Microsoft 365 account tokens from affected applications
- **Status**: Vulnerability affects Word, PowerPoint, Excel, and other Microsoft 365 Android apps

### Google Gemini Voice Assistant Prompt Injection
- **Description**: Malicious notifications can inject commands into Google Gemini's voice assistant
- **Impact**: Attackers can hijack voice assistant functionality and execute unauthorized actions
- **Status**: Vulnerability allows social engineering attacks through poisoned notifications from WhatsApp, Slack, SMS, Signal, Instagram, or Messenger

### Windows Search URI Vulnerability
- **Description**: Unpatched vulnerability in Windows Search URI handling that exposes NTLMv2 hashes
- **Impact**: Attackers can steal user authentication credentials for lateral movement
- **Status**: Currently unpatched and exploitable

### Redis Remote Code Execution Flaw
- **Description**: Use-after-free vulnerability in Redis blocking-client code discovered by autonomous AI tools
- **Impact**: Authenticated users can execute arbitrary OS commands on the database server
- **Status**: Redis has patched the vulnerability
- **CVE ID**: CVE-2026-23479

### HTTP/2 Bomb Denial-of-Service Attack
- **Description**: New DoS attack technique that can crash web servers within seconds using HTTP/2 protocol manipulation
- **Impact**: Complete service disruption for affected web servers
- **Status**: Affects major web servers including NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora

## Affected Systems and Products

- **Acer Wave 7 Mesh Routers**: Multiple models affected by maximum-severity zero-day vulnerabilities
- **Linux Kernel**: Various distributions experiencing active exploitation
- **Android Operating System**: Multiple versions under active attack
- **Microsoft 365 Android Apps**: Word, PowerPoint, Excel, and other productivity applications
- **Microsoft Visual Studio Code**: Development environment vulnerable to token theft
- **Google Gemini**: Voice assistant functionality on Android devices
- **Redis Database**: Server installations with blocking-client functionality
- **Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora
- **Automatic Tank Gauge (ATG) Systems**: Fuel monitoring systems in critical infrastructure
- **Windows Systems**: Search URI functionality exposing authentication credentials

## Attack Vectors and Techniques

- **Social Engineering**: Malicious notifications used to hijack Google Gemini and trick VS Code users
- **Supply Chain Attacks**: Abuse of Google DoubleClick domain for malware delivery via DesckVB RAT
- **Spear Phishing**: Pakistan-based espionage targeting Afghan government officials
- **AI-Enhanced Evasion**: Automated testing of malware against EDR solutions from Sophos, CrowdStrike, and Windows Defender
- **Protocol Manipulation**: HTTP/2 Bomb attacks exploiting web server vulnerabilities
- **Credential Harvesting**: NTLMv2 hash theft through Windows Search URI exploitation
- **Token Theft**: GitHub OAuth token stealing via VS Code vulnerability
- **Malspam Campaigns**: Email-based delivery of remote access trojans using legitimate services

## Threat Actor Activities

- **Chinese-Speaking Groups**: Deploying Atlas RAT malware in European cyberattacks with new backdoor capabilities
- **Pakistan-Based Espionage**: Targeting Afghanistan's Finance Ministry using Xeno RAT for intelligence gathering
- **China-Linked APT Groups**: Conducting espionage operations across Latin America targeting maritime shipping and oil production
- **Iranian Ransomware Actors**: Utilizing sanctioned Nobitex cryptocurrency exchange for payment processing
- **Cybercriminal Networks**: Operating coordinated crypto fraud schemes across Southeast Asia with $3.8 million in frozen assets
- **Malware-as-a-Service Operators**: Targeting Minecraft users through YouTube with Weedhack malware campaigns
- **Stock Exchange Attackers**: Conducting monthslong email surveillance campaigns against finance executives using legitimate Windows tools