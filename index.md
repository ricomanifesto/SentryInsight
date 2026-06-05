# Exploitation Report

Current cybersecurity landscape reveals critical exploitation activity targeting enterprise infrastructure and software supply chains. Most concerning is the active exploitation of CVE-2026-20245, an unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager enabling root privilege escalation. Additional active threats include exploitation of a critical WordPress plugin flaw leading to complete site compromise, ongoing supply chain attacks targeting npm packages with IronWorm malware, and sophisticated web shell frameworks targeting Microsoft IIS servers. The threat landscape is further complicated by AI-powered attack vectors and malvertising campaigns deploying advanced backdoors across multiple platforms.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity vulnerability in Cisco Catalyst SD-WAN Manager allowing unauthorized privilege escalation
- **Impact**: Attackers can gain root-level access to network infrastructure devices
- **Status**: Currently unpatched and actively exploited in the wild
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in WordPress plugin with approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution
- **Status**: Actively exploited by threat actors

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: Authentication bypass vulnerability allowing file write operations leading to root access
- **Impact**: Unauthenticated attackers can write files and escalate to root privileges
- **Status**: Recently patched with public exploit code available
- **CVE ID**: CVE-2026-20230

### Claude Code GitHub Action Repository Hijacking
- **Description**: Vulnerability in Anthropic's Claude Code GitHub Action
- **Impact**: Complete repository takeover through malicious GitHub issues
- **Status**: Actively exploitable against public repositories

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Zero-day vulnerability enabling root access
- **WordPress Everest Forms Pro Plugin**: Critical flaw affecting ~4,000 installations
- **Cisco Unified Communications Manager**: File write vulnerability with public exploits
- **Microsoft Internet Information Services (IIS)**: Targeted by OP-512 threat cluster
- **npm Package Registry**: 36 packages infected with IronWorm malware
- **Hola Browser for Windows**: Compromised in supply chain attack delivering cryptocurrency miners
- **GitHub Repositories**: Vulnerable to takeover via Claude Code Action flaw
- **Automatic Tank Gauge (ATG) Systems**: Over 900 US gas station systems exposed online

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Unpatched Cisco SD-WAN vulnerability being actively exploited
- **Supply Chain Attacks**: IronWorm malware targeting npm ecosystem and browser software
- **Web Shell Deployment**: Custom framework targeting IIS servers for persistent access
- **Malvertising Campaigns**: FlutterShell backdoor distributed via malicious Google and YouTube ads
- **Phishing Operations**: TA4922 expanding global reach with sophisticated campaigns
- **Repository Hijacking**: Single malicious GitHub issues compromising entire repositories
- **Magecart Campaigns**: Credit card theft using Stripe API infrastructure for hosting payloads

## Threat Actor Activities

- **OP-512 Threat Cluster**: Previously unreported group targeting Microsoft IIS servers with custom web shell frameworks for persistent access and lateral movement
- **PCPJack**: Hijacked 230 cloud servers across AWS, Google Cloud, and Azure to create covert SMTP relay networks for malicious email operations
- **TA4922 (China-linked)**: Expanded phishing attacks from East Asia to UK, Germany, Italy, and South Africa, demonstrating global operational capabilities
- **Operation FlutterBridge**: macOS malvertising campaign deploying FlutterShell backdoor through compromised Google and YouTube advertisements
- **IronWorm Campaign**: Rust-written malware targeting developers through npm supply chain, stealing credentials for further propagation across software development environments