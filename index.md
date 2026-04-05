# Exploitation Report

Current cybersecurity threats demonstrate a sophisticated landscape of active exploitation targeting enterprise infrastructure and supply chains. Critical vulnerabilities in FortiClient EMS (CVE-2026-35616) are being actively exploited in the wild, while threat actors are leveraging social engineering campaigns to compromise popular npm packages including Axios. Large-scale attacks against Next.js applications (CVE-2025-55182) have successfully breached hundreds of hosts for credential harvesting. Additionally, North Korean threat groups are conducting targeted social engineering operations against cryptocurrency platforms and software maintainers, resulting in significant financial losses and supply chain compromises.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: Critical security flaw in Fortinet's FortiClient Enterprise Management Server requiring out-of-band patches
- **Impact**: Active exploitation allowing unauthorized access to enterprise management systems
- **Status**: Patches released by Fortinet, actively exploited in the wild
- **CVE ID**: CVE-2026-35616

### Next.js React2Shell Vulnerability
- **Description**: Large-scale exploitation of React2Shell vulnerability targeting Next.js applications
- **Impact**: Credential harvesting operation stealing database credentials, SSH private keys, and Amazon Web Services access keys
- **Status**: 766 Next.js hosts successfully breached
- **CVE ID**: CVE-2025-55182

### Malicious npm Package Campaign
- **Description**: 36 malicious packages disguised as Strapi CMS plugins deployed to exploit Redis and PostgreSQL databases
- **Impact**: Deployment of persistent implants and database exploitation
- **Status**: Active campaign targeting npm ecosystem

## Affected Systems and Products

- **FortiClient EMS**: Enterprise management server infrastructure requiring immediate patching
- **Next.js Applications**: Web applications vulnerable to React2Shell exploitation
- **npm Registry**: 36 malicious packages targeting Redis and PostgreSQL databases
- **Axios HTTP Client**: Popular JavaScript library compromised through social engineering
- **iOS Applications**: SparkCat malware variants targeting cryptocurrency wallet recovery phrases
- **Linux Servers**: PHP web shells using HTTP cookies for command and control persistence
- **Solana DeFi Platform**: Drift exchange losing $285 million through social engineering attacks

## Attack Vectors and Techniques

- **Social Engineering**: Sophisticated campaigns targeting software maintainers and platform administrators
- **Supply Chain Attacks**: Compromising popular open-source packages and dependencies
- **Credential Harvesting**: Large-scale operations stealing authentication materials and access keys
- **Cookie-Controlled Web Shells**: PHP-based persistence mechanisms on Linux servers using HTTP cookies
- **Device Code Phishing**: OAuth 2.0 Device Authorization Grant flow abuse with 37x increase in attacks
- **Durable Nonce Attacks**: Advanced cryptocurrency theft techniques targeting DeFi platforms

## Threat Actor Activities

- **UNC1069**: North Korean threat group conducting social engineering against Axios maintainers and cryptocurrency platforms
- **TA416**: China-aligned group targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing
- **TeamPCP**: Supply chain attack group responsible for European Commission breach affecting 30 EU entities
- **Qilin Ransomware**: Active against political organizations including German political party Die Linke
- **DPRK-Linked Groups**: Multiple North Korean actors conducting cryptocurrency theft and software supply chain attacks
- **ShinyHunters and Lapsus$**: Opportunistic groups claiming credit for TeamPCP-related breaches