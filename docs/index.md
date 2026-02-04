# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact vulnerabilities actively being exploited in the wild. CISA has flagged a critical SolarWinds Web Help Desk remote code execution flaw as actively exploited and added it to the Known Exploited Vulnerabilities catalog, ordering federal agencies to patch within three days. Russian state-sponsored threat actor APT28 has rapidly weaponized CVE-2026-21509, a Microsoft Office vulnerability, deploying specially crafted RTF documents in espionage campaigns within just three days of the exploit becoming available. Additionally, threat actors are actively exploiting CVE-2025-11953 in the React Native Metro Development Server, targeting developers through malicious npm packages. A coordinated reconnaissance campaign is also targeting Citrix NetScaler infrastructure using thousands of residential proxies to discover login panels for potential exploitation.

## Active Exploitation Details

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical security flaw in SolarWinds Web Help Desk (WHD) that allows attackers to execute arbitrary code remotely
- **Impact**: Complete system compromise, unauthorized access to help desk systems and potentially connected infrastructure
- **Status**: Actively exploited in attacks, CISA has mandated federal agencies patch within three days

### Microsoft Office Rich Text Format Vulnerability
- **Description**: Security flaw in Microsoft Office that can be exploited through specially crafted Rich Text Format (RTF) documents
- **Impact**: Enables multistage infection chain for malicious payload delivery in espionage operations
- **Status**: Recently patched but actively exploited by APT28 within three days of disclosure
- **CVE ID**: CVE-2026-21509

### React Native Metro Development Server Vulnerability
- **Description**: Critical flaw in the Metro Development Server within the "@react-native-community/cli" npm package
- **Impact**: Remote code execution on developer systems, malicious payload delivery for Windows and Linux
- **Status**: Actively exploited to target developers through malicious npm packages
- **CVE ID**: CVE-2025-11953

### Docker Ask Gordon AI Vulnerability
- **Description**: Security flaw in Ask Gordon AI assistant built into Docker Desktop and Command-Line Interface allowing code execution via image metadata manipulation
- **Impact**: Code execution through manipulation of container image metadata
- **Status**: Patched by Docker

## Affected Systems and Products

- **SolarWinds Web Help Desk**: Critical vulnerability affecting help desk infrastructure
- **Microsoft Office**: Multiple versions vulnerable to RTF-based attacks through CVE-2026-21509
- **React Native Development Environment**: "@react-native-community/cli" npm package with Metro server vulnerability
- **Docker Desktop and CLI**: Ask Gordon AI assistant component
- **Citrix NetScaler**: Infrastructure being targeted in coordinated reconnaissance campaigns
- **macOS Systems**: Targeted by Python-based infostealers and GlassWorm malware through compromised OpenVSX extensions
- **Notepad++ Hosting Infrastructure**: Compromised for six months to redirect targeted users to malicious downloads

## Attack Vectors and Techniques

- **Malicious RTF Documents**: APT28 uses specially crafted Rich Text Format documents to initiate infection chains
- **Fake Advertising and Installers**: Python-based infostealers targeting macOS through deceptive installation packages
- **Compromised npm Packages**: Exploitation of React Native Metro vulnerability through malicious packages
- **Supply Chain Attacks**: GlassWorm malware distributed through poisoned OpenVSX software components
- **Residential Proxy Networks**: Thousands of residential proxies used for Citrix NetScaler reconnaissance
- **Container Image Metadata**: Exploitation of Docker AI assistant through manipulated image metadata
- **Hosting Provider Compromise**: Notepad++ updates redirected through compromised hosting infrastructure
- **Phishing Campaigns**: Fake PDF lures used to harvest Dropbox credentials in malware-free attacks

## Threat Actor Activities

- **APT28 (UAC-0001)**: Russian state-sponsored group rapidly weaponizing Microsoft Office CVE-2026-21509 in espionage campaigns codenamed operations
- **Lotus Blossom**: China-linked threat actor attributed with medium confidence to Notepad++ hosting infrastructure compromise lasting six months
- **Unknown Threat Actors**: Coordinated reconnaissance campaign against Citrix NetScaler using residential proxy networks for login panel discovery
- **Criminal Groups**: Exploiting React Native Metro vulnerability to target developers with malicious payloads across Windows and Linux platforms
- **Everest Extortion Gang**: Claimed responsibility for Iron Mountain data breach, though impact appears limited to marketing materials
- **Insider Threats**: Coinbase contractor improperly accessed approximately thirty customer records in December incident