# Exploitation Report

The cybersecurity landscape is currently experiencing a wave of critical zero-day exploitations, with threat actors actively targeting enterprise infrastructure through multiple attack vectors. Most notably, Cisco firewall devices are under active attack through CVE-2025-10023 and CVE-2025-10033, prompting CISA to issue emergency directives. Additionally, a maximum severity vulnerability CVE-2025-10035 in Fortra's GoAnywhere MFT platform is being exploited as a zero-day, allowing remote command injection without authentication. Nation-state actors, including Iranian APT groups and Russian COLDRIVER, are deploying sophisticated malware campaigns while Chinese APT group UNC5221 is targeting edge devices with backdoor operations.

## Active Exploitation Details

### Cisco Secure Firewall ASA Zero-Day Vulnerabilities
- **Description**: Two critical vulnerabilities affecting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Threat actors can deploy RayInitiator and LINE VIPER malware, compromise network infrastructure, and establish persistent access to enterprise environments
- **Status**: Actively exploited in the wild, patches available, CISA emergency directive issued
- **CVE ID**: CVE-2025-10023, CVE-2025-10033

### Fortra GoAnywhere MFT Command Injection
- **Description**: Maximum severity vulnerability in Fortra's GoAnywhere Managed File Transfer software allowing remote command injection
- **Impact**: Attackers can inject commands remotely without authentication, potentially leading to complete system compromise
- **Status**: Actively exploited as zero-day approximately one week before public disclosure, patches now available
- **CVE ID**: CVE-2025-10035

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce AI agent platform susceptible to indirect prompt injection attacks
- **Impact**: Attackers can exfiltrate sensitive CRM data through AI prompt manipulation, exposing customer information and business data
- **Status**: Recently patched by Salesforce following responsible disclosure

## Affected Systems and Products

- **Cisco Secure Firewall ASA**: All versions running VPN web server functionality
- **Cisco Secure Firewall Threat Defense (FTD)**: Devices with ASA software components
- **Fortra GoAnywhere MFT**: Managed File Transfer software installations
- **Salesforce Agentforce**: AI agent platform and associated CRM integrations
- **macOS Systems**: Targeting Xcode developers through XCSSET malware variants
- **Microsoft Edge**: Browsers vulnerable to malicious sideloaded extensions
- **NPM Package Ecosystem**: Users of unofficial 'postmark-mcp' package

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in enterprise infrastructure
- **Supply Chain Attacks**: Compromising third-party vendors to access primary targets, as seen in Volvo case
- **Phishing Campaigns**: SVG-based phishing targeting Ukrainian government agencies and Vietnamese entities
- **Malicious NPM Packages**: Supply chain compromise through trojanized Node.js packages
- **AI Prompt Injection**: Indirect prompt manipulation to extract sensitive data from AI systems
- **Code Signing Certificate Abuse**: Iranian threat actors using legitimate SSL.com certificates to sign malware
- **Browser Extension Sideloading**: Deployment of malicious extensions in Microsoft Edge

## Threat Actor Activities

- **Iranian APT Groups**: Charming Kitten's Subtle Snail offshoot deploying malware signed with legitimate certificates from SSL.com
- **Russian COLDRIVER APT**: Conducting ClickFix-style attacks delivering BO Team and Bearlyfy lightweight malware families
- **Chinese APT UNC5221**: Deploying "Brickstorm" backdoors on network edge devices that cannot run traditional EDR agents
- **Scattered Spider**: Responsible for £80 million ($107 million) in losses to U.K.'s Co-operative Group
- **Vane Viper**: Operating global malware and ad fraud network generating over 1 trillion DNS queries
- **Unknown Nation-State Actor**: Previously linked to "ArcaneDoor" campaign, now targeting Cisco infrastructure with multiple zero-days