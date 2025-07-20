# Exploitation Report

During the last news cycle, several high-impact attacks were observed in the wild. The most critical activity involves the zero-day (CVE-2025-54309) in CrushFTP that grants unauthenticated administrative control of file-transfer servers and is already being weaponised against public-facing instances. Parallel campaigns show innovative trade-craft: “PoisonSeed” defeats FIDO2 hardware keys by abusing WebAuthn’s cross-device feature; a phishing-enabled account takeover on the npm registry converted widely-used eslint packages into malware droppers; and new Ivanti Connect Secure zero-days are being chained to deploy the in-memory “MDifyLoader” and embedded Cobalt Strike beacons. Linux supply-chain risks remain a theme – malicious Arch Linux AUR packages were found installing Chaos RAT. Collectively, these incidents underscore an elevated threat level across authentication workflows, software-supply chains, and edge-exposed appliances.

## Active Exploitation Details

### CrushFTP Administrative Access Zero-Day  
- **Description**: Logic flaw in the web management interface allows remote adversaries to bypass authentication and obtain full administrative rights.  
- **Impact**: Complete server takeover, exfiltration or modification of all hosted files, lateral movement into internal networks.  
- **Status**: Actively exploited in the wild; vendor has issued fixed versions (10.7.1 / 11.2 or later) along with mitigations.  
- **CVE ID**: CVE-2025-54309  

### “PoisonSeed” FIDO2 MFA Downgrade Attack  
- **Description**: Phishing framework that leverages WebAuthn’s cross-device sign-in capability. Victims scan a QR code and unknowingly approve a fraudulent push, downgrading from FIDO2 security-key authentication to weaker app-based approval controlled by the attacker.  
- **Impact**: Account compromise even when FIDO2 hardware keys are mandated; enables session hijacking and subsequent business-email compromise.  
- **Status**: Ongoing campaign; no software patch required, but mitigations rely on user education and disabling cross-device WebAuthn where feasible.  

### Hijack of eslint-config-prettier & eslint-plugin-prettier (npm)  
- **Description**: Threat actors phished maintainers, stole credentials, and published trojanised package updates. Malicious post-install scripts download secondary payloads that profile hosts and deploy malware.  
- **Impact**: Supply-chain exposure for thousands of downstream JavaScript projects; potential remote-code execution during development or CI builds.  
- **Status**: Malicious versions yanked from npm; maintainers restored control and published clean releases.  

### Malicious Arch Linux AUR Packages Installing Chaos RAT  
- **Description**: Three newly-submitted AUR packages embedded obfuscated installation routines that retrieved and executed the Chaos remote-access trojan.  
- **Impact**: Full remote access to affected Linux workstations and servers, credential theft, lateral movement.  
- **Status**: Packages removed from AUR; users must manually audit and purge compromised hosts.  

### Ivanti Connect Secure / Policy Secure Zero-Days (MDifyLoader Dropper)  
- **Description**: Unpatched flaws in the VPN gateway allow unauthenticated attackers to write files and trigger command execution, planting the MDifyLoader malware that subsequently injects an in-memory Cobalt Strike beacon.  
- **Impact**: Network perimeter breach, persistent foothold, data exfiltration, and potential ransomware staging.  
- **Status**: Exploits observed in the wild; Ivanti engineering work-arounds released with full patches pending.  

## Affected Systems and Products

- **CrushFTP Server**: Versions prior to 10.7.1 / 11.2 on Windows, Linux, macOS  
- **FIDO2 / WebAuthn Workflows**: All major browsers supporting cross-device sign-in on desktop and mobile platforms  
- **eslint-config-prettier & eslint-plugin-prettier (npm)**: Compromised releases pushed on the npm registry (now deprecated)  
- **Arch Linux**: Systems that built and installed the withdrawn AUR packages (all x86_64 distributions)  
- **Ivanti Connect Secure & Policy Secure Gateways**: All unpatched versions exposed to the internet  

## Attack Vectors and Techniques

- **WebAuthn Cross-Device Abuse**  
  - **Vector**: QR-code phishing downgrades FIDO2 to weaker approval flow, bypassing hardware-key enforcement.  

- **Package-Repository Account Takeover**  
  - **Vector**: Spear-phishing of npm maintainers → credential theft → malicious package uploads containing post-install malware droppers.  

- **Supply-Chain Poisoning (AUR)**  
  - **Vector**: Submission of new AUR packages with hidden curl | bash routines fetching Chaos RAT.  

- **Unauthenticated Web Management Exploit**  
  - **Vector**: Crafted HTTP requests against CrushFTP’s web interface exploit authentication bypass logic.  

- **Gateway RCE Chain (Ivanti)**  
  - **Vector**: Combination of file-write and command-injection zero-days enabling deployment of MDifyLoader and in-memory Cobalt Strike.  

## Threat Actor Activities

- **PoisonSeed Operators**  
  - **Campaign**: Targeting enterprise Office 365 tenants; focuses on bypassing FIDO2 MFA through QR-code lures and real-time session hijacking.  

- **Unknown npm Phishing Group**  
  - **Campaign**: Compromised eslint* packages; infrastructure delivers information-stealers and remote shells to developer environments.  

- **APT28 (Fancy Bear)**  
  - **Campaign**: “Authentic Antics” malware stealing Microsoft 365 credentials; observed alongside credential-harvesting infrastructure though no new CVE exploitation reported.  

- **Unattributed Actors Exploiting CrushFTP**  
  - **Campaign**: Mass-scanning of public CrushFTP servers; post-exploitation leads to data exfiltration and creation of rogue admin accounts.  

- **Ivanti Zero-Day Actors (linked to MDifyLoader)**  
  - **Campaign**: Highly targeted intrusions against government and telecom networks; focus on stealthy in-memory implants and beaconing to C2 servers via parent-child HTTP header spoofing.  

- **Chaos RAT Distributors on AUR**  
  - **Campaign**: Opportunistic compromise of Arch Linux users; indicators suggest financially-motivated group repurposing previously leaked RAT source code.