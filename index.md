# Exploitation Report

The current threat landscape reveals several critical vulnerabilities actively exploited in the wild, with attackers targeting enterprise infrastructure and mobile platforms. Most concerning is the active exploitation of CVE-2026-22719, a VMware Aria Operations command injection flaw that CISA has flagged as exploited in attacks. Additionally, sophisticated threat actors are leveraging the Coruna iOS exploit kit containing 23 exploits across five chains targeting iOS versions 13-17.2.1, while FreeScout helpdesk platforms face zero-click attacks enabling complete system compromise. Commercial spyware operators are exploiting CVE-2026-21385, a Qualcomm zero-day vulnerability in targeted Android attacks.

## Active Exploitation Details

### VMware Aria Operations Command Injection Vulnerability
- **Description**: A command injection flaw in VMware Aria Operations allowing remote code execution
- **Impact**: Attackers can gain broad access to victims' cloud environments and execute arbitrary commands
- **Status**: Actively exploited in the wild, patches available from Broadcom VMware
- **CVE ID**: CVE-2026-22719

### FreeScout Mail2Shell Zero-Click Attack
- **Description**: Maximum severity vulnerability in FreeScout helpdesk platform enabling remote code execution
- **Impact**: Complete server hijacking without any user interaction or authentication required
- **Status**: Zero-click exploitation reported, allowing full system compromise

### Coruna iOS Exploit Kit
- **Description**: Previously undocumented set of 23 iOS exploits deployed across five exploitation chains
- **Impact**: Enables spyware deployment, cryptocurrency theft, and complete device compromise
- **Status**: Actively used by multiple threat actors in espionage and financially motivated attacks

### Qualcomm Zero-Day Android Vulnerability
- **Description**: High-severity memory corruption flaw in Qualcomm components
- **Impact**: Enables targeted surveillance and device compromise on Android devices
- **Status**: Actively exploited in targeted attacks by suspected commercial spyware or nation-state actors
- **CVE ID**: CVE-2026-21385

### Cisco Secure FMC Maximum Severity Flaws
- **Description**: Two maximum-severity vulnerabilities in Cisco Secure Firewall Management Center software
- **Impact**: Attackers can gain root access to affected systems
- **Status**: Security updates released by Cisco to address the flaws

## Affected Systems and Products

- **VMware Aria Operations**: Cloud management platform vulnerable to command injection attacks
- **FreeScout Helpdesk Platform**: Open-source customer support platform susceptible to zero-click compromise
- **iOS Devices**: iPhones running iOS versions 13.0 through 17.2.1 targeted by Coruna exploit kit
- **Android Devices**: Devices with Qualcomm components affected by memory corruption vulnerability
- **Cisco Secure FMC**: Firewall management systems at risk of root-level compromise
- **HungerRush POS Systems**: Restaurant point-of-sale platforms targeted in extortion campaigns

## Attack Vectors and Techniques

- **Zero-Click Exploitation**: Mail2Shell attacks require no user interaction to compromise FreeScout servers
- **Command Injection**: VMware Aria Operations vulnerability exploited through malicious command execution
- **Mobile Exploit Chains**: Coruna kit uses sophisticated multi-stage exploitation targeting iOS devices
- **Memory Corruption**: Qualcomm vulnerability exploited through memory manipulation techniques
- **OAuth Abuse**: Hackers manipulating legitimate OAuth redirection mechanisms to bypass security protections
- **Fake Tech Support**: Attackers impersonating IT support to deploy Havoc C2 framework
- **Package Repository Poisoning**: Malicious Laravel packages deployed via Packagist to distribute RATs

## Threat Actor Activities

- **APT41-Linked Silver Dragon**: Targeting government entities in Europe and Southeast Asia using Cobalt Strike and Google Drive for command and control
- **Commercial Spyware Operators**: Exploiting Qualcomm zero-day in targeted Android surveillance campaigns
- **Cryptocurrency Theft Groups**: Using Coruna iOS exploit kit for financial crimes targeting crypto wallets
- **Nation-State Actors**: Suspected involvement in Qualcomm zero-day exploitation for espionage purposes
- **Sloppy Lemming (Indian APT)**: Targeting defense and critical infrastructure with custom Rust-coded tools and cloud-based C2
- **Hacktivist Groups**: Conducting 149 DDoS attacks against 110 organizations across 16 countries following Middle East conflicts
- **Ransomware Operators**: Utilizing RDP brute-force attacks and geo-distributed VPN infrastructure for deployment
- **Phishing-as-a-Service Providers**: Tycoon2FA platform disrupted after facilitating tens of millions of phishing messages monthly