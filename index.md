# Exploitation Report

During the last 48 hours, threat actors have been observed actively exploiting a privilege-escalation flaw in the Linux kernel’s OverlayFS subsystem and a now-patched Google Chrome zero-day to gain elevated privileges and deploy the “Trinper” backdoor. The Linux bug is already listed in CISA’s Known Exploited Vulnerabilities (KEV) catalog, indicating widespread, in-the-wild abuse across major distributions. Meanwhile, a group tracked as “TaxOff” weaponized CVE-2025-2783 in Chrome to deliver malware through drive-by downloads. Concurrently, multiple campaigns are abusing Cloudflare Tunnels, weaponized GitHub repositories, and malicious Minecraft mods, illustrating a surge in living-off-the-land and supply-chain techniques that bypass traditional perimeter defenses.

## Active Exploitation Details

### Linux OverlayFS Privilege-Escalation Vulnerability
- **Description**: A flaw in the OverlayFS subsystem allows unprivileged local users to override security checks when mounting overlay filesystems, enabling the execution of arbitrary code with kernel-level permissions.  
- **Impact**: Successful exploitation grants full root privileges, enabling complete system takeover, credential dumping, lateral movement, and persistence.  
- **Status**: Confirmed active exploitation in the wild; CISA added the bug to its KEV catalog. Linux vendors have released patches and back-ported fixes.  
<!-- No CVE line because the article did not explicitly list one -->

### Google Chrome Skia Rendering Engine Vulnerability
- **Description**: An integer-handling issue in Chrome’s Skia graphics component that permits remote code execution when a user visits a maliciously crafted webpage.  
- **Impact**: Attackers can achieve sandbox escape and execute arbitrary code on the host, facilitating the installation of the “Trinper” backdoor.  
- **Status**: Exploited as a zero-day by the TaxOff threat actor in mid-March 2025; Google has issued an emergency update across all channels.  
- **CVE ID**: CVE-2025-2783  

## Affected Systems and Products

- **Linux Kernel (OverlayFS subsystem)**
  - **Platform**: Major Linux distributions including Ubuntu, Debian, Red Hat, Fedora, and SUSE running vulnerable kernel versions prior to vendor patches.
  
- **Google Chrome (pre-patch versions)**
  - **Platform**: Windows, macOS, and Linux desktop environments running builds prior to the security update that addresses CVE-2025-2783.

## Attack Vectors and Techniques

- **Drive-By Download Exploitation**
  - **Vector**: Malicious websites leveraging CVE-2025-2783 to compromise unpatched Chrome browsers.

- **Local Privilege Escalation**
  - **Vector**: Post-exploitation use of the OverlayFS vulnerability to escalate from user to root on Linux hosts.

- **Cloudflare Tunnel Abuse**
  - **Vector**: Phishing emails containing attachments that resolve to attacker-controlled Cloudflare Tunnel subdomains hosting RAT payloads.

- **Weaponized GitHub Repositories**
  - **Vector**: “Water Curse” implants malicious code in cloned/open-source projects distributed via 76 hijacked GitHub accounts.

- **Malicious Minecraft Mods Distribution**
  - **Vector**: “Stargazers” lures gamers to install trojanized Java mods that siphon credentials and session tokens.

- **ChainLink Phishing**
  - **Vector**: Chained redirects using trusted SaaS (Google Drive, Dropbox) to evade email filtering and steal browser-session cookies.

- **.lnk Shortcut In-Memory Execution**
  - **Vector**: “Serpentine#Cloud” delivers weaponized Windows shortcut files that execute payloads directly in memory, bypassing disk-based detection.

## Threat Actor Activities

- **TaxOff**
  - **Campaign**: Exploited CVE-2025-2783 in Chrome to deliver the Trinper backdoor targeting unspecified organizations via malicious websites.

- **Water Curse**
  - **Campaign**: Utilizes 76 compromised GitHub accounts to stage multi-stage malware, focusing on data exfiltration and follow-on access sales.

- **Stargazers Ghost Network**
  - **Campaign**: Distributes fake Minecraft mods/cheats, infecting over 1,500 players with infostealers on Windows systems.

- **Serpentine#Cloud**
  - **Campaign**: Conducts stealthy attacks using Cloudflare Tunnels, .lnk files, and living-off-the-land binaries (LOLBins) for in-memory payload execution.

- **HoldingHands**
  - **Campaign**: Runs information-stealing operations against Taiwanese businesses and government entities with multiple custom malware strains.

