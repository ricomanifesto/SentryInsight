# Exploitation Report

Over the past week, threat actors have intensified real-world exploitation of several high-impact vulnerabilities, focusing on widely-deployed network infrastructure and cloud-native platforms. Chinese state-sponsored operators (“Salt Typhoon”) are abusing a critical Cisco flaw to compromise Canadian telecom networks, while Docker hosts with exposed APIs are being hijacked at scale for covert cryptocurrency mining over Tor. In parallel, a newly-uncovered Windows LNK vulnerability is weaponized by the XDigo malware against Eastern-European governments, and fresh Citrix NetScaler ADC/Gateway bugs are already drawing attacker attention. Russian APT28 continues to evolve its tradecraft, delivering BEARDSHELL and COVENANT malware through Signal chat, highlighting the blend of social-engineering and zero-click exploitation vectors now in active use.

## Active Exploitation Details

### Misconfigured Docker Remote API Cryptocurrency Mining
- **Description**: Attackers scan for Docker Engine hosts that expose the Remote API without authentication, then programmatically deploy malicious containers that download and run cryptocurrency-mining payloads. Tor is embedded for C2 and payout anonymization.  
- **Impact**: Full control over container workloads, unauthorized consumption of compute resources, potential lateral movement to host OS and adjacent containers.  
- **Status**: Ongoing global campaign with significant traffic spikes observed; no vendor patch—mitigation requires disabling unauthenticated APIs and applying least-privilege network controls.

### Critical Cisco Network Device Vulnerability Exploited by “Salt Typhoon”
- **Description**: A critical flaw in Cisco enterprise networking software allows unauthenticated remote command execution on edge routers/switches via the web management interface. Salt Typhoon leveraged it to breach a major Canadian telecom and siphon sensitive network data.  
- **Impact**: Device takeover, configuration manipulation, traffic interception, and pivoting into internal telecom infrastructure.  
- **Status**: Cisco has released patches and guidance; exploitation remains active against unpatched or unmonitored devices.

### Windows LNK Shortcut Processing Flaw Leveraged by XDigo
- **Description**: Malformed Windows shortcut (​.lnk) files trigger code execution when rendered by Windows Explorer. The Go-based XDigo loader embeds the exploit to install additional payloads and evade user interaction.  
- **Impact**: Initial execution on target workstations, credential theft, persistent backdoors, and data exfiltration from government networks.  
- **Status**: Exploits observed in March 2025; Microsoft updates are available, but XDigo continues to succeed where patching lags.

### Citrix NetScaler ADC and Gateway Critical Vulnerabilities
- **Description**: Recently disclosed remote-code-execution and session hijacking bugs in NetScaler appliances enable attackers to bypass authentication, steal session tokens, and run arbitrary commands on the underlying BSD OS.  
- **Impact**: Complete appliance compromise, decryption of VPN traffic, installation of web shells, and lateral movement into corporate environments.  
- **Status**: Citrix has issued fixed builds; preliminary exploit code has surfaced, and limited in-the-wild activity has been detected against outdated instances.

## Affected Systems and Products

- **Cisco Enterprise Routers & Switches**: Devices running vulnerable IOS XE / networking OS builds  
  - **Platform**: Carrier-grade and enterprise network edge environments  

- **Docker Engine Hosts**: Any version with the TCP Remote API exposed without authentication  
  - **Platform**: Linux-based container servers in cloud, on-prem, and hybrid infrastructures  

- **Microsoft Windows Desktops & Servers**: Versions vulnerable to the current LNK parsing flaw  
  - **Platform**: Government and enterprise Windows environments  

- **Citrix NetScaler ADC / Gateway**: Appliances prior to the latest security release  
  - **Platform**: Data-center and cloud edge load balancers, VPN gateways  

- **Signal Desktop & Mobile Clients (delivery vector)**: Used by APT28 to push malicious files  
  - **Platform**: Windows endpoints and Android devices within Ukrainian government networks  

## Attack Vectors and Techniques

- **Unauthenticated API Exposure**  
  - **Vector**: Direct Internet access to Docker Remote API (port 2375/2376) without TLS or auth  

- **Remote Web-Interface RCE**  
  - **Vector**: Crafted HTTP/S requests to vulnerable Cisco management endpoints  

- **Malicious LNK Files**  
  - **Vector**: Weaponized shortcut embedded in spear-phishing archives; code executes on preview  

- **Session Token Hijacking in NetScaler**  
  - **Vector**: Exploit grabs live authentication cookies, enabling password-less VPN entry  

- **Encrypted Instant-Messenger Delivery**  
  - **Vector**: APT28 sends weaponized archives via Signal chats, bypassing traditional email filters  

## Threat Actor Activities

- **Salt Typhoon (China-linked)**
  - **Campaign**: Targeted Canadian telecom provider; exploitation of Cisco vulnerability for espionage and network foothold expansion.

- **APT28 / UAC-0001 (Russia-linked)**
  - **Campaign**: Uses Signal messenger to deliver BEARDSHELL and COVENANT malware, focusing on Ukrainian government entities; blends social engineering with new delivery channels.

- **Cryptocurrency Miner Operators (overlapping with “Commando Cat” TTPs)**
  - **Campaign**: Mass-exploitation of Docker APIs, deployment of mining containers, Tor-based C2 for stealth and resilience.

- **XDigo Operators (currently unattributed)**
  - **Campaign**: Spear-phishing attacks on Eastern-European governments; weaponizes Windows LNK flaw to gain initial access and exfiltrate sensitive data.

- **Unidentified Threat Actors Exploiting Citrix NetScaler**
  - **Campaign**: Early probing and limited exploitation of newly disclosed NetScaler vulnerabilities, likely gearing up for broader ransomware or espionage operations.

