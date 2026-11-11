-- Multi-Vendor Co-Sell Bundle Cohorting & Channel Funnel Attribution (SQL Joins & CTEs)
WITH account_bundle_profile AS (
    SELECT
        a.account_id,
        a.recency_months,
        a.history_band,
        a.history_spend,
        a.platform_adopted,
        a.security_adopted,
        CASE
            WHEN a.platform_adopted = 1 AND a.security_adopted = 1 THEN 'Dual_Cloud_Security_Bundle'
            WHEN a.platform_adopted = 1 AND a.security_adopted = 0 THEN 'Cloud_Platform_Only'
            ELSE 'Security_Suite_Only'
        END AS bundle_posture,
        a.channel,
        a.zip_region,
        a.newbie_flag
    FROM dim_shared_accounts a
),
campaign_outcomes AS (
    SELECT
        p.bundle_posture,
        p.channel,
        c.campaign_arm,
        COUNT(*) AS accounts_targeted,
        SUM(c.visited) AS engaged_accounts,
        SUM(c.converted) AS converted_deals,
        ROUND(AVG(c.visited) * 100.0, 4) AS visit_rate_pct,
        ROUND(AVG(c.converted) * 100.0, 4) AS conversion_rate_pct,
        ROUND(SUM(c.realized_spend), 2) AS total_pipeline_revenue,
        ROUND(AVG(p.history_spend), 2) AS avg_prior_arr
    FROM account_bundle_profile p
    INNER JOIN fct_cosell_campaign_arms c
        ON p.account_id = c.account_id
    GROUP BY p.bundle_posture, p.channel, c.campaign_arm
)
SELECT
    bundle_posture,
    channel,
    campaign_arm,
    accounts_targeted,
    engaged_accounts,
    converted_deals,
    visit_rate_pct,
    conversion_rate_pct,
    total_pipeline_revenue,
    avg_prior_arr
FROM campaign_outcomes
ORDER BY bundle_posture, channel, campaign_arm;
