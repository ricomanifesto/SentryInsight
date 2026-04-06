# Exploitation Report

Critical vulnerability exploitation activity continues to escalate with multiple high-impact threats being actively leveraged by cybercriminals. The most significant exploitation involves CVE-2026-35616, a critical FortiClient Enterprise Management Server vulnerability that prompted emergency patching and CISA directive for federal agencies. Storm-1175, a China-based financially motivated group linked to Medusa ransomware, has been deploying both n-day and zero-day exploits in high-velocity attacks. Additional active exploitation includes React2Shell vulnerability CVE-2025-55182 being used in automated credential harvesting campaigns, while ransomware groups Qilin and Warlock are employing vulnerable driver exploitation techniques to disable over 300 EDR security tools.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: Critical security flaw in FortiClient Enterprise Management Server that allows attackers to compromise enterprise management infrastructure
- **Impact**: Complete compromise of FortiClient EMS instances, enabling attackers to gain control over enterprise endpoint management systems
- **Status**: Actively exploited in the wild; emergency patches released by Fortinet; CISA ordered federal agencies to patch by Friday
- **CVE ID**: CVE-2026-35616

### React2Shell Vulnerability
- **Description**: Security flaw in Next.js applications that enables remote code execution through React server components
- **Impact**: Automated credential harvesting, extraction of secrets, and system data exfiltration from vulnerable web applications
- **Status**: Actively exploited by threat cluster UAT-10608 in large-scale automated campaigns
- **CVE ID**: CVE-2025-55182

### Zero-Day and N-Day Exploits by Storm-1175
- **Description**: Multiple zero-day and recently patched vulnerabilities being exploited by China-based cybercriminal group
- **Impact**: Deployment of Medusa ransomware payloads and high-velocity attack campaigns against various targets
- **Status**: Active exploitation ongoing with high-velocity deployment patterns

### Vulnerable Driver Exploitation (BYOVD)
- **Description**: Bring Your Own Vulnerable Driver technique used to load malicious drivers and bypass security controls
- **Impact**: Complete disabling of 300+ EDR tools and security solutions, enabling ransomware deployment
- **Status**: Actively used by Qilin and Warlock ransomware operations

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: All versions prior to emergency patch release, particularly impacting federal agencies and enterprise environments
- **Next.js Applications**: Web-exposed applications vulnerable to React2Shell exploitation
- **Enterprise EDR Solutions**: Over 300 endpoint detection and response tools targeted by BYOVD attacks
- **Redis and PostgreSQL**: Database systems targeted by malicious npm packages for persistent implant deployment
- **Chrome Extensions**: Over 6,000 Chrome extensions being scanned and monitored for data collection
- **Mobile iOS Devices**: iOS 18 systems affected by DarkSword vulnerability requiring Apple's emergency patch

## Attack Vectors and Techniques

- **Automated Exploitation**: Large-scale automated tools used for React2Shell vulnerability exploitation and credential harvesting
- **Social Engineering**: Six-month sophisticated social engineering operations, including fake Microsoft Teams error scenarios
- **Supply Chain Attacks**: Malicious npm packages disguised as legitimate Strapi CMS plugins
- **BYOVD Technique**: Loading vulnerable legitimate drivers to disable security tools and deploy ransomware
- **OAuth Device Code Phishing**: 37x surge in device code phishing attacks abusing OAuth 2.0 flows
- **QR Code Phishing**: Traffic violation scams switching to QR code-based phishing in text messages

## Threat Actor Activities

- **Storm-1175**: China-based financially motivated group deploying Medusa ransomware through zero-day and n-day exploits in high-velocity campaigns
- **DPRK-Linked Groups**: Using GitHub as command-and-control infrastructure for multi-stage attacks targeting South Korean organizations
- **UAT-10608**: Emerging threat cluster conducting automated credential harvesting campaigns exploiting React2Shell
- **Qilin Ransomware**: Employing BYOVD techniques to disable EDR tools and conducting attacks against political organizations including Die Linke German political party
- **Warlock Ransomware**: Utilizing vulnerable driver exploitation to silence security tools on compromised hosts
- **REvil/GandCrab Leaders**: German authorities identified key figures including 31-year-old Russian Daniil Maksimov ("UNKN") behind major ransomware operations
- **TA416**: China-aligned threat actor targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025