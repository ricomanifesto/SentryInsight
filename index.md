# Exploitation Report

Critical security vulnerabilities are actively being exploited across multiple platforms and attack vectors. Most notably, Google has patched two Android Framework zero-day vulnerabilities that were exploited in targeted attacks, while malicious actors continue to leverage supply chain attacks through NPM packages and poisoned development tools. State-sponsored groups, particularly from North Korea and Iran, are conducting sophisticated campaigns targeting developers and critical infrastructure sectors. The cybercrime ecosystem has evolved into a service-based model, with attackers renting tools, infrastructure, and access as subscription services.

## Active Exploitation Details

### Android Framework Zero-Day Vulnerabilities
- **Description**: Two critical security flaws in the Android Framework that allow attackers to compromise targeted systems
- **Impact**: Successful exploitation enables attackers to gain unauthorized access and control over Android devices in targeted attacks
- **Status**: Actively exploited in the wild; patches released in Google's December 2025 security bulletin addressing 107 total vulnerabilities

### Picklescan Security Tool Bypass
- **Description**: Three critical security flaws in the open-source Picklescan utility that allow malicious PyTorch models to evade detection
- **Impact**: Attackers can execute arbitrary code by loading untrusted PyTorch models while bypassing security scans
- **Status**: Actively exploited to circumvent AI model security scanning tools

### Malicious NPM Package Campaign
- **Description**: Large-scale supply chain attack targeting developers through poisoned NPM packages that evade AI-driven security scanners
- **Impact**: Exposure of up to 400,000 developer secrets and credentials through the Shai-Hulud 2.0 attack
- **Status**: Ongoing campaign with hundreds of infected packages published to NPM registry

## Affected Systems and Products

- **Android Devices**: All versions affected by Framework vulnerabilities, requiring December 2025 security update
- **PyTorch Development Environment**: Systems using Picklescan utility for model security scanning
- **NPM Package Registry**: Hundreds of malicious packages affecting Node.js developers
- **Visual Studio Marketplace**: 24 malicious extensions impersonating popular developer tools
- **Open VSX Registry**: Compromised extensions targeting developers
- **IP Camera Systems**: Over 120,000 IP cameras hacked in Korea for illicit content distribution
- **Oracle E-Business Suite**: University of Pennsylvania servers compromised in August attack
- **Rust Crate Repository**: Malicious packages targeting Web3 developers across Windows, macOS, and Linux

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages distributed through legitimate software repositories (NPM, Visual Studio Marketplace, Rust Crates)
- **AI Security Evasion**: Hidden prompts and scripts designed to fool AI-powered security scanning tools
- **Social Engineering**: Fake Calendly invites impersonating major brands to steal Google Workspace and Facebook business credentials
- **Identity Rental Schemes**: North Korean operators recruiting legitimate developers to rent their identities for illicit activities
- **Memory-Only Execution**: Advanced backdoors operating entirely in memory to avoid detection
- **Cross-Platform Targeting**: Malware designed to operate across Windows, macOS, and Linux systems

## Threat Actor Activities

- **Lazarus APT (North Korea)**: Conducting sophisticated remote worker identity rental schemes to infiltrate organizations while funding state operations through IT work
- **MuddyWater (Iran)**: Deploying new MuddyViper backdoor with Fooder loader against Israeli entities across multiple sectors including academia, government, manufacturing, and utilities
- **GlassWorm Campaign**: Returning with 24 malicious Visual Studio extensions impersonating popular developer tools to compromise development environments
- **Tomiris Group (Russian-speaking)**: Targeting government and diplomatic entities in CIS member states and Central Asia using new Havoc framework tools
- **Inc Ransomware Gang**: Successfully attacked CodeRED Emergency Alert Platform, forcing shutdown and claiming theft of sensitive subscriber data
- **Korean IP Camera Hackers**: Four individuals arrested for hacking over 120,000 IP cameras and selling intimate footage to foreign adult sites