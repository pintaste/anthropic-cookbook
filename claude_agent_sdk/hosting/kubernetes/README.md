# Tier 3 — Kubernetes

> **Coming in a follow-up PR.** This tier is owned by a separate contributor.
> It deploys the same `hosting/Dockerfile` image behind a gateway with
> pod-per-session routing, a standby pool, and egress lockdown — conforming to
> the same [interface contract](../README.md#interface-contract) as tiers 1 and 2.
>
> See §8 of [`07_Hosting_the_agent.ipynb`](../../07_Hosting_the_agent.ipynb)
> for the architecture walkthrough in the meantime.
