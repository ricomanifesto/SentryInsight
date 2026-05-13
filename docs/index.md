# Exploitation Report

The current threat landscape is dominated by sophisticated supply chain attacks targeting package managers and developer ecosystems. Multiple campaigns have emerged targeting RubyGems, npm, and PyPI repositories with malicious packages designed for data exfiltration and credential theft. Notable incidents include the GemStuffer campaign compromising over 150 RubyGems packages to exfiltrate UK council portal data, and the Shai-Hulud attack affecting hundreds of packages across npm and PyPI. Critical vulnerabilities have also been disclosed in enterprise systems, including remote code execution flaws in Fortinet products and mail transfer agents, while major data breaches continue to impact educational institutions and automotive companies. The threat actor ShinyHunters has been particularly active, conducting extortion attacks against educational technology platforms affecting millions of users.

## Active Exploitation Details

### GemStuffer Campaign - RubyGems Repository Attack
- **Description**: A malicious campaign that uploaded over 150 malicious gems to the RubyGems repository, using the registry as a data exfiltration channel
- **Impact**: Successful exfiltration of scraped UK council portal data through compromised Ruby packages
- **Status**: Active campaign targeting the Ruby ecosystem with ongoing malicious package uploads

### Shai-Hulud Supply Chain Attack
- **Description**: A large-scale supply chain attack compromising hundreds of packages across npm and PyPI repositories, delivering credential-stealing malware
- **Impact**: Credential theft targeting developers and potential compromise of downstream applications
- **Status**: Active campaign with fresh infections affecting TanStack, Mistral AI, Guardrails AI, UiPath, and OpenSearch packages

### TrickMo Android Banking Trojan
- **Description**: New variant of Android banking malware using The Open Network (TON) for command-and-control communications
- **Impact**: Banking credential theft and creation of network pivots through SOCKS5 proxies on compromised Android devices
- **Status**: Active in the wild with enhanced evasion capabilities

### Fortinet Critical Remote Code Execution Vulnerabilities
- **Description**: Critical vulnerabilities in FortiSandbox and FortiAuthenticator products enabling remote command execution
- **Impact**: Attackers can execute arbitrary commands or code on affected Fortinet security appliances
- **Status**: Patches released by Fortinet

### Exim BDAT Vulnerability in GnuTLS Builds
- **Description**: Severe security issue in Exim mail transfer agent affecting GnuTLS configurations, leading to memory corruption
- **Impact**: Potential remote code execution on mail servers running affected Exim configurations
- **Status**: Security updates released by Exim

## Affected Systems and Products

- **RubyGems Repository**: Over 150 malicious gems uploaded, registry temporarily suspending new signups
- **npm and PyPI Packages**: Hundreds of packages compromised including TanStack, Mistral AI, Guardrails AI, UiPath, and OpenSearch
- **Android Devices**: Targeted by TrickMo banking trojan with enhanced network pivot capabilities
- **Fortinet Products**: FortiSandbox and FortiAuthenticator affected by critical RCE vulnerabilities
- **Exim Mail Servers**: GnuTLS builds vulnerable to memory corruption and potential code execution
- **Canvas Learning Management System**: 3.65TB of data stolen from Instructure's educational platform
- **Hugging Face AI Models**: Tokenizer library files vulnerable to manipulation for data exfiltration
- **SAP Systems**: Commerce Cloud and S/4HANA affected by critical vulnerabilities
- **Škoda Online Shop**: Customer data compromised through website breach

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages uploaded to legitimate repositories (RubyGems, npm, PyPI) to compromise downstream users
- **Data Exfiltration via Package Repositories**: Using legitimate package management infrastructure as covert communication channels
- **Mobile Banking Malware**: Android trojans using encrypted messaging platforms (TON) for C2 communications
- **SOCKS5 Proxy Creation**: Establishing network pivots through compromised mobile devices
- **AI Model Manipulation**: Weaponizing Hugging Face tokenizer files to hijack model outputs
- **Memory Corruption Exploits**: Targeting mail transfer agents through protocol-specific vulnerabilities
- **Credential Harvesting**: Self-propagating worms designed to steal developer credentials and API keys

## Threat Actor Activities

- **TeamPCP**: Responsible for the Shai-Hulud supply chain attacks, demonstrating sophisticated package compromise techniques across multiple ecosystems
- **GemStuffer Campaign Operators**: Conducted targeted data exfiltration against UK council portals using RubyGems as infrastructure
- **ShinyHunters Extortion Group**: Successfully breached Instructure's Canvas platform, stealing 3.65TB of data and reaching a ransom agreement to prevent data leak
- **TrickMo Developers**: Enhanced their Android banking trojan with TON-based C2 communications and SOCKS5 proxy capabilities for improved persistence and evasion