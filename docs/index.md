# Exploitation Report

## Executive Summary

North Korean state-sponsored threat actor Lazarus Group is actively exploiting a Windows zero-day vulnerability (CVE-2026-68820) to target defense-sector organizations through the Operation Dream Job campaign, achieving SYSTEM-level access and deploying novel backdoors. Simultaneously, a massive supply chain compromise involving 737 malicious Chrome VPN extensions has been discovered routing user traffic through attacker-controlled SOCKS5 proxies, primarily targeting Russian-speaking users seeking circumvent censorship tools.

Multiple critical infrastructure vulnerabilities are under active exploitation in the wild, including a VMware vCenter flaw (CVE-2026-593...) granting persistent remote access, a Cisco ASA/FTD denial-of-service vulnerability crashing VPN appliances remotely, and a Microsoft SharePoint vulnerability with publicly available proof-of-concept code already weaponized by attackers. Microsoft's August 2026 Patch Tuesday addressed 398 vulnerabilities including a Windows kernel driver zero-day under active attack, while researchers disclosed the "ShieldBreak" Microsoft Defender zero-day and "Plug and Pwn" USB-based SYSTEM privilege escalation technique.

## Active Exploitation Details

### Windows Kernel Driver Zero-Day (CVE-2026-68820)
- **Description**: A zero-day vulnerability in a core Windows kernel driver handling network socket operations, allowing attackers to escalate privileges to SYSTEM level
- **Impact**: Full SYSTEM access on compromised Windows hosts, enabling deployment of persistent backdoors and lateral movement
- **Status**: Actively exploited by Lazarus Group against defense-sector targets; patched in Microsoft August 2026 Patch Tuesday
- **CVE ID**: CVE-2026-68820

### VMware vCenter Critical Vulnerability
- **Description**: A critical security flaw in Broadcom VMware vCenter allowing unauthenticated attackers to gain persistent remote access to virtualization management infrastructure
- **Impact**: Persistent remote access to vCenter servers, potential compromise of entire virtualized environments and associated workloads
- **Status**: Actively exploited in the wild per QUIRSO findings; patches available from Broadcom
- **CVE ID**: CVE-2026-593...

### Cisco ASA/FTD Denial-of-Service Vulnerability
- **Description**: High-severity DoS vulnerability in Secure Firewall ASA and Threat Defense (FTD) software exploitable remotely without authentication
- **Impact**: Remote device crashes causing VPN and firewall service disruption for affected organizations
- **Status**: Actively exploited in the wild to crash devices; Cisco has issued warnings and patches
- **CVE ID**: Not explicitly provided in source articles

### Microsoft SharePoint Vulnerability
- **Description**: Critical Microsoft SharePoint vulnerability with proof-of-concept exploit published by Rapid7, enabling remote code execution
- **Impact**: Potential full compromise of SharePoint servers and associated data; lateral movement into connected Microsoft 365 environments
- **Status**: PoC publicly available; hackers already leveraging exploit in attacks
- **CVE ID**: Not explicitly provided in source articles

### Microsoft Defender "ShieldBreak" Zero-Day
- **Description**: Zero-day exploit bypassing Microsoft Defender protections to achieve SYSTEM privileges, released by researcher Nightmare Eclipse (Chaotic Eclipse)
- **Impact**: Complete bypass of endpoint protection with SYSTEM-level code execution; affects patched August 2026 systems
- **Status**: PoC publicly released; Microsoft Defender patch bypass demonstrated
- **CVE ID**: Not explicitly provided in source articles

### Adobe ColdFusion and Campaign Classic Critical Flaws
- **Description**: Three maximum-severity (CVSS 10.0) vulnerabilities across Adobe ColdFusion, Commerce, and Campaign Classic products
- **Impact**: Unauthenticated arbitrary code execution leading to complete server compromise
- **Status**: Patches released by Adobe; exploitation status in wild not explicitly confirmed
- **CVE ID**: Not explicitly provided in source articles

### SAP Commerce Cloud Data Hub Adapter Flaw
- **Description**: Maximum-severity vulnerability in SAP Commerce Cloud (Data Hub Adapter) allowing unauthenticated arbitrary code execution
- **Impact**: Full server compromise without authentication requirements; exposure of commerce and customer data
- **Status**: Patches released by SAP; active exploitation not explicitly confirmed
- **CVE ID**: CVE identifier assigned but not provided in source articles

### Fortinet Vulnerabilities Exploited by Gunra Ransomware
- **Description**: Older flaws in Fortinet firewalls and VPN appliances being leveraged by Gunra ransomware-as-a-service operation
- **Impact**: Initial access to critical infrastructure targets with MFA bypass capabilities using leaked Conti code
- **Status**: Actively exploited in ransomware campaigns against critical infrastructure
- **CVE ID**: Not explicitly provided in source articles

