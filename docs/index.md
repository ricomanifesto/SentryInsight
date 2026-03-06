# Exploitation Report

Critical exploitation activity has escalated significantly with multiple high-severity vulnerabilities being actively exploited across various platforms. The most concerning developments include two Cisco Catalyst SD-WAN Manager vulnerabilities flagged as actively exploited, CVSS 9.8 rated vulnerabilities in Hikvision and Rockwell Automation products added to CISA's KEV catalog, and a maximum severity zero-click vulnerability in FreeScout helpdesk platform. Additionally, Google reported tracking 90 zero-day vulnerabilities exploited throughout 2025, with nearly half targeting enterprise software and appliances. WordPress sites are under attack through a critical vulnerability in the User Registration & Membership plugin, while sophisticated phishing campaigns continue to evolve with ClickFix operations using Windows Terminal to deploy Lumma Stealer malware.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two security flaws affecting Cisco Catalyst SD-WAN Manager (formerly SD-WAN vManage) that allow unauthorized access and control
- **Impact**: Attackers can gain administrative access to SD-WAN infrastructure and potentially compromise entire network segments
- **Status**: Actively exploited in the wild; patches available

### Hikvision and Rockwell Automation Critical Vulnerabilities
- **Description**: Critical security flaws with CVSS 9.8 severity ratings affecting industrial control systems and video surveillance equipment
- **Impact**: Complete system compromise with potential for remote code execution and unauthorized access
- **Status**: Added to CISA KEV catalog due to active exploitation; immediate patching required

### FreeScout Helpdesk Platform Zero-Click Vulnerability
- **Description**: Maximum severity vulnerability enabling remote code execution without any user interaction or authentication requirements
- **Impact**: Complete server compromise through zero-click attack vector, allowing full control of mail servers
- **Status**: Actively exploited; immediate patching critical

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in plugin installed on over 60,000 WordPress sites allowing unauthorized administrative access
- **Impact**: Attackers can create admin accounts and gain full control of WordPress installations
- **Status**: Actively exploited; affects significant number of websites

### VMware Aria Operations Command Injection Flaw
- **Description**: Command injection vulnerability in VMware Aria Operations cloud management platform
- **Impact**: Broad access to victims' cloud environments and infrastructure
- **Status**: Currently being exploited; cloud resources at significant risk

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network infrastructure management systems vulnerable to unauthorized access
- **Hikvision Video Surveillance Systems**: Industrial security cameras and monitoring equipment
- **Rockwell Automation Industrial Control Systems**: Manufacturing and industrial automation platforms
- **FreeScout Helpdesk Platform**: Customer support and ticketing systems
- **WordPress Sites**: Over 60,000 websites using User Registration & Membership plugin
- **VMware Aria Operations**: Cloud infrastructure management and monitoring platforms
- **Enterprise Software and Appliances**: Nearly half of the 90 tracked zero-day exploits target enterprise environments

## Attack Vectors and Techniques

- **Zero-Click Exploitation**: Mail2Shell attacks against FreeScout servers requiring no user interaction
- **Social Engineering**: ClickFix campaigns using Windows Terminal to deploy malware payloads
- **Privilege Escalation**: WordPress plugin exploitation to create unauthorized admin accounts
- **Network Infrastructure Compromise**: SD-WAN manager exploitation for network-wide access
- **Command Injection**: VMware Aria Operations attacks enabling cloud environment compromise
- **Phishing-as-a-Service**: Tycoon 2FA platform facilitating large-scale credential theft operations
- **Self-Propagating Attacks**: JavaScript worms targeting Wikipedia and similar platforms

## Threat Actor Activities

- **UAT-9244 (Chinese APT)**: Targeting South American telecommunications providers since 2024 with new malware toolkit affecting Windows, Linux, and network-edge devices
- **APT28 (Russian)**: Deploying BadPaw loader and MeowMeow backdoor in campaigns targeting Ukrainian entities
- **APT36 (Pakistani)**: Utilizing AI-powered malware development techniques to scale malware production
- **Dust Specter (Iran-linked)**: Targeting Iraqi government officials with SPLITDROP and GHOSTFORM malware while impersonating Ministry of Foreign Affairs
- **ClickFix Campaign Operators**: Conducting widespread social engineering campaigns using Windows Terminal to deploy Lumma Stealer
- **Phobos Ransomware Operation**: International cybercriminal network with Russian administrator recently pleading guilty to wire fraud conspiracy