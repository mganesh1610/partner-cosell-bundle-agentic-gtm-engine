# Partner Go-To-Market (GTM) Architecture, Formulations & Power BI Scorecard Runbook

## 1. Multi-Vendor Co-Sell Bundle Definition & Value Proposition

This project models joint solution bundling across complementary enterprise software categories (pairing a **Cloud Infrastructure Platform** with an **Enterprise Zero-Trust Security & Compliance Suite** and **Digital Document Workflows**):

1. **Shared-Customer Cohorting (`sql/cosell_bundle_gtm_mart.sql`):**
   - Partitions `64,000` accounts into `Dual_Cloud_Security_Bundle` (`6,448` shared accounts), `Cloud_Platform_Only`, and `Security_Suite_Only` cohorts across `Web`, `Phone`, and `Multichannel` GTM channels (`27` reporting cohorts).
2. **Exact Newton-Raphson IRLS Propensity Model (`src/cosell_agentic_gtm_pipeline.py`):**
   - Fits L2-regularized logistic regression ($\lambda = 1.0$) on `51,200` training accounts and evaluates on `12,800` held-out accounts:
     $$\hat{p}_i = \sigma(\mathbf{x}_i^\top \hat{\boldsymbol{\beta}}), \quad \mathbf{H}^{(t)} = \mathbf{X}^\top \mathbf{W}^{(t)} \mathbf{X} + \lambda \mathbf{I}_{-0}$$
   - Achieves **`0.8495` holdout ROC-AUC**, **`0.0775` Brier score**, and **`2.75x` top-quintile lift** to prioritize single-vendor accounts ready for co-sell bundle attachment.
3. **Doubly Robust AIPW Co-Sell Incrementality:**
   - Combines propensity weighting $\hat{e}(X)$ with stratified outcome expectations $\hat{\mu}_1(X), \hat{\mu}_0(X)$:
     $$\hat{\tau}_{\text{AIPW}} = \frac{1}{N}\sum_{i=1}^N \left[ \hat{\mu}_1(X_i) - \hat{\mu}_0(X_i) + \frac{T_i (Y_i - \hat{\mu}_1(X_i))}{\hat{e}(X_i)} - \frac{(1 - T_i)(Y_i - \hat{\mu}_0(X_i))}{1 - \hat{e}(X_i)} \right]$$

---

## 2. 4-Node Agentic AI Sales-Floor Collateral Deployment Workflow

1. **`IntentPlaybookRouter`:** Sublinear word + character 4-gram TF-IDF multiclass linear router trained strictly on `10,003` training queries and evaluated on `3,080` held-out sales-floor queries (`91.40%` Top-1 / `98.02%` Top-2 accuracy across `6` GTM playbooks).
2. **`HybridCollateralRAG`:** Reciprocal Rank Fusion ($k = 60$) combining Okapi BM25 ($k_1 = 1.2, b = 0.75$) and sublinear TF-IDF cosine scoring across `36` governed battlecards, solution briefs, ROI calculators, and partner checklists.
3. **`BattlecardComposer`:** Emits structured sales-floor packets pairing bundle value propositions, approved TCO discount bands (`14.5%–18.5%`), and verifiable collateral IDs (`COL-001`..`COL-036`).
4. **`AccuracyAndTimelinessGate`:** Deterministic release gate enforcing `verified_pricing == True`, `freshness_days <= 30`, and valid `COL-` citation provenance before surfacing collaterals to field sales reps.

---

## 3. Governed Power BI `DAX` Measures for Executive GTM Reporting

```dax
Co-Sell Conversion Rate % =
DIVIDE(
    SUM('bundle_segment_gtm_scorecard'[converted_deals]),
    SUM('bundle_segment_gtm_scorecard'[accounts_targeted]),
    0
)

Dual-Bundle Pipeline Revenue =
CALCULATE(
    SUM('bundle_segment_gtm_scorecard'[total_pipeline_revenue]),
    'bundle_segment_gtm_scorecard'[bundle_posture] = "Dual_Cloud_Security_Bundle"
)
```
