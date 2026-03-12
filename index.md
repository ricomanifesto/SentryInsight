# Exploitation Report

Current exploitation activity reveals several critical threats targeting diverse systems and platforms. The most significant concern is the active exploitation of an n8n workflow automation platform vulnerability, which CISA has added to its Known Exploited Vulnerabilities catalog due to confirmed attacks in the wild, with approximately 24,700 exposed instances remaining vulnerable. Additionally, threat actors are leveraging supply chain attacks through malicious NPM packages, compromising CI/CD pipelines to steal developer credentials, while ransomware groups continue targeting healthcare infrastructure and medical technology companies. Microsoft's March 2026 Patch Tuesday addressed 79 vulnerabilities including two publicly disclosed zero-day flaws, and multiple Android malware families are actively targeting financial applications and cryptocurrency wallets.

## Active Exploitation Details

### n8n Workflow Automation Platform RCE Vulnerability
- **Description**: Critical remote code execution flaw in n8n workflow automation platform allowing arbitrary command execution
- **Impact**: Attackers can execute arbitrary commands on affected systems and potentially expose stored credentials
- **Status**: Actively exploited in the wild, patches available, CISA has ordered federal agencies to remediate

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities affecting Windows operating systems and Microsoft software
- **Impact**: Various impacts depending on specific vulnerabilities, allowing potential system compromise
- **Status**: Publicly known but patches released in March 2026 Patch Tuesday update

### Elementor Ally WordPress Plugin SQL Injection
- **Description**: SQL injection vulnerability in Elementor's Ally WordPress plugin for web accessibility
- **Impact**: Attackers can steal sensitive data from affected WordPress sites without authentication
- **Status**: Vulnerability disclosed, affects over 250,000 WordPress installations

### nx NPM Package Supply Chain Compromise
- **Description**: Supply chain attack targeting the nx NPM package that compromised developer environments
- **Impact**: Complete AWS cloud environment compromise achieved within 72 hours using stolen keys
- **Status**: Previously exploited by UNC6426 threat actor, ongoing campaign effects

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Approximately 24,700 instances remain exposed globally
- **WordPress Sites**: Over 250,000 sites using Elementor Ally plugin vulnerable to SQL injection
- **Microsoft Windows**: Various versions affected by 79 vulnerabilities including 2 zero-days
- **Android Devices**: Multiple malware families targeting banking apps, Pix payments, and crypto wallets
- **NPM Ecosystem**: JavaScript developers targeted through 88 malicious packages in PhantomRaven campaign
- **Rust Development Environment**: Five malicious Rust crates targeting CI/CD pipelines
- **GitHub Actions**: Xygeni's security action compromised via tag poisoning attack
- **Salesforce Cloud**: Misconfigured guest user permissions exposing sensitive client data
- **Healthcare Systems**: Medical facilities in Australia, New Zealand, and Tonga targeted by INC ransomware
- **Stryker Medical Technology**: Systems offline following Iran-linked wiper malware attack

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of n8n platform vulnerabilities for system compromise
- **Supply Chain Attacks**: Malicious packages in NPM and Rust ecosystems targeting developers
- **SQL Injection**: Database attacks through vulnerable WordPress plugins
- **Tag Poisoning**: Compromising GitHub Actions through malicious version tags
- **Social Engineering**: Android malware disguised as legitimate applications like Starlink
- **Wiper Malware**: Data destruction attacks by Iran-linked Handala group
- **EDR Evasion**: BlackSanta malware designed to disable endpoint detection and response tools
- **Zombie ZIP Technique**: Specially crafted compressed files to evade security detection
- **AI Browser Manipulation**: Tricking AI-powered browsers into phishing attacks within minutes
- **Configuration Exploitation**: Leveraging overly permissive cloud configurations

## Threat Actor Activities

- **UNC6426**: Leveraged nx NPM compromise to gain AWS admin access within 72 hours of initial breach
- **INC Ransomware Group**: Targeting healthcare infrastructure across Oceania region including government agencies and emergency clinics
- **Handala (Iran-linked)**: Conducted wiper malware attack against Stryker medical technology company
- **PhantomRaven Campaign**: Ongoing supply chain attacks through 88 malicious NPM packages stealing developer data
- **Russian-speaking Threat Actor**: Year-long campaign targeting HR departments with BlackSanta EDR killer malware
- **Sednit (Russian APT)**: Resurfaced with sophisticated new malware toolkit after period of using simple implants
- **Chinese Nexus Actors**: Shifted focus to Qatar amid Iranian conflict, demonstrating rapid geopolitical pivoting capabilities
- **Southeast Asia Scam Centers**: Over 150,000 accounts disabled by Meta in coordinated law enforcement action
- **Android Malware Groups**: Six distinct families targeting financial applications with advanced evasion techniques