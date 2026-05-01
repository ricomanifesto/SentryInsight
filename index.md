# Exploitation Report

Current threat activity demonstrates a significant surge in supply chain attacks targeting development ecosystems, particularly npm packages, alongside critical zero-day exploitations affecting major platforms. TeamPCP has emerged as a prominent threat actor orchestrating widespread credential-stealing campaigns against SAP development environments and Python repositories. Simultaneously, critical authentication bypass vulnerabilities in cPanel and WHM (CVE-2026-41940) are being actively exploited as zero-days, while a newly disclosed Linux privilege escalation flaw dubbed "Copy Fail" affects all major distributions. The threat landscape is further complicated by AI-assisted vulnerability discovery revealing severe flaws in healthcare platforms and development tools.

## Active Exploitation Details

### cPanel and WHM Authentication Bypass
- **Description**: Critical authentication bypass vulnerability allowing unauthorized access to control panels without authentication credentials
- **Impact**: Complete compromise of web hosting management systems, potential server takeover, and access to all hosted websites and databases
- **Status**: Actively exploited as zero-day since late February 2026, emergency patches now available
- **CVE ID**: CVE-2026-41940

### Linux "Copy Fail" Privilege Escalation
- **Description**: Local privilege escalation vulnerability affecting Linux kernels released since 2017, allowing unprivileged users to gain root access
- **Impact**: Complete system compromise from local user accounts, potential for lateral movement in enterprise environments
- **Status**: Proof-of-concept exploit published, patches available for major distributions

### Qinglong Task Scheduler RCE
- **Description**: Authentication bypass vulnerabilities in the Qinglong open-source task scheduling tool enabling remote code execution
- **Impact**: Deployment of cryptocurrency miners on developers' servers, potential for broader system compromise
- **Status**: Actively exploited for cryptomining operations

### Google Gemini CLI Critical RCE
- **Description**: Maximum severity security flaw in Gemini CLI npm package and GitHub Actions workflow
- **Impact**: Remote code execution in continuous integration environments, potential supply chain contamination
- **Status**: Patched by Google after discovery

## Affected Systems and Products

- **cPanel and WHM**: All versions prior to latest emergency updates, affecting web hosting control panels globally
- **WP Squared**: WordPress management platform affected by same authentication bypass as cPanel
- **Linux Distributions**: All major distributions with kernels released since 2017 affected by Copy Fail vulnerability
- **SAP npm Packages**: Multiple official SAP development packages compromised in supply chain attacks
- **PyTorch Lightning**: Popular Python machine learning framework compromised with malicious versions
- **Intercom-client**: Python package targeted in credential theft campaign
- **WordPress Quick Page/Post Redirect Plugin**: Over 70,000 sites affected by dormant backdoor active for five years
- **Qinglong Task Scheduler**: Open-source automation tool exploited for cryptomining
- **OpenEMR**: Electronic health record platform with 38 newly discovered security flaws
- **Roblox Gaming Platform**: 610,000 user accounts compromised and sold

## Attack Vectors and Techniques

- **Supply Chain Compromise**: TeamPCP conducting "Mini Shai-Hulud" attacks against npm ecosystem, targeting SAP and Python development packages
- **Zero-Day Exploitation**: Active exploitation of unpatched authentication bypass in cPanel/WHM infrastructure
- **AI-Assisted Package Injection**: DPRK-linked actors using AI language models to insert malicious dependencies into legitimate projects
- **GitHub Repository Spoofing**: EtherRAT campaign using fake administrative tool repositories to distribute malware
- **Credential Harvesting**: Multiple campaigns focused on stealing developer authentication tokens and cloud credentials
- **Dormant Backdoor Activation**: Long-term persistence through backdoors hidden in popular WordPress plugins
- **DDoS-for-Hire Operations**: Brazilian anti-DDoS firm secretly operating botnet for attacking ISPs
- **Tunneling Service Abuse**: DEEP#DOOR Python backdoor using legitimate tunneling services for persistence

## Threat Actor Activities

- **TeamPCP**: Conducting broad supply chain attacks targeting SAP development ecosystem, deploying Vect 2.0 ransomware that acts as a wiper due to design flaws
- **North Korean APT Groups**: Leveraging AI tools to inject malicious npm packages, creating fake companies as cover for operations
- **Ukrainian Cybercriminals**: Specialized Roblox account theft operation affecting over 610,000 users, generating $225,000 in profits
- **Romanian Swatting Ring**: Organized harassment campaign targeting 75+ public officials and journalists through false emergency calls
- **Brazilian Cybercriminals**: Operating DDoS botnets while masquerading as legitimate anti-DDoS protection services
- **EtherRAT Operators**: Sophisticated campaign targeting high-privilege professional accounts through GitHub repository spoofing
- **Cryptocurrency Scammers**: International operations with 276 arrests across 9 fake investment centers