# Exploitation Report

Current threat landscape reveals sophisticated exploitation campaigns targeting critical infrastructure and supply chain vulnerabilities. North Korean threat actors are conducting large-scale credential harvesting operations exploiting Next.js vulnerabilities, while China-aligned groups target European governments with PlugX malware and OAuth-based phishing. Supply chain attacks continue to pose significant risks, with social engineering campaigns successfully compromising popular npm packages like Axios. Mobile platforms face new threats from SparkCat malware variants infiltrating both iOS and Android app stores, targeting cryptocurrency wallet recovery phrases. Web-based attacks are evolving with cookie-controlled PHP web shells providing persistent access to Linux servers, while ransomware groups like Qilin continue to target political organizations with multi-extortion tactics.

## Active Exploitation Details

### React2Shell Vulnerability
- **Description**: A critical vulnerability in Next.js framework allowing remote code execution and credential harvesting
- **Impact**: Attackers can steal database credentials, SSH private keys, and Amazon Web Services credentials from compromised hosts
- **Status**: Actively exploited in large-scale operations affecting 766 Next.js hosts
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Exploit
- **Description**: A severe mobile OS-cracking tool targeting iOS systems
- **Impact**: Complete compromise of iOS devices, allowing unauthorized access to device data and functionality
- **Status**: Recently patched by Apple in iOS 18 update, breaking precedent for emergency patches

### Cookie-Controlled PHP Web Shells
- **Description**: Sophisticated web shells using HTTP cookies as control channels on Linux servers
- **Impact**: Remote code execution capabilities with persistent access through cron job scheduling
- **Status**: Actively deployed by threat actors for maintaining long-term access to compromised systems

## Affected Systems and Products

- **Next.js Framework**: 766 hosts confirmed compromised in credential harvesting campaign
- **iOS Devices**: All versions prior to iOS 18 vulnerable to DarkSword exploit toolkit
- **Linux Servers**: PHP-enabled web servers targeted with cookie-controlled web shells
- **Axios npm Package**: Popular JavaScript HTTP client compromised through supply chain attack
- **Drift Protocol**: Solana-based decentralized exchange losing $285 million in security incident
- **European Commission Cloud**: 30 EU entities' data exposed in TeamPCP breach
- **Zendesk Platform**: Third-party support ticket system breach affecting Hims & Hers customers
- **Die Linke Political Party**: German political organization hit by Qilin ransomware

## Attack Vectors and Techniques

- **Supply Chain Social Engineering**: North Korean UNC1069 group targeting npm package maintainers with sophisticated phishing campaigns
- **OAuth-Based Phishing**: China-aligned TA416 using legitimate OAuth flows to bypass security controls
- **Durable Nonce Attacks**: DPRK-linked actors exploiting Solana blockchain vulnerabilities for financial theft
- **Mobile App Store Infiltration**: SparkCat malware variants successfully passing app store review processes
- **Residential Proxy Networks**: 78% evasion rate against IP reputation systems across 4 billion sessions
- **Multi-Extortion Ransomware**: Combined encryption and data theft tactics for increased pressure on victims
- **Insider Threat Exploitation**: System administrators using privileged access for extortion attempts

## Threat Actor Activities

- **UNC1069 (North Korea)**: Conducting sophisticated social engineering campaigns against open-source maintainers, successfully compromising Axios npm package through targeted phishing
- **TA416 (China)**: Targeting European government and diplomatic organizations with PlugX malware deployment and OAuth-based credential harvesting since mid-2025
- **TeamPCP**: Large-scale supply chain attacks affecting European Commission and multiple EU entities, with expanding blast radius amid hacker infighting
- **Qilin Ransomware Group**: Targeting political organizations with data theft and system encryption, confirmed attack against German political party Die Linke
- **DPRK-linked Actors**: Financial-motivated attacks against cryptocurrency platforms, successfully draining $285 million from Drift Protocol through Security Council compromise
- **ShinyHunters and Lapsus$**: Claiming credit for various breaches related to TeamPCP activities, creating confusion in attribution and response efforts