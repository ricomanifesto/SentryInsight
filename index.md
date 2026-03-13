# Exploitation Report

Recent security activity reveals a concerning landscape of active exploitations across multiple sectors, with threat actors leveraging both sophisticated malware and critical vulnerabilities. The most significant developments include the active exploitation of the n8n automation platform vulnerability that CISA has flagged as a critical threat to federal systems, the emergence of AI-generated Slopoly malware in ransomware campaigns, and targeted attacks against Apple devices using the Coruna exploit kit. Iranian-linked threat actors have escalated their activities with destructive wiper attacks against major healthcare infrastructure, while cybercriminals continue to innovate with new malware families targeting financial systems and supply chain attacks through compromised repositories.

## Active Exploitation Details

### n8n Automation Platform RCE Vulnerability
- **Description**: A critical remote code execution vulnerability in the n8n workflow automation platform that allows attackers to execute arbitrary code on vulnerable systems
- **Impact**: Full system compromise, unauthorized access to sensitive data, and potential lateral movement within networks
- **Status**: Actively exploited in the wild, CISA has added to Known Exploited Vulnerabilities catalog with mandatory patching requirements for federal agencies
- **CVE ID**: CVE-2024-50389

### Apple WebKit Vulnerability (Coruna Exploit Kit)
- **Description**: A security flaw in Apple's WebKit browser engine that is being exploited through the Coruna exploit kit in targeted cyberespionage and cryptocurrency theft campaigns
- **Impact**: Device compromise, data exfiltration, and unauthorized access to cryptocurrency wallets
- **Status**: Apple has released security updates for older iOS, iPadOS, and macOS devices; actively exploited in targeted attacks

### Xygeni GitHub Action Tag Poisoning
- **Description**: Supply chain attack targeting the xygeni/xygeni-action GitHub Action through malicious tag manipulation
- **Impact**: Code execution in CI/CD pipelines, potential compromise of software build processes, and unauthorized access to development environments
- **Status**: Active C2 implant operated for up to one week before detection

## Affected Systems and Products

- **n8n Automation Platform**: Approximately 24,700 exposed instances remain vulnerable to remote code execution attacks
- **Apple iOS/iPadOS Devices**: Older iPhone and iPad models targeted by Coruna exploit kit campaigns
- **Veeam Backup & Replication**: Multiple critical RCE vulnerabilities patched in backup infrastructure systems
- **WordPress Sites**: Over 250,000 WordPress installations using Elementor Ally plugin affected by SQL injection vulnerability
- **Android Devices**: Six new malware families targeting Pix payments, banking apps, and cryptocurrency wallets
- **NPM Package Registry**: 88 malicious packages in PhantomRaven campaign targeting JavaScript developers
- **GitHub Actions**: Xygeni security vendor's GitHub Action compromised via tag poisoning attack

## Attack Vectors and Techniques

- **AI-Generated Malware**: Slopoly malware created using generative AI tools for persistent access in ransomware operations
- **Supply Chain Poisoning**: PhantomRaven campaign deploying malicious NPM packages to steal developer credentials and sensitive data
- **Wiper Malware Attacks**: Iranian-linked Handala group deploying destructive malware against healthcare infrastructure
- **Financial Overlay Attacks**: VENON malware using Rust-based credential-stealing overlays targeting Brazilian banking customers
- **Proxy Network Exploitation**: SocksEscort network leveraging AVRecon malware on compromised edge devices for cybercrime operations
- **Tag Poisoning**: GitHub Actions compromise through malicious tag manipulation enabling C2 implant deployment

## Threat Actor Activities

- **Hive0163**: Financially motivated group deploying AI-assisted Slopoly malware for persistent access in Interlock ransomware attacks
- **Handala (Iranian-linked)**: Pro-Palestinian hacktivist group claiming responsibility for wiper malware attack against Stryker medical technology company
- **Iran MOIS**: Ministry of Intelligence colluding with cybercriminal groups to enhance cyberattack capabilities and expand operational reach
- **PhantomRaven Campaign**: Ongoing supply chain attacks targeting npm registry with credential-stealing packages affecting JavaScript developers
- **INC Ransomware Group**: Targeting healthcare organizations across Australia, New Zealand, and Tonga with significant operational disruptions
- **AiLock Ransomware**: Listed England Hockey as victim on data leak site following successful breach of the sports governing body
- **BlackCat (ALPHV) Affiliates**: Continued law enforcement actions against ransomware negotiators involved in insider schemes with cryptocurrency exchanges