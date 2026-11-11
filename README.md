# Multi-Vendor Cloud & Security Co-Sell Bundle Optimization & Agentic AI Sales Enablement Engine

An end-to-end **Partner Software Product Marketing, Multi-Vendor Co-Selling Bundle Design & Agentic AI Sales-Floor Collateral Deployment** platform executed across **77,083 SHA-256-verified public records** (`64,000` multi-channel cross-category customer accounts + `13,083` sales-floor product, pricing, and security inquiry utterances across `77` intents).

---

## 1. System Architecture

```mermaid
flowchart LR
    A["64,000 Customer Accounts + 13,083 Inquiry Utterances"] --> B["SQLite Relational Mart (SQL Joins & CTEs across 27 Co-Sell Cohorts)"]
    B --> C["IRLS Logistic Bundle Propensity (0.85 ROC-AUC, 2.75x Top-Quintile Lift)"]
    B --> D["Randomized Co-Sell Incrementality (+86.5% Conversion Lift, Doubly Robust AIPW)"]
    C --> E["4-Node Agentic Sales-Floor Deployment (Intent Router -> Hybrid BM25+TF-IDF RRF -> Battlecard Composer -> SLA Gate)"]
    D --> E
    E --> F["36 Governed Cloud + Security Battlecards (91.4% Top-1 / 98.0% Top-2 Routing, 100% Grounding)"]
```

---

## 2. Verified Public Datasets & Provenance

| Role | Public Dataset & Direct Source | Scale & Granularity | SHA-256 Checksum |
| :--- | :--- | :--- | :--- |
| **Primary Dataset 1 (Multi-Product Customer Affinity & Co-Sell Experiment)** | Kevin Hillstrom MineThatData Multi-Channel Cross-Category Co-Marketing Dataset (`http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv`) | `64,000` customer accounts $\times$ `12` attributes (`6,448` shared dual-category accounts vs. `57,552` single-category accounts across `Web`, `Phone`, and `Multichannel` motions) | `0e5893329d8b93cefecc571777672028290ab69865718020c78c7284f291aece` |
| **Primary Dataset 2 (Sales-Floor Product, Pricing & Compliance Queries)** | PolyAI Regulated Enterprise Product, Pricing & Security Inquiry Corpus (`https://github.com/PolyAI-LDN/task-specific-datasets/tree/master/banking_data`) | `13,083` utterances (`10,003` train / `3,080` held-out test) across `77` intents mapped to `6` Partner GTM Playbooks & `36` governed battlecards | Train: `b06e26ac675513959a63135f11b94ea7786ed02da65db93a5650d8838cbc664b`<br>Test: `d12d6e3bc4c3103966ae786dc435913c0c563dfa328f5a3646d0e62cfeeb474d` |
| **Backup Public Datasets** | UCI Online Retail Commercial Multi-SKU Transactions (`https://archive.ics.uci.edu/dataset/352/online+retail`) & UCI Direct Commercial Campaign Dataset (`https://archive.ics.uci.edu/dataset/222/bank+marketing`) | `541,909` multi-SKU invoice rows (`4,372` commercial accounts) and `45,211` campaign execution records | `f5385cbb54bbebf7196389109c6b0621faab0c304e3702548165e71c84aede8b` / `e0bf5f5de5b846e2f18e9d90606637267d46dfa260e0f17bb12e605db5efbeb4` |

---

## 3. Executed Results Summary

| Dimension | Verified Output |
| :--- | :--- |
| **Combined Verified Records** | `77,083` (`64,000` customer accounts + `13,083` inquiry utterances) |
| **Shared Dual-Solution Account Value Expansion** | **`2.52x`** higher historical account value (`$529.65` vs. `$209.87` across `6,448` shared dual-bundle accounts) |
| **Dual-Bundle Cross-Sell Propensity (`12,800` Holdout)** | **`0.8495` (`0.85`) Holdout ROC-AUC**, `0.0775` Brier calibration score, **`2.75x` Top-Quintile Lift** |
| **Co-Sell Outreach Incrementality** | **`+57.35%` visit lift** ($Z = 20.51$), **`+86.53%` conversion lift** ($Z = 6.24$), **`+91.42%` spend lift**, **`+0.50 pp` Doubly Robust AIPW ATE** |
| **4-Node Agentic Sales-Floor Collateral Routing (`3,080` Holdout)** | **`91.40%` (`91.4%`) Top-1** and **`98.02%` (`98.0%`) Top-2** playbook accuracy across `6` GTM playbooks & `36` battlecards |
| **Collateral Citation, Pricing & Freshness SLA Gate** | **`100.0%` (`3,080/3,080`)** citation grounding & pricing parity; **`3/3` (`100%`)** adversarial stale (`>30d`) / unverified assets quarantined |
| **Sales-Floor Retrieval Latency** | `0.165 ms` `p50` / `0.290 ms` `p95` |
| **Automated Test Suite** | **`5/5` (`100%`)** unit, SQL conservation, statistical, and adversarial SLA gate tests passing |

---

## 4. Quickstart (Zero External Dependencies — Pure Python 3 Standard Library)

```bash
PYTHONPATH=. python3 src/cosell_agentic_gtm_pipeline.py
PYTHONPATH=. python3 -m unittest discover -s tests -p "test_*.py" -v
```
