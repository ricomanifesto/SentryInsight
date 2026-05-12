# Exploitation Report

Several critical vulnerabilities are currently under active exploitation, representing significant threats to enterprise and consumer environments. The most concerning activity involves an AI-developed zero-day exploit targeting web administration tools, a critical cPanel vulnerability being exploited to deploy backdoors, and supply chain compromises affecting development tools. Notable threat actors including Mr_Rot13 and TeamPCP are actively exploiting these vulnerabilities to deploy malware, establish persistence, and compromise development environments. Additionally, widespread malvertising campaigns are targeting macOS users while criminal marketplace infrastructure continues to facilitate cybercriminal operations.

## Active Exploitation Details

### AI-Developed Zero-Day 2FA Bypass
- **Description**: An unknown threat actor has developed the first known zero-day exploit that bypasses two-factor authentication systems using artificial intelligence assistance
- **Impact**: Allows attackers to completely circumvent 2FA protections, providing unauthorized access to protected accounts and systems
- **Status**: Currently under active exploitation; Google Threat Intelligence Group has identified this as an ongoing campaign

### cPanel Critical Vulnerability
- **Description**: A critical security flaw in cPanel environments that allows attackers to deploy backdoor malware
- **Impact**: Enables complete compromise of web hosting environments, installation of persistent backdoors, and potential lateral movement
- **Status**: Under active exploitation by threat actor Mr_Rot13 to deploy "Filemanager" backdoor
- **CVE ID**: CVE-2026-41940

### Canvas Portal Defacement Vulnerability
- **Description**: A security vulnerability in Instructure's Canvas learning management system that allows unauthorized modification of login portals
- **Impact**: Attackers can deface educational portals and leave extortion messages, potentially disrupting educational services
- **Status**: Actively exploited by hackers; Instructure has confirmed the exploitation

### Dirty Frag Linux Privilege Escalation
- **Description**: A privilege escalation vulnerability in Linux distributions similar to Copy Fail and Dirty Pipe exploits
- **Impact**: Allows local attackers to escalate privileges to root level on affected Linux systems
- **Status**: May already be under limited exploitation according to security researchers

### Ollama Out-of-Bounds Read Vulnerability
- **Description**: A critical security flaw in the Ollama AI platform that allows remote memory access
- **Impact**: Remote, unauthenticated attackers can leak entire process memory, potentially exposing sensitive data
- **Status**: Vulnerability disclosed; exploitation potential confirmed

## Affected Systems and Products

- **cPanel and Web Host Manager (WHM)**: Critical vulnerability affecting web hosting control panels
- **Jenkins Marketplace**: Compromised CheckMarx AST plugin affecting CI/CD environments
- **Canvas Learning Management System**: Educational technology platform experiencing portal defacement attacks
- **Enterprise Linux Distributions**: Multiple distributions vulnerable to Dirty Frag privilege escalation
- **Ollama AI Platform**: AI inference platform vulnerable to memory leak attacks
- **JDownloader Website**: Popular download manager site compromised to distribute malware
- **Hugging Face Platform**: AI model repository hosting malicious OpenAI impersonation projects
- **Google Play Store**: Fraudulent apps with 7.3 million downloads targeting Android users
- **NVIDIA GeForce NOW**: Gaming service affected by data breach exposing Armenian user data

## Attack Vectors and Techniques

- **AI-Assisted Exploit Development**: Threat actors using large language models to develop zero-day exploits and automate attack orchestration
- **Supply Chain Compromise**: Multiple incidents involving compromised software repositories and official distribution channels
- **Malvertising Campaigns**: Google Ads abuse and Claude.ai chat exploitation to distribute macOS malware
- **Social Engineering**: Fake applications and repositories impersonating legitimate software projects
- **Web Application Exploitation**: Direct exploitation of web-based administration tools and content management systems
- **Blockchain-Based C2 Communications**: TrickMo malware adopting TON blockchain for covert command and control
- **Windows API Abuse**: GhostLock tool demonstrating legitimate API misuse for file access blocking

## Threat Actor Activities

- **Mr_Rot13**: Actively exploiting cPanel vulnerabilities to deploy Filemanager backdoors in hosting environments
- **TeamPCP**: Responsible for compromising CheckMarx Jenkins AST plugin weeks after previous KICS supply chain attack
- **ShinyHunters**: Claims responsibility for second attack against Instructure, targeting PII of hundreds of millions of users
- **Unknown AI-Assisted Actor**: Developing and deploying first known AI-generated zero-day exploits targeting 2FA systems
- **Brazilian Threat Groups**: Operating TCLBANKER banking trojan targeting 59 financial platforms via WhatsApp and Outlook worms
- **Malvertising Operations**: Multiple campaigns targeting macOS users through Google Ads and Claude.ai platform abuse
- **Android Malware Operators**: Deploying fraudulent call history applications stealing payments from 7.3 million Play Store downloads