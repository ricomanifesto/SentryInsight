# Exploitation Report

# Comprehensive Exploitation Report - May 2025

## Summary of Critical Exploitation Activity

This report provides an overview of the most critical vulnerabilities actively exploited as of May 2025. It includes zero-day vulnerabilities, recently patched vulnerabilities that were exploited in the wild, and new attack vectors and techniques. The report also highlights notable threat actors and their activities.

## Exploited Vulnerabilities

### Zero-Day Vulnerabilities

1. **CVE-2025-32756** - Fortinet FortiVoice Systems
   - **Description**: A critical remote code execution (RCE) vulnerability exploited as a zero-day.
   - **Impact**: Allows attackers to execute arbitrary code on vulnerable systems.
   - **Affected Systems**: FortiVoice enterprise phone systems.
   - **Mitigation**: Apply the latest security updates released by Fortinet.

2. **CVE-2025-31324** - SAP NetWeaver
   - **Description**: A critical security flaw exploited by China-linked APTs to breach critical systems.
   - **Impact**: Compromise of critical infrastructure networks.
   - **Affected Systems**: SAP NetWeaver servers.
   - **Mitigation**: Implement SAP's security patches immediately.

3. **Windows Zero-Day Bug** - Browser-Led RCE
   - **Description**: A zero-day vulnerability in Windows exploited for remote code execution via browsers.
   - **Impact**: Allows attackers to execute code remotely through browser interactions.
   - **Affected Systems**: Windows operating systems.
   - **Mitigation**: Apply the latest Microsoft security updates.

### Recently Patched Vulnerabilities

1. **Azure DevOps Server CVSS 10 Bug**
   - **Description**: A critical vulnerability with a CVSS score of 10 impacting Azure DevOps Server.
   - **Impact**: Potential for complete system compromise.
   - **Affected Systems**: Azure DevOps Server.
   - **Mitigation**: Apply the security patches provided by Microsoft.

2. **Ivanti EPMM Vulnerabilities**
   - **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) exploited for remote code execution.
   - **Impact**: Allows attackers to execute code remotely.
   - **Affected Systems**: Ivanti EPMM software.
   - **Mitigation**: Update to the latest version as per Ivanti's advisories.

3. **SAP Zero-Day Flaw**
   - **Description**: A second zero-day vulnerability in SAP NetWeaver exploited in recent attacks.
   - **Impact**: Compromise of SAP systems.
   - **Affected Systems**: SAP NetWeaver servers.
   - **Mitigation**: Apply SAP's security updates.

### New Attack Vectors and Techniques

- **Earth Ammit Campaigns**: Targeting drone supply chains via ERP systems in Taiwan and South Korea, indicating a focus on military and satellite sectors.
- **Horabot Malware**: Distributed through invoice-themed phishing emails targeting Windows users in Latin America.

### Notable Threat Actors

- **Earth Ammit**: Engaged in cyber espionage targeting military and satellite sectors.
- **China-Linked APTs**: Exploiting SAP vulnerabilities to target critical infrastructure.
- **Konni (Opal Sleet, TA406)**: North Korean group targeting Ukrainian government entities for intelligence collection.

## Recommendations for Mitigation

1. **Patch Management**: Ensure all systems are updated with the latest security patches, especially for critical vulnerabilities in Microsoft, Fortinet, SAP, and Ivanti products.
2. **Network Segmentation**: Implement network segmentation to limit the spread of attacks within an organization.
3. **Phishing Awareness**: Conduct regular training for employees to recognize and report phishing attempts.
4. **Endpoint Protection**: Deploy advanced endpoint protection solutions to detect and mitigate malware threats like Horabot.
5. **Zero-Trust Architecture**: Adopt a zero-trust security model to enhance defenses against unauthorized access.

By addressing these vulnerabilities and following the recommended mitigation strategies, organizations can significantly reduce their risk of exploitation and enhance their overall security posture.

## Active Exploitation Details



## Affected Systems and Products



## Attack Vectors and Techniques



## Threat Actor Activities

 