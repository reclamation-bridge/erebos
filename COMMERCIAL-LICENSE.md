# Commercial License for erebos

**Last Updated:** November 22, 2026 (v2.0, replaces v1.0 of March 9, 2026, which was
never in effect for any release)

---

## Overview

Erebos is dual-licensed:

- **Open Source:** Available under the GNU Affero General Public License v3.0 (AGPL-3.0) for
  individuals, open source projects, and AGPL-compatible use
- **Commercial:** Available under a proprietary license for organizations that cannot or prefer
  not to use AGPL-3.0

This document describes the commercial licensing option.

---

## What is AGPL-3.0 and Why Does It Matter?

The GNU Affero General Public License v3.0 (AGPL-3.0) is a "copyleft" license. It works like the
GPL-3.0, with one addition for software used over a network:

1. **Derivative works must also be AGPL-3.0.** If you modify Erebos and distribute your changes,
   you must release those changes under AGPL-3.0.
2. **Combined works must be AGPL-3.0.** If you distribute a larger application that incorporates
   Erebos, the whole application must be licensed under AGPL-3.0.
3. **Source code must be made available** to anyone you distribute the software to.
4. **The network clause:** if you modify Erebos and let people use it over a network (for
   example, as a hosted service), you must offer those users the complete source code of your
   modified version. Under plain GPL-3.0, hosting without distributing triggered no obligation;
   under AGPL-3.0 it does.

**For many organizations, this is incompatible with proprietary software development or hosted
offerings.**

---

## When You Need a Commercial License

You need a commercial license if:

- ✅ You're building a **proprietary product** that integrates Erebos
- ✅ You're creating a **closed-source tool** that includes Erebos and is distributed or offered
  to users outside your organization
- ✅ You want to **modify Erebos** without releasing your changes as open source
- ✅ Your organization's **legal policy prohibits AGPL-licensed dependencies**
- ✅ You're offering a **SaaS or hosted service** built on a modified Erebos without publishing
  your modified source to its users
- ✅ You want to **resell or redistribute** Erebos as part of a commercial offering
- ✅ You're distributing **Slate**, or a product built on Slate, without meeting AGPL-3.0
  (Slate ships with the Erebos core; see "Slate" below)

You **do NOT need a commercial license** if:

- ❌ You're using Erebos for personal use
- ❌ You're contributing to open source projects (AGPL-compatible)
- ❌ You're using Erebos unmodified, or you're comfortable publishing your modifications under
  AGPL-3.0
- ❌ Your organization can comply with AGPL-3.0 requirements

---

## What the Commercial License Provides

A commercial license grants you:

1. **Freedom from AGPL copyleft:** no requirement to release your derivative works, combined
   applications, or hosted modifications as open source
2. **Proprietary use rights:** build closed-source products and services incorporating Erebos
3. **Modification rights:** modify the code without sharing changes publicly
4. **Redistribution rights:** include Erebos in commercial products or services
5. **Patent protection:** same patent grant as AGPL-3.0, protecting you from patent claims
6. **Support and updates:** access to priority support and commercial release branches
   (optional tier)

---

## License Tiers

### Tier 1: Single Developer License

**$500 USD per year**

- **Use:** One developer working with Erebos
- **Products:** Unlimited proprietary products or services
- **Support:** Email support (best-effort, 3-5 business day response)
- **Updates:** Access to all releases during license period

### Tier 2: Team License (5 developers)

**$2,000 USD per year**

- **Use:** Up to 5 developers working with Erebos
- **Products:** Unlimited proprietary products or services
- **Support:** Email support (priority, 1-2 business day response)
- **Updates:** Access to all releases during license period
- **Support calls:** 2 hours per year of 1:1 technical consultation

### Tier 3: Organization License (Unlimited developers)

**$5,000 USD per year**

- **Use:** Unlimited developers within your organization
- **Products:** Unlimited proprietary products or services
- **Support:** Email support (priority, 1 business day response)
- **Updates:** Access to all releases during license period
- **Support calls:** 6 hours per year of technical consultation
- **Custom features:** Influence roadmap, request features

### Enterprise / Custom Arrangements

For organizations with specific needs:

- Multi-year agreements (discounted rates)
- Custom feature development
- Dedicated support channels
- On-premise deployment assistance (including self-hosted deployments in regulated
  environments; regulatory compliance of your deployment remains your responsibility)
- Training and onboarding

**Contact for pricing:** Based on requirements and scale

---

## Slate

Slate is the simplified, non-technical edition built on the Erebos core.

- **Slate's own interface code** is licensed under the BSD 3-Clause license and can be reused
  freely on its own.
- **The Erebos core that Slate runs on** is covered by this dual license (AGPL-3.0 or
  commercial).
