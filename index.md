# Exploitation Report

The current threat landscape is dominated by several critical zero-day vulnerabilities and active exploitation campaigns targeting enterprise infrastructure. Most notably, the Ivanti Endpoint Manager Mobile (EPMM) vulnerability CVE-2026-6973 is being actively exploited in the wild, prompting CISA to issue emergency patching directives for federal agencies. Simultaneously, the Linux "Dirty Frag" zero-day represents a significant privilege escalation threat across all major distributions, while the ShinyHunters group continues their aggressive campaign against educational institutions through the Canvas platform. These incidents highlight the evolving tactics of threat actors who are increasingly targeting cloud infrastructure and educational systems with sophisticated malware frameworks and social engineering techniques.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution Vulnerability
- **Description**: A high-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) allowing attackers to gain administrative-level access to affected systems
- **Impact**: Attackers can achieve complete system compromise with admin-level privileges, potentially leading to lateral movement and data exfiltration
- **Status**: Actively exploited in zero-day attacks; CISA has mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Dirty Frag Zero-Day Local Privilege Escalation
- **Description**: An unpatched local privilege escalation vulnerability affecting the Linux kernel across all major distributions, described as a successor to Copy Fail
- **Impact**: Local attackers can gain root privileges with a single command, providing complete system control
- **Status**: Zero-day vulnerability with publicly available proof-of-concept exploit; currently unpatched
- **CVE ID**: CVE-2026-31

### PAN-OS Remote Code Execution Vulnerability
- **Description**: A critical security flaw in Palo Alto Networks PAN-OS systems that enables remote code execution and root access
- **Impact**: Attackers can achieve root access and conduct espionage activities on network security appliances
- **Status**: Under active exploitation since April 9, 2026; attempted exploits detected

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management platform vulnerable to remote code execution
- **Linux Kernel**: All major Linux distributions affected by Dirty Frag privilege escalation vulnerability
- **Canvas Learning Management System**: Educational technology platform compromised through login portal vulnerabilities
- **PAN-OS Systems**: Palo Alto Networks firewalls and security appliances
- **Android Devices**: Google Play Store hosting fraudulent call history applications affecting 7.3 million downloads
- **WhatsApp and Outlook**: Messaging platforms exploited by TCLBANKER for malware distribution
- **Cloud Infrastructure**: AWS, Azure, and other cloud environments targeted by PCPJack credential theft framework

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM and Linux kernel
- **Social Engineering**: ClickFix techniques used to distribute Vidar Stealer malware in Australia
- **Malware Distribution**: TCLBANKER spreading through trojanized MSI installers disguised as legitimate software
- **Worm-Like Propagation**: PCPJack utilizing five different vulnerabilities to spread across cloud systems
- **Application Store Abuse**: Fraudulent Android applications on Google Play Store for payment theft
- **Credential Harvesting**: PamDOORa backdoor using PAM modules to steal SSH credentials
- **Supply Chain Targeting**: Quasar Linux RAT specifically targeting developer systems for broader compromise

## Threat Actor Activities

- **ShinyHunters**: Conducting persistent attacks against Instructure's Canvas platform, successfully breaching educational institutions twice and defacing hundreds of college login portals
- **RansomHouse**: Claiming responsibility for the Trellix source code repository breach and releasing proof-of-concept images
- **TCLBANKER Operators**: Targeting 59 banking, fintech, and cryptocurrency platforms using sophisticated trojanized installers
- **PCPJack Campaign**: Actively stealing credentials from exposed cloud infrastructure while simultaneously cleaning TeamPCP infections
- **darkworm**: Advertising the PamDOORa Linux backdoor on Russian cybercrime forums for $1,600
- **ClickFix Campaign**: Targeting Australian organizations with Vidar Stealer malware through social engineering
- **North Korean IT Workers**: Utilizing laptop farms operated by convicted American nationals to fraudulently obtain remote employment at nearly 70 U.S. companies