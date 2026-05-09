# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities and active exploitation campaigns targeting enterprise infrastructure and cloud environments. Most concerning is the active exploitation of Ivanti Endpoint Manager Mobile (EPMM) vulnerability CVE-2026-6973, which CISA has mandated federal agencies patch within four days due to zero-day attacks. Additionally, a new Linux kernel zero-day dubbed "Dirty Frag" is providing root access across major distributions, while the PCPJack credential stealer framework is exploiting five CVEs to spread worm-like across cloud systems. Multiple threat groups including ShinyHunters, RansomHouse, and various banking trojans are conducting widespread campaigns affecting educational institutions, financial platforms, and enterprise systems globally.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) that grants administrative-level access to affected systems
- **Impact**: Attackers can gain full administrative control over mobile device management infrastructure and potentially access managed devices
- **Status**: Currently being exploited in zero-day attacks; patches available and CISA has mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Kernel "Dirty Frag" Zero-Day
- **Description**: Local privilege escalation vulnerability in the Linux kernel described as a successor to Copy Fail vulnerability
- **Impact**: Allows local attackers to gain root privileges on most major Linux distributions with a single command
- **Status**: Unpatched zero-day with proof-of-concept exploit available

### PAN-OS Remote Code Execution
- **Description**: Critical security flaw in Palo Alto Networks PAN-OS that enables remote code execution and root access
- **Impact**: Threat actors can achieve root access and conduct espionage activities on network security appliances
- **Status**: Under active exploitation since approximately April 9, 2026; unsuccessful exploitation attempts detected

### PCPJack Credential Theft Framework
- **Description**: New worm-like credential theft framework targeting exposed cloud infrastructure while removing TeamPCP malware artifacts
- **Impact**: Steals credentials from cloud environments and spreads laterally across systems
- **Status**: Active in the wild, exploiting five different CVEs to propagate

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management platforms used by federal agencies and enterprises
- **Linux Distributions**: All major Linux distributions affected by Dirty Frag kernel vulnerability
- **Palo Alto Networks PAN-OS**: Network security appliances and firewalls
- **Cloud Infrastructure**: AWS, Azure, and other cloud platforms targeted by PCPJack framework
- **cPanel and WHM**: Web hosting control panels with three newly disclosed vulnerabilities
- **Canvas Learning Management System**: Educational technology platform used by schools and universities nationwide
- **NVIDIA GeForce NOW**: Cloud gaming service affecting Armenian users
- **Hugging Face Platform**: AI model repository hosting malicious OpenAI impersonation
- **Google Play Store**: Android app marketplace with fraudulent call history applications
- **Financial Platforms**: 59 banking, fintech, and cryptocurrency platforms targeted by TCLBANKER trojan

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM and Linux kernel
- **Social Engineering via ClickFix**: Australian-targeted campaigns using fake error messages to distribute Vidar Stealer
- **Trojanized Software**: TCLBANKER distributed through fake Logitech AI Prompt Builder MSI installer
- **Repository Impersonation**: Fake OpenAI Privacy Filter project on Hugging Face delivering information stealers
- **Worm Propagation**: Self-spreading malware via WhatsApp and Outlook for TCLBANKER banking trojan
- **PAM Module Backdoors**: PamDOORa backdoor using Linux Pluggable Authentication Modules to steal SSH credentials
- **Supply Chain Targeting**: Quasar Linux RAT targeting developer systems to compromise software development pipelines
- **Cloud Credential Harvesting**: PCPJack using parquet files for stealthy target discovery across cloud environments
- **Mobile App Fraud**: Fake call history apps on Google Play Store with 7.3 million downloads stealing payments

## Threat Actor Activities

- **ShinyHunters**: Conducting second attack against Instructure's Canvas platform, defacing login portals for hundreds of educational institutions and claiming data extortion
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach, leaked proof-of-concept images
- **TCLBANKER Operators**: Brazilian threat group targeting financial platforms with self-spreading banking trojan via social media and email
- **PCPJack Operators**: Credential theft campaign targeting cloud infrastructure while actively cleaning TeamPCP infections
- **Darkworm**: Threat actor advertising PamDOORa Linux backdoor for $1,600 on Russian cybercrime forum Rehub
- **North Korean IT Workers**: Using laptop farms operated by sentenced Americans to fraudulently obtain remote employment at U.S. companies
- **ClickFix Campaign Operators**: Targeting Australian organizations with social engineering attacks distributing Vidar Stealer malware
- **Mobile App Fraudsters**: Creating fake call history applications to steal payments from millions of Android users