### "Plug and Pwn" Windows Plug and Play Abuse
- **Description**: Attack technique abusing Windows Plug and Play feature to force installation of vulnerable vendor software, achieving SYSTEM privileges
- **Impact**: Local privilege escalation to SYSTEM via malicious USB devices or emulated hardware
- **Status**: Proof-of-concept disclosed by researchers; requires physical or virtual USB access
- **CVE ID**: Not explicitly provided in source articles

## Affected Systems and Products

- **Microsoft Windows**: All supported versions affected by kernel driver zero-day (CVE-2026-68820) and additional 397 vulnerabilities patched in August 2026; Windows kernel driver handling network sockets specifically targeted
- **Microsoft Defender**: August 2026 Patch Tuesday updates bypassed by ShieldBreak zero-day exploit
- **VMware vCenter**: Broadcom VMware vCenter servers vulnerable to CVE-2026-593... allowing persistent remote access
- **Cisco Secure Firewall ASA and FTD**: VPN and firewall appliances vulnerable to remote DoS exploitation causing device crashes
- **Microsoft SharePoint**: On-premises and cloud SharePoint instances affected by critical RCE vulnerability with public PoC
- **Adobe ColdFusion**: All supported versions with three CVSS 10.0 critical flaws enabling arbitrary code execution
- **Adobe Campaign Classic**: Affected by maximum-severity vulnerability in August 2026 security updates
- **Adobe Commerce**: Included in Adobe's critical patch release for arbitrary code execution flaws
- **SAP Commerce Cloud (Data Hub Adapter)**: Unauthenticated RCE vulnerability in cloud commerce platform component
- **Fortinet FortiGate Firewalls and VPN Appliances**: Older vulnerabilities exploited by Gunra ransomware gang with MFA bypass
- **Google Chrome Browser**: Chrome Web Store platform hosting 737 malicious VPN/proxy extensions with millions of potential installs
- **Android Devices**: Kimwolf v7/AISURU botnet targeting Android and IoT devices with HTTP/2 DDoS capabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Lazarus Group leveraging CVE-2026-68820 for initial access and privilege escalation to SYSTEM in targeted defense sector intrusions
- **Supply Chain Compromise**: 737 malicious Chrome extensions masquerading as legitimate VPN/proxy services, distributed via official Chrome Web Store to intercept and proxy browser traffic through attacker-controlled SOCKS5 infrastructure
- **Social Engineering / Operation Dream Job**: Lazarus Group using fake job offers targeting defense industry professionals to deliver payloads exploiting Windows zero-day
- **Trojanized Legitimate Software**: Sandworm (APT28) distributing trojanized WireGuard VPN clients via fake job offers targeting IT administrators and system administrators since May 2026
- **Public PoC Weaponization**: Rapid7-published SharePoint exploit PoC immediately adopted by threat actors for active attacks
- **USB/Plug and Play Abuse**: "Plug and Pwn" technique forcing Windows to install vulnerable vendor drivers via malicious USB device emulation for LOCAL SYSTEM escalation
- **Endpoint Protection Bypass**: ShieldBreak zero-day specifically targeting Microsoft Defender's protection mechanisms post-August 2026 patches
- **Ransomware with Blockchain Resilience**: DeadLock ransomware utilizing blockchain-backed decentralized infrastructure for C2 communications and data leak sites resistant to takedown
- **Credential Harvesting via Malicious Packages**: Malicious LiteLLM PyPI packages stealing cloud keys, SSH keys, Kubernetes tokens, and database passwords affecting 2,100+ organizations
- **AI Reasoning Extraction**: API flaw across OpenAI, Anthropic, and Google allowing recovery of hidden model reasoning, secrets, and API keys from session logs
- **HTTP/2 DDoS Obfuscation**: Kimwolf v7 botnet making volumetric attack traffic mimic legitimate browsing patterns to evade detection

## Threat Actor Activities

- **Lazarus Group (North Korea)**: Active exploitation of CVE-2026-68820 Windows zero-day in Operation Dream Job campaign targeting defense-sector companies; deploying never-before-seen backdoors with SYSTEM access; using social engineering via fake recruitment
- **Sandworm / APT28 (Russia)**: Targeting IT professionals and system administrators since May 2026 with trojanized WireGuard VPN clients distributed through fake job offers; focusing on high-value network access targets
- **Gunra Ransomware Gang**: Ransomware-as-a-service operation exploiting Fortinet firewall/VPN flaws and bypassing MFA using leaked Conti code; successfully targeting critical infrastructure organizations
- **Nightmare Eclipse / Chaotic Eclipse / INFINITE NIGHTMARE / MSNightmare**: Security researcher releasing ShieldBreak Microsoft Defender zero-day PoC demonstrating patch bypass with SYSTEM privileges
- **DeadLock Ransomware Operation**: Utilizing blockchain-based decentralized infrastructure for resilient C2 and data leak operations; novel approach to infrastructure takedown resistance
- **Kimwolf/AISURU Botnet Operators**: Deploying v7 Android/IoT botnet with enhanced HTTP/2 DDoS capabilities mimicking legitimate browser traffic for operational resilience
- **Unknown/Unattributed Actors**: Actively exploiting VMware vCenter (CVE-2026-593...), Cisco ASA/FTD DoS, and Microsoft SharePoint vulnerabilities in opportunistic campaigns; weaponizing public PoC code rapidly

