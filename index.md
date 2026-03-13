# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple platforms, with Google Chrome and Apple iOS devices facing immediate threats from sophisticated attack campaigns. Two high-severity Chrome zero-days affecting the Skia graphics library and V8 JavaScript engine have been exploited in the wild, prompting emergency security updates. Meanwhile, Apple has backported security fixes to older iOS devices to address vulnerabilities targeted by the Coruna exploit kit in cyberespionage and crypto-theft operations. Additionally, CISA has flagged an actively exploited remote code execution vulnerability in n8n workflow automation platform, with over 24,700 instances remaining exposed to attack. The threat landscape is further complicated by AI-generated malware campaigns, critical infrastructure targeting by Iranian APTs, and sophisticated botnet operations affecting hundreds of thousands of compromised devices globally.

## Active Exploitation Details

### Chrome Zero-Day Vulnerabilities in Skia and V8
- **Description**: Two high-severity vulnerabilities affecting Google Chrome's Skia graphics library and V8 JavaScript engine that have been actively exploited in zero-day attacks
- **Impact**: Attackers can potentially execute arbitrary code, compromise user systems, and steal sensitive information through malicious web pages
- **Status**: Google has released emergency security updates to patch both vulnerabilities

### n8n Workflow Automation RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in the n8n workflow automation platform that allows unauthorized command execution
- **Impact**: Attackers can gain complete control over affected n8n instances, execute arbitrary commands, and potentially pivot to other systems
- **Status**: Actively exploited according to CISA, with over 24,700 exposed instances remaining vulnerable

### Apple iOS Coruna WebKit Exploit
- **Description**: Security vulnerability in WebKit component of older iOS, iPadOS, and macOS Sonoma versions targeted by the Coruna exploit kit
- **Impact**: Used in cyberespionage campaigns and crypto-theft attacks to compromise Apple devices
- **Status**: Apple has backported security fixes to older device versions after active exploitation was discovered

### Linux AppArmor CrackArmor Vulnerabilities
- **Description**: Nine security vulnerabilities within the Linux kernel's AppArmor security module that can be exploited by unprivileged users
- **Impact**: Enables privilege escalation to root access, bypass of container isolation, and circumvention of kernel security protections
- **Status**: Disclosed vulnerabilities affecting Linux systems with AppArmor enabled

## Affected Systems and Products

- **Google Chrome**: All versions prior to the latest security update, affecting Skia graphics library and V8 JavaScript engine components
- **Apple iOS Devices**: Older iPhone and iPad models running vulnerable versions of iOS and iPadOS
- **n8n Platform**: Over 24,700 exposed instances of the workflow automation platform globally
- **Linux Systems**: Distributions using AppArmor security module, particularly affecting containerized environments
- **Veeam Backup & Replication**: Multiple critical vulnerabilities affecting backup infrastructure
- **Brazilian Banking Systems**: 33 financial institutions targeted by Rust-based VENON malware
- **Android Devices**: Six new malware families targeting Pix payments, banking apps, and cryptocurrency wallets

## Attack Vectors and Techniques

- **Zero-Day Web Exploitation**: Malicious websites leveraging Chrome vulnerabilities in Skia and V8 components
- **Workflow Automation Compromise**: Direct exploitation of exposed n8n instances for remote code execution
- **Mobile WebKit Attacks**: Coruna exploit kit targeting iOS devices through browser vulnerabilities
- **Container Escape**: CrackArmor flaws enabling privilege escalation from unprivileged containers
- **AI-Generated Malware**: Slopoly malware created using generative AI tools for persistent access
- **Proxy Botnet Operations**: SocksEscort network compromising residential routers across 163 countries
- **Banking Overlays**: VENON malware using credential-stealing overlays targeting Brazilian financial institutions
- **Supply Chain Compromise**: Xygeni GitHub Action compromised via tag poisoning attack

## Threat Actor Activities

- **Hive0163**: Financially motivated group using AI-generated Slopoly malware in ransomware attacks for persistent network access
- **Iranian MOIS**: Collaborating with cybercriminal groups to enhance cyberattack capabilities and expand operational reach
- **SocksEscort Operators**: Criminal proxy service enslaving 369,000 IP addresses across 163 countries before law enforcement disruption
- **BlackCat (ALPHV) Associates**: Ransomware negotiators secretly partnering with cryptocurrency exchange insiders for money laundering
- **INC Ransomware Group**: Targeting healthcare infrastructure across Australia, New Zealand, and Tonga
- **Brazilian Banking Malware Authors**: Developing Rust-based VENON malware specifically targeting 33 Brazilian financial institutions
- **AiLock Ransomware Gang**: Claiming responsibility for England Hockey data breach incident
- **Interlock Ransomware Operators**: Utilizing AI-generated malware for extended network persistence and data theft