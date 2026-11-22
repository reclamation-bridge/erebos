# How Slate is licensed

Slate is the simplified, non-technical edition of erebos. It has two parts, licensed
differently:

| Part | What it is | License |
| --- | --- | --- |
| **Slate's interface** | This repository: Slate's own UI, layouts, wording, and the code that makes erebos simpler to use | [BSD 3-Clause](LICENSE) |
| **The erebos core** | The engine Slate runs on, pulled in as a dependency, not copied into this repo | [GNU AGPL v3.0](https://github.com/reclamation-bridge/erebos/blob/main/LICENSE) **or** the [erebos commercial license](https://github.com/reclamation-bridge/erebos/blob/main/COMMERCIAL-LICENSE.md) |

## What this means in practice

- **Using Slate yourself:** nothing to do. It's free.
- **Reusing Slate's interface code on its own** (in your own project, without the erebos core):
  BSD 3-Clause applies. Keep the copyright notice; that's it.
- **Distributing Slate as a complete application** (interface + erebos core), or offering a
  modified Slate to users over a network: the combined work must meet **AGPL-3.0**, because the
  erebos core is AGPL. If you can't or don't want to, an **erebos commercial license** covers the
  erebos core as used in Slate.

## Contributing

- Contributions to **this repository** are accepted under BSD 3-Clause (the same license they
  come in under is the license they go out under). No CLA is needed here.
- Changes to the **erebos core** belong in the erebos repository, where contributors sign the
  [erebos CLA](https://github.com/reclamation-bridge/erebos/blob/main/CLA.md).
- Don't copy erebos source files into this repository. Import the core as a dependency, so the
  BSD and AGPL parts stay cleanly separated.

## Questions

Commercial licensing: [tallest@uncletallest-productions.org](mailto:tallest@uncletallest-productions.org)
