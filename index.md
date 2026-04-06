# Exploitation Report

Critical vulnerabilities are being actively exploited across enterprise infrastructure and software supply chains. The most severe activity includes active exploitation of a critical FortiClient EMS vulnerability (CVE-2026-35616) that prompted emergency patching from Fortinet, widespread automated credential theft campaigns targeting Next.js applications through React2Shell exploitation (CVE-2025-55182), and sophisticated social engineering operations by North Korean threat actors targeting cryptocurrency platforms and npm package maintainers. Supply chain attacks have intensified with malicious npm packages targeting Redis and PostgreSQL databases, while nation-state actors continue targeting European government entities with advanced phishing and malware deployment techniques.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: A critical security flaw in Fortinet's FortiClient Enterprise Management Server that allows unauthorized access and system compromise
- **Impact**: Attackers can gain unauthorized access to enterprise management systems, potentially compromising managed endpoints across organizations
- **Status**: Actively exploited in the wild; emergency patches released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Vulnerability in Next.js Applications
- **Description**: A vulnerability in Next.js applications that enables automated credential theft through shell command injection
- **Impact**: Large-scale automated credential harvesting campaigns targeting web applications
- **Status**: Currently being exploited in widespread automated attacks
- **CVE ID**: CVE-2025-55182

### iOS DarkSword Vulnerability
- **Description**: A severe mobile operating system vulnerability that allows advanced persistent access and system compromise
- **Impact**: Enables sophisticated mobile device exploitation and persistent access for threat actors
- **Status**: Patched by Apple in iOS 18, breaking precedent for older iOS version patches

## Affected Systems and Products

- **Fortinet FortiClient EMS**: Enterprise management servers vulnerable to unauthorized access
- **Next.js Applications**: Web applications using React framework susceptible to automated credential theft
- **iOS Devices**: Mobile devices running iOS versions prior to security updates
- **Redis Databases**: Targeted by malicious npm packages for persistent implant deployment
- **PostgreSQL Databases**: Exploited through compromised npm packages for backdoor installation
- **Linux Servers**: Targeted with PHP web shells using HTTP cookie control channels
- **npm Registry**: Compromised with 36 malicious packages disguised as Strapi CMS plugins
- **Axios HTTP Client**: Popular JavaScript library compromised through social engineering

## Attack Vectors and Techniques

- **Social Engineering Campaigns**: Sophisticated months-long operations targeting software maintainers with fake Microsoft Teams error fixes
- **Supply Chain Compromise**: Injection of malicious code into legitimate npm packages and popular JavaScript libraries
- **QR Code Phishing**: Traffic violation scams using QR codes in text messages to redirect to credential harvesting sites
- **Device Code Phishing**: OAuth 2.0 Device Authorization Grant flow abuse showing 37x surge in attacks
- **PHP Web Shell Deployment**: Cookie-controlled remote code execution on Linux servers with cron persistence
- **Malicious Mobile Apps**: SparkCat malware variants on iOS and Android app stores targeting cryptocurrency wallet recovery phrases
- **Automated Credential Theft**: Large-scale automated campaigns exploiting web application vulnerabilities

## Threat Actor Activities

- **UNC1069 (North Korean APT)**: Conducted sophisticated social engineering campaign against Axios maintainer leading to npm supply chain attack
- **DPRK-linked Groups**: Six-month social engineering operation culminating in $285 million Drift cryptocurrency platform theft
- **TA416 (China-linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **Qilin Ransomware Group**: Claimed responsibility for attack against German political party Die Linke, threatening sensitive data leak
- **TeamPCP**: Supply chain attacks expanding with involvement from ShinyHunters and Lapsus$ groups creating complex attribution scenarios
- **Internal Threat**: Former infrastructure engineer pleaded guilty to extortion plot involving locking 254 Windows servers