# Source influences

This repository-owned method implements Tobi's requested technical decision
discipline. It is not a renamed copy of Matt Pocock's Codebase Design or a claim
that one language, framework or set of ten rules is universally best.

Reviewed influences on 2026-11-04 include:

- The former global Engineering profile, archived in this repository on 2026-09-10,
  especially its architecture/patterns and current-primary-source requirements.
- SEI's architecture trade-off reasoning:
  https://sei.cmu.edu/library/steps-in-an-architecture-tradeoff-analysis-method-quality-attribute-models-and-analysis/
- John Ousterhout's stated design concerns and book background:
  https://web.stanford.edu/~ouster/cgi-bin/book.php
- Dan McKinley's organizational-cost heuristic, treated as practitioner experience:
  https://mcfunley.com/choose-boring-technology
- Architecture trade-offs rather than universal distributed-system prescriptions:
  https://martinfowler.com/articles/microservice-trade-offs.html
- Contextual pattern selection:
  https://learn.microsoft.com/en-us/azure/architecture/patterns/
- Operational reliability and systematic performance investigation:
  https://sre.google/sre-book/ and https://www.brendangregg.com/usemethod.html

Configuration and operating-lifecycle influences reviewed on 2026-11-05:

- [Twelve-Factor Config](https://www.12factor.net/config) distinguishes deployment
  settings from internal program wiring. Its environment-variable prescription is
  context-specific, not this skill's universal storage rule.
- [Spring Boot externalized configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html)
  illustrates supported sources, precedence and validation. These are questions
  to resolve in the actual ecosystem, not a required framework or config stack.
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
  informs access and credential lifecycle; [Google's ADC documentation](https://docs.cloud.google.com/docs/authentication/application-default-credentials)
  illustrates identity binding versus key material. Platform-specific mechanisms
  and warnings require checking against the actual deployment.
- Docker's [build-secret guidance](https://docs.docker.com/build/building/secrets/)
  and [volume lifecycle](https://docs.docker.com/engine/storage/volumes/) illustrate
  build/runtime access and persistence boundaries; they do not mandate containers.
- PostgreSQL's [export scope](https://www.postgresql.org/docs/current/app-pgdump.html)
  and AWS's [recovery testing guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/test.html)
  inform the distinction between backup output and demonstrated recovery. A dump
  command or provider-specific procedure is not a universal recovery plan.
- GitHub's [deployment boundaries](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
  and [artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations)
  illustrate scoped release access and origin evidence. Provenance does not prove
  artifact safety or the live outcome; no CI vendor or attestation system is required.

These links record inspected influences, not a mandatory live reading list or
current technology catalogue. State of the Art owns fresh discovery and evidence.
The ten initial practices are original synthesis; the actual choice must be
supported by the task's constraints and current sources. No source was copied
as a complete manual, and no current product version is frozen into this skill.
