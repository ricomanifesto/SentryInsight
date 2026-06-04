# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms including Android, Linux, Microsoft 365, and various web servers. CISA has issued warnings about active attacks exploiting vulnerabilities in Android and Linux kernel systems. Zero-day vulnerabilities are being actively exploited in Acer Wave 7 routers with maximum severity ratings. Microsoft 365 Android applications contain a serious flaw that allows unauthorized access to account tokens. Additionally, a new HTTP/2 Bomb denial-of-service attack can crash major web servers within seconds, and Visual Studio Code contains a zero-day vulnerability enabling GitHub token theft through social engineering.

## Active Exploitation Details

### Android and Linux Kernel Vulnerabilities
- **Description**: CISA has warned about active exploitation of vulnerabilities in both the Linux kernel and Android operating system
- **Impact**: Allows attackers to compromise Android devices and Linux systems
- **Status**: Currently being actively exploited in the wild according to CISA warnings

### Acer Wave 7 Router Zero-Days
- **Description**: Two maximum-severity zero-day vulnerabilities affecting Acer's Wave 7 mesh routers
- **Impact**: Complete router compromise with maximum severity rating
- **Status**: Actively exploitable zero-days, Acer working on patches

### Microsoft 365 Android Debug Flag Vulnerability
- **Description**: A leftover development debug flag in Microsoft 365 Android apps disabled security checks that should limit account-token sharing to trusted Microsoft applications
- **Impact**: Any malicious app installed on the same device can steal Microsoft 365 account tokens and access user data
- **Status**: Vulnerability disclosed, affects production builds of Word, PowerPoint, Excel and other Microsoft 365 Android apps

### Visual Studio Code GitHub Token Theft
- **Description**: Zero-day vulnerability in Visual Studio Code that allows attackers to steal GitHub authentication tokens through a one-click attack
- **Impact**: Complete theft of GitHub OAuth tokens, enabling unauthorized repository access
- **Status**: Zero-day with public exploit code available

### Redis Remote Code Execution Flaw
- **Description**: Use-after-free vulnerability in Redis blocking-client code discovered by autonomous AI tools
- **Impact**: Allows authenticated users to execute arbitrary operating system commands on the Redis host machine
- **Status**: Patched by Redis
- **CVE ID**: CVE-2026-23479

### Windows Search URI NTLM Hash Disclosure
- **Description**: Unpatched vulnerability in Windows Search URI handling that can be exploited to steal user NTLMv2 hashes
- **Impact**: Enables attackers to obtain NTLM authentication hashes for credential attacks
- **Status**: Currently unpatched

### Google Gemini Prompt Injection
- **Description**: Vulnerability in Google Gemini's voice assistant that allows malicious commands to be hidden in notifications
- **Impact**: Enables social engineering attacks and unauthorized actions through voice assistant manipulation
- **Status**: Disclosed vulnerability affecting Android Gemini voice assistant

## Affected Systems and Products

- **Android Operating System**: Linux kernel vulnerabilities actively exploited
- **Acer Wave 7 Mesh Routers**: Two maximum-severity zero-day vulnerabilities
- **Microsoft 365 Android Apps**: Word, PowerPoint, Excel, and other Office applications affected by debug flag issue
- **Visual Studio Code**: Zero-day vulnerability enabling GitHub token theft
- **Redis Database**: Use-after-free vulnerability in blocking-client code
- **Windows Search**: Unpatched URI vulnerability affecting NTLM hash security
- **Google Gemini**: Voice assistant prompt injection vulnerability on Android
- **Web Servers**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora affected by HTTP/2 Bomb attack

## Attack Vectors and Techniques

- **Social Engineering via Notifications**: Malicious WhatsApp, Slack, SMS, Signal, Instagram, or Messenger notifications exploiting Google Gemini
- **One-Click Attacks**: VS Code vulnerability exploited through malicious links to steal GitHub tokens
- **Malspam Campaigns**: Google DoubleClick domain abuse to deliver DesckVB RAT malware
- **HTTP/2 Bomb DoS**: New denial-of-service technique crashing web servers within seconds from a single machine
- **Account Token Theft**: Exploitation of Microsoft 365 Android debug flags by malicious applications
- **Remote Code Execution**: Redis vulnerability allowing arbitrary command execution by authenticated users
- **NTLM Hash Harvesting**: Windows Search URI manipulation to steal authentication hashes
- **AI-Automated EDR Evasion**: Python scripts testing malware against Sophos, CrowdStrike, and Windows Defender

## Threat Actor Activities

- **Pakistani Intelligence Services**: Targeting Afghan Finance Ministry using Xeno RAT malware with standard TTPs
- **Chinese-Speaking Cybercrime Groups**: Deploying Atlas RAT backdoor and previously undocumented malware in European cyberattacks
- **China-Linked Espionage Groups**: Attacking at least a dozen Latin American nations, gathering intelligence on maritime shipping, oil production, and geopolitical interests
- **Weedhack Malware Campaign**: Targeting Minecraft players via YouTube to distribute system control malware
- **CountLoader Operations**: Affecting 86,000 victims through cryptocurrency mining malware distributed via pirated content
- **Email Campaign Against Financial Sector**: Monthslong targeted attack against global stock exchange executive using legitimate Windows tools