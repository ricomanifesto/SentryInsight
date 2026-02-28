# Exploitation Report

Current threat landscape analysis reveals several critical exploitation activities across multiple platforms and industries. The most concerning developments include a zero-day vulnerability in Cisco SD-WAN systems that has been actively exploited for three years, ongoing attacks against over 900 Sangoma FreePBX instances through web shell deployment, and sophisticated North Korean threat actors deploying new malware tools to breach air-gapped networks. Additional critical concerns include the exposure of Google Cloud API keys that can be abused to access Gemini AI endpoints, and newly disclosed critical vulnerabilities in Trend Micro Apex One and Juniper Networks PTX routers that allow complete system compromise.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability that has been actively exploited by sophisticated threat actors for approximately three years
- **Impact**: Complete system compromise allowing attackers to gain unauthorized access to SD-WAN infrastructure
- **Status**: Under active exploitation with minimal forensic evidence left behind by attackers
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: A command injection vulnerability in FreePBX systems that allows attackers to deploy web shells for persistent access
- **Impact**: Complete system compromise with over 900 instances currently infected with web shells
- **Status**: Ongoing attacks with persistent infections remaining across affected systems

### Ivanti Connect Secure Zero-Day Vulnerability
- **Description**: Zero-day vulnerability exploited to deploy RESURGE malware implants on Ivanti devices
- **Impact**: Allows attackers to establish dormant persistent access to compromised systems
- **Status**: Active exploitation with malware capable of remaining dormant on affected devices
- **CVE ID**: CVE-2025-0282

### OpenClaw AI Agent WebSocket Vulnerability (ClawJacked)
- **Description**: High-severity security flaw allowing malicious websites to connect to locally running AI agents through WebSocket connections
- **Impact**: Complete hijacking of local OpenClaw AI agents by malicious websites
- **Status**: Fixed by OpenClaw, but represents novel attack vector against AI agents

### Trend Micro Apex One Remote Code Execution Flaws
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software
- **Impact**: Remote code execution capabilities on vulnerable Windows systems
- **Status**: Recently patched by Trend Micro

### Juniper Networks PTX Router Critical Vulnerability
- **Description**: Critical flaw in Junos OS Evolved running on PTX Series routers
- **Impact**: Allows unauthenticated remote code execution with root privileges, enabling complete router takeover
- **Status**: Newly disclosed critical vulnerability requiring immediate patching

## Affected Systems and Products

- **Cisco SD-WAN Systems**: All SD-WAN infrastructure components affected by three-year exploitation campaign
- **Sangoma FreePBX Instances**: Over 900 compromised systems with web shell infections
- **Ivanti Connect Secure**: Systems vulnerable to RESURGE malware deployment
- **OpenClaw AI Agents**: Local AI agent installations vulnerable to WebSocket hijacking
- **Trend Micro Apex One**: Windows systems running vulnerable versions of the security software
- **Juniper Networks PTX Routers**: All PTX Series routers running vulnerable Junos OS Evolved versions
- **Google Cloud API Services**: Thousands of exposed API keys with Gemini access capabilities
- **Air-Gapped Networks**: Systems targeted by North Korean threat actors using USB-based malware

## Attack Vectors and Techniques

- **WebSocket Hijacking**: Malicious websites exploiting ClawJacked vulnerability to connect to local AI agents
- **Web Shell Deployment**: Command injection attacks against FreePBX systems for persistent access
- **USB-Based Malware Propagation**: North Korean actors using removable drives to bridge air-gapped networks
- **Blockchain-Based C2 Infrastructure**: Aeternum C2 botnet using Polygon blockchain to store encrypted commands
- **Third-Party Cloud Service Abuse**: ScarCruft using Zoho WorkDrive for command-and-control communications
- **API Key Abuse**: Previously harmless Google Cloud API keys being weaponized for Gemini AI access
- **Trojanized Gaming Tools**: Distribution of Java-based RATs through gaming utilities on browsers and chat platforms
- **Supply Chain Compromise**: Malicious Go modules designed to harvest passwords and deploy Rekoobe backdoor

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks using USB propagation methods
- **ScarCruft (North Korean)**: Using Zoho WorkDrive and USB malware to compromise air-gapped systems with fresh toolsets
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **Kimwolf Botmaster "Dort"**: Operating the world's largest and most disruptive botnet through exploited vulnerabilities
- **Sophisticated Unknown Actor**: Exploiting Cisco SD-WAN zero-day for three years while leaving minimal forensic evidence
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, with 30 arrests made in Europol-led operation
- **Cryptocurrency Scammers**: Exploiting exposed Korean tax agency wallet seeds to steal $4.8 million in crypto assets