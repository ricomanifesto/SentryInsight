# Exploitation Report

The most critical exploitation activity observed this cycle centers on multiple, concurrent attacks against edge-network and browser technologies. A previously unknown zero-day is being leveraged to compromise fully-patched, end-of-life SonicWall SMA 100 appliances and implant the “OVERSTEP” rootkit, enabling ransomware deployment by actors linked to the Abyss group (UNC6148). Simultaneously, mass exploitation of a recently patched Fortinet FortiWeb remote-code-execution flaw is resulting in web-shell infestations across Internet-facing WAF instances. On the client side, Google Chrome users are being targeted with an in-the-wild sandbox-escape (CVE-2025-6558), prompting emergency browser updates. These campaigns demonstrate a clear trend: threat actors are prioritizing perimeter devices and widely-installed software to obtain initial access, evade detection, and launch follow-on ransomware or data-theft operations.

## Active Exploitation Details

### SonicWall SMA 100 Zero-Day (“OVERSTEP” Rootkit)
- **Description**: An unknown vulnerability in SonicWall Secure Mobile Access (SMA) 100 series appliances (firmware fully up to date, but product line now end-of-life) allows attackers to modify the boot loader and install a persistent rootkit dubbed “OVERSTEP.”  
- **Impact**: Provides attackers with root-level persistence, remote command execution, credential theft, and staging of Abyss ransomware payloads.  
- **Status**: Actively exploited in the wild; no official patch available because the hardware is EoL. SonicWall advises immediate device replacement or network isolation.

### Fortinet FortiWeb Remote Code Execution Flaw
- **Description**: Recently patched RCE vulnerability in FortiWeb web-application firewalls is being abused via publicly released exploit code to drop web shells on exposed instances.  
- **Impact**: Unauthenticated attackers gain full system control, enabling lateral movement, data exfiltration, and staging of further malware.  
- **Status**: Active exploitation observed; Fortinet has issued firmware updates. Instances not yet patched remain vulnerable.

### Google Chrome Sandbox-Escape
- **Description**: High-severity type-confusion bug in the V8 engine that permits a renderer-to-browser sandbox escape when a user visits a malicious site.  
- **Impact**: Attackers achieve arbitrary code execution in the browser process, leading to full user compromise and potential distribution of secondary payloads.  
- **Status**: Fixed in Chrome 125.0.6422.141 for Windows, macOS, and Linux; exploitation confirmed in the wild.  
- **CVE ID**: CVE-2025-6558

## Affected Systems and Products

- **SonicWall Secure Mobile Access 100 Series**: SMA 200, 210, 400, 410 appliances (all firmware levels)  
  - **Platform**: On-premises VPN/remote-access gateway appliances (now end-of-life)

- **Fortinet FortiWeb**: Versions prior to the May 2025 security update (all hardware and virtual form factors)  
  - **Platform**: Web-application firewall appliances and virtual machines running FortiWeb OS

- **Google Chrome**: Versions prior to 125.0.6422.141 on Windows, macOS, Linux, and Android  
  - **Platform**: Desktop and mobile browsers leveraging the Chromium codebase

## Attack Vectors and Techniques

- **Zero-Day Appliance Exploitation**  
  - **Vector**: Direct HTTPS management-interface access against SonicWall SMA devices to trigger the unknown flaw, overwrite boot loader, and install OVERSTEP.

- **Public Exploit Weaponization (FortiWeb)**  
  - **Vector**: Crafted HTTP requests exploiting the FortiWeb RCE, followed by web-shell deployment for persistent remote control.

- **Browser Sandbox Escape**  
  - **Vector**: Malicious web pages exploiting CVE-2025-6558 to transition from renderer to browser process, gaining OS-level execution.

- **Malware Loader via Collaboration Platforms**  
  - **Technique**: Matanbuchus 3.0 delivered through spoofed Microsoft Teams chats; leverages DNS-based C2 and EDR evasion to stage ransomware—often observed post-FortiWeb or SMA compromise for lateral deployment.

## Threat Actor Activities

- **UNC6148 / Abyss Ransomware**  
  - **Campaign**: Backdooring SonicWall SMA devices with OVERSTEP, gathering credentials, and deploying Abyss ransomware in enterprise environments. Target scope includes technology, manufacturing, and healthcare sectors.

- **Unattributed FortiWeb Exploiters**  
  - **Campaign**: Mass Internet scanning for vulnerable FortiWeb instances, automatic web-shell installation, and monetization via access-broker underground markets.

- **Crimeware Operators behind Matanbuchus 3.0**  
  - **Activities**: Using Microsoft Teams phishing lures to implant the upgraded loader, which now detects EDR processes and communicates over DNS tunnels; observed collaborating with multiple ransomware-as-a-service affiliates.

