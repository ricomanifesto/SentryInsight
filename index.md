# Exploitation Report

The cybersecurity landscape has experienced significant exploitation activity with Google tracking 90 zero-day vulnerabilities actively exploited in attacks throughout 2025, with nearly half targeting enterprise software and appliances. Critical vulnerabilities are being exploited across multiple platforms including Cisco SD-WAN systems, VMware Aria Operations, and FreeScout helpdesk platforms. Advanced threat actors including Iran-nexus groups and Russia's APT28 are deploying sophisticated malware campaigns targeting government entities, while the discovery of the Coruna iOS exploit kit demonstrates the evolution of mobile device targeting with 23 exploits spanning five attack chains.

## Active Exploitation Details

### Cisco SD-WAN Manager Vulnerabilities
- **Description**: Two security flaws in Cisco Catalyst SD-WAN Manager are being actively exploited by attackers in the wild
- **Impact**: Allows attackers to compromise SD-WAN infrastructure and potentially gain network access
- **Status**: Cisco has flagged these as actively exploited and is urging administrators to upgrade vulnerable devices

### VMware Aria Operations Command Injection Flaw
- **Description**: A command injection vulnerability in VMware Aria Operations platform
- **Impact**: Could grant attackers broad access to victims' cloud environments and resources
- **Status**: Currently being exploited in active attacks against cloud infrastructures

### FreeScout Mail2Shell Zero-Click Attack
- **Description**: A maximum severity vulnerability in the FreeScout helpdesk platform enabling zero-click remote code execution
- **Impact**: Allows complete server hijacking without any user interaction or authentication required
- **Status**: Active exploitation capability with no user interaction needed

### Coruna iOS Exploit Kit
- **Description**: A sophisticated exploit kit containing 23 iOS exploits across five attack chains targeting iPhone models
- **Impact**: Enables targeted espionage campaigns and financially motivated crypto theft attacks
- **Status**: Deployed by multiple threat actors targeting iOS versions 13.0 through 17.2.1

### Cisco Secure Firewall Management Center Flaws
- **Description**: Two maximum-severity vulnerabilities in Cisco Secure FMC software
- **Impact**: Provides attackers with root-level access to firewall management systems
- **Status**: Security updates released by Cisco to address these critical flaws

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Multiple versions affected by actively exploited vulnerabilities
- **VMware Aria Operations**: Cloud management platform vulnerable to command injection attacks
- **FreeScout Helpdesk Platform**: Mail processing functionality enabling zero-click attacks
- **Apple iOS Devices**: iPhone models running iOS versions 13.0 to 17.2.1 targeted by Coruna exploit kit
- **Cisco Secure Firewall Management Center**: FMC software versions with maximum severity vulnerabilities
- **Enterprise Software and Appliances**: Nearly half of the 90 tracked zero-days target enterprise systems

## Attack Vectors and Techniques

- **Zero-Click Exploitation**: FreeScout vulnerability requires no user interaction for successful compromise
- **Command Injection**: VMware Aria Operations flaw exploited through command injection techniques
- **Phishing Campaigns**: Multiple threat actors using sophisticated phishing to deliver malware payloads
- **Mobile Exploit Chains**: Coruna kit uses five different exploit chains for iOS device compromise
- **Adversary-in-the-Middle (AitM)**: Tycoon2FA platform facilitated large-scale credential harvesting attacks
- **Social Engineering**: LastPass users targeted with fake support email threads for vault password theft
- **Spear Phishing**: APT28 and Dust Specter campaigns using targeted phishing against government officials

## Threat Actor Activities

- **APT28 (Russia-linked)**: Deploying BadPaw loader and MeowMeow backdoor in campaigns targeting Ukrainian entities
- **Dust Specter (Iran-nexus)**: Targeting Iraqi government officials with SPLITDROP and GHOSTFORM malware while impersonating Ministry of Foreign Affairs
- **Phobos Ransomware Operation**: Russian administrator pleaded guilty to wire fraud conspiracy affecting hundreds of victims worldwide
- **Silver Dragon (China-linked)**: Part of APT41 nexus conducting cyber espionage against governments in EU and Southeast Asia using legitimate network services
- **Hacktivist Groups**: 149 DDoS attacks against 110 organizations across 16 countries following Middle East conflict escalation
- **Multiple Threat Actors**: Using Coruna iOS exploit kit for both espionage and financial crime targeting crypto assets
- **Cybercriminal Forums**: LeakBase platform with 142,000 members dismantled by FBI and Europol for trading stolen credentials and cybercrime tools