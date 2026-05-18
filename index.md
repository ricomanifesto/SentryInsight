# Exploitation Report

Critical exploitation activity is currently targeting multiple systems with several active zero-day vulnerabilities and recently disclosed flaws being leveraged by threat actors. The most significant threats include a Windows privilege escalation zero-day dubbed "MiniPlasma" allowing SYSTEM access on fully patched systems, active exploitation of NGINX servers causing worker crashes and potential remote code execution via CVE-2026-42945, and ongoing attacks against Microsoft Exchange Server through CVE-2026-42897. Additional critical activity involves WordPress plugin vulnerabilities being exploited for credit card skimming, supply chain attacks targeting npm packages and AI codebases, and Russian state-sponsored actors evolving their Kazuar backdoor into a sophisticated P2P botnet infrastructure.

## Active Exploitation Details

### Windows MiniPlasma Privilege Escalation Zero-Day
- **Description**: A privilege escalation vulnerability in Windows systems that allows attackers to gain SYSTEM privileges on fully patched Windows installations
- **Impact**: Complete system compromise with highest level administrative access
- **Status**: Zero-day vulnerability with proof-of-concept exploit publicly released, no patch currently available

### NGINX Server Vulnerability
- **Description**: A security flaw affecting both NGINX Plus and NGINX Open that enables worker process crashes and potential remote code execution
- **Impact**: Service disruption, denial of service, and possible complete server compromise
- **Status**: Under active exploitation in the wild following public disclosure
- **CVE ID**: CVE-2026-42945

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: A high-severity vulnerability in on-premise Exchange Server versions that allows arbitrary code execution through crafted email-based cross-site scripting attacks
- **Impact**: Arbitrary code execution on Exchange servers through malicious email messages
- **Status**: Actively exploited in attacks, mitigations available
- **CVE ID**: CVE-2026-42897

### Cisco SD-WAN Controller Authentication Bypass
- **Description**: Maximum severity vulnerability in Cisco Catalyst SD-WAN Controller allowing unauthorized administrative access
- **Impact**: Complete administrative control over network infrastructure
- **Status**: Actively exploited, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Critical Vulnerability
- **Description**: Critical security flaw in the Funnel Builder plugin for WordPress enabling injection of malicious JavaScript into WooCommerce checkout pages
- **Impact**: Credit card data theft and financial fraud through checkout page skimming
- **Status**: Under active exploitation for payment card skimming attacks

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the WordPress Burst Statistics plugin
- **Impact**: Admin-level access to WordPress websites
- **Status**: Actively exploited by hackers to gain unauthorized administrative access

## Affected Systems and Products

- **Windows Systems**: All fully patched Windows installations vulnerable to MiniPlasma privilege escalation
- **NGINX Servers**: Both NGINX Plus and NGINX Open installations affected by worker crash vulnerability
- **Microsoft Exchange Server**: On-premise Exchange Server installations vulnerable to email-based XSS attacks
- **Cisco SD-WAN Infrastructure**: Cisco Catalyst SD-WAN Controller systems experiencing unauthorized access
- **WordPress Websites**: Sites using Funnel Builder and Burst Statistics plugins under active attack
- **npm Package Ecosystem**: node-ipc package compromised affecting Node.js applications
- **OpenAI Corporate Environment**: Two employee devices compromised through TanStack supply chain attack
- **Avada Builder Plugin**: WordPress sites with estimated one million installations at risk of credential theft

## Attack Vectors and Techniques

- **Privilege Escalation**: MiniPlasma zero-day exploit providing SYSTEM-level access on Windows
- **Email-Based Exploitation**: Crafted emails targeting Exchange Server XSS vulnerability
- **Supply Chain Attacks**: Compromised npm packages and JavaScript libraries targeting developer environments
- **Web Application Injection**: Malicious JavaScript injection into WordPress e-commerce checkout processes
- **Device Code Phishing**: Microsoft 365 account hijacking through Tycoon2FA phishing kit abuse
- **Authentication Bypass**: Direct administrative access through plugin vulnerabilities
- **P2P Botnet Infrastructure**: Modular peer-to-peer networks for persistent access and stealth operations
- **Session Token Theft**: Browser session and authentication token stealing via REMUS infostealer

## Threat Actor Activities

- **Turla/Secret Blizzard**: Russian state-sponsored group evolved Kazuar backdoor into modular P2P botnet for long-term persistence and data collection
- **TeamPCP**: Hacker group threatening to leak Mistral AI source code repositories unless buyers are found
- **Tycoon2FA Operators**: Enhanced phishing kit targeting Microsoft 365 accounts through device-code attacks and Trustifi URL abuse
- **WordPress Plugin Attackers**: Multiple threat actors exploiting plugin vulnerabilities for financial gain through credit card skimming
- **Supply Chain Attackers**: Targeting software development ecosystems through compromised packages and repositories
- **REMUS Infostealer Operators**: Focus on session theft and authentication token harvesting for scalable credential access
- **Exchange Server Attackers**: Leveraging email-based XSS vulnerabilities for server compromise
- **Cisco Infrastructure Attackers**: Exploiting maximum severity SD-WAN vulnerabilities for network control