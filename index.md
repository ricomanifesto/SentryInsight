# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited across multiple platforms, with threat actors targeting Linux systems, network appliances, and educational technology platforms. The most severe active exploitations include CVE-2026-6973 affecting Ivanti EPMM systems, which grants administrator-level access through remote code execution, and the newly discovered "Dirty Frag" Linux kernel zero-day that provides root privileges across all major distributions. Additionally, widespread supply chain compromises are occurring through malicious repositories and website defacements, with ShinyHunters conducting major extortion campaigns against educational institutions using Canvas platforms.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) allowing unauthorized access to mobile device management systems
- **Impact**: Attackers can gain administrator-level access to enterprise mobile management infrastructure and potentially compromise managed devices
- **Status**: Actively exploited in limited zero-day attacks, patch available
- **CVE ID**: CVE-2026-6973

### Linux Kernel Dirty Frag Zero-Day
- **Description**: Unpatched local privilege escalation vulnerability in the Linux kernel affecting all major distributions
- **Impact**: Local attackers can gain root privileges with a single command, providing complete system control
- **Status**: Zero-day with public proof-of-concept exploit available, no patch currently available

### PAN-OS Remote Code Execution
- **Description**: Critical security flaw in Palo Alto Networks PAN-OS enabling remote code execution on network security appliances
- **Impact**: Threat actors can achieve root access and conduct espionage activities on enterprise firewalls
- **Status**: Under active exploitation since April 2026, attempts detected but some unsuccessful

### Canvas Education Platform Vulnerability
- **Description**: Unspecified vulnerability in Instructure's Canvas learning management system affecting login portals
- **Impact**: Mass defacement of educational institution login pages and potential data exposure
- **Status**: Actively exploited by ShinyHunters in widespread extortion campaign

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems across federal and corporate environments
- **Linux Distributions**: All major distributions including Ubuntu, Red Hat, SUSE, and others affected by Dirty Frag kernel vulnerability
- **Palo Alto Networks PAN-OS**: Network security appliances and firewall systems
- **Instructure Canvas**: Education technology platforms used by hundreds of colleges and universities nationwide
- **JDownloader**: Popular download manager with compromised official website distributing malicious installers
- **cPanel/WHM**: Web hosting control panels with three newly patched vulnerabilities
- **NVIDIA GeForce NOW**: Cloud gaming service with confirmed data breach affecting Armenian users
- **Hugging Face**: Machine learning repository platform hosting fake OpenAI projects with infostealer malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities in critical infrastructure systems
- **Supply Chain Compromise**: Malicious code injection into legitimate software distribution channels including JDownloader and fake repositories
- **Social Engineering**: ClickFix campaigns and fake application repositories targeting developers and end users
- **Website Defacement**: Mass compromise of educational login portals for extortion purposes
- **Credential Harvesting**: PAM module abuse through PamDOORa backdoor and cloud infrastructure targeting via PCPJack framework
- **Worm Propagation**: Self-spreading malware through messaging platforms like WhatsApp and email systems
- **Trojanized Installers**: Legitimate software packages replaced with malicious variants containing Python RATs and banking trojans

## Threat Actor Activities

- **ShinyHunters**: Conducting second major attack against Instructure's Canvas platform, executing mass extortion campaign affecting hundreds of educational institutions
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach with proof-of-concept data leaks
- **Brazilian Cybercriminals**: Deploying TCLBANKER trojan targeting 59 financial platforms with WhatsApp and Outlook spreading capabilities
- **Russian Forum Actors**: Marketing PamDOORa Linux backdoor on Rehub cybercrime forum for $1,600 by threat actor "darkworm"
- **PCPJack Operators**: Targeting exposed cloud infrastructure while actively removing competing TeamPCP malware from compromised systems
- **Mobile App Scammers**: Distributing fraudulent call history applications through Google Play Store with 7.3 million downloads for payment theft