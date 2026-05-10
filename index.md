# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with zero-day vulnerabilities and sophisticated malware campaigns. The most severe concerns include active exploitation of Ivanti Endpoint Manager Mobile (EPMM) systems through CVE-2026-6973, a new Linux kernel privilege escalation vulnerability dubbed "Dirty Frag," and widespread compromise of educational platforms through Canvas breaches. Multiple threat actors are leveraging novel attack vectors including supply chain compromises, social engineering techniques, and worm-like propagation methods to steal credentials and establish persistent access across cloud infrastructure and enterprise environments.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: A high-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile that allows attackers to gain administrative-level access to systems
- **Impact**: Attackers can achieve complete system compromise with administrative privileges, enabling lateral movement and persistent access
- **Status**: Currently being exploited in limited zero-day attacks; patch available and CISA has mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Kernel "Dirty Frag" Privilege Escalation
- **Description**: A new unpatched local privilege escalation vulnerability affecting the Linux kernel across major distributions, described as a successor to Copy Fail
- **Impact**: Local attackers can gain root privileges with a single command on most major Linux distributions
- **Status**: Zero-day vulnerability with public proof-of-concept exploit available; currently unpatched

### Canvas Platform Vulnerabilities
- **Description**: Multiple vulnerabilities in the widely-used Canvas education technology platform that allow unauthorized access and system compromise
- **Impact**: Complete platform compromise affecting hundreds of educational institutions nationwide, disrupting classes and exposing student data
- **Status**: Actively exploited by ShinyHunters group in mass extortion campaign

### Ollama Out-of-Bounds Read Vulnerability
- **Description**: Critical security vulnerability in Ollama that allows remote, unauthenticated attackers to leak entire process memory
- **Impact**: Complete memory disclosure leading to potential credential theft and sensitive data exposure
- **Status**: Recently disclosed vulnerability with active exploitation potential

### PCPJack Framework Exploits
- **Description**: Newly discovered credential theft framework exploiting multiple CVEs to spread across cloud infrastructure
- **Impact**: Widespread credential theft across cloud environments with worm-like propagation capabilities
- **Status**: Active in the wild, targeting exposed cloud infrastructure

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: All versions prior to latest security update affected by zero-day exploitation
- **Linux Kernel**: All major distributions including Ubuntu, RHEL, SUSE, and Debian affected by Dirty Frag vulnerability
- **Canvas Education Platform**: Hundreds of colleges and universities experiencing service disruptions and data exposure
- **JDownloader**: Official website compromised to distribute malicious installers with Python RAT malware
- **cPanel and WHM**: Three new vulnerabilities allowing privilege escalation, code execution, and denial-of-service
- **Ollama AI Platform**: Critical memory disclosure vulnerability affecting all installations
- **Cloud Infrastructure**: Multiple cloud environments targeted by PCPJack framework exploiting five CVEs
- **Android Devices**: 7.3 million downloads of fraudulent call history apps from Google Play Store
- **Banking Platforms**: 59 financial institutions targeted by TCLBanker trojan
- **Hugging Face Repository**: Fake OpenAI project distributing information-stealing malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM and Linux kernel
- **Supply Chain Compromise**: Compromised official download sites distributing malicious installers instead of legitimate software
- **Social Engineering (ClickFix)**: Sophisticated technique tricking users into executing malicious PowerShell commands
- **Worm-Like Propagation**: PCPJack framework automatically spreading across cloud infrastructure after initial compromise
- **Malicious Repository Hosting**: Fake projects on legitimate platforms like Hugging Face distributing malware
- **WhatsApp and Outlook Spreading**: TCLBanker malware self-propagating through messaging platforms
- **PAM Module Abuse**: PamDOORa backdoor leveraging Linux authentication modules to steal SSH credentials
- **Mobile App Store Fraud**: Malicious apps masquerading as legitimate utilities on Google Play Store
- **Educational Platform Targeting**: Mass exploitation of Canvas vulnerabilities for extortion campaigns

## Threat Actor Activities

- **ShinyHunters Group**: Conducting multiple high-profile attacks including second breach of Instructure/Canvas platform and ongoing extortion campaigns affecting educational institutions nationwide
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-concept images demonstrating successful intrusion
- **TCLBanker Operators**: Brazilian cybercriminal group targeting 59 banking and cryptocurrency platforms using trojanized software installers and messaging platform propagation
- **PCPJack Developers**: Advanced threat actors creating sophisticated worm frameworks for cloud credential theft while actively removing competing malware (TeamPCP) from compromised systems
- **Crimenetwork Operators**: German authorities shut down criminal marketplace generating over 3.6 million euros before arresting the administrator
- **PamDOORa Developer "darkworm"**: Advertising Linux backdoor on Russian cybercrime forums for $1,600, targeting SSH credential theft through PAM module manipulation
- **Quasar Linux RAT Operators**: Targeting software developers to establish silent footholds for supply chain compromise attacks
- **ClickFix Campaign Actors**: Australian authorities warning of ongoing campaigns using social engineering to distribute Vidar Stealer malware