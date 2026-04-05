# Exploitation Report

Critical exploitation activity is currently dominated by several active campaigns targeting enterprise infrastructure and supply chain components. Most notably, attackers are exploiting the React2Shell vulnerability in Next.js applications for automated credential theft, while FortiClient EMS systems face active exploitation requiring emergency patches. The threat landscape is further complicated by sophisticated supply chain attacks targeting popular npm packages, North Korean-linked social engineering campaigns against major JavaScript libraries, and widespread device code phishing attacks that have surged dramatically. These attacks demonstrate a clear shift toward targeting foundational software components and authentication mechanisms that underpin modern enterprise environments.

## Active Exploitation Details

### React2Shell in Next.js Applications
- **Description**: A vulnerability in Next.js applications that allows attackers to execute automated credential theft campaigns
- **Impact**: Large-scale automated credential harvesting from vulnerable web applications
- **Status**: Currently being exploited in active campaigns
- **CVE ID**: CVE-2025-55182

### FortiClient EMS Critical Flaw
- **Description**: A critical security vulnerability in Fortinet's FortiClient Enterprise Management Server
- **Impact**: Allows attackers to gain unauthorized access to enterprise endpoint management infrastructure
- **Status**: Actively exploited in the wild, emergency patches released by Fortinet
- **CVE ID**: CVE-2026-35616

### DarkSword iOS Exploitation Tool
- **Description**: A severe mobile OS-cracking tool targeting iOS systems
- **Impact**: Complete compromise of iOS devices and data extraction capabilities
- **Status**: Apple has broken precedent by patching this vulnerability in iOS 18

## Affected Systems and Products

- **Next.js Applications**: Web applications using vulnerable Next.js frameworks susceptible to React2Shell attacks
- **FortiClient EMS**: Enterprise management servers for Fortinet endpoint security solutions
- **npm Package Registry**: 36 malicious packages disguised as Strapi CMS plugins targeting Redis and PostgreSQL databases
- **iOS Mobile Devices**: Apple mobile devices running iOS versions prior to recent patches
- **Axios HTTP Client**: Popular JavaScript library compromised through social engineering of maintainer accounts
- **Linux Servers**: Web servers running PHP applications vulnerable to cookie-controlled web shell attacks

## Attack Vectors and Techniques

- **Social Engineering**: Sophisticated campaigns targeting software maintainers with fake Microsoft Teams error fixes and technical support requests
- **Supply Chain Compromise**: Malicious npm packages and compromised popular JavaScript libraries
- **Device Code Phishing**: OAuth 2.0 Device Authorization Grant flow abuse showing 37x increase in attacks
- **Cookie-Controlled Web Shells**: PHP-based backdoors using HTTP cookies for command and control on Linux servers
- **Automated Credential Harvesting**: Large-scale automated attacks targeting web application authentication systems

## Threat Actor Activities

- **UNC1069 (North Korean)**: Orchestrated sophisticated social engineering campaign against Axios maintainer, leading to npm supply chain attack
- **TeamPCP**: Responsible for European Commission cloud hack exposing data from 30 EU entities
- **TA416 (China-aligned)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **DPRK-linked Groups**: Conducting social engineering attacks against cryptocurrency platforms, including $285 million theft from Drift exchange
- **Qilin Ransomware Group**: Claimed responsibility for attack against German political party Die Linke
- **SparkCat Operators**: Deploying new malware variants on Apple App Store and Google Play Store targeting cryptocurrency wallet recovery phrases