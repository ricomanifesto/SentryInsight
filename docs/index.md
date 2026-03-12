# Exploitation Report

Critical exploitation activity is currently focused on multiple high-impact vulnerabilities across various platforms. The most urgent threat involves the n8n workflow automation platform, which CISA has flagged for active exploitation and added to its Known Exploited Vulnerabilities catalog, with approximately 24,700 instances remaining exposed to remote code execution attacks. Apple has issued emergency security updates for older iOS devices targeted by the Coruna WebKit exploit kit, indicating active zero-day exploitation in the wild. Additionally, sophisticated supply chain attacks are proliferating across development ecosystems, with threat actors compromising npm packages, Rust crates, and even GitHub Actions to steal developer credentials and gain unauthorized access to cloud environments. The threat landscape is further complicated by advanced malware campaigns targeting Android devices, EDR evasion techniques, and coordinated ransomware operations by established criminal groups.

## Active Exploitation Details

### n8n Remote Code Execution Vulnerability
- **Description**: Critical security flaw in the n8n workflow automation platform allowing arbitrary command execution and exposure of stored credentials
- **Impact**: Attackers can achieve complete remote code execution and access sensitive stored credentials on compromised systems
- **Status**: Actively exploited in the wild, patched by vendor, added to CISA KEV catalog with mandatory patching deadline for federal agencies

### Coruna WebKit Exploit
- **Description**: Security vulnerability in WebKit affecting older iOS, iPadOS, and macOS Sonoma devices
- **Impact**: Enables exploitation through malicious web content, allowing attackers to compromise Apple devices
- **Status**: Actively exploited as part of the Coruna exploit kit, Apple has backported fixes to older device versions

### nx npm Supply Chain Compromise
- **Description**: Supply chain attack targeting the nx npm package that resulted in credential theft
- **Impact**: Complete breach of victim cloud environments within 72 hours, including AWS admin access
- **Status**: Previously compromised package used by UNC6426 threat actor for ongoing attacks

### Elementor Ally Plugin SQL Injection
- **Description**: SQL injection vulnerability in the Ally WordPress plugin for web accessibility
- **Impact**: Allows exploitation to steal sensitive data from WordPress databases without authentication
- **Status**: Affects over 250,000 WordPress installations, patch status unknown

### GitHub Action Tag Poisoning Attack
- **Description**: Compromise of Xygeni's xygeni-action GitHub Action through tag poisoning technique
- **Impact**: Active command and control implant operated for up to one week, compromising CI/CD pipelines
- **Status**: Recently discovered and remediated, affected AppSec vendor operations

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Approximately 24,700 exposed instances requiring immediate patching
- **Apple iOS/iPadOS/macOS**: Older device versions targeted by Coruna exploit kit, emergency updates issued
- **WordPress Sites**: Over 250,000 installations using vulnerable Elementor Ally plugin
- **npm Ecosystem**: Multiple malicious packages in PhantomRaven campaign targeting JavaScript developers
- **Rust Crates**: Five malicious packages masquerading as time utilities on crates.io
- **Android Devices**: Multiple malware families targeting Pix payments, banking apps, and crypto wallets
- **Microsoft Software**: 84 vulnerabilities patched including two publicly known zero-days
- **Enterprise Networks**: HR departments specifically targeted by BlackSanta EDR killer malware
- **Salesforce Cloud**: Misconfigurations in guest user settings exposing sensitive client data

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious packages injected into npm, Rust, and Python repositories to steal developer credentials
- **WebKit Exploitation**: Browser-based attacks through malicious web content targeting Apple devices
- **SQL Injection**: Database attacks through vulnerable WordPress plugins affecting hundreds of thousands of sites
- **EDR Evasion**: BlackSanta malware specifically designed to disable endpoint detection and response systems
- **Social Engineering**: Malware disguised as legitimate applications like Starlink to trick Android users
- **Tag Poisoning**: Manipulation of version control tags to compromise GitHub Actions and CI/CD pipelines
- **Zombie ZIP Technique**: Specially crafted compressed files designed to bypass antivirus and EDR detection
- **Phishing Campaigns**: Advanced attacks designed to overwhelm SOC analysts and exhaust investigation resources

## Threat Actor Activities

- **UNC6426**: Leveraged stolen nx npm package credentials to achieve complete AWS environment compromise within 72 hours
- **PhantomRaven Campaign**: Ongoing supply chain attacks deploying 88 malicious npm packages to steal developer data
- **BlackCat/ALPHV Ransomware**: Continued operations with insider trading schemes involving cryptocurrency exchanges
- **INC Ransomware Group**: Targeting healthcare organizations across Oceania including government agencies and emergency clinics
- **Handala (Iranian-linked)**: Claimed responsibility for wiper malware attack against medical technology company Stryker
- **Chinese Nexus Actors**: Shifting focus to Qatari entities amid Iranian conflict, demonstrating rapid tactical pivoting
- **Russian-speaking Actors**: Year-long campaign targeting HR departments with BlackSanta EDR killer malware
- **BeatBanker Operators**: Distributing Android malware through fake Starlink applications and counterfeit Google Play Store sites
- **Southeast Asian Scam Centers**: Large-scale operations with over 150,000 accounts disabled by Meta in coordinated crackdown