# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation, with threat actors leveraging SQL injection flaws, supply chain attacks, and zero-day vulnerabilities to compromise systems worldwide. The most severe incidents include a Ghost CMS SQL injection vulnerability being exploited in large-scale ClickFix campaigns, a maximum-severity LiteSpeed cPanel plugin flaw allowing root-level script execution, and a Trend Micro Apex One zero-day vulnerability targeting Windows systems. Additionally, coordinated supply chain attacks have compromised multiple package repositories including npm, PyPI, Laravel-Lang, and Packagist, delivering sophisticated credential-stealing malware to developers globally.

## Active Exploitation Details

### Ghost CMS SQL Injection Vulnerability
- **Description**: Critical SQL injection flaw in Ghost CMS that allows attackers to inject malicious JavaScript code
- **Impact**: Enables injection of malicious code that triggers ClickFix attack flows in large-scale campaigns
- **Status**: Currently being exploited in active campaigns
- **CVE ID**: CVE-2026-26980

### LiteSpeed cPanel Plugin Authentication Bypass
- **Description**: Maximum-severity security vulnerability affecting LiteSpeed User-End cPanel Plugin
- **Impact**: Allows attackers to execute scripts with root privileges on compromised systems
- **Status**: Under active exploitation in the wild
- **CVE ID**: CVE-2026-48172

### Trend Micro Apex One Zero-Day
- **Description**: Zero-day vulnerability in Trend Micro Apex One cybersecurity software
- **Impact**: Enables attacks targeting Windows systems with potential for system compromise
- **Status**: Actively exploited in attacks, recently patched by vendor
- **CVE ID**: Not specified in the article

### Drupal Core SQL Injection
- **Description**: Critical SQL injection vulnerability in Drupal Core
- **Impact**: Allows attackers to execute unauthorized database queries and potentially gain system access
- **Status**: Recently patched but added to CISA KEV catalog due to active exploitation attempts

### Langflow Vulnerability
- **Description**: Security flaw affecting the Langflow platform
- **Impact**: Enables unauthorized access or system compromise
- **Status**: Added to CISA Known Exploited Vulnerabilities (KEV) catalog

### Cisco Secure Workload REST API Flaw
- **Description**: Maximum-severity authentication bypass in Cisco Secure Workload REST API
- **Impact**: Allows unauthenticated remote attackers to access sensitive data
- **Status**: Recently patched by Cisco
- **CVE ID**: CVE-2026-20223

## Affected Systems and Products

- **Ghost CMS**: Content management systems vulnerable to SQL injection attacks
- **LiteSpeed cPanel Plugin**: Web hosting control panels with the affected plugin installed
- **Trend Micro Apex One**: Enterprise endpoint security solutions on Windows systems
- **Drupal Core**: Websites and applications built on the Drupal platform
- **Laravel-Lang Packages**: PHP applications using compromised localization packages
- **npm, PyPI, CratesIO**: Development environments using packages from these repositories
- **Packagist**: PHP applications using compromised packages from the repository
- **Langflow**: Organizations using the Langflow platform
- **Cisco Secure Workload**: Network security monitoring and policy enforcement systems
- **Ubiquiti UniFi OS**: Network infrastructure management systems

## Attack Vectors and Techniques

- **SQL Injection Attacks**: Exploitation of database query vulnerabilities to inject malicious code and trigger ClickFix campaigns
- **Supply Chain Attacks**: Compromising legitimate package repositories to distribute credential-stealing malware
- **Zero-Day Exploitation**: Leveraging previously unknown vulnerabilities before patches are available
- **ClickFix Campaign Flows**: Using injected JavaScript to redirect users to malicious sites or trigger unwanted actions
- **Malicious CI/CD Workflows**: Automated attacks targeting GitHub repositories with malicious commits and workflows
- **Cross-Platform Credential Theft**: Deployment of comprehensive credential-stealing frameworks across multiple operating systems
- **GitHub Version Tag Abuse**: Manipulating version control tags to distribute malicious packages
- **Linux Binary Deployment**: Using GitHub Releases to host and distribute malicious Linux executables

## Threat Actor Activities

- **TrapDoor Campaign**: Coordinated cross-ecosystem supply chain attack targeting npm, PyPI, and Crates.io repositories to distribute credential-stealing malware
- **Laravel-Lang Attackers**: Sophisticated threat actors compromising Laravel localization packages to deploy cross-platform credential stealers
- **Packagist Campaign**: Coordinated attack affecting eight packages on Packagist repository using GitHub-hosted Linux malware
- **Megalodon Campaign**: Automated attack pushing 5,718 malicious commits to 5,561 GitHub repositories within a six-hour window using malicious CI/CD workflows
- **Ghostwriter (UAC-0057/UNC1151)**: Belarus-aligned threat actor targeting Ukrainian government entities using Prometheus phishing malware and lures
- **Webworm APT**: Chinese advanced persistent threat group using Discord and Microsoft Graph APIs to target European Union government systems
- **Kimwolf Botnet Operator**: Canadian cybercriminal operating a DDoS botnet affecting nearly two million devices worldwide for DDoS-for-hire attacks