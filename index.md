# Exploitation Report

Over the past week, the most critical exploitation activity centers on a high-severity Linux Kernel privilege-escalation flaw in the OverlayFS subsystem. U.S. CISA has confirmed in-the-wild abuse, adding the bug to its Known Exploited Vulnerabilities (KEV) catalog and urging immediate patching across all major Linux distributions. Concurrently, multiple threat actors—including Predatory Sparrow, BlueNoroff, and several cloud-enabled crimeware operators—are running financially and politically-motivated campaigns that leverage sophisticated social-engineering, living-off-the-land, and cloud-tunneling techniques to gain initial access and exfiltrate data. While other newly disclosed vulnerabilities (e.g., BeyondTrust Remote Support pre-auth RCE and Veeam Backup & Replication critical RCE) do not yet show evidence of exploitation, they remain high-risk because proof-of-concept code and patch details are publicly available.

## Active Exploitation Details

### Linux Kernel OverlayFS Privilege Escalation
- **Description**: A logic error in the OverlayFS subsystem allows unprivileged local users to craft malformed overlay filesystems that bypass namespace isolation, overwrite critical files, and escalate privileges.
- **Impact**: Attackers can obtain full root access, pivot to lateral movement, implant persistent backdoors, and disable security controls.
- **Status**: Confirmed active exploitation in the wild; CISA added the flaw to the KEV list. Patches are available from all major Linux vendors and must be applied or back-ported immediately.
- **CVE ID**: *Not provided in the source articles*

## Affected Systems and Products

- **Linux distributions (Ubuntu, Debian, Red Hat, SUSE, Fedora, Alma, Rocky, etc.)**  
  - **Platform**: Any system running vulnerable kernel versions with OverlayFS enabled—cloud instances, on-prem servers, containers, and IoT appliances.
- **Nobitex Cryptocurrency Exchange Infrastructure**  
  - **Platform**: Web-based trading platform, hot-wallet servers, and backend databases (compromised via Predatory Sparrow intrusion).
- **Enterprise macOS Workstations**  
  - **Platform**: macOS Ventura/Sonoma endpoints targeted by BlueNoroff’s custom malware during fake Zoom interviews.
- **BeyondTrust Remote Support (RS) & Privileged Remote Access (PRA)**  
  - **Platform**: Windows and Linux appliances vulnerable to a newly patched pre-auth RCE flaw (no exploitation observed yet).
- **Veeam Backup & Replication (all editions prior to fixed build for CVE-2025-23121)**  
  - **Platform**: Windows-based backup servers—critical infrastructure for data-protection environments.

## Attack Vectors and Techniques

- **Local Privilege Escalation via OverlayFS**  
  - **Vector**: Crafted user-controlled overlay mounts overwrite setuid binaries, granting root.
- **Cloudflare Tunnel Abuse**  
  - **Vector**: Malicious documents or LNK files open outbound `cloudflared` tunnels to attacker-controlled sub-domains, bypassing inbound firewall rules.
- **Deepfake Business Meetings**  
  - **Vector**: AI-generated video avatars of executives in Zoom calls trick employees into launching signed macOS droppers.
- **Multi-Stage GitHub Malware Delivery (Water Curse / Stargazers)**  
  - **Vector**: Weaponized repositories deliver obfuscated Java or PowerShell loaders that fetch stealer payloads.
- **Legacy Authentication Credential Harvesting (ChainLink Phishing)**  
  - **Vector**: Phishing emails link to Google Drive/Dropbox files that host fake login portals, sidestepping traditional URL-based filters.

## Threat Actor Activities

- **Predatory Sparrow**  
  - **Campaign**: Political sabotage of Iran’s Nobitex exchange, destroying ≈$90 M in cryptocurrency and leaking customer data.
- **BlueNoroff (aka Sapphire Sleet / TA444)**  
  - **Campaign**: Financially motivated attacks on cryptocurrency and fintech firms; uses deepfake Zoom calls to deploy macOS malware.
- **Unknown Cloudflare-Tunnel Actor (“Serpentine#Cloud”)**  
  - **Campaign**: LNK-based spear-phishing with in-memory execution; targets corporate users to establish covert C2 channels.
- **Water Curse**  
  - **Campaign**: 76 hijacked GitHub accounts push staged malware aimed at data exfiltration and potential ransomware deployment.
- **Stargazers Ghost Network**  
  - **Campaign**: Distribution-as-a-Service for malicious Minecraft mods infecting >1,500 gamers with Java infostealers.
- **HoldingHands**  
  - **Campaign**: Information-stealing operations against Taiwanese organizations since at least January, using multiple custom tools.

The current exploitation landscape underscores the urgency of patching Linux kernels, hardening cloud egress controls, and increasing employee awareness of deepfake-enabled social engineering.