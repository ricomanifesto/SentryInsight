# Exploitation Report

Critical exploitation activity is surging across multiple platforms and attack vectors. The VMware Aria Operations command injection vulnerability CVE-2026-22719 is being actively exploited in the wild, prompting CISA to add it to their Known Exploited Vulnerabilities catalog. A sophisticated iOS exploit kit called Coruna has been identified targeting iPhone models with 23 exploits across five chains, affecting iOS versions 13.0 through 17.2.1. Additionally, a Qualcomm zero-day vulnerability CVE-2026-21385 is being exploited in targeted Android attacks, potentially linked to commercial spyware or nation-state operations. Several maximum-severity vulnerabilities have also been disclosed, including a zero-click attack against FreeScout helpdesk platforms and critical flaws in Cisco's Secure Firewall Management Center.

## Active Exploitation Details

### VMware Aria Operations Command Injection Flaw
- **Description**: A command injection vulnerability in VMware Aria Operations that allows attackers to execute arbitrary commands on affected systems
- **Impact**: Attackers can gain broad access to victims' cloud environments and execute commands with elevated privileges
- **Status**: Currently being exploited in active attacks, patches available
- **CVE ID**: CVE-2026-22719

### Coruna iOS Exploit Kit
- **Description**: A previously undocumented set of 23 iOS exploits organized into five exploitation chains targeting multiple iOS versions
- **Impact**: Enables targeted espionage campaigns and financially motivated attacks against iOS devices, allowing complete device compromise
- **Status**: Active deployment by multiple threat actors in targeted attacks
- **CVE ID**: Not specified in articles

### Qualcomm Zero-Day Android Vulnerability
- **Description**: A high-severity memory corruption flaw in Qualcomm components affecting Android devices
- **Impact**: Allows attackers to compromise Android devices through memory corruption exploitation
- **Status**: Currently being exploited in targeted attacks, potentially by commercial spyware or nation-state actors
- **CVE ID**: CVE-2026-21385

### Mail2Shell Zero-Click Attack
- **Description**: A maximum severity vulnerability in the FreeScout helpdesk platform allowing remote code execution without user interaction or authentication
- **Impact**: Complete server compromise through zero-click exploitation, enabling full system control
- **Status**: Vulnerability disclosed, exploitation capability demonstrated

## Affected Systems and Products

- **VMware Aria Operations**: Cloud management platform vulnerable to command injection attacks affecting cloud environments
- **iOS Devices**: iPhone models running iOS versions 13.0 through 17.2.1 targeted by Coruna exploit kit
- **Android Devices**: Devices with Qualcomm components affected by memory corruption vulnerability
- **FreeScout Helpdesk Platform**: Mail server functionality vulnerable to zero-click remote code execution
- **Cisco Secure Firewall Management Center**: Maximum severity vulnerabilities providing root access
- **Phishing Infrastructure**: Tycoon2FA platform disrupted after facilitating 64,000 attacks globally
- **LeakBase Cybercrime Forum**: Major platform for trading stolen credentials with 142,000 members seized

## Attack Vectors and Techniques

- **Command Injection**: VMware Aria Operations exploitation through malicious command execution
- **Zero-Click Exploitation**: FreeScout vulnerability requires no user interaction for successful compromise
- **Mobile Exploit Chains**: Coruna kit uses sophisticated multi-stage exploitation targeting iOS devices
- **Memory Corruption**: Qualcomm vulnerability exploited through memory manipulation techniques
- **Phishing-as-a-Service**: Tycoon2FA platform enabled adversary-in-the-middle credential harvesting
- **Credential Stuffing**: Brute-force RDP attacks used to unmask ransomware infrastructure networks
- **Supply Chain Attacks**: Fake Laravel packages on Packagist deploying cross-platform remote access trojans

## Threat Actor Activities

- **APT41-Linked Silver Dragon**: Chinese threat group targeting government entities in Europe and Southeast Asia using Cobalt Strike and Google Drive for command and control
- **Sloppy Lemming**: India-nexus APT group targeting defense and critical infrastructure with custom Rust-coded tools and cloud-based C2
- **Phobos Ransomware Operation**: Russian administrator pleaded guilty to wire fraud conspiracy related to hundreds of global victims
- **Multiple Threat Actors**: Using Coruna iOS exploit kit for both espionage and financial crime operations
- **Hacktivist Groups**: 149 DDoS attacks against 110 organizations across 16 countries following Middle East conflicts
- **Cybercriminal Syndicates**: African cybercrime network disrupted by Interpol resulting in 574 arrests and $3 million recovery