# Major Events and Global Markets: a cross-country, cross-industry event study

How do major macro shocks reprice stocks across industries and across
countries? This study applies the event-study method (CAPM market model,
abnormal and cumulative abnormal returns) to **11 industries** under **5 major
events**, comparing the UK, US, and Chinese markets.

**Course:** Event study project, School of Economics and Management, Tsinghua
University, December 2024. **Advisor:** Prof. Sun Jing.
**Authors:** Zhu Hongyi, Marco Ortiz Togashi.

## The design

**Five events** (event date used as day 0):

| Event | Date |
|---|---|
| Global Financial Crisis (Lehman) | 2008-09-15 |
| Brexit Referendum | 2016-06-23 |
| Covid-19 lockdown in China | 2020-01-23 |
| Russia-Ukraine war | 2022-02-24 |
| Trump re-election | 2024-11-06 |

**Eleven industries:** Agriculture & Food, Automotive, Defense & Aerospace,
Energy & Utilities, Finance & Insurance, Healthcare & Pharmaceuticals,
Manufacturing & Industrial Goods, Real Estate & Construction, Retail &
Consumer Goods, Technology & Telecommunications, Transportation &
Infrastructure.

For each industry-event cell, an industry return series is regressed on its
market index over a pre-event estimation window to fit a CAPM market model.
Expected returns are projected into a 30-day event window, the abnormal return
is actual minus expected, and abnormal returns accumulate into a CAR path. OLS
summaries (alpha, beta, R-squared, p-value) quantify each fit, and abnormal
returns are compared across industries per event.

## Findings

Industries diverge sharply in their sensitivity to events. Defense &
aerospace, technology, and healthcare behaved as **safe havens** during
geopolitical conflict and the public-health shock, while energy and
manufacturing were **pressured** through supply-chain disruption and demand
swings. The study reads these differences through policy-transmission,
market-efficiency, and industry-vulnerability lenses, with cross-industry
comparison per event (see `figures/`).

The market-model **betas** (from `results/ols_summary.csv`, built out of the
55 per-cell OLS fits) quantify the same structure and are remarkably stable
across all five events: defensive industries sit well below 1, cyclical ones
well above.

| Industry | Brexit | Covid CN | Trump 24 | GFC 08 | RU war |
|---|---|---|---|---|---|
| Agriculture and Food | 0.75 | 0.74 | 0.91 | 0.73 | 0.82 |
| Automotive | 1.09 | 1.10 | 1.19 | 1.13 | 1.31 |
| Defense and Aerospace | 1.03 | 1.09 | 1.22 | 0.94 | 0.91 |
| Energy and Utilities | 0.94 | 0.98 | 1.04 | 0.81 | 0.83 |
| Finance and Insurance | 1.30 | 1.33 | 1.21 | 1.37 | 1.39 |
| Healthcare and Pharmaceuticals | 0.76 | 0.72 | 0.96 | 0.72 | 0.83 |
| Manufacturing and Industrial Goods | 1.15 | 1.11 | 1.30 | 1.09 | 1.15 |
| Real Estate and Construction | 1.07 | 1.10 | 1.11 | 1.00 | 1.19 |
| Retail and Consumer Goods | 0.86 | 0.85 | 1.14 | 0.80 | 0.99 |
| Technology and Telecommunications | 0.84 | 0.82 | 0.92 | 0.84 | 0.89 |
| Transportation and Infrastructure | 1.43 | 1.47 | 1.07 | 1.24 | 1.31 |

Two readings worth calling out: finance carries the highest beta in almost
every event (leverage amplifies shocks regardless of their nature), and
defense & aerospace swings from cyclical under Trump's re-election (1.22) to
defensive during the actual wars and crises (0.91-0.94), which is the
safe-haven rotation in a single number.

## Repository layout

```
src/                     analysis pipeline (run in this order)
  split_by_events.py                 split combined returns into per-event files
  expected_return_calculation.py     CAPM expected returns per industry-event
  ar_calculation.py                  abnormal return = industry - expected
  event_analysis_expected_return.py  expected-return event-study step
  event_analysis_ar_car.py           AR / CAR construction and plots
  event_analysis_ols.py              market-model OLS per industry-event
results/
  ols/                   55 OLS summaries (11 industries x 5 events): alpha, beta, R^2, p
  ols_summary.csv        the 55 cells combined into one table (industry, event, alpha, beta, ...)
  expected_returns/      55 expected-return series (CAPM projections)
  abnormal_returns/      55 abnormal-return series (industry, market, expected, AR)
  ar_car_results.csv     per-company CAR over each event window
  industry_averages.csv, industry_30day_averages.csv,
  industry_event_30day_returns_cleaned.csv   aggregated industry return panels
figures/                 5 cross-industry AR comparison plots (one per event)
```

## Reproduce

```bash
pip install -r requirements.txt
# All scripts read their inputs from a configurable data root:
#   default   <repo>/data          (create it and drop the raw folders there)
#   override  EVENT_STUDY_DATA=/path/to/data python src/event_analysis_ols.py
# The data root must hold the raw folders the pipeline expects
# (OLS/, "UK Result/", Event_Analysis_Output/, Split_By_Industry/, ...).
# The scripts run in the order listed above.
```

## Data

Stock and index prices were pulled from Yahoo Finance for the UK, US, and
Chinese markets. **Raw price data is not committed** (Yahoo Finance data is
not redistributable): only derived series and statistics are stored here, the
CAPM expected returns, the abnormal-return series, the OLS summaries, the
aggregated industry return panels, and the comparison figures. None of the
committed CSVs contain raw OHLC quotes; they hold return series (percentage
changes) and regression outputs only.

## Notes and limitations

- The original scripts carried hard-coded absolute paths from the author's
  machine; these have been replaced by a configurable `DATA_ROOT`
  (`EVENT_STUDY_DATA` env var, default `<repo>/data`) with the analysis logic
  untouched.
- `Event Analysis.py` from the original working folder is **not** part of this
  project (it is an unrelated app-comparison script that happened to share the
  name) and is intentionally excluded.
- Estimation and event windows are short, so single-cell significance should
  be read alongside the cross-industry comparison rather than in isolation.

## Report

The full written report (Chinese, with English abstract) is included at
[`report/Event_Study_Report.pdf`](report/Event_Study_Report.pdf).

## License

Code is released under the MIT License (see `LICENSE`). The written report
remains the intellectual work of the two authors, Zhu Hongyi and Marco Ortiz
Togashi.