## Source Attribution

- **Hundreds of fake Chrome VPN extensions route traffic through a proxy**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hundreds-of-fake-chrome-vpn-extensions-route-traffic-through-a-proxy/
- **Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor**: The Hacker News - https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html
- **Walmart's \&quot;Trusted Agent\&quot; Approach to Purple Teaming**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/walmart-trusted-agent-approach-purple-teaming
- **Plug and Pwn attack uses fake USB devices for Windows SYSTEM access**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/plug-and-pwn-attack-uses-fake-usb-devices-for-windows-system-access/
- **Lazarus hackers exploited Windows zero-day to target defense firms**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/
- **FBI: Hackers target online accounts to steal nude photos**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fbi-warns-of-hackers-targeting-online-accounts-to-steal-explicit-photos/
- **737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One**: The Hacker News - https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html
- **The Threat Hiding in Your Hiring Process: How Fake Remote Workers Get In**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-threat-hiding-in-your-hiring-process-how-fake-remote-workers-get-in/
- **Ransomware Hits Colombian Justice Ministry Days Before Presidential Transition**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/ransomware-hits-colombian-justice-ministry-presidential-transition
- **Walmart Leaders Transform Security Operations Without Going Bananas**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/walmart-leaders-transform-security-operations-without-going-bananas
- **Hackers leverage new Microsoft SharePoint exploit in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/hackers-leverage-new-microsoft-sharepoint-exploit-in-attacks/
- **OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning**: The Hacker News - https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html
- **Enterprise Defenses Recovered at the Edge and Collapsed Inside**: The Hacker News - https://thehackernews.com/2026/08/enterprise-defenses-recovered-at-edge.html
- **Signal adds new security feature to thwart man-in-the-middle attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/signal-adds-new-security-feature-to-thwart-man-in-the-middle-attacks/
- **Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws**: The Hacker News - https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html
- **New Microsoft Defender 'ShieldBreak' zero-day grants SYSTEM privileges**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldbreak-zero-day-grants-system-privileges/
- **Attackers Exploit VMware vCenter Vulnerability to Gain Persistent Remote Access**: The Hacker News - https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html
- **Malicious LiteLLM Releases Tied to Trivy Hack May Have Exposed 2,100+ Organizations**: The Hacker News - https://thehackernews.com/2026/08/malicious-litellm-releases-tied-to.html
- **SAP Commerce Cloud Flaw Could Let Unauthenticated Attackers Execute Arbitrary Code**: The Hacker News - https://thehackernews.com/2026/08/sap-commerce-cloud-flaw-could-let.html
- **ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access**: The Hacker News - https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
- **Cisco ASA and FTD Flaw Exploited in the Wild Can Trigger Remote DoS**: The Hacker News - https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html
- **Google says Chrome cuts 7 billion unwanted Android notifications a day to fight abuse**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/google-says-chrome-cuts-7-billion-unwanted-android-notifications-a-day-to-fight-abuse/
- **DeadLock ransomware uses blockchain to resist infrastructure takedown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/deadlock-ransomware-uses-blockchain-to-resist-infrastructure-takedown/
- **Microsoft's Patch Tuesday Deluge Continues With August Updates**: Dark Reading - https://www.darkreading.com/application-security/microsofts-patch-tuesday-deluge-continues
- **Microsoft Plugs Nearly 400 Security Holes**: Krebs on Security - https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/
- **Gunra Ransomware Gang Exploits Fortinet Flaws, Bypasses MFA**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/gunra-ransomware-gang-fortinet-flaws-bypasses-mfa
- **Sandworm hackers target IT pros with trojanized WireGuard VPN client**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/sandworm-hackers-target-it-pros-with-trojanized-wireguard-vpn-client/
- **Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack**: The Hacker News - https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html
- **Cisco warns of ASA and FTD VPN flaw exploited to crash devices**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/cisco-warns-of-asa-and-ftd-vpn-flaw-exploited-to-crash-devices/
- **Kimwolf v7 Android Botnet Makes HTTP/2 DDoS Traffic Look Like Legitimate Browsing**: The Hacker News - https://thehackernews.com/2026/08/kimwolf-v7-android-botnet-makes-http2.html
