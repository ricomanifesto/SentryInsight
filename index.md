# Exploitation Report

CISA has issued urgent warnings about active exploitation targeting critical vulnerabilities in Android and Linux systems, while multiple zero-day vulnerabilities continue to emerge across widely-used platforms. Chinese threat actors are deploying new malware including the Atlas RAT in expanded European operations, and attackers are leveraging AI to automate evasion techniques against endpoint detection systems. Critical infrastructure faces ongoing threats with attacks targeting fuel tank monitoring systems and web servers vulnerable to the new HTTP/2 Bomb denial-of-service attack. Additionally, coding errors in Microsoft 365 Android applications and Google Gemini voice assistant have created significant attack vectors for credential theft and system compromise.

## Active Exploitation Details

### Android and Linux Kernel Vulnerabilities
- **Description**: CISA has confirmed active exploitation of vulnerabilities affecting the Linux kernel and Android operating system
- **Impact**: Attackers can gain unauthorized access to affected Android and Linux systems
- **Status**: Currently being exploited in the wild; patches may be available depending on specific vulnerability

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer Wave 7 mesh routers
- **Impact**: Complete compromise of affected router systems with maximum severity rating
- **Status**: Zero-day vulnerabilities with no patches currently available; Acer working on fixes

### Visual Studio Code GitHub Token Theft
- **Description**: Zero-day vulnerability in Microsoft Visual Studio Code that allows attackers to steal GitHub authentication tokens through a one-click attack
- **Impact**: Complete theft of GitHub OAuth tokens and potential repository access
- **Status**: Zero-day vulnerability with active exploitation possible

### Redis Remote Code Execution Flaw
- **Description**: Use-after-free vulnerability in Redis blocking-client code that allows authenticated users to execute arbitrary OS commands
- **Impact**: Full system compromise on machines hosting Redis databases
- **Status**: Recently patched by Redis
- **CVE ID**: CVE-2026-23479

### Microsoft 365 Android Apps Token Stealing
- **Description**: Development debug flag left enabled in production builds of Microsoft 365 Android apps, disabling security checks for account token sharing
- **Impact**: Any malicious app on the same device can steal Microsoft 365 account tokens
- **Status**: Security flaw affecting current production builds

### Windows Search URI NTLM Hash Disclosure
- **Description**: Unpatched vulnerability in Windows Search URI functionality that allows attackers to steal NTLMv2 hashes
- **Impact**: Credential theft enabling potential lateral movement and privilege escalation
- **Status**: Currently unpatched and exploitable

### Google Gemini Voice Assistant Hijacking
- **Description**: Prompt injection vulnerability in Google Gemini's voice assistant that allows malicious notifications to execute hidden commands
- **Impact**: Social engineering attacks and unauthorized actions through voice assistant manipulation
- **Status**: Active vulnerability affecting Android users

## Affected Systems and Products

- **Acer Wave 7 Mesh Routers**: All models affected by two maximum-severity zero-day vulnerabilities
- **Android Operating System**: Multiple versions affected by actively exploited vulnerabilities
- **Linux Kernel**: Various distributions and versions under active attack
- **Microsoft Visual Studio Code**: All versions vulnerable to GitHub token theft attack
- **Redis Database**: Versions affected by CVE-2026-23479 remote code execution flaw
- **Microsoft 365 Android Apps**: Word, PowerPoint, Excel, and other apps with disabled security settings
- **Windows Search**: All Windows versions with Search URI functionality
- **Google Gemini Voice Assistant**: Android implementations vulnerable to prompt injection
- **Major Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora affected by HTTP/2 Bomb attack
- **Automatic Tank Gauge Systems**: Internet-exposed fuel monitoring systems targeted in attacks

## Attack Vectors and Techniques

- **One-Click Exploitation**: Attackers use specially crafted links in VS Code to steal GitHub tokens instantly
- **Malicious Notifications**: Poisoned notifications from WhatsApp, Slack, SMS, and other messaging apps hijack Google Gemini
- **AI-Powered EDR Evasion**: Python scripts automatically test malware against Sophos, CrowdStrike, and Windows Defender
- **HTTP/2 Bomb DoS**: Single-machine attacks crash web servers within seconds using HTTP/2 protocol vulnerabilities
- **Debug Flag Abuse**: Production applications with leftover development flags bypass security controls
- **Search URI Exploitation**: Windows Search functionality manipulated to leak NTLM credentials
- **Remote Access Trojan Deployment**: Atlas RAT and other malware spread through sophisticated campaigns
- **Infrastructure Targeting**: Direct attacks against fuel tank monitoring and critical infrastructure systems
- **Malspam Campaigns**: DesckVB RAT delivered through Google DoubleClick domain abuse

## Threat Actor Activities

- **Chinese-Speaking Groups**: Expanded targeting to European organizations using Atlas RAT and previously undocumented malware
- **China-Linked Espionage Groups**: Attacked at least twelve Latin American nations, gathering intelligence on maritime shipping, oil production, and geopolitical interests
- **Cybercriminal Organizations**: Nine organized crime groups dismantled in illegal streaming operations across Europe
- **Finance-Targeting Actors**: Monthslong email campaign against global stock exchange executive using legitimate Windows tools
- **Minecraft-Targeting Campaigns**: Weedhack malware-as-a-service targeting gaming communities through YouTube
- **CountLoader Operations**: Malware affecting 86,000 victims through pirated content distribution
- **Critical Infrastructure Attackers**: Targeting internet-exposed automatic tank gauge systems used for fuel monitoring