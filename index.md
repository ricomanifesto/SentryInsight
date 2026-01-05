# Exploitation Report

Critical exploitation activity is dominated by several significant ongoing campaigns targeting diverse infrastructure. The Fortinet 2FA bypass vulnerability remains under active exploitation with over 10,000 internet-exposed firewalls still vulnerable to attacks. The RondoDox botnet has been conducting a persistent nine-month campaign exploiting the React2Shell flaw to hijack IoT devices and web servers. Supply chain attacks continue to pose severe threats, with the Shai-Hulud worm variants targeting npm packages and Trust Wallet's Chrome extension compromise resulting in $8.5 million in cryptocurrency theft. Additionally, the Transparent Tribe threat actor has launched new RAT attacks against Indian government and academic institutions, while the ongoing LastPass breach continues to enable cryptocurrency thefts years after the initial compromise.

## Active Exploitation Details

### Fortinet 2FA Bypass Vulnerability
- **Description**: A five-year-old two-factor authentication bypass vulnerability affecting Fortinet firewalls
- **Impact**: Allows attackers to bypass 2FA protections and gain unauthorized access to network infrastructure
- **Status**: Actively exploited with over 10,000 internet-exposed firewalls remaining vulnerable

### React2Shell Critical Flaw
- **Description**: Critical vulnerability being exploited by the RondoDox botnet to compromise IoT devices and web servers
- **Impact**: Enables remote hijacking of IoT devices and web applications for botnet enrollment
- **Status**: Under active exploitation in a persistent nine-month campaign

### SmarterMail Remote Code Execution
- **Description**: Maximum-severity security flaw in SmarterTools SmarterMail email software
- **Impact**: Allows attackers to achieve remote code execution on vulnerable email servers
- **Status**: Critical vulnerability with CSA issuing active exploitation warnings
- **CVE ID**: CVE-2025-13915

### IBM API Connect Authentication Bypass
- **Description**: Critical authentication system vulnerability in IBM API Connect
- **Impact**: Allows attackers to gain remote access to API management applications
- **Status**: Newly disclosed critical vulnerability requiring immediate patching
- **CVE ID**: CVE-2025-13915

## Affected Systems and Products

- **Fortinet Firewalls**: Over 10,000 internet-exposed devices vulnerable to 2FA bypass attacks
- **IoT Devices and Web Servers**: Targeted by RondoDox botnet through React2Shell exploitation
- **SmarterTools SmarterMail**: Email software vulnerable to remote code execution
- **IBM API Connect**: API management platform with critical authentication bypass
- **macOS Systems**: Targeted by GlassWorm campaign through trojanized crypto wallet applications
- **Trust Wallet Chrome Extension**: Compromised leading to $8.5 million cryptocurrency theft
- **npm Registry**: Targeted by modified Shai-Hulud worm variants
- **Unleash Protocol**: Decentralized platform lost $3.9 million through multisig hijack
- **LastPass Encrypted Vaults**: Ongoing exploitation enabling cryptocurrency theft

## Attack Vectors and Techniques

- **2FA Bypass**: Direct exploitation of authentication mechanisms in Fortinet firewalls
- **Botnet Enrollment**: IoT device compromise through React2Shell vulnerability exploitation
- **Supply Chain Attacks**: NPM package poisoning through Shai-Hulud worm variants
- **Browser Extension Compromise**: Malicious updates to legitimate Chrome extensions
- **Trojanized Applications**: Malicious VSCode/OpenVSX extensions delivering compromised crypto wallets
- **Multisig Hijacking**: Unauthorized contract upgrades enabling asset withdrawal
- **Remote Access Trojan Deployment**: Email-based delivery of RATs targeting government entities
- **Encrypted Vault Exploitation**: Long-term cryptocurrency theft from compromised password managers

## Threat Actor Activities

- **ShinyHunters**: Claims to have breached Resecurity systems, though firm reports it was a honeypot operation
- **Transparent Tribe**: Launching new RAT attacks against Indian governmental, academic, and strategic entities
- **RondoDox Operators**: Conducting persistent nine-month botnet campaign targeting IoT infrastructure
- **Shai-Hulud Attackers**: Developing modified worm variants for npm registry exploitation and supply chain attacks
- **GlassWorm Campaign**: Fourth wave targeting macOS developers with malicious development tools
- **DarkSpectre Group**: Attributed to multiple browser extension campaigns affecting 8.8 million users globally
- **LastPass Breach Actors**: Continuing to exploit 2022 breach data for ongoing cryptocurrency thefts
- **Chinese APT Groups**: Historical exploitation of Ivanti EPMM zero-day vulnerabilities affecting thousands of organizations