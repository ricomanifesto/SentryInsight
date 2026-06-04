# Exploitation Report

Critical security vulnerabilities are currently being actively exploited across multiple platforms and applications. CISA has issued warnings about ongoing attacks targeting Linux kernel and Android operating system vulnerabilities. Zero-day vulnerabilities have been discovered in Acer Wave 7 routers with maximum severity ratings, while Microsoft 365 Android applications contain a serious authentication bypass flaw. Additional significant threats include a new HTTP/2 DoS attack affecting major web servers, exploitation targeting automatic tank gauge systems, and various social engineering attacks leveraging AI-generated content and malicious notifications.

## Active Exploitation Details

### Linux Kernel and Android Vulnerabilities
- **Description**: CISA warns of active exploitation targeting vulnerabilities in the Linux kernel and Android operating system
- **Impact**: Attackers can potentially gain unauthorized access to affected Linux and Android systems
- **Status**: Currently being actively exploited in the wild; organizations urged to apply patches immediately

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer Wave 7 mesh routers
- **Impact**: Complete compromise of affected router systems with maximum severity rating
- **Status**: Zero-day vulnerabilities with patches in development by Acer

### Microsoft 365 Android Authentication Bypass
- **Description**: A leftover debug flag in Microsoft 365 Android apps disabled security checks that limit account-token sharing to trusted Microsoft apps
- **Impact**: Any Android app on the same device can steal Microsoft 365 account tokens and access user data
- **Status**: Authentication security controls bypassed in production builds

### Redis Remote Code Execution Flaw
- **Description**: Use-after-free vulnerability in Redis blocking-client code discovered by autonomous AI tool
- **Impact**: Authenticated users can execute arbitrary OS commands on the machine hosting the Redis database
- **Status**: Patched by Redis
- **CVE ID**: CVE-2026-23479

### Windows Search URI NTLM Hash Disclosure
- **Description**: Unpatched vulnerability in Windows Search URI functionality that can be exploited to steal user credentials
- **Impact**: Attackers can steal NTLMv2 hashes from victims
- **Status**: Currently unpatched

### Visual Studio Code GitHub Token Theft
- **Description**: Zero-day vulnerability in Microsoft Visual Studio Code that enables one-click attacks to steal GitHub authentication tokens
- **Impact**: Complete theft of GitHub OAuth tokens through social engineering
- **Status**: Zero-day with public exploit code released

## Affected Systems and Products

- **Acer Wave 7 Mesh Routers**: All models affected by maximum-severity zero-day vulnerabilities
- **Linux Systems**: Kernel vulnerabilities actively exploited across distributions
- **Android Devices**: Operating system vulnerabilities and Microsoft 365 app authentication bypass
- **Microsoft 365 Android Apps**: Word, PowerPoint, Excel, and other Office applications with disabled security settings
- **Redis Database**: Use-after-free vulnerability in blocking-client code
- **Windows Systems**: Search URI functionality vulnerable to credential theft
- **Visual Studio Code**: GitHub integration vulnerable to token theft
- **Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora affected by HTTP/2 DoS
- **Automatic Tank Gauge Systems**: Internet-exposed fuel monitoring systems targeted by attackers
- **Google Gemini**: Android voice assistant vulnerable to notification-based prompt injection

## Attack Vectors and Techniques

- **Social Engineering via Notifications**: Malicious WhatsApp, Slack, SMS, Signal, Instagram, or Messenger notifications used to hijack Google Gemini voice assistant
- **HTTP/2 Bomb DoS Attack**: Single-machine denial-of-service attack that can crash web servers within seconds using HTTP/2 protocol vulnerabilities
- **Malicious App Installation**: Android malware exploiting Microsoft 365 authentication bypass through simple app installation
- **One-Click GitHub Token Theft**: Social engineering attacks using Visual Studio Code links to steal developer credentials
- **AI-Powered EDR Evasion**: Python scripts used to automatically test malware against endpoint detection systems from Sophos, CrowdStrike, and Windows Defender
- **DoubleClick Domain Abuse**: Google's DoubleClick domain used in malspam campaigns to deliver DesckVB RAT while evading detection
- **Atlas RAT Deployment**: Chinese threat actors using new backdoor malware in European cyberattacks

## Threat Actor Activities

- **Chinese-Speaking Cybercrime Groups**: Expanded targeting to European organizations using previously undocumented Atlas backdoor malware and other custom tools
- **China-Linked Espionage Groups**: Attacked at least a dozen Latin American nations gathering intelligence on maritime shipping, oil production, and geopolitical interests
- **Minecraft-Focused Malware Operators**: Weedhack campaign targeting Minecraft players via YouTube to distribute system control malware
- **Fuel Infrastructure Attackers**: Threat actors specifically targeting internet-exposed automatic tank gauge systems used in fuel monitoring
- **Financial Sector Attackers**: Monthslong email campaign against global stock exchange providing continuous access to executive communications
- **CountLoader Campaign**: Malware operation affecting over 86,000 victims through pirated content distribution
- **Cryptocurrency Miners**: Spreading malware through pirated content to deploy mining operations on victim systems