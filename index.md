# Exploitation Report

Critical exploitation activity continues across multiple attack vectors, with several high-impact vulnerabilities being actively exploited by state-sponsored groups and cybercriminals. The most concerning developments include APT28's exploitation of a zero-day MSHTML vulnerability, ongoing attacks against Sangoma FreePBX instances through web shell deployment, and a sophisticated three-year campaign targeting Cisco SD-WAN infrastructure. North Korean threat actors remain highly active, deploying new toolsets for air-gapped network infiltration and conducting supply chain attacks through malicious npm packages. Additionally, security researchers have disclosed critical flaws in AI systems and cloud services that pose significant risks to enterprise environments.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A security flaw in Microsoft's MSHTML component that was exploited as a zero-day vulnerability before Microsoft's February 2026 Patch Tuesday
- **Impact**: Allows threat actors to execute arbitrary code and compromise targeted systems
- **Status**: Patched by Microsoft in February 2026, but was actively exploited before the patch release
- **CVE ID**: CVE-2026-21513

### Ivanti Connect Secure Zero-Day
- **Description**: A vulnerability in Ivanti Connect Secure devices that allows deployment of the RESURGE malware implant
- **Impact**: Enables persistent access to compromised systems with malware that can remain dormant on devices
- **Status**: Actively exploited with CISA issuing warnings about dormant infections
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: A command injection vulnerability affecting Sangoma FreePBX instances that allows web shell deployment
- **Impact**: Complete system compromise with persistent access through web shells
- **Status**: Over 900 instances remain compromised despite patches being available since December
- **CVE ID**: Not specified in articles

### Cisco SD-WAN Critical Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been under active exploitation
- **Impact**: Complete network infrastructure compromise by sophisticated threat actors
- **Status**: Exploited for three years by unknown advanced persistent threat actors
- **CVE ID**: CVE-2026-20127

### ClawJacked Vulnerability in OpenClaw AI
- **Description**: A high-severity flaw that allows malicious websites to hijack locally running OpenClaw AI agents via WebSocket connections
- **Impact**: Unauthorized access to AI agents, potential data theft and system compromise
- **Status**: Fixed by OpenClaw but represents emerging risks in AI security
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Microsoft MSHTML Component**: Core Windows component used in web rendering and Internet Explorer functionality
- **Ivanti Connect Secure**: Enterprise VPN and secure access solutions widely used in corporate environments
- **Sangoma FreePBX**: Open-source PBX software used for telecommunications infrastructure
- **Cisco SD-WAN**: Enterprise software-defined wide area network solutions
- **OpenClaw AI Agents**: Artificial intelligence automation tools running locally
- **Google Cloud API Keys**: Previously benign API keys now capable of accessing Gemini AI services
- **Chrome Extensions**: QuickLens extension compromised to deliver cryptocurrency theft malware
- **npm Package Registry**: 26 malicious packages distributed as part of North Korean supply chain attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: APT28 leveraging unpatched MSHTML vulnerabilities for targeted attacks
- **Web Shell Deployment**: Command injection attacks against FreePBX systems for persistent access
- **Supply Chain Compromise**: North Korean actors publishing malicious npm packages with Pastebin C2 infrastructure
- **WebSocket Hijacking**: Malicious websites exploiting AI agent communication protocols
- **USB-Based Air-Gap Bridging**: ScarCruft/APT37 using removable media to breach isolated networks
- **Browser Extension Compromise**: QuickLens extension modified to steal cryptocurrency wallets
- **API Key Abuse**: Legitimate Google Cloud keys repurposed for unauthorized Gemini AI access
- **ClickFix Social Engineering**: Fake error messages tricking users into executing malicious code

## Threat Actor Activities

- **APT28 (Russia-linked)**: Exploiting CVE-2026-21513 MSHTML zero-day vulnerability for targeted espionage operations
- **North Korean Actors (Contagious Interview Campaign)**: Publishing 26 malicious npm packages with cross-platform RAT capabilities using Pastebin for command and control
- **ScarCruft/APT37 (North Korea)**: Deploying new tools for air-gapped network infiltration using Zoho WorkDrive for C2 communications and USB-based malware propagation
- **Unknown Sophisticated Actor**: Conducting three-year exploitation campaign against Cisco SD-WAN infrastructure with minimal forensic evidence
- **Cybercriminals**: Compromising QuickLens Chrome extension to steal cryptocurrency from thousands of users
- **The Com Collective**: Online cybercrime group targeting children and teenagers, disrupted by Europol operation resulting in 30 arrests
- **Kimwolf Botnet Operators**: Running world's largest botnet through exploitation of disclosed vulnerability