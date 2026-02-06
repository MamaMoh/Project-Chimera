from orchestrator.orchestrator_service import OrchestratorService


def main() -> None:
    orchestrator = OrchestratorService()
    decision = orchestrator.run_once("Generate a short welcome post.")
    print(f"Decision: {decision.decision} ({decision.rationale})")


if __name__ == "__main__":
    main()
