# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value platforms and systems across educational technology, cloud infrastructure, and enterprise environments. The most severe incidents include active zero-day exploitation of Ivanti Endpoint Manager Mobile systems granting administrative access, a new Linux kernel privilege escalation vulnerability affecting all major distributions, and widespread attacks on Canvas educational platforms by the ShinyHunters group. Additional concerning activity involves sophisticated malware campaigns targeting macOS users through Google Ads, supply chain attacks on popular software distribution platforms, and worm-like credential theft malware spreading across cloud infrastructure while exploiting multiple known vulnerabilities.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile Remote Code Execution
- **Description**: High-severity remote code execution vulnerability in Ivanti EPMM being exploited in limited attacks in the wild
- **Impact**: Attackers can gain administrative-level access to endpoint management systems
- **Status**: Under active exploitation with patches available; CISA has given federal agencies four days to secure their networks
- **CVE ID**: CVE-2026-6973

### Linux Kernel "Dirty Frag" Local Privilege Escalation
- **Description**: Unpatched zero-day vulnerability in the Linux kernel allowing local privilege escalation with a single command
- **Impact**: Local attackers can gain root privileges on all major Linux distributions
- **Status**: Currently unpatched with proof-of-concept exploit available; described as successor to Copy Fail vulnerability

### Ollama Out-of-Bounds Read Vulnerability
- **Description**: Critical security flaw allowing remote, unauthenticated attackers to leak entire process memory
- **Impact**: Complete process memory disclosure to remote attackers without authentication
- **Status**: Critical vulnerability disclosed with exploitation details available

### cPanel and WHM Multiple Vulnerabilities
- **Description**: Three newly disclosed vulnerabilities in cPanel and Web Host Manager platforms
- **Impact**: Privilege escalation, code execution, and denial-of-service attacks possible
- **Status**: Patches released; immediate updates recommended

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Enterprise mobile device management systems with administrative access compromise
- **Linux Kernel**: All major Linux distributions vulnerable to local privilege escalation
- **Ollama**: AI model serving platform with memory leak vulnerability
- **cPanel/WHM**: Web hosting control panel systems across hosting providers
- **Canvas LMS**: Educational technology platform serving hundreds of colleges and universities
- **JDownloader**: Popular download manager with compromised distribution site
- **Hugging Face**: AI model repository platform with malicious repositories
- **NVIDIA GeForce NOW**: Cloud gaming service with confirmed data breach affecting Armenian users
- **Google Play Store**: Android app marketplace with fraudulent payment-stealing applications

## Attack Vectors and Techniques

- **Malvertising Campaigns**: Abuse of Google Ads to distribute macOS malware targeting Claude.ai users
- **Supply Chain Compromise**: JDownloader website compromise to distribute Python RAT malware through legitimate installers
- **Social Engineering**: ClickFix technique used to distribute Vidar Stealer malware in Australian campaigns
- **Repository Poisoning**: Fake OpenAI repositories on Hugging Face delivering information-stealing malware
- **Worm-like Propagation**: PCPJack malware spreading across cloud infrastructure while stealing credentials
- **Self-Spreading Mechanisms**: TCLBanker malware propagating through WhatsApp and Outlook messaging platforms
- **PAM Module Exploitation**: PamDOORa backdoor using Linux PAM modules to steal SSH credentials
- **Zero-day Exploitation**: Direct exploitation of unpatched vulnerabilities for immediate access

## Threat Actor Activities

- **ShinyHunters Group**: Conducting second major attack against Instructure's Canvas platform, exploiting vulnerabilities to deface login portals and extort educational institutions
- **RansomHouse**: Claimed responsibility for Trellix source code repository breach with leaked proof-of-concept materials
- **Brazilian Threat Actors**: Operating TCLBANKER campaign targeting 59 banking, fintech, and cryptocurrency platforms with self-spreading capabilities
- **darkworm**: Advertising PamDOORa Linux backdoor on Russian cybercrime forum Rehub for $1,600
- **Unknown Actors**: Multiple campaigns involving Google Ads abuse, fake app distribution, and cloud infrastructure targeting with sophisticated evasion techniques