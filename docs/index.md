# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple domains, with the most critical being active attacks against the Langflow AI platform. CISA has confirmed that threat actors are actively exploiting CVE-2026-33017, a critical vulnerability affecting the Langflow framework that enables attackers to hijack AI workflows through code injection. The rapid exploitation timeline demonstrates attackers' increasing speed in weaponizing newly disclosed vulnerabilities. Additionally, the Coruna iOS exploit framework represents an evolution of the sophisticated Operation Triangulation campaign, while various threat actors continue targeting e-commerce platforms, cryptocurrency wallets, and enterprise systems through advanced attack techniques.

## Active Exploitation Details

### Langflow AI Platform Critical Vulnerability
- **Description**: A critical code injection vulnerability in the Langflow framework that allows attackers to hijack AI workflows
- **Impact**: Attackers can execute malicious code and take control of AI workflow processes, potentially compromising entire AI systems
- **Status**: Actively exploited in the wild according to CISA warnings; threat actors began exploitation within hours of disclosure
- **CVE ID**: CVE-2026-33017

### Ajax Football Club IT System Vulnerabilities
- **Description**: Unspecified vulnerabilities in Ajax Amsterdam's IT infrastructure that enabled unauthorized access to fan data
- **Impact**: Data breach affecting several hundred individuals and potential ticket hijacking capabilities
- **Status**: Exploited by threat actors; incident disclosed by the club

### PolyShell Magento Vulnerability
- **Description**: A vulnerability affecting version 2 of Magento Open Source and Adobe Commerce installations
- **Impact**: Attackers can compromise e-commerce stores and potentially access customer data and payment information
- **Status**: Actively exploited, targeting 56% of all vulnerable Magento stores

### Citrix NetScaler Vulnerabilities
- **Description**: Two vulnerabilities in NetScaler ADC and NetScaler Gateway, with one being similar to the previously exploited CitrixBleed and CitrixBleed2 flaws
- **Impact**: Potential for zero-day style attacks similar to previous NetScaler exploitations
- **Status**: Recently patched by Citrix with urgent patching recommendations

## Affected Systems and Products

- **Langflow Framework**: AI workflow platform vulnerable to code injection attacks
- **Ajax Amsterdam IT Systems**: Football club's customer management and ticketing systems
- **Magento Open Source v2**: E-commerce platform installations targeted by PolyShell attacks
- **Adobe Commerce v2**: Enterprise e-commerce solutions vulnerable to PolyShell exploitation
- **Citrix NetScaler ADC**: Application delivery controller systems requiring immediate patching
- **Citrix NetScaler Gateway**: Network access solutions with critical vulnerabilities
- **iOS Devices**: Targeted by the Coruna exploit framework, evolution of Operation Triangulation
- **Anthropic Claude Chrome Extension**: Previously vulnerable to zero-click XSS prompt injection
- **E-commerce Sites**: Targeted by WebRTC skimmer attacks bypassing Content Security Policy
- **Cryptocurrency Wallets**: 728 different wallet types targeted by Torg Grabber infostealer

## Attack Vectors and Techniques

- **Code Injection**: Primary attack method for the Langflow vulnerability enabling AI workflow hijacking
- **Zero-Click Exploits**: Coruna framework utilizes zero-click iMessage exploits for iOS device compromise
- **WebRTC Data Channels**: Novel payment skimmer technique bypassing Content Security Policy controls
- **Phishing Campaigns**: Multi-stage attacks targeting TikTok for Business accounts and Microsoft credentials
- **Bot-Driven Fraud**: Automated attack chains combining bots, proxies, and stolen credentials
- **XSS Prompt Injection**: Zero-click cross-site scripting attacks via malicious web pages
- **No-Code Platform Abuse**: Exploitation of Bubble AI app builder for hosting phishing infrastructure

## Threat Actor Activities

- **Red Menshen (China-linked)**: Long-term espionage campaign embedding BPFDoor implants in telecom networks for government surveillance
- **Coruna Kit Operators**: Utilizing evolved Operation Triangulation exploit code for mass iOS device attacks
- **PolyShell Attackers**: Systematically targeting vulnerable Magento installations across multiple regions
- **Cryptocurrency Threat Actors**: Operating Torg Grabber campaigns against 850+ browser extensions including 700+ crypto wallets
- **E-commerce Skimmers**: Deploying WebRTC-based payment card skimmers to bypass security controls
- **RedLine Operation**: Extensive infostealer malware campaign with administrator extradited to the United States
- **LeakBase Forum**: Major cybercrime marketplace for stolen data and hacking tools, with suspected owner arrested in Russia
- **Xinbi Marketplace**: Chinese-language cryptocurrency marketplace selling stolen data, sanctioned by the UK