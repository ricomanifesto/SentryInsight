# Exploitation Report

Critical exploitation activity is currently targeting multiple attack surfaces, with threat actors exploiting vulnerabilities in Fortinet firewalls, IBM API Connect authentication systems, and leveraging supply chain attacks through compromised browser extensions and npm packages. The most severe immediate threats include over 10,000 internet-exposed Fortinet firewalls vulnerable to a five-year-old 2FA bypass exploit that remains actively exploited, and a critical IBM API Connect authentication flaw with a CVSS 9.8 rating. Additionally, sophisticated supply chain attacks like Shai-Hulud continue to evolve, with new variants targeting npm registries and browser extensions, resulting in millions of dollars in cryptocurrency theft and affecting millions of users worldwide through malicious browser extension campaigns.

## Active Exploitation Details

### Fortinet Firewall 2FA Bypass Vulnerability
- **Description**: A five-year-old two-factor authentication bypass vulnerability in Fortinet firewalls that allows attackers to circumvent security controls
- **Impact**: Attackers can gain unauthorized access to protected systems by bypassing 2FA mechanisms
- **Status**: Actively exploited in the wild with over 10,000 internet-exposed devices still vulnerable

### IBM API Connect Authentication Flaw
- **Description**: Critical security flaw in IBM API Connect authentication system that enables remote access exploitation
- **Impact**: Attackers can gain remote access to the API Connect application and potentially compromise connected systems
- **Status**: Critical vulnerability requiring immediate patching
- **CVE ID**: CVE-2025-13915

### React2Shell Critical Vulnerability
- **Description**: Critical flaw being exploited by the RondoDox botnet to compromise IoT devices and web servers
- **Impact**: Enables hijacking of IoT devices and web applications for botnet enrollment
- **Status**: Under active exploitation for nine months in persistent campaign

### Trust Wallet Chrome Extension Compromise
- **Description**: Vulnerability in Trust Wallet's Chrome extension that was exploited through the Shai-Hulud supply chain attack
- **Impact**: Resulted in theft of approximately $8.5 million from over 2,500 cryptocurrency wallets
- **Status**: Compromised extension linked to industry-wide npm supply chain attack

## Affected Systems and Products

- **Fortinet Firewalls**: Over 10,000 internet-exposed devices remain vulnerable to 2FA bypass attacks
- **IBM API Connect**: Authentication system affected by critical remote access vulnerability
- **IoT Devices and Web Servers**: Targeted by RondoDox botnet through React2Shell exploitation
- **Trust Wallet Chrome Extension**: Compromised through Shai-Hulud supply chain attack affecting 2,500+ wallets
- **Browser Extensions**: DarkSpectre campaigns impacted 8.8 million users through malicious extensions
- **macOS Systems**: Targeted by GlassWorm malware campaign using trojanized crypto wallet applications
- **npm Registry**: Affected by modified Shai-Hulud worm variants for supply chain attacks
- **Discord Platforms**: Targeted by VVS Stealer malware for credential harvesting

## Attack Vectors and Techniques

- **Two-Factor Authentication Bypass**: Exploitation of legacy Fortinet firewall vulnerabilities to circumvent 2FA
- **Supply Chain Attacks**: Shai-Hulud variants targeting npm packages and browser extensions for widespread compromise
- **Remote Access Exploitation**: Critical IBM API Connect authentication bypass enabling remote system access
- **Botnet Enrollment**: RondoDox using React2Shell exploits for persistent IoT device compromise
- **Trojanized Applications**: GlassWorm campaign delivering malicious crypto wallets through VSCode/OpenVSX extensions
- **Information Stealing**: VVS Stealer using obfuscated Python code to harvest Discord credentials and tokens
- **Phishing Campaigns**: Multi-stage attacks abusing Google Cloud email features for credential theft
- **Browser Extension Manipulation**: Large-scale campaigns affecting millions through malicious browser add-ons

## Threat Actor Activities

- **RondoDox Operators**: Conducting nine-month persistent campaign targeting IoT devices and web servers through React2Shell exploitation
- **Transparent Tribe**: Launching new RAT attacks against Indian government and academic institutions with remote access trojans
- **DarkSpectre Threat Actor**: Operating multiple browser extension campaigns (ShadyPanda, GhostPoster, DarkSpectre) affecting 8.8 million users
- **Shai-Hulud Operators**: Evolving supply chain attack methods with modified variants targeting npm registry and browser extensions
- **GlassWorm Campaign**: Fourth wave targeting macOS developers with trojanized cryptocurrency wallet applications
- **ShinyHunters Group**: Claiming breach of cybersecurity firm Resecurity, though disputed as honeypot access
- **Kimwolf Botnet Operators**: Targeting local networks through vulnerability exploitation for months
- **VVS Stealer Developers**: Creating Python-based information stealers specifically targeting Discord users and credentials