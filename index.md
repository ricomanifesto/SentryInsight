# Exploitation Report

Multiple security bulletins issued this week confirm that attackers are weaponizing a high-severity privilege-escalation flaw in the Linux kernel’s OverlayFS subsystem to obtain full root access on a broad range of Linux distributions. CISA has added the bug to its Known Exploited Vulnerabilities (KEV) catalogue, warning that exploitation is occurring in the wild and urging immediate patching. Although several other critical vulnerabilities—such as new Linux PAM/Udisks elevation issues and a pre-authentication RCE in BeyondTrust Remote Support—were disclosed, there is currently no evidence they are being exploited. The OverlayFS issue therefore represents the most urgent threat to enterprise and cloud environments this week.

## Active Exploitation Details

### Linux Kernel OverlayFS Privilege Escalation Vulnerability
- **Description**: A flaw in the OverlayFS file-system implementation allows an unprivileged local user to overwrite or bypass security checks when copying file capabilities between different mount namespaces. By crafting malicious OverlayFS mounts, an attacker can modify file attributes and escalate privileges.
- **Impact**: Successful exploitation grants full root privileges, enabling complete takeover of affected hosts, installation of persistent malware, lateral movement, and the disabling of security controls.
- **Status**:  
  • Confirmed active exploitation; added to CISA KEV catalogue  
  • Patches have been released by major Linux vendors (Ubuntu, Debian, Red Hat, SUSE, etc.), but many systems remain un-patched in the field.  
- **CVE ID**: Not explicitly provided in the referenced articles

## Affected Systems and Products

- **Linux Kernel (OverlayFS subsystem)**: Kernel branches used by Ubuntu 22.04/20.04, Debian 12/11, Red Hat Enterprise Linux 9/8, AlmaLinux/Rocky 8–9, SUSE Linux Enterprise 15, Amazon Linux 2023, and other derivatives  
- **Platform**: All x86_64 and ARM Linux environments, including on-prem servers, cloud instances (AWS, Azure, GCP), containers, and embedded devices running vulnerable kernels

## Attack Vectors and Techniques

- **Local Privilege Escalation via OverlayFS**  
  - **Vector**: An attacker with any local foothold (SSH account, compromised web-app user, or container breakout) mounts a crafted OverlayFS filesystem to manipulate file capabilities, then executes a binary with elevated privileges to gain root.

## Threat Actor Activities

- **Unattributed threat actors**  
  - **Campaign**: Opportunistic exploitation of exposed Linux hosts following public release of proof-of-concept code; observed in cloud environments and edge devices.  
  - **Activities**: Privilege escalation, deployment of cryptominers, installation of persistence daemons, and preparation for lateral movement inside enterprise networks.