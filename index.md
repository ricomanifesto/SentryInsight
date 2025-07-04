# Exploitation Report

Coordinated exploitation activity is surging against widely-deployed edge and mail-server infrastructure. A newly profiled threat actor dubbed **NightEagle (APT-Q-95)** is weaponizing a previously unknown Microsoft Exchange Server flaw to breach Chinese military and technology entities, while **China-nexus operators** are chaining two zero-day bugs in Ivanti Connect Secure appliances to compromise French government, telecom, and transport networks. In some cases, the intruders are **“self-patching”** the Ivanti devices after gaining access, blocking competitors and complicating incident response. Both campaigns enable remote code execution (RCE), persistent footholds, and broad lateral movement, underscoring the high risk to any organization still running unpatched Exchange or Ivanti edge VPN gear.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day Exploited by NightEagle
- **Description**: An undocumented vulnerability in on-premises Exchange allows unauthenticated remote attackers to execute arbitrary code via specially crafted requests to the Outlook Web Access (OWA) interface. NightEagle leverages it to drop web shells and a bespoke backdoor.
- **Impact**: Full server takeover, email and attachment exfiltration, credential dumping, and pivoting into internal networks that house sensitive R&D and defense data.
- **Status**: Confirmed in-the-wild exploitation; Microsoft has not yet issued a formal patch. Mitigations revolve around disabling exposed OWA endpoints and enhanced monitoring of Exchange IIS logs.

### Ivanti Connect Secure / Policy Secure Zero-Days (Auth Bypass + Command Injection)
- **Description**: Two chained vulnerabilities—first an authentication bypass on the web administrative interface, followed by a command-injection flaw—allow attackers to gain root-level access on Ivanti Secure Access appliances.
- **Impact**: Remote code execution, credential harvesting, installation of web shells, network tunneling, and the ability to compromise downstream assets using legitimate VPN sessions.
- **Status**: Active exploitation against French government, telecom, finance, media, and transport sectors. Ivanti has released emergency patches and signatures; however, threat actors are observed patching the devices themselves post-breach to monopolize access.

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premises editions exposed to the Internet (2013, 2016, 2019)  
  **Platform**: Windows Server environments, typically in enterprise and government networks  

- **Ivanti Connect Secure (formerly Pulse Secure) & Ivanti Policy Secure Appliances**: All supported hardware and virtual models prior to the out-of-band fix  
  **Platform**: Purpose-built VPN/Zero Trust gateways deployed in corporate DMZs  

## Attack Vectors and Techniques

- **OWA Web-Shell Planting**  
  - **Vector**: Crafted HTTP(S) requests against `/owa/` endpoints exploit the Exchange zero-day, write web shells into the `FrontEnd\HttpProxy` path, then issue authenticated commands.

- **Authentication Bypass → Command Injection Chain**  
  - **Vector**: Public-facing Ivanti admin portal receives a forged session token that bypasses auth controls; subsequent POST request injects shell commands executed with root privileges.

- **Self-Patching / Turf-Locking**  
  - **Vector**: After establishing root access on Ivanti gateways, the attacker installs official vendor patches to close the very zero-days they used, preventing detection and rival intrusions.

## Threat Actor Activities

- **NightEagle (APT-Q-95)**  
  - **Campaign**: Targeting Chinese aerospace, defense R&D, and semiconductor firms since April 2025. Uses custom loader “FeatherDrop” to deploy in-memory C2 implants; exfiltrates engineering documents and military comms.

- **China-nexus Operators Leveraging Ivanti Zero-Days**  
  - **Campaign**: Multi-wave intrusion set observed by the French National Cybersecurity Agency (ANSSI). Objectives include reconnaissance of governmental networks, collection of telecom subscriber data, and persistence for long-term espionage.

- **Initial Access Broker (Unnamed, possibly overlapping with above)**  
  - **Campaign**: Monetizes footholds by selling VPN-level access on underground forums. Notably patches the exploited Ivanti appliances post-compromise, illustrating a “defensive” offensive tactic to maintain exclusive control over victim environments.

---

**Stay vigilant:** Prioritize patching or isolating Exchange and Ivanti edge systems, deploy additional web-shell detection rules, and monitor for anomalous administrative or VPN activity.