# Exploitation Report

During the last week, multiple high-impact vulnerabilities moved directly from disclosure to active exploitation. The most critical events center on Citrix NetScaler appliances, where “CitrixBleed 2” (CVE-2025-5777) was weaponised in the wild almost two weeks before proof-of-concept code became public, enabling unauthenticated memory disclosure and session hijacking against internet-facing gateways. VMware simultaneously shipped emergency patches for four ESXi/Workstation/Fusion zero-days that researchers exploited during the Pwn2Own Berlin contest, demonstrating reliable guest-to-host escapes and code execution. While Cisco released fixes for a CVSS 10 flaw in Identity Services Engine, no in-the-wild exploitation has yet been observed, making CitrixBleed 2 and the newly patched VMware issues the most pressing threats. Parallel campaigns abusing Microsoft Teams voice calls to drop the Matanbuchus loader, Salt Typhoon’s extended National Guard intrusion, and Google’s legal action against the BadBox 2.0 Android botnet further illustrate the current threat landscape.

## Active Exploitation Details

### CitrixBleed 2 – Citrix NetScaler ADC/Gateway Memory Disclosure
- **Description**: An unauthenticated flaw allowing attackers to read adjacent memory from vulnerable NetScaler ADC and Gateway processes, exposing valid session tokens, cookies, and credentials.
- **Impact**: Enables session hijacking, lateral movement into internal Citrix VDI environments, and potential full network compromise without needing valid accounts.
- **Status**: Actively exploited in the wild since at least two weeks before public PoCs. Citrix has released patches and strongly urges immediate upgrade or mitigation.
- **CVE ID**: CVE-2025-5777

### VMware ESXi / Workstation / Fusion Zero-Days (Pwn2Own Berlin 2025)
- **Description**: A collection of four distinct vulnerabilities demonstrated at Pwn2Own allowing guest virtual machines to execute code on the host or escape the hypervisor boundary. Flaws include out-of-bounds writes and logic errors in device emulation components.
- **Impact**: Full host compromise from a malicious or compromised guest, potential pivot to other infrastructure managed by the hypervisor.
- **Status**: Zero-day status at the contest; VMware subsequently released security updates for ESXi, Workstation, Fusion, and Tools. No evidence of malicious in-the-wild exploitation yet, but public knowledge significantly raises risk.

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: 14.1 before 14.1-20.18; 13.1 before 13.1-51.19; 13.0 before 13.0-92.21; 12.1 (eol) – appliance and VPX platforms
  - **Platform**: On-prem appliances, cloud instances, and managed service deployments
- **VMware ESXi**: 8.x, 7.x branches prior to the May 2025 patch set  
  - **Platform**: Bare-metal hypervisors running on x86-64 servers
- **VMware Workstation Pro / Player**: 17.x before 17.5.2  
  - **Platform**: Windows and Linux desktop virtualization hosts
- **VMware Fusion / Fusion Pro**: 13.x before 13.5.2  
  - **Platform**: macOS virtualization hosts

## Attack Vectors and Techniques

- **Unauthenticated Memory Scraping (CitrixBleed 2)**  
  - **Vector**: Crafted HTTP/HTTPS requests to the device management interface leak sensitive memory regions containing active session tokens.

- **Guest-to-Host Hypervisor Escape (VMware Zero-Days)**  
  - **Vector**: Malicious code inside a VM issues specially crafted instructions or triggers device emulation bugs leading to arbitrary code execution on the host.

- **Social Engineering via Teams Voice Calls**  
  - **Vector**: Fake IT help-desk calls through Microsoft Teams urge victims to disable security controls and download a malicious “support tool” that sideloads the Matanbuchus malware loader.

- **Public Repository Malware Hosting**  
  - **Vector**: Attackers store Amadey payloads and stealers in GitHub repositories, abusing trust in GitHub domains to bypass network filters.

## Threat Actor Activities

- **Unknown Actors (CitrixBleed 2)**  
  - **Campaign**: Mass scanning and exploitation of exposed NetScaler gateways for credential theft and persistence. Activity predates vendor acknowledgement.

- **Security Researchers @ Pwn2Own**  
  - **Campaign**: Controlled exploitation of VMware zero-days earning contest points and cash awards; details now responsibly disclosed and patched.

- **Matanbuchus Operators**  
  - **Campaign**: Phishing via Microsoft Teams calls targeting corporate employees; objective is initial loader deployment leading to Cobalt Strike or ransomware affiliates.

- **Salt Typhoon (Chinese State-Sponsored)**  
  - **Campaign**: Nine-month stealth intrusion into a U.S. National Guard network to exfiltrate configuration data, leveraging stolen credentials and living-off-the-land techniques.

- **BadBox 2.0 Operators**  
  - **Campaign**: Large-scale Android supply-chain infection (10 million devices) for ad-fraud; Google filed civil suit and is moving for takedown and domain seizure.

- **GitHub/Amadey Campaign Actors**  
  - **Campaign**: Use of public repositories for payload staging, distributing stealers to global victims while evading traditional web filtering.

---

**Remain vigilant**: prioritise patching Citrix NetScaler appliances and VMware virtualisation products, monitor Teams traffic for unsolicited voice calls, and enforce egress controls to GitHub and other public code-hosting services.