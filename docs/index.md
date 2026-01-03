# Exploitation Report

Critical exploitation activity continues across multiple vectors, with active campaigns targeting both legacy vulnerabilities and newly disclosed flaws. The most significant threats include a five-year-old two-factor authentication bypass vulnerability affecting over 10,000 Fortinet firewalls, the React2Shell flaw being exploited by the RondoDox botnet to compromise IoT devices and Next.js servers, and ongoing supply chain attacks through the Shai-Hulud worm targeting npm packages. Additionally, threat actors are leveraging compromised data from the 2022 LastPass breach to conduct sophisticated cryptocurrency thefts, while new malware campaigns target macOS users and abuse legitimate cloud services for phishing operations.

## Active Exploitation Details

### **Fortinet Two-Factor Authentication Bypass**
- **Description**: A five-year-old vulnerability in Fortinet firewalls that allows attackers to bypass two-factor authentication mechanisms
- **Impact**: Complete authentication bypass, allowing unauthorized access to protected network infrastructure
- **Status**: Actively exploited with over 10,000 Internet-exposed devices remaining vulnerable

### **React2Shell Critical Flaw**
- **Description**: Critical vulnerability in Next.js applications that enables remote code execution
- **Impact**: Full server compromise, malware deployment, and cryptominer installation
- **Status**: Actively exploited by RondoDox botnet for nine months
- **CVE ID**: CVE-2025-55182

### **IBM API Connect Authentication Bypass**
- **Description**: Critical authentication system vulnerability in IBM API Connect
- **Impact**: Remote access to applications and potential system compromise
- **Status**: Recently disclosed with maximum severity rating
- **CVE ID**: CVE-2025-13915

### **SmarterMail Remote Code Execution**
- **Description**: Maximum-severity flaw in SmarterTools SmarterMail email software
- **Impact**: Remote code execution capabilities for attackers
- **Status**: Critical alert issued by Singapore's Cyber Security Agency

## Affected Systems and Products

- **Fortinet Firewalls**: Over 10,000 Internet-exposed devices vulnerable to 2FA bypass attacks
- **Next.js Servers**: Web applications and IoT devices targeted by RondoDox botnet exploitation
- **IBM API Connect**: Authentication systems with CVSS 9.8 rated vulnerability
- **SmarterTools SmarterMail**: Email software with maximum severity RCE flaw
- **macOS Systems**: Targeted by GlassWorm malware through trojanized crypto wallet applications
- **Chrome Browser Extensions**: Trust Wallet and other extensions compromised via supply chain attacks
- **npm Registry**: JavaScript packages infected with modified Shai-Hulud worm payloads

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of legacy 2FA vulnerabilities in network appliances
- **Supply Chain Poisoning**: Malicious npm packages and browser extensions delivering backdoors
- **Social Engineering**: Phishing campaigns abusing Google Cloud Application Integration features
- **Botnet Operations**: RondoDox and Kimwolf botnets targeting IoT devices and local networks
- **Cryptocurrency Theft**: Long-term exploitation of stolen LastPass vault data for wallet compromise
- **Malware Distribution**: Trojanized applications targeting macOS developers and crypto users

## Threat Actor Activities

- **RondoDox Operators**: Nine-month campaign exploiting React2Shell to build IoT botnet infrastructure
- **Transparent Tribe**: New RAT attacks targeting Indian government and academic institutions
- **Shai-Hulud Attackers**: Modified worm variants testing new payloads on npm registry
- **GlassWorm Campaign**: Fourth wave targeting macOS developers with malicious VSCode extensions
- **DarkSpectre Group**: Browser extension campaigns impacting 8.8 million users across multiple operations
- **Kimwolf Botnet**: Network infiltration campaigns exploiting months-old vulnerabilities
- **LastPass Breach Exploiters**: Ongoing cryptocurrency thefts traced to 2022 data breach