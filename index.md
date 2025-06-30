# Exploitation Report

Recent threat-hunting investigations highlight an urgent need to patch Citrix NetScaler appliances and Progress MOVEit Transfer servers as attackers weaponize multiple critical flaws. “Citrix Bleed 2” (CVE-2025-5777) is now under confirmed, in-the-wild exploitation, while a previously disclosed authentication-bypass weakness in NetScaler ADC/Gateway remains unpatched on more than 1,200 internet-facing devices. Concurrently, GreyNoise telemetry shows renewed scanning for MOVEit Transfer SQL-injection bugs, signalling imminent follow-on breaches similar to the 2023 mass-extortion wave. Additional reports warn of exploitable Bluetooth chipset vulnerabilities that permit surreptitious microphone access, underscoring the breadth of attack surface across both enterprise and consumer technology. Coordinated campaigns by groups such as Blind Eagle, Scattered Spider, LapDogs and Mustang Panda are leveraging these and other entry points to deliver remote-access trojans, steal credentials, and conduct large-scale espionage.

## Active Exploitation Details

### Citrix Bleed 2 – NetScaler ADC/Gateway Memory Exposure
- **Description**: A request-smuggling flaw in Citrix NetScaler ADC and NetScaler Gateway (“Citrix Bleed 2”) that exposes session tokens and other sensitive data directly from memory.
- **Impact**: Enables unauthenticated attackers to hijack active sessions, bypass multifactor authentication, and pivot laterally inside enterprise environments.
- **Status**: Confirmed active exploitation; patches and updated firmware images are available from Citrix.
- **CVE ID**: CVE-2025-5777

### NetScaler ADC/Gateway Critical Authentication Bypass
- **Description**: A critical design weakness allowing crafted HTTP requests to completely bypass the login process on vulnerable NetScaler ADC and NetScaler Gateway appliances.
- **Impact**: Provides full administrative access and VPN session takeover, frequently followed by credential dumping and ransomware deployment.
- **Status**: Evidence of ongoing exploitation; more than 1,200 appliances remain unpatched despite vendor fixes.

### Progress MOVEit Transfer SQL-Injection Chain
- **Description**: Multiple SQL-injection vulnerabilities in MOVEit Transfer that enable remote execution of code and exfiltration of hosted files.
- **Impact**: Mass data theft from file-transfer instances, often leading to extortion-based breaches targeting government, healthcare, and financial organisations.
- **Status**: Active reconnaissance and exploit attempts observed since 27 May 2025; patches are available and must be applied promptly.

### Bluetooth Audio Chipset Vulnerabilities
- **Description**: Logical flaws in a widely used Bluetooth System-on-Chip (SoC) employed by over two dozen audio-device vendors; exploitable to force devices into unauthorized recording or data-leak states.
- **Impact**: Attackers within Bluetooth range can eavesdrop through built-in microphones or extract user data stored on the device.
- **Status**: Proof-of-concept exploits published; firmware updates are expected from affected manufacturers, but roll-out timelines vary.

## Affected Systems and Products

- **Citrix NetScaler ADC / NetScaler Gateway**: Unpatched 14.1, 13.1, 13.0, and prior firmware trains  
  **Platform**: On-premises and cloud-hosted ADC/VPN appliances

- **Progress MOVEit Transfer**: All versions prior to the latest hotfix releases issued in May–June 2025  
  **Platform**: Windows-based managed file-transfer servers (on-prem & cloud)

- **Bluetooth Audio Devices using impacted SoC**: Headsets, earbuds, speakerphones from at least ten hardware vendors  
  **Platform**: Consumer and enterprise Bluetooth peripherals across Windows, macOS, Linux, Android, iOS

## Attack Vectors and Techniques

- **Session Token Harvesting via Memory Leak**  
  **Vector**: Malformed HTTP/2 requests extract raw memory from NetScaler processes, revealing authentication cookies.

- **Authentication Bypass with Crafted HTTP Headers**  
  **Vector**: Manipulated Host and X-Forwarded-For headers trick NetScaler into treating external traffic as trusted, skipping login logic.

- **SQL-Injection to RCE on MOVEit**  
  **Vector**: Unauthenticated POST requests inject malicious SQL that writes webshells, enabling full remote code execution.

- **Short-Range Bluetooth Abuse**  
  **Vector**: Attacker pairs or remains in observer mode, then exploits SoC firmware flaws to enable hidden microphone recording.

## Threat Actor Activities

- **Blind Eagle**  
  **Campaign**: Phishing operations against Colombian banks hosting payloads on Proton66; delivers bespoke RATs post-initial compromise.

- **Scattered Spider**  
  **Campaign**: Expanding social-engineering intrusions into aviation and transportation; leverages stolen credentials to access Citrix environments, aligning with current NetScaler exploit trends.

- **LapDogs (China-linked)**  
  **Campaign**: Uses more than 1,000 compromised SOHO routers as operational infrastructure for espionage, facilitating covert C2 traffic for post-exploitation tooling.

- **Mustang Panda**  
  **Campaign**: Targeted spear-phishing against Tibetan entities deploying PUBLOAD loader and Pubshell backdoor for long-haul intelligence collection.

- **Silver Fox**  
  **Campaign**: Malvertising via fake software sites to deliver Sainbox RAT and a hidden rootkit; likely abuses browser and OS misconfiguration rather than N-day CVEs.

- **ReliaQuest Observations**  
  **Campaign**: Detects spike in Citrix Bleed 2 exploitation attempts originating from mixed clusters of financially-motivated and state-aligned actors.

- **GreyNoise Telemetry**  
  **Campaign**: Reports automated scanning focused on MOVEit Transfer endpoints, suggesting resurgence of Cl0p-style data-theft operations.