- **Distributing Slate as a complete application** therefore means meeting AGPL-3.0 for the
  whole, or holding an Erebos commercial license, which covers the Erebos core as used in Slate.

---

## How to Purchase

1. **Email:** [tallest@uncletallest-productions.org](mailto:tallest@uncletallest-productions.org)
2. **Subject:** "Commercial License Request - Erebos"
3. **Include:**
   - Organization name
   - Number of developers
   - Intended use case (including whether it involves Slate or a hosted service)
   - Tier preference (or request custom quote)

You will receive:

- License agreement document
- Payment instructions
- License certificate upon payment

**Payment methods:** PayPal, bank transfer, check (USD only)

---

## License Agreement Terms

### Grant of Rights

Upon payment, you receive a non-exclusive, worldwide, royalty-free license to:

- Use Erebos in proprietary applications and services
- Modify the source code for your purposes
- Distribute modified or unmodified versions as part of your products
- Create derivative works without AGPL obligations

### Restrictions

You may NOT:

- Relicense Erebos under a different license
- Remove copyright notices or attribution
- Use the Erebos or Slate names or trademarks without permission
- Hold the author liable for damages (software provided "AS IS")

### Term and Renewal

- **Duration:** One year from purchase date
- **Renewal:** Optional annual renewal at current rates
- **Perpetual use:** Code licensed during active period remains licensed perpetually
- **Updates:** Requires active license

### Termination

License terminates if:

- Payment is not received
- You violate license terms
- You choose not to renew (perpetual rights to licensed version remain)

---

## Frequently Asked Questions

**Q: Can I try before buying?**
A: Yes. Use the AGPL-3.0 version for evaluation. If you decide to build a proprietary product or
hosted service, purchase a commercial license before deployment.

**Q: Do I need a license for development/testing?**
A: No. You can develop and test under AGPL-3.0. Purchase a commercial license before you
distribute a proprietary product or put a modified version in front of users over a network.

**Q: What if I'm a solo indie developer?**
A: If you're comfortable with AGPL-3.0 (open sourcing your product), use the free version. If
you want to build a proprietary product, the Single Developer License ($500/year) is your option.

**Q: I host Erebos internally for my own team. Does the network clause apply?**
A: If you run it unmodified, no source obligation arises. If you modify it and users interact
with it over a network, AGPL-3.0 requires offering those users your modified source, unless you
hold a commercial license.

**Q: Can I get a discount for non-profits or educational institutions?**
A: Contact us. We offer case-by-case consideration for non-profits, educational institutions,
and open source organizations with valid use cases.

**Q: What happens if I stop paying after the first year?**
A: You retain rights to the version(s) licensed during your active period. You lose access to
new updates and support.

**Q: Can I switch from AGPL to commercial mid-project?**
A: Yes. Purchase before your next distribution or deployment. Anything you already distributed
under AGPL-3.0 stays available to its recipients under AGPL-3.0; from the purchase on, your
releases can be under the commercial terms.

**Q: Is support guaranteed?**
A: Best-effort support is included. Response times are targets, not guarantees. For guaranteed
SLA support, contact us for custom enterprise terms.

---

## Why Dual Licensing?

**For users:** Free open source software for individuals and AGPL-compatible projects.

**For businesses:** Option to build proprietary products and services without AGPL restrictions.

**For the project:** Sustainable funding to continue development, pay for infrastructure, and
support the community.

**For the author:** Ability to work on this full-time if commercial adoption reaches that scale.

---

## Open Source Commitment

Regardless of commercial licensing:

- The core project remains open source under AGPL-3.0
- All releases are published publicly
- Community contributions are welcomed and credited. Contributors sign a short
  [Contributor License Agreement](CLA.md) so their work can be offered under both licenses,
  and the maintainer commits that accepted contributions always stay available as open source
- AGPL-3.0 users receive the same features as commercial users
- No "commercial-only" features (support and legal terms differ, not functionality)

Commercial licensing supports development of features that benefit everyone.

---

## Contact

**Questions about commercial licensing:**
Email: [tallest@uncletallest-productions.org](mailto:tallest@uncletallest-productions.org)

**Questions about the open source version:**
Use [GitHub Discussions](https://github.com/reclamation-bridge/erebos/discussions)

**Bug reports and feature requests:**
Use [GitHub Issues](https://github.com/reclamation-bridge/erebos/issues)

---

## Legal

This commercial license is offered by:

**Jerry Jackson (Uncle Tallest)**
Uncle Tallest Productions
Austin, Texas, USA

The software is provided "AS IS" without warranty of any kind. The author is not liable for
damages arising from use of the software. See LICENSE file for AGPL-3.0 terms.

---

**Version:** 2.0
**Effective:** November 22, 2026
**Author:** Jerry Jackson
**Repository:** https://github.com/reclamation-bridge/erebos
