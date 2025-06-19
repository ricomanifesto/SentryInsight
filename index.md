# Exploitation Report

The most pressing exploitation activity observed this cycle centers on multiple privilege-escalation flaws targeting Linux systems and a pre-authentication remote-code-execution issue in BeyondTrust’s Remote Support products. Attackers are actively weaponizing a high-severity OverlayFS bug in the Linux kernel (added to CISA’s KEV list), while new research highlights additional local‐root flaws in PAM and Udisks that affect all major distributions. In parallel, Russian state-aligned APT29 is bypassing Google account two-factor authentication by coercing victims into creating “app passwords,” providing persistent access to cloud email. Enterprise software is also in the crosshairs: BeyondTrust has patched a critical Remote Support vulnerability that allowed unauthenticated RCE, and Asana disclosed an implementation flaw that exposed customer data from its new Model Context Protocol (MCP) AI feature. Collectively, these issues give adversaries reliable initial access and rapid privilege escalation paths across cloud, desktop, and server environments.

## Active Exploitation Details

### Linux OverlayFS Privilege Escalation
- **Description**: A vulnerability in the Linux kernel’s OverlayFS subsystem allows improper handling of user-supplied overlay filesystems, enabling overwriting of critical files.
- **Impact**: Local attackers instantly elevate privileges to root, escape containers, and execute arbitrary code with full system control.
- **Status**: Confirmed in-the-wild exploitation; CISA has issued an emergency directive and added the flaw to its Known Exploited Vulnerabilities catalog. Kernel patches are available from major distributions.
  
### Linux PAM Token Handling Flaw
- **Description**: A logic error in Pluggable Authentication Modules (PAM) mishandles user session credentials, permitting non-privileged users to manipulate authentication tokens.
- **Impact**: Local privilege escalation to root on impacted hosts.
- **Status**: Proof-of-concept exploit code released; vendors are shipping updated PAM libraries.

### Linux Udisks2 Helper Privilege Escalation
- **Description**: Udisks2’s helper binaries run with elevated privileges and insufficient parameter sanitization, allowing crafted commands to be executed as root.
- **Impact**: Full root access from any local account; particularly dangerous on shared multi-user servers and developer workstations.
- **Status**: Researchers demonstrated exploitation across Ubuntu, Fedora, Debian, and Arch. Fixes are rolling out via distribution repositories.

### BeyondTrust Remote Support Pre-Auth RCE
- **Description**: A flaw in BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) exposes an unauthenticated endpoint that can be abused to run arbitrary commands on the appliance OS.
- **Impact**: Remote attackers gain system-level execution, pivot inside corporate networks, and harvest privileged credentials.
- **Status**: Vendor released hotfixes and urges immediate upgrade; exploitation is considered practical due to public technical details.

### Google Account App Password 2FA Bypass
- **Description**: Google’s “application-specific passwords” feature generates long-lived credentials that bypass modern MFA. APT29 abuses social-engineering emails to trick targets into creating and sharing these passwords.
- **Impact**: Full access to Gmail and linked Google Workspace data, despite 2FA protections.
- **Status**: Ongoing phishing campaign; no patch (feature working as designed). Google recommends disabling unused app-password functionality and enforcing FIDO2 keys.

### Asana MCP AI Feature Data Exposure
- **Description**: A misconfiguration in Asana’s Model Context Protocol (MCP) caused cross-tenant data leakage when AI models pulled contextual information.
- **Impact**: Confidential project data was visible to unauthorized organizations.
- **Status**: Feature temporarily disabled while a fix is deployed; customers have been notified of potential exposure.

## Affected Systems and Products
- **Linux Kernel (OverlayFS subsystem)**: Ubuntu 22.04/24.04, Debian 12, RHEL 9, Fedora 40, Alpine, container images based on affected kernels  
- **PAM Libraries**: libpam-runtime across Debian, Ubuntu, Fedora, openSUSE, Arch  
- **Udisks2**: Versions packaged with GNOME and major desktop/server distributions  
- **BeyondTrust Remote Support (RS) & Privileged Remote Access (PRA)**: All builds prior to latest hotfix release (June 2025) on Windows, Linux, and virtual appliances  
- **Google Workspace / Gmail**: All consumer and enterprise accounts where “app passwords” are enabled  
- **Asana (Cloud SaaS)**: Organizations that opted-in to the MCP AI feature between 4 April – 2 June 2025  

## Attack Vectors and Techniques
- **Local Kernel Exploit**: Droppers or post-exploitation scripts invoke OverlayFS/PAM/Udisks exploits to jump from unprivileged user to root.  
- **Phishing with App Password Creation**: Spear-phish email directs victim to create a Google app password and send it to the attacker, bypassing 2FA.  
- **Unauthenticated API Call**: Crafted HTTP/HTTPS request targets vulnerable BeyondTrust RS/PRA endpoint, delivering remote shell.  
- **Cross-Tenant AI Query Leak**: Malformed MCP requests pull data from improper tenant contexts inside Asana’s backend.  

## Threat Actor Activities
- **Actor/Group**: APT29 (Russia)  
  - **Campaign**: Leveraging Gmail app-password abuse to maintain persistent access to diplomatic and policy research targets; combines phishing, MFA bypass, and cloud data exfiltration.

- **Actor/Group**: BlueNoroff / TA444 (North Korea)  
  - **Campaign**: Deepfake Zoom calls to distribute signed Mac malware, followed by local privilege-escalation (often using the newly disclosed PAM/Udisks exploits) to steal cryptocurrency.

- **Actor/Group**: Predatory Sparrow (Pro-Israel hacktivists)  
  - **Campaign**: Breach of Iran’s Nobitex exchange; destructive transfer and burn of approximately $90 M in crypto assets.

- **Actor/Group**: Water Curse (newly identified)  
  - **Campaign**: Weaponized GitHub repositories hosting multi-stage loaders; gains initial execution and pivots to root via OverlayFS exploit.

- **Actor/Group**: Stargazers Ghost Network  
  - **Campaign**: Distributing malicious Minecraft mods through GitHub and gaming forums; steals credentials, then uses local LPE exploits for persistence and lateral movement.

- **Actor/Group**: Serpentine#Cloud (unknown)  
  - **Campaign**: .lnk shortcut phishing leveraging Cloudflare Tunnel subdomains; post-exploitation scripts test for OverlayFS vulnerability to guarantee root access.

- **Actor/Group**: Unnamed cloud-focused operators (per “Cloudflare Tunnel” phishing report)  
  - **Campaign**: Uses trusted Cloudflare infrastructure to hide C2, dropping remote-access trojans that invoke PAM-based LPE on Linux hosts.

## End of Report