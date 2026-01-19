# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by several zero-day attacks targeting enterprise infrastructure and security products. China-linked threat actors have been actively exploiting zero-day vulnerabilities in Sitecore content management systems and Cisco Secure Email Gateway products to gain initial access to North American critical infrastructure systems. Additionally, a critical command injection vulnerability in Fortinet's FortiSIEM platform is under active exploitation, while malicious browser extensions continue to target enterprise HR and ERP platforms through social engineering tactics.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sitecore content management systems that allows threat actors to gain initial access to targeted systems
- **Impact**: Enables unauthorized access to critical infrastructure systems and serves as an entry point for broader network compromise
- **Status**: Currently being exploited by China-linked APT group UAT-8837 targeting North American critical infrastructure

### Cisco Secure Email Gateway Zero-Day RCE
- **Description**: A maximum-severity remote code execution vulnerability in Cisco AsyncOS Software for Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Impact**: Allows attackers to achieve remote code execution on affected email security appliances
- **Status**: Actively exploited by China-linked APT groups; Cisco has released security updates
- **CVE ID**: CVE-2025-20002

### Fortinet FortiSIEM Command Injection Vulnerability
- **Description**: A critical command injection vulnerability in Fortinet's FortiSIEM security information and event management platform
- **Impact**: Enables attackers to execute arbitrary commands on affected systems
- **Status**: Under active exploitation from multiple IP addresses shortly after disclosure
- **CVE ID**: CVE-2025-64155

### AMD StackWarp Hardware Vulnerability
- **Description**: A hardware-level vulnerability affecting AMD processors that breaks AMD SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) protections
- **Impact**: Allows attackers to bypass hardware-level security protections on virtualized environments
- **Status**: Recently disclosed vulnerability affecting AMD Zen 1-5 CPUs

## Affected Systems and Products

- **Sitecore CMS**: Content management systems used by organizations in critical infrastructure sectors
- **Cisco Email Security Appliances**: AsyncOS Software for Cisco Secure Email Gateway and Cisco Secure Email and Web Manager
- **Fortinet FortiSIEM**: Security information and event management platforms
- **AMD Processors**: Zen 1 through Zen 5 architecture CPUs with SEV-SNP capabilities
- **Chrome Browser Extensions**: Enterprise users of HR platforms like Workday and ERP systems like NetSuite
- **StealC Malware Control Panels**: Web-based control panels used by StealC information stealer operators

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of undisclosed vulnerabilities in enterprise software and hardware
- **Malicious Browser Extensions**: Social engineering through fake productivity and security tools targeting enterprise platforms
- **Spear Phishing**: Venezuela-themed political lures used to deliver LOTUSLITE backdoor to U.S. policy entities
- **ClickFix-Style Attacks**: Browser crash simulation followed by malicious Chrome extension installation delivering ModeloRAT
- **ZIP Archive Concatenation**: GootLoader malware using 500-1,000 concatenated ZIP archives to evade detection
- **Cross-Site Scripting**: XSS vulnerabilities in malware control panels exploited for intelligence gathering

## Threat Actor Activities

- **UAT-8837 (China-linked)**: Targeting North American critical infrastructure systems using Sitecore zero-day vulnerabilities for initial access
- **China-linked APT Groups**: Exploiting Cisco Secure Email Gateway zero-day for remote code execution capabilities
- **KongTuke Campaign**: Distributing ModeloRAT through CrashFix Chrome extension using browser crash social engineering
- **GhostPoster Campaign**: Operating 17 malicious browser extensions across Chrome, Firefox, and Edge with 840,000+ installations
- **Black Basta Ransomware**: Leadership identified by Ukrainian and German law enforcement; leader added to Europol and Interpol wanted lists
- **StealC Operators**: Information stealing malware operations compromised through XSS vulnerabilities in their control panels
- **LOTUSLITE Operators**: Targeting U.S. government and policy entities with Venezuela-themed spear phishing campaigns