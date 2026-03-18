# Exploitation Report

The current threat landscape reveals several critical exploitation activities spanning supply chain attacks, ransomware operations, AI platform vulnerabilities, and targeted campaigns against infrastructure. Most notably, CISA has flagged an actively exploited Wing FTP Server vulnerability that is being used in the wild, while the GlassWorm malware campaign has evolved to target hundreds of code repositories across GitHub, npm, and VSCode platforms. Ransomware groups like LeakNet and Warlock have adopted sophisticated new techniques including ClickFix social engineering and BYOVD (Bring Your Own Vulnerable Driver) methods. Additionally, AI platforms including Amazon Bedrock, LangSmith, and SGLang have been found to contain critical flaws enabling data exfiltration and remote code execution.

## Active Exploitation Details

### Wing FTP Server Information Disclosure Vulnerability
- **Description**: A medium-severity security flaw in Wing FTP Server that allows attackers to leak server path information
- **Impact**: Server path disclosure that may be chained with other vulnerabilities to achieve remote code execution
- **Status**: Actively exploited in the wild according to CISA; added to Known Exploited Vulnerabilities (KEV) catalog

### GlassWorm Supply Chain Attack
- **Description**: Evolved malware campaign targeting code repositories and development environments using stolen GitHub tokens to force-push malicious code
- **Impact**: Injection of malware into hundreds of Python repositories, VSCode extensions, and npm packages affecting software supply chain integrity
- **Status**: Ongoing active campaign with new evasion techniques hiding malware in dependencies

### AI Platform Vulnerabilities in Amazon Bedrock, LangSmith, and SGLang
- **Description**: Multiple flaws in AI code execution environments enabling DNS-based data exfiltration techniques
- **Impact**: Sensitive data exfiltration from AI environments and potential remote code execution capabilities
- **Status**: Newly disclosed vulnerabilities affecting major AI platforms

## Affected Systems and Products

- **Wing FTP Server**: All versions affected by the information disclosure vulnerability
- **GitHub Repositories**: Hundreds of Python projects compromised via stolen tokens
- **VSCode/OpenVSX Extensions**: Multiple malicious extensions distributed through official channels
- **npm Package Registry**: Compromised packages affecting JavaScript/Node.js ecosystems
- **Amazon Bedrock**: AI service vulnerable to data exfiltration attacks
- **LangSmith**: AI development platform with code execution vulnerabilities
- **SGLang**: AI framework susceptible to DNS-based data theft
- **Microsoft Exchange Online**: Service outages affecting mailbox and calendar access
- **Samsung Galaxy Book 4**: Windows 11 devices experiencing C: drive access issues
- **Companies House WebFiling**: UK government business registry service

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: LeakNet ransomware using fake error messages to trick users into downloading malware
- **BYOVD (Bring Your Own Vulnerable Driver)**: Warlock ransomware group using legitimate but vulnerable drivers for post-exploitation activities
- **DNS Data Exfiltration**: Novel technique for extracting sensitive data from AI code execution environments
- **Stolen Token Abuse**: GlassWorm attackers using compromised GitHub tokens to inject malware into repositories
- **Deno Runtime Loader**: LeakNet deploying in-memory malware loaders based on JavaScript/TypeScript runtime
- **Font Rendering Attacks**: New technique to hide malicious commands from AI tools using HTML font manipulation
- **KakaoTalk Propagation**: Malware spreading through compromised messaging application contacts
- **Phishing with Trusted Brands**: Multi-stage attacks impersonating legitimate services like PayPal and Amazon

## Threat Actor Activities

- **LeakNet Ransomware Group**: Adopting ClickFix techniques delivered through compromised websites and deploying Deno-based in-memory loaders for stealthier operations
- **Warlock Ransomware Group**: Enhancing post-exploitation capabilities with BYOVD techniques for more persistent and stealthy cross-network activities
- **GlassWorm Operators**: Conducting sophisticated supply chain attacks targeting development environments with evolved evasion techniques
- **Konni (North Korean APT)**: Deploying EndRAT through spear-phishing campaigns and using KakaoTalk desktop applications to propagate malware to victim contacts
- **China-Nexus Groups**: Conducting extensive cyber espionage campaigns against Southeast Asian military organizations with persistent access maintained for years using novel backdoors
- **European Sanctioned Entities**: Chinese and Iranian firms targeted for sanctions due to cyberattacks against European critical infrastructure