# Exploitation Report

During the last week, the most severe exploitation activity centers on Citrix NetScaler appliances, where the critical “Citrix Bleed 2” flaw (CVE-2025-5777) was weaponized in the wild nearly two weeks before public proof-of-concept code surfaced. Simultaneously, four previously unknown vulnerabilities in VMware ESXi, Workstation, Fusion, and Tools were demonstrated as zero-days at the Pwn2Own Berlin 2025 contest, prompting out-of-band patches from VMware. Attackers are also abusing collaboration platforms—most notably Microsoft Teams voice calls—to distribute the Matanbuchus malware loader, underscoring a continued shift toward social-engineering vectors that bypass traditional email defenses. State-sponsored and financially motivated threat actors remain highly active, with Chinese group “Salt Typhoon” infiltrating a U.S. National Guard network for nine months and Google moving to dismantle the BadBox 2.0 Android botnet that infected more than 10 million devices.

## Active Exploitation Details

### Citrix Bleed 2 (NetScaler ADC/Gateway)
- **Description**: A request-smuggling flaw in NetScaler ADC and NetScaler Gateway that allows attackers to hijack authenticated sessions, exfiltrate credentials, and potentially execute arbitrary code.
- **Impact**: Unauthenticated attackers can steal session tokens, move laterally inside corporate networks, and gain full control of published applications and VPN gateways.
- **Status**: Actively exploited in the wild since at least two weeks before public PoCs. Citrix has released patches and urges immediate appliance upgrades and token/session invalidation.
- **CVE ID**: CVE-2025-5777

### VMware ESXi / Workstation / Fusion / Tools – Multiple Zero-Days
- **Description**: Four distinct memory-safety and privilege-escalation vulnerabilities (use-after-free, out-of-bounds write, and logic flaws) uncovered and exploited live during the Pwn2Own Berlin 2025 contest.
- **Impact**: Successful exploitation enables guest-to-host escapes, arbitrary code execution on the hypervisor, and potential takeover of underlying hosts running production VMs.
- **Status**: Demonstrated as zero-days; VMware released emergency patches for all supported branches. No reports yet of exploitation outside the contest environment.

## Affected Systems and Products

- **Citrix NetScaler ADC & NetScaler Gateway**  
  - Firmware builds prior to the May 2025 security update  
  - Platform: On-premises and cloud-hosted NetScaler appliances

- **VMware ESXi, Workstation Pro/Player, Fusion, and VMware Tools**  
  - ESXi 8.x, 7.x, 6.7; Workstation 17; Fusion 13; corresponding Tools versions  
  - Platform: vSphere hypervisors on bare-metal servers, Windows/Linux/macOS endpoints running Workstation/Fusion

- **Microsoft Teams**  
  - All desktop clients capable of receiving external voice calls  
  - Platform: Windows & macOS collaboration environments

## Attack Vectors and Techniques

- **HTTP Request-Smuggling (Citrix Bleed 2)**  
  - **Vector**: Crafted HTTP/2 requests to NetScaler Gateway trigger desynchronization between front-end and back-end parsing, leaking authenticated sessions.

- **Guest-to-Host Escape (VMware Zero-Days)**  
  - **Vector**: Malicious code executed in a VM leverages memory-corruption flaws in virtual USB/XHCI or graphics components to attain host-level execution.

- **Social-Engineering via Voice Call (Matanbuchus)**  
  - **Vector**: Attackers impersonate IT helpdesk staff in Microsoft Teams, initiating a voice call that persuades victims to click malicious share-links delivering the Matanbuchus loader.

- **Public GitHub Payload Hosting (Amadey Campaign)**  
  - **Vector**: Malware-as-a-Service operators upload stealer payloads to GitHub repos, then download them from compromised systems to bypass content-filtering.

- **Trojanized Android Firmware (BadBox 2.0)**  
  - **Vector**: Pre-installed backdoors on off-brand Android devices enroll endpoints into a botnet used for ad-fraud and data theft.

## Threat Actor Activities

- **Unknown Crimeware Operators**  
  - Exploiting CVE-2025-5777 globally against healthcare, finance, and government NetScaler instances; observed mass-scanning, token theft, and lateral movement.

- **Pwn2Own Berlin Research Teams**  
  - Demonstrated practical exploits for four VMware zero-days, earning $400,000 in prizes and triggering vendor patches.

- **Matanbuchus Affiliates (“Water-Curlew” cluster)**  
  - Running voice-phishing campaigns on Microsoft Teams to deploy loaders that fetch Cobalt Strike and Stealer-as-a-Service families.

- **Salt Typhoon (Chinese state-sponsored)**  
  - Maintained covert access to a U.S. National Guard enclave for nine months, exfiltrating network configuration data to facilitate future operations.

- **BadBox 2.0 Operators**  
  - Controlled a 10-million-device Android botnet focused on large-scale ad-fraud; legal takedown initiated by Google to disrupt monetization.

- **Amadey Malware-as-a-Service Crew**  
  - Leveraging GitHub for resilient payload delivery, spreading RedLine and Lumma stealers inside enterprise networks while evading domain-based filtering.

