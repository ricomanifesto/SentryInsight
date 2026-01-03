# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and infrastructure components. The RondoDox botnet is actively exploiting the React2Shell vulnerability to compromise IoT devices and Next.js servers in a nine-month campaign. Over 10,000 Fortinet firewalls remain vulnerable to ongoing attacks exploiting a five-year-old two-factor authentication bypass. The Kimwolf botnet is stalking local networks through a vulnerability that has been exploited for months. Meanwhile, sophisticated supply chain attacks continue with the Shai-Hulud worm targeting npm registries and Trust Wallet's Chrome extension being compromised, resulting in $8.5 million in cryptocurrency theft. Critical vulnerabilities in IBM API Connect and SmarterTools SmarterMail are also under active threat, with maximum severity ratings requiring immediate attention.

## Active Exploitation Details

### React2Shell Vulnerability in Next.js
- **Description**: Critical flaw affecting Next.js servers that allows remote code execution
- **Impact**: Enables attackers to infect servers with malware and cryptocurrency miners through the RondoDox botnet
- **Status**: Actively exploited in a persistent nine-month campaign targeting IoT devices and web applications
- **CVE ID**: CVE-2025-55182

### Fortinet Firewall 2FA Bypass
- **Description**: Five-year-old two-factor authentication bypass vulnerability in Fortinet firewalls
- **Impact**: Allows attackers to bypass authentication mechanisms and gain unauthorized access
- **Status**: Actively exploited with over 10,000 Internet-exposed firewalls still vulnerable

### IBM API Connect Authentication Flaw
- **Description**: Critical authentication system vulnerability in IBM API Connect
- **Impact**: Could allow attackers to gain remote access to the application
- **Status**: Recently disclosed with critical CVSS 9.8 rating
- **CVE ID**: CVE-2025-13915

### SmarterMail Remote Code Execution
- **Description**: Maximum-severity security flaw in SmarterTools SmarterMail email software
- **Impact**: Could be exploited to achieve remote code execution
- **Status**: Alert issued by Singapore's Cyber Security Agency

### Kimwolf Botnet Exploitation
- **Description**: Internet-wide vulnerability being exploited by the Kimwolf botnet
- **Impact**: Enables botnet operators to compromise local network infrastructure
- **Status**: Has been exploited for months with ongoing active campaigns

## Affected Systems and Products

- **Fortinet Firewalls**: Over 10,000 Internet-exposed devices vulnerable to 2FA bypass attacks
- **Next.js Servers**: Web applications and IoT devices targeted by RondoDox botnet through React2Shell flaw
- **IBM API Connect**: Authentication system vulnerable to remote access attacks
- **SmarterTools SmarterMail**: Email software at risk of remote code execution
- **Trust Wallet Chrome Extension**: Browser extension compromised affecting over 2,500 crypto wallets
- **npm Registry**: JavaScript package repository targeted by modified Shai-Hulud worm
- **macOS Systems**: Targeted by GlassWorm campaign through malicious VSCode/OpenVSX extensions
- **Browser Extensions**: DarkSpectre campaigns impacting 8.8 million users across multiple platforms

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Shai-Hulud worm variations targeting npm packages and browser extensions
- **Trojanized Applications**: GlassWorm campaign distributing malicious crypto wallet applications to macOS developers
- **Botnet Operations**: RondoDox and Kimwolf botnets exploiting infrastructure vulnerabilities for persistent access
- **Authentication Bypass**: Multi-year exploitation of Fortinet 2FA vulnerabilities
- **Remote Code Execution**: Critical flaws in enterprise software enabling direct system compromise
- **Cryptocurrency Theft**: Browser extension compromises leading to wallet drainage attacks
- **Multi-Stage Phishing**: Google Cloud Application Integration features abused for legitimate-looking phishing campaigns

## Threat Actor Activities

- **RondoDox Operators**: Conducting persistent nine-month campaign against IoT devices and web servers using React2Shell exploit
- **Kimwolf Group**: Operating botnet infrastructure targeting local networks through long-term vulnerability exploitation
- **GlassWorm Campaign**: Fourth wave targeting macOS developers with trojanized cryptocurrency applications
- **Shai-Hulud Actors**: Modified worm variants testing new payloads on npm registry for supply chain attacks
- **DarkSpectre Operations**: Large-scale browser extension campaigns affecting millions of users globally
- **Transparent Tribe**: Fresh RAT attacks targeting Indian governmental, academic, and strategic entities
- **Cryptocurrency Thieves**: Exploiting LastPass 2022 breach data for ongoing wallet drainage attacks years after initial compromise