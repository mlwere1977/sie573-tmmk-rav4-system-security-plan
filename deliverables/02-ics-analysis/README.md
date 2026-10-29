# Milestone 2: Industrial Control System Analysis (Week 3)

📄 [`ICS_Analysis_Team_5.pdf`](ICS_Analysis_Team_5.pdf)

A research paper analyzing TMMK's ICS/OT environment as the foundation for the risk assessment.

**Sections**
- **Architecture & system monitoring:** Purdue-model segmentation (Enterprise IT → OT DMZ → Ops → Control → Floor VLAN), read against NIST SP 800-82r2 principles: segmentation, segregation, DMZ boundary protection, defense in depth.
- **Cyber and physical security in automotive OT:** identifies the R&D → plant software handoff as the critical weak point. Nothing verifies that the package on the encrypted drive is unchanged on arrival, and the same drives also feed the OT DMZ cluster. One compromised transfer could reach both the vehicle and the ICS that builds it.
- **Historical threats:** 2022 Kojima Industries ransomware (14 plants, ~13,000 vehicles), Stuxnet PLC logic manipulation, the RAV4 headlight CAN bus injection (CVE-2023-29389), and the Toyota cloud misconfiguration leak (2012–2023).
- **Evolution of ICS/OT security:** from "security by obscurity" and air gaps, to defense in depth, to resiliency engineering that assumes breach (SP 800-160 Vol. 2, SP 800-161).

**Key insight carried forward:** availability-first OT design plus IT/OT convergence makes the factory floor *"the definitive root of trust for consumer safety."*
