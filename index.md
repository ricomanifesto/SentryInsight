# Exploitation Report

Over the past week, defenders have faced a surge in high-impact exploitation activity ranging from a fresh Google Chrome zero-day leveraged for stealthy back-door deployment to active Linux kernel privilege-escalation attacks that grant instant root on multiple distributions. Simultaneously, critical enterprise software such as Veeam Backup & Replication and BeyondTrust Remote Support received emergency patches for remotely exploitable flaws, while threat actors continued innovating on delivery — North Korea’s BlueNoroff deep-faked executives on Zoom, and multiple campaigns abused Cloudflare Tunnels, weaponized GitHub repositories, and malicious Minecraft mods to distribute multi-stage malware. The following sections detail each actively exploited or newly patched vulnerability, affected systems, attack techniques, and threat-actor operations observed in the reporting period.

## Active Exploitation Details

### Google Chrome Skia Integer Overflow
- **Description**: A memory-safety flaw in the Skia graphics library that allows attackers to corrupt memory and achieve arbitrary code execution in the browser context.  
- **Impact**: Drive-by compromise leading to full browser takeover and subsequent deployment of the Trinper backdoor.  
- **Status**: Exploited as a zero-day in mid-March by the TaxOff threat actor; Google has issued an emergency update.  
- **CVE ID**: CVE-2025-2783  

### Linux Kernel OverlayFS Privilege Escalation
- **Description**: A logic error in OverlayFS namespace handling lets unprivileged users craft a malicious mount sequence to overwrite critical files.  
- **Impact**: Local attackers instantly escalate to root, facilitating container breakout or full system takeover on bare-metal and cloud hosts.  
- **Status**: Actively exploited in the wild; CISA has added the bug to the KEV catalog and instructed federal agencies to patch immediately. Kernel maintainers and major distros have released fixes.  

### BeyondTrust Remote Support / Privileged Remote Access Pre-Auth RCE
- **Description**: Input-validation flaw in the web interface permits unauthenticated attackers to send crafted requests that trigger command execution under the NT SYSTEM or root context.  
- **Impact**: Full compromise of help-desk jump servers, enabling lateral movement into high-privilege environments.  
- **Status**: No confirmed exploitation yet, but proof-of-concept code is circulating. Patches are available from BeyondTrust.  

### Veeam Backup & Replication Remote Code Execution
- **Description**: Improper authentication in the Veeam Backup service allows remote attackers to bypass access controls and execute arbitrary code as the service account.  
- **Impact**: Complete compromise of backup infrastructure, with potential for data destruction or ransomware facilitation.  
- **Status**: Patched; customers urged to upgrade immediately.  
- **CVE ID**: CVE-2025-23121  

### Linux udisks Local Privilege Escalation
- **Description**: Two logic errors in how udisks verifies device ownership and policy-kit permissions allow crafted dbus calls to spawn root-owned processes.  
- **Impact**: Local attackers obtain root on desktop and server distributions that ship the vulnerable daemon.  
- **Status**: Publicly disclosed with patches; no confirmed exploitation yet, but low-complexity PoC code exists.  

## Affected Systems and Products

- **Google Chrome**: Desktop editions prior to the emergency patch release (Windows, macOS, Linux)  
- **Linux Kernel**: Multiple distributions running vulnerable OverlayFS code paths (common in kernels < 6.x after specific back-ports)  
- **BeyondTrust Remote Support (RS) & Privileged Remote Access (PRA)**: All on-prem and virtual appliance versions prior to vendor hotfix  
- **Veeam Backup & Replication**: Builds earlier than 12.1.2 (all supported operating systems)  
- **udisks-daemon**: Default packages in Ubuntu, Debian, Fedora, and derivatives shipping the vulnerable code  

## Attack Vectors and Techniques

- **Drive-By Download (Chrome Zero-Day)**  
  - **Vector**: Malicious websites trigger the Skia integer overflow, leading to shellcode execution inside the renderer process.  

- **Local Privilege Escalation via OverlayFS**  
  - **Vector**: Crafted mount followed by file-replacement to gain root on local Linux hosts or escape containers.  

- **Phishing with Cloudflare Tunnels**  
  - **Vector**: Attackers embed Cloudflare Tunnel sub-domains in email attachments; victims fetch payloads that bypass perimeter controls.  

- **Deepfake Social Engineering**  
  - **Vector**: BlueNoroff imposters use AI-generated executive videos in Zoom calls to convince employees to run signed Mac malware installers.  

- **Malicious LNK & Living-off-the-Land (Serpentine#Cloud)**  
  - **Vector**: Weaponized shortcut files execute in-memory PowerShell that spawns Cloudflare Tunnels for C2.  

- **Virtualized App Hijacking (GodFather Trojan)**  
  - **Vector**: Android malware spins up an isolated virtual environment, replacing legitimate banking apps to intercept credentials.  

## Threat Actor Activities

- **TaxOff**  
  - **Campaign**: Exploited Chrome CVE-2025-2783 to implant Trinper backdoor on diplomatic and energy-sector targets.  

- **BlueNoroff (Sapphire Sleet / TA444)**  
  - **Campaign**: Used deepfake Zoom calls to distribute custom macOS malware aimed at cryptocurrency-holding startups.  

- **Water Curse**  
  - **Campaign**: Leveraged 76 hijacked GitHub accounts to stage multi-stage loaders and exfiltrate victim data.  

- **Serpentine#Cloud (Unattributed)**  
  - **Campaign**: Mass-mailing LNK files; post-exploitation relies on Cloudflare Tunnels and LOLBins for persistent access.  

- **Stargazers Ghost Network**  
  - **Campaign**: Distributed malicious Minecraft mods through GitHub and gaming forums, infecting 1,500+ players with Java infostealers.  

- **HoldingHands**  
  - **Campaign**: Ongoing information-stealing operations against Taiwanese government and business entities using custom pickpocket-style malware.  

- **TA000 (Generic)**  
  - **Campaign**: New phishing methodology dubbed “ChainLink” abusing Google Drive and Dropbox shared links to capture enterprise credentials.  

## End of Report