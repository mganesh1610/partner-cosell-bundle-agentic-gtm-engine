#!/usr/bin/env python3
"""Automated unit, SQL reconciliation, statistical, and adversarial governance tests."""
import json
import unittest

from src.cosell_agentic_gtm_pipeline import (
    OUTPUT_DIR,
    build_governed_collateral_kb,
    map_intent_to_cosell_playbook,
    run_pipeline,
    verify_collateral_gate,
)


class TestCoSellAgenticGTMEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summary = run_pipeline()

    def test_public_dataset_scale_and_conservation(self) -> None:
        self.assertEqual(self.summary["hillstrom_accounts"], 64000)
        self.assertEqual(self.summary["sales_floor_utterances_total"], 13083)
        self.assertEqual(self.summary["combined_public_records"], 77083)
        self.assertEqual(
            self.summary["shared_dual_solution_accounts"] + self.summary["single_solution_accounts"],
            64000,
        )

    def test_bundle_expansion_and_cosell_incrementality(self) -> None:
        self.assertGreater(self.summary["dual_vs_single_arr_expansion_x"], 1.8)
        self.assertGreater(self.summary["cosell_visit_lift_pct"], 50.0)
        self.assertGreater(self.summary["cosell_conversion_lift_pct"], 55.0)
        self.assertGreater(self.summary["cosell_conversion_z_stat"], 4.5)
        self.assertGreater(self.summary["doubly_robust_aipw_ate_pp"], 0.30)
        self.assertGreater(self.summary["bundle_engagement_holdout_roc_auc"], 0.80)

    def test_agentic_sales_floor_routing_and_grounding(self) -> None:
        self.assertEqual(self.summary["governed_collaterals_count"], 36)
        self.assertEqual(self.summary["gtm_playbooks_count"], 6)
        self.assertGreaterEqual(self.summary["playbook_top1_accuracy_pct"], 88.0)
        self.assertGreaterEqual(self.summary["playbook_top2_accuracy_pct"], 96.0)
        self.assertEqual(self.summary["collateral_citation_grounding_pct"], 100.0)
        self.assertEqual(self.summary["adversarial_stale_or_unverified_blocked"], "3/3")

    def test_collateral_sla_and_pricing_gates(self) -> None:
        kb = build_governed_collateral_kb()
        self.assertEqual(len(kb), 36)
        for asset in kb:
            ok, code = verify_collateral_gate(asset)
            self.assertTrue(ok, code)
        ok_stale, code_stale = verify_collateral_gate(
            {"collateral_id": "COL-999", "freshness_days": 31, "sla_max_days": 30, "verified_pricing": True}
        )
        self.assertFalse(ok_stale)
        self.assertEqual(code_stale, "QUARANTINED_STALE_ASSET_SLA")

    def test_exported_artifacts_exist(self) -> None:
        self.assertTrue((OUTPUT_DIR / "cosell_agentic_validation_summary.json").is_file())
        self.assertTrue((OUTPUT_DIR / "bundle_segment_gtm_scorecard.csv").is_file())
        self.assertTrue((OUTPUT_DIR / "agentic_playbook_routing_audit.csv").is_file())
        loaded = json.loads((OUTPUT_DIR / "cosell_agentic_validation_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(loaded["sqlite_mart_cohort_rows"], 27)
        self.assertEqual(
            map_intent_to_cosell_playbook("compromised_card"),
            "Security_ZeroTrust_Compliance_Playbook",
        )


if __name__ == "__main__":
    unittest.main()
